#!/usr/bin/env python3

BOUND = 4096

EXPECTED_PERIODIC = {
    36: (36,),
    64: (64, 72),
    72: (72, 64),
    144: (144,),
    288: (288,),
    1152: (1152,),
}

EXPECTED_TERNARY = {
    36: "1100",
    64: "2101",
    72: "2200",
    144: "12100",
    288: "101200",
    1152: "1120200",
    4096: "12121201",
    10368: "112020000",
    4608: "20022200",
}

def ternary(n):
    if n == 0:
        return "0"
    ds = []
    while n:
        ds.append(str(n % 3))
        n //= 3
    return "".join(reversed(ds))

def shifted_product(n):
    assert n > 0
    product = 1
    while n:
        d = n % 3
        product *= d + 2
        n //= 3
    return product

def orbit_cycle(start):
    seen = {}
    orbit = []
    n = start
    max_value = n
    while n not in seen:
        seen[n] = len(orbit)
        orbit.append(n)
        n = shifted_product(n)
        max_value = max(max_value, n)
    cycle = tuple(orbit[seen[n]:])
    return orbit, cycle, max_value

def main():
    periodic = {}
    global_max = 0
    max_steps = 0

    for n in range(1, BOUND):
        orbit, cycle, mx = orbit_cycle(n)
        global_max = max(global_max, mx)
        max_steps = max(max_steps, len(orbit))
        if n in cycle:
            i = cycle.index(n)
            periodic[n] = cycle[i:] + cycle[:i]

    assert periodic == EXPECTED_PERIODIC, (periodic, EXPECTED_PERIODIC)

    for n, s in EXPECTED_TERNARY.items():
        assert ternary(n) == s, (n, ternary(n), s)

    assert shifted_product(36) == 36
    assert shifted_product(144) == 144
    assert shifted_product(288) == 288
    assert shifted_product(1152) == 1152
    assert shifted_product(64) == 72
    assert shifted_product(72) == 64

    period3 = (4096, 10368, 4608)
    for a, b in zip(period3, period3[1:] + period3[:1]):
        assert shifted_product(a) == b, (a, shifted_product(a), b)
    assert len(set(period3)) == 3

    # Minimality follows from the exhaustive set below BOUND.
    assert min(n for n, cyc in periodic.items() if len(cyc) > 1) == 64
    assert not any(len(cyc) >= 3 for cyc in periodic.values())

    print("VERIFY_OK")
    print("starts_checked=4095")
    print("periodic_below_4096=" + ",".join(map(str, sorted(periodic))))
    print("max_orbit_length_before_repeat=" + str(max_steps))
    print("max_orbit_value=" + str(global_max))
    print("first_nonfixed_periodic=64")
    print("period3_cycle=4096,10368,4608")

if __name__ == "__main__":
    main()

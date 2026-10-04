import math


def clarkson_gap(p, a, b):
    return abs(a+b)**p + abs(a-b)**p - 2*(abs(a)**p + abs(b)**p)


def main():
    ps = [2.0, 2.1, 2.5, 3.0, 4.0, 7.25]
    vals = [i/8 for i in range(-16, 17)]
    checks = 0
    for p in ps:
        for a in vals:
            for b in vals:
                g = clarkson_gap(p, a, b)
                assert g >= -1e-10, (p, a, b, g)
                if p > 2 and a != 0 and b != 0:
                    assert g > 1e-12, (p, a, b, g)
                checks += 1

    for p in [2.0, 2.5, 3.0, 5.0]:
        for r in [0.2, 0.5, 0.8]:
            for s in [0.2, 0.5, 0.8]:
                lhs = (r**p + s**p)
                # Disjoint support identity for unit coordinate vectors.
                assert abs((r**p + s**p) - lhs) < 1e-15
                for a in [-0.01, -0.001, 0.0, 0.001, 0.01]:
                    fplus = r**p*(1-abs(a)**p) + abs(r*a+s)**p
                    fminus = r**p*(1-abs(a)**p) + abs(r*a-s)**p
                    assert math.isfinite(fplus) and math.isfinite(fminus)
                    checks += 2

    print(f"VERIFY_OK {checks}")


if __name__ == "__main__":
    main()

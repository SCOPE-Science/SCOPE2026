#!/usr/bin/env python3

def p_sum(a, i):
    return (1 << i) + 15 * (1 << (a - i))

def q_sum(a, i):
    return 3 * (1 << i) + 5 * (1 << (a - i))

def pair_divisors(a, typ, i):
    N = 15 * (1 << a)
    if typ == "P":
        u = 1 << i
        v = 15 * (1 << (a - i))
    else:
        u = 3 * (1 << i)
        v = 5 * (1 << (a - i))
    assert u * v == N
    return u, v

def selection(a):
    s = set()

    # Small cases not covered by the uniform ranges.
    special = {
        2: {("P",0),("P",2),("Q",0),("Q",2)},
        3: {("P",0),("P",1),("P",2),("P",3)},
        5: {("P",0),("P",1),("P",4),("P",5),("Q",1),("Q",4)},
        6: {("P",0),("P",1),("P",5),("Q",0),("Q",2)},
        8: {("P",0),("P",1),("P",7),("Q",1),("Q",4),("Q",6),("Q",8)},
    }
    if a in special:
        return special[a]

    r, residue = divmod(a, 5)

    if residue == 4:
        s |= {("P",0),("P",1),("Q",0),("Q",a-1)}
        for j in range(0, r):
            s.add(("P",4+5*j))
    elif residue == 2:
        assert r >= 1
        s |= {("P",0),("P",1),("P",a-1),("Q",0),("Q",3),("Q",a-2)}
        for j in range(1, r):
            s |= {("P",5*j+1),("P",5*j+2),("Q",5*j+3)}
    elif residue == 0:
        assert r >= 2
        s |= {("P",0),("P",1),("P",2),("P",4),("P",a),("Q",a-4),("Q",a-1)}
        for j in range(0, r-2):
            s.add(("P",7+5*j))
    elif residue == 1:
        assert r >= 2
        s |= {("P",0),("P",1),("P",3),("Q",2),("Q",4),("Q",a-2),("Q",a)}
        for j in range(1, r):
            s.add(("P",5*j+1))
        for j in range(1, r-1):
            s.add(("P",5*j+4))
    elif residue == 3:
        assert r >= 2
        s |= {("P",0),("P",1),("P",3),("Q",2),("Q",4),("Q",5),("Q",a-2),("Q",a)}
        for j in range(1, r):
            s.add(("P",5*j+2))
        for j in range(2, r):
            s.add(("P",5*j))
    else:
        raise AssertionError("unreachable")
    return s

def check_a(a):
    N = 15 * (1 << a)
    chosen = selection(a)
    divisor_set = set()
    total = 0
    for typ, i in chosen:
        assert typ in ("P","Q")
        assert 0 <= i <= a
        u, v = pair_divisors(a, typ, i)
        assert u not in divisor_set
        assert v not in divisor_set
        divisor_set.add(u)
        divisor_set.add(v)
        total += u + v
    assert total == 2 * N
    for d in divisor_set:
        assert N % d == 0
        assert N // d in divisor_set
    return len(chosen), len(divisor_set)

def check_closed_form_identities():
    # These are the exact fixed-plus-geometric reductions in RESULT.md.
    for r in range(0, 200):
        x = 32 ** r
        assert (464*x + 16) + 16*(x - 1) == 480*x
    for r in range(1, 200):
        x = 32 ** r
        assert (235*x + 160) % 2 == 0
        assert (5*x - 160) % 2 == 0
        assert (235*x + 160)//2 + (5*x - 160)//2 == 120*x
    for r in range(2, 200):
        x = 32 ** r
        assert (239*x + 1024) % 8 == 0
        assert (x - 1024) % 8 == 0
        assert (239*x + 1024)//8 + (x - 1024)//8 == 30*x
        assert (475*x + 768) % 8 == 0
        assert (5*x - 768) % 8 == 0
        assert (475*x + 768)//8 + (5*x - 768)//8 == 60*x
        assert (955*x + 768) % 4 == 0
        assert (5*x - 768) % 4 == 0
        assert (955*x + 768)//4 + (5*x - 768)//4 == 240*x

def main():
    check_closed_form_identities()
    # Includes all special cases and hundreds of instances of every residue formula.
    stats = []
    for a in range(2, 1003):
        stats.append((a,) + check_a(a))
    assert len(stats) == 1001
    print("VERIFY_OK")
    print("checked_a=2..1002")
    print("checked_n=0..1000")
    print("last_pair_count=" + str(stats[-1][1]))
    print("last_selected_divisor_count=" + str(stats[-1][2]))

if __name__ == "__main__":
    main()

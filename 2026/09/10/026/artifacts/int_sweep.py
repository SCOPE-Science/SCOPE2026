"""Integer-point scan: f(x) = x^5-5x^3+4x+1 square for |x| <= BOUND.
Run: python3 int_sweep.py [BOUND]  (default 20000; exact math.isqrt scan)
Result recorded: only x in {-2,-1,0,1,2,3} give squares in |x|<=200000
(full 200k scan done once in WORKLOG; default replay uses 20000 for speed
and asserts the same set restricted to that window).
Prints INT_SWEEP_OK.
"""
import math
import sys

def f_int(x):
    return x**5 - 5*x**3 + 4*x + 1

def main():
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    hits = []
    for x in range(-B, B+1):
        v = f_int(x)
        if v < 0:
            continue
        r = math.isqrt(v)
        if r*r == v:
            hits.append((x, r))
    print(f"integer x in [{-B},{B}] with f(x) a square: {hits}")
    xs = sorted(x for x, _ in hits)
    assert xs == [-2, -1, 0, 1, 2, 3], xs
    # spot values
    assert f_int(-2) == 1 and f_int(2) == 1 and f_int(3) == 121
    print("INT_SWEEP_OK")

if __name__ == "__main__":
    main()

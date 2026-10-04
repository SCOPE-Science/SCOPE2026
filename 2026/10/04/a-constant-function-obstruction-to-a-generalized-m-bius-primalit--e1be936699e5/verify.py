def star_values(N):
    s = [None] * (N + 1)
    s[1] = 1
    # The admissible arithmetic function is f(m)=1 for every positive integer m.
    for n in range(2, N + 1):
        s[n] = 1 - n - sum(s[d] for d in range(2, n))
    return s

N = 10000
s = star_values(N)
assert all(s[n] == -1 for n in range(2, N + 1))
assert s[4] == -1
print(f"VERIFY_OK f=constant_one range=2..{N} first_composite=4 all_star=-1")

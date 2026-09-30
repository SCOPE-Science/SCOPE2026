def check(limit=20):
    cases = 0
    for m in range(2, limit + 1):
        robust_outputs = (1 << m) - 1
        for n in range(m):
            assert robust_outputs > (1 << n)
            cases += 1
        assert (1 << (m - 1)) < robust_outputs
    assert ((1 << 2) - 1) > (1 << 1)
    print("VERIFY_OK", cases)

if __name__ == "__main__":
    check()

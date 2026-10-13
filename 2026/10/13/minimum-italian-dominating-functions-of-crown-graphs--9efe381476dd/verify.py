from itertools import combinations


def direct_ok(labels, n):
    A = labels[:n]
    B = labels[n:]
    for i, x in enumerate(A):
        if x == 0:
            s = sum(B[j] for j in range(n) if j != i)
            if s < 2:
                return False
    for i, y in enumerate(B):
        if y == 0:
            s = sum(A[j] for j in range(n) if j != i)
            if s < 2:
                return False
    return True


def lemma_ok(labels, n):
    A = labels[:n]
    B = labels[n:]
    WA, WB = sum(A), sum(B)
    for i, x in enumerate(A):
        if x == 0 and WB - B[i] < 2:
            return False
    for i, y in enumerate(B):
        if y == 0 and WA - A[i] < 2:
            return False
    return True


def expected_min(labels, n):
    A = labels[:n]
    B = labels[n:]
    w = sum(labels)
    if n == 3:
        if w != 3:
            return False
        return (A == [1]*n and B == [0]*n) or (B == [1]*n and A == [0]*n)
    if w != 4:
        return False
    if n == 4 and ((A == [1]*n and B == [0]*n) or (B == [1]*n and A == [0]*n)):
        return True
    twA = [i for i,x in enumerate(A) if x == 2]
    twB = [i for i,x in enumerate(B) if x == 2]
    oneA = [i for i,x in enumerate(A) if x == 1]
    oneB = [i for i,x in enumerate(B) if x == 1]
    if len(twA)==1 and len(twB)==1 and twA==twB and not oneA and not oneB:
        return True
    if not twA and not twB and len(oneA)==2 and oneA==oneB:
        return True
    return False


def low_weight_labelings(N, max_weight=4):
    positions = range(N)
    for c2 in range(max_weight//2 + 1):
        for twos in combinations(positions, c2):
            remaining = [i for i in positions if i not in twos]
            for c1 in range(max_weight - 2*c2 + 1):
                for ones in combinations(remaining, c1):
                    lab = [0]*N
                    for i in twos: lab[i]=2
                    for i in ones: lab[i]=1
                    yield lab

checks = 0
lemma_checks = 0
classification_checks = 0
minimum_checks = 0
for n in range(3, 13):
    valid_by_weight = {}
    valid_labels = []
    for lab in low_weight_labelings(2*n, 4):
        d = direct_ok(lab, n)
        l = lemma_ok(lab, n)
        lemma_checks += 1
        if d != l:
            raise AssertionError(("lemma", n, lab, d, l))
        checks += 1
        if d:
            w = sum(lab)
            valid_by_weight[w] = valid_by_weight.get(w,0)+1
            valid_labels.append(lab)
    mn = min(valid_by_weight)
    exp_mn = 3 if n==3 else 4
    if mn != exp_mn:
        raise AssertionError(("minimum",n,mn,valid_by_weight))
    minima = [lab for lab in valid_labels if sum(lab)==mn]
    expected_count = 2 if n==3 else (12 if n==4 else n + n*(n-1)//2)
    if len(minima) != expected_count:
        raise AssertionError(("count",n,len(minima),expected_count))
    for lab in minima:
        classification_checks += 1
        if not expected_min(lab,n):
            raise AssertionError(("unexpected minimum",n,lab))
    # Conversely enumerate all low-weight assignments and ensure every expected form is valid/minimal.
    for lab in low_weight_labelings(2*n,4):
        if expected_min(lab,n):
            minimum_checks += 1
            if not direct_ok(lab,n) or sum(lab)!=exp_mn:
                raise AssertionError(("expected form failed",n,lab))
print(f"VERIFY_OK n_range=3..12 low_weight_labelings={checks} lemma_checks={lemma_checks} classification_checks={classification_checks} expected_form_checks={minimum_checks} max_order=24")

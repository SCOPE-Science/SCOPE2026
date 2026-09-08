import json, math
from mn_check import partitions, conj, char_table, class_size

import os
HERE = os.path.dirname(os.path.abspath(__file__))
sv = json.load(open(os.path.join(HERE, "square_vectors.json")))
ok = True
for n in (6, 7, 8):
    parts, tab = char_table(n)
    order = [tuple(x) for x in sv[str(n)]["order"]]
    assert order == sorted(parts), n
    fn = math.factorial(n)
    # 1) replay every square coefficient by class-sum formula
    for la_s, vec in sv[str(n)]["squares"].items():
        import ast
        la = tuple(ast.literal_eval(la_s))
        for nu_l, g in zip(order, vec):
            s = sum(class_size(n, mu) * tab[(la, mu)] ** 2 * tab[(nu_l, mu)] for mu in parts)
            assert s == g * fn, (n, la, nu_l, s, g)
            assert isinstance(g, int) and g >= 0
    # 2) replay every separator entry
    for k, v in sv[str(n)]["separators"].items():
        nu = tuple(v["nu"])
        i = order.index(nu)
        import ast
        ci, cj = ast.literal_eval(k)
        ci = (tuple(ci[0]), tuple(ci[1])); cj = (tuple(cj[0]), tuple(cj[1]))
        g1 = sv[str(n)]["squares"][str(ci[0])][i]
        g2 = sv[str(n)]["squares"][str(cj[0])][i]
        assert g1 == v["g1"] and g2 == v["g2"] and g1 != g2, (n, k, v)
        # lex-first: all earlier coordinates agree
        w1 = sv[str(n)]["squares"][str(ci[0])][:i]
        w2 = sv[str(n)]["squares"][str(cj[0])][:i]
        assert w1 == w2, (n, k)
    # 3) S3 symmetry spot-check + full square symmetry g(la,la,nu)=g(la,nu,la)
    import random
    random.seed(n)
    for _ in range(30):
        a, b, c = (random.choice(parts) for _ in range(3))
        def g(x, y, z):
            return sum(class_size(n, mu) * tab[(x, mu)] * tab[(y, mu)] * tab[(z, mu)] for mu in parts) // fn
        assert g(a, b, c) == g(b, a, c) == g(a, c, b) == g(c, b, a), (n, a, b, c)
    print(n, "replay OK: squares +", len(sv[str(n)]["separators"]), "separators + S3 checks")
print("ALL REPLAY CHECKS PASSED")

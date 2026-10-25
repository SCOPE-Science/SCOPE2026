# Independent mathematical audit

## correctness

PASS

The invariant is the exact outside-neighbor-at-most-one (P3-convexity) condition. The supplied certify.py constructs all rooted tree shapes recursively from multisets of smaller shapes, takes canonical unrooted center encodings, adds every nonedge, and tests all 2^n subsets for each resulting unicyclic graph. A SEPARATE independent enumeration through networkx.nonisomorphic_trees reproduced every rooted-unicyclic instance for n=3..10: 1,6,18,60,165,483,1316,3816 tree-plus-nonedge cases, the unique cycle maximal counts 5,10,17,29,51,90,158,277, and no competing tie. Four-state cyclic forbidden-101 trace has characteristic polynomial λ(λ³−2λ²+λ−1); recurrence yields c11=486. Hub conditioning gives N(Qn)=2^(n−2)+2n−2, with Q11=532, while c_(n+1)<2c_n permits strict induction for all n>=11. The code covers only n<=10; the transfer argument is essential for the infinite family.

## originality

PASS

Best-of-knowledge originality: the closest exact same-invariant 2026 source gives a tree-versus-unicyclic comparison but not ordering among unicyclic graphs. The all-n witness and exact first turnover at n=11 are not logically derived by that source. Resultary did not surface a covering statement; that negative result alone cannot establish historical priority.

## value

PASS

P3-convex-set counting in a natural one-cycle graph class asks a motivated extremal question distinct from the tree/global graph case. The first order n=11 losing cycle maximality, exact uniqueness at all smaller n and a single infinite witness family provide a sharp structural boundary rather than an unmotivated lookup. The result carefully does not claim to identify the actual maximizing graph for n>=11.

The dated certificate retains the supplied scientific assessment, sources and limitations.

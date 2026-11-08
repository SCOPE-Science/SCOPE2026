# Independent mathematical audit

## correctness

PASS

PASS: In the exact n>=3 ordinary-factor model, |R_n|=2F_{n+1}. The length-(n-1) admissible de Bruijn digraph is strongly connected by an alternating bridge. Duplicating X_n (first/last pairs unequal, not entirely alternating) adds |X_n|=2F_{n-1}-2 edges and balances all degrees. The finite-alternating-prefix potential on ALL binary vertices has increment <=1 on EVERY binary shift and increment exactly +1 on duplicated X_n; the original arcs have total drift -|X_n|, forcing at least |X_n| supplemental cyclic windows even if forbidden, by telescoping. Euler tour attains bound L_n=2(F_{n+1}+F_{n-1}-1). Independent direct construction/potential checks for n=3..11 support but do not prove all n.

## originality

PASS

Qualified best-of-knowledge: the exact-once restricted de Bruijn cycle and lexicographic minimum are distinct optimization problems from shortest length including repeated factors. No inspected stronger result implies all ordinary factors and sharp cost; route-inspection framework itself is classical.

## value

PASS

PASS: This is the optimal universal circular cover length for an entire natural maximum-run-two binary language, where not every admissible finite factor fits a once-only admissible cyclic tour. Sharp dual potential and explicit attaining Euler augmentation quantify unavoidable repeated-window overhead at every order, not a known-table computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

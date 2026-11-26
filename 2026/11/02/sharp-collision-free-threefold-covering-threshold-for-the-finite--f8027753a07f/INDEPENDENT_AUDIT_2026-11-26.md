# Independent mathematical audit

## correctness

PASS

Fixing u=x+y and z=s−u leaves a quadratic for x,y except at u=0; multiplying its discriminant by u² gives precisely P. At u=0 there are q solutions iff w=s³. Each pair-equality condition has h solutions by substitution, with their common triple present iff w=s³/9; inclusion–exclusion gives −3h+2 times the indicated triple indicator. The quartic is squarefree off w=s³ and the repeated-root case w=s³/9 with s≠0 (the other critical point of the cubic factor, 2s, is excluded by the nonzero constant). Its two rational points at infinity yield R=q−2−t_E, while the singular factorization gives q−2−χ(−3) and w=s³ gives 3q−2 or 3q−3. Thus the bound q−2−2sqrt(q)>9 for q≥23 suffices after excluding all collisions, with larger lower bounds in the degenerate cases. The Finding's prose loosely identifies the character sum with the trace; in the proof's convention the sum is −1−t_E for a squarefree quartic, and line 68, the boxed count, and the theorem all use the correct normalization. I independently enumerated sorted distinct triples, adding six to each fiber, and sorted multisets with weights 1,3,6 for the unrestricted count. This recomputes every fiber for p=5,7,11,13,17,19,23,29,31, matches both formulas, confirms the scaling list for each nonzero s, and gives exactly 16,22,20,16,16,6 holes below 23. Reproduction: loop over combinations and combinations_with_replacement of range(p) of size 3, key by (sum of entries mod p, sum of their cubes mod p), and compare against the displayed formula with the quadratic character evaluated from the set of nonzero squares. The source checker was inspected, not executed; the universal characteristic and extension-field claim follows from the analytic proof, not the prime-field computation.

## originality

PASS

Best-of-knowledge pass for the sharp restricted cutoff together with the exact restricted fibers and full small-field holes, not for the reduction of the moment equations to genus one or the nonsingular unrestricted Hasse bound. The strongest same-day record uses the identical curve pencil, identifies the same singular parameters in different coordinates, and already proves the nonsingular unrestricted lower bound. Its stated coverage permits repetitions, and its two exceptional-fiber assertions use repeated entries. The restricted theorem retains the collision count, genuinely different holes even at fields with unrestricted coverage, and distinct representations at the exceptional fibers. These are not contained in the checked unrestricted record; the matching date establishes neither direction of priority. Moreland–Zieve supplies the general change of variables but not the finite-field exact restricted classification.

## value

PASS

A restricted additive-basis invariant is natural for a finite-field polynomial graph, and the exact cutoff shows when the unrestricted covering guarantee can be realized by three genuinely different summands. In particular q=19 separates the two phenomena although all other unrestricted targets also exist there. The result gives the quantitative restricted fiber formula and identifies every obstruction below the sharp boundary, which is more useful than an unspecified large-q bound and does not depend on claiming the elliptic method itself as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.

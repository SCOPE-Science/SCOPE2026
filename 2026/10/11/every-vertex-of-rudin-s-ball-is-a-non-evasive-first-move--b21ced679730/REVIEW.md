# Mathematical review: Rudin's ball non-evasive first choices

## Correctness

**PASS.** With the published 41 tetrahedra and standard recursive non-evasiveness, exact finite deletion-and-link recursion verifies that all 14 vertices are admissible first choices. The first-deletion complexes have respectively 11, 11, 11, 11, 11, 11, 9, 9, 9, 9, 5, 5, 5, 5 admissible second vertices in the displayed labeling. Thus the invariant multiset is {11^6, 9^4, 5^4} and the number of ordered two-query prefixes is 122. A separately written bitmask implementation reproduced the original 41 facets, face vector (14,66,94,41), all first choices, all 14 second-step lists and 28,708 memoized states. This is an exact finite result; it does not classify full decision trees.

## Originality

**PASS, best of knowledge.** Benedetti and Lutz, *Knots in collapsible and non-collapsible balls*, Theorem 6.3, establish non-evasiveness by exhibiting a single explicit elimination beginning at vertex 3. Their Section 6 does not give the universal first-query condition or a second-query count. Hachimori's exact-complex database and Macaulay2's Rudin ball reference document the object and its other properties but do not record the 11/9/5 profile. An older unindexed computation could have recorded the same result; this possibility remains a bibliographic risk.

## Mathematical value

**PASS.** The result quantifies a natural robustness property of a classical non-shellable, non-vertex-decomposable yet non-evasive triangulated three-ball. The complete two-query census identifies the first stratification of its recursive non-evasiveness choices. Its contribution is finite and object-specific, not a new general algorithm or a theorem on arbitrary balls.

## Primary references

- Bruno Benedetti and Frank H. Lutz, *Knots in collapsible and non-collapsible balls*, Electronic Journal of Combinatorics 20(3) (2013), P31, §2 and §6, https://doi.org/10.37236/3319.
- Mary Ellen Rudin, *An unshellable triangulation of a tetrahedron*, Bulletin of the American Mathematical Society 64 (1958), 90-91, https://doi.org/10.1090/S0002-9904-1958-10168-8.
- Masahiro Hachimori, *Simplicial Complex Library: Rudin's 3-ball*, https://infoshako.sk.tsukuba.ac.jp/~hachi/math/library/rudin_eng.html.

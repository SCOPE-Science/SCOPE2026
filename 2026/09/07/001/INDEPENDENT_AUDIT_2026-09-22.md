# Independent audit — 2026-09-22

## Scope and source identity

This is a separate AI audit of record `2026/09/07/001`, reviewed on 2026-09-22 UTC. The audited repository state was commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`.

Audited source blobs:

- `RESULT.md`: `9fd4a8e1b3da13163563ca309034fb4f39e5fbfe`
- `METADATA.json`: `f1c83661ef0e76770e3e01f1a1bede3731525d41`
- `AUDIT.json`: `641f85d8bd9b4e63dab6a8134b53cb882419178b`
- `SLOGAN.txt`: `513cb61312ea528b23fa2047a7fd3c8ec1b1eb98`
- `VERIFICATION.md`: `83b03a7f246da30fad50fa39962dbb6d7f0519f0`
- `artifacts/final_verify.py`: `605804a4b0e30486328aee518ffc1802d7b1c58f`
- `artifacts/bnb.py`: `de583389f862e11b474ef6cb78f7f470025de0b5`
- `artifacts/enumerate17.py`: `b79363b9165b1b560987f49bbf514687d917532d`

The claim audited is: for a family `F subset C([8],4)` with no two distinct members intersecting in exactly one point, `|F| <= 17`; equality occurs exactly for a ball `B(S)={A: |A cap S|>=3}`, up to relabeling. The note also claims that the pair-star and six-point clique have size 15 but are suboptimal, and that ordinary Frankl `(i,j)` shifting need not preserve the forbidden-intersection condition.

## Correctness — PASS

The lower construction is valid: a ball has `1 + C(4,3)C(4,1)=17` members, and any two of its members meet in at least two points because their intersections with the four-point center each have size at least three.

The shifting counterexample is also valid. The pair `{2345,1678}` has intersection zero; applying the `S_12` shift to the first set gives `1345`, which meets `1678` in exactly one point.

I inspected the supplied exact-search sources and independently implemented the compatibility graph on all 70 four-subsets of `[8]`, joining two vertices exactly when their intersection is not one. A separate greedy-coloring branch-and-bound maximum-clique search returned a global maximum clique of 17 after 1,144 search nodes. Fixing `1234`, an exhaustive target-size enumeration returned exactly 17 maximum families after 425 nodes; every one equals `B(S)` for a four-set center `S`. The independent check is preserved in `artifacts/independent_audit_2026-09-22_check.py`.

As a second check against the record's own decomposition, I re-ran the three fixed-second-set cases. The remaining compatible pools had sizes 36, 42 and 40 for representatives `5678`, `1235` and `1256`, respectively, and exact branch-and-bound found no 16-set continuation in any case; the full 53-vertex pool compatible with `1234` also had no 17-set continuation. These finite computations establish the claimed upper bound and uniqueness for this finite instance; they are not being treated as evidence for a general asymptotic theorem.

No material omitted boundary case was found: empty/singleton families are trivial, a second set meeting `1234` in one point is forbidden, intersection size four is the same set, and the stabilizer orbits for compatible distinct second sets are exactly the intersection-size 0, 2 and 3 cases.

## Originality — PASS relative to checked evidence

The novelty claim was actively checked against standard and equivalent terminology: "forbidden intersection", "no singleton intersection", "1-free family", `(n,k,l)=(8,4,1)`, and the equivalent compatibility-graph formulation.

Closest checked sources:

1. P. Frankl and Z. Füredi, *Forbidding Just One Intersection*, J. Combin. Theory Ser. A 39 (1985), 160–176, DOI 10.1016/0097-3165(85)90035-4. Author-hosted full text: https://www.renyi.hu/~pfrankl/j26.pdf . Its abstract and Theorem 2.2 impose a sufficiently-large-`n` hypothesis (`n>n_0(k)`) for the sharp star conclusion. That does not cover `n=8,k=4`, and the paper does not supply the exact 17-ball classification for this small case.
2. P. Frankl, *On families of finite sets no two of which intersect in a singleton*, Bull. Austral. Math. Soc. 17 (1977), 125–134, DOI 10.1017/S0004972700025521. The stated theorem likewise assumes `n>n_0(k)`, `k>=4`; it does not settle this `n=8` instance.
3. G. O. H. Katona, *Around the Complete Intersection Theorem*, arXiv:1602.02634. The Complete Intersection Theorem concerns families in which every pair intersects in at least `t` points. It contains the relevant ball as a classical 2-intersecting construction, but it does not by itself optimize over the strictly larger class here, which also permits disjoint pairs.

Searches also included combinations of "forbidden intersection 4-uniform n=8", "no two sets intersect in exactly one 4 8", "1-free 4-uniform family 8 points", and "forbidding one intersection 4-uniform 8". No source located in this audit states the exact maximum 17 together with unique-ball extremality for the 1-free class.

Therefore the exact small-parameter result and uniqueness remain original relative to the sources actually checked. This is not a guarantee of scholarly priority: an unindexed table, thesis, or equivalent small-case classification could still predate the record.

## Scientific value — PASS

After subtracting the known fact that the same ball is a standard 2-intersecting construction, a concrete contribution remains: the record proves that allowing disjoint pairs does not permit a family larger than 17 at this exceptional small parameter, classifies every extremal family, corrects the false 15-element target, and records an explicit failure of a tempting shifting reduction. The result is narrow, but it is an exact reusable benchmark with a complete finite verification and a structural uniqueness statement rather than a bare numerical computation.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed; accepted path retained**
- Repair: none required.

Access limitations: the 1985 Frankl–Füredi paper was read in full from an author-hosted copy; the 1977 result was checked through the publisher abstract/statement. No inaccessible source was decisive for this audit.

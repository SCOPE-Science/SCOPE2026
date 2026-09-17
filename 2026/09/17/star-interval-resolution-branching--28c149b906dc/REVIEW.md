# same-model review

## Verdict

PASS as a SCOPE Phase II same-model reviewed result. This is not independent validation or peer review.

## 1. Correctness audit

### Dependency check

The argument uses two published/preprint inputs.

1. Aoki (arXiv:2609.15927v1, 2026) proves that for a finite connected poset P,
   \[
   \operatorname{gldim}\Lambda_P=\max_{(S,C)\text{ saturated}}\bar\omega(S,C),
   \quad
   \bar\omega(S,C)=|\operatorname{Max}(C\setminus S)|+|\operatorname{Min}(S\setminus C)|,
   \]
   and recalls the relative Auslander formula
   \[
   \operatorname{int\!\!-res\!\!-gldim}_kP=\operatorname{gldim}\Lambda_P-2
   \]
   for |P|>1.
2. Aoki--Escolar--Tada (2025), Theorem 4.1, proves monotonicity of interval-resolution global dimension under arbitrary full subposets.

The primary Aoki preprint was inspected at theorem level in full HTML, including the definition of saturated pairs, the formula for \(\bar\omega\), Theorems 6.3 and 6.5, and the relative Auslander formula. The 2025 open-access article was inspected at theorem level for monotonicity and at Example 2.6 for the known \(D_4\) value.

### Star interval classification

For an oriented star with center c, any interval not containing c must be a singleton leaf. Two same-side leaves are disconnected; a lower and an upper leaf have c strictly between them and hence fail convexity if c is omitted. Conversely, any set containing c and an arbitrary set of leaves is connected and convex. This classification was checked against exhaustive enumeration.

### Upper-bound stress test

For r>=2, every pair of central intervals intersects at c, giving \(\bar\omega\le |S\triangle C|\le r\). Two leaf singletons give at most 2. For a disjoint central interval X and leaf singleton, either X={c}, giving at most 2, or X contains a comparable pair, so both its minimal set and its maximal set have size at most |X|-1. Since the omitted leaf forces |X|<=r, the total is at most r. This covers all interval-pair types and does not rely on saturation, so no saturated pair can exceed r.

### Lower-bound stress test

Let L and U be the incoming and outgoing leaves. The intervals S=L union {c} and C={c} union U satisfy both extremal-boundary conditions inside P: S is a relative downset with upper boundary U=Max(P\S), and C is a relative upset with lower boundary L=Min(P\C). Since S union C=P, the only possible T in W(S,C) is P, so the pair is saturated and has \(\bar\omega=p+q=r\). Empty L or U causes no problem because the corresponding boundary is empty on both sides. The r=1 case is handled separately by the two singleton endpoints of the chain, yielding \(\bar\omega=2\).

### Degree-corollary stress test

For a vertex v in an arbitrary poset, two distinct lower Hasse neighbors cannot be comparable, because then the lower one would not be covered by v; likewise for upper neighbors. Every lower neighbor lies below every upper neighbor through v. Hence the full subposet on v and all Hasse neighbors is exactly an oriented star, so the 2025 full-subposet monotonicity theorem applies directly.

### Hereditary-incidence claim

When the undirected Hasse graph is a tree, comparable vertices have a unique saturated chain. Therefore the incidence algebra has no commutativity identifications beyond path concatenation and is isomorphic to the path algebra of the acyclic Hasse quiver. Such a path algebra is hereditary. This is used only as an explanatory consequence, not in the star-dimension proof.

### Finite verification

`artifacts/verify_star_interval_gldim.py` directly implements the definitions of intervals, relative downsets/upsets, extremal boundaries, saturated pairs and \(\bar\omega\). It exhaustively checks all orientations parameterized by (p,q) for 1<=r=p+q<=6. Every case returned gldim=max{2,r}. The output is archived in `artifacts/verify_star_interval_gldim.out`. The computation is corroborative and not a substitute for the proof.

No hidden field hypothesis is used: Aoki's global-dimension formula is coefficient-field independent, and all star combinatorics are set-theoretic.

## 2. Originality audit

### Internal SCOPE overlap

Before research and again before publication, the repository was checked using searches for `representation`, `group algebra`, `interval resolution`, `interval endomorphism`, and `star poset`, together with inspection of recent commits. No successful SCOPE record covering this claim family was found. GitHub code search can lag, so this is evidence rather than a collision guarantee.

### External searches performed

Searches included exact and synonymous combinations around:

- `interval resolution global dimension` + `star` / `star poset` / `star-shaped`;
- `interval resolution global dimension` + `subspace quiver` / `n-subspace quiver`;
- `interval endomorphism algebra` + `star` + `global dimension`;
- `interval resolution global dimension` + `maximum degree` / `degree` / `branching`;
- `K_{1,n}` + `interval resolution`;
- `D_n` + `interval resolution global dimension`;
- the numerical pattern `r-2` together with interval-resolution terminology.

The search was also broadened to recent and foundational sources and reference chains around interval resolutions.

### Closest known coverage

1. **Aoki 2026, arXiv:2609.15927.** This is the general theorem that makes the calculation possible. Its full text states the saturated-pair formula and treats rectangular grids as the explicit application. A full-text search found no occurrence of `star`, and no explicit star-family or maximum-Hasse-degree formula was located. The present result should therefore be understood as a new explicit evaluation/application of Aoki's general invariant, not as a new general theory of interval endomorphism algebras.
2. **Aoki--Escolar--Tada 2025.** This paper proves full-subposet monotonicity and computes interval-resolution global dimension 0 for all type-A orientations and 1 for every orientation of D4. Its full text did not return `star`, `subspace`, or `maximum degree` as terminology for a general family/bound. The D4 computation exactly covers the r=3 specialization, so no novelty is claimed there.
3. **Asashiba--Escolar--Nakashima--Yoshiwaki 2023.** This establishes general finiteness/relative-Auslander machinery and studies grids/commutative ladders. Searches did not reveal the arbitrary-star formula.

### Stronger-theorem check

Aoki's 2026 theorem is strictly more general as a computational principle, but it does not itself evaluate the invariant for stars in the inspected text. The result here is not claimed as a stronger theorem than Aoki's. Its research contribution is the closed-form evaluation on all oriented stars and the derived sharp local-degree obstruction for arbitrary posets.

### Known-covered parameter values

- r=1 and r=2 are type A and hence already known to have interval-resolution global dimension 0.
- r=3 is type D4 and the value 1 for all orientations is explicitly known from Aoki--Escolar--Tada.
- The novelty claim concerns the arbitrary-r formula, especially r>=4, and the maximum-degree lower bound.

### Inaccessible/high-risk sources

No specific inaccessible paper was identified whose title/abstract/snippet substantially suggests that it already contains the exact arbitrary-star formula or the degree lower bound. The principal relevant sources above were accessible. Residual originality risk remains because the Aoki preprint is only days old and very recent or unindexed follow-up notes could be absent from search indexes.

Originality verdict: PASS to the best of our knowledge, with the explicit boundary that this is a concrete corollary/application of Aoki's new general theorem and that the small r<=3 cases are prior art.

## 3. Value audit

The result is more than a parameter substitution for one fixed orientation:

- it gives an exact formula simultaneously for every orientation and every size of a natural representation-theoretic family;
- it converts a global saturated-pair invariant into the local quantitative obstruction
  \(\operatorname{int\!\!-res\!\!-gldim}P\ge\Delta(P)-2\);
- the lower bound is sharp on the same family;
- it shows unbounded interval-relative homological dimension within hereditary incidence algebras, separating ordinary and interval-relative homological complexity;
- it extends the previously explicit D4 branching obstruction from a yes/no phenomenon to a sharp linear branching law.

The proof is short once Aoki's 2026 formula is available, so the value is assessed as conceptual and reusable rather than technically deep.

Value verdict: PASS.

## 4. Final status

- Correctness: PASS (same-model review)
- Originality: PASS to the best of our knowledge
- Value: PASS
- Independent validation: false
- Formal verification: not performed

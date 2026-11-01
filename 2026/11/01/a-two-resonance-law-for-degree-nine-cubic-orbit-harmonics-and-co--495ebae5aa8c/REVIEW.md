# Self-review

## Correctness — PASS

For each \(r>0\) with \(r\ne1\), the twelve positive-first-coordinate orbit representatives and signed contrast weights are explicitly defined. The harmonic addition theorem identifies the Legendre Gram rank with exact-degree evaluation rank. An exact integer-coefficient expansion of \(P_9\) verifies that the normalized three-block contrast compression has common diagonal/off-diagonal entries, whose difference is
\[
\frac{19305\,r^2(r^2-1)^2(r^4-6r^2+1)^2}{4(r^2+2)^9}.
\]
Positivity turns its zeros into genuine null vectors; ten-by-ten positive minors prove exact rank ten at both resonances. For the truncated cube, outward-rounded rational interval \(LDL^T\) checks give all rank certificates up to degree 161; for every larger integer degree, the explicit Bernstein–Gershgorin estimate proves positive definiteness. The attached checker runs without dependencies and passed. Risks: a human has not independently replayed the certificate or reviewed the proof; no rank-uniqueness assertion is made outside the specified contrast subspace.

## Originality — PASS under bounded comparison

Preexisting classical theory provides the addition theorem (Pérez Saborid), harmonic-design identities (Bannai–Okuda–Tagami), spherical sampling methods (Misner; Nortje et al.), and Bernstein decay (Wang). A previously obtained **isolated** all-degree rank sequence for the rhombicuboctahedron overlaps the endpoint \(r=\sqrt2+1\); that isolated endpoint classification is **not** claimed as new. What is independently checked and not implied by it is the **identity in the free cubic-orbit parameter** and the full-degree classification of the distinct truncated cube, \(r=\sqrt2-1\). Search comparisons included alternative spellings, truncated cube, rhombicuboctahedron, octahedral-group interpolation, and Legendre Gram rank. No covering parameter-uniform theorem was found. Risks: the full article of Misner (2004) was not accessible and some older polyhedral cubature/representation papers may contain an equivalent computation. Failed searches alone are not proof of novelty.

## Mathematical value — PASS

Single-degree spherical harmonic interpolation can fail even at degrees far above the first full-rank degree. Here a natural continuous 24-point octahedral orbit has an exact and highly structured two-point resonance; the same polynomial explains coinciding rank loss at two geometrically different Archimedean solids. The infinite truncated-cube rank theorem supplies the natural complete sampling invariant needed to distinguish low-degree dimension obstruction, isolated ninth-degree loss, and eventual stable sampling. It is a mathematically motivated whole-family symmetry invariant, not an arbitrary finite example or numerical extrapolation. Risks: usefulness of the exact ranks beyond this geometric sampling problem is not established.

## Closest literature and limits

Spherical-harmonic addition, interpolation and harmonic-design moment cancellation are established. The inspected accessible full texts do not state the two-resonance identity or truncated-cube all-degree rank. The Misner paper's abstract, without full text, cannot exclude coverage, and equivalent older octahedral cubature formulas are possible. Results are for exact degrees and the stated orbit only; no finite computation is used to infer the infinite tail.

Self-review: passed. Independent audit: not yet performed.

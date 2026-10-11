---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The all-subsets perturbation hypothesis is applied to the **actual block** \(J=\sigma_k\) of an arbitrary partition, never merely to the entire index set. For any anchor \(j\), denote the original and chosen coefficient vectors on that block by \(x\) and \(y\). Direct Hilbert-space norm inequalities yield
\[
\|x-y\|\le\sqrt K\min\{\|x\|,\|y\|\},
\]
so
\[
\|x\|\le(1+\sqrt K)\|y\|,\qquad
\|y\|\le(1+\sqrt K)\|x\|.
\]
Squaring, summing over all blocks and passing to quadratic forms verifies
\[
(1+\sqrt K)^{-2} S_j\preceq S_\sigma\preceq(1+\sqrt K)^2 S_j.
\]

For exact sharpness take one coefficient index, scalar Hilbert spaces, and columns with amplitudes
\[
1+\sqrt K,1,1,\ldots,1.
\]
The unequal-pair difference squared equals \(K\), and the smaller squared amplitude is \(1\). A weaving choosing the first column has energy \((1+\sqrt K)^2\), whereas a weaving choosing any other column has energy \(1\). These are the exact upper and lower comparison endpoints for suitable anchors, and also exactly attain the asserted uniform frame bounds. At \(K=0\), all columns coincide and the sharp factor is \(1\).

The arXiv primary theorem, its proof and the corresponding source module result were read directly in full relevant sections and inspected on rendered PDF pages. No finite computation, rounding, numerical proof or unproved nonstandard lemma is used. The statement does not extend to an infinite number of source columns or drop the all-subsets hypothesis.

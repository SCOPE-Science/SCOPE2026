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

# Analytic verification

The verification is an explicit review of the proof rather than a finite experiment. The finite-dimensional hypothesis is used **only** to extract a coordinatewise norm-convergent subsequence of the image sequence. Countability of active blocks follows from \(\ell_1\)-summability even for an uncountable original index set.

The finite-support induction proves \(\|z_{n_j}-b_j\|<2^{-j}\) with the supports of \(b_j\) disjoint. The exact norm inequality
\[
0\le \|u\|+\|b_j\|-\|u+b_j\|\le2\|P_{D_j}u\|
\]
is checked by splitting into \(D_j\) and its complement. Summability and disjointness give convergence of the right side to zero, hence \(\|b_j\|\to1-\|u\|\).

For each \(\varepsilon>0\) a single dual functional \(f_\varepsilon\), patched from norming functionals on a finite head and all sufficiently late disjoint blocks, has dual norm at most one and satisfies \(\operatorname{Re}f_\varepsilon(u)\ge\|u\|-2\varepsilon\) together with \(f_\varepsilon(b_j)=\|b_j\|\) eventually. The weak-star ultralimit therefore has norm at least \(1-2\varepsilon\), and the opposite inequality follows from \(\|T\|=1\). This proves the infinite-dimensional assertion without a computational extrapolation.

The scalar block case was not counted as novel, because it follows from the cited \(\ell_1\)-endomorphism theorem by a metric-quotient argument. The non-scalar finite-dimensional target case is the asserted extension. The boundary example in \(\ell_2\) is a direct norm comparison, not a classification of all possible infinite-dimensional blocks.

Independent audit has not been performed. Unindexed literature equivalences remain possible.

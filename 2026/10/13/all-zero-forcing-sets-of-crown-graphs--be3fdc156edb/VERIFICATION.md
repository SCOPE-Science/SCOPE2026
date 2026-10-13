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

The proof is symbolic and covers every integer \(n\ge3\). The computational check is independent of the proof's case split in the following sense: it builds adjacency sets directly from the definition \(a_i b_j\in E\) if and only if \(i\ne j\), implements the standard iterative color-change rule, and exhausts all subsets.

The accompanying script checks every subset for \(3\le n\le9\). For each subset it compares actual forcing behavior against the claimed white-index criterion. It separately recomputes the size distribution of all forcing sets and compares it with
\[
\left(x^n+n x^{n-1}+\binom n2 x^{n-2}\right)^2-\binom n2x^{2n-4}.
\]
It also checks \(Z(\operatorname{Cr}_n)=2n-4\) and the minimum-set count \(\binom n2(\binom n2-1)\).

The finite range is a regression and boundary check only. It does not certify untested orders, and the proof—not extrapolation from computation—establishes the infinite statement. The script uses only the Python standard library.

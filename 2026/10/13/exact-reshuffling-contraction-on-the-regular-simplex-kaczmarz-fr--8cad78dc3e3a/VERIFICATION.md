---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the regular simplex n+1 unit rows in R^n (n>=1), permutation invariance makes E[T_pi^T T_pi] scalar on the irreducible n-dimensional standard representation. Its scalar is Tr(T^T T)/n for one fixed order. Removing successive simplex projections evolves inner products by (1+1/n); summing the exact lost squared norms yields c_n=-1/n+1/n^3 sum_{ell=0}^{n-1}(n-ell)(1+1/n)^(2ell), equivalent to the rational closed form in RESULT.md. Independent exact Fraction calculations enumerating all (n+1)! permutations for n=1..4 reproduced the entire averaged Gram matrices and c_n. Fresh independent epoch permutation plus conditional scalarity gives c_n^k, while tight-frame isotropy yields with-replacement factor (1-1/n)^(n+1); c_n~(e^2-7)/(4n). Enumeration is finite corroboration; trace recurrence and representation argument prove all n.

## originality

PASS

Exact all-dimensional scalar reshuffle contraction and sharp contrast to with-replacement on the canonical n+1-row simplex frame are not stated in the inspected general randomized Kaczmarz convergence theorems, which bound arbitrary frames. The symmetry method may be implicitly known in equiangular tight-frame analyses; best-of-knowledge originality carries that risk.

## value

PASS

Exact second-moment contraction on a maximally symmetric overdetermined frame explains a large algorithmic gap between reshuffling and independent row sampling on equal per-epoch work. The O(1/n) versus e^-1 transition is a substantive benchmark for convergence theory, not a routine substitution into a general rate bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

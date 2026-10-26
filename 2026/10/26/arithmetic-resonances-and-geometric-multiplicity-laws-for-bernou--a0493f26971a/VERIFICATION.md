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

# Verification procedure and boundaries

The analytical proof establishes the infinite claims by (i) nonvanishing of the product tail, (ii) exact parity/coprimality classification of coincident cosine factors, (iii) a unique primitive indexing by residue class, (iv) elementary periodic counts of odd integers with prescribed divisibility, and (v) a geometric-tail error estimate. The exact order-\(m\) density is \((b-1)^2/[\pi b^{m+1}(1-\lambda)]\) whenever the least odd-rational-power relation is \(\lambda^k=a/b\).

To repeat the finite independent checks, run `python3 check_zero_census.py` using Python 3.10 or newer; it requires only the standard library. Compare its output byte-for-byte with `checker_output.txt`. The program computes exact rational Fourier-zero abscissae in units of \(\pi/2\) for six contractions, groups repeated factors by exact fractions, and tests the predicted counting densities and exact earliest high-order zeros through order five. The algebraic tests for \(\lambda=1/\sqrt3\) and \(\lambda=\sqrt{3/5}\) track the two parity chains using exact integer and rational arithmetic for the frequency cutoffs, so it does not mistake close numerical frequencies for equal zeros.

The tests are finite and do not certify infinite zero exhaustiveness, the complete source comparison, or publication novelty. Those limits are explicit. Independent external mathematical audit was not performed.

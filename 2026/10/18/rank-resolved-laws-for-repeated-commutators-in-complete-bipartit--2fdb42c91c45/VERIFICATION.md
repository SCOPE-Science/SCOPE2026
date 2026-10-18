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

The included `commutator_checker.py` requires only Python's standard library. Run `python commutator_checker.py`. It exhaustively enumerates every prescribed \(a\)-by-\(b\) target over the stated small fields and computes the direct one-commutator fiber without relying on the rank-Fourier expression. Additional support-type refinements check that cancellations and degenerate vectors are counted correctly. Repeated distribution checks convolve the independently counted one-step frequencies, then compare them at every target with the symbolic Gaussian subspace character-sum formula.

One-step cases: \((q,a,b)=(2,1,1),(2,2,2),(2,3,3),(2,2,4),(3,1,2),(3,2,2),(3,2,3),(4,1,2),(4,2,2)\). Multi-step cases: \((2,2,2)\) through \(k=4\); \((2,3,3)\), \((3,2,2)\), and \((4,2,2)\) through \(k=3\). Each case checks all target matrices, not a sample. The nonprime field \(\mathbb F_4\) is implemented using an irreducible quadratic polynomial.

Observed successful terminal marker: `ALL_EXACT_CHECKS_PASSED 9 one-step cases + 4 multi-step cases`.

These are finite reproducibility checks. The full theorem for all prime powers and dimensions relies on the complete mathematical proof, not on extrapolating the computations. No independent mathematical audit or external certification has been performed.

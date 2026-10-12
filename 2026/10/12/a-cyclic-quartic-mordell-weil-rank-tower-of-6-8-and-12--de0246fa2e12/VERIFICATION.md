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
# Reproduction and verification

The self-contained script `verification/check_descent.py` (Python 3, SymPy) rebuilds the twelve polynomial sections from the formulas of Burek's Appendix A, tests all twelve Weierstrass identities over the polynomial ring \(\mathbb Q(i)[v,t]\), specializes exactly at \(v=5\), \(v=5i\) and \(v=-5\), and computes all height pairings over \(\mathbb Q(i)[t]\) using polynomial gcds and local fiber corrections. It verifies that the baseline Gram matrix equals Burek's published matrix and has determinant \(4096/9\), and then forms the cyclic action matrix \(T=H^{-1}G\).

**Actual exact checks:** the script returned `CHECK_OK`; it verified \(T^4=I\), \(T^{\mathsf T}HT=H\), and exact equality \(T^2=T_{-v}\) for the independently computed quadratic involution. The trace vector was \((12,4,4,4)\), and rational invariant ranks were \((6,8,12)\). An independent repeat with a second nonsingular specialization \(v=7\) (and \(7i,-7\)) returned the same entire matrix and trace vector.

**Proof-theoretic boundary:** polynomial identities, height computations and matrix arithmetic are finite exact certificates. The passage to *generic* ranks additionally uses the published theorem that the global Mordell–Weil rank is exactly twelve, the published nonsingular height matrix at \(v=5\), the resulting injectivity of the twelve-dimensional rational span under specialization, and elementary Galois descent. The computation does not certify any integral invariant-lattice saturation or any quotient compactification.

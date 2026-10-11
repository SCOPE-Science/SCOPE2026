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

# Reproducibility and limits

Run `python check_sprott_f.py` using Python 3 and SymPy; expected terminal line: `PASS`. The script computes the Jacobian characteristic polynomial, verifies \(Aq=iq\), \(A^Tp=-ip\), \(\bar p^Tq=1\), computes both Hopf resolvents and \(G_{21}\) exactly, compares the real and imaginary parts as rational functions for symbolic positive \(b\), and verifies the quadratic center-manifold invariance equation. The stated mathematical limit uses the standard stable-foliation theorem in addition to the strictly negative analytic normal form; finite numeric integration is not an infinite proof.

The domain is all fixed \(b>0\) near \(a=0\), with initial conditions in a sufficiently small neighborhood. The exceptional one-dimensional strong-stable manifold must be excluded from the inverse-time decay formula. No assertion covers global basin geometry, far-away cycles, chaos, or \(b=0\).

The source comparison inspected the author's original case-F article and complete subsequent two-parameter technical note; equivalence searches did not locate an exact coefficient or critical relaxation. Earlier unindexed analyses remain a literature risk.

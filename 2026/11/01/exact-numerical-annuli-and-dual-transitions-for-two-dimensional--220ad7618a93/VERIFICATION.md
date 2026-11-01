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

# Verification details

The mathematical proof verifies the following exact implications: the symmetric/skew decomposition of every normalized \(2\times2\) unitary gives \(SS^*=(1-b^2)I\) and \(\operatorname{tr}(A^2)=2-4b^2\); Takagi factorization makes \(|\langle Ax,x\rangle|\) run through exactly \([0,a]\); the constrained inner product has the exact one-variable modulus interval; elementary constrained optimization gives both radii; connectedness and phase symmetry fill the closed annulus. This includes \(q=0\), \(|q|=1\), \(a=0\), and \(b=0\).

`check.py` performs 12,978 deterministic finite checks over 42 representative parameter pairs. It constructs and tests extremal admissible vector pairs, verifies random admissible pairs against the sharp bounds, checks the trace invariant, and tests conjugacy invariance. Run `python3 check.py` with NumPy. Finite tests alone do not certify the universal claim. The independent audit has not been performed, and no human certification is asserted.

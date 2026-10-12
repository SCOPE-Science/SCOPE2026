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

The proof is unbounded and symbolic. Its lattice checks are
\[
D=xe+yf=xO+(x+y)F,
\]
\[
D^2=2xy,\qquad D\!\cdot\!F=x,\qquad D\!\cdot\!O=y-x.
\]
The only integral isotropic rays in \(U\) are the \(e\)- and \(f\)-rays; only the \(f\)-ray is nef because \(e\!\cdot\!O=-1\). The only \((-2)\)-classes are \(\pm(e-f)\). These identities reduce the cited K3 base-divisor and very-ampleness criteria to \(x=1\) and \(x=2\), respectively.

The accompanying script then performs an independent arithmetic consistency replay for \(2\le d\le5000\). It checks the coprime-factor-pair count, the stated base-point-free and very-ample count formulas, and the minimal thresholds \(D^2=12\) and \(D^2=24\). A finite replay is not used as a proof for the all-\(d\) assertion; the prime-power allocation argument in the proof establishes the count formulas for every \(d>1\).

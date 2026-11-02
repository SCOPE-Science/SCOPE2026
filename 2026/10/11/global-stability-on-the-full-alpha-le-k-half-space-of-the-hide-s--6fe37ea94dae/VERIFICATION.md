---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Algebraic verification and limits

The displayed ODE and \(V=\alpha x^2+(y-\alpha/k)^2+\alpha\beta z^2\) give exactly
\[
\dot V=-2\alpha(k-\alpha)x^2/k-2k(y-\alpha/k)^2-2\alpha\beta b z^2.
\]
Direct symbolic expansion leaves the zero polynomial for the difference of both sides. At \(\alpha=k\), the derivative zero set is \(\{y=1,z=0\}\). Any invariant trajectory in this set satisfies \(0=\dot z=x\), hence is the equilibrium. Positivity/coercivity of \(V\), global continuation, and LaSalle's invariance principle complete the proof.

**Specific defect in the earlier literature:** the printed energy \(W=[\alpha x^2+(y-\alpha/k)^2+z^2]/2\) has derivative \(-\alpha(k-\alpha)x^2/k-k(y-\alpha/k)^2-bz^2+(1-\alpha\beta)xz\). Substituting \((\alpha,k,b,\beta;x,y,z)=(1,2,1,3;-2,1/2,1)\) yields \(+1\). This invalidates that proof's universal nonpositivity step but not its stated strict-interior theorem, which is re-proved by the corrected energy.

No numerical experiment or external attestation is represented as proof; the full theorem depends on the exact identity and invariance argument. The strict parameter region is explicitly covered by Li (2022), Theorem 2.2. Other historical equivalent boundary proofs cannot be ruled out absolutely.

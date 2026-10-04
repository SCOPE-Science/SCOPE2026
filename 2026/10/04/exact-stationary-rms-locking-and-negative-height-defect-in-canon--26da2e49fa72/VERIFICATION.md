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

For an invariant compactly supported probability measure \(\mu\), the identity \(\int LF\,d\mu=0\) was applied to exactly three test functions.

1. For \(F=z\), direct differentiation gives \(Lz=1-xy\), hence \(\int xy\,d\mu=1\).
2. For \(F=y^2/2\), direct differentiation gives \(L(y^2/2)=xy-y^2\), hence \(\int y^2\,d\mu=1\).
3. For \(F=xy\), direct differentiation gives \(L(xy)=x^2-xy+y^2z\). Combining this with the first two identities yields
\[
\int y^2z\,d\mu=-\int(x-y)^2\,d\mu.
\]

The equality case was checked dynamically. If the square defect vanishes, the invariant support lies in \(x=y\). Compact support excludes the orbit \((0,0,z+t)\); invariance then forces \(z=0\), followed by \(x^2=1\). Thus only the two equilibria remain.

No numerical trajectory, finite census, floating-point estimate, or unproved asymptotic step is used. The result does not assert that a chaotic invariant measure exists or is unique.

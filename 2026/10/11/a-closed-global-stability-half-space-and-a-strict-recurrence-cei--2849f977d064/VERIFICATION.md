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

The proof uses exact algebra and invariant-set arguments. `verify.py` reconstructs the centered polynomial vector field and verifies coefficient-by-coefficient that
\[
\frac{d}{dt}\frac{x^2+Y^2+z^2}{2}=s x^2-bY^2-cz^2,
\]
where \(Y=y-1/b\) and \(s=1/b-a\). It also checks that the Aybar specialization \(b=c\), \(a=c+1/c\) reduces the derivative to \(-c(x^2+Y^2+z^2)\).

For \(a>1/b\), the proof derives the analytic inequality \(\dot V\le-2mV\) with \(m=\min\{a-1/b,b,c\}\). For \(a=1/b\), no numerical approximation is used: properness of \(V\) gives compact forward sublevel sets, and the zero-derivative set can contain a complete forward orbit only when \(x=Y=z=0\).

The strict recurrence ceiling uses the exact variation-of-constants formula for \(\dot y+by=1-x^2\) and bounded completeness to pass to the infinite past. Equality forces the entire past \(x\)-history to vanish and hence forces the equilibrium by the differential equations and uniqueness.

The checker verifies the polynomial identities only; it does not replace the LaSalle or bounded-complete arguments. The result does not classify parameter triples outside \(a\ge1/b\).

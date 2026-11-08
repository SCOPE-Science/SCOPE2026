---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

On the balanced scroll ruling curve, the rank-d orthogonal projector is block-diagonal with d copies vv^T/s, s=Σ_{j=0}^n t^{2j}. Squared chordal distance to rank-d Q is d−N_Q(t)/s(t), with W=N′_Q s−N_Q s′ of maximal degree 4n−2 since degree-(4n−1) terms cancel and the leading nonzero coefficient is −[t^{2n−1}]N. s has simple roots in characteristic zero; the Wronskian first-jet linear system has no basepoints and a generic numerator gives 4n−2 distinct finite roots away from s=0. Restricted block projectors from coprime f,g∈V_n yield N=(d−1)f²/<f,f>+g²/<g,g>; differential tangent f f_perp+g g_perp has dimension2n, and the numerator N lies outside it for d≠0, so the map to P(V_{2n}) is dominant. The cut locus for these data is f(t)g(t)=0; coprimality of W with fg defines a nonempty open set and extends to general full-rank Q. This reconstructs the characteristic-zero unrestricted proof. Independent sympy n=2,d=3 witnessed degree 6, gcd(W,W′)=1 and gcd(W,sfg)=1; finite-field checker in checks/verify.py covers samples n=2..7 and d=2,3,5 but not genericity in all parameters.

## originality

PASS

Qualified PASS limited to the generic rank-d PROJECTOR-data critical count 4n−2 and cut-locus avoidance for balanced scroll ruling curve. The numerical ED degree 4n−2 is explicitly prior art and not credited as new. Full primary Section 4 of the highly relevant 2026 article is inaccessible; its potential broader theorem remains a substantial priority risk, and numerical equality of degrees alone is not a proof of equivalence.

## value

PASS

The rank-d projector constraint and avoidance of the algebraic cut locus are meaningful in nearest-subspace optimization; an ED-degree computed for unrestricted ambient data need not equal the Grassmann critical-point count. A complete formula for all balanced scroll ruling curves plus a geometric explanation of equality is a reusable enumerative statement beyond the already known ED count, despite being a special balanced family.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

For odd prime-power q, the coefficient-marked genus-four hyperelliptic family y^2=(x^2+1)G_{u,v}(x) has smooth locus v*(u^2-4v)*(1+u+v)!=0, cardinality q^2-3q+3. Factor G=P_{t1}P_{t2} where t_i solve t^2+u*t+v and P_t=t(x^2+1)^2-4x^2. Each P_t has roots expressed using sqrt(t) and sqrt(1-t), with exact splitting field Fq(i,sqrt(t1),sqrt(1-t1),sqrt(t2),sqrt(1-t2)); no roots collide on smooth locus. For split quadratic t_i, all four roots rational iff both character tests +1, otherwise 2^2; for irreducible t_i, norm characters chi(v),chi(1+u+v) classify 2^4 versus 4^2 over eight roots. The independent x=±i block contributes 1^2 or 2 according to epsilon=chi(-1). Counting good t via sum chi(t(1-t))=-epsilon and conjugate pairs over Fq² yields four coefficient frequencies comb(g,2),g*(q-2-g),comb(q-2-g,2)+(q-1)*(q-3)/8,3*(q²-1)/8, g=(q-4-epsilon)/4. These sum q²-3q+3 and give splitting degrees <=4 and exact Frobenius fixed branch points. For genus four, Jac[2] invariants are Frobenius-invariant even subsets of ten branch points modulo complement; the all-even-cycle alternating-complement option is impossible because length five is odd, yielding stated orders 256/128,64/32,16,4 depending on epsilon. Independently counted rational branch roots and four frequency types directly in all valid coefficient pairs over q=3,5,7,11,13. This is all odd prime powers by character algebra, not finite extrapolation; geometric isomorphism classes, zeta functions and Newton polygons are out of scope.

## originality

PASS

Qualified PASS for the four-type finite-field Frobenius frequency table, splitting degrees, and rational 2-torsion in the explicitly marked family. Bruin–Kulkarni supplies the EXACT SAME genus-four family and Jacobian-square isogeny (these are not new). The relevant accessible original Example 7.3 does not state these global coefficient-frequency and torsion classifications; broad hyperelliptic character theory gives tools, not a seen equivalent final statement.

## value

PASS

A complete, exact arithmetic stratification of an already-important genus-four Jacobian-square family, including Frobenius types, frequencies, rational Weierstrass counts and rational two-torsion, is a natural finite-field invariant used in arithmetic geometry. The new distribution is not equivalent to the previously known decomposition-isogeny statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

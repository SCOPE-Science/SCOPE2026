---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The fixed nonsplit quadric has a 16-dimensional cubic quotient, hence exactly 65535 nonzero cubic sections. Its rational projective automorphism group S5 acts on those sections; exact ideals Q,F and Jacobian rank-drop minors on three affine charts test geometric smoothness, not mere F2 rational points. Conic-plane binary sextic must be square of squarefree cubic (char2 discriminant ad+bc), while tangent-plane conjugate-line criterion a=0,b≠0,c=0 yields proper reduced triple double-contact. Inspected finite-field code and 683-row orbit_certificate.tsv; independent weighted aggregation matches 683 ambient orbits, 254 smooth orbits (27060 sections), tau sections (10300,12810,3600,350), orbit counts (96,120,32,6), all 33 joint strata, 396 five-point smooth curves and six extremal orbit masks. Separately checked geometric smoothness via independent Sympy Groebner on two singular masks and all six extremal smooth masks. This is exact finite classification with a source-embedded complete enumerator; full independent re-enumeration was NOT performed.

## originality

PASS

Known abstract genus-four model census and finite-field moduli point counts do not state the 33-stratum embedded proper tritangent spectrum, although equations could enable computation. Best-of-knowledge; checked source and access limitations recorded in residual_risks.

## value

PASS

Proper tritangents of canonical genus-four curves are natural theta-contact objects. Splitting the rational planes into conic and quadric-tangent types on a nonsplit binary quadric and listing all 33 strata, six extremal S5 orbits and the full-five-rational-point obstruction provides a motivated complete finite classification not merely an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.

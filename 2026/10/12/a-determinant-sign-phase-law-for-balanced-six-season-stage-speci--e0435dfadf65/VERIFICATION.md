---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The 20 binary length-six words with three J=L diag(u,1) and three A=L diag(1,v) split under rotation into classes of sizes 6 blocked, 6+6 mixed, 2 alternating. The mixed traces agree by two-letter 2×2 reversal trace identity. All products share determinant (ad−bc)^6(uv)^3. Independent symbolic expansion with six free variables verified TM−TB=−bc(ad−bc)(d+au)(a+dv)(1−uv)^2 and TT−TM=−bc(ad−bc)(bc(1+uv)+a²u+d²v)(1−uv)^2. All other factors are strictly positive under the full hypotheses, and for positive 2×2 products the Perron root increases strictly with trace at fixed nonnegative determinant. Independently enumerated the 20 schedules and four orbit classes and checked equality of all 20 determinants. Therefore sign(det L) determines the complete strict ranking, with equality exactly det L=0; the rational biological witness crosses unit growth. Finite parameter tests were supplemental and are not an infinite proof.

## originality

PASS

Greene’s trace-reversal theorem and Schneider’s four-necklace analysis cover the cyclic/reversal combinatorial ingredients; they do not, in material inspected, determine the specialized stage-treatment trace-gap sign factorization. Mertens–van den Bosch–Heesterbeek 2002 studies seasonal ordering in structured crop rotation but its complete text was inaccessible, so overlap remains material rather than dismissed. A closely related unpublished or historical model-specific computation could cover the phase law.

## value

PASS

This is a complete and sharp six-season schedule classification, not a generic order-dependence observation: exact determinant-controlled reversal independent of treatment intensities, and a feasible biological example where reordering identical numbers of interventions changes extinction-vs-growth. Natural applied matrix-product gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

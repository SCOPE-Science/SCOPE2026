---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Using the known symmetric-gate exact mean time T_h(x), independently checked the two expressions and root equations. B(x)=(exp x-1)/x² is uniformly coercive; rare-limit E_h=T_h-1/(2h) is bounded below by B. The compact C² expansions H+hJ and B+exp(x)/(x sqrt(2h)) imply convergence of all global minimizers to unique nondegenerate roots x_s=1.6244614336663, x_b=1.5936242600400; local implicit-function uniqueness follows at sufficiently small/large h. IFT expansions x_s-0.2262351716h+O(h²), and x_b-x_b/sqrt(2h)+O(h^-1) have opposite sides of x_b, forcing nonmonotonicity without all-h uniqueness. Independent numerical minimization at h=.0005,.001,.01,100,10000 agreed with limiting directions and scales. Finite samples do not prove global branch behavior.

## originality

PASS

Best-of-knowledge acceptance for the stated narrowly quantified original contribution; known antecedents and overlapping results explicitly excluded. Published mathematical records were queried by equivalent statements; primary literature inspected to the material actually accessible, without implying that lack of a hit guarantees novelty.

## value

PASS

A constant active duty cycle of one half isolates target temporal correlation from equilibrium occupation; reentrance of the optimizer under this natural controlled perturbation is a nontrivial optimization phenomenon with sharp endpoint calibration. It is not a new MFPT formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.

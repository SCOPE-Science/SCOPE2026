---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

I reconstructed the phase matrix using polynomial spectral projectors of the six-cycle adjacency matrix, rather than evaluating the bundled formulas alone. The two proposed cosines satisfy c²=(1−sqrt(6)/2)c+sqrt(6)/4, and their weighted mean is (1−sqrt(6))/10. This gives the moments through degree four by the two-term recurrence; exact substitution into the four distance classes gives 1/6 in every case. The cosines are distinct and in (−1,1) (e.g. sqrt(6)<2.5, sqrt(10)<3.2 and sqrt(6)>2.2); the weight perturbation has magnitude less than 1/2. Equality of the distance-one and distance-two probabilities forces c=0,1,−1/2, giving distance-one probabilities 1/9,0,0. Translation and reflection cover all entries. Integral eigenvalues give a common 2π shift, so both times can be put strictly beyond any cutoff.

## originality

PASS

The supported distinct claim is the exact two-atom witness, giving minimum support two. The singleton obstruction is prior work, arbitrary-support existence for C6 is explicitly covered by a distinct Resultary crown-graph result with a four-atom witness, and lateness is a periodicity consequence. The inspected stronger-looking statements do not settle the two-point feasibility question.

## value

PASS

The number of time settings is a natural exact resource for random-time quantum mixing. C6 is a concrete case known to fail at a single time and known to succeed with a larger support. The positive exact witness closes the gap at the first possible support size, rather than just recomputing nonuniformity or showing approximate flattening. A future comparison of support bounds can use this sharp example directly.

The dated certificate retains the supplied scientific assessment, sources and limitations.

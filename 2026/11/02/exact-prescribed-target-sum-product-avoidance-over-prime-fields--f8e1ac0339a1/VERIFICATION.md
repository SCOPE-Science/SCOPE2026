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

The source correctly represents simultaneous forbidden repeated-operand sums/products as an independent-set graph with loops at c/2 and square roots of c. Projective completion by two involutions s(x)=c-x,m(x)=c/x gives alternating components. The semisimple ratio h=sm partitions non-fixed points by PGL order; parity and square status determine the looped paths. The unipotent c=4 case is separately handled. Counting inverse-paired eigenvalue ratios in split/nonsplit 2-adic tori gives the claimed E_p. Independent networkx graph independence and direct projective composition checks agreed on 420 target cases in 15 prime fields <=59. Finite agreement is not a universal proof; the projective orbit argument supplies arbitrary p.

## originality

PASS

Tang's 2026 c=1 case is structurally related but has h projective order three and does not entail variable c spectra or E_p. General finite-field sum-product growth controls cardinalities, not avoidance of a specified target. Resultary semantic search for target-specific dihedral orbits found no direct dominating result. Best-of-knowledge pass with residual possibility of older equivalent Möbius/dihedral graph classification.

## value

PASS

For a natural generalization of the recently posed fixed-target problem, it completely determines a genuinely target-dependent infinite family and exact frequency of exceptional residues, with a structural explanation; the result is not a renamed c=1 instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.

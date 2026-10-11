---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

ML theoremhood is co-r.e. and non-theoremhood in recursively axiomatizable Skvo is co-r.e., so their intersection is \(\Pi^0_1\). For a fixed strongly aperiodic tileset \(A\), a product \(W\otimes A\) tiles exactly when \(W\) tiles and cannot tile periodically, by coordinate projection and pairing. The primary source's two canonical-formula equivalences then give \(W\) tiles iff the product formula lies in \(\mathrm{ML}\setminus\mathrm{Skvo}\). The construction is effective, so ordinary Wang tileability supplies many-one hardness.

## originality

PASS

The primary 2026 paper proves undecidability of ML and Skvo and obtains one separator from any fixed aperiodic tileset, but it does not classify the entire set difference. Pawlowski classifies ML theoremhood, not the difference. The audited product with a fixed strongly aperiodic factor uniformizes every ordinary tileability instance into a separator while preserving tileability, which is the missing many-one hardness step.

## value

PASS

The result upgrades mere proper inclusion and separate undecidability results to a sharp completeness classification of the full logical separation set. That is a natural metalogical invariant with a clear uniform reduction, not an arbitrary special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.

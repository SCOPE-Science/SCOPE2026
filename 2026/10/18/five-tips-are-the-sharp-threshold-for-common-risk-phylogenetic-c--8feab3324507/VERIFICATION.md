---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With rooted Faith PD (zero on an empty survivor set), the change on an edge of length l subtending m tips on the protected path is l times the probability that all m initially go extinct, l q^m. Divide total gain by the common positive q. A singleton at the root has score H, strictly above a competitor with a positive nonpendant path edge. At n=2 both root children are singleton, so both tie: the uniqueness wording in Proof Step 2 needs this qualification, but the stated fixed-optimum assertion holds. For 2+2 the paired score difference is (b-a)(1-q); for 2+3 the triplet outgroup C strictly dominates D,E by (t-b)(1-q), and C minus either A or B is (1-q)(a-b(1+q)). This gives precisely the open switching region, its tie, and strict constant winners at a=b and a=2b since q=0,1 are excluded. These splits exhaust the binary possibilities through five tips. Independent exact replay /workspace/branches/replay_3.py enumerated actual before-and-after expected PD over all 32 outcomes for the positive ultrametric H=4 witness: at q=1/4,1/2,3/4 the optimizer sets were respectively C, ABC, AB. That replay verifies the witness, not the universal proof. The frozen verifier was inspected, not run.

## originality

PASS

The novel claim assessed is the global-optimum boundary for a single change under independent identical risks and ultrametricity, not the HED score, the gain identity, or heterogeneous-risk rank sensitivity. The examined related records about unit edges or two switches do not establish this single-switch global classification. This is a best-of-knowledge comparison of inspected material, not a general priority determination.

## value

PASS

This tests a natural expectation that equal risks and a molecular clock might fix the best conservation priority. The first possible switch, full sharp parameter interval and globally optimal tie sets supply a reusable exact benchmark, not just a crossing between two nonoptimal tips or a new name for HED. It gives no policy prescription for taxa with heterogeneous or dependent risks, uncertain phylogeny, or different intervention costs.

The dated certificate retains the supplied scientific assessment, sources and limitations.

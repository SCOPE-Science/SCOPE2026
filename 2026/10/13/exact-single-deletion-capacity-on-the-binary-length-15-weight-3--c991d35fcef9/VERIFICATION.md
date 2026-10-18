---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The complete explicit 37-row code_triples.csv was inspected. A separate checker generated the distinct one-deletion descendants from original ordered binary strings, verified pairwise disjoint descendant sets for all 37 words, verified the dual fractional q(y) coverage >=1 for each of the 455 candidate weight-3 input words, and summed all output weights to 37. The analytic run-case upper argument correctly treats three singleton runs, a double plus isolated run, and one triple run; total dual mass (78+26+7)/3=37. Primal construction and dual bound match exactly.

## originality

PASS

Cullina–Kulkarni–Kiyavash establish optimal constant-weight deletion code graph colorings, not the independence number; their modified VT classes at this specific n,w have 35 words, while this code has 37. Kulkarni–Kiyavash establish a general fractional transversal method but not the specific optimized q or exact capacity 37. No exact 37-entry table was located by targeted searches; narrow finite historical risk remains.

## value

PASS

A sharp exact one-deletion capacity in the natural constant-composition weight-three layer at length 15 is independently useful and separates chromatic optimality from maximum code size. An explicit 37-word witness with matching all-candidate rational dual certificate settles this finite packing problem nontrivially, without claiming broader census or decoding guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.

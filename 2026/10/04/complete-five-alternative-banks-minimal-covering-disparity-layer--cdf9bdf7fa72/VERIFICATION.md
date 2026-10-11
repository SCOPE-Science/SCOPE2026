---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

I independently enumerated all \(2^{10}=1024\) labeled tournaments on five alternatives and recomputed both solution concepts from their definitions. The Banks set was obtained from inclusion-maximal transitive subtournaments, with transitivity checked by absence of directed 3-cycles; the minimal covering set was obtained by direct external covering-stability testing. This reproduced the exact order-five histogram \((1,1):320,(3,3):520,(5,5):64,(4,3):120\), with exactly 120 disparities, all satisfying \(MC(T)\subsetneq BA(T)\). Canonicalization under all \(5!\) relabelings gave one canonical code, occurring 120 times, hence one asymmetric isomorphism class with full orbit size 120. This independently verifies the package's finite classification rather than relying on its saved output.

## originality

PASS

The 2015 disparity paper was inspected in an author-hosted full PDF. It reports exhaustive generation of non-isomorphic tournaments through order ten, gives disparity index five for Banks versus minimal covering, and displays a five-alternative witness with the 4-versus-3 choice sets. Those published statements establish the threshold and a witness but do not state that every order-five disparity is the same isomorphism class, nor the labeled count 120 and probability 15/128. Resultary and targeted exact searches did not locate a published uniqueness/census theorem. Thus the threshold is prior work, while the complete threshold-layer classification survives as original to the best of current evidence.

## value

PASS

The first order at which two standard tournament solutions separate is a natural structural boundary. Classifying every tournament on that first layer, rather than merely exhibiting a witness, shows that the discrepancy has a unique symmetry type and a fixed containment pattern. That complete minimal-layer classification is mathematically useful and not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

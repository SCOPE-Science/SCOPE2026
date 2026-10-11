---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exact finite classification is internally coherent and independently reconstructible. The assigned program enumerates all monotone Boolean functions on five labeled players, removes the two constant functions to obtain 7579 simple games, tests the desirability relation directly and obtains 3285 labeled complete games, then canonicalizes minimal-winning-coalition antichains under all 120 player permutations to obtain 117 classes. A second route enumerates nonincreasing integer weights in the bounded range used by the certificate and all quotas; its canonical class set equals the complete-game class set exactly, so the weighted classification is not inferred from the first route alone. Exact rational Deegan--Packel scores give 695 labeled violations and 17 isomorphism classes. The minimum number of minimal winning coalitions among violations is three; 60 labeled games attain it and form one class. The representative \([8;5,3,2,1,1]\) has minimal winners \(\{1,2\},\{1,3,4\},\{1,3,5\}\), player 2 strictly dominates player 3, and the normalized scores are \((7/18,1/6,2/9,1/9,1/9)\). A fresh independent reconstruction reproduced \((7579,3285,117,695,17,3,1)\) and separately reproduced the equality of the 117 complete and bounded-weight canonical classes. The finite exhaustive computation is the proof because the theorem itself is exactly a finite five-player census.

## originality

PASS

Freixas and Kurz explicitly study Deegan--Packel local monotonicity, define the same desirability/dominance framework, and establish that Deegan--Packel can fail local monotonicity; their full paper studies classes, costs and small-player examples rather than an exact isomorphism census of all five-player weighted games. The known total of 117 five-player weighted classes is prior enumerative data, but that total does not identify which classes violate Deegan--Packel monotonicity or prove the unique three-minimal-winner boundary. Current Resultary searches using Deegan--Packel, five-player, local-monotonicity, 17-class, and minimal-winning-coalition formulations did not return a prior record with this exact classification. The contribution is therefore the violation census and its sparsest structural class, not the known onset of failure or the known total number of games.

## value

PASS

Five players are the first natural size at which Deegan--Packel local monotonicity can fail, making the complete classification at that boundary mathematically motivated. The exact fraction 17 of 117 and the unique sparsest three-minimal-winner class sharpen an existence result into a reusable structural census. This is meaningful finite work under the audit standard: it is exhaustive on a canonical first-failure domain rather than an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.

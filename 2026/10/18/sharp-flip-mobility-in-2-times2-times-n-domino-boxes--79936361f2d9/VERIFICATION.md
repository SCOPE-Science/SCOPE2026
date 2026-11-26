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

The reachable plugs starting at the empty boundary are only the empty set, adjacent pairs, and the full set: a full plug forces an empty successor, and an adjacent pair forces either empty or its complement. Thus cutting exactly at empty plugs gives the unique monomer/full-block/alternating-tube decomposition. A square contributes once when it contains opposite matching edges. The internal block counts (1, 4, 2 for a length-two tube, and m-1 for a longer tube) and the common-ring-edge junction count exhaust the three square orientations. The lower bound is the sum of the 2m/3 bounds; equality at length divisible by three singles out length-three tubes and requires A_next != A^c, giving 4 times 3^(k-1). The residue constructions close the rounded bound even at n=1,2. The upper bound uses 3m-2 per block and two per junction; a tube has a strict deficit and a full block at an external junction cannot contribute two. This leaves precisely the uniform layer pairings, plus the isolated full block at n=2. The sixteen reachable layer types count each tiling once and assign each cap and interface exactly once, including the n=1 empty power. Independent direct matching enumeration agrees with both archived full histograms for n=1,...,8. To replay, recursively pair the first unmatched cube with each available neighbor and count flippable unit squares in all three orientations at the leaves; compare the resulting exact histograms with direct_output.txt and transfer_output.txt. The all-n proof is the block and layer argument in RESULT.md lines 25–72, not extrapolation.

## originality

PASS

The same thin boxes were already known to be flip connected, and layer/plug transfer and enumeration are related frameworks. The compared statements do not cover the number of immediately available moves as a random variable over tilings, its two sharp extremes and equality structures, or its weighted enumerator. No matching exact record surfaced in the bounded catalogue inspection; that is not proof of priority.

## value

PASS

The established connectivity of the natural face-flip graph does not indicate the available branching at each tiling. The two exact degrees distinguish high- and low-mobility regions and show nontrivial length-three rigidity at the minimum. The transfer formula makes the full local-degree distribution computable for arbitrary lengths without building the reconfiguration graph. These are useful local structural facts for studying flip walks, not claims about distances, mixing, or connectivity novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.

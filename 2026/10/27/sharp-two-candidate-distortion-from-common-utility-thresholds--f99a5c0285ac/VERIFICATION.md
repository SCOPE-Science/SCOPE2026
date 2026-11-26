---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two reported bins intersect after reflecting B's bin through x↦1−x. The closure of a feasible interval has length at most w, including an isolated cut report (length zero) if the tie convention creates one. Therefore the mean utility X lies in [L,U] with U−L≤w. The extreme competing welfare ratios for the two possible choices are bounded by max(1,(1−L)/L) and max(1,U/(1−U)); zero denominators are handled by taking the other choice. Comparing them reduces to L+U≥1 for choosing A, and the selected candidate's mean is then at least (1−w)/2. Pairing a widest open cell with its reflected open cell gives one report profile whose compatible means approach (1−w)/2 and (1+w)/2; thus whichever deterministic winner is fixed, one endpoint sequence enforces the claimed supremum. This is a worst case over all finite n, not an equality claimed separately at every fixed n. At most 2t+1 cells are possible, so equality in w≥1/(2t+1) requires the full equally spaced partition. Each reflection pair must supply exactly one original threshold and this condition is sufficient, giving precisely 2^t choices and loss 1+1/t. The frozen exact-rational checker was inspected, not run; it checks only bounded cell profiles and the indicated finite optimizer selections.

## originality

PASS

The same shared-threshold elicitation model is present in prior work, but the inspected same-model general theorems and other located formulations do not determine the fixed-threshold binary minimax loss, its two-voter lower bound, or the exact finite threshold-design optimum with all optimizer sets. This is a bounded comparison, not a priority guarantee.

## value

PASS

Binary choice is the basic common-winner case, and choosing a finite number of shared thresholds has a direct information-design purpose. The result supplies both a worst-case price for any prescribed thresholds and a sharp design prescription, including the exact penalty 1/t and all optimal choices. The two-voter witness explains why increasing the allowed population size is unnecessary for the minimax obstruction. These are precise quantities the general order bounds do not supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.

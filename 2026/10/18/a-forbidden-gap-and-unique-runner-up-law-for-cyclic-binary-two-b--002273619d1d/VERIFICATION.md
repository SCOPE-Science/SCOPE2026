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

For fixed composition, moving the first bit to the end changes the scattered 01 count by nw_i−b, so the height profile gives the exact rotation spread. Coprimality makes all n height residues distinct. Rotating to the unique minimum normalizes it to 0. Range n−1 forces the standard residue choice and hence the upper mechanical (Christoffel) word; range n repeats residue zero at its endpoints and is impossible. Range n+1 forces precisely the lift 1→n+1. At the lift the predecessor has residue b+1 and the successor a+1; a,b≥2 ensures that the entering and exiting steps swap from −b,+a to +a,−b and all other steps are unchanged. Closure gives exactly b ones. The mean over all cuts is ab/2, by counting the sum of the one positions in the normalized representative; the lift increases the mean height by 1 and gives the asserted two holes. A shorter cyclic period would repeat the rotation counts, so both necklaces have n representatives. An independent direct count (branches/e3de86da-8de0-4e43-bbba-ede5e6e13768/independent_check.py and independent_check_full.txt) covered 44 parameter pairs, 33,122 words and 457,898 rotations through n=15, reproducing the spectra and 88 extremal necklaces. The uploaded checker was read, not executed; the height argument proves the unbounded claim.

## originality

PASS

The supported distinct contribution is the forbidden spread and unique next rotation class, with its exact punctured spectrum and explicit representative. Rotation-count distinctness, Christoffel balance, and familiar minimum-class regularity overlap with existing work. The closest same-statistic variance result supports the minimum case, not the exact range gap or constrained lift for the next case. No earlier or separate covering statement for that addition was found in the bounded comparison.

## value

PASS

For the natural scattered-pair statistic, the result identifies the entire first departure from the balanced necklace, not just a stability estimate or a small-case table. The discrete gap, uniqueness, and explicit change of two steps explain how the smallest attainable imbalance arises at every allowed composition.

The dated certificate retains the supplied scientific assessment, sources and limitations.

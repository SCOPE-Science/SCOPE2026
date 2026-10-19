---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

## Mathematical checks

The argument starts from the explicit ruler representation \(Z_n[j]=1+\nu_2(j)\) and proves that every factor with largest letter \(k\) appears in each of the identical intervening \(Z_k\) blocks, crossing their unique \(k\) positions. Therefore every such factor coverage contains the entire \(k\)-letter position set. The exact minimal-coverages characterization and all-attractor enumeration follow without computational extrapolation.

The minimum-span argument uses the unique occurrence of the largest letter, the two closest occurrences of the next-largest letter, and the occurrence counts in the intervening \(Z_{n-2}\). Edge cases \(n=1,2\) are stated separately or checked in the proof.

## Reproducibility

Run `python3 check.py` with the Python 3 standard library. It enumerates all distinct factors and their true position coverages, reduces the coverage inclusion order to its minima, checks that these agree with the one-letter coverages, and checks every size-minimal attractor for orders \(1\) through \(6\). It separately counts minimum-span solutions. The frozen output of this actual execution is `check_output.txt`.

## Limits

The finite checker covers \(2^n-1\) positions for \(1\le n\le6\); the all-order result rests on the explicit proof, not on extrapolating these experiments. Literature overlap was checked against recent primary texts and published record descriptions, with residual risk of unindexed equivalent statements. No independent audit or external certification is claimed.

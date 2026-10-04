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

The bundled `verify.py` is a complete exact checker for the finite claim. It performs these checks from first principles:

1. Enumerates all \(2^{16}-1=65535\) nonempty subsets of \(\mathbb Z_4\times\mathbb Z_2^2\).
2. Computes character zeros using exact counts of the phases \(1,i,-1,-i\); no floating point is used.
3. Tests spectrality by exhaustive clique search for a translated spectrum containing \(0\).
4. Tests tiling independently by exhaustive clique search for a translated complement containing \(0\).
5. Asserts equality of the two predicates for every subset and the exact size counts \(16,120,1436,1574,1\).
6. Enumerates every automorphism by possible generator images and bijectivity, obtaining exactly \(192\).
7. Combines these with all \(16\) translations and verifies the affine-orbit counts \(1,3,10,12,1\).

Reviewed replay output:

`VERIFY_OK subsets=65535 accepted=3147 sizes=16,120,1436,1574,1 aut=192 affine=3072 orbits=1,3,10,12,1`

The verification proves only the stated finite classification. It does not extrapolate to larger groups.

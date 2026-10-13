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

`verify.py` uses only the Python standard library. It rebuilds all \(32\) vertices of the five-cube, represents each ordinary coordinatewise pair sum as a base-three integer, and enumerates every \(B_2\)-subset containing \(00000\) in increasing word order. The acceptance invariant includes self-pairs, so repeated summands are checked exactly as required by the definition.

The normalized exhaustive search returns maximum size \(12\) and \(72\) normalized maxima. The verifier then applies all \(32\) xor translations, deduplicates to \(192\) labeled maxima, checks every one directly, and applies all \(3840\) Hamming isometries to a representative. The resulting orbit has size \(192\), equal to the complete census, and the direct stabilizer count is \(20\).

The same replay checks coordinate one-counts \((6,6,6,6,6)\), exactly one antipodal pair, and Hamming-distance counts \((5,20,30,10,1)\) for distances \(1\) through \(5\). `census.json` stores every labeled maximum, and the verifier compares it with the regenerated census.

The proof is finite and exhaustive only for dimension five. It does not extrapolate the computation to larger dimensions, and the literature comparison is not itself a proof of novelty.

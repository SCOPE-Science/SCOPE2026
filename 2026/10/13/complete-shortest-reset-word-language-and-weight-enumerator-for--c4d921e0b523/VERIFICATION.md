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

# Verification and reproducibility

## Proof checks

The theorem is proved for every \(n\ge2\). The proof uses (i) the unique possible shortest-reset terminal image, (ii) the Frobenius obstruction for return cycles of lengths \(n-1\) and \(n\), (iii) the trajectories starting at \(n-1\) and \(n-2\), and (iv) a target-set containment invariant at each position of every admissible word. The exceptional \(n=2\) case is checked directly. The count follows only after both necessity and sufficiency are established.

## Standalone finite checks

- `python3 verify_dp.py` passed: exhaustive subset-image dynamic programming over the binary alphabet for \(2\le n\le12\) reproduces the entire letter-count distribution at the shortest length and confirms no shorter resets. It also checks all target-set inclusions for \(2\le n\le40\).
- `g++ -O3 -std=c++17 verify_independent.cpp -o verify_independent` followed by `./verify_independent` passed: direct enumeration of every binary input string of length \(n^2-3n+3\), for \(2\le n\le6\), agrees word-by-word with the predicted compulsory positions. This is a distinct implementation of the state update.

The measured counts for \(n=2,3,4,5,6\) are \(1,1,4,64,4096\). Neither program claims to enumerate infinitely many cases. Both programs have no non-standard library dependencies.

## Limits

The full-result correctness is supplied by the written proof; computational checks are consistency evidence only. The search for prior equivalent classifications is necessarily incomplete, and the review described in the accompanying document is not an independent audit.

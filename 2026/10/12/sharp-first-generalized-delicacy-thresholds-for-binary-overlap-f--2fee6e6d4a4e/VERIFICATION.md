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

Run `python3 verify.py` beside `certificate.json`.

The first enumerator builds overlap-free words recursively. Since its current prefix is already overlap-free, it needs only to test whether the newly appended bit completes an overlap ending at the final position.

The second enumerator is deliberately independent: for every \(1\le n\le14\), it scans all \(2^n\) binary words and checks every start position and every possible overlap period from scratch. The two generated languages are required to agree exactly.

For each complete language \(\mathcal O_n\), the verifier computes the Hamming distance from every word to every distinct word, reconstructs the entire isolation-distance histogram, and matches it to `certificate.json`. It then extracts all words at isolation distance \(3\) at length \(13\) and all words at isolation distance \(4\) at length \(14\), verifies the complete lists, and checks the reversal/complement orbit statements.

The exhaustive domain is exactly what the theorem needs: lengths below and at the claimed minima. No inference about larger \(k\) or longer words is made. Independent audit has not been performed.

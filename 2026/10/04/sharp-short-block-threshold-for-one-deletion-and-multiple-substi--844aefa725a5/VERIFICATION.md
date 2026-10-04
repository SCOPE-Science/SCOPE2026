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

The universal proof is combinatorial. Its critical implication is that deleting one fixed coordinate embeds a radius-\(s\) Hamming ball in each channel ball; disjointness therefore forces prefix Hamming distance at least \(2s+1\). The boundary construction is checked separately by the fact that distinct constant descendants have Hamming distance \(2s+1\).

`verify_short_threshold.py` independently reconstructs the channel by enumerating every deletion coordinate and every length-\(n-1\) word within Hamming distance at most \(s\). It exhaustively checks \(0\le s\le2\), \(2\le q\le3\), all positive lengths below the threshold, and the threshold length itself. Below the threshold it searches every pair of source words and confirms that no pair has disjoint output sets. At the threshold it confirms that every compatible pair has different first symbols and that all constant words are mutually compatible.

The finite checks are regression evidence only. They do not establish the theorem for untested \(q\), \(s\), or \(n\); those quantifiers are supplied by the proof in `RESULT.md`.

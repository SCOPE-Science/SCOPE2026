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

The verifier recomputes all binary subsequence counts of lengths \(1\), \(2\), and \(3\) for the two seed factors and checks their exact occurrence positions in \(\sigma^4(0)\). It also verifies a fourth-order coefficient that separates them.

For \(0\le t\le10\), it directly constructs \(\sigma^t(u)\) and \(\sigma^t(v)\), checks their occurrence in \(\sigma^{t+4}(0)\), their distinctness, and equality of every subsequence count through order \(3\).

A separately implemented transfer formula groups subsequence occurrences in a morphic image by the source blocks they use. The verifier exhaustively compares that formula with direct dynamic-programming counts for all binary source words of length at most \(5\), all nonempty binary morphism images of length at most \(2\), and every binary target of length at most \(3\).

The theorem for all \(t\) follows from the symbolic morphism-preservation argument, not from finite extrapolation.

Independent audit has not been performed.

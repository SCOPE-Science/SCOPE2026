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
# Checks performed
The proof was reconstructed from the definition, including the exact adjacent-colour counts for a red or blue edge and the parity/degree-class argument excluding two colours except at \(n=4\).

The supplied `verify.py` checks the explicit constructions for \(K_3,K_4,K_5,K_7\), checks the equitable three-part construction for \(K_6\) and every \(K_n\) with \(8\le n\le200\), and exhaustively enumerates every two-colouring of \(K_n\) for \(3\le n\le6\). The stored verifier output records a successful replay.

# Limits
The finite program does not certify the theorem for infinitely many orders. Infinite correctness rests on the written degree-sum proof and on the symbolic inequality \(2\lceil n/3\rceil\le n-2\) in the stated ranges. Literature searches cannot prove novelty; the originality conclusion remains subject to the residual source-coverage risk listed in AUDIT.json.

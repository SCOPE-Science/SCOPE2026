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

The source theorem was checked in the version first public on 2026-10-02. Its relevant inputs are the negative-doubling address map, the parity-sensitive finite-return definitions, the two symbolic left-endpoint forms, and the singleton alternative.

The proof was replayed algebraically from those inputs. For a length-\(k\) word \(w\), direct iteration of the address recursion gives
\[
\pi_{-2}(w\xi)=A_w+(-1/2)^k\pi_{-2}(\xi).
\]
When \(k\) is even, substituting \(\xi=\beta\) and \(\xi=\alpha\) into the two source endpoints gives the difference \(2^{-k}(b-a)\). When \(k\) is odd, the periodic endpoint satisfies its affine fixed-point equation; solving it together with \(\beta=w\alpha\) gives \((b-a)/(2^k+1)\).

No numerical sampling, finite enumeration, or timeout result is used. The verification does not claim a formula outside the source's weak-admissible plateau class, does not classify plateau frequencies, and does not remove the source's isolated dual-coding convention at precritical points.

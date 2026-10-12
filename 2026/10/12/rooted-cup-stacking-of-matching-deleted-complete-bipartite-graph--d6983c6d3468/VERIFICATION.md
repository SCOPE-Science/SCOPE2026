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

The result follows from the packet-counting necessity and matching-based constructive sufficiency in `RESULT.md`. Run `python3 verify_cup.py` under Python 3.9 or newer, without third-party packages; `verify_output.txt` records the output from an actual execution. The checker constructs all graph edges and shortest-path distances, enumerates legal moves over memoized occupancy vectors for all small cases, and separately validates the theorem's explicit sequences for larger parameter ranges.

The 346 exhaustive decisions cover all targets of the graphs with \(m,n\ge3\) and \(m+n\le9\); 666,192 is the **sum** of individually memoized states inspected (not a count of distinct global configurations). Constructive witnesses were checked for 6,984 successful targets on graphs with \(3\le m,n\le12\). Neither computation proves the theorem for arbitrary orders; Hall's theorem and the direct packet argument supply the infinite proof. No independent validation has been performed.

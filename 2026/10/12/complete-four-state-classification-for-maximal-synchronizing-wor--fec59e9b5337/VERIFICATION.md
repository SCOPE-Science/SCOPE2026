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

The verifier checks all \(65{,}536\) ordered labeled binary transition pairs on four states. One engine constructs and minimizes the reachable subset automaton by partition refinement. A second engine tests the exact maximality conditions independently: reachability of all non-singleton subsets followed by table-filling distinguishability of subset states. The engines agree on every automaton.

The verifier then fixes \(b(q)=q+1\pmod4\) and checks all \(256\) possible second letters. Among the \(144\) rank-\(3\) maps, exactly \(128\) are maximal and exactly \(16\) fail; the failure set is exactly the conjunction of kernel-pair antipodality and omitted/double-image antipodality.

Finally, all \(1536\) maximal ordered labeled automata are canonicalized under all \(24\) state relabelings and the letter swap, yielding exactly \(32\) classes, each of orbit size \(48\). The four-state example printed in the primary source is separately replayed.

Independent audit has not been performed.

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

# Direct verification and limits

Run `python3 verify.py` from the extracted package. The standalone program enumerates all \(\tau_i\)-orbit subsets of \(Q_n\) for \(2\le n\le5\), checks every scale \(1\le r\le n\), then compares all orbit pairs through \(n=6\). It tests orbit edge inclusion, all cross-orbit distances, and the equivalence of the full simplicial face predicates. It also evaluates the earlier Feng multiplicity formula at dimensions \(6\) through \(11\). The recorded `verify-output.txt` is obtained by executing the same script.

The computer check covers **20** scale cases, **4,028** orbit-pair comparisons and **72,946** nonempty accepted orbit-subset faces in the exhaustive cases; it terminates with `VERIFY_OK`. The unbounded assertions and PL property are proved mathematically in `RESULT.md`; finite enumeration is neither a proof for all dimensions nor a claim about ambient scale-four homology. The source theorem is Feng (2023), Theorem 24, and is not recreated by the script. Independent audit has not been performed.

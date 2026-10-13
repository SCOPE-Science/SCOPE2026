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
# Reproduction

Run `python3 verify.py` in the directory containing this file. Only the Python standard library is used. The expected final marker is `VERIFY_OK`.

The verifier enumerates all \(84\) binary linear maps from \(\mathbb F_2^k\) into \(\mathbb F_2^2\) for \(1\le k\le3\), and independently enumerates every parity matrix of lengths up to the predicted optimum (at most four) to test whether the guaranteed function separation is four. It also generates parity matrices for the full nonzero-column set in \(\mathbb F_2^s\) for \(s=1,2,3,4\) and checks *all* message differences in those instances. The odd-weight parity-label pool and the excluded hypercube matching pairs are checked for \(3\le r\le8\).

The all-parameter assertion rests on the symbolic hypercube matching upper bound and the weight-one/two/three case analysis in RESULT.md. Finite enumeration is not interpreted as a proof for arbitrary dimension. The source document comparison, although substantial, is not an independent novelty certification.

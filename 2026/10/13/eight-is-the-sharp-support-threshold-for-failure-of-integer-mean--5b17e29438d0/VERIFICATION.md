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

Run `python verify.py` using an ordinary Python 3 interpreter. All 15 rational certificates for support lengths three through seven are checked by exact integer-ratio arithmetic: for each witness \(q_0\), the script confirms \(H_{r,j}(q_0)>0\) and \(D_{r,j}(q_0)<0\). It also confirms the eight-point signs at \(34/25\) and \(11/8\), including exact printed fractions in the proof.

The exhaustive enumeration covers possible integer mean positions of a log-affine law on every contiguous subinterval of length at most seven, rather than enumerating arbitrary real-valued probability vectors. The passage from all discrete log-concave laws to log-affine extremizers uses the published discrete localization theorem [Marsiglietti and Melbourne, arXiv:2004.12005, Theorem 2.10]. The remaining parameter optimization follows from strict variance and tail-covariance derivatives. This finite computation does not itself certify the published localization theorem or scientific novelty.

The eight-point distribution is specified by a unique root of a real polynomial, not by an approximate decimal and not by assuming finite numerical root-finding is a proof. The root bracket and monotonicity certify the strict majority reversal.

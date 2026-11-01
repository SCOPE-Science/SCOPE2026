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

Run `python3 verify.py` with Python 3.10+ and SymPy. The complete, deterministic standalone program constructs all matchings for both boards, signed integral fourth-to-third boundaries, unimodular unit pivots with tracked original-column witnesses, exact integer three-divisibility checks, a small residual Smith-normal-form computation, and both mod-three boundary quotients. The recorded output is `verification_output.txt`.

The 1552 unit pivots and residual Smith factors of \(3\), repeated five times, compute source three-torsion. All sixteen residual columns are independently reconstructed in the original chain basis and divided by exactly three, giving signed integral cycles. Their mod-three classes span dimension five before and after inclusion. The full complete-board mod-three fourth-boundary matrix is formed directly from all its 4320 four-simplices, not by copying the source boundary. All 30 source vertices are included as literal ambient vertices with matching orientation.

The program verifies face counts, integer witness identities, Smith factors, modular ranks, and the final inclusion rank, and prints `VERIFY_OK` only if all assertions succeed. No claim is made for board sizes other than six, no homology outside degree three is calculated here, and the tool does not replace independent mathematical validation.

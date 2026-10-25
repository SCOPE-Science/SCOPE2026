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
# Reproducibility and scope

Run `python3 verify.py` with a standard Python installation. The program computes the Young carry transitions from their defining integer equations, independently from the proposed table, for every integer \(n\) from \(3\) through \(60\). It checks that precisely eight proposed carry states arise, that each has the two advertised outgoing edges and digit labels, that the initial leading-digit restriction is correct, that all eight states are reachable, and that the even/odd pivot sets are exact. It checks the claimed reverse-multiple path counts through even digit length \(24\) and odd digit length \(25\).

Observed result:

`VERIFY_OK: n=3..60, exhaustive legal digit-pair transitions, 8-state reachability, both pivot classes, exact counts through digit length 25`

These are finite checks, not an exhaustive search over infinitely many \(n\). The universal theorem follows from the parameter-symbolic carry equations and interval bounds in `RESULT.md`. The open-ended novelty comparison is limited by potential unlocated equivalent proofs. Independent audit and validation have not been performed.

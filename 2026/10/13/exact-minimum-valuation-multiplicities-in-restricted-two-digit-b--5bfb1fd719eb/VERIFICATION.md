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
# Reproducibility and limits

Run `python3 verify.py` in an ordinary Python 3 installation; it uses the standard library only. The recorded result in `verification_output.txt` reports 169 exhaustively compared small parameter cases, 156,645 corresponding restricted coefficients, 11,534 checked constructive witnesses over both smaller and large rows, and 35 direct integer-binomial checks. No external package, downloaded certificate, or specialized proof system is required.

Legendre factorial valuations and digit-sum valuations were compared independently for each enumerated selected coefficient. The direct integer method computes actual binomial coefficients. The infinite proof is the borrow-run classification in `RESULT.md`; limited enumeration does not certify arbitrary parameters or historical novelty. Independent mathematical validation has not been performed.

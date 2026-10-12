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

The proof is symbolic. The finite replay checks only the arithmetic facts used to identify and minimize the explicit counterexample.

Run:

`python verify.py`

Expected terminal line:

`VERIFY_OK least_counterexample=1871 smaller_form_primes_checked=72 progression_modulus=660 progression_residue=551`

The script verifies primality of \(1871\), the identity \(1871=-27^2+2\cdot27\cdot25+2\cdot25^2\), the obstruction \(11\mid935\) with \(10\mid1870\), the forced smaller composite candidates \(551=19\cdot29\) and \(1211=7\cdot173\), and an independent enumeration of primes below \(1871\) congruent to \(11\pmod{12}\) against the obstruction condition. It also checks \(551\pmod{660}\) simultaneously implies representation congruence and the \(q=11\) obstruction.

The script does not prove von Staudt--Clausen, Adams' theorem, Dirichlet's theorem, or the class-number-one fact for \(\mathbb Q(\sqrt3)\). Those are explicit mathematical inputs in `RESULT.md`.

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

# Verification of the even-kinetic skew-flow theorem

The exact autonomous system and energy domain are given in `RESULT.md`; no time change is used. Its polynomial identity \(\dot H=0\) and exact factorization \(4/3-V(u)=(u+1)(2-u)^2/3\) can be checked mechanically for each even integer \(p\ge4\). The proof of the complete theorem is symbolic and analytic, not a finite computation.

From the extracted package directory, install `requirements.txt` in a suitable environment and run `python verify.py`. The script symbolically verifies the two polynomial identities for sample even exponents, computes physical periods and mean drifts using independently implemented weighted quadrature, checks the exact balance \(I_2=2I_1\), tests approach to each asymptotic constant, brackets zero-drift levels, and integrates one representative periodic trajectory for \(p=4\). A successful complete run prints `CHECK_OK`.

The program's tested energies, exponents and ODE tolerances are **illustrations**. They do not certify nonexistence of additional zeros, global numerical error bounds, arbitrary-exponent asymptotics or priority. Infinite quantifiers, eventual signs, analyticity and finiteness rest on the explicit arguments in `RESULT.md`. Independent audit has not been performed.

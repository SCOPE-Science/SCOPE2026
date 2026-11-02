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

# Verification of the exact randomized-order stability law

The accompanying `verify.py` runs using Python 3.10 or newer and the standard library only. Actual checks executed: **193**, with result `VERIFICATION_OK 193 checks x_star 7.750259588325559 s_star 2.783928804464216`.

The program constructs the two planar step matrices in rational arithmetic and checks determinant, trace, exact fair-averaged Gram identity, and one-step conditional norm identities. For eight-step depth it explicitly enumerates each order history and checks the resulting average for several initial states and shear strengths. It checks the two strict rational stability witnesses and corroborates the cubic crossing identity, numerical crossover and threshold order on both sides.

The verified identities are finite consistency checks. The analytic proof in `RESULT.md` supplies the all-parameter, every-integer-iterate statement and proves uniqueness of the cubic crossover by calculus. The checker does not establish publication priority, general switching stability, almost-sure Lyapunov exponents, or nonlinear extensions.

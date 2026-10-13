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

# Verification and reproducibility

The mathematical theorem is proved analytically in `RESULT.md`. Its crucial equalities and inequalities are: the next-generation matrix representation; positivity of its Perron vector; the balanced-flow relative-entropy inequality; per-group Cauchy–Schwarz; equality rigidity; and the explicit fast-migration resolvent. All hypotheses are stated there and are necessary for the corresponding steps.

For an exact finite example, run `python3 verify.py` using Python 3 and only its standard library. On replay from the packaged file, the program returned `VERIFY_OK`. It calculates host shares \(s=(1/2,1/2)\), exposures \(q=(5/4,3/4)\), variance floor \(M=17/16\), the matrix \(L\), and the two-by-two migration resolvent for five rational rate parameters. It then checks the symbolic-in-rate characteristic polynomial identity by verifying both polynomial coefficients exactly: evaluation at \(M\) is \(-3/[256(\kappa+1)]\), negative for every \(\kappa>0\). The rank-one limit gives \(M\). Rational computations use `fractions.Fraction`, not floating-point tolerance.

This finite example is not an exhaustive proof for general \(m,n\); that proof is in `RESULT.md`. Literature searches and self-review do not establish unique authorship or independent validation. The manuscript is limited to strictly positive group weights and vector stationary probabilities, nonempty host use of every patch, finite irreducible migration generators and common epidemiological parameters. No separate external validation has been performed.

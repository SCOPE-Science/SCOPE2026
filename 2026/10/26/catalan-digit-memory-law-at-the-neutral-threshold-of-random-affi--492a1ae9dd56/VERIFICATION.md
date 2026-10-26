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

The standalone `verify.py` runs with standard Python 3 and uses exact integers and `fractions.Fraction`; execute `python verify.py`. Successful execution prints `PASS: 279 exact integer/rational assertions`.

For \((b,p,N)\) equal to \((2,2/5,12)\), \((3,3/5,8)\), \((4,1/2,6)\), and \((2,1/3,10)\), it propagates **all** depth-\(N+2\) finite digit words under independently selected expanding shifts and uniformly selected contractions. It directly checks the covariance of the centered leading-digit coding \(f(a)=2a-(b-1)\) at every lag through \(N\), with rational weights and no floating-point approximation. Its transition operator acts on finite digit strings, not on the auxiliary Dyck-walk model used in the proof.

The remaining assertions check Catalan convolution for indices \(1\) through \(39\), and agreement of two independently enumerated finite-variance sums for five switching probabilities and horizons \(1\) through \(40\). The arithmetic test verifies 40 lag-covariance instances, 39 Catalan identities and 200 finite-variance identities. The general theorem, the infinite correlation sum and the critical square-root asymptotic are established by the analytic argument in `RESULT.md`, not by finite checking.

The domain includes every integer base \(b\ge2\), every probability \(0<p<1\), and every nonconstant real-valued first-digit coding. The reproducibility program samples only selected rational parameters; no claim of exhaustive testing or independent mathematical audit is made.

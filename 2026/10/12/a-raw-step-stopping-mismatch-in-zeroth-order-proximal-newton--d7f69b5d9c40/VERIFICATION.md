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

`verify_zopn_stop.py` normalizes \(\varepsilon=1\) and checks all numerical identities with Python's exact rational arithmetic. It verifies:

- the Lemma 2.4 lower line-search bound \(\underline t=1/4\);
- the Theorem 3.3(i) radius ceiling \(\Delta\leq1/42\) and the choice \(\Delta=1/100\);
- exactness of the central-difference gradient on \(f(x)=x^2/2\);
- the first FISTA step \(d_0=-1/2\);
- zero subproblem residual;
- activation of the printed raw-step stopping test;
- returned point \(3/2\) and stationarity residual \(3/2>1\).

The universal statement for every \(\varepsilon>0\) is proved by homogeneity, not by enumeration. The check does not test later iterates, because the finding is a first-iteration termination counterexample. It also does not claim that the paper's numerical experiment configuration, which initializes BFGS with the identity, exhibits this witness.

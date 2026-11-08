---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For equilibrium-initialized OU with independent Poisson resets to uniform past, all one-time marginals stay N(0,D/kappa), but the joint process is not stationary. Jump product calculus for A_t=int X and H=E[A_t X_t] gives J’=2H, H’=sigma²-(kappa+r)H+(r/t)J; thus J’’+(kappa+r)J’-(2r/t)J=2sigma² with J(0)=J’(0)=0. The moment bound J<=sigma² t² selects the regular solution. Laplace transform and Kummer inversion give the stated all-T expression and its beta=1 exponential-integral limit. The three asymptotics follow from beta=2r/(kappa+r) and Kummer negative-ray expansions; boundary r=kappa gives log(T)/T. Independently differentiated the analytic expression at three parameter times to verify the ODE residual to high precision. The claim excludes CLT, almost-sure limits, and nonharmonic potentials.

## originality

PASS

Best-of-knowledge originality for the exact stated theorem only; public primary comparison and published-record semantic searches found related methods but no prior statement implying the complete final claim. This is not proof of worldwide priority. No exact time-average J(T) tabulation found; published OU integrator records concern numerical stationary bias

## value

PASS

Non-Markovian ergodic sampling is a natural observable missing from one-time Gibbs relaxation: the sharp kappa=r transition changes the integrated variance from 1/T through log(T)/T to a slower power. This is a motivated exact path statistic with physical meaning, not an arbitrary numerical parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

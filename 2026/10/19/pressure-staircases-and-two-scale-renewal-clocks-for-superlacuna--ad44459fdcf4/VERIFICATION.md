---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The positive pressure root exists uniquely for every finite penalty. Inducing an ergodic measure at markers yields a finite-mean gap marginal r, whose entropy is finite by comparison to q_j=exp(-t-pa_j); the two-sided gap code generates the induced system. Kac and Abramov reduce the pressure inequality to nonnegativity of relative entropy; equality fixes the marginal and the iid gap process. The all-zero measure has strictly smaller variational pressure. At t_n=log(n-1+s), eventual doubling bounds the normalized sum of smaller gaps by a vanishing multiple of a_{n-1}/a_n (plus a finite prefix), and the larger-gap exponential tail, even with its length factor, tends uniformly to zero on positive pressure compacts. Monotonicity brackets a_n p_n and length bias gives condensation and the mean. For the microscopic law, geometrically stopping at the next distinguished gap gives the displayed transform: after division by q_n only the j=n−1 term survives, giving s/(s+1−exp(-u)). The blocks of intervening gaps are independent. Their mean normalized at the *macroscopic* scale is (1−pi_n)/pi_n, so neighboring starts are asymptotically unit spaced. Under stationarity, conditioning on the distinguished gap containing zero (probability tending to one) gives a uniform integer offset independent of both sides; minimum rescaled separation 1 reduces vague convergence on compacts to finitely many starts and gives joint phase independence. For factorials, the lower-length normalized sum is 1/n+O(n^-2); the quadratic Taylor remainder is O(n^-2) and the upper tail is exponentially small on compact s-ranges, giving the stated signs and coefficients. A separate bisection sweep for s=.3,.5,.7 and n=40,80,160,320 checked the factorial formulas and exact-delay transform against their limits, not the spatial convergence. No uploaded code was executed.

## originality

PASS

The weighted root equation and Bernoulli inducing law are covered by prior work, as are the underlying renewal/length-bias tools. The supported distinct claim is the parameter-window scale separation: the pressure and length-bias concentration, combined with the geometric microscopic inter-start correction and its joint limit with the stationary phase, plus the factorial coefficients.

## value

PASS

The result answers what a stationary observation sees as markers become expensive: gaps with vanishing marker-conditioned probability occupy nearly all time. It identifies both the distance scale of a stationary near-lattice and a smaller nondegenerate correction tied to the second-largest relevant length, rather than merely computing an entropy root or confirming concentration numerically.

The dated certificate retains the supplied scientific assessment, sources and limitations.

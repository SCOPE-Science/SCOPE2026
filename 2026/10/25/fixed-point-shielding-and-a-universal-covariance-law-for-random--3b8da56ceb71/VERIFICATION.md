---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

With composition eta^{-1}Pi^{-1}eta Pi, A_x=1 iff eta(Pi(x))=Pi(eta(x)). If eta(x)=x, P(A_x)=f/n and fixing Pi(j)=j makes Pi(x) uniform on the remaining n-1 values unless j=x. If eta(x)!=x, the ordered distinct images of x and eta(x) give P(A_x)=g/[n(n-1)]. Conditioning on Pi(j)=j yields probability 1/(n-1) for j=x or eta(x), and (g-2+2*1_{j fixed eta})/[(n-1)(n-2)] otherwise. Bernoulli subtraction gives all six claimed covariance branches. Summing the fixed-x and moved-x row contributions g/[n(n-1)] and 2f/[n(n-1)(n-2)] yields fg/[(n-1)(n-2)]. f=0 gives each cross-pair Bernoulli independence; f=n makes A_x constant; 0<f<n gives positive diagonal covariance. When f=0, Pi=id forces C=n whereas a noncommuting Pi exists (center S_n trivial for n>=3), establishing aggregate dependence. Independent exact enumeration of all eta,Pi for n=3,4,5 checked 3438 pair covariances; finite tests only corroborate the unrestricted conditional-counting argument.

## originality

PASS

The related marginal commutator fixed-point laws of Diaconis–Evans–Graham and permutation fixed-point action laws of Diaconis–Fulman–Guralnick do not state or imply the joint moments with the same Pi. An n-cycle is a special eta, but known circular-successions distribution cannot determine these mixed covariances. Claim is the fully indexed arbitrary-partner exact matrix and surprising derangement pairwise-vs-aggregate separation; priority remains best of knowledge.

## value

PASS

The statistic C is a natural measure of a permutation commutator, and F is the most basic statistic of the same random permutation. A complete local cross-dependence classification for every deterministic eta and the exact positive covariance depending only on f distinguish genuine pairwise independence from dependence of the totals; the n>=3 family and exact boundary cases are mathematically meaningful beyond routine marginal expectations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

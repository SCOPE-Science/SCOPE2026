---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: For w_k=k^(q/p)-(k-1)^(q/p), all w_k>0, sum_{k<=m}w_k=m^(q/p), and 0<q<1. Any decreasing selected magnitude vector of sum S is a convex combination of vectors (S/j)1_{[j]}; by concavity of sum w_i x_i^q it has gauge at least S m^(1/p-1). Output of a one-block averaging V_B has norm <=S m^(1/p-1), proving exact ||V_B||=1 from the indicator witness, for real and complex scalars. For binary k,j selected ones, telescoping the same weights yields factor (k/n)^(1-1/p)*rho(j/k), rho(t)=[1+(2^(q/p)-1)t^q]^(1/q)/(1+t)^(1/p). Bound by max rho and take k=n,j/n→t to get exact limit for restricted binary inputs; no claim for full operator norm. Derivative sign is H(t)=A t^(q-1)[p+(p-1)t]-1; its derivative changes sign at most once, and rho(t)>1 near zero with rho(0)=rho(1)=1, ensuring the first critical root is the unique global maximum. q→0 test t=q and upper bound yield 2^(1/p). q→1, t_*^eta=pA[1+(p-1)t_*/p] with log(pA)=log B_p-eta*kappa_p+O(eta²), giving t_*~e^-kappa B_p^(1/eta) and R-1~eta t_*/p. Independent finite gauge/binary profiles corroborate, but analytic proof establishes all p,q.

## originality

PASS

Best-of-knowledge originality after comparing exact statements and implications; four structured comparisons and source-inspection limits are included.

## value

PASS

PASS: The sharp contrast between a single contractive block and strictly expanding binary two-block averages is a natural quantitative refinement of the existing nonlocally convex Lorentz averaging theory. The exactly determined binary restricted extremal profile and q→1 exponentially small defect identify a delicate transition to the Banach regime; a future analyst can use the precise lower bound without needing the still-open unrestricted norm. No falsely broad claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.

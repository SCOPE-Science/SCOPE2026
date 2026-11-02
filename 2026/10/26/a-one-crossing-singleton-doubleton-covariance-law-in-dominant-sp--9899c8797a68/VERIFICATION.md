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

With M hypergeometric for n draws from B dominant and r distinct singleton individuals, F1=n-M+1_{M=1}, F2=1_{M=2}, so Cov(F1,F2)=p2(E[M]-2-p1). The relevant sign factor is E[g(M)]-2 with g(0)=g(1)=0 and g(m)=m for m≥2. The coupling from B+1 to B removes a new dominant individual if sampled and replaces it uniformly among previously unselected old individuals; each old size-n subset is obtained with probability 1/C(B+r,n). It ensures M_B≤M_{B+1} and has a positive event 1→2 when r≥n−1, establishing strict T increase. T(2)<0 since M=1 possible, T(B)→n−2>0 for fixed n≥3, hence unique threshold (possible single zero). If B/r→q/(1−q), hypergeometric M→Bin(n,q), giving limit H_n(q)=nq[1−(1−q)^{n−1}]−2 strictly increasing from −2 to n−2; bracketing gives threshold scaling. The roots q_n decrease, and 2<nq_n<3 yields limit c(1−e^{-c})=2. For n=2, F1+2F2=2 so Cov=−2Var(F2). Exact labeled-subset enumeration independently corroborated the hypergeometric formula and B=2,5,6 examples at n=3,r=2, but asymptotic/global claims rest on the coupling and limit arguments.

## originality

PASS

Best-of-knowledge comparison of actual propositions, implications and hypotheses; the credited prior fragments are not claimed as new. Full texts actually read are identified, and inaccessible same-object papers remain explicit risks; an unsuccessful search is not novelty proof. Previous successive-species-discovery covariance and richness/frequency covariance are different random variables and sampling designs. Their sign change is not a theorem implying the present same-sample F1-F2 result; the exact hypergeometric coupling supplies the missing assertion.

## value

PASS

The covariance of the natural singleton and doubleton species frequency counts controls ecological sampling and uncertainty calculations. A sharp abundance-driven negative/zero/positive transition plus explicit finite-population threshold and rare-tail scaling is a new motivated sign classification, not an arbitrary numerical statistic or a claim of universal abundance profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The Mallows q^inv insertion-rank factorization gives independent U_t with P(U_t=r)=q^(t-r)/[t]_q, for every n>=2 and real q>0. Record R_t=1{U_t=t}, descent D_i=1{U_{i+1}<=U_i}; hence cross-covariance is zero for j outside {i,i+1}. Conditioning on record i gives the positive diagonal ([i+1]_q-1-q)/((1+q)[i]_q[i+1]_q); record i+1 forces D_i=0, giving negative superdiagonal -q/((1+q)[i+1]_q). Sum per i simplifies to -q/((1+q)[i]_q[i+1]_q), strictly negative; q=1 telescopes to -(n-1)/(2n). Independently enumerated all exact rational covariance entries for n=2..6 and q=1/2,1,2, all matched. This is an all-finite-n identity by factorization, not finite extrapolation.

## originality

PASS

Primary scientific comparisons concern same objects, parameters, reductions and stronger-coverage possibilities; no inspected statement decisively covers the complete final claim. Best-of-knowledge originality with explicit remaining access/priority risks.

## value

PASS

Local signs, exact sparsity and uniform negativity of record-count/descent-count dependence are natural second-order statistics in Mallows random permutations, distinct from marginal expectations or aggregate counts. Exact all-q formula can inform joint limit and dependency analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.

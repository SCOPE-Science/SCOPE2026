---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

All 16 Bernoulli outcomes yield smallest squared singular values 0,1,(3-sqrt 5)/2,2, with exact probability polynomials. Summation gives E sigma_min²=s²-(sqrt 5-1)ab(a+b-2ab); determinant zero iff both Bernoulli pair-products vanish, probability (1-a²)(1-b²). Writing k=ab/s²<=1/2 gives loss/s²=ks sqrt(1+2k)-2k²s²=(1+2k)/8-2k²(s-sqrt(1+2k)/(4k))²<=1/4; equality a=b=1/2. For s<=1, u=(a+b)/s in[1,sqrt2], derivative sign governed by strictly decreasing h(u)=(3u²-1)/(4u(u²-1)); threshold h(sqrt2)=5/(4sqrt2). Independent exact 16-state symbolic and derivative checks passed; no inference to high dimension.

## originality

PASS

Best-of-knowledge PASS, with actual primary statement/implication comparison and listed residual priority risks; an unsuccessful search is not historical novelty proof. General low-precision matrix results are not equivalent to the exact 16-pattern squared-singular-value law or orientation phase boundary. The cited main improvement theorem has nontrivial rank, variance and dimension assumptions that do not fit this test family. A higher-dimensional theorem with restrictive aspect-ratio/variance parameters does not dominate a two-dimensional exact degradation theorem; no contradiction of any hypothesis is asserted.

## value

PASS

Small singular values motivate recent claims about stochastic-rounding regularization. The smallest perfectly conditioned square family is a natural boundary case with a sharp 30.9% loss in expected squared min-singular energy, 9/16 rank collapse at the worst case, and an exact symmetry-breaking orientation threshold. This is a structural counterbalance, not a false claim that tall-matrix theorems fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.

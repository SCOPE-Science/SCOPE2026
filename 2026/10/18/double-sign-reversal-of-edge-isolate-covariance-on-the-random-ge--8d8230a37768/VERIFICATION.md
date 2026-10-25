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

For a singled-out isolated vertex, its other n-1 points are i.i.d. uniform on the complementary arc of length a=1-2r. Their pair circular distance cannot wrap through the excluded arc because |U-V|<=a<1-r, so the conditional edge probability is 1-((a-r)/a)^2 for r<=1/3 and 1 otherwise. Thus E[EI]=n a^(n-1) C(n-1,2)p and E[E]E[I]=n^2(n-1)r a^(n-1), proving exact covariance formula for every n>=2 and 0<r<1/2. Its polynomial Q_n=-4+(3n+10)r-8nr^2 for r<=1/3, plus the linear second branch, determine zero/sign intervals; checked n=2..5 negative, n>=6 two thresholds including junction n=6 r+=1/3. Independent symbolic rational/algebra checks and dense 501-radius sample for n=2..15 corroborated exact identities and signs. Expansion of Q root r-=4/(3n)+8/(27n²)+... and r=c/n yields cov(E,I)/n→(1/2)e^-2c c(3c-4). No independent-edge approximation or Poissonization is used.

## originality

PASS

Best-of-knowledge originality PASS after fresh published findings search and mathematical comparison of alias objects, stronger coverage, exact tables, and prior-result implications. Known general tools are credited, rather than claimed anew; risk remains documented: Penrose, Random Geometric Graphs (2003), chapter 3 full mathematical statements not read because authorized Oxford access reported vpn_disconnected; an earlier exact mixed-count formula there might subsume an aspect of this claim.

## value

PASS

Exact mixed dependence between edge count and isolated-vertex count in a natural spatial random graph has nonobvious two sign reversals for every n>=6 and a precise sparse critical mean degree 8/3. The result identifies a concrete regime where a superficially monotone covariance intuition fails and gives finite-sample covariances, rather than a routine first-moment computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

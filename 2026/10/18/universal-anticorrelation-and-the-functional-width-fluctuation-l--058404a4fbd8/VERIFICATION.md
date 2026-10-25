---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Support widths reduce to a single cosine arc modulo cell length 2q_n (q_n=pi/n even and pi/(2n) odd; odd amplitude 2R cos q_n). Direct overlap integration gives C_q(r)=((2q-r)cos r+r cos(2q-r)+sin(2q-r)+sin r)/(4q). Its derivative equals r(2q-r)[sinc(2q-r)-sinc r]/(4q)<0 for r in (0,q), sinc decreasing on (0,pi). Centered periodic autocovariance has zero full-period integral and hence negative minimum. Uniform cosine Taylor series and Var(cos qU)=q^4/45-q^6/315+O(q^8) give deterministic uniform O(q^2) coupling. Independent SymPy series returned lag coefficient -(15 z^4-60 z^3+60 z^2-8)/360 (equals 1/45-z^2(2-z)^2/24). This verifies the quartic correlation; marginal endpoints and skewness follow from E[U^{2j}]=1/(2j+1). The whole-process statement uses a common angle, not independent directions.

## originality

PASS

Akiyama and Kamae already derive exact width profiles and a two-edge expectation formula; their Theorems 3–4 cover the odd-versus-doubled-even width identity and cannot be renamed as new. New best-of-knowledge content is the uniform process-level normalized scaling limit, its explicit quartic lag law and negative sharp constant; the earlier formula provides enough information to derive them but does not explicitly do so.

## value

PASS

A natural geometric statistic (random width of inscribed regular polygons approaching a disk) obtains a universal non-Gaussian functional fluctuation limit and a sharp negative two-angle dependence law; this captures joint process structure invisible in one-point mean/variance computations and distinguishes strongly dependent angular field from an i.i.d. width law.

The dated certificate retains the supplied scientific assessment, sources and limitations.

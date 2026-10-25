---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For H=2 sum X_i, F(w)=product(L_i+T_i w+W_i w^2)=P(w^2)+w Q(w^2). If all weights positive, each quadratic has roots strictly in left half-plane and the phase arg F(iy) increases strictly from 0 to n*pi. Thus the negative zeros of P and Q are simple and strictly alternate. Positive partial-fraction decomposition Q/P=sum_j c_j/(z+a_j) and strict Newton coefficient log-concavity of P/(z+a_j) give p_(k+1)/p_k > q_(k+1)/q_k > p_(k+2)/p_(k+1) for all interior indices, forcing all P and Q mode pairs to occupy neighboring half-grid points. For boundary weights, approximate by positive triples and pass to weak cross-multiplied inequalities; coefficients remain real-rooted with consecutive supports and at most two adjacent modal indices. The only configurations that could produce a 5/2 mode gap contradict one of the weak inequalities, so all separations <=3/2. The n=2 witness (0,1/4,3/4),(1/2,0,1/2) yields F=(2w+6w^2+2w^3+6w^4)/16 and cross-parity mode separation 3/2. Cases with one impossible conditioning event are rightly excluded. Infinite n and continuous parameter intervals follow algebraically, not by enumeration.

## originality

PASS

Best-of-knowledge PASS: Broadie-Petkova (2026) study the same parity-conditioned trinomial sum and prove only a universal 5/2 separation by separate mean bounds. The stronger joint strict ratio sandwich, interior exact 1/2, global sharp 3/2 plus example are not stated there. Classical Hermite-Biehler and Newton interlacing are prior tools and do not themselves state the new modal consequence; Gnedin treats extended Bernoulli cross-modality rather than this pair of parity laws.

## value

PASS

A sharp universal adjacent parity-conditional mode separation significantly improves the published 5/2 bound, with a stronger rigid interior result and an exact boundary extremizer. This is a structural, all heterogeneous-trial theorem useful for rank/threshold comparisons of Poisson trinomial sums, not a routine Poisson-binomial mode bound applied twice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

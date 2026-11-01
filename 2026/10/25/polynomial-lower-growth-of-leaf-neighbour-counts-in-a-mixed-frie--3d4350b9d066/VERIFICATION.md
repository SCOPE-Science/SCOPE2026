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

For 0<p<1/2, exact conditional attachment probabilities are P(Delta L=+1)=[p+(1-p)(L+S)]/n and P(Delta L=-1)=[pL+(1-p)L/D]/n, with S=sum_{nonleaf neighbours u}1/D(u)>=0 and L<=D. Hence conditional drift is [(1-2p)(L-1)+(1-p)(1-L/D+S)]/n. For Y=(L-1)_+, when L>=2 the increment equals Delta L; for L<=1, Y next is nonnegative. Therefore E[Y_(n+1)|F_n]>=(1+(1-2p)/n)Y_n. Seed events occur with probabilities p/2 at n=3 for v=1,2 and p^2/[v(v+1)] at n=v+2 for v>=3, giving positive expected Y. Gamma-product iteration implies liminf n^-(1-2p) E Y >= b Gamma(m)/Gamma(m+1-2p) >0. Independently enumerated 11,824 exact rational conditional-transition/difference checks on growing finite trees; no finite experiment is used as an infinite-time proof.

## originality

PASS

The same zero-step/one-step mixture appears in Cannings–Jordan (2013), whose derived statistics concern the global proportion of leaves, and in Addario-Berry et al (2024 preprint, 2026 journal), which explicitly proposes the mixture and observes qualitative degree divergence. Neither inspected manuscript gives the fixed-vertex leaf-neighbour expected excess lower bound with n^(1-2p) exponent. This exact local expectation inequality is accepted as a best-knowledge increment; possible derivations in older local preferential/random-walk attachment literature remain priority risk.

## value

PASS

The mixed random-friend-tree model is a natural interpolation between uniform recursive attachment and one-step redirection. An explicit polynomial lower bound on leaf-neighbour excess for each fixed vertex answers a local quantitative question not settled by qualitative degree divergence or global leaf density. Although proof uses an elementary drift inequality, it is a motivated infinite-horizon growth theorem with explicit constants, not just an algebraic sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.

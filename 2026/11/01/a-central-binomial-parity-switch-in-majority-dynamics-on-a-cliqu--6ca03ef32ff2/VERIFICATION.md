---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Symmetry reduction by k of r nonhub clique ones, hub h, leaf ell gives k′=k 1_{2(k+h-1)>=r}+(r-k)1_{2(k+h)>r}, hub majority from k+ell among r+1 neighbors (ties retain h), ell′=h. Split h=0 cases at central k and complement all bits for h=1, proving every trajectory, the two possible terminal phase types, and sharp bounds F^4=F^3 (even r) or F^4=F^2 (odd r). For odd r the balanced labelled nonhub bits genuinely complement in each two-cycle, not just their count. There are C(r,floor r/2) such h=0 states and their complement h=1 partners; binomial weights yield all four nonzero classes, with total 2^(r+2). Independent full bitmask updates of 8176 initial labelled states for r=2..10 give exactly those classes. This finite check corroborates the symbolic all-r case split.

## originality

PASS

Goles–Olivos 1980 proves at most eventual period two on any finite symmetric threshold network, while Benjamini et al 2014/2018 study random, regular and unimodular graphs and voting time. These do not provide a clique with ONE exceptional pendant leaf exact all-labelled state counts or the shift of the central-binomial layer from a 3-step transient to initial primitive 2-cycles. A complete classification for clique-coronas with one leaf at EVERY clique vertex is not the graph here. The elementary nature of the reduction leaves a priority risk for unindexed lecture examples.

## value

PASS

It is a natural minimal symmetry-breaking perturbation of complete-graph majority dynamics, and shows a nontrivial parity-induced change from terminal consensus to recurrent two-cycles with sharp transient times and exact basin sizes, rather than simply repeating the period-two upper bound. The complete census is a useful benchmark in deterministic voting on almost-complete graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.

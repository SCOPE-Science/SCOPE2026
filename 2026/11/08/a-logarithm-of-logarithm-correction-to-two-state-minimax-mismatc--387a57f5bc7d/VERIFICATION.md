---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For two-state generator Q, u=a(1-exp(-(a+b)t))/(a+b), v=b(1-exp(-(a+b)t))/(a+b), and w=u+(1-u-v)epsilon. The entropy chain rule yields Phi=h(epsilon)+(1-epsilon)h(u)+epsilon h(v)-h(w). Its strict concavity follows from w(1-w)-(1-u-v)^2 epsilon(1-epsilon)=(1-epsilon)u(1-u)+epsilon v(1-v)>0. Fano and interior tests force the maximizer epsilon_t ->0; Phi'(Ct)>0 for each fixed C forces epsilon_t/t->infinity; the stationary equation then gives epsilon_t log(1/t)->a/(a-b). The Taylor error O(t^2/epsilon_t)=o(t) gives F=at(L-log L)+o(t) and the fair-prior equal-rate exact case. Boundary rates fixed positive, a>b, nonuniform as a-b->0. Source verifier code was read and its finite assertions classified as diagnostics; independent proof algebra checked, not a claim that the script was executed here.

## originality

PASS

Independent comparison of the full relevant main article and Supplemental SX of arXiv:2610.03478 against the fixed two-state singular boundary layer found only the leading escape-rate coefficient and qualitative concentration, not the logarithmic prior rate or absolute-o(t) entropy expansion. The 2025 commitment-capacity paper gives general channel concavity and algorithms, not this limit. Search failure is not novelty proof; equivalent classical binary-channel asymptotics remain a risk.

## value

PASS

Quantified optimizer boundary concentration and the t loglog(1/t) correction identify a genuine singular regime invisible to the known leading maximum-escape-rate law, with a distinct symmetric boundary. This provides exact asymptotic cost and prior information for near-identity two-state channels rather than a textbook reparametrization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

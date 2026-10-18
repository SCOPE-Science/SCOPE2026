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

Reconstructed 4-person (s,i) state recursion e(s,i)=i+Σ_{j≥1} binom(s,j)a_i^j(1−a_i)^(s−j)e(s−j,j), with a_i^S=1−(1−p)^i, a_i^G=g and e(s,0)=0. Independently symbolically derived all E_k polynomials and derivative/factor identities from inspected verification/check.py, including E1S−E1G(p)=3p³(1−p)² and E2S−E2G(p)=2p(1−p)²(1+2p−p²). A(g)=E1G(g) strictly increases by A′=3(1−g)Q4 with degree4 Bernstein coefficients (1,9/4,23/6,5/4,2)>0. A(2p−p²)−E1S(p)=3p(1−p)³P8, P8 has all nine positive listed Bernstein coefficients. Thus unique p<g<2p−p². Ratio B′/A′<2(1+2x−x²)/(3x²), from exact P5 identity and six positive Bernstein coefficients, implies E2S(p)>E2G(g); E3 gap >p(1−p)². Binomial K~Bin(4,q) average gives [3/2 q²(1−q)² ΔE2+q³(1−q) ΔE3]>0. This is isolated one-shot importation, not full epidemic ordering.

## originality

PASS

Best-of-knowledge originality: relevant primary statement/implication comparisons do not cover the precisely stated contribution; no absolute priority certification. Same household model and same R* terminology are important, but equal E1 and strict E2,E3 inequality do not follow from merely defining transitions or R*. No implication-equivalent result identified in the read portions.

## value

PASS

Comparing mechanistically different household epidemic rules after calibrating the same early household reproduction mean tests whether linear early-growth equivalence controls response to correlated multiple imports. The sharp, all-p four-person inequality with explicit parameter envelope provides a motivated exact counterpoint to global-epidemic numerical studies, not an arbitrary isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For q even, the projective-plane incidence axioms yield BB^T=B^TB=J in F2 and Bu=B^Tu=u. The toggled C=B+ef^T has rank rho+1 because e is not in im(B), f is not in im(B^T), and the rank-one update supplies e to im(C). P=CC^T and Q=C^TC have exactly three-dimensional images spanned by u,b,e and u,c,f, so rank(A^2)=6. For deletion delta=e^Tb=1, the restrictions collapse to a one-dimensional w, with P^2=ww^T nonzero, P^3=0, and the bipartite A^3,A^4,A^5 ranks 4,2,0. For insertion delta=0, P and Q restrict to 3x3 matrices with irreducible F2 characteristic polynomial t^3+t+1 of order 7. A interchanges the two invertible three-dimensional summands; A^7 swaps them, giving 2^3=8 states fixed by A^7, exactly a fixed state plus one 7-cycle; the 56 others form four 14-cycles. Kernel dimensions deliver all first-entry and phase-basin formulas. These algebraic identities apply to non-Desarguesian planes too. Independently rebuilt the Fano incidence and checked all 49 possible toggles (21 deletions, 28 insertions), their power ranks and 7/14-period structure. Finite checks are corroborative, not the universal proof.

## originality

PASS

General finite linear dynamics, projective-plane binary incidence parity, and XOR circulant convergence theory are prior art, but neither the inspected XOR-circulant results nor projective-plane extremal-cycle results imply a Levi-graph incidence-toggle nilpotency-five versus 7/14-cycle dichotomy, particularly for all even-order non-Desarguesian planes. The state counts require the toggled-incidence rank calculation and its six-dimensional Fitting component, which those general statements do not supply. Best-knowledge PASS with risk of an older equivalent binary incidence-matrix calculation.

## value

PASS

The smallest possible graph edit splits a natural high-girth regular incidence-graph Boolean dynamics into universal extinction versus a rigid 64-state periodic subsystem. Sharp times, complete orbit census and rank-dependent basins have direct structural meaning for stability of finite linear dynamical networks and do not amount to arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

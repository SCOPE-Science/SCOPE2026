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

For each n>=2 the bridge excursion half-lengths conditioned on K=k are weighted positive compositions with Catalan weights w_j=C_(j-1). Lagrange inversion yields Z(n,k)=k/(2n-k)*choose(2n-k,n-k). The select-weight (ell_i-1)/(n-k) and ordered Catalan convolution w_a w_b/w_j are normalized exactly; each target cyclic adjacent pair gives k oriented parents, so the total coefficient is k(2n-k-1)/[(k+1)(n-k)Z(n,k)]=1/Z(n,k+1). The kernel therefore preserves the required exact marginal law at every k. Each one-coordinate positive split preserves sum and decreases every sorted top-r sum; it drops sum of squares by 2ab>=2. Equality of the expectation drop occurs only at k=n-1, since at earlier k a component >=3 occurs with positive mass and strictly larger drop. Independent rational enumeration checked every composition n=2..9, all k, including 502 target probabilities and the sharp-drop condition; this is a finite check and the unrestricted proof is the combinatorial argument.

## originality

PASS

The exact conditioned composition law is explicitly prior (Serlet 2014); published tied-down excursion rank laws (Lindell--Holst 2007) are also prior. The final claim is the explicit k-to-k+1 size-biased Catalan single-coordinate split followed by uniform cyclic rotation, its exact simultaneous all-k construction, almost-sure vector majorization, and sharp quadratic expectation drop. A separate Resultary semantic search and broader Galton--Watson/forest literature checks found no dominant statement; the potentially related Pitman--Winkel forest composition theorem was materially inspected and its state space/operation differs. Priority against unexamined general forest fragmentations remains qualified, not certified.

## value

PASS

The number of returns is a natural path conditioning and the whole ordered vector, not just one scalar rank, admits one explicit simultaneous Markovian refinement. The all-level coupling gives new samplewise majorization and an exact sharp universal quadratic decrement; it is a motivated structural bridge-pinning fact rather than a Catalan table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

The symmetric adjacency matrix with one added hub self-weight when n is even gives strictly nonzero odd local fields, and the integer Lyapunov -s(t+1)^T W s(t) decreases strictly unless s(t+2)=s(t); hence eventual period at most two. With constant hub 0, the rim follows AND then AND; the identity A(A(x))_i=x_(i-2)x_i x_(i+2) forces constant values along each step-two cycle, and hub majority leaves precisely the two unanimous fixed states and two fixed-hub genuine two-cycle orbits when n even (accounting also for complements). With flipping hub, the rim returns iff no isolated 1 along each step-two cycle, with exact strict inequalities 2a>n and 2b<n. Cyclic runs of 1 length >=2, separated by zero-runs, have coefficient (ell/r) C(a-r-1,r-1) C(ell-a-1,r-1); the n odd/even G_n/G_(n/2)^2 polynomial counts labeled states without rotation quotient. Every orbit has one hub-zero state, so B_n counts orbits, not twice the number. For n>=96 the injective concatenations of 110 and 1100 on the step-two cycles give at least 2^(n/12) flipping cycles. Independent direct update enumeration for n=4..13 and independent run count agreed exactly; finite tests do not prove all n.

## originality

PASS

Classical symmetric threshold-network period-at-most-two and majority dynamics on trees/cycles are prior. The wheel with universal hub is neither a tree nor a local-radius cycle automaton, and prior accessible full articles do not give this exact hub-flip generating polynomial or exponential count. Resultary parity-automata studies use XOR, not majority. Equivalent wheel threshold-network calculations remain possible.

## value

PASS

The coexistence of exactly two fixed points with exponentially many distinct two-cycle attractors is a substantial structural distinction for synchronous consensus/majority models. The explicit finite generating polynomial gives exact labeled counts for every graph size and rigorously distinguishes reversing-hub from fixed-hub oscillators; none is mere code enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

On a connected sink-free graph a period-two return forces the two-step firing-count vector into the Laplacian kernel; primitive period two forces exactly one firing per vertex. For a phase assignment, the admissible chip-height interval at vertex v has exactly k_v=#opposite-phase neighbors integers; the inequalities are necessary and sufficient. On the corona C_n with r>=1 leaves/core vertex, leaf phase is forced opposite core with one height choice, while core contributes r+e_(i-1)+e_i for binary cyclic edge cuts e_i. Closed spin words correspond to even-parity cuts, two spin lifts cancel temporal two-phase division, giving P_{n,r}(z)=1/2[tr(T_r(z)^n)+tr(T_r(-z)^n)]. T_r(1) has trace 2(r+1), determinant -1; T_r(-1) has double eigenvalue -1, so N_{n,r}=1/2[(r+1+sqrt((r+1)^2+1))^n+(r+1-sqrt(...))^n]+(-1)^n. Independent edge-cut enumerations yielded n=3,4,5 at r=1 counts 37,162,681, n=4,r=2 count 722, and n=5,r=3 count 17683. The inspected supplied verifier additionally specifies six microscopic finite checks; that log alone is not infinite proof. A bounded h_v<2d_v enumeration is exhaustive only for primitive two-cycles by the proved intervals.

## originality

PASS

Best-of-knowledge PASS: Jiang provides general period return constraints, Dall'Asta treats an undecorated ring, and Scully–Jiang–Zhang classify firing patterns/pendant operations; none of the materially inspected statements provides the labelled microscopic two-cycle generating polynomial for every n,r. The exact transfer-matrix parity correction is not a direct reparameterization of qualitative period bounds. Original 1992 Bitar–Goles full text remains a named historical risk.

## value

PASS

Labelled period-two orbit counts are natural dynamical invariants of a conservative synchronous chip-firing automaton; the uniform-leaf-decorated cycle is a canonical unicyclic family. The polynomial completely resolves the core disagreement interfaces and determines an r-independent parity term despite r-dependent exponential growth, a structural distinction invisible to a general period-return criterion. The all-(n,r) exact enumeration is not an arbitrary small graph table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

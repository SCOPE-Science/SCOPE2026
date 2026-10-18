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

For x=(a,ξ), y=(b,η), fixed edge-target bracket is det(w_u,w_v) for vertex columns w_v=(a_v,b_v). With U exactly the set of nonzero columns, nonzero target edges B force W(B)⊆U. Since G[U] is a forest, each root has q²−1 possibilities; a prescribed zero edge has q−1 nonzero child solutions and a nonzero prescribed edge has q child solutions. Choices are independent and central entries contribute q^(2|E|), proving exactly q^(2m+|B|)∑_{U⊇W(B)}(q²−1)^c(U)(q−1)^(e(U)−|B|), for every finite forest and q including characteristic 2 and empty graph. All terms nonnegative and U=V is positive, giving surjectivity. Independent direct determinant enumeration checked 103 finite target/forest/field instances; the unrestricted proof is tree rooting.

## originality

PASS

Rossmann 2022 studies graphical group conjugacy class sizes, equivalently zero-commutator counts and adjoint ranks. Tittmann–Averbouch–Makowsky provide induced-component polynomials relevant to z=0. Neither measured invariant determines the exact fiber over each nonzero prescribed central target. Resultary's 2026 tree graphical group character-degree polynomial involves weighted support matching numbers (different statistic); its Kronecker path algebra commutator formula uses different multiplication. Prescribed support-by-support full bracket fibers appear best-of-knowledge not covered.

## value

PASS

The graphical two-step nilpotent Lie algebra is a standard graph construction and bracket word maps are natural to centralizer and probability questions. An all-target exact fiber law for arbitrary forests and fields is a complete structural enumeration, including shape-sensitive examples where edge-support position changes the answer. It extends genuinely beyond the familiar zero bracket polynomial and can support probabilistic commutator computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

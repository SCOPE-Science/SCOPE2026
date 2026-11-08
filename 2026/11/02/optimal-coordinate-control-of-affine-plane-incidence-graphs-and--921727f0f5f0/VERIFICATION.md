---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For any EXISTING affine plane q>=2 and its unweighted combinatorial point-line Laplacian with independent vertex input columns, NN^T=qI+J follows directly from finite-plane incidence. It yields rank q^2 and an exhaustive orthogonal Laplacian decomposition: radial eigenvalues 0,2q+1, line-kernel eigenvalue q (multiplicity q), and two simple-parameter eigenvalues lambda±=(2q+1±sqrt(4q+1))/2, each multiplicity q^2-1. PBH therefore requires q^2-1 controls; the class-constant line kernel forces selected lines in >=q directions. For |S|=q^2-1, testing either lambda± reduces to nonsingularity of the square (|C|+1)x(|C|+1) all-ones-plus-selected-incidence matrix H(T,C); lambda=q contributes the class condition, radial modes are detected by any nonempty set. For q concurrent lines through O, T={O,P_i in distinct chosen lines} makes H invertible since (1-q)x_O=0. Counting distinct affine signatures (all-ones, each e_i, and zero) with nonzero unique affine circuit gives exactly 2q(q-1)^q choices for each pencil, multiplied by q^2(q+1). Independent direct PBH/geometry rational enumeration confirms all 120 q=2 size-three placements with 56 successes and 48 successful q=3 fixed-pencil omitted-point sets. These are checks, NOT the universal proof. Existing plane orders only; arbitrary weighted/projective planes excluded.

## originality

PASS

Best-of-knowledge originality PASS based on direct comparison of exact statements, hypotheses and implications. Prior model ingredients and general lemmas are credited; no inspected full-text theorem establishes the precise additional classification. The named inaccessible and abstract-only comparisons remain risks, not proof of priority. Existing symmetric-network multiplicity bound plus plane spectrum yields only the minimum number of required drivers. The q-direction necessity, H(T,C) sufficiency for each minimum placement, and 2q³(q+1)(q−1)^q pencil count additionally require incidence geometry arguments not supplied by the compared general results.

## value

PASS

An exact all-minimum coordinate-actuator certificate for a natural finite geometry graph, a necessary direction-coverage obstruction and a simultaneously sharp construction answer meaningful structural controllability questions. The exact concurrent-pencil count distinguishes configurations beyond a generic multiplicity lower bound; q>=2 construction demonstrates feasibility. This is not just rephrasing the textbook PBH test because geometry reduces all candidate placements to one explicit small incidence determinant and yields a closed natural-family census.

The dated certificate retains the supplied scientific assessment, sources and limitations.

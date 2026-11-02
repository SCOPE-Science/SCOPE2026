---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The S_n action permutes off-diagonal edges transitively and preserves both edge subspaces. Any equivariant vertex-potential-to-cycle map has the form a x_i+b x_j+c sum_k x_k and zero row/column sums force a=b=c=0 for all n>=3; hence there are no intertwiners cut-to-cycle nor cycle-to-cut. Group averaging forces each canonical orthogonal projector to be the unique equivariant projection and norm-minimal for all invariant norms. An explicit Laplacian solution for injection along an edge determines five disjoint current orbits, their signs and counts; their absolute sum is ||Q||_1=(3n-4)/n. Diagonal resistance (2n-1)/(n(n-1)) gives ||C||_1=2(2n²-6n+3)/(n(n-1)), with symmetric matrices equating l1 and l-infinity norms and a direct polynomial sign giving crossover n=5. Independent exact rational Laplacian inversion verified every column through n=8, including boundary n=3. The all-n proof rests on representation and electrical identities, not the finite range.

## originality

PASS

Compared exact statements, not shared terminology. Hodge cut/current projections and transportation cost supply equivalent settings. A scalar effective resistance gives the diagonal of Q, not the entire absolute current column sums needed for operator norms. The group-averaging framework is prior, but the crown-specific equivariant uniqueness and formulas require calculation. The known cube calculation is a special case; it does not automatically imply the n-dependent formulas and crossover. A general abstract method alone does not give explicit norms for crown n>=5. The theorem derives an infinite parameter formula from exact sign/orbit calculations, not reprinting a known tabulation. Failed search does not certify absence of a hidden older formula. Diagonal resistance alone cannot determine off-diagonal absolute current norms, and the cube n=4 cannot imply the all-n crossing. The new proof provides the required full current decomposition and intertwiner vanishing.

## value

PASS

The result determines relative projection constants of natural cut and cycle Banach subspaces for an infinite edge-transitive graph family, identifies the unique equivariant minimizers and a sharp crossover in norm dominance. It extends a previously known n=4 cube special case to a family-wide structural calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

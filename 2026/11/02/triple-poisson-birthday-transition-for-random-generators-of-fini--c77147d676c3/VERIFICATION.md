---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Write Q=q^f. High Q-Frobenius powers lift residues to the unique coefficient field, since the radical is nilpotent. Once that field is generated, subtract the field components: spanning the cotangent space is necessary and sufficient, since products of tangent lifts span the successive radical layers and the filtration terminates. Distinct full-degree Frobenius orbits give distinct maximal polynomial kernels; CRT supplies the residue indicators and high Frobenius powers lift them to the actual factor idempotents. Consequently generation is exactly absence of the three stated obstructions. Uniform sampling makes residues and tangent matrices independent, irrespective of the higher radical. The proper-subfield probability is asymptotic to Q^(-k/2) for even f and smaller order for odd f (zero for f=1); a unique maximal-size proper subfield supplies the even case. For d>0, the rank-defect probability is asymptotic to Q^(d-1-k), so r times this probability vanishes, tends to c, or diverges on the stated sides of d=k/2+1; for d=0 the obstruction is absent. Conditional on bounded U, the remaining coordinates are uniform in T/f orbit boxes. In the j-th collision factorial moment the disjoint pairs give (f c^2/2)^j; any connected component with v>=3 vertices contributes order (Q^k)^(1-v/2), uniformly for bounded U. Tightness of U and this conditional limit give independence, with V exactly independent already at finite q. For the positive regime use the probability of zero counts (e.g. intersection with the open half-integer cube, whose boundary carries no limiting mass). Above the threshold the rank obstruction suffices. I independently evaluated the finite product via logarithms for f=k=d=2 and c=1, reproducing the four displayed probabilities to eight decimals. The general conclusion is analytic, not a finite experiment.

## originality

PASS

Pass applies to the full q-growing phase diagram and the joint law of the three separately identified obstructions, not to the algebraic criterion, the matrix rank formula, or the classical birthday limit in isolation. There is substantive two-obstruction overlap with the finite étale profile result in a different limit and exact-count overlap for split radical-square-zero products. Neither carries the arbitrary local factors with even residue degree and the simultaneously critical cotangent obstruction.

## value

PASS

Generation of an increasingly large product is a natural test beyond single-factor generator criteria. The simultaneous Poisson window identifies precisely when three algebraically different causes all survive and distinguishes their effects, rather than reporting only a zero-event probability. The complete threshold is uniform across arbitrary higher radical structure; it distinguishes a residue-field birthday effect from the onset of widespread local nongeneration. The individual probabilistic tools are standard but the exact balance and joint classification answer a motivated structural question.

The dated certificate retains the supplied scientific assessment, sources and limitations.

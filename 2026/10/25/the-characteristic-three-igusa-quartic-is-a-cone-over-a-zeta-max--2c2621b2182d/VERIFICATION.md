---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS — Reconstructed Newton polynomial identity on e1=0, the characteristic-three translation symmetry x->x+t(1,...,1), and the cone with section x5=0. For nonvertex singulars the cubic gradient equation x_i^3-a*x_i=b implies each coordinate in one of three affine F3 positions; sum and p2 constraints force precisely two coordinates of each value, modulo affine relabeling 90/6=15 points, all F3-rational. Hessian on H/<1> has rank3 transverse to each node; no positive-dimensional base singular locus, hence integral normal cone and 15 A1 nodes. Quartic hypersurface adjunction and rational double-point resolution produce a K3. Independently enumerated the 40 P3(F3) and 820 P3(F9) points using exact GF(9) arithmetic, finding |S(F3)|=25, |S(F9)|=145 (consistent with the submitted verifier). Adding 15q yields Y counts 70,280 and H2 Frobenius sums 60,198; Weil absolute value |alpha|=3 makes equality in sum(alpha²)=198=22*9 force alpha=±3, with multiplicities 21 and 1 from first trace. Derives all-extension zeta, not finite extrapolation.

## originality

PASS

PASS, qualified. The classical fifteen lines and equation of the Igusa quartic and 15-node quartic surfaces are known in characteristic zero (Hulek–Sankaran and Rito). Neither full inspected complex geometry nor their stated scope implies the explicitly specified coefficientwise F3 cone degeneration, all geometric singulars or its exact zeta. The Igusa Kuranishi cone returned by Resultary is an unrelated six-parameter tangent-bundle singularity. Direct searches found no matching F3 zeta dataset; still possible old K3 tables contain an equivalent model.

## value

PASS

PASS — The characteristic-three degeneration is a nontrivial special-fiber geometry of a standard Siegel-moduli quartic equation, with a complete fifteen-node singular-locus classification and exact Frobenius zeta of a natural resolved K3 surface. All-extension point counts derived from two finite counts and Deligne are a useful exact arithmetic invariant rather than a small arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

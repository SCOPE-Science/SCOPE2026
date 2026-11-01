---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For full-dimensional 3D zonotopes with parallel generating directions merged, the exposed-edge normal arrangement of each generator direction has exactly 2 k_i sectors, proving E=2 sum_i k_i. Every k_i >=2. The exhaustive rank-three configurations yield E=12 only with 3 independent directions (parallelotope), E=18 only with 3 distinct directions in a plane and one outside (affine prism over a genuine centrally symmetric hexagon), and E>=24 in every other case. For >=5 directions either four have no coplanar triple, or three span a plane and a fifth generator inside/outside that plane forces at least 12 total plane incidences. For any 3-polytope the number of complete vertex-edge-facet flags is F=4E. Hence Δ=(8/9)E−M. The symmetric 3D Blaschke–Santaló upper bound M<=16π²/9 implies the E>=24 lower bound (8E−16π²)/9. For an affine hexagonal prism H×[-1,1], integration of the polar support-function sections gives polar 3-volume (2/3)area(H°) and product M=(4/3) area(H)area(H°)<=4π²/3 by the planar symmetric Blaschke–Santaló inequality. Thus its Δ>=16−4π²/3 >0. For a parallelotope E=12 and exact centered product 32/3, so Δ=0. Polarity preserves Mahler product and reverses complete flags; Z° has zero deficit iff it is the polar cross-polytope of a parallelotope. The larger E>=24 bound exceeds the prism bound by (4/9)(12−π²)>0. No inference from finite examples to the universal theorem.

## originality

PASS

Best-of-knowledge novel motivated special-class consequence: Winter 2026 already proves the general Mahler–flag inequality but explicitly leaves its equality classification open in Conjecture 3. The present theorem resolves equality and provides a fixed positive absolute deficit for every nonparallelotope 3D zonotope and its polar. Classical Blaschke–Santaló already controls the volume product; it has no combinatorial flag threshold. The published universal homothetic-frusta result ALREADY implies M(H×I)=(4/3)M(H) as a special case: that prism factor alone must not be credited as new. Neither its theorem nor the reverse-Mahler zonoid stability result supplies the zonotopal edge trichotomy plus flag comparison and global strict gap. These standard ingredients make the deduction short but do not exhibit full prior statement coverage. Other unindexed combinations remain an explicit priority risk.

## value

PASS

The object is the natural infinite class of all 3D zonotopes and duals of zonotopes, and the invariant Δ is the exact quantitative deficit in a recent published Mahler–flag inequality whose equality characterization was explicitly left conjectural. The result answers equality for the entire class and identifies a positive geometry-independent absolute margin once the extremal parallelotope/cross-polytope is excluded. The nontrivial 18-edge hexagonal-prism chamber forces a separate 2D product input, while the remaining E>=24 chamber enjoys a strictly larger margin. This is a mathematically motivated sharp qualitative boundary/equality classification, even though the explicit constant is nonoptimal and its known sublemmas are elementary. No paper-sized/general theorem or formal proof is demanded and no new general Mahler inequality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

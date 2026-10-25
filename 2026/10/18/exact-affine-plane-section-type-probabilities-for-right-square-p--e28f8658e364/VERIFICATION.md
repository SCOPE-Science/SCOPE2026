---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For P_h=conv((±1,±1,0),(0,0,h)), h>0, conditioning motion-invariant planes on intersection gives orientation density proportional to width and uniform offset conditional on orientation. A generic plane has N in {3,4,5} cut edges; exactly four disjoint 2-vs-3 sign partitions yield pentagons (apex paired with a base vertex). A triangular-prism Minkowski difference Q and Q^+=conv(Q∪{0}) translate each separating-offset length into mean-width(Q^+)-mean-width(Q). Evaluating the standard exterior-dihedral-edge mean width formula produces P5=F/B, with B=2(pi-acos(1/r))+s acos(1/r^2), F=2s asin(1/r^2)+4 acos(1/r)-pi sqrt(2), r=sqrt(1+h^2), s=sqrt(2+h^2). Crofton edge crossing sum gives E N=2pi(2+s)/B and P3=4-E N+P5, P4=E N-3-2P5. Direct asymptotics give positive interior pentagons and 2(2-sqrt(2))/h tall-height decay; maximum existence, not uniqueness, is asserted. Independent width-weighted normal-and-offset simulations at h=0.4,1,2,5 (130000 draws each) differed from exact three-type distribution by at most 0.00182; h=2 predicts (0.36485656,0.50418302,0.13096043). Finite simulation cannot prove the exact integral formulas.

## originality

PASS

The probability law for random affine *sections* is mathematically different from the previously published square/rectangular-pyramid law for five-vertex *orthogonal projections*. A recent deterministic combinatorial slicing paper studies section patterns, not the invariant conditioned plane distribution. Neither source has been found to imply this exact height-dependent full section distribution; residual stereology priority uncertainty remains.

## value

PASS

The complete triangle/quadrilateral/pentagon law of random affine sections of the simplest non-simplicial pyramid is a natural stochastic-geometric observable; it includes correct width-biased orientation sampling, explicit elementary integrals, an interior maximum existence mechanism and sharp thin/tall asymptotics. It is not just edge enumeration or a restatement of shadow probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.

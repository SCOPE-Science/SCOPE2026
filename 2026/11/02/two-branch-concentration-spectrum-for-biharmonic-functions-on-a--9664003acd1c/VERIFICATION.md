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

Almansi separation and angular orthogonality give a complete direct sum of two regular radial modes per harmonic, with the same orthogonality after cutoff. For p=2m+d their full-ball radial Gram matrix has entries 1/(p+2i+2j) (i,j in {0,1}); the restricted matrix is t^(p/2) diag(1,t) G diag(1,t). Thus its determinant ratio is t^(p+2). An orthonormal radial basis after factoring out r^m is √p and √(p+4)((p+2)r²−p)/2. Integrating its two squared norms over the cutoff gives trace t^(p/2)[(p+2)²(1−t)²+8t]/4. Vieta gives the stated roots, distinct since t∈(0,1), and the inner and outer integrals are strictly positive on every nonzero radial polynomial. Tilting every coefficient-vector quotient by r² strictly decreases it; taking a maximizer in degree m+1 and a minimizer in degree m gives the two strict eigenvalue comparisons. The upper root is asymptotic to the trace, and dividing the product by it gives the lower root and both constants. Compactness follows from decay of the upper root. Taking logs gives cutoff degrees (L±2 log L)/ell+O(1); multiplying their separation (4/ell) log L+O(1) by the leading multiplicity 2(L/ell)^(d−2)/(d−2)! gives the stated difference coefficient. The cumulative multiplicity 2M^(d−1)/(d−1)!+O(M^(d−2)) yields cancellation of the two first-order shifts in the total; the second-order terms O(L^(d−3)(log L)^2) fit the remainder. These arguments include m=0 and retain multiplicities at cross-block collisions. The checker was read, not run.

## originality

PASS

The radial block method and extremely close planar block formula are prior, as is the phenomenon of opposite logarithmic count corrections in other settings. The supported distinction is the ordinary real-ball d≥3 biharmonic operator with the dimension-dependent spherical multiplicities and sharp branch excess and total count. In even dimensions the radial eigenvalues can already be read by shifting the mode parameter of the bianalytic disk block: 2m+d=2(m+d/2−1)+2. That algebraic overlap is not a new block method or even a new scalar formula at those indices. The inspected disk results do not supply the real spherical-harmonic multiplicities or the resulting L^(d−2) log L coefficient for this operator.

## value

PASS

The two branch counts describe how many independent fourth-order modes actually concentrate in a concentric core. The leading total count alone conceals the opposite logarithmic shifts; the explicit excess coefficient quantifies a distinction absent from a single harmonic branch. The centered cutoff and ordinary biharmonic extension are natural choices, and the result uses the real dimension rather than merely restating a disk block calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

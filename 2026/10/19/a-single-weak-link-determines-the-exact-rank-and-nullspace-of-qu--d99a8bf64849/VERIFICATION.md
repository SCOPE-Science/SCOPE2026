---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The theorem has an analytic proof; finite checks do not establish its unrestricted quantifiers.

## Deterministic package check

Run `python verify.py` with Python 3 and NumPy. The exact part uses `fractions.Fraction`, explicit adjacency actions, exact Gaussian elimination, and integer binomial coefficients to test the full moment determinant and its triangular entries at \(3\le n\le25\) and eight rational bond weights, including the limiting path and perfect cycle. The independent spectral part diagonalizes separately constructed weighted adjacency matrices at \(3\le n\le18\), groups repeated eigenvalues before forming the Cesàro projector sum, and checks rank, normalization and bond-reversal invariance at seven bond weights. The observed successful run was:

```text
VERIFY_OK exact_moment_profiles=184 independent_spectral_profiles=112 spectral_entries=14728 orders=3..25
```

## Claim-to-evidence map

* Spectral simplicity for every \(g\ge0\), \(g\ne1\): the two endpoint recurrence equations force \(g^2=1\) if the eigenspace has dimension at least two.
* Exact upper rank \(q=\lceil n/2\rceil\): simple eigenvectors have fixed parity under the defective-edge reflection; their entrywise squares are invariant under reversal.
* Exact lower rank and kernel: for \(2k<n\), nonwinding closed-walk counts and unique first defect excursions yield \(\det W=(-1)^{q-1}(g^2-1)^{q-1}\); the moment matrix is in the span of squared eigenvectors.
* Perfect-link \(g=1\): Godsil (arXiv:1103.2578), Lemma 6.1, explicitly evaluates the cycle average and hence its rank and antipodal kernel.
* Boundary \(g=0\): the weighted Hamiltonian is a path, consistent with Godsil's previously established average-mixing formula, not an independently claimed discovery.

No interval-arithmetic or formal proof assistant is claimed. Numerical rank tolerance cannot certify unbounded parameter ranges. The physical system has a single *nonnegative* bond weight; negative bond weights or magnetic flux are outside the theorem.

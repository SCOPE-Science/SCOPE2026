---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In L2(p tensor p), decompose a score into its constant, additive potentials u(a)+u(b) and v(a)-v(b) with centered u,v, and a row/column-degenerate residual h. These are orthogonal and exhaust the score space under full support. The plus sum on a path has single endpoint weights and doubled interior weights, variance (4m-2)||u||^2, whereas the minus sum is the endpoint difference of variance 2||v||^2; the two endpoint cross terms cancel. Degeneracy gives zero covariance with all single-letter terms and between all distinct interaction windows, even through one-letter overlaps. The interaction variance is m||h||^2. Dividing by the squared weighted norms of these scores and by m gives exactly 2-1/m, 1/m and 1, plus the constant null direction. This proves the ranks, sharp equality spaces for nonzero centered costs, and the m=1 coincidence. On cycles every plus weight is 2 and the minus sum vanishes; n>=3 ensures distinct windows never share both letters, including n=3. Thus gradient scores join the nullspace and the other normalized eigenvalues become 2 and 1. The same covariance follows by enumerating the two overlap orientations, with m-1 contributions each on a path and n on the cycle. The exact trace is q^2-1; the bounded one-dependent CLT permits a singular Gaussian limit and gives the stated known-p weighted chi-square via the squared whitened norm. Replay: RESULT.md lines 48–95; an independent exact-rational q=2, p=(1/3,2/3), n=3 enumeration checked both path and cycle covariance and score equations. The uploaded verify_bigram.py and VERIFICATION.md were inspected, not run; their 25 cases are path/cycle configurations over several alphabet/size laws, not 25 distinct laws each tested in both geometries.

## originality

PASS

Pass only for the complete exact finite-length nonuniform whitened spectra and the sharp path-to-cycle boundary effect with extremizing subspaces. The known-probability Pearson asymptotic law is directly covered in earlier work, not merely related; it is neither credited as new nor needed as a novel ingredient. The strongest accessible comparison has the limiting decomposition but does not establish the complete finite-length spectral comparison.

## value

PASS

The result resolves which modes of a natural overlapping-count table are poorly conditioned and why. Path gradients retain exactly the random endpoint imbalance, giving small but nonzero variance; closing the path eliminates exactly those directions while leaving the interaction and symmetric families at stable scales. The finite spectra and equality families therefore give exact rank and conditioning information even at small sample sizes or nonuniform letter frequencies, beyond the previously known limiting Pearson calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

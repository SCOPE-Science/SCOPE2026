---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The no-jump generator is dissipative. An A(Q_n) eigenspace is dark iff its functions vanish on every lossy site, since any real eigenvalue of H=JA-iGamma forces Gamma v=0 and contractivity eliminates nontrivial real-axis Jordan blocks. Walsh weight-w characters diagonalize A, so sector visibility is exactly the rank of M_{r,w}(S,T)=(-1)^|S∩T|. Standard Boolean-lattice harmonic modules have dimensions mu_i=C(n,i)-C(n,i-1); direct Newton finite differencing of the signed intersection generating function gives restriction scalar (-2)^i [z^(w-i)](1-z)^(r-i)(1+z)^(n-r-i), which contributes mu_i precisely when nonzero. The central odd generating functions (1+z)(1-z²)^(m-i) have every coefficient nonzero, proving injectivity in each energy sector for n=2m+1, r=m,m+1, while other radii fail by middle-shell dimension. For even n=2m, alternating harmonic parities give central dark dimension 2^(2m-1)-C(2m,m)/2; the adjacent layer has C(2m,m)/2 dark dimensions and their restrictions have complementary middle-sector kernels, yielding full capture jointly. Independently reconstructed and compared 203 complete rational/integer shell ranks for n<=7; this supports, not replaces, all-n proof. Endpoint n=1,2 and r=0,n are covered.

## originality

PASS

The Boolean harmonic decomposition, hypercube quantum walk diagonalization, and general absorption/dark-state principles are prior. The full exact binary Walsh-energy shell restriction and odd-even all-initial-state complete-layer theorem are not contained in the inspected nonbinary cumulative-band spectral theorem or earlier hypercube mixing/point-target work. This is qualified best-of-knowledge originality; an implicit association-scheme specialization is a residual risk.

## value

PASS

A sharp structural absorption boundary for a natural loss support: odd hypercubes need one complete shell but even cubes need two, with exact sector-by-sector lost subspaces and no dependence on positive rate magnitudes. This distinguishes eventual full-state capture from return probability at a single initial vertex and provides benchmarks for coherent transport and controllability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

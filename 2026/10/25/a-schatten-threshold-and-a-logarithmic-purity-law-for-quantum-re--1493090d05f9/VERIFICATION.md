---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Read the actual seven-blob source package at its assigned Git tree (the tree returned AUDIT.json, METADATA.json, RESULT.md, REVIEW.md, SLOGAN.txt, VERIFICATION.md, check.py and matched Git blob IDs). The final claim jointly concerns r>0, a separable Hilbert-space self-adjoint H and any positive trace-one initial state. The exact Kummer scalar response f_r(ω,t) is published prior work and is a random-unitary characteristic function, so |f|<=1 and f(0)=1. On S_2 the difference Liouvillian is self-adjoint; dominated spectral convergence f(ω,t)->1_{ω=0} yields the Hilbert-Schmidt projection. Compact Hilbert-Schmidt operators commuting with H have only finite-dimensional H-invariant eigenspaces away from zero singular values, hence the fixed-point projection is sum_E P_E ρ0 P_E. Interpolation with trace-norm contraction gives convergence for 1<p<2; S_2 dominance handles p>=2. The trace of the fixed point is pure-point mass m. If m<1, no trace-norm limit can exist (a trace-norm limit would equal the unique S_2 limit but would have trace one). If m=1, finite-eigenspace compressions and 1-norm contractivity give convergence. In the rank-one finite flat band, exact purity is ∫∫w(E)w(E')|f_r(E-E',t)|² dE dE'; Kummer's algebraic expansion at Bohr scale ω=y/sqrt(log(rt)) gives |f|²->e^{-2y²/r²}, with a uniform Gaussian envelope on the compact difference band. Since w∈L∞⊂L², its autocorrelation is continuous at zero and the approximate identity has mass r sqrt(pi/2), establishing the constant. For every positive null epsilon, select T_n with epsilon(T_n)<2^-n/n; choose two distinct eigenvalues 3n and 3n+δ_n with δ_n>0 small enough that |f(δ_n,T_n)|>=1/2. A pure state with pair weights 2^{-n-1} then has finite moments of all orders, and the 2x2 compression yields trace norm >=2^{-n-1} at T_n, making rate ratio unbounded. This proves nonuniformity but does not claim an individual universal lower rate. Independent numerical checks of exact mpmath hypergeometric values at logarithmic times L=6,12,20 recovered the e^{-2y²} local-frequency limit trend; a separately written 90-point Gauss-Legendre purity integral gave sqrt(L) P=1.19008,1.19077,1.19359 at L=6,11,20, consistent with slow convergence toward sqrt(pi/2)=1.25331, but finite checks are not infinite proof. The special-function uniformity is the nonstandard analytical point and is supported by the inspected Kummer-sector expansion, not merely check.py's PASS log.

## originality

PASS

Qualified best-of-knowledge originality for the joint three-part theorem, NOT for the exact scalar multiplier or ordinary fixed-frequency coherence decay already proved in arXiv:2608.02297. The 28-page primary text proves a gapped/discrete stationary density and continuum positional spreading, but its Eq. (14) and Appendix C do not state the all-spectrum Schatten/trace topology criterion, the sharp sqrt(log t) purity coefficient for a spectral band, or a compact-resolvent arbitrary-slow trace-distance example. The closest independent 2018 reset paper has a fixed-state Markovian reset and a shifted Lindblad generator, not uniform-history memory. New mathematical work is the norm-topology classification plus near-diagonal purity asymptotics and a quantitative slow-rate obstruction; ordinary spectral/ergodic ingredients are correctly credited. Stronger general dephasing and Tauberian theorems may imply parts and remain priority risks, so this is not a guarantee of uniqueness.

## value

PASS

The precise topology in which a history-reset state equilibrates is intrinsic to quantum dynamics: all S_p observables for p>1 settle while the trace norm cannot settle when initial probability lies in continuous spectral subspaces. The exact logarithmic spectral-purity constant for a natural flat energy band is an independently useful quantitative prediction not computed in the motivating paper, and the doublet example shows why compact confinement and all finite energy moments do not guarantee a rate. These jointly address a motivated gap in spectral relaxation theory rather than a parameter rebranding, artificial finite slice, or a known-table reprint. Routine fixed-frequency dephasing and the classical Kummer formula are credited as ingredients, not used alone to justify value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

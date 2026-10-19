# Scientific review

## Correctness

**PASS.** The canonical stationary law follows from exact detailed balance for both fixed-edge exclusion generators and the autonomous gate. The invariant linear occupation sector closes exactly under the exclusion generator; its canonical covariance is the explicit finite-population susceptibility \(\chi_{n,k}=k(n-k)/[n(n-1)]\). The joint generator is a positive finite-dimensional self-adjoint block operator on vertex-centered fields, making the Green–Kubo formula legitimate. A variational test vector supported on the OFF-component nullspace proves the finite-rate lower bound. The Schur complement on that nullspace has perturbation compression exactly \(pI\), proving both the asymptotic coefficient and the boundedness boundary. Complete-graph Poisson equations give the stated all-rate identity. Exact rational calculations with separately built full configuration and reduced generators test the formulas. Numerical enumeration was not substituted for the all-parameter proof.

## Originality

**PASS within materially inspected literature; incomplete historical coverage remains a risk.** Static symmetric-exclusion spectral data [1] do not imply the dynamic-gate cut projection without an additional time-dependent resolvent comparison. Dynamical-percolation random-walk work [2] focuses on one-walker mixing and hitting with independently switched edges, not the canonical multi-particle stationary Green–Kubo quantity. Static-conductance occupation fluctuations [3] are a different limiting regime. Dynamic-environment exclusion self-duality [4] is an antecedent explicitly acknowledged in the proof; its infinite-lattice hydrodynamic theorem does not itself give the finite-graph all-rate lower bound, singular coefficient, or complete-graph identity. Searched mathematical records presented general reversible variance inequalities and switched graph dynamics, but no matching implication was verified. Residual risk: a general slow-switching reversible-chain theorem may yield the same coefficient after translation, or an uninspected historical calculation may have already made the specialization.

## Value

**PASS.** For finite networks subject to rare connectivity changes, the exact coefficient distinguishes fluctuations that scale with structural cut persistence from those that stay bounded despite unchanged static occupancy statistics. The result is a graph-topological *if-and-only-if* classification for arbitrary canonical particle count, with an all-rate lower bound that attains the leading slow-switching constant. The complete-graph closed form supplies an exact benchmark with no uncontrolled approximation. It is not a claim about a phase transition or faster/slower mixing under a separate dynamic observable.

## Scope and risks

The observation must be linear in occupations and centered over all vertices. Edges must retain symmetric rates; the global gate must be autonomous and exponentially switching. The singular limit is after taking the stationary long-time variance. The inspected works [1]–[4] cover related machinery, so the strongest novelty claim is only for the explicit combined finite-graph law. Independent audit and exhaustive bibliographic verification have not been performed.

Self-review: passed. Independent audit: not yet performed.

# Review: exact diagonal balance and compact-recurrence bounds for the Halvorsen flow

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The central calculation is exact. With \(\sigma=a+b+c\), \(S=x+y+z\), and \(Q=x^2+y^2+z^2\), direct summation gives
\[
\dot S=-\sigma S-dQ.
\]
Completing the square gives
\[
\dot S=\frac{3\sigma^2}{4d}-d\left\|X+\frac{\sigma}{2d}{\bf1}\right\|^2.
\]
A symbolic expansion gives zero residual for both identities and verifies the diagonal equilibrium \(E=-(\sigma/d){\bf1}\).

The bounded-forward mean-square identity follows by time integration with a vanishing bounded endpoint term. On \(\sigma=0\), monotonicity of \(S\), integrability of \(Q\), and uniform continuity of \(Q\) imply convergence of every bounded forward solution to the origin; applying the argument on the full real line rules out every nonzero bounded complete orbit.

For \(\sigma\ne0\), the variation-of-constants formula fixes the sign of \(dS/\sigma\) on bounded complete trajectories. The estimate \(Q\ge S^2/3\) then yields a Riccati comparison: crossing below \(dS/\sigma=-3\) forces finite-time divergence in the appropriate time direction, contradicting bounded completeness. Equality cases in Cauchy--Schwarz and the variation formula give the two rigid boundary equilibria. Integrating the generator balance against an invariant probability measure yields the stated second-moment bound.

The proof was checked for both signs of \(d\) and both signs of \(\sigma\); no dissipativity or global-boundedness assumption is silently used. Claims are conditional on bounded forward or bounded complete trajectories where stated.

## Originality

PASS, to the best of our knowledge.

The 1997 Sprott note gives the standard cyclic system and numerical bifurcation behavior. The 2016 Vaidyanathan--Azar chapter is described in accessible abstracts as treating qualitative properties, dissipativity, Lyapunov exponents, adaptive control, and synchronization. The 2025 Othman--Jalal paper gives the four-parameter cyclic form used here, local equilibrium stability, a transcritical bifurcation at \(a=-b-c\), and Hopf bifurcations.

The 2025 paper was inspected in full text. Its stated scope and conclusion are local bifurcation and stability results; searches in the full text for bounded, global, invariant, sphere, and mean did not reveal the balance/slab/invariant-measure statements proved here. Broader searches for the Halvorsen system together with boundedness, global convergence, invariant measures, mean-square constraints, diagonal sums, compact invariant sets, and the parameter combination \(a+b+c\) did not locate equivalent results.

The strongest residual risk is Vaidyanathan and Azar, “Adaptive Control and Synchronization of Halvorsen Circulant Chaotic Systems,” DOI 10.1007/978-3-319-30340-6_10: its full text was not inspected. Its accessible abstract does not advertise any of the present global identities, but the chapter does discuss qualitative properties of the same system. Sprott's later books were not directly inspected and remain a secondary risk because they collect structural facts about simple chaotic flows.

No concrete evidence of prior coverage of the sharp slab, the universal mean-square sphere law, the critical compact-invariant-set collapse, or the \(O((a+b+c)^2/d^2)\) invariant-measure second-moment bound was found.

## Value

PASS.

The result supplies exact global restrictions that are independent of the detailed periodic or chaotic structure of an attractor. The sharp slab provides a pointwise obstruction for every compact invariant set; the sphere law gives an exact diagnostic for any bounded trajectory or invariant measure; and the critical-surface theorem upgrades the known local equilibrium collision to a global exclusion of nontrivial compact recurrence. The second-moment estimate quantifies how all compact recurrent regimes must collapse in RMS amplitude as the transcritical surface is approached.

These conclusions are useful for analytical bifurcation studies and as exact consistency checks for numerical simulations of Halvorsen-type flows.

## Scientific limitations

The theorem does not establish existence of bounded attractors or periodic orbits for any parameter set, and it does not assert global existence for arbitrary initial data. The slab is a restriction on bounded complete trajectories, not a trapping region for every forward solution. The invariant-measure amplitude bound is a second-moment statement and does not by itself give a uniform pointwise bound on \(\|X\|\) inside a compact invariant set.

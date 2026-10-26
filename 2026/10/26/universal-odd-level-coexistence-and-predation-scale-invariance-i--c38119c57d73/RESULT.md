# Universal odd-level coexistence and predation-scale invariance in hierarchical ecological chains

## Finding

**Theorem (global ecological sorting and singular zero-predation boundary).** Fix an integer \(n\ge 3\). In the homogeneous hierarchical May–Leonard mean-field chain defined below, if all \(n\) species are initially present, reproduction exceeds mortality, and every predation rate is strictly positive, then every solution converges to an equilibrium. Exactly the odd-indexed species \(1,3,5,\ldots\) survive; every even-indexed species becomes extinct. The total surviving density is \(1-d/r\). Moreover, the normalized vector of limiting densities is independent of \(r\), \(d\), and any *common positive multiplier* of the predation rates. It is determined exactly by a triangular initial-value problem involving only the initial population ratios and the relative predation rates, as specified below.

For \(n=3\), this limiting composition has the closed form
\[
\frac{x_3(\infty)}{x_1(\infty)}
=\frac{x_3(0)}{x_1(0)}
 \exp\!\left(-\frac{p_2}{p_1}\frac{x_2(0)}{x_1(0)}\right).
\]

This positive-predation limit is **singular at zero predation**: setting all predation rates equal to zero first preserves every initially present species, whereas taking the long-time limit with any common positive predation intensity extinguishes every even-indexed species.

## Assumptions and scope

Consider the deterministic well-mixed population model for species \(1,\dots,n\), with vacancy fraction \(1-N\), where \(N(t)=\sum_{i=1}^{n}x_i(t)\):
\[
\dot x_1=x_1\bigl(r(1-N)-d\bigr),\qquad
\dot x_i=x_i\bigl(r(1-N)-d-p_{i-1}x_{i-1}\bigr)
\quad (2\le i\le n).
\]
The parameters satisfy \(r>d\ge 0\), \(p_i>0\) for \(1\le i<n\), and \(x_i(0)>0\) for all \(i\), with \(N(0)\le1\). Species \(i\) suppresses species \(i+1\), but not conversely. Every species has the same reproduction and intrinsic mortality rates. The statement concerns deterministic solutions, not finite-population stochastic extinction events.

Set \(a_1=1\), \(a_i=x_i(0)/x_1(0)\), and \(q_i=p_i/p_1\), with \(q_1=1\). Define \(Y_1(s)=1\) and, for \(2\le i\le n\), the triangular system
\[
Y_i(0)=a_i,\qquad
\frac{dY_i}{ds}=-q_{i-1}Y_{i-1}Y_i\quad(s\ge0).
\]
All \(Y_i\) remain positive. The theorem asserts that the limits \(L_i=\lim_{s\to\infty}Y_i(s)\) exist, with \(L_i>0\) for odd \(i\) and \(L_i=0\) for even \(i\), and that
\[
\lim_{t\to\infty}x_i(t)=
\left(1-\frac dr\right)
\frac{L_i}{\sum_{j\text{ odd}}L_j}.
\]
This also gives a constructive specification of every limiting abundance, with no assumptions of convergence inserted into its definition.

## Proof

**1. Forward invariance, persistence of total density, and the top species.** The positive simplex is forward invariant: each species equation contains its own density as a factor, and at \(N=1\) the total derivative is nonpositive. Put \(a=r-d>0\), \(P=\max_{i<n}p_i\), and \(Q(t)=\sum_{i=1}^{n-1}p_i x_i(t)x_{i+1}(t)\). Summing the equations gives
\[
\dot N=aN-rN^2-Q,
\qquad 0\le Q\le P N^2.
\]
Consequently \(\dot N\ge aN-(r+P)N^2\). Comparison with the scalar logistic equation shows
\[
\liminf_{t\to\infty}N(t)\ge \frac{a}{r+P}>0.
\]
Subtracting the logarithmic equations for \(x_i\) and \(x_1\) yields the exact identity
\[
\frac{x_i(t)}{x_1(t)}=a_i
\exp\!\left(-p_{i-1}\int_0^t x_{i-1}(u)\,du\right)
\le a_i\qquad(i\ge2).
\]
Thus \(N(t)\le Bx_1(t)\), where \(B=\sum_i a_i\). Hence \(x_1(t)\) is bounded below by a positive constant for all sufficiently large \(t\). In particular, the increasing ecological clock \(s(t)=p_1\int_0^t x_1(u)\,du\) tends to infinity.

**2. Reduction to a triangular chain and the parity induction.** In the new clock, the ratios \(Y_i(s(t))=x_i(t)/x_1(t)\) satisfy the claimed triangular equations; the dependence on \(r\) and \(d\) cancels exactly. The base case is \(Y_2(s)=a_2e^{-s}\), which is integrable. Whenever \(Y_{2j}\) is integrable, the equation for \(Y_{2j+1}\) gives
\[
L_{2j+1}=a_{2j+1}\exp\!\left(-q_{2j}\int_0^\infty Y_{2j}(s)\,ds\right)>0.
\]
Conversely, if \(Y_{2j+1}\) has a positive limit, then
\(Y_{2j+2}'=-q_{2j+1}Y_{2j+1}Y_{2j+2}\) forces \(Y_{2j+2}\) to decrease exponentially in \(s\), hence to be integrable. Induction establishes strict positivity of every odd limit and zero of every even limit through the final species. As \(s(t)\to\infty\) and \(0<x_1(t)\le1\), all even-indexed \(x_i(t)\) tend to zero.

**3. Total biomass and individual limits.** Every summand of \(Q(t)\) contains an even-indexed species, so \(Q(t)\to0\). The scalar differential equation \(\dot N=aN-rN^2-Q(t)\), the positive eventual lower bound on \(N\), and logistic comparison imply \(N(t)\to a/r\): for any sufficiently small \(\varepsilon>0\), eventually \(0\le Q(t)\le\varepsilon\); the lower comparison equation \(z'=az-rz^2-\varepsilon\) converges to its larger positive equilibrium, which tends to \(a/r\) as \(\varepsilon\downarrow0\), while \(\dot N\le aN-rN^2\) gives the upper limit. Since \(x_i/N=Y_i/\sum_jY_j\), the displayed formula for every limiting abundance follows.

**4. Exact three-species formula and parameter scaling.** For three species, \(Y_2(s)=a_2e^{-s}\) and
\[
Y_3(s)=a_3\exp\!\left[-q_2a_2(1-e^{-s})\right],
\]
so \(L_3=a_3e^{-q_2a_2}\). The triangular system depends on the predation rates only through their ratios \(q_i\), and not on \(r,d\); all dependences claimed in the finding follow. When every \(p_i=0\), all logarithmic growth rates are equal, so every initial population ratio remains fixed and \(N(t)\to1-d/r\). The even-indexed species then have strictly positive limits, unlike for any common positive predation intensity. Thus the two limit operations do not commute.

## Verification

The included `verify.py` independently integrates the physical ecological equations and the triangular ratio equations for three- and five-species instances, checks the three-species analytic formula, and tests parameter-scale invariance for multiple parameter choices. These finite numerical checks are corroborative only: the unrestricted-\(n\) result follows from the comparison argument and parity induction, not from finite simulations. Run with `python verify.py`; it uses the Python standard library.

## Relationship to prior work

Samanta et al. (arXiv:2609.09027v1, first posted 8 September 2026) introduce this directed hierarchical May–Leonard model. Their equations (4)–(5) are exactly the dynamical rules used here. Their Proposition 1 establishes that adjacent positive populations cannot coexist at equilibrium in the homogeneous case; their Theorem 1 and accompanying analysis give a bound on the number of coexisting species under the independent-set assumption, and Appendix B treats local stability for three- and five-species examples. Those equilibrium and local-stability statements do not establish which independent set every strictly positive initial condition selects, the global limit for arbitrary chain length, or the predation-scale-invariant limiting composition. The present theorem strengthens them on the fully seeded, identical-reproduction-and-mortality subfamily, without claiming the analogous conclusion for heterogeneous demographic rates.

Hou (arXiv:0711.3385) provides general criteria for a **single point** global attractor in competitive Lotka–Volterra systems. Here, for \(n\ge3\), the equilibria with positive odd coordinates form a continuum and different initial population ratios produce different limit points; therefore a theorem demanding one globally attracting equilibrium does not imply this initial-state-dependent selection formula. Calleja-Solanas et al. (2026) analyze invasion cycles through interaction-matrix structure, rather than the explicit feed-forward selection map of this acyclic path.

## Limitations

All species must be initially present. If the top species is absent, the surviving parity can shift; if an intermediate species is absent, the chain may split. A zero predation edge changes the limiting system discontinuously and is excluded from the positive-rate theorem. Unequal reproduction-to-mortality ratios destroy the cancellation behind the triangular flow. The result concerns an infinite, well-mixed deterministic population; demographic noise can ultimately extinguish even species predicted to persist at positive deterministic density. The all-species homogeneous assumption and initial-state dependence are essential. Literature searches cannot exclude an earlier equivalent result under different terminology.

## References

1. R. Samanta, S. Dawn, S. Jahiruddin, S. Bhattacharyya, C. Hens, and S. N. Chowdhury, *Selection Rules for Species Coexistence in a Hierarchical May–Leonard Model*, arXiv:2609.09027v1 (first posted 2026-09-08). https://arxiv.org/html/2609.09027v1
2. Z. Hou, *Global Attractor in Competitive Lotka–Volterra Systems*, arXiv:0711.3385 (2007). https://arxiv.org/abs/0711.3385
3. V. Calleja-Solanas et al., *A General Framework for Invasion Cycles in Ecology*, Ecology (2026), doi:10.1002/ecy.70380. https://doi.org/10.1002/ecy.70380

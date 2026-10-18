# Sharp tristability threshold in symmetric Snowdrift complex contagion

## Finding

For the two-strategy complex-contagion evolutionary ODE of Chiba-Okabe and Plotkin, a natural symmetric Snowdrift payoff line has a **sharp and exhaustive** transition from two attracting pure-strategy states to three attracting states, the third being coexistence. Write the complexity exponent as \(\gamma=1+k\) with \(k>0\), let the benefit-to-cost ratio be \(b/c=3/2\), and set \(\lambda=\alpha c\in(0,2)\). Here \(\alpha\) is the payoff-selection coefficient and \(c>0\) is the Snowdrift cost.

If \(0<k<1\), exactly three interior equilibria occur if and only if
\[
\boxed{2k<\lambda<2}. 
\]
They consist of two repelling threshold points \(x_-<1/2<x_+\) and the attracting mixed state \(x=1/2\). Both boundary equilibria \(x=0,1\) are also attracting, giving **exactly three attracting equilibria and five equilibria in total**. The basins of attraction, relative to \([0,1]\), are \([0,x_-)\), \((x_-,x_+)\), and \((x_+,1]\), respectively; trajectories starting exactly at a threshold remain at that threshold. If \(0<k<1\) and \(\lambda\le 2k\), or if \(k\ge1\), there is only one interior equilibrium \(x=1/2\), which repels; every other initial state tends to its nearer boundary equilibrium. At \(\lambda=2k\), the central equilibrium is nonhyperbolic but still repelling. This classification is global for every initial condition in the closed state interval and includes the transition equality.

The three-attractor regime is realized with exact rational fixed points by \(\gamma=3/2\), \(\alpha=1/9\), \(c=10\), \(b=15\):
\[
\operatorname{Eq}(F)=\{0,\,1/5,\,1/2,\,4/5,\,1\}.
\]
The stable points are \(0,1/2,1\); the two remaining points are repelling.

## Assumptions and scope

Fix \(\gamma>1\), \(\alpha>0\), \(c>0\), \(b=3c/2\), and \(0<\lambda=\alpha c<2\). The Snowdrift payoff matrix for cooperators (first row) and defectors (second row) is
\[
\begin{pmatrix}b-c/2&b-c\\b&0\end{pmatrix}=
\begin{pmatrix}c&c/2\\3c/2&0\end{pmatrix}.
\]
With \(x\in[0,1]\) denoting the cooperator fraction, the payoff difference is \(D(x)=c(1/2-x)\). We examine the following published continuum approximation as an autonomous ODE, **not** the exact underlying finite-population stochastic chain:
\[
\dot x=F(x):=x(1-x)\bigl[x^k(1+\lambda(1/2-x))-(1-x)^k(1-\lambda(1/2-x))\bigr].
\]
The strict condition \(0<\lambda<2\) implies \(1\pm\alpha D(x)>0\) on the whole interval, and \(k>0\) makes the vector field continuously differentiable on \([0,1]\). Thus solutions are unique and cannot cross equilibria; the interval is invariant. The symmetric payoff restriction fixes the ordinary Snowdrift mixed-strategy Nash point at \(1/2\), making it natural to study whether complex contagion changes its stability without shifting its location.

## Proof

**1. Exact scalar reduction.** Put \(z=1-2x\in[-1,1]\), \(k=\gamma-1>0\), and for \(-1<z<1\) define
\[
H_k(z)=\tanh\bigl(k\operatorname{artanh}z\bigr)
=\frac{(1+z)^k-(1-z)^k}{(1+z)^k+(1-z)^k}.
\]
A direct rearrangement of the ODE's bracket gives
\[
F(x)=x(1-x)\bigl[x^k+(1-x)^k\bigr]
\left[\frac{\lambda z}{2}-H_k(z)\right].
\]
The prefactor is positive for \(0<x<1\); therefore all interior equilibria are \(x=1/2\) and the nonzero solutions of \(H_k(z)/z=\lambda/2\), with symmetry \(z\mapsto-z\).

**2. Strict shape of the comparison curve.** For \(0<z<1\), write \(h=H_k(z)\). Direct differentiation yields
\[
h'=\frac{k(1-h^2)}{1-z^2},\qquad
h''=\frac{2k(1-h^2)(z-kh)}{(1-z^2)^2}.
\]
When \(0<k<1\), \(0<h<z\) because \(\tanh\) is strictly increasing; hence \(h''>0\). Thus \(H_k\) is strictly convex and \(H_k(z)/z\) strictly increases from \(k\) as \(z\downarrow0\) to \(1\) as \(z\uparrow1\). When \(k>1\), \(h>z\), so \(h''<0\), and the quotient strictly decreases from \(k\) to \(1\). For \(k=1\) it is identically \(1\). These claims also follow directly from the displayed derivatives and limits.

**3. Exhaustive equilibria and signs.** Because \(0<\lambda/2<1\), for \(0<k<1\) the equation \(H_k(z)/z=\lambda/2\) has exactly one \(z_*\in(0,1)\) if and only if \(k<\lambda/2<1\). It then gives exactly two additional interior equilibria \(x_-=(1-z_*)/2\) and \(x_+=(1+z_*)/2\). On the left half interval, the bracket has the sign of \(\lambda/2-H_k(z)/z\); on the right its sign reverses. Monotonicity gives the flow signs, in order between equilibria, \(-,+,-,+\). Therefore the endpoints and center attract, the off-center equilibria repel, and the exact three basins stated above follow by monotonic bounded convergence of scalar trajectories. If \(\lambda/2\le k\), that bracket is negative to the left and positive to the right: only the central, repelling, interior equilibrium remains. For \(k\ge1\), the quotient is everywhere at least \(1>\lambda/2\), so the same two-attractor conclusion holds. Every equilibrium on the open interval is thus accounted for.

**4. The critical equality.** In the case \(0<k<1\), the power series at \(z=0\) gives
\[
H_k(z)=kz+\frac{k(1-k^2)}3z^3+O(z^5).
\]
At \(\lambda=2k\), with \(v=x-1/2\), this yields
\[
\dot v=\frac{2^{2-k}k(1-k^2)}3v^3+O(v^5).
\]
The cubic coefficient is strictly positive. Thus \(x=1/2\) is nonhyperbolic and repelling, not neutrally stable. For \(\lambda>2k\), its linear derivative is \(F'(1/2)=-2^{-k-1}(\lambda-2k)<0\), while the two newly appearing off-center equilibria are repelling. This is the local subcritical pitchfork orientation for increasing \(\lambda\), and the ratio argument establishes its global completeness.

**5. Exact witness and slopes.** For \(k=1/2\) and \(\lambda=10/9\), set \(t=\sqrt{x/(1-x)}>0\). After multiplying the interior fixed-point equation by the positive factor \(9(1+t^2)\), it factors exactly as
\[
2(t-2)(t-1)(2t-1)=0.
\]
Consequently the only interior roots are \(x=1/5,1/2,4/5\). Exact differentiation of the original vector field gives
\[
F'(1/5)=F'(4/5)=\frac{2\sqrt5}{75}>0,
\quad F'(1/2)=-\frac{\sqrt2}{36}<0,
\quad F'(0)=F'(1)=-\frac49<0.
\]
These signs independently certify the claimed five-equilibrium configuration and local stability types in the explicit example. Strict inequality of all five slopes means the configuration persists under sufficiently small independent perturbations of the parameters within the full nonsymmetric Snowdrift family, although the exact reflection symmetry and central value \(1/2\) do not generally persist.

## Verification

The standalone script `verify_symmetric_snowdrift.py` performs exact SymPy checks of the cubic factorization, all three interior roots, their derivative signs, and both endpoint derivatives; it also runs eight qualitative numerical sign-pattern samples in other parameter regimes. Run it with `python verify_symmetric_snowdrift.py`. It completed successfully in the current check. The computational samples are illustrations, not a proof of the continuum parameter ranges; the global claims follow from Steps 1–4.

## Relationship to prior work

Chiba-Okabe and Plotkin, *Social learning with complex contagion* (arXiv:2406.14922, first submitted June 21, 2024; PNAS 2024), derive the precise continuum vector field used here and study Snowdrift, Donation, and Coordination games. Their Table 1, Snowdrift row for \(\gamma>1\), \(c<2/\alpha\), and \(b-c<1/\alpha\), labels both boundary equilibria stable and the interior equilibrium category “unstable & potentially non-unique.” In the stated open parameter subregime, the present theorem proves that a *stable* coexistence equilibrium is simultaneously present between two unstable interior thresholds, while both boundaries remain stable. Thus the original table’s broad cell does not describe the complete stability pattern: in particular, an unqualified reading that every interior equilibrium in that cell is unstable is disproved by the exact example. The theorem determines the **exact multiplicity, stability pattern, separating basins, and codimension-one boundary** in the symmetric Snowdrift family, including a rational five-equilibrium witness. The source’s general at-least-one-unstable statement is consistent with this theorem and is not disputed. More general conformist/contrarian models have pitchfork bifurcations but use different microscopic and payoff mechanisms; their phase diagrams do not directly imply the stated criterion for this ODE.

## Limitations

The threshold \(2(\gamma-1)\) is proved for the stated symmetric payoff ratio, not arbitrary Snowdrift payoffs. Robustness under small payoff asymmetry is local to the exact hyperbolic example and does not give a global classification of the asymmetric family. The result concerns the continuum, weak-selection approximation and does not claim finite-population fixation probabilities, stochastic metastability, or validity of the approximation for all microscopic parameters. The full arXiv HTML body, its linear-game arguments, Table 1, and appended supplement sections S1–S3 were inspected. A separate publisher-hosted supplementary PDF was not accessible for an independent text comparison; the literature search is not a uniqueness proof. No independent external audit is claimed.

## References

1. H. Chiba-Okabe and J. B. Plotkin, *Social learning with complex contagion*, arXiv:2406.14922 (initial posting 2024-06-21); *Proceedings of the National Academy of Sciences* **121** (2024), e2414291121, doi:10.1073/pnas.2414291121. Equation (2), Snowdrift payoff matrix, Table 1, and Materials and Methods (Linear Games).
2. F. Bagnoli and R. Rechtman, *Bifurcations in models of a society of reasonable contrarians and conformists*, *Physical Review E* **92** (2015), 042913, doi:10.1103/PhysRevE.92.042913 (different conformity setting, contextual comparison only).

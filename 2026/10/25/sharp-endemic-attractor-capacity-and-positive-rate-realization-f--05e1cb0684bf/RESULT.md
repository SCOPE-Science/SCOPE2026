# Sharp endemic-attractor capacity and positive-rate realization for arbitrary-order simplicial SIS dynamics

## Finding

Consider the scalar homogeneous mean-field SIS contagion model on a complete simplicial structure with all interaction orders through groups of \(M+1\) agents:
\[
\dot y=-\gamma y+(1-y)\sum_{j=1}^{M}\frac{s_j}{j!}y^j,\qquad 0\le y\le1,
\]
where \(M\ge1\) is an integer, \(\gamma>0\) is the recovery rate and all rescaled infection rates \(s_1,\ldots,s_M>0\). An *endemic equilibrium* is a zero in \((0,1)\); an *attractor* means a locally asymptotically stable equilibrium for this one-dimensional autonomous flow.

**Sharp capacity theorem.** For each \(M\), at most \(\lceil M/2\rceil\) distinct endemic equilibria can be locally asymptotically stable, allowing nonhyperbolic equilibria among those counted. This bound is attained by an open set of strictly positive rate vectors, with all \(M\) endemic equilibria simple. More strongly, for any prescribed distinct numbers \(0<r_1<\cdots<r_M<1\) satisfying \(\sum_{j=1}^M r_j<1\), there are explicit positive rates for which the endemic equilibrium set is exactly \(\{r_1,\ldots,r_M\}\). The attracting ones are precisely the roots \(r_j\) with \(M-j\) even.

Consequently, the least *maximum interaction-group size* admitting \(k\) distinct attracting endemic equilibria, among these homogeneous one-population models, is exactly \(2k\) for every integer \(k\ge1\). In particular, **three coexisting attracting endemic states require at least six-body transmission, and strictly positive rates with six-body transmission realize them robustly.**

## Assumptions and scope

The model is the deterministic one-dimensional polynomial mean-field equation (II.31) of Kiss, Iacopini, Simon and Georgiou, \(\mathrm{arXiv}:2309.12752\), in the equivalent factored form above. Group order \(j\) comprises a susceptible focal agent and \(j\) simultaneous infectious neighbors, so the maximum physical group size is \(M+1\); \(M\) is not the number of total agents or the number of endemic roots. The claim concerns equilibria of this deterministic model, **not** stationary positive infection fractions in a finite-population absorbing stochastic SIS process. All rates are positive, including those for every lower interaction order; no transmission coefficient is set to zero. The interval \([0,1]\) is positively invariant: at \(0\) the vector field is zero and at \(1\) it equals \(-\gamma\).

The upper bound holds for all positive real rates and includes degenerate cases. The construction holds for every prescribed ordered set with total below one and returns positive real coefficients; rational roots return rational rates. Strict inequalities ensure all constructed endemic equilibria are hyperbolic and persist with the same stability types under sufficiently small simultaneous rate perturbations.

## Proof

**1. Universal upper bound.** Divide the right-hand side by \(y>0\) and define
\[
P(y)=-\gamma+(1-y)\sum_{j=1}^{M}\frac{s_j}{j!}y^{j-1}.
\]
It is a polynomial of degree exactly \(M\), because the leading coefficient is \(-s_M/M!<0\). Each distinct positive endemic equilibrium is a zero of \(P\). For an isolated locally asymptotically stable equilibrium of a scalar analytic autonomous ODE, the vector field is positive immediately to its left and negative immediately to its right. Between any two distinct attracting equilibria the continuous field must therefore vanish at least once more. Thus \(k\) distinct attracting endemic equilibria demand at least \(2k-1\) distinct zeros in \((0,1)\), while \(P\) has at most \(M\) real zeros. Hence \(2k-1\le M\), or \(k\le\lceil M/2\rceil\). This argument does not assume hyperbolicity of the equilibria being bounded.

**2. A coefficient-positive root interpolation.** Fix \(0<r_1<\cdots<r_M<1\) with \(\sum r_j<1\), and set
\[
E(y)=\prod_{j=1}^{M}(y-r_j),\quad
\gamma=E(1)=\prod_{j=1}^{M}(1-r_j)>0,\quad
Q(y)=\frac{E(y)-E(1)}{y-1}=\sum_{j=1}^{M}b_j y^{j-1}.
\]
The quotient is a polynomial by the factor theorem. Write \(\sigma_i\) for the \(i\)-th elementary symmetric function of the roots, with \(\sigma_0=1\). Coefficient comparison using synthetic division shows
\[
b_{M-q}=\sum_{i=0}^{q}(-1)^i\sigma_i\qquad (q=0,\ldots,M-1).
\]
Because \(\sigma_1=\sum r_j<1\), each \(\sigma_i>0\) and
\[
(i+1)\sigma_{i+1}
=\sum_{j=1}^{M}r_j\,\sigma_i(r_1,\ldots,\widehat{r_j},\ldots,r_M)
\le\sigma_1\sigma_i<\sigma_i
\]
for \(1\le i<M\), where the hat omits one variable. Thus the \(\sigma_i\) decrease strictly for \(i\ge1\). Every alternating partial sum in the formula for \(b_{M-q}\) is at least \(1-\sigma_1>0\), by grouping the remaining terms as nonnegative successive pairs (and, if necessary, a positive last term). Therefore **every \(b_j>0\)**, despite the highly oscillatory desired endemic polynomial.

Choose \(s_j=j!\,b_j>0\). The defining identity \((y-1)Q(y)=E(y)-\gamma\) gives the *exact vector-field identity*
\[
\dot y=y[(1-y)Q(y)-\gamma]=-yE(y).
\]
The endemic roots are therefore exactly \(r_1,\ldots,r_M\), all simple. At \(r_j\), differentiation yields
\[
F'(r_j)=-r_j\prod_{\ell\ne j}(r_j-r_\ell),
\]
which is negative precisely when \(M-j\) is even. Their number is exactly \(\lceil M/2\rceil\). Strict positivity of rates, strictly interior roots, and nonzero derivatives imply persistence of this pattern in an open neighborhood by the implicit function theorem.

**3. Sharp interaction size and reproducible rational family.** For any \(M\ge1\), the choice
\[
r_j=\frac{j}{M(M+1)},\qquad j=1,\ldots,M,
\]
has \(\sum_j r_j=1/2\), giving positive rational rates for all \(M\). To get \(k\) attracting endemic states the upper bound requires \(M\ge2k-1\), hence group size \(M+1\ge2k\); taking \(M=2k-1\) meets that bound. For \(k=3\) one has \(M=5\), exact endemic roots \(1/30,1/15,1/10,2/15,1/6\), recovery rate \(\gamma=2639/4500\), and infection rates
\[
(s_1,s_2,s_3,s_4,s_5)=
\left(\frac{29689}{50625},\frac{211}{180},\frac{107}{30},12,120\right).
\]
The attracting roots are \(1/30,1/10,1/6\); the other two are hyperbolic repellers. No smaller maximal group size can support three attracting positive equilibria in this homogeneous one-population class.

## Verification

The companion `verify.py` implements polynomial products, synthetic division, exact rate recovery, the full identity \(F(y)=-yE(y)\), strict coefficient positivity and nonzero derivative signs using rational arithmetic only. It checks the explicit rational family for \(M=1,\ldots,20\) and a further 52 nonuniform rational-root configurations, with 72 completed test cases in total. The proof above, not finite enumeration, establishes the theorem for arbitrary \(M\) and admissible real roots. Execute `python verify.py` with Python 3. The script has no external dependencies and performs no scientific network access.

## Relationship to prior work

Kiss–Iacopini–Simon–Georgiou (2023), particularly equation (II.31), establish/formulate the arbitrary-order homogeneous mean-field dynamics and explicitly conjecture that increasing interaction order can allow arbitrarily many distinct endemic equilibria (discussion, pages 13–14 of the available manuscript). Their detailed bifurcation classifications address groups through four agents. The present capacity theorem answers the proposed all-order multiplicity question **for attracting endemic equilibria**, determines a sharp minimum group size and shows that the positivity constraints on *all* lower-order infection rates do not obstruct attaining the algebraic capacity.

Kiss–Bick–Simon (2024) study homogeneous and two-population low-dimensional reductions, with results for groups up to four agents in a single population and additional multistability from two-population coupling. Their multistable two-population examples do not contradict this **one-population** sharp bound. Iacopini and collaborators (2019) analyze lower-order simplicial contagion and associated discontinuous transitions. Generic scalar-polynomial root counting alone does not establish the constructive sharpness under strictly positive infection coefficients; the quotient-positive interpolation above supplies that missing admissibility step.

## Limitations

This is not a complete bifurcation classification as rates vary, does not describe basins beyond the one-dimensional equilibrium ordering, and assumes a single homogeneous population and complete simplicial mean-field dynamics. Multigroup models can support additional stable states at lower interaction orders; finite stochastic SIS processes on finite populations ultimately admit disease-free absorption. The arbitrary-order mean-field formula is analyzed as the stated deterministic model; no new all-order hydrodynamic-limit theorem is claimed. The source-by-source priority comparison is not an independent literature certification: uncatalogued broader positive-coefficient realization results may exist.

## References

1. I. Z. Kiss, I. Iacopini, P. L. Simon and N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures* (2023), arXiv:2309.12752, https://arxiv.org/abs/2309.12752 . Readable full text: https://nul.repository.guildhe.ac.uk/id/eprint/1505/1/higher_order_proofs%20(10).pdf .
2. I. Z. Kiss, C. Bick and P. L. Simon, *Decoding how higher-order network interactions shape complex contagion dynamics* (2024), arXiv:2410.15330, https://arxiv.org/abs/2410.15330 .
3. I. Iacopini et al., *Simplicial models of social contagion* (2019), arXiv:1810.07031, https://arxiv.org/abs/1810.07031 .

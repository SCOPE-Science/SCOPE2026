# Sharp high-recovery transport and correlation-length crossover in tandem exclusion

## Finding

Consider the thermodynamic stationary tandem exclusion process with the cooperative transitions \(110\to101\) at rate \(\alpha>0\) and \(101\to011\) at rate \(\beta>0\). Write \(q=\beta/\alpha\), let \(J(\rho,q)\) be the stationary particle current at density \(0<\rho<1\), and let \(\xi(\rho,q)\) be the stationary occupation correlation length (defined below). The exact current and correlation transfer matrix are established in [1].

**Theorem.** For every \(q>0\), the current \(\rho\mapsto J(\rho,q)\) has exactly one global maximizer \(\rho_*(q)\in(0,1)\). As \(q\to\infty\),
\[
1-\rho_*(q)=2^{-2/3}q^{-1/3}-\frac{2^{-4/3}}{3}q^{-2/3}+O(q^{-1}),
\]
\[
\frac{J(\rho_*(q),q)}{\alpha}=1-3\,2^{-2/3}q^{-1/3}+5\,2^{-4/3}q^{-2/3}+O(q^{-1}),
\]
and, for \(q>1\),
\[
\xi(\rho_*(q),q)=2^{-1/3}q^{1/3}-\frac13+O(q^{-1/3}).
\]
Define the stationary susceptibility by \(\chi(\rho,q)=\sum_{k\in\mathbb Z}\operatorname{Cov}(\eta_0,\eta_k)\). At the maximizing density,
\[
\chi(\rho_*(q),q)=1-2^{1/3}q^{-1/3}+O(q^{-2/3}),
\]
so the diverging optimal correlation length is accompanied by a vanishing correlation amplitude and finite limiting susceptibility.

For every **fixed** density \(\rho\in(0,1)\), the same model instead satisfies
\[
\xi(\rho,q)\sim\sqrt{q\rho(1-\rho)}\qquad(q\to\infty).
\]
The fixed-density coefficient corrects the expression in [1, Eq. (19)], which agrees with the exact transfer-matrix result only at \(\rho=1/2\). Thus optimizing the current creates a high-density boundary layer of width \(q^{-1/3}\) and changes the associated cluster-length growth from order \(q^{1/2}\) at fixed density to order \(q^{1/3}\) at optimal density.

## Assumptions and scope

The model is on a periodic one-dimensional lattice, with the thermodynamic limit taken at fixed density before the large-\(q\) limit. All rates are strictly positive. The density varies continuously in \((0,1)\) only at the thermodynamic level. There is no assertion about maximizing over integer particle numbers on a fixed finite ring. For \(q>1\), the subleading transfer eigenvalue is positive; \(\xi\) is the inverse negative logarithm of the ratio of its magnitude to the Perron eigenvalue. The current and the Gibbs transfer matrix used below are the existing stationary formulas of [1]. All asymptotic constants in this theorem concern the sequential thermodynamic/high-recovery limits, not an unspecified joint finite-size limit.

## Proof

Put \(s>0\) for the unique positive solution to the established thermodynamic density relation
\[
q(1-\rho)s^2+(1-2\rho)s-\rho=0.
\]
Solving for density gives the strictly increasing bijection
\[
\rho=\frac{s(1+qs)}{1+2s+qs^2},\qquad
\frac{d\rho}{ds}=\frac{1+2qs+qs^2}{(1+2s+qs^2)^2}>0.
\]
In particular, \(s\downarrow0\) corresponds to \(\rho\downarrow0\), and \(s\to\infty\) to \(\rho\uparrow1\). From the stationary current in [1, Eq. (10)], the normalized current becomes
\[
j_q(s):=\frac{J}{\alpha}=\frac{qs^2\{2+(q+1)s\}}{(1+s)(1+qs)(1+2s+qs^2)}.
\]
The same expression follows directly by averaging the two local transitions in the associated stationary two-state Markov chain: the conditional occupation probabilities are \(P(1\mid1)=qs/(1+qs)\) and \(P(1\mid0)=s/(1+s)\), so the normalized current is the density times \(P(1\mid1)P(0\mid1)+qP(0\mid1)P(1\mid0)\).

Exact differentiation gives
\[
\frac{dj_q}{ds}=-\frac{qsP_q(s)}{(1+s)^2(1+qs)^2(1+2s+qs^2)^2},
\]
where
\[
\begin{aligned}
P_q(s)={}&(q^3+q^2)s^5+4q^2s^4-(2q^2+2)s^3\\
&-(2q^2+8q+6)s^2-(5q+9)s-4.
\end{aligned}
\]
For every \(q>0\), these polynomial coefficients in descending powers have exactly one sign change. Descartes' rule, \(P_q(0)=-4<0\), and \(P_q(s)\to+\infty\) as \(s\to\infty\) show there is exactly one positive root \(s_*(q)\). The current increases before that root and decreases after it; since \(j_q(s)\to0\) at both endpoints, this gives the unique global maximizer for every \(q>0\).

For asymptotics set \(\varepsilon=q^{-1/3}\) and \(s=\varepsilon v\). Multiplying the stationarity polynomial by \(\varepsilon^4\) yields, on bounded \(v\)-intervals,
\[
\varepsilon^4P_{\varepsilon^{-3}}(\varepsilon v)
=v^5-2v^2-2\varepsilon v^3+O(\varepsilon^2).
\]
Let \(c=2^{1/3}\). The leading polynomial is negative at every fixed \(0<v<c\) and positive at every fixed \(v>c\). The unique positive root is consequently trapped between \((c-\delta)\varepsilon\) and \((c+\delta)\varepsilon\) for every fixed sufficiently small \(\delta>0\). Since the derivative of \(v^5-2v^2\) at \(v=c\) equals \(6c>0\), the implicit-function theorem gives the sharper expansion
\[
s_*(q)=c\varepsilon+\frac{c^2}{3}\varepsilon^2+O(\varepsilon^3).
\]
Substitute this expansion into the exact identity
\[
1-\rho_*(q)=\frac{1+s_*(q)}{1+2s_*(q)+q s_*(q)^2}
\]
and into \(j_q(s_*(q))\). Expansion through order \(\varepsilon^2\) gives
\[
1-\rho_*=\frac{c}{2}\varepsilon-\frac{c^2}{12}\varepsilon^2+O(\varepsilon^3),
\qquad
j_q(s_*)=1-\frac{3c}{2}\varepsilon+\frac{5c^2}{4}\varepsilon^2+O(\varepsilon^3),
\]
which are precisely the first two asserted expansions.

For correlations, the existing transfer matrix has Perron eigenvalue \(\lambda_+=1+s\), eigenvalue product \(\lambda_+\lambda_-=z(q-1)\), and fugacity \(z=s(1+s)/(1+qs)\). Hence the **exact** eigenvalue ratio simplifies to
\[
R_q(s):=\frac{\lambda_-}{\lambda_+}=\frac{(q-1)s}{(1+s)(1+qs)}\quad(q>1),
\qquad
\xi^{-1}=-\log R_q(s).
\]
At any fixed density \(0<\rho<1\), the density equation yields
\[
s=\sqrt{\frac{\rho}{1-\rho}}q^{-1/2}+O(q^{-1}).
\]
The exact ratio then implies
\[
\xi^{-1}=\log(1+s)+\log\left(1+\frac1{qs}\right)-\log(1-q^{-1})
=\frac{q^{-1/2}}{\sqrt{\rho(1-\rho)}}+O(q^{-1}).
\]
Both \(s\) and \(1/(qs)\) contribute at order \(q^{-1/2}\). Dropping the second term leads to the incorrect general-density prefactor printed in [1, Eq. (19)]; at \(\rho=1/2\) their leading contributions are equal and the published coefficient happens to agree.

At the maximizing density, the already established expansion for \(s_*\) instead gives
\[
\xi(\rho_*,q)^{-1}=c\varepsilon+\frac{2}{3c}\varepsilon^2+O(\varepsilon^3),
\]
and inversion, using \(c^3=2\), proves
\[
\xi(\rho_*,q)=c^{-1}\varepsilon^{-1}-\frac13+O(\varepsilon).
\]
Finally, the stationary two-state Markov representation implies \(\operatorname{Cov}(\eta_0,\eta_k)=\rho(1-\rho)R_q(s)^{|k|}\) at all integer separations \(k\). For \(q>1\), summing the geometric series gives
\[
\chi(\rho,q)=\rho(1-\rho)\frac{1+R_q(s)}{1-R_q(s)}.
\]
At the optimum, \(\rho_*(1-\rho_*)=(c/2)\varepsilon+O(\varepsilon^2)\) and \(1-R_q(s_*)=c\varepsilon+O(\varepsilon^2)\); their ratio tends to one. Substituting the two-order expansions above gives the sharper \(\chi=1-c\varepsilon+O(\varepsilon^2)\).

This concludes the proof.

## Verification

The standalone script `verify_tep.py` symbolically verifies the density parametrization, derivative factorization, Markov-chain current, transfer-eigenvalue ratio, and second-order singular expansions. It additionally performs independent direct-density numerical optimizations for eight recovery ratios, fixed-density correlation checks for four densities and three large recovery ratios, and optimized-asymptotic checks for five recovery ratios. It passed 67 groups of deterministic symbolic/numerical assertions in the provided environment. Numerical checks corroborate the proof; finite experiments do not prove uniqueness or asymptotics.

For orientation, at \(q=10^6\), the exact fixed-density correlation length at \(\rho=1/5\) is approximately \(399.9999\), whereas the coefficient in [1, Eq. (19)] would predict about \(1000\); the corrected leading law predicts \(400\). At the optimal density \(q=10^6\), the computed correlation length is approximately \(79.037\), compared with \(2^{-1/3}q^{1/3}-1/3\approx79.037\).

## Relationship to prior work

[1] introduces the tandem exclusion process, proves its stationary Gibbs structure, and derives its full thermodynamic stationary current and eigenvalue-based correlation-length formula. Those formulas are **not new here**. Its discussion establishes fixed-density \(J\to\alpha\rho\), sketches that the current maximum lies beyond half filling, and states an asymptotic correlation-length coefficient in Eq. (19). The present finding gives a global uniqueness proof, sharp simultaneous strong-recovery optimization (including second-order terms), and the previously unreported optimal-density correlation crossover. The direct algebraic simplification of [1]'s exact transfer ratio also corrects its general fixed-density asymptotic coefficient. The existence of an exact source formula means the new asymptotics can be derived from prior data; the distinct mathematical content is the nonuniform global-optimization analysis and the correctly coupled limiting regimes.

[2] studies token-mediated TASEP with independent token binding and scarcity, a related cooperative transport problem. Its transition rules and stationary density-current relation differ from the present nearest-neighbor tandem process, so its general observations about rate-dependent currents do not entail the stated coefficient or the quintic optimizer. Standard two-state transfer-matrix and implicit-function results are used as tools rather than claimed as discoveries.

## Limitations

The findings concern the thermodynamic, spatially homogeneous stationary model of [1]. In particular, no uniform finite-ring error bound is established as \(q\) grows, no current fluctuations or relaxation-time estimates are obtained, and no claim is made for boundary-driven, disordered, multicomponent, or token-driven variants. This proof does not independently rederive the underlying Gibbs stationarity theorem; it independently verifies the algebraic current and transfer-matrix consequences of the formulas in [1]. Priority over unpublished or unindexed treatments of the same singular optimization remains uncertain.

## References

[1] N. P. N. Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1 (first posted 2026-06-01), https://arxiv.org/abs/2606.01568 ; especially Eqs. (10)–(12), (17)–(19), and Appendix B.

[2] B. Kavčič and G. Tkačik, *Token-driven totally asymmetric simple exclusion processes*, Physical Review E **111**, 054122 (2025), DOI: 10.1103/PhysRevE.111.054122.

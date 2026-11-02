# A two-band concentration law for vacuum and excited Gaussian Fock modes

## Finding
Let \(e_j(z)=z^j/\sqrt{j!}\) be normalized analytic Bargmann–Fock monomials for \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). For each integer \(m\ge1\) and \(A>0\), define the robust two-state concentration
\[
\mathcal R_m(A)=\sup_{|\Omega|=\pi A}\min\left\{\int_\Omega|e_0|^2\,d\gamma,\ \int_\Omega|e_m|^2\,d\gamma\right\},
\]
where the supremum is over measurable subsets of the complex plane.

For \(m=1\), the unique optimal set, modulo planar null sets, is the concentric annulus whose squared radii lie in \([u,u+A]\), with \(u=A/(e^A-1)\). The two captured masses coincide and the exact optimum is \(e^{-u}(1-e^{-A})\).

For every \(m\ge2\), let \(t_m\in(m-1,m)\) be the unique positive solution of
\[
m(1-e^{-t_m})=t_m,
\]
and set \(a_m=e^{-t_m}\), \(b_m=e^{-t_m}t_m^m/m!\), \(\delta_m=b_m-a_m>0\),
\[
\alpha_m=\frac{b_m}{1+\delta_m},\qquad p_m=\frac{\delta_m}{1+\delta_m},\qquad c_m=(m!)^{1/m}.
\]
Then, as \(A\downarrow0\),
\[
\mathcal R_m(A)=\alpha_m A+O_m(A^2),\qquad
\sup_{u\ge0}\min_{j\in\{0,m\}}\int_u^{u+A}\frac{t^j e^{-t}}{j!}\,dt
=e^{-c_m}A+O_m(A^2),
\]
with \(\alpha_m>e^{-c_m}\). Consequently, for every sufficiently small positive area, the globally best robust mask outperforms every single concentric annulus. The leading coefficient is realized by the *two-component* radial squared-radius mask
\[
[0,p_m A]\ \cup\
[t_m-(1-p_m)A/2,\ t_m+(1-p_m)A/2].
\]
More strongly, if masks \(\Omega_A\) of area \(\pi A\) satisfy robust capture \(\alpha_m A-o(A)\), the normalized distributions of their squared radii, using *planar area* rather than Gaussian mass, converge weakly to
\[
p_m\delta_0+(1-p_m)\delta_{t_m}.
\]
For increasing excitation index, \(\alpha_m\sim(2\pi m)^{-1/2}\), whereas the best one-annulus coefficient is \(\exp(-(m!)^{1/m})\). Hence the improvement factor increases exponentially in the excitation index.

## Assumptions and scope
The mask is an arbitrary measurable planar set of finite prescribed Euclidean area, with no radial assumption in the definition of \(\mathcal R_m\). The objective protects **two specified pure monomial states separately**; it is not the least eigenvalue of the localization compression on their two-dimensional span when the mask is nonradial. Uniqueness in the \(m=1\) statement is modulo sets of Euclidean measure zero. The asymptotics at \(m\ge2\) hold for each fixed integer \(m\) as \(A\downarrow0\), not uniformly in \(m\).

## Proof
**1. Radial reduction and an upper certificate.** For a measurable \(\Omega\), let \(w(t)\in[0,1]\) denote the fraction of angles \(\theta\in[0,2\pi)\) for which \(\sqrt t e^{i\theta}\in\Omega\). Polar integration gives \(\int_0^\infty w(t)\,dt=A\) and the two concentrations \(\int w(t)f_0(t)\,dt\) and \(\int w(t)f_m(t)\,dt\), where \(f_j(t)=t^je^{-t}/j!\). This also covers arbitrary nonradial masks.

For \(m\ge2\), the ratio \(h_m(t)=t^m/(e^t-1)\) is zero at both endpoints of \((0,\infty)\). Its logarithmic derivative vanishes exactly when \(m(1-e^{-t})=t\). Strict concavity of \(m(1-e^{-t})-t\), its positive derivative at zero and its negative value at \(t=m\) show there is exactly one positive root \(t_m\). Moreover \(t_m>m-1\), because \(e^{m-1}>m\). Therefore \(h_m\) has one positive maximizer \(t_m\).

Put \(\theta=\alpha_m\). A rearrangement of the maximal-ratio inequality gives, for every \(t\ge0\),
\[
\theta f_0(t)+(1-\theta)f_m(t)\le\theta.
\]
Equality holds only at \(t=0\) and \(t=t_m\). Indeed the inequality is equivalent for \(t>0\) to \(h_m(t)\le h_m(t_m)\); at zero both sides equal \(\theta\). Since the pointwise minimum of two numbers is no greater than their convex average, integration yields the *nonasymptotic* inequality \(\mathcal R_m(A)\le\alpha_m A\).

**2. Why the two peaks are distinct and both needed.** For \(m\ge3\), arithmetic–geometric mean gives \(c_m<(m+1)/2\le m-1<t_m\). For \(m=2\), \(e^{\sqrt2}>1+\sqrt2+(\sqrt2)^2/2=2+\sqrt2\), implying \(2(1-e^{-\sqrt2})>\sqrt2\), hence \(t_2>\sqrt2=c_2\). Thus always \(t_m>c_m\), or \(b_m>a_m\). In particular \(0<p_m<1\), and equality in the upper certificate has exactly two separated possible radii. At \(t=c_m\), where \(f_0=f_m=e^{-c_m}\), strictness of that certificate yields \(e^{-c_m}<\alpha_m\).

**3. Matching construction.** For \(A>0\) sufficiently small, use the two disjoint squared-radius intervals shown in the finding. Their total length is exactly \(A\). Taylor expansion at zero and at the fixed interior point \(t_m\) gives the vacuum mass
\[
\big[p_m+(1-p_m)a_m\big]A+O_m(A^2)
\]
and the excited-mode mass
\[
(1-p_m)b_m A+O_m(A^2).
\]
The two leading coefficients both equal \(\alpha_m\), by the definition of \(p_m\). Combining the constructed lower bound with Step 1 gives \(\mathcal R_m(A)=\alpha_m A+O_m(A^2)\).

**4. One-annulus obstruction.** A single concentric annulus with area \(\pi A\) has squared-radius interval \([u,u+A]\), \(u\ge0\). The functions \(f_0,f_m\) have globally bounded derivatives, hence uniformly over \(u\ge0\), the quotient of the smaller captured mass by \(A\) differs by \(O_m(A)\) from \(\min\{f_0(u),f_m(u)\}\). The latter increases as \(f_m\) on \([0,c_m]\), then decreases as \(f_0\) on \([c_m,\infty)\) (note \(c_m<m\)). Its unique maximum is \(e^{-c_m}\). Choosing \(u=c_m\) supplies the matching lower bound. Since this coefficient is strictly below \(\alpha_m\), all single concentric annuli lose to the two-component construction when \(A\) is sufficiently small.

**5. Rigidity of nearly optimal masks.** For each \(\Omega_A\), the probability measure \(\nu_A=w_A(t)dt/A\) represents the squared radius under normalized planar area. If the robust captured mass is \(\alpha_m A-o(A)\), Step 1 implies \(\int[\alpha_m-\theta f_0-(1-\theta)f_m]d\nu_A=o(1)\). The bracket is continuous, strictly positive away from \(\{0,t_m\}\), and tends to \(\alpha_m>0\) at infinity. Therefore \(\nu_A\) is tight and every weak limit is supported on the two points. Both individual captured masses divided by \(A\) tend to \(\alpha_m\), since each is at least \(\alpha_m-o(1)\) and their strictly positive convex average is at most \(\alpha_m\). The limiting excited-mode mass forces the weight of \(t_m\) to be \(\alpha_m/b_m=1-p_m\). The limit is consequently unique.

**6. Adjacent-mode exception.** For \(m=1\), the density \(f_1(t)=te^{-t}\) has unique highest-density interval of every length \(A\), determined by the equality of its two endpoint values: \(u e^{-u}=(u+A)e^{-(u+A)}\), so \(u=A/(e^A-1)\). The bathtub principle makes this annulus the unique area-constrained maximizer of the first-excited-state capture over *all* planar masks. Because \(f_1'=f_0-f_1\), the vacuum and first-excited captures on that annulus coincide. The robust objective is always bounded above by the first-excited capture, so the same unique annulus maximizes the robust objective, with value \(e^{-u}(1-e^{-A})\).

Finally, \(t_m=m+O(me^{-m})\) follows from its defining equation, and Stirling's formula gives \(b_m\sim(2\pi m)^{-1/2}\), \(a_m=o(b_m)\), and \(\alpha_m\sim(2\pi m)^{-1/2}\). Since \(c_m\sim m/e\), the one-annulus coefficient is exponentially smaller.

## Verification
The standalone Python 3 checker `check.py` evaluates the stationarity equation, the two peak identities, strict small-window coefficient separation, sampled dual inequalities, direct Simpson quadratures of the proposed two-band masks, and the exact adjacent-mode mass identity. It passed 206 deterministic assertions. The uncountable pointwise inequality, all-area uniqueness, weak-limit statement, and asymptotic error bounds are established analytically above; the finite checks are not presented as an exhaustive certificate.

## Relationship to prior work
The standard Fock monomial diagonalization and Gamma-density reduction are classical. Galbis' 2021 preprint (subsequently published in 2022) establishes a universal area-based bound for radial Fock Toeplitz operators and bounds individual monomial captures, without formulating the two-state robust objective or deriving its separated limiting support. Huang and Xue (2023) generalize Galbis' integration inequalities, again pertaining to single-density norm estimates. The separate state objectives and their sharp joint small-area upper certificate are essential here; merely knowing each individual density's best annulus does not give this minimax law. The principal new distinction is the exact \(m=1\) versus \(m\ge2\) two-point optimal-support threshold, the strict one-annulus deficit, and rigidity of arbitrary near-optimal masks.

## Limitations
The result does not classify the exact optimizing sets at finite areas when \(m\ge2\), prove their topological disconnection among arbitrary nonradial masks, or control joint optimality over all superpositions in the two-mode span. The strength of the result for \(m\ge2\) is the sharp first-order concentration constant and rigidity as area tends to zero. Priority claims remain subject to possible unlocated earlier simultaneous-state optimization literature.

## References
1. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first public 2021-02-03); Complex Analysis and Operator Theory 16 (2022), article 15. https://arxiv.org/abs/2102.02031 ; https://doi.org/10.1007/s11785-021-01187-3
2. Y. C. Huang and F. Xue, *On Galbis' integration lemmas*, arXiv:2310.03050 (2023). https://arxiv.org/abs/2310.03050
3. Y. C. Huang and J.-Y. Zhang, *Norm bounds for self-adjoint Toeplitz operators with non-radial symbols on the Fock space*, arXiv:2405.11147 (2024). https://arxiv.org/abs/2405.11147

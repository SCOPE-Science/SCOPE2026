# Higher-rank panhandle polytopes have a Poisson width law and an exact geometric deficit

## Finding
For each fixed integer \(r\ge3\), a panhandle matroid base polytope loses a strictly positive but second-order-small amount of Euclidean mean directional width relative to the encompassing hypersimplex. In the balanced-growth regime the exact normalized loss is
\[
\mathcal D_r(\rho)=(r-1)\log(1+\rho)-\sum_{j=1}^{r-1}\frac{1-(1+\rho)^{-j}}j.
\]
Its full centered random-direction width has the Poisson-order-statistic limit specified below. The finite-rank coefficient is strictly increasing with the relative size of the excluded block and satisfies \(\mathcal D_r(\rho)=r(r-1)\rho^2/4+O_r(\rho^3)\) near zero.

## Assumptions and scope
Fix an integer \(r\ge3\). For integers \(p\ge r\), \(q\ge2\), set \(n=p+q\), \(d=n-1\), \(A=[p]\), and \(B=[n]\setminus A\). In the affine hyperplane \(\{x\in\mathbb R^n:\sum_i x_i=r\}\) use the induced Euclidean metric. The two polytopes are
\[
P_{r,p,n}=\operatorname{conv}\{\mathbf1_S:|S|=r,\ |S\cap A|\ge r-1\},\qquad
\Delta_{r,n}=\operatorname{conv}\{\mathbf1_S:|S|=r\}.
\]
These are the panhandle matroid base polytope and uniform-matroid hypersimplex, respectively. Let \(E=\{x\in\mathbb R^n:\sum_i x_i=0\}\), let \(U\) be Haar-uniform on its unit sphere, and define directional width \(W_K(U)=\max_{x\in K}\langle U,x\rangle-\min_{x\in K}\langle U,x\rangle\).

Assume \(p\to\infty\) and \(q/p\to\rho\in(0,\infty)\), with fixed \(r\). For the standard normal distribution function \(\Phi\), put \(u_p=\Phi^{-1}(1-1/p)>0\) and \(a_p=u_p^{-1}\). Let \(E_1,\ldots,E_r,E_*\) be independent rate-one exponential variables and \(\Gamma_j=E_1+\cdots+E_j\). Define
\[
H_{r,\rho}=-\sum_{j=1}^{r-1}\log\Gamma_j+\max\{-\log\Gamma_r,\log\rho-\log E_*\}.
\]
Let \(H'_{r,\rho}\) be an independent copy. Then, as \(p\to\infty\),
\[
\frac{\sqrt d\,W_{P_{r,p,n}}(U)-2r u_p}{a_p}\ \Longrightarrow\ H_{r,\rho}+H'_{r,\rho},
\]
and
\[
\lim_{p\to\infty}\frac{\sqrt d}{2a_p}\left(\mathbb EW_{\Delta_{r,n}}-\mathbb EW_{P_{r,p,n}}\right)=\mathcal D_r(\rho).
\]
Writing \(\gamma\) for Euler's constant and \(H_m^{\rm harm}=\sum_{j=1}^{m}1/j\), with \(H_0^{\rm harm}=0\), the individual mean has the refinement
\[
\mathbb E[\sqrt d\,W_{P_{r,p,n}}]=2ru_p+2a_p\left[r\gamma-rH_{r-1}^{\rm harm}+(r-1)+\log(1+\rho)+\sum_{j=1}^{r-1}\frac{1-(1+\rho)^{-j}}j\right]+o(a_p).
\]
The theorem does not assert these limits uniformly in growing rank or for \(\rho=0\) or \(\rho=\infty\).

## Proof
**1. Exact greedy support formula.** For independent Gaussian coordinate scores \(G=(X_1,\ldots,X_p,Y_1,\ldots,Y_q)\), list the \(X\)-scores in descending order \(X_{(1)}\ge\cdots\ge X_{(p)}\), and set \(Y_{(1)}=\max_jY_j\). Every permitted basis uses either the \(r\) largest \(X\)-scores or the \(r-1\) largest \(X\)-scores and the largest \(Y\)-score. Consequently
\[
h_P(G)=\sum_{j=1}^{r-1}X_{(j)}+\max\{X_{(r)},Y_{(1)}\},\qquad
h_\Delta(G)=\sum_{j=1}^rG_{(j)}.
\]
For all finite \(p,q,r\), the support difference is nonnegative. Both polytopes have constant coordinate sum \(r\), so replacing \(G\) by its orthogonal projection onto \(E\) subtracts the same constant from each support. Moreover \(W_K(G)=h_K(G)+h_K(-G)\) and \(\mathbb EW_K(G)=2\mathbb Eh_K(G)\) by Gaussian symmetry.

**2. An exact finite positive integral.** For real \(t\), let \(s(t)=1-\Phi(t)\), and let \(A_t\) and \(B_t\) be the respective numbers of \(X\)- and \(Y\)-scores exceeding \(t\). They are independent \(\operatorname{Bin}(p,s(t))\) and \(\operatorname{Bin}(q,s(t))\). For a threshold \(t\), the unrestricted maximum number of selected coordinates exceeding \(t\) is \(\min(r,A_t+B_t)\); the panhandle maximum is \(\min(r,A_t+\min\{B_t,1\})\). Layer-cake integration of the difference of the two sums of selected scores gives, with no Gaussian approximation,
\[
\mathbb E[h_\Delta(G)-h_P(G)]
=\int_{-\infty}^{\infty}\sum_{k=0}^{r-2}\Pr(A_t=k)
\sum_{\ell=2}^{r-k}\Pr(B_t\ge\ell)\,dt. \tag{1}
\]
This integral is strictly positive when \(p\ge r\), \(q\ge2\), because the integrand is positive on an interval.

**3. Extremal point process and directional-width law.** The classical normal extreme-value limit, centered at \(u_p\) and scaled by \(a_p\), makes the first \(r\) ordered \(X\)-scores converge jointly to \(-\log\Gamma_j\). The maximum of the \(q\) independent \(Y\)-scores converges jointly, under the *same* normalization, to \(\log\rho-\log E_*\). The upper and lower extreme processes converge jointly to independent copies, by multinomial Poisson convergence on disjoint upper and lower Gaussian tails. Applying the exact support formula gives
\[
\frac{W_P(G)-2ru_p}{a_p}\Longrightarrow H_{r,\rho}+H'_{r,\rho}.
\]
Indeed \(\sqrt d/\|G_E\|\to1\) in probability and its relative deviation is \(O_{\Pr}(d^{-1/2})\); because \(u_p^2=O(\log p)\) and \(d\asymp p\), the resulting radial error after division by \(a_p\) is \(O_{\Pr}(\log p/\sqrt p)=o_{\Pr}(1)\). Since \(U=G_E/\|G_E\|\), the angular statement follows.

**4. Expectation, exact coefficient and positivity.** Normal-maxima tail inequalities give uniform integrability of each of the finitely many scaled top order statistics and the pooled maximum: their positive tails are exponentially bounded, and their negative tails are bounded by a polynomial times a Poisson-type double exponential on the relevant central range; farther into the Gaussian left tail, the binomial bound improves further. Thus the centered support expectations converge as well as their laws. For a Poisson process with intensity \(\rho e^{-x}\,dx\), the upper \(r\) points are a shift by \(\log\rho\) of the unit-intensity process; hence the unrestricted expected top-\(r\) support exceeds the \(X\)-only support by \(r\log(1+\rho)\). The panhandle support exceeds the \(X\)-only support by
\[
C_r(\rho)=\mathbb E\left[\log\frac{\rho\Gamma_r}{E_*}\right]_+
=\int_0^1\frac{1-(1+\rho t)^{-r}}t\,dt
=\log(1+\rho)+\sum_{j=1}^{r-1}\frac{1-(1+\rho)^{-j}}j.
\]
The integral identity follows by conditioning on \(\Gamma_r\) and integrating the unit-exponential survival probability; the last equality follows by differentiation in \(\rho\) and the value zero at the origin. Therefore the scaled Gaussian support loss tends to \(r\log(1+\rho)-C_r(\rho)=\mathcal D_r(\rho)\). Since \(\mathbb EW_K(U)=\mathbb EW_K(G)/\mathbb E\|G_E\|\) and \(\mathbb E\|G_E\|/\sqrt d\to1\), this is exactly the stated mean angular-width limit with the factor two in the denominator.

For completeness, \(\mathbb E[-\log\Gamma_j]=\gamma-H_{j-1}^{\rm harm}\), which gives the individual mean expansion above. Finally,
\[
\mathcal D'_r(\rho)=\sum_{j=1}^{r-1}\left[\frac1{1+\rho}-(1+\rho)^{-j-1}\right]>0\quad(\rho>0),
\]
which proves strict positivity and monotonicity; a Taylor expansion at zero gives \(r(r-1)\rho^2/4+O_r(\rho^3)\).

## Verification
The accompanying stand-alone Python program `verify_width.py` checks 120 exhaustive finite basis optimizations against the greedy support formula, compares the exact positive binomial integral (1) to 160,000 independent Gaussian samples for \((p,q,r)=(4,3,3)\), and evaluates the fixed-rank coefficient against finite \((p,q)\) integrations at larger sizes. With the fixed reproducibility seed in the script, the simulation estimates \(0.23674741512508113\), the integral is \(0.23920176634808954\), and the simulation standard error is \(0.0011243664257310866\). The program ends `VERIFY_OK`. These finite checks are corroboration; the all-dimensional assertion depends on the analytic argument.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin introduced and investigated this precise panhandle family in Ehrhart theory (first public preprint 2022-01-28, arXiv:2201.12442). Deligeorgaki, McGinnis and Vindas-Meléndez investigated its Ehrhart positivity and chain-forest enumeration (first public preprint 2023-11-02, arXiv:2311.01640). Those enumerative results do not state this Gaussian-order-statistic width law. A previously obtained exact rank-two Schubert mean-width and Poisson law applies only at rank \(r=2\); the present claim is restricted to all fixed \(r\ge3\), with a genuinely higher-order extremal coefficient \(\mathcal D_r\), not the rank-two assertion. Standard normal extreme-value and Poisson point-process convergence are classical tools used, not claimed as inventions.

## Limitations
Originality is a best-knowledge assessment, not a mathematical uniqueness theorem. Equivalent formulations in older high-dimensional Gaussian support, matroid optimization, or extreme-value literature could exist. Finite examples and the checker cannot establish infinite limits. The theorem fixes \(r\) and requires \(\rho\in(0,\infty)\); no claim is made for a growing rank or endpoint block ratios. This work has not undergone independent mathematical validation.

## References
1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (first public 2022-01-28), https://arxiv.org/abs/2201.12442.
2. D. Deligeorgaki, D. McGinnis, A. R. Vindas-Meléndez, *Ehrhart Bounds for Panhandle and Paving Matroids Through Enumeration of Chain Forests*, arXiv:2311.01640 (first public 2023-11-02), https://arxiv.org/abs/2311.01640.
3. Classical normal extremal Poisson-process and gamma-arrival-time representation; used in the proof with derivations of the necessary finite-order assertions.

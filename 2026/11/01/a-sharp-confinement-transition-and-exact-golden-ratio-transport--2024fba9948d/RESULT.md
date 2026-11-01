# A sharp confinement transition and exact golden-ratio transport statistics for a remainder-added linear map

## Finding

For the real recurrence
\[
H_{a,k}(x)=\frac{x}{k}+\operatorname{rem}(ax,1),\qquad a,k>0,
\]
with signed truncation remainder, there is a sharp **confinement-versus-escape boundary at \(k=1\)**. If \(k>1\), every bounded set of initial conditions is eventually carried into a common compact interval; if \(0<k<1\), sufficiently remote initial points escape to infinity. At \(k=1\), every non-eventually-fixed orbit escapes in absolute value, but its movement is governed exactly by an expanding \(\beta\)-transformation rather than by a simple exponential law.

For the natural noninteger Markov calibration \(a=(\sqrt5-1)/2\), put \(\varphi=(1+\sqrt5)/2\). If the fractional phase at time zero is sampled from its explicitly described invariant probability, the displacement \(S_n=x_n-x_0\) on the positive half-line has, for every integer \(n\ge1\),
\[
\mathbb E S_n=\frac{n}{\sqrt5},\qquad
\operatorname{Var}(S_n)=nC_0+2\sum_{j=1}^{n-1}(n-j)C_j,
\]
where the *complete, exact autocovariance sequence* is
\[
C_j=\left(\frac12-\frac{\sqrt5}{5}\right)\varphi^{-j}
+\frac{\sqrt5-2}{10}(-\varphi^{-2})^j,\qquad j\ge0.
\]
Consequently,
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Var}(S_n)}{n}
=\frac{5+3\sqrt5}{50}.}
\]
The variance has a bounded finite-time correction, indeed
\[
\operatorname{Var}(S_n)=\frac{5+3\sqrt5}{50}n
-\frac{2+4\sqrt5}{25}+O(\varphi^{-n}).
\]
In particular, the exact asymptotic drift \(1/\sqrt5\), which also holds for Lebesgue-almost every positive starting point, differs from the unbiased value \(1/2\) at integer expansion coefficients.

## Assumptions and scope

Signed remainder means \(\operatorname{rem}(y,1)=y-\operatorname{trunc}(y)\), with truncation toward zero and \(\operatorname{rem}(0,1)=0\). Thus on nonnegative numbers the remainder is the usual fractional part \(\{y\}\), whereas on negative numbers the map is odd. Initial conditions are arbitrary real numbers in the confinement and escape assertions. The transport-statistical conclusions use \(k=1\), \(a=\varphi-1\), and a probability on one nonnegative phase cell \([j/a,(j+1)/a)\), \(j=0,1,\ldots\). Its pushforward under \(x\mapsto\{ax\}\) has the invariant density below. The statistical probability is a distribution on initial conditions; no external random forcing is applied to the recurrence.

Let \(t=\varphi^{-1}\), \(I_0=[0,t)\), and \(I_1=[t,1)\). The invariant phase density is
\[
h(u)=\begin{cases}
(1+t)/(1+t^2),&0\le u<t,\\
1/(1+t^2),&t\le u<1.
\end{cases}
\]
The phase-invariant distribution is equivalent to Lebesgue measure. Nothing here asserts a continuous compact global attractor for a discontinuous map, a Gaussian limit law, a security property, or the same coefficients for other real choices of \(a\).

## Proof

**1. Sharp confinement and escape.** The remainder is always bounded in absolute value by one. Thus
\[
|H_{a,k}(x)|\le k^{-1}|x|+1.
\]
For \(k>1\) the iterated bound is
\[
|x_n|\le k^{-n}|x_0|+\frac{k}{k-1}(1-k^{-n}).
\]
Every interval \([-R,R]\) with \(R>k/(k-1)\) is forward invariant and absorbs every bounded initial set. Conversely, the reverse triangle inequality gives
\[
|H_{a,k}(x)|\ge k^{-1}|x|-1.
\]
When \(0<k<1\), let \(L=k/(1-k)\). For every \(|x_0|>L\), induction gives
\[
|x_n|\ge L+k^{-n}(|x_0|-L)\longrightarrow\infty.
\]
Therefore no bounded interval can attract all initial conditions in that regime.

**2. Exact critical semiconjugacy and bounded-orbit criterion.** At \(k=1\), on the nonnegative half-line set \(u_n=\{ax_n\}\). Then
\[
x_{n+1}=x_n+u_n,\qquad
u_{n+1}=\{(a+1)u_n\},\qquad
x_n-x_0=\sum_{i=0}^{n-1}u_i.
\]
The second identity follows by taking fractional parts of \(a(x_n+u_n)\). In particular, the positive orbit is monotone. If it is bounded then \(\sum u_n<\infty\) and \(u_n\to0\). For sufficiently large \(n\), \(u_n<1/(a+1)\) and hence \(u_{n+1}=(a+1)u_n\). A nonzero term would then increase geometrically, contradicting convergence to zero. Thus some \(u_n=0\), and the original orbit becomes fixed. The converse is immediate. Oddness yields the corresponding statement on negative initial conditions. Thus every non-eventually-fixed critical orbit diverges to the relevant infinite endpoint.

**3. Golden-mean phase law.** Set \(a=\varphi-1\). The phase map is \(T(u)=\{\varphi u\}\), with two affine branches
\[
T(u)=\begin{cases}\varphi u,&u<t,\\\varphi u-1,&u\ge t.\end{cases}
\]
Its two Markov intervals have transitions \(I_0\to I_0\cup I_1\) and \(I_1\to I_0\), giving the primitive adjacency matrix \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\). The Lebesgue transfer operator is exactly
\[
(\mathcal Lg)(u)=\varphi^{-1}\left[g(u/\varphi)+\mathbf1_{[0,t)}(u)\,g((u+1)/\varphi)\right].
\]
Direct substitution proves \(\mathcal Lh=h\) for the stated positive normalized piecewise constant density. Expansivity and the primitive Markov partition give the standard unique mixing absolutely continuous invariant probability; its density is equivalent to Lebesgue. Direct integration yields
\[
\mu=\int_0^1 u h(u)\,du
=\frac{1+t^3}{2(1+t^2)}=\frac1{\sqrt5}.
\]
Ergodicity and the critical displacement sum give \(S_n/n\to\mu\) for almost every initial phase; positive density transfers this to Lebesgue-a.e. initial condition in every cell. In comparison, for any positive integer \(a\), the map \(u\mapsto\{(a+1)u\}\) preserves uniform Lebesgue probability and hence has mean phase \(1/2\); the noninteger golden drift is genuinely biased.

**4. Exact all-lag correlations.** On the four-dimensional vector space of piecewise affine densities, encode \(g\) by coefficients \((A_0,B_0,A_1,B_1)^\top\) such that \(g(u)=A_i u+B_i\) for \(u\in I_i\). The transfer operator acts by the exact matrix
\[
M=\begin{pmatrix}
\varphi^{-2}&0&\varphi^{-2}&0\\
0&\varphi^{-1}&\varphi^{-2}&\varphi^{-1}\\
\varphi^{-2}&0&0&0\\
0&\varphi^{-1}&0&0
\end{pmatrix}.
\]
Let \(h_0=(1+t)/(1+t^2)\), \(h_1=1/(1+t^2)\). The centered initial density \(g=(u-\mu)h(u)\) has coefficient vector
\[
v=(h_0,-\mu h_0,h_1,-\mu h_1)^\top.
\]
The exact algebraic identities
\[
\bigl(M^2-t^3M-t^3I\bigr)v=0,
\qquad C_0=\frac{3-\sqrt5}{10},\qquad C_1=\frac{\sqrt5-2}{10}
\]
follow by substitution and integration over \(I_0,I_1\), where
\[
C_n=\int_0^1(u-\mu)(\mathcal L^n g)(u)\,du.
\]
Consequently \(C_{n+2}=t^3(C_{n+1}+C_n)\) for all \(n\ge0\). Its characteristic roots are \(t\) and \(-t^2\), and the two initial values uniquely give the claimed two-exponential covariance formula, with no numerical extrapolation.

**5. Finite-time and asymptotic variance.** Stationarity makes the variance of \(S_n\) equal to \(nC_0+2\sum_{j=1}^{n-1}(n-j)C_j\). For \(|r|<1\), the exact finite sum is
\[
\sum_{j=1}^{n-1}(n-j)r^j
=\frac{r((n-1)-nr)+r^{n+1}}{(1-r)^2}.
\]
Substituting \(r=t\) and \(r=-t^2\) gives the displayed finite-time variance, its coefficient \(C_0+2\sum_{j\ge1}C_j=(5+3\sqrt5)/50\), and its constant correction \(-2\sum_{j\ge1}jC_j=-(2+4\sqrt5)/25\). The error term follows from \(|t|<1\). This establishes all statistical assertions.

## Verification

The standalone file `verify.py` uses exact SymPy algebra to check the invariant-density identities, the four-dimensional transfer operator, its eigenvalue factorization, the annihilating quadratic identity for the centered density, sixteen consecutive covariance identities, the all-time variance summation identity for sixteen finite values, and numerous exact rational orbit identities for integer expansion parameters. The proof above establishes the claims for all stated real parameters, phases and integers; the finite checks do not replace this proof.

## Relationship to prior work

The defining work of Moysis, Kafetzis, Baptista and Volos (2022), in its equations (4) and (23), introduces the same remainder-added linear map and investigates enhanced Lyapunov exponents, unstable periodic behavior, numerical diagrams and pseudo-random-bit generation. Its linear-map discussion does not determine the global confinement boundary or transport statistics at the neutral choice \(k=1\). The multiple-remainder extension by Moysis and collaborators (2023) studies Lyapunov and encryption properties of sums of remainder terms, not this critical single-remainder transport law.

The \(\beta\)-transformation and its Parry invariant density are classical. In particular, the golden-ratio invariant density and the resulting stationary mean are consequences of that general theory, and are **not claimed independently novel**. The contribution here is the exact unwrapped-orbit transition and the complete all-lag covariance and all-time transport-variance formulas for the defining remainder-added map. General rigorous diffusion-coefficient methods for expanding maps, such as Jenkinson, Pollicott and Vytnova (2018), prove existence and numerical approximation procedures in broad settings but do not state this exact value for this observable and model.

## Limitations

The parameter \(a=\varphi-1\) is a distinguished noninteger Markov slice, not a classification of all noninteger values. The variance is with respect to the invariant phase initialization, not an arbitrary finite-time ensemble. No independent mathematical review has been performed, and the precise publication-priority status of this exact transport coefficient remains subject to further specialist literature review. Discontinuous interval dynamics is treated in the forward absorbing-set sense, without asserting the existence of a compact global attractor in a topology that has not been specified. No claim is made about the security or quality of a pseudo-random-number generator.

## References

1. L. Moysis, I. Kafetzis, M. S. Baptista and C. Volos, “Chaotification of One-Dimensional Maps Based on Remainder Operator Addition,” *Mathematics* **10** (2022), article 2801; published 2022-08-07. DOI: 10.3390/math10152801.
2. L. Moysis et al., “Chaotification of 1D Maps by Multiple Remainder Operator Additions—Application to B-Spline Curve Encryption,” *Symmetry* **15** (2023), article 726. DOI: 10.3390/sym15030726.
3. O. Jenkinson, M. Pollicott and P. Vytnova, “Rigorous Computation of Diffusion Coefficients for Expanding Maps,” *Journal of Statistical Physics* **170** (2018), 221–253; first public 2017-11-30. DOI: 10.1007/s10955-017-1930-8.
4. C. Kalle, “Isomorphisms between positive and negative beta-transformations,” *Ergodic Theory and Dynamical Systems* (2014). DOI: 10.1017/ETDS.2012.127.

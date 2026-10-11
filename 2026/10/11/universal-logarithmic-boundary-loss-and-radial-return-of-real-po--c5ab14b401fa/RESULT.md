# Universal logarithmic boundary loss and radial return of real Poisson Schwarz contractivity

## Finding

For every fixed real exponent \(1\le p<\infty\), let \(N_p(r)\) be the sharp norm of the circle Poisson operator at radius \(0<r<1\), from real-valued, mean-zero \(L^\infty\) boundary data to normalized \(L^p\). Then
\[
\boxed{\displaystyle
\frac{N_p(r)}r=1-\frac4{\pi^2}(1-r)\log\frac1{1-r}+O_p(1-r),\qquad r\uparrow1.}
\]
Thus the first logarithmic relative loss has a universal positive coefficient independent of the finite exponent \(p\). In particular, for **every** finite \(p\ge1\) there is a radius \(r_p<1\) such that \(N_p(r)<r\) whenever \(r_p<r<1\).

For \(p>p_{\mathbb R}=4.1095286347363\ldots\), the opposite strict inequality \(N_p(r)>r\) holds for all sufficiently small positive \(r\). Consequently the sharp norm passes through equality at least once as the radius increases from zero to one. No uniqueness of crossing is claimed.

## Assumptions and scope

Work on \(\mathbb T=\{e^{i\theta}:0\le\theta<2\pi\}\) with probability measure \(dm=d\theta/(2\pi)\). Define
\[
P_rf(e^{i\theta})=\sum_{n\in\mathbb Z}r^{|n|}\widehat f(n)e^{in\theta},\qquad
N_p(r)=\sup_{\substack{f\in L^\infty(\mathbb T;\mathbb R),\ \widehat f(0)=0\\\|f\|_\infty\le1}}\|P_rf\|_{L^p(dm)}.
\]
The asymptotic is for **each fixed** finite exponent, not uniformly as \(p\to\infty\). All statements refer to real boundary functions, not the complex-valued sharp norm or the centered Poisson operator acting on data with nonzero mean.

The critical exponent \(p_{\mathbb R}\) is uniquely characterized by
\[
\left(\frac4\pi\right)^{p_{\mathbb R}}
\frac{\Gamma((p_{\mathbb R}+1)/2)}{\sqrt\pi\,\Gamma(p_{\mathbb R}/2+1)}=1.
\]
This exponent and the exact extremizer reduction are established in the cited work of Kovalev.

## Proof

**1. Exact real maximizer.** The real-valued boundary function \(f_*(e^{i\theta})=\operatorname{sgn}(\cos\theta)\) is admissible. Its harmonic extension is
\[
U(re^{i\theta})=\frac2\pi\arctan\frac{2r\cos\theta}{1-r^2}.
\]
Kovalev's Proposition 2.1 establishes \(N_p(r)=\|U(r\,\cdot)\|_p\) for every \(p\ge1\). Its underlying argument may be reconstructed as follows: a real harmonic extension \(u=P[f]\) of any admissible \(f\) has analytic completion \(F\) with \(F(0)=0\) and \(|\operatorname{Re}F|\le1\). The conformal map \(\Phi(z)=4\arctan(z)/\pi\) sends the disk onto this vertical strip. Thus \(\Phi^{-1}\circ F\) is a disk self-map fixing zero and \(u=\operatorname{Re}\Phi\circ(\Phi^{-1}\circ F)\). Schwarz's lemma and Littlewood's subordination inequality, applied to the subharmonic function \(|\operatorname{Re}\Phi|^p\), bound the integral mean of \(|u|^p\) by that of \(|U|^p\); \(f_*\) attains equality.

**2. Reduce the deficit to one singular integral.** Put \(a=(1-r^2)/(2r)\). Symmetry gives the exact expression
\[
N_p(r)^p=\frac2\pi\int_0^{\pi/2}
\left(\frac2\pi\arctan\frac{\cos\theta}{a}\right)^p d\theta.
\]
As \(r\uparrow1\), \(a\downarrow0\). For \(x>0\), use \(\arctan(x/a)+\arctan(a/x)=\pi/2\) and set \(x=\cos\theta\) to obtain
\[
1-N_p(r)^p
=\frac2\pi\int_0^1
\frac{1-\left(1-\frac2\pi\arctan(a/x)\right)^p}
{\sqrt{1-x^2}}\,dx.
\]
The integrand is between zero and \(1/\sqrt{1-x^2}\). For \(0<a<1/2\), the portion \(0<x<a\) therefore contributes \(O(a)\).

**3. Quantify the boundary logarithm.** On \(a\le x\le1\), set \(t=a/x\in[0,1]\). The function \(t\mapsto1-(1-(2/\pi)\arctan t)^p\) has two bounded derivatives on \([0,1]\) for each fixed \(p\ge1\), since its inner base is at least \(1/2\). Taylor's formula consequently gives, uniformly on this interval,
\[
1-\left(1-\frac2\pi\arctan t\right)^p
=\frac{2p}{\pi}t+O_p(t^2).
\]
The weighted error is bounded by a constant times
\[
a^2\int_a^1\frac{dx}{x^2\sqrt{1-x^2}}
=a\sqrt{1-a^2}=O(a).
\]
The leading integral is explicitly
\[
\int_a^1\frac{dx}{x\sqrt{1-x^2}}
=\log\frac{1+\sqrt{1-a^2}}a
=\log(1/a)+O(1).
\]
It follows that
\[
1-N_p(r)^p=\frac{4p}{\pi^2}a\log(1/a)+O_p(a).
\]
Taking the \(p\)-th root, with \(p\) fixed, yields
\[
N_p(r)=1-\frac4{\pi^2}a\log(1/a)+O_p(a).
\]
Finally \(a=(1-r)+O((1-r)^2)\) and \(1/r=1+O(1-r)\), giving precisely the asserted expansion for \(N_p(r)/r\). The positive logarithmic term dominates its \(O_p(1-r)\) remainder for \(r\) sufficiently close to one, proving eventual strict contractivity.

**4. Opposite behavior near zero.** As \(r\downarrow0\), the same exact maximizer formula gives \(U(re^{i\theta})/r\to(4/\pi)\cos\theta\) uniformly. Hence
\[
\lim_{r\downarrow0}\frac{N_p(r)}r
=\frac4\pi\|\cos\theta\|_{L^p(dm)}.
\]
This quantity exceeds one exactly for \(p>p_{\mathbb R}\), by the monotonicity of probability-normalized cosine moments and the defining equation of \(p_{\mathbb R}\). Continuity of the explicit integral for \(0<r<1\), combined with eventual strict contractivity, proves the claimed existence of an equality radius.

## Verification

The standalone script `verify_poisson_boundary.py` uses only Python's standard library. Running `python3 verify_poisson_boundary.py` checks twelve finite consistency assertions: angular quadrature against the independent Fourier-Parseval identity for \(p=2\) at four radii, the two opposite strict regimes for two supercritical exponents, and convergence toward the \(p\)-linear angular-deficit coefficient for four exponents. The latter numerical comparisons use loose finite-scale tolerances because the rigorous remainder causes slow inverse-logarithmic convergence. All twelve assertions passed on the packaged script. They corroborate but do **not** prove the all-radius or infinite-limit theorem.

For a separate analytic normalization check, Parseval gives
\[
N_2(r)^2=\frac8{\pi^2}\sum_{k\ge0}\frac{r^{4k+2}}{(2k+1)^2}.
\]
Differentiating yields
\[
\frac{d}{dr}N_2(r)^2=\frac8{\pi^2r}\log\frac{1+r^2}{1-r^2},
\]
which has the same logarithmic coefficient as the general calculation at \(p=2\).

## Relationship to prior work

Kovalev, *Schwarz-contractivity of the Poisson operator* (arXiv:2609.28938v1), determines the all-radius **critical exponent** for real boundary data and identifies the exact extremizer. The paper establishes the value of its normalized moment at the boundary radius but does not provide the sharp rate of approach for every finite exponent or the resulting radius-dependent return of strict contractivity above its critical exponent. The present result uses the published exact extremizer reduction but derives a different, quantitative near-boundary conclusion.

Brevig, Ortega-Cerdà and Seip, *A converse to the Schwarz lemma for planar harmonic maps* (arXiv:2011.10967), study first derivatives at the origin and Hardy dual-norm inequalities; those results do not give this \(L^\infty_0\to L^p\) radial norm asymptotic. Related small-time Poisson heat-content expansions for indicator sets concern different functionals and can explain analogous logarithms in special moments, but no inspected source establishes this full fixed-\(p\) operator-norm asymptotic and its supercritical crossing consequence.

## Limitations

The statement is asymptotic as \(r\uparrow1\) with fixed \(p\); it gives neither an explicit universal neighborhood of contractivity nor a complete classification of all crossing radii, and it does not extend to \(p=\infty\). It makes no claim for complex-valued data or for data with nonzero mean. Classical Poisson-semigroup perimeter/heat-content asymptotics and unindexed literature may contain overlapping techniques or equivalent special cases; the comparison does not certify global novelty or independent validation.

## References

1. L. V. Kovalev, *Schwarz-contractivity of the Poisson operator*, arXiv:2609.28938v1, 24 September 2026. https://arxiv.org/html/2609.28938v1
2. O. F. Brevig, J. Ortega-Cerdà and K. Seip, *A converse to the Schwarz lemma for planar harmonic maps*, arXiv:2011.10967v2 (2020). https://arxiv.org/abs/2011.10967
3. L. Acuña Valverde, *On the heat content for the Poisson kernels over the unit ball in the Euclidean space*, arXiv:1706.09477 (2017); *Bulletin of the London Mathematical Society* 52 (2020), 1093–1104. https://arxiv.org/abs/1706.09477

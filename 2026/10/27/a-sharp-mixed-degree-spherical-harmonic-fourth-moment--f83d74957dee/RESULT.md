# A sharp mixed-degree spherical-harmonic fourth moment

## Finding
Let \(\sigma\) be probability surface measure on \(S^2\subset\mathbb R^3\). Let \(\mathcal H_j\) be the complex-valued restrictions of homogeneous harmonic polynomials of degree \(j\), and put \(V=\mathcal H_1\oplus\mathcal H_2\). For every \(f\in V\),
\[
\int_{S^2}|f|^4\,d\sigma\le\frac{375}{112}\left(\int_{S^2}|f|^2\,d\sigma\right)^2.
\]
The constant is sharp. For nonzero \(f\), equality holds precisely when there are \(\gamma\in\mathbb C\setminus\{0\}\) and \(\omega\in S^2\) for which
\[
f(x)=\gamma\left[\sqrt{\frac{45}{32}}\,(\omega\cdot x)+\sqrt{\frac{85}{32}}\,P_2(\omega\cdot x)\right],\quad P_2(t)=\frac{3t^2-1}{2}.
\]
The two harmonic degrees are both essential: the sharp fourth-moment ratios on either summand alone are \(9/5\) and \(15/7\), respectively, strictly below \(375/112\).

## Assumptions and scope
The surface integral is normalized to total mass one; all norms in this note use this measure. The complex vector space is exactly the direct sum of degrees one and two, with the degree-zero constant term excluded. Every real-valued \(f\in V\) has a unique representation
\[
f(x)=\ell(x)+q(x),\quad \ell(x)=u\cdot x,\quad q(x)=x^{\mathsf T}Ax,
\]
where \(u\in\mathbb R^3\) and \(A\) is a real symmetric traceless \(3\times3\) matrix. Spherical surface points satisfy \(|x|=1\).

## Proof
Write \(\mathbb E\) for integration against \(\sigma\), and set \(U=|u|^2\), \(T=\operatorname{tr}(A^2)\), and \(M=u^{\mathsf T}A^2u\). The normalized even coordinate moments obey
\[
\mathbb E[x_1^{2a}x_2^{2b}x_3^{2c}]=
\frac{(2a-1)!!(2b-1)!!(2c-1)!!}{(2a+2b+2c+1)!!},\qquad a,b,c\ge0,
\]
with \((-1)!!=1\). These follow from rotational invariance or Gaussian radial factorization. Expansion gives the exact identities
\[
\begin{aligned}
\mathbb E\ell^2&=U/3,&\mathbb E q^2&=2T/15,\\
\mathbb E\ell^4&=U^2/5,&\mathbb E q^4&=4T^2/105,\\
\mathbb E(\ell^2q^2)&=(2UT+8M)/105.&
\end{aligned}
\]
For the quartic quadratic moment, rotational invariance makes it a degree-four symmetric polynomial in the eigenvalues of \(A\); under trace zero the only such invariant is proportional to \(T^2\), because \(\operatorname{tr}(A^4)=T^2/2\). Evaluation on \(A=\operatorname{diag}(-1,-1,2)\) fixes the coefficient \(4/105\). The mixed identity follows by the displayed sixth-order sphere moments. Odd-degree products \(\mathbb E\ell^3q\) and \(\mathbb E\ell q^3\) vanish under \(x\mapsto-x\).

Set \(s=U/3\), \(t=2T/15\), and \(S=s+t=\mathbb E f^2\). The eigenvalues of a real symmetric traceless \(3\times3\) matrix satisfy \(\|A\|_{\rm op}^2\le2T/3\): fixing one eigenvalue, the other two sum to its negative, and their squared sum is at least half its square. Thus \(M\le(2/3)UT\), with equality for nonzero \(u,A\) exactly when \(A\) has eigenvalues \((\lambda,-\lambda/2,-\lambda/2)\) and \(u\) belongs to the simple eigenline.

Substitution yields the *exact real deficit identity*
\[
\boxed{\begin{aligned}
\frac{375}{112}S^2-\mathbb E(\ell+q)^4
&=\frac{192}{35}\left(s-\frac{15}{32}S\right)^2\\
&\quad+\frac{16}{35}\left(\frac23UT-M\right).
\end{aligned}}
\]
Both terms are nonnegative. Equality forces \(s/S=15/32\) and axial alignment of \(u,A\). Since \(\mathbb E(\omega\cdot x)^2=1/3\) and \(\mathbb E P_2(\omega\cdot x)^2=1/5\), this gives exactly the displayed real extremizers, up to nonzero real scaling and reversal of \(\omega\).

Finally, for complex \(f=g+ih\) with real \(g,h\in V\), Cauchy–Schwarz and the sharp real inequality give
\[
\begin{aligned}
\mathbb E|f|^4&=\mathbb Eg^4+2\mathbb E(g^2h^2)+\mathbb Eh^4\\
&\le\frac{375}{112}(\mathbb Eg^2+\mathbb Eh^2)^2.
\end{aligned}
\]
If both parts are nonzero and equality holds, equality in Cauchy–Schwarz forces \(g^2=c^2h^2\) almost everywhere for some \(c>0\). The real-analytic functions \(g\pm ch\) have product zero identically on the connected sphere; hence one factor vanishes identically. Thus \(g,h\) are real multiples, so every complex equality case is a complex scalar times a real equality case. The cases where one part vanishes are included. This proves the claimed exhaustive classification.

## Verification
The standalone `check.py` uses the exact formula for all normalized sphere monomial moments and verifies six moment identities plus the two-term deficit for 125 explicitly constructed non-coaxial and coaxial rational matrix/vector configurations. It also integrates the normalized zonal degree-one and degree-two basis functions symbolically, confirms their pure and mixed fourth moments, and checks the exact optimizing square completion. It reports 1008 assertions passed. The proof of the universal theorem is analytical; these finite tests check the formulas but do not replace the reasoning for arbitrary coefficients.

## Relationship to prior work
Kwon and Lee, *Sharp \(L^p\)–\(L^q\) estimates for the spherical harmonic projection* (arXiv:1709.09795, initially public September 28, 2017), study single-degree spherical-harmonic projection bounds with constants implicit in asymptotic estimates. Their theorems do not determine the mixed degree-one/two, exact \(L^2\)-to-\(L^4\) norm or equality profiles here. Germain, *\(L^2\) to \(L^p\) bounds for spectral projectors on thin intervals in Riemannian manifolds* (arXiv:2306.16981, June 29, 2023), reviews spectral-window norm estimates and the distinct zonal and highest-weight concentration mechanisms. That framework motivates a question about spectral combinations but does not give this finite-band exact constant. A published result on sharp fourth moments of degree-two harmonics alone supplies the pure-degree comparison \(15/7\); optimizing the mixed cross moment and proving axial alignment are additional steps, not consequences of that pure-degree theorem alone.

## Limitations
This result is restricted to \(S^2\), the mean-zero band \(\mathcal H_1\oplus\mathcal H_2\), and exponent four. It makes no claim about adding the constant level, higher degrees, or higher-dimensional spheres. The literature comparison is best-knowledge rather than a guarantee that no equivalent theorem exists in unindexed work; independent mathematical validation has not occurred.

## References
1. Y. Kwon and S. Lee, *Sharp \(L^p\)–\(L^q\) estimates for the spherical harmonic projection*, arXiv:1709.09795 (first posted 2017-09-28), https://arxiv.org/abs/1709.09795 .
2. P. Germain, *\(L^2\) to \(L^p\) bounds for spectral projectors on thin intervals in Riemannian manifolds*, arXiv:2306.16981 (first posted 2023-06-29), https://arxiv.org/abs/2306.16981 .

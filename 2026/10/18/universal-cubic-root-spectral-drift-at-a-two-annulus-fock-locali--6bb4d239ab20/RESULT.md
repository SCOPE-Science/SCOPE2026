# Universal cubic-root spectral drift at a two-annulus Fock localization threshold

## Finding

A radial Toeplitz localization operator supported on two concentric thin annuli has a sharply classified maximal-eigenvalue location. At the unique annular separation where its Gaussian limiting profile develops a quartic-flat maximum, every maximizing monomial degree has a **universal negative cubic-root displacement**, although the annulus widths vary:

\[
\lim_{N\to\infty}\frac{k_N-N}{N^{1/3}}=-\sqrt[3]{2}.
\]

This is accompanied by a positive spectral-norm correction of exact order \(N^{-2/3}\). Above the threshold, the leading profile has two symmetric maxima, but the first asymptotic correction selects only the **lower-degree** maximum. The leading Gaussian profile itself, radial diagonalization, and general Gaussian smoothing are known ingredients, not claimed as new.

## Assumptions and scope

Let \(\mathcal F^2(\mathbb C)\) be the entire-function Hilbert space with measure \(\pi^{-1}e^{-|z|^2}\,dA(z)\), normalized monomials \(e_k(z)=z^k/\sqrt{k!}\), and orthogonal projection \(P\). Fix a shell half-width \(\delta>0\) and separation parameter \(a>\delta\). Write \(b=a-\delta\) and \(c=a+\delta\). For each positive integer \(N>c^2\), form the two disjoint squared-radius intervals

\[
E_N=[N-c\sqrt N,N-b\sqrt N]\cup[N+b\sqrt N,N+c\sqrt N]
\]

and let \(T_N f=P(\mathbf1_{\{|z|^2\in E_N\}}f)\). The operator is positive, compact and diagonal, with

\[
T_N e_k=\lambda_{N,k}e_k,\qquad
\lambda_{N,k}=\frac1{k!}\int_{E_N}e^{-t}t^k\,dt,\quad k\in\mathbb Z_{\ge0}.
\]

Set \(\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}\), \(\Phi(x)=\int_{-\infty}^x\varphi(u)\,du\), and

\[
g(x)=\int_{[-c,-b]\cup[b,c]}\varphi(u-x)\,du
=\Phi(c-x)-\Phi(b-x)+\Phi(-b-x)-\Phi(-c-x).
\]

For each \(\delta>0\), there is exactly one \(a_*(\delta)>\delta\) solving

\[
\log\frac{a_*+\delta}{a_*-\delta}=2a_*\delta.
\]

The following statements hold for **every** sequence of maximizing indices \(k_N\in\operatorname*{argmax}_{k\ge0}\lambda_{N,k}\):

1. If \(\delta<a<a_*(\delta)\), then \((k_N-N)/\sqrt N\to0\), and \(\|T_N\|\to g(0)\).
2. If \(a>a_*(\delta)\), let \(x_*>0\) be the unique solution of \(e^{-b^2/2}\sinh(bx_*)=e^{-c^2/2}\sinh(cx_*)\). Then \(0<x_*<a\), and \((k_N-N)/\sqrt N\to-x_*\). Moreover, defining

\[
h(x)=g'(x)+\frac{x}{2}g''(x)+\frac13g'''(x),
\]

we have \(h(x_*)<0\) and

\[
\|T_N\|=g(x_*)-N^{-1/2}h(x_*)+o(N^{-1/2}).
\]

3. If \(a=a_*(\delta)\), set

\[
q=(a-\delta)e^{-(a-\delta)^2/2},\qquad
\gamma_\delta=\frac{\varphi(0)q a\delta}{3}>0.
\]

Then every maximizing degree obeys

\[
\boxed{\displaystyle\lim_{N\to\infty}\frac{k_N-N}{N^{1/3}}=-\sqrt[3]{2}},
\]

and the operator norm has the sharper asymptotic

\[
\boxed{\displaystyle
\|T_N\|=g(0)+6\sqrt[3]{2}\,\gamma_\delta N^{-2/3}+o(N^{-2/3})}.
\]

The integer \(N\) centers the **squared-radius** shells. Centering ordinary radial distance instead would change the correction and is not asserted here. Parameters \(a,\delta\) stay fixed as \(N\to\infty\).

## Proof

**Step 1: exact diagonalization and localization.** Angular integration makes the monomials eigenvectors and yields the integral above, with the factorial \(k!\) as normalization. For fixed \(N\), the eigenvalues tend to zero as \(k\to\infty\), so a maximizing degree exists. The integral is the probability that a Gamma random variable with shape \(k+1\), unit scale, lies in \(E_N\). Its mean and variance both equal \(k+1\). Chebyshev's inequality, separately for degrees below \(N-K\sqrt N\), between \(N+K\sqrt N\) and \(2N\), and above \(2N\), gives

\[
\lim_{K\to\infty}\limsup_{N\to\infty}
\sup_{|k-N|>K\sqrt N}\lambda_{N,k}=0.
\]

The restriction \(k\ge0\) is included; the contribution from \(k>2N\) decreases uniformly with the distance from the shell. Since \(g(0)>0\), every maximizing degree is eventually within \(K\sqrt N\) for a sufficiently large fixed \(K\).

**Step 2: a uniform first-order Gamma expansion.** Put \(\epsilon=N^{-1/2}\), \(x=(k-N)/\sqrt N\), and \(t=N+u\sqrt N\). Stirling's formula, with its uniform remainder for \(k=N+O(\sqrt N)\), gives, for \(x\) in any fixed compact set and \(u\in[-c,c]\),

\[
\sqrt N\frac{e^{-t}t^k}{k!}
=\varphi(u-x)\left\{1+\epsilon\left[
\frac{x}{2}((u-x)^2-1)+\frac{(u-x)^3}{3}
\right]\right\}+O(\epsilon^2),
\]

where the remainder is uniform in \(x,u\). Integrating over the two shell intervals and applying the Gaussian Hermite integration identities yields

\[
\lambda_{N,k}=g(x)+\epsilon h(x)+O(\epsilon^2),
\qquad h(x)=g'(x)+\frac{x}{2}g''(x)+\frac13g'''(x).
\]

The limiting profile \(g\) is even and the first correction \(h\) is odd. These order estimates remain valid at a nearest-integer approximation of any prescribed bounded \(x\).

**Step 3: exact modality transition.** Differentiating the Gaussian interval integrals gives

\[
g'(x)=2\varphi(x)\left[e^{-b^2/2}\sinh(bx)-e^{-c^2/2}\sinh(cx)\right].
\]

For positive \(x\), the quotient \(\sinh(cx)/\sinh(bx)\) is strictly increasing from \(c/b\) to infinity because \(t\mapsto t\coth(tx)\) is strictly increasing. The function \(a\mapsto\log((a+\delta)/(a-\delta))-2a\delta\) is strictly decreasing from \(+\infty\) to \(-\infty\), proving existence and uniqueness of \(a_*\). If \(a<a_*\), the bracket in \(g'\) is negative throughout the positive axis, so \(g\) has a unique global maximum at zero. If \(a>a_*\), the bracket is initially positive and crosses zero exactly once: \(g\) has the two and only two global maxima \(\pm x_*\). Evaluating the quotient at \(x=a\) shows \(x_*<a\). At equality, \(g'\) is strictly negative for positive \(x\), yet its linear term vanishes.

**Step 4: strict selection of the negative peak above threshold.** Write \(f(x)=e^{-b^2/2}\sinh(bx)-e^{-c^2/2}\sinh(cx)\). At the positive root, define

\[
Q=e^{-b^2/2}\sinh(bx_*)=e^{-c^2/2}\sinh(cx_*)>0.
\]

Then \(f''(x_*)=-4a\delta Q\), \(f'(x_*)=Q[b\coth(bx_*)-c\coth(cx_*)]\), and direct substitution in \(h\) yields

\[
h(x_*)=2\varphi(x_*)\left(\frac{f''(x_*)}{3}-\frac{x_*f'(x_*)}{6}\right).
\]

Since \(0<c\coth(cx_*)-b\coth(bx_*)<c-b=2\delta\) and \(x_*<a\), its parenthesis is strictly less than \(Q\delta(-4a/3+x_*/3)<0\). Thus \(h(x_*)<0\) and \(h(-x_*)>0\). The compact-uniform expansion, strict quadratic maxima of \(g\) at both roots, and nearest-integer representatives show that the two local maximal eigenvalues are \(g(x_*)\pm\epsilon |h(x_*)|+o(\epsilon)\), selecting the negative root and giving the stated norm expansion.

**Step 5: quartic critical point and universal cubic-root displacement.** At \(a=a_*\), one has \(b e^{-b^2/2}=c e^{-c^2/2}=q\), so

\[
g''(0)=0,\qquad g^{(4)}(0)=2\varphi(0)q(b^2-c^2)=-24\gamma_\delta.
\]

Because \(g\) is even and \(h\) odd, Taylor expansion at the unique maximum gives

\[
g(x)=g(0)-\gamma_\delta x^4+O(x^6),\qquad
h(x)=-8\gamma_\delta x+O(x^3).
\]

Comparing a maximizer with \(k=N\) and using strict decay away from the origin first forces \(x=o(1)\). The inequality \(\gamma_\delta x^4\le C\epsilon |x|+C\epsilon^2\) then gives \(|x|=O(\epsilon^{1/3})\). Set \(y=(k-N)/N^{1/3}\), equivalently \(x=N^{-1/6}y\). For bounded \(y\), the same uniform Gamma expansion implies

\[
N^{2/3}(\lambda_{N,k}-g(0))
=-\gamma_\delta(y^4+8y)+o(1),
\]

uniformly on compact \(y\)-sets. The quartic polynomial has a **unique** maximizer at \(y=-\sqrt[3]{2}\), where its value is \(6\sqrt[3]{2}\gamma_\delta\). Integer lattice spacing in \(y\) is \(N^{-1/3}\to0\). Compactness of all maximizing \(y\)-sequences and uniqueness establish both critical asymptotics for every maximizing integer sequence.

## Verification

The bundled standard-library `verify.py` computes the Gamma eigenvalue integral by composite Simpson quadrature in the scaled coordinate, uses stable Gaussian CDF expressions, and checks the critical scalar equation, derivative identities, quartic coefficient, symmetry, strict negative-branch preference, representative finite-degree comparisons and consistency of the first-order expansion. It was executed successfully with **119 finite assertions**. These tests are reproducibility aids; the uniform asymptotics, infinite-index assertions and spectral classification are established by the proof above, not by finite experimentation.

## Relationship to prior work

Grudsky and Vasilevski (2002) established radial Fock Toeplitz diagonalization and related spectral theory. Esmeral and Maximenko (arXiv:1505.07906; first public version 2015-05-29), particularly Proposition 6.5, established the leading Gaussian-smoothing approximation to radial Toeplitz eigenvalue sequences. That leading smoothing, and the initial Gaussian profile, are **prior results** and not originality claims. Oldfield (arXiv:1404.2256, Theorem 2.4 and Corollary 2.5) proved global two-term Szegő and eigenvalue-counting asymptotics for anti-Wick localization under fixed-shape scaling; these do not directly give maximizing-degree selection for the moving two-annulus, quartic-critical family. The present narrow contribution is the explicit finite-size skewness selection, the universally normalized cubic-root degree displacement at the coalescence, and its exact norm correction.

## Limitations

The analysis is one complex-dimensional, assumes two equal-width symmetric **squared-radius** shells and fixed positive parameters, and concerns the maximal eigenvalue rather than all individual eigenvalues. It makes no assertion about parameter approaches to the critical curve as \(N\) varies, higher-dimensional Fock spaces, nonradial symbols, or arbitrary annulus arrangements. General Gamma Edgeworth theory might imply portions of the local calculation after specialized optimization, and an equivalent historical analysis of coalescing maxima may exist under different terminology. Historical priority and independent mathematical validation remain open.

## References

1. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (first submitted 2015-05-29), especially Section 6, Proposition 6.5. https://arxiv.org/abs/1505.07906
2. S. M. Grudsky and N. L. Vasilevski, *Toeplitz operators on the Fock space: radial component effects*, Integral Equations and Operator Theory **44** (2002), 10–37. https://doi.org/10.1007/BF01197858
3. J. P. Oldfield, *Two-term Szegő theorem for generalised anti-Wick operators*, arXiv:1404.2256 (2014), especially Theorem 2.4 and Corollary 2.5. https://arxiv.org/abs/1404.2256

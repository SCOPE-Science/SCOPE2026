# Sharp fourth-moment extension and a subfield localization dichotomy for binary inverse graphs

## Finding
Let \(q=2^m\), where \(m\ge1\), and define the zero-completed inverse map \(h:\mathbb F_q\to\mathbb F_q\) by \(h(0)=0\) and \(h(x)=x^{-1}\) for \(x\ne0\). On the inverse graph \(\Gamma=\{(x,h(x)):x\in\mathbb F_q\}\), the sharp Fourier extension inequality is
\[
\|Tf\|_{L^4(\mathbb F_q^2)}^4\le C_m\|f\|_{\ell^2(\mathbb F_q)}^4,\qquad
C_m=\begin{cases}3-2/q& m\text{ odd},\\4&m\text{ even}.\end{cases}
\]
Every nonzero extremizer is classified. For odd \(m\), it has the form \(f(x)=c\epsilon_x\) for every \(x\in\mathbb F_q\), where \(c\in\mathbb C\setminus\{0\}\) and \(\epsilon_x\in\{\pm1\}\). There are \(2^{q-1}\) extremizers up to nonzero complex scaling.

For even \(m\), choose \(\omega\in\mathbb F_4\subset\mathbb F_q\) of order three. The extremizers have support **exactly** \(a\mathbb F_4=\{0,a,\omega a,\omega^2a\}\) for a nonzero \(a\), and on this four-point support they have the form \(f(a\xi)=c\epsilon_\xi\) with \(\epsilon_\xi\in\{\pm1\}\), \(c\ne0\), and \(\prod_{\xi\in\mathbb F_4}\epsilon_\xi=1\). Thus there are \(4(q-1)/3\) projective extremizers. In particular, even-degree extensions have spatially localized equality cases, unlike odd-degree extensions.

## Assumptions and scope
Equip the input with counting measure, \(\|f\|_2^2=\sum_{x\in\mathbb F_q}|f(x)|^2\). Equip the output plane with probability measure \(q^{-2}\sum_{u,v\in\mathbb F_q}\), and let \(\psi:\mathbb F_q\to\{\pm1\}\) be any nontrivial additive character. Define \(Tf(u,v)=\sum_x f(x)\psi(ux+vh(x))\). All identities hold for arbitrary complex input functions, not only nonnegative coefficients. The case \(q=2\) is included in the odd-degree branch. The even-degree branch requires \(m\ge2\), so that \(\mathbb F_4\) is a subfield.

## Proof
**Pair-sum fibers.** Orthogonality of additive characters gives
\[
E(f):=\|Tf\|_4^4=\sum_{(s,t)\in\mathbb F_q^2}
\left|\sum_{\substack{x+y=s\\h(x)+h(y)=t}}f(x)f(y)\right|^2.
\]
Put \(N=\sum_x|f(x)|^2\). Because the field has characteristic two, all diagonal ordered pairs \((x,x)\) lie in the fiber \((0,0)\), contributing \(\left|\sum_x f(x)^2\right|^2\). Each off-diagonal unordered pair has two ordered representatives. Fixing its nonzero first-coordinate sum \(s\), the pair \(\{0,s\}\) has second-coordinate sum \(1/s\). Every pair with both entries nonzero has second-coordinate sum \(s/(xy)\); hence it shares the value \(1/s\) precisely when \(xy=s^2\). The corresponding roots solve \(X^2+sX+s^2=0\), equivalently \(z^2+z+1=0\) for \(z=X/s\). The latter has roots precisely when \(3\mid(q-1)\), i.e. when \(m\) is even. Other off-diagonal fibers contain a single unordered pair: specifying nonzero \(s\) and the second-coordinate sum determines \(xy\), hence determines the unordered root pair.

**Odd extension degree.** There are no exceptional collisions; expanding all singleton-pair fibers yields the exact identity
\[
E(f)=\left|\sum_x f(x)^2\right|^2+2N^2-2\sum_x|f(x)|^4.
\]
By the triangle inequality and Cauchy–Schwarz, \(\left|\sum_xf(x)^2\right|\le N\) and \(\sum_x|f(x)|^4\ge N^2/q\). Thus \(E(f)\le(3-2/q)N^2\). Equality requires all \(|f(x)|\) equal and all nonzero \(f(x)^2\) to have the same phase, which is equivalent to the displayed sign representation. Conversely every such function attains equality. Global sign is redundant under complex scaling, giving \(2^{q-1}\) projective classes.

**Even extension degree: exact collision formula.** The roots \(\omega s,\omega^2s\) produce the only exceptional collisions, so
\[
E(f)=\left|\sum_x f(x)^2\right|^2+2N^2-2\sum_x|f(x)|^4+
8\operatorname{Re}\sum_{s\ne0}f(0)f(s)\overline{f(\omega s)f(\omega^2s)}.
\]
Partition \(\mathbb F_q^\times\) into multiplication-by-\(\omega\) orbits \(O\) of size three. Write \(a=|f(0)|\), \(w_O=\sum_{x\in O}|f(x)|^2\), \(W=\sum_Ow_O\), \(S=\sum_Ow_O^2\); then \(N=a^2+W\). The last complex sum has magnitude at most \(3a\sum_O\prod_{x\in O}|f(x)|\), and \(\prod_{x\in O}|f(x)|\le(w_O/3)^{3/2}\). Also \(\sum_{x\in O}|f(x)|^4\ge w_O^2/3\) and \(\sum_Ow_O^{3/2}\le\sqrt{WS}\). Consequently
\[
E(f)\le 3N^2-2a^4-\tfrac23 S+\tfrac8{\sqrt3}a\sqrt{WS}.
\tag{1}
\]
By homogeneity take \(N=1\), and write \(A=a^2\), \(W=1-A\), and \(s=\sqrt S\), so \(0\le s\le W\). The bound (1) is
\[
3-2A^2-\tfrac23s^2+\tfrac8{\sqrt3}\sqrt{A(1-A)}\,s.
\tag{2}
\]
The quadratic (2) has its maximum at \(s_*=2\sqrt3\sqrt{A(1-A)}\). If \(0\le A\le1/13\), its unrestricted maximum is \(3-2A^2+8A(1-A)\le3+8/13<4\). If \(A\ge1/13\), then \(s_*\ge W\), so (2) increases over the admissible interval and its maximum is attained at \(s=W\). Put \(b=\sqrt{W/3}\), with \(N=a^2+3b^2\). At \(s=W\), (1) reduces to
\[
3N^2-2a^4-6b^4+24ab^3
=4N^2-3(a-b)^2(a^2+2ab+5b^2)\le4N^2.
\]
Equality forces \(a=b>0\), \(S=W^2\), and equality in every triangle, Cauchy–Schwarz and arithmetic–geometric mean step. The relation \(S=W^2\) forces exactly one nonempty \(\omega\)-orbit. The magnitude equalities then force the four nonzero coefficients to have common magnitude; diagonal equality forces their squares to have a common phase. After division by one nonzero scalar these coefficients are signs. Finally, each of the three exceptional cross terms is positive exactly when the product of the four signs is \(+1\). Conversely these four-point sign packets make every inequality above an equality. Each nonzero \(\omega\)-orbit corresponds to one of \((q-1)/3\) distinct \(a\mathbb F_4\) supports; on each support eight even-product sign vectors give four projective classes. Thus the projective count is \(4(q-1)/3\).

## Verification
The included standalone program `artifacts/verify.py` uses exact Gaussian-integer convolution over explicit models of \(\mathbb F_{2^m}\) for \(1\le m\le6\). It checks the pair-fiber classification, both fourth-moment identities, random complex-coefficient test cases, each asserted bound, sharp witnesses, and strict inequality after perturbing an even-degree packet. Reproduce with `python3 artifacts/verify.py`. The full quantifier range is proved algebraically above; finite checks do not constitute its proof.

## Relationship to prior work
Mockenhaupt–Tao established the finite-field restriction framework, principally for odd characteristic and paraboloids, rather than the weighted fourth moment of the zero-completed inverse graph in characteristic two. The classical differential classification of the inverse permutation distinguishes almost-perfect-nonlinear behavior in odd extension degree from four-uniformity in even extension degree. Carlet's work on inverse-function sum-free subspaces explicitly establishes inverse sums over subfield subspaces, subsuming the **existence** of the four-point zero-sum configuration here. The new claim is the *sharp complex-weighted fourth-moment norm and the exhaustive equality classification*, not the existence of the inverse-map collisions or subfield packets. González-Riquelme–Oliveira e Silva prove sharp extension results for other finite-field surfaces, including odd-characteristic hyperbolic paraboloids, but not this inverse graph. Priority relative to unindexed additive-energy or cryptographic literature is not guaranteed.

## Limitations
The result applies only to the zero-completed multiplicative inverse graph over binary fields. It concerns fourth-power \(\ell^2\to L^4\) extension with the specified counting/probability normalization and does not provide general higher-moment norms, stability estimates, or corresponding odd-characteristic inverse graph results. Differential uniformity and subfield vanishing are prior mathematical ingredients; their rediscovery is not asserted. Search cannot exclude a historically equivalent weighted formulation, and independent validation remains outstanding.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (first posted 2002-04-18), https://arxiv.org/abs/math/0204234.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (2024), https://arxiv.org/abs/2405.16647.
3. C. Carlet, *On the vector subspaces of finite binary fields over which the multiplicative inverse function sums to zero*, *Designs, Codes and Cryptography*, DOI 10.1007/s10623-024-01531-6, https://link.springer.com/article/10.1007/s10623-024-01531-6.
4. J. Jeong, N. Koo and S. Kwon, *New differentially 4-uniform permutations from modifications of the inverse function*, *Mathematics* 10 (2022), 4538, https://www.mdpi.com/2227-7390/10/23/4538.

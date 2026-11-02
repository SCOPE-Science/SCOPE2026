# Exact degree-three threshold for tied maximal coefficients on progression trinomials

## Finding
Let \(m\geq3\), \(n\geq2\), and let \(\alpha-\beta,\alpha,\alpha+\beta\in\mathbb N_0^n\) be distinct multi-indices of common total degree \(m\), with \(\beta\in\mathbb Z^n\setminus\{0\}\). For arbitrary complex \(a,b,c\), form
\[
P(z)=a z^{\alpha-\beta}+b z^\alpha+c z^{\alpha+\beta}.
\]
If \(P\) is a monomial, or if its two largest nonzero coefficient moduli coincide, then the coefficient Bohnenblust–Hille inequality holds with unit constant:
\[
\boxed{\bigl(|a|^{p_m}+|b|^{p_m}+|c|^{p_m}\bigr)^{1/p_m}\leq\|P\|_{\infty,\mathbb D^n},\qquad p_m=\frac{2m}{m+1}.}
\]
Equality among the admitted nonzero polynomials occurs exactly for monomials: the inequality is strict whenever at least two positive coefficients attain the common maximum. The unit constant is optimal for the union of monomials and tied-maximal-coefficient polynomials, and the sufficient degree threshold \(m=3\) cannot be reduced to \(m=2\): the unimodular-coefficient quadratic
\[
Q(z_1,z_2)=z_1^2+z_1z_2-z_2^2
\]
has \(\|Q\|_\infty=\sqrt5\) but coefficient \(\ell_{4/3}\)-norm \(3^{3/4}>\sqrt5\).

## Assumptions and scope
The field is complex. The norm is the supremum on the open unit polydisk, equivalently the maximum on its distinguished torus, not the Euclidean ball. The three exponent vectors form a nonconstant three-term arithmetic progression; their total degrees are all \(m\). There are no restrictions on the dimension, the step \(\beta\), or coefficient phases. The tie is between the two *largest positive* coefficient moduli, not necessarily the coefficients at the two ends. Monomials are also explicitly admitted. Zero coefficients are allowed. The claim is restricted to this exact three-term progression family; it asserts neither exact contractivity for arbitrary supports nor a general optimal Bohnenblust–Hille constant.

## Proof
**1. Torus and ellipse reduction.** On \(\mathbb T^n\), \(|z^\alpha|=1\), and \(z^\beta\) runs through all of \(\mathbb T\) since \(\beta\ne0\). Thus
\[
\|P\|_\infty=\max_{|w|=1}|a w^{-1}+b+cw|.
\]
Set \(u=|a|\), \(v=|c|\), \(h=|b|\). A common phase rotation and a reparametrization of \(w\) make the two outside coefficients nonnegative. The outside contribution then traces the ellipse
\[
(u+v)\cos\theta+i(v-u)\sin\theta.
\]
Write its semiaxes as \(s=u+v\) and \(d=|u-v|\), so \(s\geq d\geq0\). The location of the complex number of modulus \(h\) is the only remaining phase choice.

**2. A phase-minimization lemma.** The maximum modulus of \((s\cos\theta,d\sin\theta)+t\), over the ellipse, is minimized among all translations \(t\in\mathbb R^2\) with \(\|t\|_2=h\) when \(t\) lies on the minor-axis direction. In particular the minimum equals the peak for \(u w^{-1}+h-vw\).

Here is a proof including degeneracies. For \(s>d\), maximize the squared distance over the unit disk in \(x\in\mathbb R^2\). For a translation \(t=(t_1,t_2)\), the maximization apart from \(h^2\) is
\[
\max_{\|x\|_2\leq1}\left(s^2x_1^2+d^2x_2^2+2st_1x_1+2dt_2x_2\right).
\]
Completing two squares with a parameter \(\lambda>s^2\) gives the *exact* trust-region formula
\[
\inf_{\lambda>s^2}\left(\lambda+\frac{s^2t_1^2}{\lambda-s^2}+\frac{d^2t_2^2}{\lambda-d^2}\right).
\]
To verify exactness, if the infimum occurs at an interior parameter, stationarity gives \(\sum_i(s_i t_i/(\lambda-s_i^2))^2=1\), and this unit vector attains the completed-square upper bound. If the infimum is reached only as \(\lambda\downarrow s^2\), then necessarily \(t_1=0\); the limiting stationarity condition makes \(|dt_2/(s^2-d^2)|\leq1\), so choosing the first coordinate to complete a unit vector also attains the bound. This argument also covers \(d=0\), \(t=0\), and the zero linear term; if \(s=d\), the ellipse is a circle and the translation direction makes no difference. For each fixed \(\lambda>s^2\), the coefficient multiplying \(t_1^2\) is at least that multiplying \(t_2^2\), since \(x\mapsto x/(\lambda-x)\) is increasing. For \(t_1^2+t_2^2=h^2\), each expression, and hence its infimum, is minimized at \(t_1=0\). This proves the lemma. Maxima over the closed disk and its boundary coincide because the squared distance is convex; choosing the boundary never decreases the maximum.

**3. The two tie types.** Divide by the common positive maximal coefficient modulus. For a nonmonomial admitted polynomial, the two largest positive coefficient moduli tie. If the two outer coefficients tie, write \(u=v=1\), \(h=t\), \(0\leq t\leq1\). The lemma gives the universal bound
\[
\|P\|_\infty^2\geq4+t^2.
\]
If the middle and one outer coefficient tie, write \(u=h=1\), \(v=t\), \(0\leq t\leq1\), after possibly exchanging the outer coefficients. The lemma gives the sharp lower bound (over phases)
\[
\|P\|_\infty^2\geq M(t)^2:=\max_{-1\leq x\leq1}\{(2+2t+t^2)+2(1-t)x-4tx^2\}.
\]
Elementary maximization of the concave quadratic yields
\[
M(t)^2=\begin{cases}(2-t)^2,&0\leq t\leq1/5,\\[2mm]
1/(4t)+3/2+9t/4+t^2,&1/5\leq t\leq1.
\end{cases}
\]
Both tie types obey the same simple lower certificate
\[
\boxed{\|P\|_\infty^2>13/5+t+t^2.}
\]
For the outer tie this follows from \(4>13/5+t\). For the mixed tie at \(t\leq1/5\), the difference equals \(7/5-5t\geq2/5\). At \(t\geq1/5\), it equals \((25t^2-22t+5)/(20t)>0\), since the numerator has negative discriminant \(22^2-4\cdot25\cdot5=-16\) and positive leading coefficient.

**4. A coefficient certificate at exponent \(3/2\).** The three coefficient moduli after normalization are \(1,1,t\). For \(0\leq t\leq1\), the mean-value theorem for the function \(x\mapsto(2+x)^{4/3}\), the elementary inequalities \(2^{4/3}<13/5\) and \((4/3)3^{1/3}<2\), and arithmetic–geometric mean give
\[
(2+t^{3/2})^{4/3}\leq2^{4/3}+\frac43 3^{1/3}t^{3/2}
<13/5+2t^{3/2}\leq13/5+t+t^2.
\]
The two strict numerical inequalities can be checked by cubing positive quantities: \(16<(13/5)^3\) and \(64/9<8\). Therefore the coefficient \(\ell_{3/2}\)-norm is strictly less than \(\|P\|_\infty\) whenever the two maxima are positive and equal. Since \(p_m=2m/(m+1)\geq3/2\) for \(m\geq3\) and finite-dimensional \(\ell_p\)-norms decrease with \(p\), the asserted contractivity follows for every \(m\geq3\). A polynomial with one nonzero term has equality trivially, and makes the coefficient one sharp on the declared union.

**5. Exact failure at degree two.** On the torus, divide \(Q\) by \(z_1z_2\) and put \(w=z_1/z_2\). Then \(Q/(z_1z_2)=1+w-w^{-1}=1+2i\sin\theta\) when \(w=e^{i\theta}\), so \(\|Q\|_\infty^2=5\). Its coefficient \(\ell_{4/3}\)-norm is \(3^{3/4}\), which exceeds \(\sqrt5\) because the fourth powers satisfy \(27>25\). This exhibits three equal largest coefficient magnitudes and proves the stated degree cutoff sharp within this support subclass.

## Verification
The optional standalone `checker.py` runs finite exact-rational comparisons of the two algebraic lower certificates, strict polynomial positivity, and sampled complex-phase maxima; it also checks the low-degree counterexample. Its finite numerical scans are diagnostic, not substitutes for the trust-region argument or infinite-dimensional quantifiers. The independent proof steps requiring no numerical approximation are the exact trust-region dual, elementary scalar inequalities, and the explicit degree-two torus evaluation. Run with `python3 checker.py` in a Python 3 environment; no external packages are required.

## Relationship to prior work
Caro-Montoya, Núñez-Alarcón and Serrano-Rodríguez (first public version 23 July 2026) prove asymptotic contractivity of Bohnenblust–Hille constants under bounded variable incidence in monomials. Their theorem concerns degree-dependent optimal constants for all coefficients and does not imply exact constant one for a tied-largest-coefficient three-term arithmetic progression at degree three. A later work of Pellegrino and Teixeira (27 October 2026) proves exact contractivity under a largest-coefficient comparability hypothesis, but only beyond a very large general degree threshold \(M_N\). Its displayed formula for \(M_3\) is strictly larger than three, so its theorem does not supply the optimal degree-three statement or the explicit sharp degree-two boundary; its generic support results are credited, not claimed. Classical Fourier support and ellipse identities are standard tools, and the novelty claim is restricted to this particular sharp degree cutoff and coefficient tie class.

## Limitations
Apart from the separately admitted monomials, the condition that two maximal coefficient moduli tie is essential to the proof; no classification for unequal top magnitudes is asserted. The three exponent indices must be an arithmetic progression. Exact contractivity does not extend to *all* coefficient choices on that support: a sharply dominant center can violate it. The result does not determine the general three-term optimal Bohnenblust–Hille constant. A broader earlier sup-norm or coefficient-norm result may imply this special case; no assertion of independently certified publication priority is made.

## References
1. N. Caro-Montoya, D. Núñez-Alarcón, D. Serrano-Rodríguez, *Asymptotic Contractivity of Bohnenblust–Hille Constants with Bounded Monomial Support*, arXiv:2607.20847 (first posted 23 July 2026), *Bull. Braz. Math. Soc.* 57 (2026), article 40. https://arxiv.org/abs/2607.20847 and https://doi.org/10.1007/s00574-026-00527-1 .
2. D. M. Pellegrino, E. V. Teixeira, *Rigidity of Exact Contractivity in the Complex Polynomial Bohnenblust–Hille Inequality*, arXiv:2610.36887v1 (27 October 2026), Theorems A–B and Lemma 2.1. https://arxiv.org/html/2610.36887v1 .

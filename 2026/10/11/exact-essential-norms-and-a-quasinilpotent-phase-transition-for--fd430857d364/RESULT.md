# Exact essential norms and a quasinilpotent phase transition for affine composition commutators

## Finding
Let \(-1<\alpha<0\) and \(0<a,b<1\). In the weighted Dirichlet space \(\mathcal D_\alpha\), define \(\varphi_a(z)=1-a+az\), \(\varphi_b(z)=1-b+bz\), and
\[
K_{a,b}=C_{\varphi_a}C_{\varphi_b}^*-C_{\varphi_b}^*C_{\varphi_a}.
\]
Set
\[
c_1=1-a+\frac ab(1-b),\qquad
c_2=\frac{2-a-b}{b},\qquad
\theta=\frac{c_1}{c_2}.
\]
Since \(c_2-c_1=2(1-a)(1-b)/b>0\), \(0<\theta<1\). Then
\[
\boxed{\|K_{a,b}\|_{\mathrm{ess}}=(ab)^{-\alpha/2}(1-\theta)\theta^{\theta/(1-\theta)}.}
\]
Its Fredholm essential spectrum has an abrupt parameter transition:
\[
\boxed{\sigma_{\mathrm{ess}}(K_{a,b})=
\begin{cases}
[0,\|K_{a,b}\|_{\mathrm{ess}}],&a=b,\\
\{0\},&a\ne b.
\end{cases}}
\]
In particular, the Calkin image is nonzero and quasinilpotent for every \(a\ne b\), but is a nonzero positive element with an interval spectrum for \(a=b\). Along the diagonal, \(\|K_{a,a}\|_{\mathrm{ess}}=a^{-\alpha}(1-a)a^{a/(1-a)}\).

## Assumptions and scope
The unit disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and \(dA(z)=dx\,dy/\pi\). The Hilbert norm is
\[
\|f\|_{\mathcal D_\alpha}^2
=|f(0)|^2+(1+\alpha)\int_{\mathbb D}|f'(z)|^2(1-|z|^2)^\alpha\,dA(z).
\]
The essential norm is distance to compact operators. Essential spectrum means the spectrum in the quotient of bounded operators by compact operators, equivalently the set of scalars for which the shifted operator is not Fredholm. Only real parameters \(0<a,b<1\) and \(-1<\alpha<0\) are claimed. The cases \(a=1\), \(b=1\), and general linear-fractional maps are not included.

## Proof
**1. Reduction to weighted Bergman space.** The orthogonal decomposition \(\mathcal D_\alpha=\mathbb C\oplus\mathcal D_{\alpha,0}\), where the second summand consists of functions vanishing at zero, makes every composition operator a finite-rank perturbation of its compression to \(\mathcal D_{\alpha,0}\). Differentiation \(f\mapsto f'\) is unitary from this summand to the weighted Bergman space \(A^2_\alpha(\mathbb D)\). The compressed \(C_{\varphi_a}\) becomes
\[
(D_a g)(z)=a\,g(1-a+az).
\]
It follows that the Calkin class of \(K_{a,b}\) is represented by the commutator \(D_aD_b^*-D_b^*D_a\), up to a unitary equivalence and an additional finite-dimensional zero summand.

**2. Explicit Laplace model.** The Cayley transform \(w=(1+z)/(1-z)\) maps \(\mathbb D\) to the right half-plane. Under the standard weighted Bergman unitary, whose change-of-variable multiplier is proportional to \((w+1)^{-\alpha-2}\), the operator \(D_a\) becomes
\[
F(w)\longmapsto a^{-\alpha-1}F\!\left(\frac{w+1-a}{a}\right).
\]
This follows directly from \(\frac{1+\varphi_a(z)}{1-\varphi_a(z)}=(w+1-a)/a\) and \(w'+1=(w+1)/a\). The weighted Paley–Wiener transform \(F(w)=\int_0^\infty e^{-wt}f(t)\,dt\) identifies the Bergman space, up to a common constant factor in its norm, with
\[
H_\alpha=L^2((0,\infty),t^{-\alpha-1}\,dt).
\]
Let \((U_s f)(t)=s^{-\alpha/2}f(st)\) for \(s>0\), a unitary representation of the multiplicative group: substitution \(v=st\) verifies \(\|U_s f\|=\|f\|\) and \(U_sU_t=U_{st}\). For \(m_a(t)=e^{-(1-a)t}\), we obtain the exact unitary model
\[
D_a\ \simeq\ a^{-\alpha/2}M_{m_a}U_a.
\]
Indeed, the Laplace transform of \(a^{-\alpha}e^{-(1-a)t}f(at)\) is \(a^{-\alpha-1}F((w+1-a)/a)\).

**3. Calkin representative for the commutator.** From \(U_sM_g=M_{g(s\cdot)}U_s\) and \(U_b^*=U_{1/b}\), direct multiplication yields
\[
D_aD_b^*-D_b^*D_a
\ \simeq\ (ab)^{-\alpha/2}M_hU_{a/b},
\qquad h(t)=e^{-c_1t}-e^{-c_2t}.
\]
Here \(c_1=1-a+(a/b)(1-b)\) and \(c_2=(2-a-b)/b\), so \(0<c_1<c_2\) and \(h(t)>0\) for every \(t>0\).

**4. Exact essential norm.** Multiplication by a bounded continuous function on the nonatomic space \(H_\alpha\) has both operator norm and essential norm equal to its essential supremum: for each neighborhood of a maximizer there are infinitely many orthonormal functions supported in disjoint measurable subsets, annihilated asymptotically by any compact operator. Right multiplication by a unitary leaves the essential norm unchanged. Thus
\[
\|K_{a,b}\|_{\mathrm{ess}}=(ab)^{-\alpha/2}\sup_{t>0}\big(e^{-c_1t}-e^{-c_2t}\big).
\]
The strictly positive function inside the supremum vanishes at both endpoints and has exactly one critical point,
\[
t_*=\frac{\log(c_2/c_1)}{c_2-c_1}>0.
\]
Differentiating and substituting \(\theta=c_1/c_2\) gives \(h(t_*)=(1-\theta)\theta^{\theta/(1-\theta)}\), proving the norm formula and noncompactness.

**5. Essential spectrum on the diagonal.** If \(a=b\), then \(U_{a/b}=I\). The Calkin representative is multiplication by the real continuous function \(a^{-\alpha}h(t)\), whose essential range is the whole closed interval from zero to its maximum. The spectrum of a multiplication operator and the spectrum of its Calkin class both equal this essential range on a nonatomic measure space. Since \(\theta=a\), the stated explicit diagonal formula follows.

**6. Quasinilpotence off the diagonal.** Suppose \(r=a/b\ne1\), and put \(q=\max\{r,r^{-1}\}>1\). Since \(h(t)=O(t)\) as \(t\downarrow0\) and \(h(t)=O(e^{-c_1t})\) as \(t\to\infty\), there is a finite \(B>0\) such that
\[
0<h(t)\le B\min\{t,t^{-1}\}\qquad(t>0).
\]
The exact iterate formula is
\[
(M_hU_r)^n=M_{\prod_{k=0}^{n-1}h(r^k\cdot)}U_{r^n}.
\]
Writing \(t=r^u\), its multiplication coefficient is bounded by
\[
B^nq^{-\sum_{k=0}^{n-1}|u+k|}
\le B^nq^{-\lfloor n^2/4\rfloor}.
\]
The last inequality holds for every real \(u\), because the sum of absolute distances from the \(n\) consecutive integers has minimum \(\lfloor n^2/4\rfloor\) at a median. Hence
\[
\|(M_hU_r)^n\|^{1/n}
\le Bq^{-\lfloor n^2/4\rfloor/n}\longrightarrow0.
\]
Thus \(M_hU_r\) and its Calkin class have spectral radius zero. Every complex Banach-algebra element has nonempty spectrum, so the essential spectrum is precisely \(\{0\}\). On the other hand, Step 4 gives its strictly positive essential norm, hence the Calkin class is nonzero. In fact every positive integer power has nonzero essential norm, so the element is quasinilpotent but not nilpotent. This completes the proof.

## Verification
The argument is exact and analytic: it uses the unitary Paley–Wiener realization and does not extrapolate from finite matrices. Essential-norm sharpness is attained as a supremum over the full non-atomic half-line, not from a finite truncation. The identity \(c_2-c_1=2(1-a)(1-b)/b\), the differentiation at \(t_*\), and the median bound for multiplicative orbit products can be verified independently by substitution. No external computer certificate is required for any infinite-dimensional step.

## Relationship to prior work
He–Yan–Zhang–Zhao (2026, arXiv:2609.29897v1) classify Schatten membership and give essential norms for ordered products of linear-fractional composition operators in the nonnegative-weight range. In the negative-weight range they obtain two-sided estimates for each ordered product (Theorems 5.13 and 5.14), not an exact formula for the difference of the two products or for its essential spectrum. Their study motivates quantifying the commutator in the singular-weight range. Gu–He–Wang–Yan (2026, arXiv:2609.23667v1) treat individual composition-operator essential norms, including a boundary-tail formula. MacCluer–Narayan–Weir (2013, DOI:10.1080/17476933.2010.551202, especially Theorem 3.1) classify compactness of such commutators on weighted Bergman spaces; their theorem neither computes this weighted-Dirichlet norm nor its spectral phase transition. Chalendar–Partington (2023 version, arXiv:2204.05894v2) and Schroderus (2016 version, arXiv:1605.01859v3) treat spectra and norms of *individual* affine composition operators on half-plane spaces. A spectral statement for an individual operator does not determine the spectrum of the difference of two noncommuting products. The present computation instead reduces that difference to a weighted dilation with distinct endpoint decay.

## Limitations
The exact formula is restricted to real affine disk symbols with a common boundary fixed point, strict parameters \(0<a,b<1\), and singular weighted Dirichlet norms \(-1<\alpha<0\). It does not imply corresponding formulas for arbitrary linear-fractional pairs or for commutators on unrelated analytic spaces. Algebraic self-reductions may provide alternative proofs; such implicit coverage cannot be excluded solely by bibliographic searches. One older directly relevant paper on commutator compactness, Clifford–Levi–Narayan (2012), could be compared by its abstract and later exposition but its full text was not accessible for line-by-line inspection. The separate classification of compactness was already known in other analytic-space settings. This result is an exact norm-and-essential-spectrum statement, not a new general compactness criterion.

## References
1. L. He, Y. Yan, S. Zhang, X. Zhao, *Some Properties of Products of Linear Fractional Composition Operators on Weighted Dirichlet Spaces*, arXiv:2609.29897v1 (2026), Sections 3–5.
2. C. Gu, L. He, X. Wang, Y. Yan, *Closed Range and Essential Norms of Composition Operators on Weighted Dirichlet Spaces*, arXiv:2609.23667v1 (2026), Section 3.
3. B. D. MacCluer, S. K. Narayan, R. J. Weir, *Commutators of Composition Operators with Adjoints of Composition Operators on Weighted Bergman Spaces*, Complex Variables and Elliptic Equations 58 (2013), 35–54, DOI:10.1080/17476933.2010.551202.
4. J. H. Clifford, D. Levi, S. K. Narayan, *Commutator of Composition Operators with Adjoints of Composition Operators*, Complex Variables and Elliptic Equations 57 (2012), 677–686, DOI:10.1080/17476933.2010.534142.
5. I. Chalendar, J. R. Partington, *Composition Operators on Function Spaces on the Halfplane: Spectra and Semigroups*, arXiv:2204.05894v2 (2023).
6. R. Schroderus, *Spectra of Linear Fractional Composition Operators on the Hardy and Weighted Bergman Spaces of the Half-plane*, arXiv:1605.01859v3 (2016).

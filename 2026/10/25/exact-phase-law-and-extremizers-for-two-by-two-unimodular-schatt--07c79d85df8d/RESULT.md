# Exact phase law and extremizers for two-by-two unimodular Schatten-four Schur multipliers

## Finding

Let \(m=(m_{ij})_{1\le i,j\le2}\) have complex entries of modulus one and let \(S_m(X)=m\circ X\) act entrywise on complex \(2\times2\) matrices with the Schatten-four norm. Write
\[
\eta=\frac{m_{11}m_{22}}{m_{12}m_{21}}=e^{i\nu},\qquad c=\operatorname{Re}\eta=\cos\nu,\qquad -\pi<\nu\le\pi.
\]
Then the following formula is sharp for **every** such symbol:
\[
\boxed{\quad\|S_m\|_{S_4^2\to S_4^2}^{4}=
\frac{9-c+\sqrt{(9-c)^2-64}}{8}=:K(c).\quad}
\]
Moreover, its completely bounded Schatten-four multiplier norm has the same value:
\[
\boxed{\quad \|S_m\|_{\mathrm{cb},4}=K(c)^{1/4}.\quad}
\]
The equality of ordinary and completely bounded norms invokes the established two-by-two theorem of Arhancet [2]; the exact phase formula and its extremizers are proved below directly.

If \(\eta\ne1\), every nonzero ordinary norming matrix \(X=(x_{ij})\) has four equal nonzero entry moduli and its input cross-ratio
\(\zeta=x_{11}x_{22}/(x_{12}x_{21})\) equals the unique unit complex number
\[
\boxed{\quad
\zeta=\frac{c-K(c)-i\sin\nu}{3(K(c)-1)}.\quad}
\]
Conversely every nonzero matrix satisfying these two requirements attains the norm. If \(\eta=1\), then \(S_m\) is an isometry, and every nonzero input is norming.

In terms of \(\delta=|\nu|\in[0,\pi]\), the exact multiplier norm increases strictly from \(1\) to \(2^{1/4}\). Its small-phase behavior is
\[
\|S_m\|_{S_4^2\to S_4^2}
=1+\frac{\delta}{8\sqrt2}+O(\delta^2),\qquad\delta\downarrow0.
\]

## Assumptions and scope

The field is \(\mathbb C\), every entry of \(m\) has modulus exactly one, and the Schatten-four norm is unnormalized:
\(\|X\|_4=(\operatorname{Tr}((X^*X)^2))^{1/4}\). The completely bounded norm means the supremum of the norms of all finite matrix amplifications with the corresponding unnormalized Schatten-four norms. The theorem concerns precisely the two-by-two symbol family; it does not claim an exact formula for nonunimodular symbols, higher square sizes, or other exponents.

## Proof

**1. Reduction to one cross phase.** Multiplying rows and columns of the symbol by unit scalars conjugates its Schur action with left/right diagonal unitaries on the input and output. Consequently, its norm depends only on \(\eta\). We may put
\(m=\begin{pmatrix}1&1\\1&e^{i\nu}\end{pmatrix}\).
For a nonzero input \(X=\begin{pmatrix}a&b\\g&d\end{pmatrix}\), the two singular values give the identity
\[
\|X\|_4^4=\big(|a|^2+|b|^2+|g|^2+|d|^2\big)^2-2|ad-bg|^2.
\]
The Schur action preserves the first parenthesized term and changes \(ad-bg\) to \(e^{i\nu}ad-bg\).

**2. Amplitude reduction is exact.** Put \(u=|ad|\), \(v=|bg|\), and \(F=|a|^2+|b|^2+|g|^2+|d|^2\). The elementary inequalities \(|a|^2+|d|^2\ge2u\) and \(|b|^2+|g|^2\ge2v\) yield \(F\ge2(u+v)\); equality holds exactly when \(|a|=|d|\) and \(|b|=|g|\). If either product vanishes, the norm ratio is one. Otherwise write \(ad\overline{bg}=uv e^{i\theta}\). Set \(A=|ad-bg|^2\) and \(B=|e^{i\nu}ad-bg|^2\). The fourth-power ratio is
\[
Q(F^2)=\frac{F^2-2B}{F^2-2A}.
\]
Whenever \(Q>1\), one has \(A>B\) and
\(\frac{d}{d(F^2)}Q=2(B-A)/(F^2-2A)^2<0\).
Thus any maximizer with ratio greater than one must have \(F=2(u+v)\), and the fourth-power ratio becomes
\[
Q=\frac{1+p(1+\cos(\theta+\nu))}{1+p(1+\cos\theta)},\qquad
p=\frac{2uv}{(u+v)^2}\in(0,1/2].
\]
For a ratio above one this expression is strictly increasing in \(p\). Its maximum therefore has \(p=1/2\), equivalently \(u=v\). Combining with the preceding equalities forces \(|a|=|b|=|g|=|d|>0\). Conversely every relative phase \(\theta\) is available with four equal entry moduli, so the exact optimization is
\[
\|S_m\|_{4\to4}^{4}=
\max_{\theta\in\mathbb R}\frac{3+\cos(\theta+\nu)}{3+\cos\theta}.
\]
For \(\eta\ne1\), this maximum exceeds one because the cosine difference is positive at a suitable \(\theta\). For \(\eta=1\), the symbol factors into row and column phases and is an isometry.

**3. Sharp phase maximization.** For \(k\ge1\), the inequality
\(3+\cos(\theta+\nu)\le k(3+\cos\theta)\) for all real \(\theta\) holds exactly when
\[
3(k-1)\ge\sqrt{(c-k)^2+\sin^2\nu}=
\sqrt{k^2-2ck+1}.
\]
Squaring, with both sides nonnegative, is equivalent to
\[
8k^2-2(9-c)k+8\ge0.
\]
For \(c<1\) its larger root exceeds one and is \(K(c)\), whereas the smaller root is below one. Hence the least admissible \(k\ge1\) is \(K(c)\). Equality in the cosine maximization is achieved only by
\[
\cos\theta=\frac{c-K(c)}{3(K(c)-1)},\qquad
\sin\theta=-\frac{\sin\nu}{3(K(c)-1)}.
\]
The root equation shows that the right sides form a unit vector. This proves both the norm formula and the complete ordinary-norming classification. A canonical witness is
\(X=\begin{pmatrix}1&1\\1&e^{i\theta}\end{pmatrix}\), with \(\theta\) as above; at \(\delta=\pi\) this gives \(X=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\).

**4. Amplified norm.** Arhancet [2, Theorem 3.2] proves that for **every** complex \(2\times2\) Schur symbol on \(S_4^2\), its completely bounded norm equals its ordinary norm. Applying this published theorem to the directly computed formula gives the stated cb identity. The elementary proof in Steps 1–3 does not by itself establish the amplification claim.

**5. Endpoint and expansion.** The function \(9-c\) increases strictly as \(\delta\) runs from zero to \(\pi\), and the larger quadratic root is strictly increasing for \(c<1\). At \(c=1\) it equals one, and at \(c=-1\) it equals two. Since \(c=1-\delta^2/2+O(\delta^4)\), the square root in \(K(c)\) is \(2\sqrt2\,\delta+O(\delta^3)\); consequently \(K(c)^{1/4}=1+\delta/(8\sqrt2)+O(\delta^2)\).

## Verification

The standalone `check_s4_phase.py` requires Python 3 and NumPy. Running it performs 8,418 deterministic tests: an algebraic quadratic-root check and explicit norming witness at seven phases, 8,400 random complex-matrix inequality checks, and four row/column phase-gauge checks. The analytic proof above, and the published two-by-two amplification theorem [2], establish the universal claims; the finite diagnostics are not a proof for all matrices or amplifications.

## Relationship to prior work

Huang, Sukochev, and Tomskova [1] construct larger-corner Schur symbols with unequal ordinary and cb Schatten norms; their classification does not give this two-by-two phase formula. Arhancet [2] proves that such a discrepancy is impossible in dimension two, and explicitly analyzes a larger-dimensional counterexample; his published two-by-two equality theorem is used here, but does not specify the sharp dependence on the unimodular cross phase or the full family of norming matrices. Caspers and Wildschut [3] investigate ordinary and complete Schur norms more generally, including computational evidence, but do not identify this phase law. Other related exact calculations for zero-one Schur idempotents concern different (nonunimodular) symbols. An existing weak trace-class endpoint phase formula on two-by-two unimodular symbols has a different norm and does not imply this Schatten-four result.

## Limitations

Historical priority is not established by unsuccessful searches; an older equivalent norm calculation may exist. The formula is specific to unimodular complex two-by-two masks and unnormalized Schatten-four norms. The cb statement depends on an external proved theorem [2]. The equality classification concerns the ordinary scalar Schatten-four problem; no classification of matrix-amplified extremizers is asserted. The first-order phase expansion is one-sided in the nonnegative absolute phase \(\delta\), not a claim of signed differentiability at the factorable symbol.

## References

1. J. Huang, F. Sukochev, A. Tomskova, *A Schur Multiplier with Unequal Operator and Completely Bounded Norms on \(S_4\)*, arXiv:2608.20933 (first public version August 21, 2026), Sections 1, 3–4. https://arxiv.org/abs/2608.20933
2. C. Arhancet, *Optimal square size for separating the operator and completely bounded norms of Schur multipliers on \(S^4\)*, arXiv:2609.29643 (first public version September 3, 2026), especially Theorem 3.2 and Sections 1, 3–5. https://arxiv.org/abs/2609.29643
3. M. Caspers, G. Wildschut, *On the complete bounds of \(L^p\)-Schur multipliers*, arXiv:1902.07949 (2019), Sections 2 and 5. https://arxiv.org/abs/1902.07949

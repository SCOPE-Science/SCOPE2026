# Reflection root-mean-square majorization of every even Fourier moment

## Finding
Let \(G\) be an arbitrary discrete abelian group with compact dual \(\widehat G\) and normalized Haar probability measure. Let \(S\subset G\) be nonempty and finite, and suppose that for some \(t\in G\) the reflection \(Jx=t-x\) maps \(S\) to itself. For arbitrary \(c:S\to\mathbb C\), extend it by zero, set \(a_x=|c_x|\), and define the reflection root-mean-square symmetrization
\[
 b_x=\left(\frac{a_x^2+a_{Jx}^2}{2}\right)^{1/2}.
\]
For any real nonnegative finitely supported \(v\), let \(R_h(v)=\sum_{x\in G}v_xv_{x+h}\) denote its aperiodic autocorrelation (periodic when \(G\) is finite). Then simultaneously for **every** \(h\in G\),
\[
 R_h(b)\ge R_h(a),\qquad R_0(b)=R_0(a)=\|c\|_2^2.
\]
Furthermore, all these inequalities are equalities if and only if \(a_x=a_{Jx}\) for all \(x\in G\).

Define Fourier synthesis by \(\mathcal Tc(\chi)=\sum_{x\in S}c_x\chi(x)\). For every integer \(s\ge2\),
\[
\boxed{\ \|\mathcal Tc\|_{L^{2s}(\widehat G)}^{2s}\le\|\mathcal Tb\|_{L^{2s}(\widehat G)}^{2s},\qquad \|b\|_{\ell^2(G)}=\|c\|_{\ell^2(G)}.\ }
\]
If \(a\) is not invariant under \(J\), then the displayed even-moment inequality is strict for **all** integers \(s\ge2\). Therefore, whenever \(S=t-S\), **every** maximizer of the \(\ell^2(S)\)-to-\(L^{2s}(\widehat G)\) operator norm has \(|c_x|=|c_{t-x}|\). For example, on the consecutive spectrum \(S=\{0,\ldots,n-1\}\subset\mathbb Z\), all even-exponent norm maximizers have palindromic coefficient magnitudes, for every integer \(n\ge2\).

## Assumptions and scope
The theorem concerns complex coefficients with arbitrary phases; the symmetrized coefficients \(b\) are real nonnegative. No restriction is imposed on the size, exponent, or rank of the discrete abelian group. Only the coefficient support must be finite and stable under the chosen reflection. On finite groups, the output norm uses probability counting measure; on infinite discrete groups, it uses probability Haar measure on the compact dual. All sums below are finite. There is no claim about non-even exponents, a particular sharp numerical norm, uniqueness of maximizers, or a classification of their phases.

## Proof
**Step 1: exact autocorrelation increase.** Define nonnegative vectors \(u_x=(a_x,a_{Jx})\in\mathbb R^2\). Then \(b_x=\|u_x\|_2/\sqrt2\). By Cauchy--Schwarz,
\[
 b_xb_{x+h}\ge\frac12\big(a_xa_{x+h}+a_{Jx}a_{J(x+h)}\big).
\]
After summing over \(x\in G\), the first contribution is \(R_h(a)/2\). The change of variables \(y=Jx\), together with \(J(x+h)=Jx-h\), transforms the second contribution into \(R_{-h}(a)/2=R_h(a)/2\). Thus \(R_h(b)\ge R_h(a)\). The zero-shift identity follows from \(\sum_x b_x^2=\sum_x a_x^2\).

The critical step also has an explicit sum-of-squares identity: with the convention that a summand having zero denominator is zero,
\[
\begin{aligned}
R_h(b)-R_h(a)
 =\frac12\sum_{x\in G}
\frac{\big(a_xa_{J(x+h)}-a_{Jx}a_{x+h}\big)^2}
{\sqrt{(a_x^2+a_{Jx}^2)(a_{x+h}^2+a_{J(x+h)}^2)}
+a_xa_{x+h}+a_{Jx}a_{J(x+h)}}.
\end{aligned}
\]
The identity is the elementary two-dimensional Lagrange identity \(\|u\|\|v\|-\langle u,v\rangle=\det(u,v)^2/(\|u\|\|v\|+\langle u,v\rangle)\).

**Step 2: strictness.** On each two-point reflection orbit, the root-mean-square inequality gives \(2b_x\ge a_x+a_{Jx}\), strictly if its two magnitudes differ; on fixed points equality holds. Hence \(\sum_x b_x>\sum_x a_x\) whenever \(a\ne a\circ J\) and \(a\ne0\). On the other hand,
\[
 \sum_{h\in G}R_h(v)=\left(\sum_{x\in G}v_x\right)^2
\]
for any nonnegative finitely supported \(v\). The autocorrelation inequalities therefore cannot all be equalities unless \(a=a\circ J\). As \(R_0(b)=R_0(a)\), a nonsymmetric nonzero \(a\) has some nonzero shift \(h\) with \(R_h(b)>R_h(a)\).

**Step 3: simultaneous even moments.** For an integer \(s\ge2\), Fourier orthogonality gives the exact identities
\[
 \|\mathcal Tc\|_{2s}^{2s}=\sum_{y\in G}|c^{*s}(y)|^2,
 \qquad
 \|\mathcal Ta\|_{2s}^{2s}=\sum_{\substack{h_1+\cdots+h_s=0}}\prod_{j=1}^sR_{h_j}(a).
\]
Triangle inequalities on each convolution coefficient imply \(\|\mathcal Tc\|_{2s}^{2s}\le\|\mathcal Ta\|_{2s}^{2s}\). Since every \(R_h\) is nonnegative and \(R_h(b)\ge R_h(a)\), the second expression is nondecreasing when \(a\) is replaced by \(b\). If \(a\ne a\circ J\), Step 2 supplies \(h\ne0\) with strict increase. The moment expansion contains the strictly increasing nonnegative term associated with shifts \((h,-h,0,\ldots,0)\); its zero-shift factors equal \(R_0(a)^{s-2}>0\). Hence \(\|\mathcal Tb\|_{2s}>\|\mathcal Ta\|_{2s}\ge\|\mathcal Tc\|_{2s}\). This establishes all strict assertions.

**Step 4: extremizers.** Because \(S\) is finite, the unit sphere in \(\ell^2(S)\) is compact and every even-exponent synthesis norm attains its maximum. The operation \(c\mapsto b\) stays within \(S\), preserves \(\ell^2\), and strictly increases each even output norm if the original magnitudes are asymmetric. Therefore no norm maximizer can have asymmetric magnitudes.

## Verification
A dependency-free Python checker `artifacts/verify.py` independently constructs reflected coefficient pairs whose symmetrizations have integer entries, checks the correlation inequalities and strictness, and computes exact convolution moments for integers and Gaussian integers. Across 624 deterministic cyclic-group/reflection examples with sizes 2 through 14, the tests cover moments of orders 4, 6, and 8 and coefficient phases. Aperiodic examples are also checked. These finite tests corroborate the algebra; they are not used as proof of the quantification over all discrete abelian groups or all moments.

## Relationship to prior work
The Hardy--Littlewood even-integer majorant principle, discussed explicitly in Green--Ruzsa (2003) and Krenedits (2010), permits replacement of complex Fourier coefficients by their magnitudes. That established principle alone does **not** assert autocorrelation-by-autocorrelation improvement from reflection root-mean-square balancing. Katz--Rahman--Ward (2023/2025) analyze generalized palindromes and autocorrelation equality, a different equality-preserving question rather than this strict coefficientwise optimization. A four-frequency symmetry statement supplies a short-support special case, but that four-coordinate assertion cannot by itself imply the theorem for arbitrary finite supports in arbitrary discrete abelian groups.

## Limitations
The proof is an elementary Cauchy--Schwarz argument; novelty therefore remains vulnerable to an equivalent statement under older symmetrization or rearrangement terminology. The literature review is not an exhaustive priority certification. The theorem determines necessary modulus symmetry and a simultaneous extremal reduction but does not calculate the sharp norm for an arbitrary spectrum or force all maximizing phases to be affine. An abstract-only historical source on nonnegative trigonometric polynomial extrema (Goldstein--McDonald, 1984) was not used to assert noncoverage. No claim is made for exponents outside the positive even integers; in particular, classical majorant failures warn against that extension.

## References
- B. Green and I. Z. Ruzsa, *On the Hardy--Littlewood majorant problem*, first public arXiv version 19 March 2003, https://arxiv.org/abs/math/0303244 ; full text https://arxiv.org/html/math/0303244v1 .
- S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, first public arXiv version 2 June 2010, https://arxiv.org/abs/1006.0409 ; full text https://arxiv.org/html/1006.0409v3 .
- D. J. Katz, A. Rahman and M. J. Ward, *Sequences with identical autocorrelation functions*, first public arXiv version 14 August 2023, https://arxiv.org/abs/2308.07467 ; full text https://arxiv.org/html/2308.07467v3 .
- M. Goldstein and J. N. McDonald, *An Extremal Problem for Non-Negative Trigonometric Polynomials*, J. London Math. Soc. (1984), https://doi.org/10.1112/jlms/s2-29.1.81 (bibliographic and title comparison only).

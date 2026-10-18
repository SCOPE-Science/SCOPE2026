# Singular-value profiles for generalized Hilbert operators with lacunary symbols

## Finding
Fix an integer sequence \(1\le n_1<n_2<\cdots\) and a number \(q>1\) such that \(n_{j+1}\ge qn_j\) for every \(j\ge1\). For any analytic lacunary symbol \(g(z)=\sum_{j\ge1}b_jz^{n_j}\) let
\[
(\mathcal H_g f)(z)=\int_0^1 f(t)g'(tz)\,dt
\]
initially for polynomials \(f\) in the Hardy space \(H^2\). Define \(d_j=\sqrt{n_j}b_j\) and let \(D:\ell^2\to\ell^2\) be diagonal with entries \(d_j\). For every bounded operator \(T\), use the approximation number convention
\[
a_k(T)=\inf\{\|T-F\|:\operatorname{rank}F<k\},\qquad k=1,2,\ldots.
\]

**Theorem.** The operator \(\mathcal H_g\) extends boundedly to \(H^2\) if and only if \(\sup_j |d_j|<\infty\). For every such symbol, there are constants \(0<c_{\boldsymbol n}\le C_{\boldsymbol n}<\infty\) depending solely on the fixed exponent sequence, not on \(b_j\), such that
\[
c_{\boldsymbol n}a_k(D)\le a_k(\mathcal H_g)\le C_{\boldsymbol n}a_k(D),\qquad k\ge1.
\]
The operator is compact if and only if \(d_j\to0\). For compact operators the approximation numbers are their singular values; hence the latter are uniformly comparable with the nonincreasing rearrangement \(d_k^*\) of \((|d_j|)\). In particular, for every \(0<p<1\),
\[
\mathcal H_g\in\mathcal S_p\quad\Longleftrightarrow\quad
\sum_{j\ge1}n_j^{p/2}|b_j|^p<\infty.
\]
The same membership equivalence also holds for \(p\ge1\), a range covered qualitatively by prior general theory; the genuinely finer assertion here is the **per-index** comparison that holds with constants independent of \(k\), \(p\), and the coefficients.

For any nonincreasing null sequence \((w_j)\) of nonnegative numbers, taking \(b_j=w_j/\sqrt{n_j}\) realizes a compact generalized Hilbert operator with singular values comparable to \(w_k\), with comparison constants fixed by \((n_j)\). For example, \(w_j=(j+1)^{-r}\), \(r>0\), produces \(a_k(\mathcal H_g)\asymp k^{-r}\), and \(\mathcal H_g\in\mathcal S_p\) precisely for \(rp>1\).

## Assumptions and scope
The ambient Hardy norm is \(\|f\|_{H^2}^2=\sum_{k\ge0}|\widehat f(k)|^2\). Exponents are distinct positive integers with one fixed multiplicative lacunarity gap \(q>1\). Coefficients may be complex; no monotonicity, positivity, or decay is required for the bounded-operator assertion. The symbol \(g\) is analytic because \(n_j\) grows geometrically and boundedness requires at most \(|b_j|\lesssim n_j^{-1/2}\). For general analytic choices outside that bound, the integral is defined on polynomials but need not produce a bounded operator on \(H^2\). The theorem does not assert an exact universal numerical constant or a spectral statement for noncompact operators.

## Proof
**1. Matrix factorization.** With \(e_k(z)=z^k\), direct integration gives
\[
\mathcal H_g e_k(z)=\sum_{j\ge1}\frac{n_jb_j}{n_j+k}z^{n_j-1}.
\]
Let \(v_j\in\ell^2(\mathbb N_0)\) have real coordinates \(v_j(k)=\sqrt{n_j}/(n_j+k)\), and define the synthesis map \(V(c)=\sum_jc_jv_j\), initially on finite sequences. Once boundedness of \(V\) has been established, let \(U=V^*\). The map from the input coefficients \((\widehat f(k))\) to the output coordinates indexed by \((n_j-1)\) is \(DU\). Because the output monomials are orthogonal, the nonzero approximation numbers of \(\mathcal H_g\) agree with those of \(DU\).

**2. Continuous Riesz estimate.** For \(x\ge0\), set \(f_j(x)=\sqrt{n_j}/(n_j+x)\). The unitary change of variables \(x=e^t\), \(F(x)\mapsto e^{t/2}F(e^t)\), maps \(f_j\) to a translate of
\[
h(t)=\frac1{2\cosh(t/2)},\qquad a_j=\log n_j,
\]
with translation parameter \(a_j\). Since \(a_{j+1}-a_j\ge\delta:=\log q>0\), these are separated translates. The Fourier transform \(\widehat h(\xi)=\pi/\cosh(\pi\xi)\), obtained from the beta integral \(\int_0^\infty u^{-1/2-i\xi}/(1+u)\,du\), is strictly positive on the real line. The inner product between two translates is
\[
K(a_i-a_j),\qquad K(s)=\frac{|s|}{2\sinh(|s|/2)},\quad K(0)=1.
\]
As \(K(s)\) decays exponentially for large \(|s|\), the Schur bound
\[
\left\|\sum_jc_jf_j\right\|_{L^2(0,\infty)}^2
\le\left(1+2\sum_{m\ge1}K(m\delta)\right)\sum_j|c_j|^2
\]
holds for all finitely supported coefficients.

For a quantitative lower estimate, put \(R=2\pi/\delta\) and \(w_R(\xi)=R^{-1}(1-|\xi|/R)_+\). This density has integral one and Fourier transform \((\sin(Rs/2)/(Rs/2))^2\). Since distinct \(a_j\) are separated by at least \(\delta\), the off-diagonal absolute row sum of its Fourier Gram matrix is at most
\[
\frac8{R^2\delta^2}\sum_{m\ge1}\frac1{m^2}=\frac13.
\]
Consequently,
\[
\int_{-R}^R\left|\sum_jc_je^{-ia_j\xi}\right|^2d\xi
\ge\frac{2R}{3}\sum_j|c_j|^2.
\]
Plancherel and \(\min_{|\xi|\le R}|\widehat h(\xi)|^2=\pi^2\operatorname{sech}^2(\pi R)\) now yield
\[
\left\|\sum_jc_jf_j\right\|_{L^2(0,\infty)}^2
\ge m_\delta\sum_j|c_j|^2,\qquad
m_\delta=\frac{\pi R}{3}\operatorname{sech}^2(\pi R)>0.
\]
The displayed estimates first hold for finite sequences and extend to all \(\ell^2\) by continuity.

**3. Integer sampling.** For a finite linear combination \(F(x)=\sum_jc_jf_j(x)\), its left-endpoint step interpolation satisfies
\[
\|F(\lfloor\cdot\rfloor)-F\|_{L^2(0,\infty)}\le\|F'\|_{L^2(0,\infty)}.
\]
This follows by the fundamental theorem of calculus and Cauchy–Schwarz separately on every interval of length one. Direct integration shows
\[
\|f'_j\|_{L^2(0,\infty)}^2=\frac1{3n_j^2}.
\]
The derivative synthesis map therefore has a Hilbert–Schmidt bound \(\bigl(\sum_j(3n_j^2)^{-1}\bigr)^{1/2}<\infty\). On its tail indexed by \(j\ge J\), the bound tends to zero. Combining the preceding continuous Riesz lower estimate with sampling gives, for sufficiently large \(J\),
\[
\left\|\sum_{j\ge J}c_jv_j\right\|_{\ell^2(\mathbb N_0)}
\ge\frac{\sqrt{m_\delta}}2\left(\sum_{j\ge J}|c_j|^2\right)^{1/2}.
\]
The continuous upper estimate and the global finite derivative bound similarly imply that \(V\) is bounded on all of \(\ell^2\).

**4. No exceptional finite head.** We prove that \(V\) is injective, thus upgrading its tail lower bound to a global one. Suppose \(Vc=0\) with \(c\in\ell^2\). Since geometric gaps imply \(\sum_jn_j^{-1}<\infty\), the series
\[
F(t)=\sum_{j\ge1}c_j\sqrt{n_j}\,t^{n_j-1}
\]
converges in \(L^1(0,1)\), and is analytic for \(|t|<1\). For every integer \(k\ge0\),
\[
\int_0^1t^k F(t)\,dt=\sum_j\frac{c_j\sqrt{n_j}}{n_j+k}=(Vc)_k=0.
\]
Density of polynomials in \(C[0,1]\) implies \(F=0\) almost everywhere; analyticity and distinct powers imply \(c_j=0\) for all \(j\). Now suppose \(V\) were not bounded below. Unit vectors \(c^{(r)}\) with \(Vc^{(r)}\to0\) have a subsequence whose finitely many head coordinates converge. By the tail lower estimate, the tail coordinates of that subsequence are Cauchy; hence \(c^{(r)}\) converges in \(\ell^2\) to a unit vector \(c\) with \(Vc=0\), contradiction. Thus constants \(m,M>0\) exist with
\[
m\|c\|_2^2\le\|Vc\|_2^2\le M\|c\|_2^2\quad(c\in\ell^2).
\]

**5. Approximation-number comparison and endpoints.** Because \(V\) is bounded below, \(U=V^*\) is surjective and has a bounded right inverse \(R_0=V(V^*V)^{-1}\), so \(UR_0=I_{\ell^2}\). The coefficient map is \(DU\); its boundedness implies \(\sup_j|d_j|<\infty\), for example using \(D=(DU)R_0\). Conversely bounded \(D\) gives bounded \(DU\). Approximation-number ideal inequalities applied to \(D=(DU)R_0\) and \(DU=D U\) give
\[
\frac{a_k(D)}{\|R_0\|}\le a_k(DU)\le\|U\|a_k(D)
\quad\text{for every }k\ge1.
\]
An infinite diagonal operator is compact exactly when its diagonal tends to zero, and its compact singular values are the decreasing rearrangement of the diagonal moduli. This proves the principal statement. For any \(p>0\), convergence of \(\sum_k a_k(\mathcal H_g)^p\) is consequently equivalent to \(\sum_j|d_j|^p<\infty\). All implications follow for the quasi-norm range \(0<p<1\) as well as for ordinary Schatten exponents.

## Verification
A standalone exact-rational script, `checks/lacunary_hilbert_checks.py`, verifies the coefficient factorization in a four-degree lacunary example and confirms strict positivity of leading principal minors of a truncated Cauchy-kernel Gram matrix. The exact-rational tests do not establish the infinite Riesz bound, Fourier lower estimate, or operator-ideal equivalence; those conclusions follow from the full analytical proof above.

To reproduce the finite checks, run `python3 checks/lacunary_hilbert_checks.py` using Python's standard library. The output marker is `LACUNARY_HILBERT_SINGULAR_PROFILE_FINITE_IDENTITIES_OK`.

## Relationship to prior work
Norrbo, Peláez and Wu [1], first publicly available August 19, 2026, study boundedness and compactness of \(\mathcal H_g\) on Hardy spaces and obtain the corresponding lacunary-symbol criteria. Peláez and Seco [2] already characterize Schatten membership for \(p\ge1\) on appropriate Dirichlet-type Hilbert spaces, including the Hardy case, and also characterize compactness. Thus neither the \(p\ge1\) membership assertion nor qualitative compactness is asserted here as a wholly new result. The added mathematical assertion is the uniform pointwise comparison of **all** approximation numbers with a rearranged weighted symbol sequence; this supplies in particular the uncovered \(0<p<1\) quasi-Schatten range and prescribed singular-decay realizations. Guo and Tang [3] analyze Hardy-space boundedness through multiplier spaces rather than singular-value sequences.

## Limitations
The constants may deteriorate greatly as \(q\downarrow1\), and also depend on the finite initial degree pattern; no uniform positive lower constant depending on \(q\) alone is claimed. Lacunarity is essential to the argument; the statement does not apply to general analytic symbols or arbitrary Hardy exponents. The inaccessible full text of [1] leaves residual overlap risk, although its accessible abstract and descriptions concern boundedness and compactness rather than pointwise singular values. No independent audit has been performed.

## References
[1] David Norrbo, José Ángel Peláez and Fanglei Wu, *The Boundedness Problem for Generalized Hilbert Operators on Hardy Spaces*, arXiv:2608.19086 (first posted August 19, 2026).

[2] José Ángel Peláez and Daniel Seco, *Schatten classes of generalized Hilbert operators*, arXiv:1510.05455 (2015), especially Theorem 1 and Proposition 10.

[3] Yuting Guo and Pengcheng Tang, *Generalized Hilbert operators on Hardy spaces*, arXiv:2607.28221 (2026).

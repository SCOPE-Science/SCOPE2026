# Sharp single-field sign-reversal bound and reentrant pair correlations in binary Gibbs systems

## Finding
Consider a strictly positive finite-spin Gibbs law with at least three spins, arbitrary finite real interactions (including any higher-order interactions), and fixed local fields except one field \(h\) at a spin different from a selected pair. As \(h\) runs through the real line, the covariance of the selected spins either vanishes identically or changes sign at most twice. This bound is attained by a three-spin Gibbs law whose two conditional pair associations are both strictly positive. Hence an all-positive conditional association can pass through a negatively associated marginal interval and return to positive association, with the interaction couplings unchanged.

For the complete three-spin model
\[
 p_h(x,y,t)=Z_h^{-1}\exp\!\left(a xy+b xt+c yt+d xyt+h_1x+h_2y+ht\right),\quad (x,y,t)\in\{-1,1\}^3,
\]
where all parameters are real, let \(z=e^{2h}\), and define
\[
 \begin{aligned}
 A&=e^{4a+2d}-e^{-2d},\\
 B&=2\left[e^{4a}\cosh\bigl(2(b+c)\bigr)-\cosh\bigl(2(b-c)\bigr)\right],\\
 C&=e^{4a-2d}-e^{2d},\\
 Q(z)&=Az^2+Bz+C.
 \end{aligned}
\]
Then for every finite \(h,h_1,h_2\),
\[
 \operatorname{sgn}\operatorname{Cov}_h(x,y)=\operatorname{sgn}Q(e^{2h}).
\]
The sign is independent of \(h_1,h_2\), although the magnitude of the covariance generally is not. Every zero and every sign transition is thus located by an explicit polynomial of degree at most two.

In particular: (i) if \(|a|<|d|\), there is exactly one simple covariance sign reversal at a finite \(h\), regardless of \(b,c,h_1,h_2\); (ii) if \(a>|d|\), there are exactly two simple reversals precisely when \(B<-2\sqrt{AC}\); (iii) if \(a<-|d|\), there are exactly two simple reversals precisely when \(B>2\sqrt{AC}\). In (ii) and (iii), equality gives one tangential zero with no sign reversal, and the complementary strict inequality gives no zero. All boundary cases \(|a|=|d|\) are decided without exception by the positive roots of \(Q\). The pair covariance is identically zero at every field exactly when \(a=d=0\) and \(bc=0\).

A fully exact two-reversal example is
\[
 a=\frac{\log2}{4},\qquad b=\log2,\qquad c=-\log2,\qquad d=0.
\]
Here the two conditional pair odds ratios (given \(t=\pm1\)) both equal \(e^{4a}=2>1\), yet
\[
 Q(z)=z^2-\frac{193}{16}z+1
\]
has the two distinct positive roots
\[
 z_\pm=\frac{193\pm15\sqrt{161}}{32},\qquad z_-z_+=1.
\]
With \(H=\frac12\log z_+>0\), the marginal covariance is positive for \(|h|>H\), negative for \(|h|<H\), and zero at \(h=\pm H\), independently of both spectator local fields \(h_1,h_2\). This proves sharpness for every number of spins by adjoining independent spectator spins.

## Assumptions and scope
All configuration weights are strictly positive; there are finitely many binary spins \(s_j\in\{-1,+1\}\); the inverse-temperature factor is absorbed into the dimensionless interaction coefficients. For the general bound, take \(N\ge3\), distinct indices \(i,j,k\), an arbitrary real function \(R\) on \(\{-1,1\}^N\), fixed fields \(h_\ell\in\mathbb R\) at \(\ell\ne k\), and vary only the field \(h\) at \(k\):
\[
 p_h(s)=\frac{\exp\!\left(R(s)+\sum_{\ell\ne k}h_\ell s_\ell+h s_k\right)}{Z_h},\qquad h\in\mathbb R.
\]
The claim concerns the sign of \(\operatorname{Cov}_h(s_i,s_j)\), not correlation magnitudes, conditional independence of all spins, phase transitions in the thermodynamic limit, or variation of several fields simultaneously. A sign reversal means a genuine change between positive and negative values; a tangency is not counted as a reversal.

## Proof
**Step 1: An exact quadratic for any number of spins.** For \(x,y,t\in\{-1,+1\}\), let \(W_t(x,y)>0\) denote the sum of the fixed positive Boltzmann factors over all spins other than \(i,j,k\), with \(s_i=x,s_j=y,s_k=t\), and with the variable factor \(e^{h s_k}\) omitted. Set \(z=e^{2h}>0\). The unnormalized two-spin marginal entries, after removing the common positive factor \(e^{-h}\), are exactly
\[
 M_{xy}(z)=W_{-1}(x,y)+zW_{+1}(x,y).
\]
Their total \(T(z)=\sum_{x,y}M_{xy}(z)>0\). An elementary expansion of a \(2\times2\) binary table gives
\[
 \operatorname{Cov}_h(s_i,s_j)=\frac{4\bigl(M_{++}M_{--}-M_{+-}M_{-+}\bigr)}{T(z)^2}.
\]
Each \(M_{xy}\) is affine in \(z\), so its determinant is a polynomial in \(z\) of degree at most two. Unless this polynomial is identically zero it has at most two distinct positive roots, hence at most two sign changes along \(z=e^{2h}\). No restrictions on the number or order of interactions are used.

**Step 2: Exact three-spin factorization.** For the given three-spin Gibbs law, summing over \(t\) yields
\[
 M_{xy}(h)=2e^{a xy+h_1x+h_2y}\cosh(h+bx+cy+dxy).
\]
In the determinant of the four \(M\)'s, factors involving \(h_1,h_2\) cancel. After removing positive common factors, the sign is that of
\[
 F(h)=e^{4a}\left[\cosh\bigl(2(h+d)\bigr)+\cosh\bigl(2(b+c)\bigr)\right]
 -\left[\cosh\bigl(2(h-d)\bigr)+\cosh\bigl(2(b-c)\bigr)\right].
\]
This uses \(2\cosh u\cosh v=\cosh(u+v)+\cosh(u-v)\). Multiplication by \(2e^{2h}>0\) gives precisely \(Q(e^{2h})\). Thus the claimed sign formula and independence from \(h_1,h_2\) are exact.

**Step 3: Complete root classification.** The signs of \(A\) and \(C\) are respectively the signs of \(a+d\) and \(a-d\). If \(|a|<|d|\), \(AC<0\), so the two real roots of \(Q\) have opposite signs. The positive root is simple. If \(a>|d|\), then \(A,C>0\), so two positive roots occur exactly when the vertex lies at positive \(z\) and below zero, equivalently \(B<-2\sqrt{AC}\); equality yields a positive double root. Multiplying the polynomial by \(-1\) proves the stated classification for \(a<-|d|\). For \(|a|=|d|\), the same formula \(Q\) (of degree at most one after any vanished endpoint coefficient) gives every finite-field solution exactly. Finally \(Q\equiv0\) implies \(A=C=0\), hence \(a=d=0\), and then \(B=4\sinh(2b)\sinh(2c)=0\), which is equivalent to \(bc=0\). The converse is immediate.

**Step 4: Constructive sharpness.** For the displayed logarithmic couplings, \(e^{4a}=2\), \(\cosh(2(b+c))=1\), and \(\cosh(2(b-c))=257/32\), giving \(A=C=1\), \(B=-193/16\). Its discriminant is \(225\cdot161/256>0\), and its positive roots are the displayed reciprocals. Positivity of \(Q\) outside the root interval and negativity inside proves both sign changes. Conditioning on \(t=\pm1\) leaves the pair interaction \(a\pm d=a>0\), so each conditional odds ratio is \(2\). Independent additional spins multiply every two-spin table entry by the same positive factor and preserve all sign changes for arbitrary \(N\ge3\).

## Verification
A standalone standard-library Python program, `verify_reversal.py`, reconstructs Gibbs tables by direct enumeration, tests the determinant polynomial against directly computed covariances, and checks the exact reentrant witness and limiting-field opposite-sign example. Fresh execution returned `PASS 4188 finite arithmetic assertions`. This finite verification is supplementary: the uniform bound and phase classification are established by the preceding algebraic proof, not by enumeration.

## Relationship to prior work
Yi-Yu Lin (2026) proves a discrete Sklar-type bijection identifying the fixed higher-order Walsh log-linear coefficients as the Gibbs dependence nucleus and the external fields as one-body parameters. That establishes the natural setting but does not supply the present sharp sign-reversal count or three-spin field-coupling threshold classification. Older work of Bergsma and Rudas (2002) analyzes conditional versus marginal log-linear association and variation independence; Teuscher (2022) quantifies Simpson's paradox in three-way tables; Hammond, van der Heijden and Smith (2024) develop fixed-marginal log-linear table generation. These works provide the established marginal/conditional association context and are not claimed as new here. The present exact field-path polynomial, sharp uniform two-reversal bound, three-spin root atlas, and constructive reentrant example are the specific evaluated contribution. The determinant-of-an-affine-mixture observation is elementary and may be implicitly available in older contingency-table geometry; no claim of independent literature-wide priority is made.

## Limitations
The polynomial bound requires variation of one binary spin's linear field only, with all other couplings and fields fixed. It does not apply unchanged when several local fields vary along arbitrary paths, to continuous spins, or to quantum noncommuting observables. The three-spin parameter atlas is finite-dimensional; it asserts no thermodynamic phase transition. The novelty judgment is best-knowledge and remains exposed to older mixture-geometry or log-linear literature stating equivalent implications; independent validation has not been performed.

## References
1. Y.-Y. Lin, *A Sklar-Type Decomposition for Positive Binary Distributions and a Gibbs Interpretation*, arXiv:2610.12805v1, first submitted October 8, 2026. https://arxiv.org/html/2610.12805v1
2. W. P. Bergsma and T. Rudas, *Modeling conditional and marginal association in contingency tables*, Annales de la Faculté des Sciences de Toulouse **11** (2002), 455–468. https://www.numdam.org/article/AFST_2002_6_11_4_455_0.pdf
3. F. Teuscher, *The quantification of Simpson's paradox and other contributions to contingency table theory*, PLOS ONE **17** (2022), e0262502. https://doi.org/10.1371/journal.pone.0262502
4. C. Hammond, P. G. M. van der Heijden and P. A. Smith, *Generating contingency tables with fixed marginal probabilities and dependence structures described by loglinear models*, arXiv:2303.08568, publicly available 2023. https://arxiv.org/html/2303.08568v2

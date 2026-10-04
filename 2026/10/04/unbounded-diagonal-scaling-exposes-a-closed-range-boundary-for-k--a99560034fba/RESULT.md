# Unbounded diagonal scaling exposes a closed-range boundary for K-frame characterizations
## Finding
Let \(H=\ell^2(\mathbb N)\) with canonical orthonormal basis \(\{e_n\}_{n\ge1}\), and let \(K\) be the orthogonal projection onto \(\operatorname{{span}}\{{e_1\}}\). Define
\[
f_1=e_1,\qquad f_n=\frac1n e_n\quad(n\ge2),
\]
and let the nonnegative scaling sequence be
\[
a_1=1,\qquad a_n=n\quad(n\ge2).
\]
Then \(F=(f_n)\) is a \(K\)-frame and the scaled sequence \(G=(a_nf_n)=(e_n)\) is a \(K\)-frame, while the maximal diagonal multiplier \(D_a\) is unbounded on the analysis range \(R(T_F)\). Consequently, Theorems 3.8 and 3.9 of Ramesan--Ravindran, *Some Results on Scalable K-Frames*, are false as stated. The failure persists although \(K\) has closed range.

The exact replacement for arbitrary \(K\)-frames is the following. For a \(K\)-frame \(F=(f_n)\) and nonnegative scalars \(a_n\), the scaled family \(G=(a_nf_n)\) is a \(K\)-frame if and only if
\[
R(T_F)\subset D(D_a),\qquad A:=D_aT_F\in B(H,\ell^2),\qquad R(K)\subset R(A^*).
\]
Moreover, if \(R(T_F)\) is closed, then the bounded-on-range conclusion used in the published theorem is valid: \(D_a|_{{R(T_F)}}\) is bounded in the ambient \(\ell^2\)-norm.

## Assumptions and scope
The diagonal operator \(D_a\) is taken with its maximal domain
\[
D(D_a)=\{y=(y_n)\in\ell^2:(a_ny_n)\in\ell^2\}.
\]
No injectivity or surjectivity of \(K\) is assumed in the repaired characterization. The counterexample uses the especially strong case in which \(K\) is an orthogonal projection and hence has closed range. The claim concerns the analysis-range boundedness asserted in Theorems 3.8 and 3.9; it does not challenge the later result in the same paper that adds a uniform lower bound on the atom norms.

## Proof
For \(x=(x_n)\in H\),
\[
\sum_{{n\ge1}}|\langle x,f_n\rangle|^2
=|x_1|^2+\sum_{{n\ge2}}\frac{|x_n|^2}{n^2}.
\]
Since \(K^*=K\) and \(\|K^*x\|^2=|x_1|^2\),
\[
\|K^*x\|^2
\le
\sum_{{n\ge1}}|\langle x,f_n\rangle|^2
\le
\|x\|^2.
\]
Thus \(F\) is a \(K\)-frame. The scaled family is exactly the canonical orthonormal basis, because \(a_nf_n=e_n\) for every \(n\), so \(G\) is a Parseval frame and therefore a \(K\)-frame.

The analysis operator is
\[
T_Fx=(x_1,x_2/2,x_3/3,\ldots).
\]
Its range equals the maximal domain of \(D_a\), and
\[
D_aT_Fx=x.
\]
For \(m\ge2\), put \(y^{(m)}=T_Fe_m=m^{-1}e_m\). Then
\[
\|y^{(m)}\|=\frac1m,\qquad
\|D_ay^{(m)}\|=1.
\]
Hence \(D_a|_{{R(T_F)}}\) is unbounded. This directly contradicts the asserted implication that a scaled \(K\)-frame forces that restriction to be bounded.

For the repaired characterization, suppose first that \(G\) is a \(K\)-frame. Its analysis operator is \(T_G=D_aT_F\), so \(R(T_F)\subset D(D_a)\) and \(A=D_aT_F\) is bounded. The lower \(K\)-frame inequality is
\[
c\|K^*x\|^2\le\|Ax\|^2
\]
for some \(c>0\). By the Douglas range theorem this is equivalent to \(R(K)\subset R(A^*)\).

Conversely, if the three displayed conditions hold, boundedness of \(A\) gives the Bessel upper estimate, while \(R(K)\subset R(A^*)\) gives \(KK^*\le C A^*A\) for some \(C>0\), hence a positive lower \(K\)-frame bound. Thus \(G\) is a \(K\)-frame.

Finally assume \(R(T_F)\) is closed and \(G\) is a \(K\)-frame. The restriction of \(T_F\) to \(\ker(T_F)^\perp\) has a bounded inverse \(T_F^\dagger:R(T_F)\to\ker(T_F)^\perp\). For \(y\in R(T_F)\),
\[
D_ay=T_GT_F^\dagger y,
\]
so
\[
\|D_ay\|\le\|T_G\|\,\|T_F^\dagger\|\,\|y\|.
\]
Thus closed analysis range is a sufficient hypothesis for the bounded-on-range step used in the published argument.

## Verification
The counterexample is symbolic. The lower and upper \(K\)-frame estimates are explicit coordinate identities, the scaled family is exactly an orthonormal basis, and unboundedness is witnessed by the normalized coordinate sequence \(y^{(m)}\). The repaired equivalence uses only the bounded analysis operator criterion and the Douglas range theorem. The closed-range repair is the standard bounded-inverse property of \(T_F\) on \(\ker(T_F)^\perp\).

The example was also checked against the stronger possible escape condition that \(K\) have closed range: here \(K\) is rank one and orthogonal, so that condition is already satisfied.

## Relationship to prior work
Ramesan--Ravindran state in Theorem 3.8 that if \(G=(a_nf_n)\) is a \(K\)-frame then \(D_a|_{{R(T_F)}}\) is bounded, and Theorem 3.9 uses that assertion in a characterization. Their proof estimates through an inverse of \(T_F\), although a general \(K\)-frame analysis operator need not be bounded below on \(\ker(T_F)^\perp\). The same bounded-on-analysis-range assertion appeared earlier as Theorems 4.1--4.2 of *Scalability and K-Frames*.

Ahmadi--Rahimi's earlier g-frame theorem does not imply the disputed \(K\)-frame step: for a genuine g-frame the analysis operator is bounded below and has closed range, precisely the property missing in the counterexample. A 2024 paper on scalable \(K\)-g-frames repeats an analogous boundedness step in its Theorem 23, so the distinction between bounded composition \(D_aT_F\) and bounded restriction \(D_a|_{{R(T_F)}}\) remains relevant beyond the scalar setting.

## Limitations
The result does not classify all circumstances under which \(D_a|_{{R(T_F)}}\) happens to be bounded; it gives an exact general operator characterization of the scaled \(K\)-frame property and a clean sufficient repair for the published range-boundedness claim. The counterexample does not apply to hypotheses that directly force the analysis range to be closed or that uniformly bound the scaling sequence.

A literature search cannot exclude every unindexed erratum, thesis remark, or informal observation. No checked source contained this counterexample, the closed-range boundary, or the exact composition-based replacement as a correction of the cited theorem.

## References
1. S. Ramesan and K. T. Ravindran, *Some Results on Scalable K-Frames*, Matematicki Vesnik 75 (2023), 225--234. DOI: 10.57016/MV-7942HXLN.
2. S. Ramesan and K. T. Ravindran, *Scalability and K-Frames*, Palestine Journal of Mathematics 12(1) (2023), 493--500.
3. A. Ahmadi and A. Rahimi, *Scalability of G-Frames by Diagonal Operators*, Proceedings of the Institute of Mathematics and Mechanics 47(2) (2021), 215--225.
4. V. Kumar, *Scalability of Generalized Frames for Operators*, Journal of Function Spaces (2024), Article 8358987. DOI: 10.1155/2024/8358987.
5. R. G. Douglas, *On Majorization, Factorization, and Range Inclusion of Operators on Hilbert Space*, Proceedings of the American Mathematical Society 17 (1966), 413--415.

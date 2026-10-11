# Homogeneity exposes the control obstruction in a \(K\)-frame perturbation theorem
## Finding
Nouri--Rahimi--Najafzadeh's Theorem 4.3 gives a perturbation criterion intended to produce a controlled \(K\)-Bessel sequence. Its hypothesis contains the nonhomogeneous term
\[
\alpha\|c\|\,\|T_Fc\|,
\]
where \(T_Fc=\sum_k c_kf_k\), while the theorem is quantified over every finitely supported coefficient vector \(c\). That term is mathematically redundant. For every such \(c\), the published perturbation inequality is equivalent to
\[
\|(T_F-T_G)c\|\le \beta\|T_Gc\|+\gamma\|c\|.
\]
Consequently, if \(F\) has an ordinary Bessel bound \(B_F\) and \(0\le\beta<1\), then \(G\) is an ordinary Bessel sequence with the sharp universal upper bound
\[
B_G\le \left(\frac{\sqrt{B_F}+\gamma}{1-\beta}\right)^2.
\]
The stronger controlled conclusion in the published theorem is false without an additional compatibility condition. For a positive invertible control \(C\), an ordinary Bessel family \(G\) is \(C\)-controlled Bessel exactly when
\[
CS_G=S_GC,
\]
where \(S_G\) is its ordinary frame operator. Under this condition one may take the controlled upper bound \(\|C\|B_G\).

## Assumptions and scope
Let \(H\) be a complex Hilbert space. Let \(F=(f_k)\) be an ordinary Bessel sequence with synthesis operator \(T_F\) and ordinary Bessel bound \(B_F\), so
\[
\|T_Fc\|\le \sqrt{B_F}\,\|c\|
\]
for finitely supported \(c\). Let \(G=(g_k)\) be an arbitrary sequence, with the algebraic synthesis map \(T_Gc=\sum_k c_kg_k\) initially defined on finitely supported vectors. Assume \(\alpha,\gamma\ge0\) and \(0\le\beta<1\), and assume
\[
\|(T_F-T_G)c\|\le \alpha\|c\|\,\|T_Fc\|+\beta\|T_Gc\|+\gamma\|c\|
\]
for every finitely supported \(c\).

The source theorem places this inequality inside the more specialized setting of a \(C\)-controlled \(K\)-frame and imposes an additional condition involving its lower controlled bound and a pseudoinverse of \(K\). Those extra hypotheses are not needed for the ordinary Bessel conclusion proved here. The symbol \(B_F\) denotes an ordinary Bessel bound of \(F\); it need not equal the source's controlled upper bound unless an additional identification is available.

## Proof
Fix a finitely supported \(c\) and apply the perturbation inequality to \(tc\) for \(t>0\). By linearity,
\[
t\|(T_F-T_G)c\|\le \alpha t^2\|c\|\,\|T_Fc\|+\beta t\|T_Gc\|+\gamma t\|c\|.
\]
After division by \(t\), letting \(t\downarrow0\) gives
\[
\|(T_F-T_G)c\|\le \beta\|T_Gc\|+\gamma\|c\|.
\]
The converse is immediate because the omitted \(\alpha\)-term is nonnegative. Thus the two perturbation conditions are equivalent for all finitely supported coefficients.

Now
\[
\begin{aligned}
\|T_Gc\|&\le \|T_Fc\|+\|(T_F-T_G)c\|\\
&\le \sqrt{B_F}\,\|c\|+\beta\|T_Gc\|+\gamma\|c\|.
\end{aligned}
\]
Hence
\[
(1-\beta)\|T_Gc\|\le (\sqrt{B_F}+\gamma)\|c\|.
\]
The algebraic synthesis map therefore extends uniquely to a bounded operator on \(\ell^2\), with
\[
\|T_G\|\le \frac{\sqrt{B_F}+\gamma}{1-\beta}.
\]
This is exactly the ordinary Bessel estimate
\[
B_G\le \left(\frac{\sqrt{B_F}+\gamma}{1-\beta}\right)^2.
\]

The constant is sharp. In \(H=\mathbb C\), take the one-atom Bessel family \(F=(\sqrt{B_F})\) and put
\[
L=\frac{\sqrt{B_F}+\gamma}{1-\beta},\qquad G=(L).
\]
Then
\[
|L-\sqrt{B_F}|=\beta L+\gamma,
\]
so the reduced perturbation inequality is an equality for every scalar coefficient. The optimal Bessel bound of \(G\) is \(L^2\). When \(0\le\gamma<\sqrt{B_F}\), this example also lies inside the source theorem's stated smallness regime with \(K=C=I\) and \(\alpha=0\).

It remains to identify the controlled obstruction. For an ordinary Bessel family \(G\), let \(S_G\) be its frame operator and let \(C\) be positive and invertible. The controlled quadratic form used in the source is represented by \(CS_G\). If it is a legitimate real quadratic form for every vector, then \(CS_G\) is self-adjoint by polarization. Since \(C\) and \(S_G\) are themselves self-adjoint,
\[
CS_G=(CS_G)^*=S_GC.
\]
Conversely, if \(CS_G=S_GC\), then \(CS_G\) is positive and
\[
0\le CS_G\le \|C\|\,B_G I
\]
in quadratic-form order. Thus commutation is exactly the missing condition for passing from the ordinary Bessel conclusion to the controlled Bessel conclusion.

For an explicit failure of the published theorem, let
\[
H=\mathbb C^2,\qquad K=I,\qquad C=\begin{pmatrix}1&0\\0&2\end{pmatrix},
\]
let \(F=(e_1,e_2)\), and for \(0<\varepsilon<1\) let
\[
G=(e_1+\varepsilon e_2,e_2).
\]
The family \(F\) is a \(C\)-controlled \(K\)-frame with controlled bounds \(1\) and \(2\). Moreover,
\[
\|(T_F-T_G)c\|=\varepsilon|c_1|\le \varepsilon\|c\|,
\]
so the source hypothesis holds with \(\alpha=\beta=0\) and \(\gamma=\varepsilon\); its additional smallness condition becomes \(\varepsilon<1\). But
\[
S_G=\begin{pmatrix}1&\varepsilon\\\varepsilon&1+\varepsilon^2\end{pmatrix},
\qquad
CS_G=\begin{pmatrix}1&\varepsilon\\2\varepsilon&2+2\varepsilon^2\end{pmatrix},
\]
which is not self-adjoint for \(\varepsilon\ne0\). Hence \(G\) is not a \(C\)-controlled \(K\)-Bessel sequence. For example, at \(f=(1,i)\) the controlled quadratic form has a nonzero imaginary part.

## Verification
Every step above is symbolic. The scaling argument uses the theorem's universal quantifier over finitely supported coefficients and no limiting interchange with an infinite series. The ordinary Bessel estimate is an operator-norm estimate on the dense subspace of finitely supported sequences and therefore gives a unique bounded synthesis extension.

The two-dimensional counterexample satisfies the source hypotheses exactly. With \(K=I\), the pseudoinverse is \(I\); with controlled lower bound \(1\), the source smallness expression reduces to \(\varepsilon<1\). The obstruction is not numerical: \(CS_G-(CS_G)^*\) has off-diagonal entries \(-\varepsilon\) and \(\varepsilon\), so it is nonzero for every \(0<\varepsilon<1\).

The sharpness example is also exact: the perturbation inequality becomes equality and the synthesis norm of the one-atom family is exactly \((\sqrt{B_F}+\gamma)/(1-\beta)\).

## Relationship to prior work
The target article's Theorem 4.3 states the nonhomogeneous coefficient inequality and then displays a purported Bessel bound still containing \(\|c\|\). Such a coefficient-dependent quantity is not a uniform Bessel bound. The neighboring Theorem 4.2, and the earlier Casazza--Christensen perturbation theorem quoted as Theorem 4.1, use homogeneous perturbation terms instead.

An earlier 2016 preprint by the same authors on compact perturbations contains a homogeneous \(K\)-frame perturbation theorem; it does not contain the nonhomogeneous Theorem 4.3 studied here. A separate 2016 preprint by the same authors contains only the controlled \(K\)-frame equivalence theory and likewise has no perturbation section of this form.

Mahmoudieh--Hosseinnezhad--Abbaspour Tabadkan later corrected a different controlled \(K\)-frame assertion by explicitly adding a frame-operator commutation condition. That prior correction supports the general commutation mechanism used here, but it does not address the 2018 Theorem 4.3 perturbation inequality, its redundant \(\alpha\)-term, the sharp ordinary Bessel constant, or the counterexample above.

## Limitations
The sharp quantitative statement concerns ordinary Besselness of \(G\), because the source perturbation inequality alone controls only the synthesis norm. It does not by itself produce a controlled quadratic-form inequality. The controlled conclusion requires the additional compatibility \(CS_G=S_GC\).

The ordinary bound is stated in terms of an ordinary Bessel bound \(B_F\) of \(F\), not automatically the controlled upper bound denoted by \(B\) in the source theorem. The finding does not assert a lower frame bound for \(G\), nor does it address perturbation criteria in which the extra coefficient factor is normalized or otherwise made homogeneous.

## References
1. M. Nouri, A. Rahimi, Sh. Najafzadeh, *Some Results on Controlled K-Frames in Hilbert Spaces*, International Journal of Analysis and Applications 16 (2018), 62--74, DOI 10.28924/2291-8639-16-2018-62.
2. A. Rahimi, Sh. Najafzadeh, M. Nouri, *Controlled K-frames and their invariance under Compact Perturbation*, arXiv:1602.03982v1 (2016).
3. A. Rahimi, Sh. Najafzadeh, M. Nouri, *Controlled K-frames in Hilbert Spaces*, arXiv:1602.03984v1 (2016).
4. M. Mahmoudieh, H. Hosseinnezhad, G. Abbaspour Tabadkan, *Some properties of controlled K-frames in Hilbert spaces*, Wavelets and Linear Algebra 7 (2020), 47--56, DOI 10.22072/wala.2020.119701.1266.
5. P. G. Casazza, O. Christensen, *Perturbation of operators and applications to frame theory*, Journal of Fourier Analysis and Applications 3 (1997), 543--557.

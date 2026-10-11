# Bounded below on \(R(K^*)\) is the exact missing hypothesis in a \(K\)-\(g\)-frame composition theorem
## Finding
Li, Leng, and Huang state that if \(\{\Lambda_i\}\) is a \(K\)-\(g\)-frame and a bounded operator \(T\) satisfies \(TK^*=K^*T\), then \(\{\Lambda_iT\}\) is again a \(K\)-\(g\)-frame. This is false without a lower-bound hypothesis on \(T\).

The exact universal repair is the following. Let \(H\) be a Hilbert space, let \(K,T\in\mathcal L(H)\), and assume \(TK^*=K^*T\). Then
\[
\text{every \(K\)-\(g\)-frame \(\{\Lambda_i\}\) remains a \(K\)-\(g\)-frame after right composition by \(T\)}
\]
if and only if there exists \(m>0\) such that
\[
\|Tx\|\ge m\|x\|\qquad\text{for every \(x\in R(K^*)\)}.
\]
If the original \(K\)-\(g\)-frame has bounds \(A,B\), then the repaired hypothesis gives bounds \(Am^2\) and \(B\|T\|^2\) for the composed family.

A two-dimensional counterexample to the published statement is obtained with \(H=\mathbb R^2\), \(K=I\), one coefficient space equal to \(H\), \(\Lambda_1=I\), and \(T=\operatorname{diag}(1,0)\). The family \(\{\Lambda_1\}\) is Parseval, and \(TK^*=K^*T\) holds. For \(e_2=(0,1)\), however,
\[
\|\Lambda_1Te_2\|^2=0<\|K^*e_2\|^2=1,
\]
so no positive lower \(K\)-\(g\)-frame bound exists.

## Assumptions and scope
A family \(\{\Lambda_i:H\to H_i\}\) is a \(K\)-\(g\)-frame when there are \(0<A\le B<\infty\) such that
\[
A\|K^*f\|^2\le\sum_i\|\Lambda_i f\|^2\le B\|f\|^2
\qquad\text{for every \(f\in H\)}.
\]
The equivalence proved here assumes the same commutation condition \(TK^*=K^*T\) as the published theorem. The necessity statement is universal over all \(K\)-\(g\)-frames for the fixed pair \((K,T)\); it is not claimed to characterize preservation of one specially chosen frame. No closed-range assumption on \(K\) is used.

## Proof
For sufficiency, suppose that \(T\) is bounded below on \(R(K^*)\) with constant \(m>0\), and let \(\{\Lambda_i\}\) have \(K\)-\(g\)-frame bounds \(A,B\). For every \(f\in H\), commutation and the lower-bound hypothesis give
\[
\begin{aligned}
\sum_i\|\Lambda_iTf\|^2
&\ge A\|K^*Tf\|^2\\
&=A\|TK^*f\|^2\\
&\ge Am^2\|K^*f\|^2.
\end{aligned}
\]
The upper estimate is
\[
\sum_i\|\Lambda_iTf\|^2\le B\|Tf\|^2\le B\|T\|^2\|f\|^2.
\]
Thus \(\{\Lambda_iT\}\) is a \(K\)-\(g\)-frame.

For necessity, assume that right composition by \(T\) preserves every \(K\)-\(g\)-frame. Consider the single coefficient operator
\[
\Lambda_1=K^*:H\to H.
\]
It is a \(K\)-\(g\)-frame because
\[
\|K^*f\|^2\le\|K^*f\|^2\le\|K\|^2\|f\|^2.
\]
By universal preservation there is \(c>0\) such that
\[
\|K^*Tf\|^2\ge c\|K^*f\|^2
\qquad\text{for every \(f\in H\)}.
\]
Using \(K^*T=TK^*\), this becomes
\[
\|TK^*f\|\ge\sqrt c\,\|K^*f\|.
\]
Every element of \(R(K^*)\) is \(K^*f\) for some \(f\), so \(T\) is bounded below on \(R(K^*)\), with \(m=\sqrt c\). This proves the equivalence.

The published proof instead passes from \(\|TK^*f\|\) to a lower estimate involving \(\|T\|\|K^*f\|\). Boundedness supplies the opposite inequality, \(\|Tx\|\le\|T\|\|x\|\), and therefore cannot establish the required lower bound.

## Verification
The source theorem and its proof were checked in the full article. The statement appears as Theorem 5, and the displayed proof uses the invalid lower estimate just described. The counterexample is exact: \(T\) is an orthogonal projection, the commutation condition is automatic for \(K=I\), and the lower frame inequality fails on \(e_2\).

The repaired theorem is symbolic. Sufficiency is the direct frame estimate above. Necessity uses the canonical test family \(\Lambda_1=K^*\), so it does not depend on numerical experimentation, finite enumeration, or a closed-range theorem.

## Relationship to prior work
The 2017 article is the direct target: its Theorem 5 asserts preservation under bounded commuting \(T\) alone. A later 2024 paper on scalable \(K\)-\(g\)-frames proves a related preservation result under the stronger assumption that the commuting operator is an isometry. An isometry is bounded below with \(m=1\), so that later theorem is compatible with the repaired condition but is only a special case and does not state the universal equivalence above.

The primary source also records the standard \(K\)-\(g\)-frame definition and surrounding operator-range characterizations. Those do not imply that an arbitrary bounded commuting operator is bounded below on \(R(K^*)\).

## Limitations
The claim does not classify the noncommuting case. It also does not say that bounded-below behavior on \(R(K^*)\) is necessary for a particular fixed \(K\)-\(g\)-frame to survive composition; the necessity is for preservation of every \(K\)-\(g\)-frame. The exact correction may have been observed in an unindexed erratum, thesis, or informal note that was not located in the checked literature.

## References
D. Li, J. Leng, and T. Huang, “Some properties of g-frames for Hilbert space operators,” *Operators and Matrices* 11 (2017), 1075–1085. DOI: 10.7153/oam-2017-11-74.

V. Kumar, S. Malhotra, and N. Khanna, “Scalability of Generalized Frames for Operators,” *Journal of Function Spaces* (2024), Article 8358987. DOI: 10.1155/2024/8358987.

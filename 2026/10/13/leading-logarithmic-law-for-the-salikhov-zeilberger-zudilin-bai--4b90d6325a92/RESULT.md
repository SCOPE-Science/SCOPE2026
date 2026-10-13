# Leading logarithmic law for the Salikhov–Zeilberger–Zudilin–Bai window on the symmetric slice
## Finding
Let \(J(Q)=\widehat J(1,3/2-1/Q)\) be the normalized prime-elimination window measure on the symmetric slice defined in arXiv:2609.37459v1, and put \(J_\infty=\widehat J(1,3/2)\). Then, as real \(Q\to\infty\),
\[
J(Q)-J_\infty=\frac{2}{3}\frac{\log Q}{Q}+O\!\left(\frac1Q\right).
\]
Equivalently,
\[
\lim_{Q\to\infty}\frac{Q\bigl(J(Q)-J_\infty\bigr)}{\log Q}=\frac23.
\]
This proves the leading logarithmic coefficient in the source paper's numerically observed law near the limiting endpoint of the symmetric slice.

## Assumptions and scope
The definition of \(J(Q)\) and its exact series decomposition are those of arXiv:2609.37459v1. Write
\[
F_m(L)=\frac1m-\frac1{m+L}.
\]
The source gives
\[
J(Q)=\sum_{m\ge1}F_m\bigl(\ell_Q(m)\bigr),
\]
where \(0\le \ell_Q(m)\le1\). On the limiting slice one has
\[
\ell_\infty(m)=\begin{cases}1/3,&m\text{ odd},\\0,&m\text{ even}.
\end{cases}
\]
For sufficiently small \(m/Q\), the exact minimum formulas in the source select the branch displayed in the proof below. No assertion is made here about the source paper's fitted constant term beyond the leading logarithmic coefficient, nor about global unimodality or the global optimality of Bai's point.

## Proof
Put
\[
a_Q=\left(\frac32-\frac1Q\right)^{-1}
\]
and, for \(Q\ge40\), let \(N=\lfloor Q/20\rfloor\). For \(1\le m\le N\), set \(t=m/Q\). Then \(0<t\le1/20\).

For odd \(m\), the source's two candidate branch lengths are
\[
\frac{1/2-t}{1+1/Q}
\quad\text{and}\quad
\frac{1/2+t}{3/2-1/Q}.
\]
The second is the smaller whenever
\[
t\le\frac1{10}-\frac{2}{5Q}.
\]
Since \(Q\ge40\) and \(t\le1/20\), this holds. Hence
\[
\ell_Q(m)=a_Q\left(\frac12+\frac mQ\right)
\qquad(m\le N,\ m\text{ odd}).
\]
Because \(1/3=a_Q(1/2-1/(3Q))\),
\[
\ell_Q(m)-\frac13=\frac{a_Q}{Q}\left(m+\frac13\right).
\]
Therefore the difference of the corresponding summands simplifies exactly:
\[
F_m\bigl(\ell_Q(m)\bigr)-F_m(1/3)
=\frac{a_Q}{Q\bigl(m+\ell_Q(m)\bigr)}.
\]

For even \(m\), the source's candidates on this range are
\[
\frac{1/2-t}{1+1/Q}
\quad\text{and}\quad
\frac{t}{3/2-1/Q}.
\]
The second is the smaller whenever
\[
t\le\frac3{10}-\frac1{5Q},
\]
which again holds for \(m\le N\). Thus
\[
\ell_Q(m)=\frac{a_Qm}{Q}
\qquad(m\le N,\ m\text{ even}),
\]
and, since \(\ell_\infty(m)=0\),
\[
F_m\bigl(\ell_Q(m)\bigr)-F_m(0)
=\frac{a_Q}{Q\bigl(m+\ell_Q(m)\bigr)}.
\]

Consequently both parities obey the same exact identity throughout the initial block:
\[
\sum_{m\le N}\left(F_m\bigl(\ell_Q(m)\bigr)-F_m\bigl(\ell_\infty(m)\bigr)\right)
=\frac{a_Q}{Q}\sum_{m\le N}\frac1{m+\ell_Q(m)}.
\]
Since \(0\le\ell_Q(m)\le1\),
\[
\sum_{m\le N}\frac1{m+\ell_Q(m)}
=H_N+O(1)=\log Q+O(1).
\]
Also \(a_Q=2/3+O(1/Q)\). Hence the initial block equals
\[
\frac{2}{3}\frac{\log Q}{Q}+O\!\left(\frac1Q\right).
\]

It remains to control the tail. For every \(m\ge1\) and \(0\le L\le1\),
\[
0\le F_m(L)=\frac{L}{m(m+L)}\le\frac1{m^2}.
\]
Therefore
\[
\left|\sum_{m>N}\left(F_m\bigl(\ell_Q(m)\bigr)-F_m\bigl(\ell_\infty(m)\bigr)\right)\right|
\le2\sum_{m>N}\frac1{m^2}=O\!\left(\frac1N\right)=O\!\left(\frac1Q\right).
\]
Combining the initial block with this tail bound proves the theorem.

## Verification
The standalone verifier checks the exact low-index branch choices with rational arithmetic for several integer values of \(Q\), verifies the unified summand identity for both parities, and numerically evaluates truncated source series for increasing \(Q\). The numerical values of
\[
Q\bigl(J(Q)-J_\infty\bigr)-\frac23\log Q
\]
stabilize near the constant suggested by the source's empirical fit, while the proof above uses no finite extrapolation. The computation is corroborative only; the asymptotic is established by the exact branch identities and the convergent tail estimate.

## Relationship to prior work
arXiv:2609.37459v1 derives the exact window series and reports computational evidence for a sharper expansion whose leading term is \((2/3)(\log Q)/Q\). The paper explicitly presents that asymptotic behavior as numerical evidence rather than a proof. The result here proves precisely the leading logarithmic term from the source's exact branch formulas.

Bai's arXiv:2609.11276 proves the improved irrationality-measure bound at the parameter point corresponding to \(Q=3714\), and establishes a strict local minimum of its auxiliary function in the relevant chamber. Zeilberger–Zudilin, arXiv:1912.06345v2 and the published 2020 article, provide the preceding integral construction and bound. Neither source states the limiting \((\log Q)/Q\) law proved here.

Targeted searches of published findings for the source identifier, the \(\widehat J\) slice, the limit formulation, and equivalent prime-elimination-window wording found no result implying this asymptotic. The closest semantic hits concerned unrelated logarithmic asymptotics in other objects.

## Limitations
The theorem determines only the leading coefficient. It does not prove the next constant in the source's empirical expansion, any monotonicity or unimodality statement for finite \(Q\), or the global optimality of \(Q=3714\). It also assumes the exact window-series formulas proved in arXiv:2609.37459v1; the present argument begins from those formulas rather than reconstructing the earlier contour-integral arithmetic.

## References
1. David Niedbala Giraudin, *A closed-form law for the Salikhov–Zeilberger–Zudilin–Bai family, and computational evidence that Bai's point is optimal*, arXiv:2609.37459v1, 2026.
2. Yufei Bai, *The irrationality measure of \(\pi\) is at most \(7.101862832357\)*, arXiv:2609.11276, 2026.
3. Doron Zeilberger and Wadim Zudilin, *The Irrationality Measure of \(\pi\) is at most \(7.103205334137\ldots\)*, arXiv:1912.06345v2; Moscow Journal of Combinatorics and Number Theory 9 (2020), 407–419.

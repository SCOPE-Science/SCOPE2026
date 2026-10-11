# Surjectivity is too strong for a controlled \(K\)-fusion characterization

## Finding
Theorem 10 of Assila--Kabbaj--Moalige states that, for a closed-range operator \(K\), a controlled \(K\)-fusion frame is equivalent to the controlled synthesis operator being surjective.

That is too strong. A \(K\)-fusion frame only has to reconstruct the range of \(K\), so the natural synthesis condition is range inclusion rather than surjectivity onto the entire Hilbert space.

Let
\[
H=\mathbb C^2,
\qquad
M=\operatorname{span}\{e_1\},
\qquad
K=P_M.
\]
Take one fusion subspace
\[
W_1=M,
\qquad
\omega_1=1,
\]
and controls
\[
C=C'=I.
\]
For every \(f=(f_1,f_2)\),
\[
\langle \pi_M f,\pi_M f\rangle
=|f_1|^2
=\|K^*f\|^2.
\]
Hence this is a Parseval controlled \(K\)-fusion frame.

The source defines the controlled analysis operator on this example by
\[
T_{C,C'}f=P_Mf
\]
with coefficient space \(M\). Its adjoint is therefore the inclusion
\[
T_{C,C'}^*:M\hookrightarrow H.
\]
Thus
\[
R(T_{C,C'}^*)=M\ne H,
\]
so the controlled synthesis operator is not surjective. The necessity direction of Theorem 10 fails.

The exact replacement is
\[
R(K)\subseteq R(T_{C,C'}^*).
\]
This condition is equivalent to the controlled \(K\)-fusion lower inequality and does not require \(K\) to have closed range.

## Assumptions and scope
The counterexample is finite-dimensional and uses positive invertible controls \(C=C'=I\), one positive weight, and one closed fusion subspace. The operator \(K=P_M\) is a nonzero orthogonal projection and therefore has closed range, so every hypothesis of the published theorem is satisfied.

The claim concerns Theorem 10's characterization by surjectivity. It does not challenge the Bessel characterization in Theorem 9 or the basic definition of controlled \(K\)-fusion frames.

## Proof
For the one-block family,
\[
\sum_i\omega_i^2\langle \pi_{W_i}Cf,\pi_{W_i}C'f\rangle
=
\|P_Mf\|^2.
\]
Since \(K=P_M=K^*\),
\[
\|P_Mf\|^2=\|K^*f\|^2\le \|f\|^2.
\]
Thus the controlled \(K\)-fusion inequalities hold with
\[
A=B=1.
\]

The source's controlled analysis operator is
\[
T_{C,C'}:H\to M,
\qquad
T_{C,C'}f=P_Mf.
\]
For \(x\in M\),
\[
\langle T_{C,C'}f,x\rangle_M
=
\langle P_Mf,x\rangle_H
=
\langle f,x\rangle_H,
\]
so
\[
T_{C,C'}^*x=x.
\]
Therefore \(T_{C,C'}^*\) is the inclusion of \(M\) into \(H\), and its range is the proper subspace \(M\). It is not surjective.

For the corrected characterization, the controlled frame operator is
\[
S_{C,C'}=T_{C,C'}^*T_{C,C'}.
\]
The lower controlled \(K\)-fusion inequality is equivalent to the operator inequality
\[
A K K^*\le S_{C,C'}
=
T_{C,C'}^*T_{C,C'}.
\]
Douglas' range inclusion theorem, applied to \(K\) and \(T_{C,C'}^*\), gives
\[
K K^*\le \lambda T_{C,C'}^*T_{C,C'}
\quad\Longleftrightarrow\quad
R(K)\subseteq R(T_{C,C'}^*)
\]
for some \(\lambda>0\). Combining this with the Bessel condition yields the exact criterion
\[
\text{controlled \(K\)-fusion frame}
\quad\Longleftrightarrow\quad
\text{controlled Bessel family and }R(K)\subseteq R(T_{C,C'}^*).
\]

If \(K\) is surjective, then \(R(K)=H\), and the corrected condition is exactly surjectivity of \(T_{C,C'}^*\). Thus surjectivity of \(K\), not merely closed range, is the boundary at which the printed characterization becomes valid.

## Verification
The complete theorem statement and the relevant proof were inspected in the publicly available full text of the article. The source defines the controlled analysis and synthesis operators immediately before Theorem 9, states the Bessel characterization in Theorem 9, and then states Theorem 10 with surjectivity of the synthesis operator.

The source's proof of necessity obtains an estimate only for vectors in \(R(K)\) and then concludes surjectivity onto all of \(H\). The projection example above isolates exactly that range mismatch.

The standard Douglas range theorem was checked in the surrounding \(K\)-frame literature. In particular, open full text on \(K\)-\(g\)-fusion frames states the equivalence between operator domination and range inclusion, and ordinary \(K\)-frame literature records that a Bessel family is a \(K\)-frame exactly when the range of \(K\) lies in the synthesis range.

No numerical approximation or finite search is used.

## Relationship to prior work
The distinction between ordinary frames and \(K\)-frames is already encoded in synthesis ranges: an ordinary frame has surjective synthesis, whereas a \(K\)-frame only requires the synthesis range to contain \(R(K)\).

The 2020 \(K\)-\(g\)-fusion paper gives the same operator-theoretic mechanism through Douglas' theorem: a lower \(K\)-frame inequality is an operator domination statement and therefore a range-inclusion statement. That broader result supports the corrected condition but does not state that Theorem 10 of the controlled-fusion paper is false, nor does it provide the one-block projection counterexample to that theorem.

Exact-source searches using the article DOI, arXiv identifier, theorem number, surjectivity formulation, range-inclusion formulation, and correction terms did not locate an indexed correction of Theorem 10.

## Limitations
The result corrects the characterization in Theorem 10. It does not attempt to audit other statements in the article.

The corrected criterion assumes the controlled analysis and synthesis operators are well-defined in the sense used by the source. The counterexample itself has a finite-dimensional closed coefficient space, so no domain or closure issue arises.

A nonindexed erratum or informal author correction may contain the same observation.

## References
1. N. Assila, S. Kabbaj and B. Moalige, *Controlled \(K\)-Fusion Frame for Hilbert Spaces*, arXiv:2007.05110v1; Moroccan Journal of Pure and Applied Analysis 7 (2021), 116--133, DOI 10.2478/mjpaa-2021-0011.
2. Y. Huang and Y. Yang, *\(K\)-\(g\)-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, Article 57, DOI 10.1186/s13660-020-02320-0.
3. Z.-Q. Xiang, *Some Properties of Canonical Dual \(K\)-Bessel Sequences for Parseval \(K\)-Frames*, Journal of Function Spaces 2019, Article 9862369, DOI 10.1155/2019/9862369.

# Exact phase boundary for dilation conditions in rank-one nilpotent \(\Gamma_n\)-contractions
## Finding
Let \(n\ge2\), let
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad T_k=\lambda_kN\quad(1\le k\le n),
\]
where \(\lambda_k\in\mathbb C\), \(|\lambda_n|<1\), and assume that \((T_1,\ldots,T_n)\) is a \(\Gamma_n\)-contraction. Put
\[
s=(1-|\lambda_n|^2)^{1/2}
\]
and let \(F_1,\ldots,F_{n-1}\) be the unique fundamental operators. For \(1\le i,j\le n-1\), define
\[
\Delta_{ij}=\lambda_i\overline{\lambda_{n-j}}-\lambda_j\overline{\lambda_{n-i}}.
\]
Then
\[
[F_i,F_j]=-{\lambda_n\Delta_{ij}\over s^3}N,
\]
and the defect of the mixed-adjoint identity is exactly
\[
F_iF_{n-j}^*-F_jF_{n-i}^*-F_{n-j}^*F_i+F_{n-i}^*F_j
={\Delta_{ij}\over s^2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Therefore the complete pair of fundamental-operator conditions
\[
F_iF_j=F_jF_i,
\qquad
F_iF_{n-j}^*-F_jF_{n-i}^*=F_{n-j}^*F_i-F_{n-i}^*F_j
\]
for every \(i,j\) holds if and only if every \(\Delta_{ij}\) is zero. This is equivalent to the phase-reversal condition
\[
\lambda_i=\eta\overline{\lambda_{n-i}}\qquad(1\le i\le n-1)
\]
for some \(\eta\in\mathbb T\). When \(\lambda_n\ne0\), pairwise commutativity and the mixed-adjoint identity are equivalent for each pair \((i,j)\). When \(\lambda_n=0\), all \(F_i\) commute automatically, but the mixed-adjoint identity still holds exactly when \(\Delta_{ij}=0\).

## Assumptions and scope
The theorem concerns the rank-one nilpotent slice in which every coordinate is a scalar multiple of the same square-zero matrix \(N\). It assumes, rather than classifies, the spectral-set condition making \((T_1,\ldots,T_n)\) a \(\Gamma_n\)-contraction. This is enough to ensure existence and uniqueness of the fundamental operators. The result applies in particular to the nilpotent two-by-two families considered in arXiv:2609.39711v1 whenever their parameters yield a \(\Gamma_n\)-contraction.

No assertion is made that the displayed fundamental-operator conditions are necessary for the existence of a \(\Gamma_n\)-isometric dilation. The focal source shows that they are not necessary in general. The claim here is an exact classification of when those conditions themselves hold inside this natural nilpotent slice.

## Proof
Since
\[
T_n^*T_n=\begin{pmatrix}0&0\\0&|\lambda_n|^2\end{pmatrix},
\]
the defect operator is
\[
D_{T_n}=\begin{pmatrix}1&0\\0&s\end{pmatrix},
\qquad s=(1-|\lambda_n|^2)^{1/2}>0.
\]
The fundamental equation is
\[
T_i-T_{n-i}^*T_n=D_{T_n}F_iD_{T_n}.
\]
Directly,
\[
T_{n-i}^*T_n=
\begin{pmatrix}0&0\\0&\overline{\lambda_{n-i}}\lambda_n\end{pmatrix},
\]
so invertibility of \(D_{T_n}\) gives
\[
F_i=
\begin{pmatrix}
0&\lambda_i/s\\
0&-\overline{\lambda_{n-i}}\lambda_n/s^2
\end{pmatrix}.
\]
Writing \(a_i=\lambda_i/s\) and \(b_i=-\overline{\lambda_{n-i}}\lambda_n/s^2\), one has
\[
F_i=\begin{pmatrix}0&a_i\\0&b_i\end{pmatrix}.
\]
Hence
\[
[F_i,F_j]
=\begin{pmatrix}0&a_ib_j-a_jb_i\\0&0\end{pmatrix}
=-{\lambda_n\Delta_{ij}\over s^3}N.
\]
This proves the commutator formula.

For the mixed-adjoint condition, expand the four products using the same two-entry form. The off-diagonal terms cancel, and the two diagonal entries are opposite. The result is
\[
F_iF_{n-j}^*-F_jF_{n-i}^*-F_{n-j}^*F_i+F_{n-i}^*F_j
={\Delta_{ij}\over s^2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Thus the mixed-adjoint identity holds exactly when \(\Delta_{ij}=0\). If \(\lambda_n\ne0\), the commutator formula shows that commutativity holds for the same and only the same pairs. If \(\lambda_n=0\), every \(b_i=0\), so commutativity is automatic, while the mixed-adjoint criterion is unchanged.

It remains to identify the simultaneous zero locus of all \(\Delta_{ij}\). Put
\[
u=(\lambda_1,\ldots,\lambda_{n-1}),
\qquad
v=(\overline{\lambda_{n-1}},\ldots,\overline{\lambda_1}).
\]
The quantities \(\Delta_{ij}\) are precisely the two-by-two minors of the matrix with rows \(u\) and \(v\). Hence they all vanish exactly when those two rows have rank at most one. If \(u=0\), the phase-reversal relation holds for any \(\eta\in\mathbb T\). If \(u\ne0\), then also \(v\ne0\), so \(u=\eta v\) for a scalar \(\eta\). Because reversal and conjugation preserve the Euclidean norm, \(\|u\|_2=\|v\|_2\), and therefore \(|\eta|=1\). This gives the stated phase-reversal characterization. The converse is immediate.

## Verification
The proof uses only the defining fundamental equation and exact two-by-two matrix multiplication. The commutator and mixed-adjoint defect were independently expanded symbolically from
\[
F_i=
\begin{pmatrix}
0&\lambda_i/s\\
0&-\overline{\lambda_{n-i}}\lambda_n/s^2
\end{pmatrix}.
\]
Boundary cases were checked explicitly. For \(n=2\), there is only one fundamental operator and the conditions are tautological; the phase-reversal relation is always realizable. For \(\lambda_n=0\), the commutators vanish but the mixed-adjoint defect remains \(\Delta_{ij}s^{-2}\operatorname{diag}(1,-1)\). For \(u=0\), all minors vanish and the phase relation is vacuous.

The argument is an exact finite-dimensional proof. No numerical experiment, finite enumeration, or unproved limiting step is used.

## Relationship to prior work
Bhaskar Paul, arXiv:2609.39711v1, studies two-by-two \(\Gamma_n\)-contractions with noncommutative fundamental operators. Its second nilpotent family uses determinant-type expressions of the form \(\lambda_i\overline{\lambda_{n-j}}-\lambda_j\overline{\lambda_{n-i}}\) to force failures of the two conditions used in conditional dilation theory. The present result identifies the entire zero locus of those expressions, proves exact formulas for both defects, and shows that the simultaneous boundary is the rank-one, phase-reversal locus. The focal paper does not state this if-and-only-if classification.

Bisai and Pal's work on fundamental operators for the symmetrized tridisc develops existence, uniqueness, admissibility, and examples of noncommuting fundamental operators. Those results supply broader structural context but do not give the all-\(n\) coefficient classification above for the common rank-one nilpotent slice.

## Limitations
The theorem does not classify all coefficient vectors \((\lambda_1,\ldots,\lambda_n)\) for which the tuple is a \(\Gamma_n\)-contraction. It also does not construct a dilation, nor does it turn the two sufficient fundamental-operator conditions into necessary conditions for dilation. The classification is specific to tuples whose coordinates are scalar multiples of one rank-one square-zero matrix.

An originality search cannot rule out an older equivalent result stated under different terminology. The closest checked literature concerns general fundamental-operator theory, tridisc admissibility, or examples of noncommutativity; no source inspected states the exact minor formulas together with the phase-reversal classification.

## References
1. Bhaskar Paul, *The Families of \(\Gamma_n\)-Contractions Having Non-commutative Fundamental Operators*, arXiv:2609.39711v1, 2026.
2. Bappa Bisai and Sourav Pal, *Automorphisms and the fundamental operators associated with the symmetrized tridisc*, arXiv:1610.01978; published in *Proceedings of the Indian Academy of Sciences (Mathematical Sciences)*, 2021.
3. Bappa Bisai and Sourav Pal, *The fundamental operator tuples associated with the symmetrized polydisc*, *New York Journal of Mathematics* 27 (2021), 349–362.

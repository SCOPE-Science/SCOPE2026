# A Fourier-unitary obstruction to Bessel weak \(A\)-duals

## Finding
Bellomonte's Theorem 3.20 characterizes continuous weak \(A\)-frames by the existence of a Bessel weak \(A\)-dual. The implication from the frame inequality to such a dual is false on a nonatomic coefficient space.

Let
\[
H=\ell^2(\mathbb Z),\qquad X=[0,1]
\]
with Lebesgue measure, and let \((u_n)_{n\in\mathbb Z}\) be the canonical orthonormal basis of \(H\). Let
\[
(Mc)(x)=\sum_{n\in\mathbb Z}c_ne^{2\pi i n x}
\]
be the Fourier unitary from \(H\) onto \(L^2[0,1]\). Define
\[
\lambda_n=2^{-|n|},\qquad (Ac)_n=\lambda_nc_n.
\]
Then \(A\) is bounded, self-adjoint, injective, compact, and densely defined on all of \(H\). Set
\[
\phi_x=(\lambda_ne^{-2\pi i n x})_{n\in\mathbb Z}.
\]
Because
\[
\sum_{n\in\mathbb Z}\lambda_n^2
=1+2\sum_{n\ge1}4^{-n}
=\frac53,
\]
every \(\phi_x\) belongs to \(H\), with constant norm \(\sqrt{5/3}\), and \(x\mapsto\langle c,\phi_x\rangle\) is measurable for every \(c\in H\).

For every \(c\in H\),
\[
\langle c,\phi_x\rangle
=\sum_{n\in\mathbb Z}c_n\lambda_ne^{2\pi i n x}
=(MAc)(x).
\]
Hence, by Plancherel,
\[
\int_0^1|\langle c,\phi_x\rangle|^2\,dx
=\|Ac\|^2
=\|A^*c\|^2.
\]
Thus \(\phi\) is a continuous weak \(A\)-frame with lower constant \(1\).

Nevertheless, \(\phi\) has no Bessel weak \(A\)-dual.

## Assumptions and scope
The example uses a bounded operator \(A\), which is a special case of the theorem's closable densely defined operator. The coefficient space is the standard nonatomic probability space \([0,1]\), and the Hilbert space is separable.

The finding refutes only the implication in Theorem 3.20 asserting that every continuous weak \(A\)-frame has a Bessel weak \(A\)-dual. The converse implications are not assessed here. The same pointwise-representation issue also affects Proposition 3.21, which starts from an arbitrary bounded operator into \(L^2(X,\mu)\) and postulates representing vectors pointwise.

The exact missing condition in the theorem's proof is not compactness, injectivity, or boundedness of \(M\), but pointwise Bessel representability: the factor \(M:H\to L^2(X,\mu)\) used in the factorization must itself be the analysis operator of an \(H\)-valued Bessel field.

## Proof
Let \(C_\phi:H\to L^2[0,1]\) denote the analysis operator of \(\phi\). The calculation above gives
\[
C_\phi=MA.
\]
Therefore
\[
C_\phi^*=AM^*.
\]
Since \(M\) is unitary,
\[
C_\phi^*M=AM^*M=A.
\]

Assume for contradiction that there exists a Bessel weak \(A\)-dual \(\psi\). Its analysis operator
\[
C_\psi h=(\langle h,\psi_x\rangle)_{x\in[0,1]}
\]
is bounded from \(H\) to \(L^2[0,1]\). The weak dual identity says that for all \(f,u\in H\),
\[
\langle Af,u\rangle
=\int_0^1\langle f,\psi_x\rangle\langle\phi_x,u\rangle\,dx
=\langle C_\psi f,C_\phi u\rangle_{L^2}.
\]
Consequently
\[
A=C_\phi^*C_\psi.
\]
Together with \(A=C_\phi^*M\), this gives
\[
C_\phi^*(C_\psi-M)=0.
\]
But \(C_\phi^*=AM^*\) is injective because both \(A\) and \(M^*\) are injective. Hence
\[
C_\psi=M.
\]

For each \(n\in\mathbb Z\), equality in \(L^2[0,1]\) gives
\[
\langle u_n,\psi_x\rangle=e^{2\pi i n x}
\]
for almost every \(x\). Because \(\mathbb Z\) is countable, there is one full-measure set on which these equalities hold simultaneously for every \(n\). For any \(x\) in that set, Parseval's identity in \(H\) would give
\[
\|\psi_x\|^2
=\sum_{n\in\mathbb Z}|\langle u_n,\psi_x\rangle|^2
=\sum_{n\in\mathbb Z}1,
\]
which is impossible for a vector of \(H\). This contradiction proves that no Bessel weak \(A\)-dual exists.

The faulty source step is now transparent. A bounded operator \(M:H\to L^2(X,\mu)\) determines only equivalence classes of functions. On a nonatomic \(L^2\)-space, evaluation at a point is neither well-defined on equivalence classes nor a bounded functional. Therefore the Riesz representation theorem cannot be applied pointwise to \(h\mapsto(Mh)(x)\) for an arbitrary bounded \(M\).

A useful sufficient repair is Hilbert--Schmidt factorization. If \(M:H\to L^2(X,\mu)\) is Hilbert--Schmidt and \((h_n)\) is an orthonormal basis of \(H\), choose measurable representatives \(g_n=Mh_n\). Then
\[
\int_X\sum_n|g_n(x)|^2\,d\mu(x)
=\sum_n\|Mh_n\|_{L^2}^2
=\|M\|_{\mathrm{HS}}^2<\infty.
\]
Thus \(\sum_n|g_n(x)|^2<\infty\) almost everywhere. On that full-measure set define
\[
\psi_x=\sum_n\overline{g_n(x)}h_n.
\]
Then \((Mh)(x)=\langle h,\psi_x\rangle\) almost everywhere and
\[
\int_X|\langle h,\psi_x\rangle|^2\,d\mu(x)
=\|Mh\|_{L^2}^2
\le\|M\|^2\|h\|^2,
\]
so \(\psi\) is Bessel. Hilbert--Schmidt regularity is sufficient, not asserted to be necessary.

## Verification
The published source was read at Definition 3.1, Definition 3.9, Theorem 3.20, and Proposition 3.21. Theorem 3.20 explicitly states equivalence with existence of a Bessel weak \(A\)-dual. In the proof of the disputed implication, the factorization produces a bounded \(M:H\to L^2(X,\mu)\), after which the text invokes the Riesz representation theorem separately for every \(x\) to obtain \(\psi_x\). Proposition 3.21 repeats the same pointwise step for an arbitrary bounded \(M\).

The counterexample is exact. Plancherel gives the continuous weak \(A\)-frame identity, and injectivity of \(C_\phi^*=AM^*\) forces any Bessel weak dual analysis operator to equal the Fourier unitary. The contradiction then follows from the square-summability requirement for the coordinates of a Hilbert-space vector. No numerical sampling, truncation, or finite-dimensional approximation is used as proof.

## Relationship to prior work
The issue is specific to the passage from an arbitrary bounded operator into a nonatomic \(L^2\)-space to pointwise Hilbert-space representing vectors. In a discrete counting-measure coefficient space, this obstruction disappears: if \(M:H\to\ell^2(I)\) is bounded, then the coordinates are bounded functionals and may be represented by \(\psi_i=M^*e_i\). Thus the source's pointwise Riesz argument is valid in the discrete setting but not in general continuous settings.

Later work on weak \(A\)-frames and weak \(A\)-semi-frames uses the same duality framework, while general continuous-frame theory relates analysis-operator ranges to reproducing-kernel structure. These comparisons are consistent with the obstruction above: an arbitrary bounded map onto a nonatomic \(L^2\)-space need not arise from pointwise vector evaluation.

Targeted searches for the exact theorem, Proposition 3.21, point-evaluation/Riesz formulations, Fourier-unitary examples, and Hilbert--Schmidt repairs did not locate an indexed source giving this counterexample or the same source-specific correction.

## Limitations
The result does not characterize all bounded operators \(M:H\to L^2(X,\mu)\) that admit an \(H\)-valued Bessel representation. Pointwise Bessel representability is the exact condition needed by the proof, while Hilbert--Schmidt regularity is only a convenient sufficient condition.

The finding does not assess the other directions of Theorem 3.20 or unrelated results in the article. An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. G. Bellomonte, *Continuous frames for unbounded operators*, arXiv:1912.13097v1, 30 December 2019; *Advances in Operator Theory* 6 (2021), article 41, DOI 10.1007/s43036-021-00136-3.
2. J.-P. Antoine, G. Bellomonte and C. Trapani, *Weak \(A\)-frames and weak \(A\)-semi-frames*, *Constructive Mathematical Analysis* 4 (2021), 104--118, DOI 10.33205/cma.835582.
3. M. Speckbacher and P. Balazs, *Frames, their relatives and reproducing kernel Hilbert spaces*, *Journal of Physics A: Mathematical and Theoretical* 52 (2019), 495201, arXiv:1704.02818.

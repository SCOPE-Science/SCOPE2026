# Closed range repairs the image characterization of woven \(K\)-frames

## Finding
Proposition 2.5 of Bhandari--Borah--Mukherjee states, for an arbitrary bounded operator \(K\), that
\[
\{f_i\},\{g_i\}\text{ woven in }R(K^*)
\quad\Longleftrightarrow\quad
\{Kf_i\},\{Kg_i\}\text{ \(K\)-woven in }H.
\]
The reverse implication is false when \(K\) has nonclosed range.

Let
\[
H=\ell^2(\mathbb N)
\]
with standard orthonormal basis \((e_n)_{n\ge1}\), and define
\[
Ke_n=\frac1n e_n.
\]
Take
\[
f_n=g_n=n e_n.
\]
Then
\[
Kf_n=Kg_n=e_n.
\]
Thus every weave of the transformed pair is exactly the standard orthonormal basis and is a \(K\)-frame with universal bounds \(1,1\).

On the other hand, for
\[
x_N=Ke_N=\frac1N e_N\in R(K^*),
\]
the corresponding original weaving energy is
\[
\sum_{n=1}^{\infty}|\langle x_N,n e_n\rangle|^2=1,
\]
while
\[
\|x_N\|^2=\frac1{N^2}.
\]
No finite upper frame bound on \(R(K^*)\) exists. Hence Proposition 2.5 is false as stated.

There is an exact repair: if \(K\) has closed range, the equivalence is valid. If the original pair is woven on \(R(K^*)\) with bounds \(A,B\), then the image pair is \(K\)-woven with bounds
\[
A,\qquad B\|K\|^2.
\]
If the image pair is \(K\)-woven with bounds \(C,D\), then the original pair is woven on \(R(K^*)\) with bounds
\[
C,\qquad D\|K^\dagger\|^2.
\]

## Assumptions and scope
The counterexample uses the same ambient Hilbert-space norm that appears in equation (5) of the source proof.

The operator
\[
K=\operatorname{diag}\left(1,\frac12,\frac13,\ldots\right)
\]
is bounded and self-adjoint. Its range is
\[
R(K)=
\left\{
y\in\ell^2:
\sum_{n=1}^{\infty}n^2|y_n|^2<\infty
\right\}.
\]
This range is dense but not closed. For example,
\[
y=\left(1,\frac12,\frac13,\ldots\right)\in\ell^2
\]
does not belong to \(R(K)\), while its finite truncations do and converge to \(y\).

Because a nonclosed operator range is not a Hilbert space with the inherited norm, the phrase “frame in \(R(K^*)\)” is itself problematic under the standard frame definition. The counterexample is stronger than that formal issue: even if the phrase is interpreted exactly through the two-sided inequalities written in the source proof, the upper inequality fails.

## Proof
For every \(h=(h_n)\in\ell^2\),
\[
\|K^*h\|^2
=
\sum_{n=1}^{\infty}\frac{|h_n|^2}{n^2}
\le
\sum_{n=1}^{\infty}|h_n|^2
=
\|h\|^2.
\]
Since
\[
Kf_n=Kg_n=e_n,
\]
every partition chooses one copy of \(e_n\) at each index. Hence every transformed weave has energy
\[
\sum_{n=1}^{\infty}|\langle h,e_n\rangle|^2=\|h\|^2.
\]
It is therefore a \(K\)-frame with lower and upper bounds \(1,1\).

For the original pair, the same partition independence holds because \(f_n=g_n\). At
\[
x_N=\frac1N e_N
\]
the only nonzero coefficient is
\[
\langle x_N,N e_N\rangle=1.
\]
Thus the energy-to-norm ratio is
\[
\frac{1}{1/N^2}=N^2,
\]
which is unbounded. This disproves the implication from image \(K\)-wovenness to ordinary wovenness on \(R(K^*)\).

Now suppose \(K\) has closed range.

If the original pair is woven on \(R(K^*)\) with bounds \(A,B\), then for any \(h\in H\) and any partition, set
\[
x=K^*h\in R(K^*).
\]
The image weaving energy equals the original weaving energy at \(x\), and therefore lies between
\[
A\|K^*h\|^2
\]
and
\[
B\|K^*h\|^2\le B\|K\|^2\|h\|^2.
\]
This proves the first repaired implication.

Conversely, suppose the image pair is \(K\)-woven with bounds \(C,D\). For \(x\in R(K^*)\), closed range makes the Moore--Penrose inverse bounded. Put
\[
h=(K^*)^\dagger x.
\]
Then
\[
K^*h=x
\]
and
\[
\|h\|\le\|(K^*)^\dagger\|\|x\|
=
\|K^\dagger\|\|x\|.
\]
The original weaving energy at \(x\) equals the image weaving energy at \(h\). Hence it is at least
\[
C\|K^*h\|^2=C\|x\|^2
\]
and at most
\[
D\|h\|^2
\le
D\|K^\dagger\|^2\|x\|^2.
\]
This proves the repaired equivalence and the stated quantitative bounds.

## Verification
The open preprint was inspected at the definition of \(K\)-woven frames, the Moore--Penrose lemma, Proposition 2.5, its complete proof, and the adjacent Proposition 2.6.

The source proves the lower bound in the reverse implication by choosing a preimage \(h\) with
\[
x=K^*h.
\]
It then states that the upper bound follows from its general Bessel-weaving proposition. That step is unavailable: the hypothesis only says that the sequences \((Kf_i)\) and \((Kg_i)\) are Bessel, not that the original sequences have a uniform Bessel bound on \(R(K^*)\).

The counterexample is symbolic. The transformed pair is an orthonormal basis, and the failure ratio for the original pair is exactly \(N^2\).

## Relationship to prior work
Later operator-preservation work on woven \(K\)- and \(K\)-\(g\)-frames repeatedly imposes closed-range, surjectivity, or bounded-inverse hypotheses when transferring frame bounds between operator ranges. These conditions are consistent with the repair above because they provide uniform control of preimages.

A 2021 paper on weaving \(K\)-\(g\)-frames formulates its operator-transfer results using closed ranges and pseudo-inverses. A 2024 extension to \(n\)-Hilbert spaces likewise places closed-range assumptions in image-construction theorems.

Targeted searches for the exact source title, Proposition 2.5, the formulas involving \(R(K^*)\) and \(Kf_i\), nonclosed-range counterexamples, and correction terminology did not locate an indexed erratum or this diagonal counterexample.

## Limitations
The finding refutes Proposition 2.5 for arbitrary bounded \(K\) and supplies a sufficient closed-range repair with explicit bounds.

It does not claim that closed range is the weakest possible hypothesis for a particular fixed pair of sequences. Pair-specific upper control may hold even when \(R(K^*)\) is not closed.

An unindexed note, thesis, or informal correction may contain the same observation.

## References
1. A. Bhandari, D. Borah and S. Mukherjee, *Characterizations of Weaving \(K\)-frames*, arXiv:1907.08757v1, 20 July 2019; Proceedings of the Japan Academy, Series A, Mathematical Sciences 96 (2020), 39--43, DOI 10.3792/pjaa.96.008.
2. Z. Xiang, *Some new results on the weaving of \(K\)-\(g\)-frames in Hilbert spaces*, Open Mathematics 19 (2021), 1315--1329, DOI 10.1515/math-2021-0103.
3. G. Wang, *Some properties of weaving \(K\)-frames in \(n\)-Hilbert space*, AIMS Mathematics 9 (2024), 25438--25456, DOI 10.3934/math.20241242.

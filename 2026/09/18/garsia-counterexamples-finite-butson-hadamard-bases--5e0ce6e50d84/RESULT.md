# Garsia counterexamples among finite Butson-Hadamard bases

## Statement

There is an absolute constant \(c>0\) with the following property.

For every \(H>0\), there is \(M_0(H)\) such that for every prime \(M\ge M_0(H)\) one can construct a \(2M\times 2M\) complex Hadamard matrix
\[
\mathsf H_M=(h_{x,j})_{x,j=1}^{2M}
\]
whose entries are \(2M\)-th roots of unity, and such that for **every** permutation \(\tau\) of its columns there is a real vector
\[
a=(a_1,\dots,a_{2M})\in\mathbb R^{2M},
\qquad
\sum_{j=1}^{2M}a_j^2=1,
\]
for which
\[
\#\left\{
x:
\max_{1\le q\le 2M}
\left|
\sum_{\ell=1}^{q}a_{\tau(\ell)}
h_{x,\tau(\ell)}
\right|>H
\right\}
\ge c(2M).
\]

Equivalently, on a finite probability space of \(2M\) equiprobable atoms there is a **complete** orthonormal basis of unimodular functions such that every rearrangement has maximal-partial-sum operator norm at least \(H\sqrt c\).

Thus the finite counterexample to Garsia's rearrangement conjecture can be required simultaneously to be

- finite atomic;
- a complete orthonormal basis, rather than merely an orthonormal subsystem;
- unimodular at every atom; and
- the normalized column system of a Butson-type complex Hadamard matrix.

No quantitative bound for \(M_0(H)\) is asserted.

## Context

Lewko recently gave a negative solution of Garsia's conjecture. His finite theorem produces, for each \(H\), a finite unimodular orthonormal system on
\[
\mathbb T\times\{0,1\},
\]
built from two differently ordered copies of the trigonometric system, for which every permutation admits a real unit coefficient vector with large maximal partial sums on a set of fixed positive measure. His infinite construction is then completed to a unimodular orthonormal basis.

The finite theorem itself does not impose finite atomicity or completeness. The result here shows that neither feature provides an escape from the counterexample: the obstruction persists inside square complex Hadamard bases on finite sets.

## Proof

Write
\[
e(t)=e^{2\pi i t}.
\]

### 1. Lewko's finite Fourier block

Lewko's Lemma 4 supplies an absolute \(\delta>0\) such that, for the threshold \(2H\), there are an integer \(m\), a permutation \(\pi\) of \([m]\), and real coefficients \(b_1,\dots,b_m\) satisfying
\[
\sum_{j=1}^m b_j^2=1
\]
and
\[
\left|
\left\{
x\in\mathbb T:
\max_{q\le m}
\left|
\sum_{j\le q}b_j e(\pi(j)x)
\right|>2H
\right\}
\right|
\ge\delta.
\]
Denote this open bad set by \(B\).

Lewko's combinatorial Lemma 2, applied to \(\pi\), gives an integer \(N\ge m\) and a permutation \(\sigma\) of \([N]\) with the following property: for every permutation \(\tau\) of \([N]\), some \(m\)-term arithmetic progression in \([N]\) appears with order pattern \(\pi\) as a subsequence of at least one of the two lists
\[
\tau,\qquad \sigma\circ\tau.
\]

### 2. Discretize the Fourier block on a prime cyclic group

Because \(B\) is open and has measure at least \(\delta\), regularity of Lebesgue measure gives a continuous function
\[
0\le \eta\le 1_B
\]
with
\[
\int_{\mathbb T}\eta(x)\,dx\ge \frac{\delta}{2}.
\]
The uniform Riemann sums therefore satisfy
\[
\frac1M\sum_{r=0}^{M-1}\eta(r/M)\longrightarrow
\int_{\mathbb T}\eta.
\]
Hence there is \(M_1\) such that, for every \(M\ge M_1\),
\[
\#\{r\in\mathbb Z_M:r/M\in B\}\ge \frac{\delta}{3}M.
\]

Now take any prime
\[
M>\max\{N,M_1,2\}.
\]
Extend \(\sigma\) arbitrarily from \([N]\) to a permutation
\[
\widetilde\sigma:\mathbb Z_M\to\mathbb Z_M.
\]

Let
\[
\Omega_M=\mathbb Z_M\times\{0,1\}
\]
with uniform probability measure. For \(n\in\mathbb Z_M\), define
\[
u_n(r,0)=e(nr/M),\qquad
u_n(r,1)=e(\widetilde\sigma(n)r/M),
\]
and
\[
v_n(r,\varepsilon)=(-1)^\varepsilon u_n(r,\varepsilon).
\]

### 3. The \(2M\) functions form a complete unimodular basis

For \(n,m\in\mathbb Z_M\),
\[
\langle u_n,u_m\rangle
=
\frac12\left(
\delta_{nm}
+
\delta_{\widetilde\sigma(n),\widetilde\sigma(m)}
\right)
=
\delta_{nm}.
\]
Likewise,
\[
\langle v_n,v_m\rangle=\delta_{nm},
\]
while
\[
\langle u_n,v_m\rangle
=
\frac12\left(
\delta_{nm}
-
\delta_{\widetilde\sigma(n),\widetilde\sigma(m)}
\right)
=0.
\]
Thus
\[
\{u_n:n\in\mathbb Z_M\}
\cup
\{v_n:n\in\mathbb Z_M\}
\]
is an orthonormal family of \(2M\) vectors in the \(2M\)-dimensional Hilbert space \(L^2(\Omega_M)\), hence an orthonormal basis.

Every value of every basis function has modulus one. If the atoms are used as rows and the basis functions as columns, the resulting square matrix \(\mathsf H_M\) satisfies
\[
\mathsf H_M^*\mathsf H_M=2M I.
\]
Its entries are of the form
\[
e(k/M)\quad\text{or}\quad -e(k/M),
\]
hence are \(2M\)-th roots of unity because \(M\) is odd. Therefore \(\mathsf H_M\) is a Butson-type complex Hadamard matrix.

In block form, after ordering the \(u\)-columns before the \(v\)-columns,
\[
\mathsf H_M
=
\begin{pmatrix}
F_M & F_M\\
F_M P_{\widetilde\sigma} & -F_M P_{\widetilde\sigma}
\end{pmatrix},
\]
up to the harmless convention used for the permutation matrix \(P_{\widetilde\sigma}\).

### 4. Every column permutation contains Lewko's obstruction

Fix an arbitrary permutation of all \(2M\) columns.

Ignore every \(v_n\)-column and every \(u_n\)-column with \(n\notin[N]\). The remaining columns \(u_1,\dots,u_N\) inherit some order \(\tau\), a permutation of \([N]\).

By Lewko's combinatorial lemma, there is an arithmetic progression
\[
x_j=a+dj,\qquad j=1,\dots,m,
\]
in \([N]\) whose terms occur in the order
\[
x_{\pi(1)},\dots,x_{\pi(m)}
\]
either in the frequency list on the \(\varepsilon=0\) layer or in the frequency list on the \(\varepsilon=1\) layer.

Assign coefficient \(b_j\) to the corresponding \(u\)-column carrying frequency \(x_{\pi(j)}\) on that layer, and assign coefficient zero to every other column of the full basis. The coefficient vector is real and has Euclidean norm one. Columns with zero coefficient may occur between selected columns, but they do not change any partial sum; consequently the maximal partial sum for the full column ordering dominates the maximal partial sum over the selected subsequence.

On the chosen layer, at the atom \(r\in\mathbb Z_M\), the selected partial sums have absolute values
\[
\left|
\sum_{j\le q}b_j e((a+d\pi(j))r/M)
\right|
=
\left|
\sum_{j\le q}b_j e(\pi(j)dr/M)
\right|.
\]
Since the progression lies in \([N]\) and \(M>N\), its step satisfies
\[
1\le d<M.
\]
Because \(M\) is prime, multiplication by \(d\) permutes \(\mathbb Z_M\). Hence the distribution over \(r\in\mathbb Z_M\) of these finite maximal sums is exactly the distribution of the base Fourier block sampled on the grid \(\{r/M\}\).

At least \(\delta M/3\) grid points belong to \(B\), so on at least that many atoms of the chosen layer the maximal partial sum exceeds \(2H\), and therefore exceeds \(H\). Since \(\Omega_M\) has \(2M\) atoms, the exceptional proportion is at least
\[
\frac{\delta}{6}.
\]
Thus the theorem holds with the absolute constant
\[
c=\frac{\delta}{6}.
\]

Because the argument works for every sufficiently large prime \(M\), it produces infinitely many Hadamard orders for each fixed threshold \(H\).

## Interpretation

Lewko's theorem shows that no universal rearrangement can control all square-summable coefficient vectors even for uniformly bounded orthonormal systems. The present strengthening shows that incompleteness and nonatomicity are not responsible for the failure.

The counterexamples can live in finite-dimensional Hilbert spaces with exactly as many unimodular basis vectors as atoms. Equivalently, the obstruction occurs inside the rigid class of square Butson-Hadamard matrices. In this setting there is no hidden complement of the orthonormal system and no limiting probability-space issue: every vector in \(L^2(\Omega_M)\) is expanded in the displayed basis.

The block form also separates the two ingredients cleanly. The Fourier matrix supplies exact finite cyclic orthogonality, while the lower-block column permutation carries the combinatorial two-ordering obstruction.

## Prior literature and originality boundary

Lewko's arXiv:2609.18491 proves the negative answer to Garsia's conjecture and provides the two-copy trigonometric mechanism used here. It also explains how to complete the *infinite* counterexample. Those results, Lewko's Fourier divergence lemma, and his combinatorial permutation lemma are prior work and are not claimed as new.

Bourgain's earlier work supplies the classical universal upper bound for suitably rearranged uniformly bounded systems and is part of the background to Garsia's conjecture.

Dutkay--Han--Sun studied divergence and unusually large Dirichlet kernels for structured scrambled Fourier systems related to Hadamard matrices. That is a different quantifier structure: it concerns specified scrambled Fourier orderings, not a finite complete basis for which **every** column permutation admits a coefficient vector producing large maximal partial sums.

To the best of our knowledge, searches for Garsia/Kolmogorov rearrangement counterexamples on finite groups, finite atomic complete bases, complex Hadamard matrices, Butson matrices, and Fourier-Hadamard block constructions did not locate the statement above. The principal originality risk is that the finite cyclic completion is short once Lewko's new construction is available, so an unrecorded or not-yet-indexed parallel observation is plausible.

## Limitations

- No useful quantitative dependence of \(M_0(H)\) on \(H\) is obtained; the construction inherits the qualitative bounds in Lewko's Fourier-divergence and Szemerédi-theorem inputs.
- The matrices are complex Butson-Hadamard matrices. No analogous conclusion for real \(\{\pm1\}\)-Hadamard matrices is proved.
- The result does not improve Lewko's negative solution of the infinite Kolmogorov rearrangement problem.
- The result is an existence theorem and does not give an efficient algorithm for finding the permutation \(\widetilde\sigma\) or the witnessing coefficients.
- No independent validation has been performed.

## References

1. M. Lewko, *On Kolmogorov's rearrangement problem and Garsia's conjecture*, arXiv:2609.18491v1 (2026).
2. J. Bourgain, *On Kolmogorov's rearrangement problem for orthogonal systems and Garsia's conjecture*, in *Geometric Aspects of Functional Analysis (1987--88)*, Lecture Notes in Mathematics 1376, Springer, 1989, 209--250. DOI: 10.1007/BFb0090057.
3. D. E. Dutkay, D. Han, and Q. Sun, *Divergence of the mock and scrambled Fourier series on fractal measures*, Trans. Amer. Math. Soc. 366 (2014), 2191--2208; arXiv:1103.4380.

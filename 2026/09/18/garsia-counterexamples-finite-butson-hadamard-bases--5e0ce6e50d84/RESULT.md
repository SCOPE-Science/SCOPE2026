# Garsia counterexamples among finite Butson-Hadamard bases

## Statement

There is an absolute constant \(c>0\) such that for every \(H>0\) there is \(M_0(H)\) with the following property. For every prime \(M\ge M_0(H)\), there is a \(2M\times2M\) complex Hadamard matrix
\[
\mathsf H_M=(h_{x,j})
\]
whose entries are \(2M\)-th roots of unity and such that, for every permutation \(\tau\) of its columns, one can find a real vector \(a\in\mathbb R^{2M}\) with \(\|a\|_2=1\) for which
\[
\#\left\{x:
\max_{1\le q\le2M}
\left|\sum_{\ell\le q}a_{\tau(\ell)}h_{x,\tau(\ell)}\right|>H
\right\}\ge c(2M).
\]

Equivalently, Garsia's universal rearrangement bound fails even if the finite orthonormal system is required to be a complete unimodular basis on a finite atomic probability space. The basis can be the column system of a Butson-type complex Hadamard matrix.

## Context

Lewko's arXiv:2609.18491 gives a negative solution of Garsia's conjecture. Its finite construction is a unimodular orthonormal system on
\[
\mathbb T\times\{0,1\},
\]
formed from two differently ordered copies of the trigonometric system. For every ordering of those functions there is a real unit coefficient vector whose maximal partial sums are large on a set of fixed positive measure. The paper separately explains how to complete the infinite construction.

The point here is that the finite obstruction survives both discretization and completion: it can occur in a square, finite, unimodular basis with no unused orthogonal complement.

## Proof

Write \(e(t)=e^{2\pi i t}\).

Lewko's Lemma 4 gives an absolute \(\delta>0\) such that, applied at threshold \(2H\), there are an integer \(m\), a permutation \(\pi\) of \([m]\), and real coefficients \(b_1,\dots,b_m\) satisfying
\[
\sum_{j=1}^m b_j^2=1
\]
and
\[
\left|\left\{x\in\mathbb T:
\max_{q\le m}\left|\sum_{j\le q}b_j e(\pi(j)x)\right|>2H
\right\}\right|\ge\delta.
\]
Call this open set \(B\).

Lewko's Lemma 2 supplies \(N\ge m\) and a permutation \(\sigma\) of \([N]\) such that every permutation \(\tau\) of \([N]\) contains an \(m\)-term arithmetic progression with order pattern \(\pi\) in at least one of the two lists
\[
\tau,\qquad \sigma\circ\tau.
\]

Because \(B\) is open and has measure at least \(\delta\), choose a continuous cutoff \(0\le\eta\le1_B\) with
\[
\int_{\mathbb T}\eta\ge\delta/2.
\]
Uniform Riemann sums then show that, for every sufficiently large integer \(M\),
\[
\#\{r\in\mathbb Z_M:r/M\in B\}\ge \delta M/3.
\]
Take a prime \(M>N\) large enough for this estimate and extend \(\sigma\) arbitrarily to a permutation
\[
\widetilde\sigma:\mathbb Z_M\to\mathbb Z_M.
\]

On the \(2M\)-point probability space
\[
\Omega_M=\mathbb Z_M\times\{0,1\},
\]
define, for \(n\in\mathbb Z_M\),
\[
u_n(r,0)=e(nr/M),\qquad
u_n(r,1)=e(\widetilde\sigma(n)r/M),
\]
and
\[
v_n(r,\varepsilon)=(-1)^\varepsilon u_n(r,\varepsilon).
\]

The cyclic character orthogonality relations give
\[
\langle u_n,u_m\rangle=\delta_{nm},\qquad
\langle v_n,v_m\rangle=\delta_{nm},\qquad
\langle u_n,v_m\rangle=0.
\]
Hence the \(2M\) functions
\[
\{u_n:n\in\mathbb Z_M\}\cup\{v_n:n\in\mathbb Z_M\}
\]
form a complete orthonormal basis of \(L^2(\Omega_M)\). Every value has modulus one. Therefore the evaluation matrix \(\mathsf H_M\) satisfies
\[
\mathsf H_M^*\mathsf H_M=2M I.
\]
Its entries are \(e(k/M)\) or \(-e(k/M)\), hence are \(2M\)-th roots of unity because \(M\) is odd. Thus \(\mathsf H_M\) is Butson-type complex Hadamard. In block form it is, up to the convention for the permutation matrix,
\[
\mathsf H_M=
\begin{pmatrix}
F_M&F_M\\
F_M P_{\widetilde\sigma}&-F_M P_{\widetilde\sigma}
\end{pmatrix}.
\]

Now fix an arbitrary permutation of all \(2M\) columns. Restrict that order to the distinguished columns
\[
u_1,\dots,u_N.
\]
They inherit a permutation \(\tau\) of \([N]\). Lewko's Lemma 2 supplies an arithmetic progression
\[
x_j=a+dj,\qquad j=1,\dots,m,
\]
whose \(\pi\)-ordered terms occur as a subsequence in the frequency ordering on either the \(0\)-layer or the \(1\)-layer.

Assign coefficient \(b_j\) to the corresponding selected \(u\)-column and coefficient zero to every other column. The full coefficient vector is real and has norm one. Interspersed zero-coefficient columns do not change partial sums.

On the chosen layer, the relevant partial sums at \(r\in\mathbb Z_M\) have absolute values
\[
\left|\sum_{j\le q}b_j e((a+d\pi(j))r/M)\right|
=
\left|\sum_{j\le q}b_j e(\pi(j)dr/M)\right|.
\]
Since the progression lies in \([N]\) and \(M>N\), its step satisfies \(1\le d<M\). Prime \(M\) therefore makes multiplication by \(d\) a permutation of \(\mathbb Z_M\). The finite-grid distribution of this maximal sum is exactly the sampled distribution of the original Fourier block.

At least \(\delta M/3\) points of the chosen layer consequently have maximal partial sum \(>2H\), hence \(>H\). Relative to the \(2M\) atoms of \(\Omega_M\), this is a proportion at least
\[
c=\delta/6.
\]
This proves the claim. The same argument works for every sufficiently large prime \(M\), so each fixed threshold is realized at infinitely many matrix orders.

## Interpretation

The counterexample is not caused by incompleteness of the finite orthonormal system or by the use of a nonatomic probability space. It persists in a finite-dimensional Hilbert space where the number of basis vectors equals the number of atoms and every matrix entry is a root of unity.

The construction is also more structured than an arbitrary completion. The Fourier matrix supplies exact cyclic orthogonality, while a single permutation in the lower Fourier block carries Lewko's two-ordering obstruction.

## Prior literature and originality boundary

Lewko's arXiv:2609.18491 proves the negative answer to Garsia's conjecture, the finite two-copy trigonometric construction, the combinatorial permutation lemma, and the finite Fourier divergence lemma used here. It also completes the infinite counterexample. None of those ingredients is claimed as new.

Bourgain's 1989 work is the classical source for universal rearrangement bounds for uniformly bounded orthogonal systems.

Dutkay--Han--Sun, arXiv:1103.4380, studies divergence and large Dirichlet kernels for structured scrambled Fourier systems with Hadamard-related features. Its stated result concerns specified scrambled orderings rather than a complete finite basis for which every column permutation admits a bad coefficient vector.

To the best of our knowledge, searches for Garsia/Kolmogorov rearrangement counterexamples on finite groups, finite atomic complete bases, complex Hadamard matrices, Butson matrices, and Fourier-Hadamard block constructions did not locate the statement above. The main residual originality risk is that the finite cyclic completion is short once Lewko's very recent construction is available, so an unindexed parallel or folklore observation remains plausible.

## Limitations

- No useful quantitative dependence of \(M_0(H)\) on \(H\) is obtained.
- No analogous result for real \(\{\pm1\}\)-Hadamard matrices is proved.
- The result does not strengthen the infinite Kolmogorov counterexample.
- No efficient construction of the witnessing permutation \(\widetilde\sigma\) or coefficients is asserted.
- No independent validation has been performed.

## References

1. M. Lewko, *On Kolmogorov's rearrangement problem and Garsia's conjecture*, arXiv:2609.18491v1 (2026).
2. J. Bourgain, *On Kolmogorov's rearrangement problem for orthogonal systems and Garsia's conjecture*, in *Geometric Aspects of Functional Analysis (1987--88)*, Lecture Notes in Mathematics 1376, Springer, 1989, 209--250. DOI: 10.1007/BFb0090057.
3. D. E. Dutkay, D. Han, and Q. Sun, *Divergence of the mock and scrambled Fourier series on fractal measures*, Trans. Amer. Math. Soc. 366 (2014), 2191--2208; arXiv:1103.4380.

# Fourier-null stratification of determinant-one matrices over prime-square rings

## Finding
Let \(p\ge3\) be any odd prime, \(R=\mathbb Z/p^2\mathbb Z\), and \(G=M_2(R)\) with its **additive** group law. Write \(S=\{X\in G:\det X=1\}\), and, for \(M\in G\), set
\[
F_p(M)=\sum_{X\in S}\exp\!\left(\frac{2\pi i}{p^2}\sum_{i,j=1}^2 m_{ij}x_{ij}\right).
\]
For a matrix over \(R\), let an overbar denote entrywise reduction modulo \(p\). Then the complete Fourier-nonvanishing criterion is
\[
\boxed{F_p(M)\ne0\ \Longleftrightarrow\ \bar M=0\quad\text{or}\quad [\det\bar M\ne0\ \text{and}\ \det\bar M\text{ is a square in }\mathbb F_p^\times].}
\]
In particular, every frequency whose reduction has rank one vanishes, and every invertible frequency of nonsquare determinant vanishes. The complex convolution operator \(T_p f=\mathbf1_S*f\) on \(\ell^2(G)\) therefore has precisely
\[
\boxed{\operatorname{rank}T_p=p^4\left(1+\frac{(p^2-1)(p^2-p)}2\right),\qquad \operatorname{nullity}T_p=p^8-\operatorname{rank}T_p.}
\]
Its kernel is exactly the span of the additive characters indexed by the complementary frequency classes. The rank fraction is
\[
\frac{\operatorname{rank}T_p}{p^8}=\frac1{p^4}+\frac12(1-p^{-1})(1-p^{-2}),
\]
which tends to \(1/2\) as \(p\) tends through the odd primes. At \(p=3\), the rank is \(2025\) in dimension \(6561\); at \(p=5\), it is \(150625\) in dimension \(390625\).

## Assumptions and scope
All determinants and matrix-entry pairings in the definition of \(F_p\) are computed modulo \(p^2\). The integer \(p\) is an odd prime; this statement does not cover modulus \(p^r\) for \(r\ne2\), residue fields of arbitrary local rings, or noncommutative convolution by \(S\) inside the multiplicative group \(\operatorname{SL}_2(R)\). The Fourier characters are the \(p^8\) characters of the additive group of four matrix entries. No normalization factor is inserted in \(F_p\); zero locations and operator rank are invariant under nonzero normalization.

## Proof
**1. Fibres of reduction.** Fix \(A\in\operatorname{SL}_2(\mathbb F_p)\), choose an arbitrary matrix lift \(B\in M_2(R)\), and write \(\det B=1+pc\) for \(c\in\mathbb F_p\). Every lift of \(A\) has the form \(X=B+pY\) for \(Y\in M_2(\mathbb F_p)\), and the determinant constraint is exactly
\[
\langle (\operatorname{adj} A)^T,Y\rangle=-c\quad\text{in }\mathbb F_p,
\]
where \(\langle U,V\rangle=\sum u_{ij}v_{ij}\). Because \(A\) is invertible, this is a nontrivial linear functional, so each determinant-one fibre has \(p^3\) members. Moreover, the Fourier sum over that fibre vanishes unless \(\bar M\) lies in the one-dimensional span of \((\operatorname{adj} A)^T\). When \(\bar M=t(\operatorname{adj} A)^T\), that fibre contributes
\[
p^3\exp\!\left(\frac{2\pi i}{p^2}\langle M,B\rangle\right)\exp\!\left(-\frac{2\pi i}{p}tc\right),
\]
a nonzero scalar of modulus \(p^3\). This follows by finite-group character orthogonality on the affine hyperplane above, independently of the chosen lift \(B\).

**2. Primitive frequencies.** Suppose \(\bar M\ne0\). A contributing residue \(A\) must satisfy \(\bar M=t(\operatorname{adj} A)^T\). The right-hand matrix is invertible, so rank-one \(\bar M\) cannot contribute. If \(\bar M\) is invertible, taking determinants gives \(\det\bar M=t^2\); hence no residue contributes when this determinant is a nonsquare. If it is a nonzero square, there are exactly two choices \(t=\pm\sqrt{\det\bar M}\), and each gives one \(A\), namely \(A=t(\bar M^{-1})^T\). The total \(F_p(M)\) is then \(p^3\) times the sum of two \(p^2\)-th roots of unity. Such a sum cannot vanish when \(p\) is odd, since the ratio of two odd-order roots of unity cannot equal \(-1\).

**3. Imprimitive frequencies.** If \(\bar M=0\), uniquely write \(M=pN\), with \(N\in M_2(\mathbb F_p)\). Every element of a determinant-one fibre has the same character value, giving
\[
F_p(pN)=p^3\sum_{A\in\operatorname{SL}_2(\mathbb F_p)}\exp\!\left(\frac{2\pi i}{p}\langle N,A\rangle\right).
\]
The inner sum is \(p(p^2-1)\) for \(N=0\); equals \(-p\) if \(\operatorname{rank}N=1\); and equals
\[
p\sum_{u\in\mathbb F_p^\times}\exp\!\left(\frac{2\pi i}{p}(u+\det(N)/u)\right)
\]
if \(N\) is invertible. These are the rank-two special-linear character-sum identities (and can be obtained directly by summing over the Borel subgroup; see Li--Hu, Theorem 2.4). The last sum is nonzero: it comprises exactly \(p-1\) primitive \(p\)-th roots of unity, counted with multiplicity. If it vanished, the cyclotomic polynomial \(1+z+\cdots+z^{p-1}\) would divide the corresponding integer-coefficient polynomial of degree at most \(p-1\), forcing every root to occur equally often, hence the total number of summands to be divisible by \(p\); but \(p-1\) is not divisible by \(p\). Consequently \(F_p(pN)\ne0\) in all cases.

**4. Rank and kernel.** The character basis of the finite abelian group \(G\) diagonalizes convolution by \(\mathbf1_S\), with eigenvalues \(F_p(\pm M)\) depending only on the Fourier-transform sign convention. The nonvanishing criterion is invariant under \(M\mapsto-M\). Of the \(p^4\) reductions \(\bar M\in M_2(\mathbb F_p)\), exactly one is zero. Of the \((p^2-1)(p^2-p)\) invertible reductions, exactly half have square determinant, because determinant is surjective onto \(\mathbb F_p^\times\) with equal-size fibres. Each reduction has \(p^4\) lifts to \(G\). Counting nonzero character eigenvalues yields both formulas and the kernel description. The asymptotic rank fraction follows immediately.

## Verification
The accompanying executable `check.py` uses integer arithmetic to enumerate determinant-one matrices, and tests Fourier vanishing through **exact cyclotomic coefficient congruences**, without floating-point thresholds: a polynomial of degree below \(p^2\) vanishes at a primitive \(p^2\)-th root if and only if its coefficients at exponents \(r,r+p,\ldots,r+(p-1)p\) are equal for each \(0\le r<p\). It exhaustively checks every one of the \(6561\) frequencies for \(p=3\), and checks a fixed-seed sample of \(400\) frequencies for \(p=5\). Observed output:

`SL2_PRIME_SQUARE_CYCLOTOMIC_OK p=3 matrices=648 frequencies=6561`

`SL2_PRIME_SQUARE_CYCLOTOMIC_OK p=5 matrices=15000 frequencies=400`

The proof establishes the theorem for all odd primes; finite tests do not replace its unbounded quantifiers.

## Relationship to prior work
Li and Hu (2011), Theorem 2.4, give the finite-field special-linear character sums used in step 3. Hu, He, Meng and Li (2018), Theorems 3.7--3.8, give analogous trace-character Gauss sums over residue rings for \(\operatorname{SL}_r\), expressed as hyper-Kloosterman sums. Their parameter is a scalar multiplying the trace, rather than an arbitrary four-entry additive frequency matrix. A full-rank frequency can partly be transformed to a determinant-constrained trace problem; the rank-one vanishing and the complete zero-frequency census require the tangent-fibre argument above. A related restricted-Fourier-frame calculation on determinant-one matrices over finite **fields** studies different operators and does not specify this prime-square additive convolution kernel. The new statement is the complete all-frequency support and the exact operator rank, not the established special-linear character-sum identities themselves.

## Limitations
The result does not describe the nonzero eigenvalues individually or their magnitudes. General formulas for Kloosterman sums over prime-power rings provide strong adjacent literature and could conceivably contain an equivalent support characterization under different terminology. No independent mathematical validation has been performed.

## References
- Y. Li and S. Hu, *Gauss sums over some matrix groups*, first publicly available 2011-05-23, arXiv:1105.4513v1, Theorem 2.4 (finite-field full-matrix character sums).
- S. Hu, G. He, Y. Meng and Y. Li, *Gauss sums of some matrix groups over \(\mathbb Z/n\mathbb Z\)*, arXiv:1805.09729, Theorems 3.7--3.8 (trace-character sums over residue rings).

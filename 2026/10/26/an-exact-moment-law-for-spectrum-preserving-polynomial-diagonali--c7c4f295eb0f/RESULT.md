# An exact moment law for spectrum-preserving polynomial diagonalization

## Finding

For a finite-dimensional operator with real spectrum, consider the least degree of a **real** polynomial that makes the operator diagonalizable without merging any two original spectral values. This degree is not determined only by Jordan-block sizes: it also depends on signed cancellations among the spectral nodes. We give its exact moment formula and a sharp maximal-degree family governed by Jacobi orthogonality.

**Theorem.** Let \(A\) be an arbitrary complex square matrix with distinct eigenvalues \(a_1<\cdots<a_s\) in \(\mathbb R\), where \(s\ge2\). Denote by \(q_j\ge1\) the largest Jordan-block size associated with \(a_j\), and set
\[
 F(x)=\prod_{j=1}^s(x-a_j)^{q_j-1},\qquad
 h_{ij}=\min\left\{k\ge0:\int_{a_i}^{a_j} x^k F(x)\,dx\ne0\right\},\qquad H=\max_{i<j}h_{ij}.
\]
Then the smallest degree of a polynomial \(p\in\mathbb R[x]\) satisfying both (i) \(p(A)\) is diagonalizable over \(\mathbb C\) and (ii) \(p(a_1),\ldots,p(a_s)\) are pairwise distinct, is exactly
\[
 \boxed{D(A)=1+\sum_{j=1}^s(q_j-1)+H.}
\]
Let \(E=\#\{j:1<j<s,\ q_j\ \text{even}\}\). Then
\[
 0\le H\le E,\qquad 1+\sum_j(q_j-1)\le D(A)\le1+\sum_j(q_j-1)+E\le\sum_j q_j-1.
\]
For every \(s\ge2\) the final upper bound is attained by the family with every \(q_j=2\), endpoints \(a_1=-1,a_s=1\), and interior nodes the zeros of the Jacobi polynomial \(P_{s-2}^{(1,1)}\). For this family \(D(A)=2s-1\), whereas the basic derivative-divisibility lower bound is merely \(s+1\).

## Assumptions and scope

All matrices are over \(\mathbb C\), all distinct spectral nodes are real, and only the *largest* Jordan-block size at each node enters the formula. The transformed operator need not be normal or self-adjoint: the conclusion is diagonalizability under similarity, not unitary diagonalizability. Polynomials with real coefficients suffice even though \(A\) may have arbitrary complex entries. The condition that the \(s\) transformed spectral values remain pairwise distinct rules out a trivial constant functional calculus. The empty interior-node set gives \(E=0\) when \(s=2\).

## Proof

**Step 1 (Jordan jets).** On a block \(J_q(a)=aI+N\), polynomial functional calculus gives
\[
 p(J_q(a))=p(a)I+\sum_{r=1}^{q-1}\frac{p^{(r)}(a)}{r!}N^r.
\]
If the nilpotent summand is nonzero, the matrix has one eigenvalue but is not diagonalizable. Thus \(p(A)\) is diagonalizable if and only if \(p^{(r)}(a_j)=0\) for every \(j\) and every \(1\le r<q_j\). Equivalently, \(F\) divides \(p'\), so for nonconstant \(p\), \(p'=FQ\) with \(Q\in\mathbb R[x]\). Put \(b=\deg F=\sum_j(q_j-1)\); then \(\deg p=1+b+\deg Q\).

**Step 2 (exact least degree).** For \(i<j\), the difference of spectral values is
\[
 p(a_j)-p(a_i)=\int_{a_i}^{a_j}F(x)Q(x)\,dx.
\]
For each pair this is a real linear functional \(L_{ij}\) of \(Q\). It vanishes identically on polynomials of degree below \(h_{ij}\), and is nonzero on the polynomial space of degree at most \(h_{ij}\). Consequently a polynomial with \(\deg Q<H\) necessarily merges a pair for which \(h_{ij}=H\). Conversely all finitely many \(L_{ij}\) are nonzero on the space \(\mathcal Q_H\) of polynomials of degree at most \(H\). The zero set of each is a proper hyperplane. Their finite union, together with the hyperplane of vanishing leading coefficient when \(H>0\), cannot fill \(\mathcal Q_H\). Hence some *real* polynomial \(Q\) of exact degree \(H\) makes every difference nonzero; its antiderivative of \(FQ\) proves the degree formula.

**Step 3 (finite moment bound).** Each real polynomial \(F\) changes sign inside \((a_i,a_j)\) only at nodes with odd exponent \(q_k-1\), equivalently with even \(q_k\). Let \(R_{ij}(x)\) be the product of \(x-a_k\) over those interior sign-change nodes lying in \((a_i,a_j)\). Then \(F(x)R_{ij}(x)\) has constant nonzero sign away from its finitely many roots throughout that interval, so \(\int_{a_i}^{a_j}F(x)R_{ij}(x)\,dx\ne0\). Since \(\deg R_{ij}\le E\), at least one moment of order at most \(E\) is nonzero. Therefore \(h_{ij}\le E\) for every pair. This also proves finiteness of every displayed minimum and the bounds on \(D(A)\).

**Step 4 (sharp all-order family).** Fix \(s\ge2\) and take \(q_j=2\) for all nodes. Let the endpoints be \(-1,1\), and let the other \(s-2\) nodes be the simple zeros of the Jacobi polynomial \(P_{s-2}^{(1,1)}\). Then, up to a nonzero real factor,
\[
 F(x)=(x^2-1)P_{s-2}^{(1,1)}(x).
\]
Jacobi orthogonality with weight \((1-x)(1+x)=1-x^2\) gives
\[
 \int_{-1}^{1}x^kF(x)\,dx=0\quad(0\le k\le s-3),
 \qquad \int_{-1}^{1}x^{s-2}F(x)\,dx\ne0.
\]
The final nonvanishing follows because the monic degree-\(s-2\) polynomial is a nonzero multiple of \(P_{s-2}^{(1,1)}\) plus a lower-degree polynomial: orthogonality reduces the integral to its nonzero squared Jacobi norm, up to sign. Thus \(h_{1s}=s-2\), while the general bound supplies \(H\le E=s-2\), proving \(H=s-2\) and \(D(A)=s+1+(s-2)=2s-1\). When \(s=2\), the orthogonality range is empty and the nonzero constant moment gives the same conclusion.

For a concrete three-node example, use blocks \(J_2(-1)\oplus J_2(0)\oplus J_2(1)\). Here \(F(x)=x^3-x\), the full-span zeroth moment vanishes by oddness, and its first moment does not. Hence the least degree is five. The polynomial
\[
 p(x)=\frac{x^5}{5}+\frac{x^4}{4}-\frac{x^3}{3}-\frac{x^2}{2}
\]
works: \(p'=F(x)(x+1)\), and \(p(-1)=-7/60\), \(p(0)=0\), \(p(1)=-23/60\), which are distinct. Every degree-four diagonalizing polynomial has derivative a scalar multiple of \(F\) and merges the two endpoint eigenvalues.

## Verification

Symbolic rational-arithmetic checks were executed for node/size samples \((-1,0,1);(2,2,2)\), \((-2,-1,0,1);(2,3,2,4)\), \((-1,1);(3,2)\), \((-2,0,2);(1,2,1)\), and four distinct semisimple nodes. For each sample, the moment lags, degree bound, constructed separating polynomial, and all derivative constraints were recomputed exactly. The Jacobi endpoint moments were verified exactly for \(2\le s\le7\). These finite computations are diagnostic, not an infinite proof; Steps 1–4 above establish the general conclusion analytically.

The construction is independently reproducible by expanding \(F\), integrating \(x^kF\) over each pair of rational nodes, finding \(H\), selecting a real polynomial \(Q\) of degree \(H\) outside the finitely many indicated hyperplanes, then taking \(p(x)=\int_0^xF(t)Q(t)\,dt\).

## Relationship to prior work

Chang's 2025 analysis of polynomially transformed matrices treats a *given* function and counts Jordan structures satisfying diagonalizability constraints; Section 4 uses vanishing derivatives at spectral nodes. The present theorem instead optimizes the polynomial *degree* for an already-fixed operator, requires preservation of every distinct spectral value, identifies the exact signed-moment obstruction, and proves a sharp Jacobi-node extremal family. The author's earlier 2024 projector/nilpotent functional-calculus paper supplies general spectral-decomposition context but not this degree optimization. Classical Hermite interpolation gives an upper degree \(\sum_jq_j-1\) for freely prescribed distinct values; it does not by itself identify the input-specific least degree or the cancellation parameter \(H\). These distinctions are implication-level, not merely differences in terminology.

## Limitations

The formula assumes a real spectrum, and no complex-node analogue or prescribed target values are claimed. It characterizes similarity-diagonalizability, not Hermitian, normal, or unitary diagonalization. The Jacobi construction certifies a sharp upper envelope but does not classify every extremal node configuration. Novelty is assessed against the inspected sources and searched records, not guaranteed against unindexed historical literature. Exact computations in finite examples support, but do not establish, the general theorem.

## References

1. S.-Y. Chang, *Existence and Enumeration of Polynomially Transformed Matrices under Spectral and Nilpotent Constraints*, arXiv:2510.16901v1 (first submitted 2025-10-19), especially Sections 2 and 4.
2. S.-Y. Chang, *Operator Characterization via Projectors and Nilpotents*, arXiv:2411.11883v1 (first submitted 2024-11-04), especially Section 2.
3. Classical Hermite interpolation and Jacobi orthogonality (used only in the standard forms explicitly stated and proved up to the conventional orthogonality property above).

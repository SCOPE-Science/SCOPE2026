# Exact annihilating-pair census for finite upper-niltriangular matrix algebras

## Finding
For any finite field \(\mathbb F_q\) and integer \(n\ge1\), let \(J_n\) be the algebra of strictly upper-triangular \(n\times n\) matrices and set
\[
Z_n(q)=\#\{(A,B)\in J_n^2:AB=0\}.
\]
Define integer polynomials recursively by \(C_{1,0}(q)=1\), \(C_{k,r}=0\) for invalid indices, and for \(k\ge2\), \(0\le r\le k-1\),
\[
C_{k,r}(q)=q^{k-1}C_{k-1,r}(q)+q^{k-r}(q^{k-1}-q^{r-1})C_{k-1,r-1}(q),
\]
with the second summand interpreted as zero at \(r=0\). Then
\[
\boxed{Z_n(q)=\sum_{r=0}^{n-1}C_{n,r}(q)}.
\]
In particular,
\[
Z_1(q)=1,\quad Z_2(q)=q^2,\quad Z_3(q)=q^4(2q-1),\quad
Z_4(q)=q^7(q^3+3q^2-4q+1).
\]
The associated radical-ring brace has operations \(A+B\) and \(A\circ B=A+B+AB\); hence the exact probability that these operations agree on an independent uniform ordered pair is
\[
\boxed{\Pr(A\circ B=A+B)=Z_n(q)/q^{n(n-1)}}.
\]

## Assumptions and scope
There is no restriction on the characteristic. Matrices are strictly upper triangular and sampled independently and uniformly over the entire additive space \(J_n\), rather than the unipotent group or the full upper-triangular algebra. The condition is one-sided \(AB=0\), not simultaneous \(AB=BA=0\). The integer \(n=1\) is included, with the zero algebra and one ordered pair.

## Proof
Write any \(k\times k\) strictly upper-triangular matrix as
\[
A_k=\begin{pmatrix}A_{k-1}&v\\0&0\end{pmatrix},\qquad
B_k=\begin{pmatrix}B_{k-1}&b\\0&0\end{pmatrix},
\]
where \(v,b\in\mathbb F_q^{k-1}\). Multiplication gives \(A_kB_k=0\) if and only if \(A_{k-1}B_{k-1}=0\) and \(A_{k-1}b=0\). The former condition is independent of \(v\).

Let \(C_{k,r}\) count valid ordered pairs with \(\operatorname{rank}(A_k)=r\). Fix a valid pair of size \(k-1\) with \(\operatorname{rank}(A_{k-1})=s\). There are exactly \(q^{k-1-s}\) valid choices of \(b\), by rank-nullity. The vector \(v\) lies in the column space of \(A_{k-1}\) for exactly \(q^s\) choices, all preserving rank \(s\); the other \(q^{k-1}-q^s\) choices increase rank by exactly one. Thus the rank-preserving contribution is \(q^{k-1-s}q^s C_{k-1,s}=q^{k-1}C_{k-1,s}\), and the rank-increasing contribution from \(s=r-1\) is
\[
q^{k-r}(q^{k-1}-q^{r-1})C_{k-1,r-1}.
\]
These two mutually exclusive, exhaustive cases establish the recurrence, with initial condition \(C_{1,0}=1\). Summing over all possible ranks gives \(Z_n\). Every strictly upper-triangular algebra is nilpotent and hence a Jacobson radical ring; its circle operation defines a group. The relation \(A\circ B=A+B\) is literally equivalent to \(AB=0\); since \(|J_n|=q^{n(n-1)/2}\), normalization by \(|J_n|^2\) proves the probability formula. No unproved limiting assertion is used.

## Verification
The standalone `verify.py` evaluates the recurrence independently of the following direct-definition loop: over prime fields, it enumerates every \(A,B\in J_n\), multiplies their matrices and counts exact zero products. Recorded checks over \((q,n)=(2,2),(3,2),(2,3),(3,3),(2,4)\) yielded respectively \(4,9,48,405,1664\) in both calculations, and the script returned `VERIFY_OK`. Enumerations only verify the listed finite cases; the preceding rank-stratified argument proves the general statement for every prime power.

## Relationship to prior work
The probability is motivated by the recent study of relative commuting probabilities for finite skew braces by Mondal, Shumyatsky, Trombetti and Yadav (first public September 14, 2026). The present statistic tests equality of the two operations on an ordered pair in the brace arising from a nilpotent matrix algebra. It is not presented as identical to every relative commuting statistic defined there. Huang (2021) enumerates mutually annihilating pairs of general matrices under the different simultaneous constraints \(AB=BA=0\). Ekhad and Zeilberger (1995) enumerate triangular matrices satisfying \(A^2=0\), a diagonal single-matrix constraint. Neither condition directly determines the one-sided ordered-pair counts above. No complete historical-priority claim is made.

## Limitations
Only strictly upper-triangular matrix algebras are treated. The recurrence is a finite exact algorithm, not a closed product, and it does not enumerate individual isomorphism classes of braces, common annihilators, or pairs with \(AB=BA=0\). The full text of the directly motivating 2026 skew-brace paper and that of the closest older annihilating-pair paper were not available for comprehensive comparison; unexpected prior coverage remains possible. Computations cover only prime fields and small sizes.

## References
1. S. Mondal, P. Shumyatsky, M. Trombetti, M. K. Yadav, *Relative commuting probability and BFC-type results for finite skew braces*, arXiv:2609.16269 (first posted 2026-09-14), https://arxiv.org/abs/2609.16269.
2. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first posted 2021-10-29), https://arxiv.org/abs/2110.15566.
3. S. B. Ekhad and D. Zeilberger, *An Explicit Formula for the Number of Solutions of X²=0 in Triangular Matrices over a Finite Field*, arXiv:math/9512224 (1995), https://arxiv.org/abs/math/9512224.

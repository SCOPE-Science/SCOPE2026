# Complete rank-weight hierarchy of Berhuy–Molina Example 4.3
## Finding

For the explicit \(M\)-cyclic code \(C\subset \mathbb F_{3^{10}}^9\) in Berhuy–Molina Example 4.3, with
\[
f=(x^2+1)^2(x+1)^3(x-1)^2
\]
and generator
\[
g=(x-i)(x+1)^2(x-1)^2,\qquad i^2=-1,
\]
the complete generalized rank-weight hierarchy over \(\mathbb F_3\) is
\[
(M_1(C),M_2(C),M_3(C),M_4(C))=(1,2,3,5).
\]
Thus the rank-support sizes realized by optimal subcodes skip \(4\): the successive minima are \(1,2,3,5\).

## Assumptions and scope

The code is exactly the length-\(9\), dimension-\(4\) code in Example 4.3 of the cited paper. Since \(2\mid10\), the field \(\mathbb F_{3^{10}}\) contains the unique subfield \(\mathbb F_9=\mathbb F_3(i)\) with \(i^2=-1\). All coefficients needed below lie in that subfield.

For an \(r\)-dimensional \(\mathbb F_{3^{10}}\)-subcode \(D\), its generalized rank weight is the minimum possible \(\mathbb F_3\)-dimension of its rank support. In particular, every \(r\)-dimensional subcode has rank-support dimension at least \(r\).

## Proof

Write
\[
f_1=x^2+1,\qquad f_2=x+1,\qquad f_3=x-1.
\]
The primary powers \(f_1^2,f_2^3,f_3^2\) are pairwise coprime over \(\mathbb F_3\). The primary decomposition used in Theorem 4.1 of Berhuy–Molina splits the code, up to a rank-metric isometry defined over \(\mathbb F_3\), into two active components and one zero component. The active components are
\[
C_1\subset \mathbb F_{3^{10}}^4,\quad g_1=x-i,\quad \dim C_1=3,
\]
and
\[
C_2\subset \mathbb F_{3^{10}}^3,\quad g_2=(x+1)^2,\quad \dim C_2=1.
\]
The \(f_3^2\)-component is zero because \(g\) contains the full factor \((x-1)^2\).

For \(C_1\), the coefficient vectors of \(g_1,xg_1,x^2g_1\) give
\[
G_1=
\begin{pmatrix}
-i&1&0&0\\
0&-i&1&0\\
0&0&-i&1
\end{pmatrix}.
\]
The product \((x+i)(x-i)=x^2+1\) gives the codeword
\[
(1,0,1,0),
\]
so \(M_1(C_1)=1\). Its shift \((0,1,0,1)\) is independent of it, and the two vectors are defined over \(\mathbb F_3\); their span therefore has rank-support dimension \(2\). Hence \(M_2(C_1)=2\), using the universal lower bound \(M_2\ge2\).

To compute the last component weight, expand the rows of \(G_1\) in the \(\mathbb F_3\)-basis beginning with \(1,i\). Their coefficient rows include all four coordinate unit vectors: the real parts supply the second, third, and fourth coordinate directions, while the \(i\)-parts supply the first, second, and third. Consequently
\[
\operatorname{Rsupp}(C_1)=\mathbb F_3^4,
\]
and therefore \(M_3(C_1)=4\). Thus
\[
(M_1(C_1),M_2(C_1),M_3(C_1))=(1,2,4).
\]

For \(C_2\),
\[
(x+1)^2=x^2+2x+1
\]
has coefficient vector \((1,2,1)\in\mathbb F_3^3\). Since \(C_2\) is one-dimensional,
\[
M_1(C_2)=1.
\]

For a direct sum of rank-metric components over disjoint primary blocks, the generalized rank weights satisfy the convolution formula proved in Berhuy–Molina Theorem 4.1:
\[
M_r(C)=\min_{r_1+r_2=r}\bigl(M_{r_1}(C_1)+M_{r_2}(C_2)\bigr),
\]
with \(M_0=0\). Substituting the two component hierarchies gives
\[
M_1=1,\qquad M_2=2,\qquad M_3=3,\qquad M_4=5.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library. It implements \(\mathbb F_9=\mathbb F_3(i)\) with \(i^2=-1\), verifies the factorization \(x^2+1=(x-i)(x+i)\), reconstructs the two active primary generator matrices, and checks their dimensions.

It verifies the explicit rank-one and rank-two subcodes of \(C_1\), expands \(G_1\) over \(\mathbb F_3\) to confirm that its full rank support is \(\mathbb F_3^4\), verifies the rank-one generator of \(C_2\), and then evaluates the exact primary-component convolution. Successful replay prints `VERIFY_OK`.

The verifier checks the finite algebra used in the specialization; the general primary-decomposition theorem itself is taken from the cited paper.

## Relationship to prior work

Berhuy and Molina introduce this code in Example 4.3 as a benchmark for their new primary-decomposition bound. There they state
\[
M_1(C)\le2,\qquad M_4(C)\le7.
\]
Their later first-weight criterion implies \(M_1(C)=1\), and Example 4.19 explicitly sharpens the last weight to
\[
M_4(C)=5.
\]
The paper does not state the two middle weights of Example 4.3. The calculation above completes the hierarchy by proving
\[
M_2(C)=2,\qquad M_3(C)=3.
\]

The earlier work of Ducoat and Oggier develops rank-weight results for polynomial codes under a squarefree-polynomial hypothesis. The repeated-primary polynomial in this example lies outside that squarefree setup, so that paper does not supply this numerical four-weight hierarchy.

Targeted searches using the exact example, the generator polynomial, the sequence \((1,2,3,5)\), and the middle-weight notation did not locate an indexed source stating the completed hierarchy.

## Limitations

This result concerns the single explicit code of Example 4.3. It does not classify all \(M\)-cyclic codes with the same length and dimension, nor does it improve the general theorems of Berhuy–Molina. The endpoint values \(M_1=1\) and \(M_4=5\) are already consequences of results in that paper; the new finite content is the exact determination of the two missing middle weights and hence the complete hierarchy.

An unindexed note could have carried out the same specialization. The literature search cannot rule out such a source absolutely.

## References

1. G. Berhuy and J. Molina, *On the rank weight hierarchy of M-codes*, arXiv:2507.00609v1, first public version 2025-07-01; Advances in Mathematics of Communications 24 (2026), 208–236, DOI 10.3934/amc.2026035.
2. J. Ducoat and F. Oggier, *Rank weight hierarchy of some classes of polynomial codes*, Designs, Codes and Cryptography 91 (2023), 1627–1644, DOI 10.1007/s10623-022-01181-6.

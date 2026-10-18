# Barba-tight determinants force parallelepipedal minimal enlargements of real \(\ell_1^n\)

## Finding
Let \(n\ge5\) be odd and assume that an \(n\times n\) sign matrix attains the Barba bound
\[
 d_n=\sqrt{2n-1}(n-1)^{(n-1)/2}.
\]
Write \(q=\sqrt{2n-1}\). The Barba equality theorem implies that \(q\) is an odd positive integer. For any lower Auerbach basis \(v_1,\ldots,v_n\) of the real Banach space \(\ell_1^n\), and any distinct indices \(i,j\), one can independently change the signs of the selected vectors so that the induced planar norm is, for every \((a,b)\in\mathbb R^2\),
\[
 \boxed{\|a v_i+b v_j\|_1=\frac12|a+b|+\frac{|(q-1)a-(q+1)b|+|(q+1)a-(q-1)b|}{4q}.}
\]
Its polar unit ball is a three-generator centrally symmetric hexagon with absolute generator-pair determinants in the ratio \(q:q:1\). Since \(q\ge3\), neither that polar ball nor the original planar unit ball is affinely regular. Consequently **every** minimal-volume sufficient enlargement (MVSE) of \(\ell_1^n\) is a parallelepiped.

The condition holds at \(n=5\) and throughout the infinite family \(n=2p^2+2p+1\) for primes \(p\equiv3\pmod4\), via known Barba-optimal sign matrices. For example, the first values from this family are \(n=25,113,\ldots\); dimension \(5\) is a separate direct example. This is a classification under a precise extremal-determinant hypothesis, **not** a statement about all odd dimensions.

## Assumptions and scope
A sufficient enlargement for an \(n\)-dimensional normed space \(X\) is an origin-symmetric convex body \(K\subset X\) such that every isometric embedding of \(X\) into any Banach space \(Y\) admits a projection \(P:Y\to X\) with \(P(B_Y)\subseteq K\). An MVSE has the least volume among such bodies. A lower Auerbach basis minimizes the volume of its associated circumscribed basis parallelepiped; its biorthogonal functionals form an upper Auerbach basis, whose generating parallelepiped has maximal volume inside the dual unit cube [1, Proposition 2.4]. A planar unit ball is *affinely regular* when it is linearly equivalent to a Euclidean regular hexagon.

The hypothesis is the **attainment** of the stated Barba determinant upper bound, not merely existence of a large determinant or the integrality of \(q\). All spaces, matrices, and coefficients are real. Signs of the two chosen basis vectors may be changed without changing their underlying span.

## Proof
**1. Rigidity of cube determinant maximizers.** Let \(M\) maximize the absolute determinant on the cube of all real \(n\times n\) matrices with entries in \([-1,1]\). By determinant multilinearity, a sign matrix can attain this maximum; by hypothesis it is \(d_n\). If \(M\) had an entry strictly between \(-1\) and \(1\), maximizing an affine absolute-value function in that entry would force its cofactor to vanish. One may successively move every other nonvertex entry to either endpoint while retaining maximal absolute determinant. The chosen fractional entry remains interior and has zero cofactor at each stage. At the end it can be moved to an endpoint, producing a maximal-determinant **sign** matrix with a zero cofactor. This is impossible: for each Barba-optimal sign matrix, the Gram calculation below gives an inverse with no zero entry, and a cofactor is its corresponding inverse entry times the nonzero determinant. Hence every upper Auerbach basis of \(\ell_\infty^n\) consists entirely of sign vectors.

**2. Simultaneous Gram normalization and inverse.** The equality characterization of the Barba bound [2, Theorem 12] says that the row Gram matrix of any maximal sign matrix, after signed row permutation, is \((n-1)I+J\), where \(J\) is the all-ones matrix. Applying the same result to the transpose, and noting that column sign changes do not alter the row Gram matrix (and row sign changes do not alter the column Gram matrix), gives a sign matrix \(A\) satisfying
\[
 AA^{\mathsf T}=A^{\mathsf T}A=(n-1)I+J.
\]
Since \(q^2=2n-1\), the eigenspace of either Gram matrix with eigenvalue \(q^2\) is the line spanned by the all-ones vector \(\mathbf 1\). Thus \(A\mathbf1=\pm q\mathbf1\) and \(A^{\mathsf T}\mathbf1=\pm q\mathbf1\); their signs agree upon summing all entries. Negating \(A\) if necessary gives
\[
 A\mathbf1=A^{\mathsf T}\mathbf1=q\mathbf1,
 \qquad A^{-\mathsf T}=\frac{A-q^{-1}J}{n-1}.
\]
The inverse identity follows by multiplying by \(A^{\mathsf T}\). Every entry of this inverse is \((\pm1-q^{-1})/(n-1)\ne0\), as used in step 1. By [1, Proposition 2.4], the columns of \(A^{-\mathsf T}\) (up to ambient signed coordinate permutations and individual column signs) represent **every** lower Auerbach basis of \(\ell_1^n\).

**3. Exact pair-incidence counts.** Fix two distinct columns of \(A\). Because their sums both equal \(q\) and their scalar product is \(1\), their respective joint sign counts satisfy
\[
 N_{+-}=N_{-+}=\frac{n-1}{4},\quad
 N_{++}=\frac{n+1+2q}{4},\quad
 N_{--}=\frac{n+1-2q}{4}.
\]
An entry \(+1\) of \(A\) maps in \(A^{-\mathsf T}\) to \(u=(q-1)/(q(n-1))\), and an entry \(-1\) maps to \(-w\), where \(w=(q+1)/(q(n-1))\). Summing the absolute values of \(a v_i+b v_j\) in the four sign classes gives
\[
 (N_{++}u+N_{--}w)|a+b| + \frac{n-1}{4}\bigl(|ua-wb|+|wa-ub|\bigr).
\]
The first coefficient equals \(1/2\); simplifying the other two establishes the asserted norm formula, for all real \(a,b\) without exceptional cases.

**4. Hexagon obstruction and MVSE conclusion.** The planar norm is the sum of absolute values of the three nonparallel linear functionals represented by
\[
 g_0=(1/2,1/2),\quad
 g_1=((q-1)/(4q),-(q+1)/(4q)),\quad
 g_2=(-(q+1)/(4q),(q-1)/(4q)).
\]
Thus its polar unit ball is the zonotope \(\sum_{r=0}^{2}[-g_r,g_r]\). Its generator-pair determinant magnitudes are
\[
 |\det(g_0,g_1)|=|\det(g_0,g_2)|=\frac14,
 \qquad |\det(g_1,g_2)|=\frac1{4q}.
\]
A centrally symmetric hexagon linearly equivalent to a regular hexagon has equal generator-pair determinant magnitudes (the equality is preserved by linear coordinate changes, which scale all three by the same determinant). As \(q\ge3\), this condition fails. Polarity preserves affine regularity for origin-centered hexagons. By the necessary-and-sufficient criterion of [1, Theorem 3.1], no non-parallelepipedal MVSE exists.

**5. Infinite family.** In dimension \(5\), \(A=J-2I\) has \(A^{\mathsf T}A=4I+J\), so the Barba bound is attained. For every prime \(p\equiv3\pmod4\), the Brouwer--Whiteman construction as set out in [2, Theorem 16] gives a sign matrix of order \(n=2p^2+2p+1\) with the required Gram matrix. Infinitely many such primes exist; thus there are infinitely many odd dimensions (distinct from the Hadamard multiples-of-four family) in which every MVSE is parallelepipedal.

## Verification
The proof uses the exact Barba equality theorem, Ostrovskii's exact MVSE criterion, and finite-dimensional linear algebra. The included standalone Python standard-library checker recomputes the full dimension-five example with rational arithmetic, the analytic coefficient identities and the generator determinant ratios for representative odd \(q\). These finite checks corroborate algebra only; they do not replace the quantified proof, nor certify sign-matrix existence in arbitrary dimensions.

## Relationship to prior work
Ostrovskii [1, Theorem 3.1] characterized non-parallelepipedal MVSEs via a regular-hexagonal span of two lower Auerbach vectors. In [1, §4.1] the author explicitly discusses the determination of dimensions for \(\ell_1^n\), proves only the Hadamard-order parallelepiped case and the three-dimensional contrasting example. Independently, the determinant survey [2, Corollary 10, Theorem 12, Theorem 16] supplies Barba's bound, its rigid equality Gram matrix, and infinitely many orders attaining it, but does not discuss lower Auerbach two-vector norm profiles or sufficient enlargements. The new implication combines these components through all-maximizer entry rigidity, the inverse calculation, and the three-generator obstruction.

## Limitations
The result is conditional on Barba-bound attainment. It does not classify the dimensions where no such matrix exists, does not assert uniqueness of each circumscribed parallelepiped, and does not exclude regular-hexagonal subspaces spanned by arbitrary (rather than lower-Auerbach) pairs. Its originality comparison relies on available literature and database search; an unknown earlier combination of the two cited theorems remains a bibliographic risk. No independent validation has been performed.

## References
[1] M. I. Ostrovskii, *Auerbach bases and minimal volume sufficient enlargements*, arXiv:1103.0997v1 (first posted 2011-03-05), especially Proposition 2.4, Theorem 3.1, and §4.1. https://arxiv.org/html/1103.0997v1

[2] P. Browne, R. Egan, F. Hegarty, P. Ó Catháin, *A Survey of the Hadamard Maximal Determinant Problem*, arXiv:2104.06756v4 (first posted 2021-04-14), especially Corollary 10, Theorem 12, and Theorem 16. https://arxiv.org/html/2104.06756v4

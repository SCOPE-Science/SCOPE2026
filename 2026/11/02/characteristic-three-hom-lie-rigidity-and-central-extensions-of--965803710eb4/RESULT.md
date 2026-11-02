# Characteristic-three Hom–Lie rigidity and central extensions of type A2

## Finding

Let \(k\) be **any field of characteristic \(3\)**. Put \(L=\mathfrak{sl}_3(k)\), \(Z=kI_3\), and \(P=L/Z\). A Hom–Lie structure on a Lie algebra \(G\) is a \(k\)-linear map \(\varphi:G\to G\) satisfying
\[
[[x,y],\varphi(z)]+[[z,x],\varphi(y)]+[[y,z],\varphi(x)]=0\qquad(x,y,z\in G).
\]
Then the *complete* Hom–Lie spaces are
\[
\boxed{\operatorname{HomLie}(P)=k\operatorname{id}_P,\qquad
\operatorname{HomLie}(L)=k\operatorname{id}_L\oplus\operatorname{Hom}_k(L,Z).}
\]
In particular their dimensions are \(1\) and \(9\), respectively. Every Hom–Lie structure on \(L\) is uniquely of the form \(\lambda\operatorname{id}_L+f\), with \(\lambda\in k\) and \(f:L\to Z\) linear. For \(k=\mathbb F_q\), \(q=3^a\) with \(a\ge1\), the exact numbers of structures are \(q\) for \(P\) and \(q^9\) for \(L\).

Unlike Hom–Lie spaces in general, \(\operatorname{HomLie}(L)\) is closed under ordinary composition. On choosing any vector-space complement \(L=Z\oplus W\), \(\dim W=7\), its associative algebra is
\[
\left\{\begin{pmatrix}\alpha&\ell\\0&\beta I_W\end{pmatrix}:
\alpha,\beta\in k,\ \ell\in\operatorname{Hom}_k(W,Z)\right\}.
\]
Its radical consists of the seven-dimensional square-zero upper-right block; its semisimple quotient is \(k\times k\). Over \(\mathbb F_q\) this algebra has exactly \((q-1)^2q^7\) units and \(2q^7+2\) idempotents.

## Assumptions and scope

The characteristic is exactly \(3\); no algebraic-closure assumption is used. Here \(I_3\) is the identity matrix and \(P\) denotes the seven-dimensional central quotient, not a group. The definition does **not** require \(\varphi\) to preserve brackets, be invertible, or be multiplicative. The Lie bracket is the ordinary matrix commutator. As usual, \(E_{ij}\) denotes the matrix unit with its only nonzero entry equal to \(1\) in row \(i\), column \(j\). No analogous assertion for other ranks or characteristics is claimed.

## Proof

**1. The center, perfection, and lower bound.** The center of \(L\) is \(kI_3\): a matrix commuting with all off-diagonal matrix units must be scalar, and \(\operatorname{tr}(I_3)=0\) in characteristic \(3\). Thus \(\dim L=8\), \(\dim Z=1\), and \(\dim P=7\). The commutators \([E_{ij},E_{jk}]=E_{ik}\) for pairwise distinct indices and \([E_{ij},E_{ji}]=E_{ii}-E_{jj}\) show \([L,L]=L\). The Jacobi identity proves that every \(\lambda\operatorname{id}_L\) is Hom–Lie; any map with image contained in \(Z\) is Hom–Lie because the outer bracket always vanishes. These subspaces intersect trivially, giving a nine-dimensional lower bound on \(\operatorname{HomLie}(L)\).

**2. Hom–Lie maps descend.** For \(\varphi\in\operatorname{HomLie}(L)\) and \(z\in Z\), the defining identity at \((x,y,z)\) reduces to \([[x,y],\varphi(z)]=0\). Since \([L,L]=L\), one has \(\varphi(z)\in Z\). Consequently \(\varphi\) induces a Hom–Lie map on \(P\). If every Hom–Lie map on \(P\) is scalar, then \(\varphi-\lambda\operatorname{id}_L\) takes values in \(Z\). It remains to prove rigidity of \(P\).

**3. A finite, exact rank certificate for the quotient.** Choose the ordered quotient basis
\[
\mathcal B=(\bar E_{12},\bar E_{13},\bar E_{21},\bar E_{23},\bar E_{31},\bar E_{32},\bar H),
\qquad H=E_{11}-E_{22}.
\]
In \(P\), the class of \(E_{22}-E_{33}\) equals \(\bar H\). For a traceless matrix \(A\), its quotient coordinates in this basis are
\[
(A_{12},A_{13},A_{21},A_{23},A_{31},A_{32},A_{11}-A_{33}).
\]
This is well-defined since adding a scalar matrix leaves the last difference unchanged. Let \(c_{ij}^{s}\in\mathbb F_3\) be the structure constants \([b_i,b_j]=\sum_s c_{ij}^{s}b_s\), where indices run from \(0\) to \(6\). Write \(\varphi(b_k)=\sum_r v_{rk}b_r\); the unknown \(v_{rk}\) has flattened column index \(7k+r\).

For every \(0\le i<j<k\le6\) and \(0\le t\le6\), the \(t\)-component of the Hom–Jacobi identity is the linear equation
\[
\sum_{r=0}^6\left(\sum_{s=0}^6 c_{ij}^{s}c_{sr}^{t}\right)v_{rk}
+\sum_{r=0}^6\left(\sum_{s=0}^6 c_{ki}^{s}c_{sr}^{t}\right)v_{rj}
+\sum_{r=0}^6\left(\sum_{s=0}^6 c_{jk}^{s}c_{sr}^{t}\right)v_{ri}=0.
\]
There are \(\binom73\cdot7=245\) listed equations. Their rows are ordered lexicographically by \((i,j,k)\), then by \(t\). Since the identity is Hom–Lie, subtract \(v_{00}\operatorname{id}_P\) to impose \(v_{00}=0\). Delete flattened column \(0\), leaving \(48\) unknowns. In the resulting \(245\times48\) matrix over \(\mathbb F_3\), the \(48\times48\) submatrix at the following *zero-based* row indices has determinant \(1\) in \(\mathbb F_3\):

```text
0,1,2,3,4,5,6,8,10,15,16,17,20,35,36,37,38,39,40,41,42,43,44,45,46,47,
48,49,50,51,52,53,54,56,57,58,59,60,61,62,63,64,68,71,78,106,112,178
```

This is an explicit finite-field rank certificate: all of its entries follow from the displayed \(3\times3\) matrix units, and `verify.py` reconstructs and evaluates the determinant by exact elimination. A homogeneous system with this invertible minor and \(v_{00}=0\) has only the zero solution. Hence \(\operatorname{HomLie}(P)=k\operatorname{id}_P\). Since this determinant is \(1\) over the prime field, the assertion holds after extension to **every** characteristic-three field.

**4. Lift back to \(L\).** Step 2 and quotient rigidity force \(\varphi=\lambda\operatorname{id}_L+f\), with \(f(L)\subseteq Z\). Step 1 established the converse. The dimensions and finite-field counts follow immediately.

**5. Composition algebra.** In a decomposition \(L=Z\oplus W\), the restriction of \(\lambda\operatorname{id}_L+f\) has block form \(\bigl(\begin{smallmatrix}\lambda+f|_Z&f|_W\\0&\lambda I_W\end{smallmatrix}\bigr)\). The two diagonal scalars can be chosen independently. Block multiplication proves closure under composition. The off-diagonal subspace is a square-zero ideal, and the quotient is \(k\times k\), making it the radical. A block matrix is invertible precisely when both scalars are nonzero. An idempotent has diagonal values in \(\{0,1\}\); the upper-right block is arbitrary precisely when these scalars differ and must otherwise vanish. This yields the stated unit and idempotent counts.

## Verification

Two self-contained Python programs using only the standard library independently reconstruct the Lie brackets and Hom–Jacobi matrices. `verify.py` checks the displayed determinant, establishes quotient rank \(48\) and full-algebra rank \(55\), and directly verifies the scalar and central-map lower bounds. `crosscheck.py` uses a different matrix-unit ordering, a different diagonal basis, and an independent incremental rank algorithm; it obtains Hom–Lie dimensions \(1\) and \(9\). Both programs terminate with `VERIFY_OK`; recorded outputs are included. The central-lift proof and composition description are symbolic; they do not depend on finite-field sampling. The determinant certificate, with its full reconstruction algorithm, supplies the finite arithmetic needed in the only computational proof step.

## Relationship to prior work

Sun, Zhang, and Zhu, *Classification of Hom–Lie structures on finite-dimensional simple Lie algebras* (first posted 2026-10-18, arXiv:2610.25056v1), determine the subject for algebraically closed fields of characteristic different from \(2\) and \(3\). Their Theorem 1.1 and Section 3.2 do not cover the present characteristic-three central quotient. Makhlouf and Zusmanovich, *Hom–Lie structures on Kac–Moody algebras* (arXiv:1805.00187, Section 2), explicitly assume characteristic different from \(2,3\). Xie, Jin, and Liu, *Hom-structures on semi-simple Lie algebras* (2015), work over characteristic-zero algebraically closed fields. Therefore none of these statements directly implies the theorem in characteristic \(3\). The underlying defining identity and the general scalar solution are established antecedents, not new claims.

## Limitations

The theorem is specific to type \(A_2\) in characteristic three and does not provide a classification of Hom–Lie structures for all small-characteristic simple Lie algebras. The rank minor is a transparent exact arithmetic certificate, not a conceptual classification for arbitrary ranks. Novelty has been checked against accessible primary material and mathematical-record searches, but an unlocated older treatment of this characteristic-three special case remains a priority risk. Independent external audit has not been performed.

## References

1. J. Sun, C. Zhang, H. Zhu, *Classification of Hom–Lie structures on finite-dimensional simple Lie algebras*, arXiv:2610.25056v1, first submitted 2026-10-18. https://arxiv.org/html/2610.25056v1
2. A. Makhlouf, P. Zusmanovich, *Hom–Lie structures on Kac–Moody algebras*, J. Algebra 515 (2018), 278–297, arXiv:1805.00187. https://arxiv.org/abs/1805.00187
3. W. Xie, Q. Jin, W. Liu, *Hom-structures on semi-simple Lie algebras*, Open Math. 13 (2015), 617–630, DOI 10.1515/math-2015-0059. https://doi.org/10.1515/math-2015-0059

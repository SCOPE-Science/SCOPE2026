# Binary perfect evolution algebras: exact idempotent spectra and idempotent-free isomorphism strata

## Finding
For every integer \(n\ge1\), the number \(N_{n,r}\) of invertible \(n\)-by-\(n\) binary structure matrices whose evolution algebra has exactly \(2^r\) idempotents, counting zero, is
\[
N_{n,r}={n\brack r}_2\sum_{j=0}^{n-r}(-1)^j2^{\binom j2}{n-r\brack j}_2\,2^{(r+j)(n-r-j)}\,|\operatorname{GL}_{n-r-j}(\mathbb F_2)|.
\]
The only possible exponent values satisfy \(0\le r\le n\); in particular \(N_{n,0}>0\) if and only if \(n\ge2\). The numbers of **isomorphism types** of perfect binary evolution algebras without nonzero idempotents for dimensions \(2,3,4\) are \(1,8,248\). In dimension four the 248 types split into two relabeling orbits of size 8, eight of size 12, and 238 of size 24. These isomorphism counts are different from the matrix-presentation counts \(2,48,5824\).

## Assumptions and scope
The ground field is \(\mathbb F_2\). An evolution algebra of dimension \(n\) has a natural basis \(e_1,\ldots,e_n\) with \(e_i e_j=0\) for \(i\ne j\). Its structure matrix \(M\) has row \(i\) encoding \(e_i^2=\sum_j M_{ij}e_j\). It is *perfect* (also called regular in this context) when \(E^2=E\), exactly when \(M\in\operatorname{GL}_n(\mathbb F_2)\). An idempotent is an element \(x\) satisfying \(x^2=x\). \({a\brack b}_2\) denotes the number of \(b\)-planes in \(\mathbb F_2^a\), and \(|\operatorname{GL}_0(\mathbb F_2)|=1\). The all-dimensional formula counts structure matrices, while the \(n=2,3,4\) table additionally counts algebra isomorphism classes.

## Proof
**Linearization.** Write \(x=\sum_i x_i e_i\). By pairwise orthogonality of basis elements, \(x^2=\sum_i x_i^2 e_i^2\). Every \(x_i\in\mathbb F_2\) satisfies \(x_i^2=x_i\), whence in coordinate columns \(x^2=M^{\mathsf T}x\). Therefore the idempotents form exactly the fixed space \(\ker(M^{\mathsf T}-I)\), of cardinality \(2^r\) for its dimension \(r\). Transposition bijects invertible matrices and preserves dimensions of fixed spaces, so it suffices to count \(g\in\operatorname{GL}_n(\mathbb F_2)\) by \(\dim\ker(g-I)\).

**Counting exact fixed spaces.** Fix an \(r\)-plane \(U\le\mathbb F_2^n\). The matrices fixing every vector of \(U\) have, in a basis beginning with \(U\), blocks \(\begin{psmallmatrix}I_r&A\\0&B\end{psmallmatrix}\), where \(A\) has \(r(n-r)\) arbitrary binary entries and \(B\in\operatorname{GL}_{n-r}(\mathbb F_2)\). Their count is \(2^{r(n-r)}|\operatorname{GL}_{n-r}(\mathbb F_2)|\). On the lattice of subspaces, the Möbius function of an interval of dimension \(j\) is \((-1)^j2^{\binom j2}\) (proved by the Gaussian-binomial identity \(\sum_{j=0}^m(-1)^j2^{\binom j2}{m\brack j}_2=0\) for \(m>0\)). Inverting the above count over all superspaces \(W\supseteq U\) shows that the number of matrices with *exactly* \(U\) as fixed space is
\[
\sum_{j=0}^{n-r}(-1)^j2^{\binom j2}{n-r\brack j}_2\,2^{(r+j)(n-r-j)}|\operatorname{GL}_{n-r-j}(\mathbb F_2)|.
\]
Multiplying by the number \({n\brack r}_2\) of choices of \(U\) proves the displayed formula, without assuming a finite enumeration.

**Existence boundary.** For \(n=1\), the sole invertible binary matrix is \((1)\), so a nonzero idempotent exists. For every \(n\ge2\), let \(g\) be the companion matrix of a monic irreducible polynomial of degree \(n\) over \(\mathbb F_2\). Its constant term is nonzero and it has no eigenvalue \(1\), since otherwise the irreducible polynomial would be divisible by \(t+1\). Thus \(g\) is invertible and \(\ker(g-I)=0\), proving the sharp boundary. At \(n=2\), the concrete natural-basis relations \(e_1^2=e_2\), \(e_2^2=e_1+e_2\) give structure rows \((0,1),(1,1)\), so the algebra is perfect but has no nonzero idempotents.

**Isomorphism orbit count.** Let \(E_M\) and \(E_{M'}\) be perfect. Because \(e_i^2\) are linearly independent, for any natural basis \(f_j=\sum_i a_{ij}e_i\), the condition \(f_jf_k=0\) for \(j\ne k\) forces \(a_{ij}a_{ik}=0\) for every \(i\). Therefore a natural-basis change is monomial. Over \(\mathbb F_2\) all its nonzero scalars equal 1, so it is a permutation of basis vectors. The isomorphism condition is exactly simultaneous permutation of the rows and columns of \(M\). For \(n=2,3,4\), exact enumeration of invertible matrices with \(M-I\) invertible, quotienting by all \(n!\) simultaneous permutations, gives respectively the orbit counts \(1,8,248\) and, for \(n=4\), the orbit-length distribution \(8^{\times2},12^{\times8},24^{\times238}\). The complete stdlib-only code in the verification section performs this finite computation independently of the all-dimensional formula.

## Verification
Run `python3 evol_verify.py` and `python3 evol_orbits.py` in the same directory. The first exhaustively scans all \(2^{n^2}\) binary matrices for \(1\le n\le4\), compares idempotent-space nullities with the closed formula, and checks its total for \(n\le8\). The second independently groups all idempotent-free matrices through dimension four into simultaneous-permutation orbits. The expected success marker of the first script is `VERIFY_OK`. Exact matrix-presentation distributions for \(n=1,2,3,4\) are, by increasing fixed-space dimension, \((0,1)\), \((2,3,1)\), \((48,98,21,1)\), and \((5824,11640,2590,105,1)\). These checks are finite corroboration; the all-dimensional assertion is proved above.

## Relationship to prior work
García-Martínez and Pérez-Rodríguez, *A note on complete evolution algebras*, arXiv:2512.12418v1 (December 13, 2025), develops idempotent equations and a complex-field existence result for perfect evolution algebras. Its general equation \(M^{\mathsf T}(x_i^2)=x\) specializes over \(\mathbb F_2\) to the linear fixed-space identity used here, but does not itself supply the complete binary fixed-space distribution or the restricted idempotent-free orbit counts. Wei and Zou, *Isomorphism Classes of Idempotent Evolution Algebras* (2023), already establish the monomial-action description and enumerate **all** perfect algebra isomorphism classes through rank four; this known action is used, not claimed as new. The present refinement counts classes satisfying the additional nonzero-idempotent obstruction. Classical linear derangement and subspace Möbius-inversion theory supply the general fixed-space count; the contribution is its explicit algebra-specific stratification and the sharp finite-field existence boundary.

## Limitations
The exact numerical **isomorphism-orbit** census is restricted to dimensions two through four; the all-rank closed formula counts structure-matrix presentations, not isomorphism classes. Neither the linearization nor this count holds unchanged over \(\mathbb F_{2^m}\) for \(m>1\), since \(x_i^2=x_i\) is false in general. Nonzero idempotents may appear after scalar extension. The relevant 2023 classification develops broad orbit-enumeration techniques; an implicit or differently indexed idempotent-filtered table could coincide with these counts. No independent validation is claimed.

## References
1. A. García-Martínez and R. Pérez-Rodríguez, *A note on complete evolution algebras*, arXiv:2512.12418v1 (posted December 13, 2025); DOI:10.1007/s00013-026-02251-0.
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and its Applications 675 (2023), 142–178, arXiv:2310.12368; DOI:10.1016/j.laa.2023.06.006.
3. O. J. Falcón Ganfornina, R. M. Falcón Ganfornina and J. Núñez Valdés, *Classifications of evolution algebras over finite fields* (2016); earlier low-dimensional finite-field classification.

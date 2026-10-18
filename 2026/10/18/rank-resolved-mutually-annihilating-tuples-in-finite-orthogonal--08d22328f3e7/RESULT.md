# Rank-resolved mutually annihilating tuples in finite orthogonal Lie algebras

## Finding

Let \(q\) be an **odd prime power**. Let \(V\) be an \(n\)-dimensional vector space over \(\mathbf F_q\), \(n\ge 1\), equipped with a nondegenerate symmetric bilinear form \(B\). Write
\[
\mathfrak{so}(V,B)=\{X\in\operatorname{End}_{\mathbf F_q}(V):B(Xv,w)+B(v,Xw)=0\text{ for every }v,w\in V\}.
\]
For an integer \(k\ge 1\), count **ordered, labeled** tuples \((X_1,\ldots,X_k)\in\mathfrak{so}(V,B)^k\) obeying \(X_iX_j=0\) for **all** \(1\le i,j\le k\). Let their joint-image dimension be \(r=\dim\sum_i\operatorname{im}X_i\). Define the Gaussian coefficient \({a\brack b}_q\) to be the number of \(b\)-dimensional subspaces of \(\mathbf F_q^a\), zero when \(b\notin[0,a]\). Put
\[
A_{r,k}(q)=\sum_{j=0}^{r}(-1)^{r-j}q^{\binom{r-j}{2}}{r\brack j}_q q^{k\binom j2}.
\]
The **exact rank distribution** is
\[
\boxed{N_{V,k}(r;q)=I_V(r)A_{r,k}(q),}
\]
where \(I_V(r)\) is the number of totally isotropic \(r\)-subspaces of \((V,B)\), and \(I_V(r)=0\) beyond its Witt index. More explicitly, for \(0\le r\le\operatorname{wi}(V)\), these isotropic-subspace counts are:
\[
\begin{array}{c|c}
\text{form on }V&I_V(r)\\\hline
n=2m+1&{m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1)\\
n=2m,\ \text{split}&{m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i-1}+1)\\
n=2m,\ \text{nonsplit}&{m-1\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1).
\end{array}
\]
Empty products are one. For the standard dot product \(B(v,w)=v^{\mathsf T}w\) in even dimension \(2m\), the form is split exactly when \((-1)^m\) is a square in \(\mathbf F_q\). The total tuple count is \(\sum_r N_{V,k}(r;q)\).

The distribution distinguishes the two even-dimensional Witt types. For \(n=6\), \(q=3\), and \(k=2\), the split rank profile is \((N(0),N(2),N(3))=(1,4160,49920)\), totaling \(54081\), whereas the nonsplit profile is \((N(0),N(2))=(1,2240)\), totaling \(2241\). In particular, an **odd** three-dimensional joint image is possible for two matrices although each individual skew-adjoint square-zero matrix has even rank.

## Assumptions and scope

Finite fields have **odd** characteristic throughout; no claim is made for characteristic two. The bilinear form is symmetric and nondegenerate. Tuples are counted as matrices/endormorphisms, **not** modulo isometry or conjugacy. Every ordered product, including each square, is zero. The empty tuple of endomorphisms is not part of the scope (\(k\ge1\)); the all-zero tuple is counted once at \(r=0\).

The origin of this refinement is the study of orthogonal self-dual quiver representations with radical-square-zero relations, rather than unrestricted matrix tuples. Requiring skew-adjoint loops makes the joint-image subspace isotropic, imposing Witt-type distinctions invisible in the unrestricted representation census.

## Proof

**1. Isotropic joint images.** Put \(U=\sum_i\operatorname{im}X_i\). For any \(v,w\in V\) and indices \(i,j\), skew-adjointness and the product relations imply
\[
B(X_iv,X_jw)=-B(v,X_iX_jw)=0.
\]
Therefore \(B|_{U\times U}=0\), so \(U\) is totally isotropic and \(r\le\operatorname{wi}(V)\). Moreover, skew-adjointness gives \(U^\perp\subseteq\ker X_i\) for every \(i\): if \(a\in U^\perp\), then \(B(X_ia,v)=-B(a,X_iv)=0\) for all \(v\), and nondegeneracy forces \(X_ia=0\).

**2. Maps supported on a fixed isotropic subspace.** Fix a totally isotropic \(U\le V\) with dimension \(r\). The nondegenerate pairing induces an isomorphism \(V/U^\perp\cong U^*\). Any linear \(X:V\to V\) with image contained in \(U\) that is skew-adjoint must kill \(U^\perp\), hence factors as
\[
V\longrightarrow U^*\xrightarrow{T}U\longrightarrow V.
\]
The skew-adjoint equation says exactly that the bilinear form \((\lambda,\mu)\mapsto\lambda(T\mu)\) on \(U^*\) is alternating (equivalently, its coordinate matrix is skew-symmetric, with zero diagonal). Conversely, every alternating form on \(U^*\) defines exactly one such skew-adjoint map. There are thus \(q^{\binom r2}\) choices of a single map and \(q^{k\binom r2}\) ordered \(k\)-tuples with each image contained in \(U\). Because \(U\subseteq U^\perp\), every one of these maps kills \(U\); **all pairwise products automatically vanish**.

**3. Exact joint-image Möbius inversion.** Let \(F(W)=q^{k\binom{\dim W}2}\) count supported tuples with images contained in an isotropic \(W\subseteq U\), and let \(G(W)\) count those whose joint image is **exactly** \(W\). Then \(F(W)=\sum_{T\le W}G(T)\). The subspace-lattice Möbius function is
\[
\mu(T,U)=(-1)^{r-j}q^{\binom{r-j}2},\qquad j=\dim T.
\]
There are \({r\brack j}_q\) subspaces \(T\) of dimension \(j\) in \(U\). Inversion therefore yields \(G(U)=A_{r,k}(q)\), depending only on \(r,k,q\). Every tuple has a unique joint-image \(U\); summing over the \(I_V(r)\) isotropic \(r\)-subspaces proves \(N_{V,k}(r;q)=I_V(r)A_{r,k}(q)\).

**4. Isotropic-subspace product factors.** For an isotropic \(j\)-subspace \(W\), the quotient \(W^\perp/W\) is nondegenerate of dimension \(n-2j\), with the same residual Witt type. Its isotropic lines correspond exactly to isotropic one-dimensional extensions \(W\subset W'\). For a nondegenerate odd-dimensional form of dimension \(2s+1\), the number of isotropic lines is \((q^{2s}-1)/(q-1)\). For even forms of dimension \(2s\), the numbers are respectively \((q^{s-1}+1)(q^s-1)/(q-1)\) (split) and \((q^{s-1}-1)(q^s+1)/(q-1)\) (nonsplit). These follow directly by counting the zero vectors of the standard orthogonal normal forms. Multiplying those line counts as \(j\) increases from zero to \(r-1\), and dividing by the number \(\prod_{i=1}^r(q^i-1)/(q-1)\) of complete flags inside a fixed \(r\)-space, yields precisely the three displayed product formulas, including the restriction to the Witt index.

**5. Distinct rank-three phenomenon.** In the six-dimensional split hyperbolic space choose a basis with Gram matrix \(\left(\begin{smallmatrix}0&I_3\\I_3&0\end{smallmatrix}\right)\). Take \(X_1,X_2\) to have upper-right \(3\times3\) blocks
\[
S_1=\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix},\qquad
S_2=\begin{pmatrix}0&0&0\\0&0&1\\0&-1&0\end{pmatrix},
\]
with all other blocks zero. These endomorphisms are skew-adjoint, satisfy every \(X_iX_j=0\), and their images jointly span the first three basis directions. Substitution into the general formula at \(q=3,k=2\) gives the numerical profiles stated above.

## Verification

The accompanying standard-library Python file `checker.py` independently enumerates all skew-symmetric matrices (with the standard nondegenerate dot product) for small prime fields, filters tuples by their **actual** matrix products, computes joint image ranks by elimination, and compares these distributions with the formula. Exhaustive checks passed for \((n,q,k)=(3,3,2),(4,3,1),(4,3,2),(4,5,2),(5,3,1),(5,3,2)\), with respective rank profiles \((1)\), \((1,16)\), \((1,64)\), \((1,288)\), \((1,80)\), \((1,320)\), listing rank zero and then rank two. A separate exact six-dimensional hyperbolic matrix witness verifies odd joint-image rank three, both six-dimensional Witt-type profiles, and the skew-adjoint relations. The checker also tests integrality, nonnegativity, and support for a broader finite range of parameters. Run using `python3 checker.py`; success ends with `CHECKER_OK`. Prime-power coverage and arbitrary dimensions follow from the proof, **not** from exhaustive computation.

## Relationship to prior work

Boos and Cerulli Irelli (2021) study self-dual orthogonal/symplectic quiver representations, with their isotropic geometry and degeneration questions, over characteristic zero. The present result treats a finite-field **point count with a joint-image rank refinement** for a radical-square-zero loop family, rather than a degeneration-order theorem. Brouwer, Gow, and Sheekey (2014) enumerate **individual symmetric nilpotent matrices**; self-adjoint single-map enumeration does not determine the all-products-zero skew-adjoint tuple strata. Fulman and Guralnick (2018) count **commuting pairs** in several finite Lie algebras; the stronger zero-product relations, rank-refinement, and orthogonal-form sensitivity here do not follow from the commuting-pair total. Durán Díaz and coauthors (2020) analyze square-zero bases of matrix Lie algebras, with isotropy arguments for skew-symmetric square-zero matrices; this is relevant structural background but is not an identified enumeration of ordered mutually annihilating tuples. Huang (2021) treats **unrestricted** mutually annihilating matrix pairs, not orthogonal skew-adjoint families. No general claim about being first in all literature is made.

## Limitations

Only odd characteristic and nondegenerate symmetric forms are covered. The formula is for **labeled** tuples, not isometry orbits, and does not determine generating functions for tuples with merely commuting (nonzero) products. A related 2020 square-zero Lie-algebra article was assessed from its abstract and indexed mathematical passages, but its complete publisher text was not obtainable for line-by-line comparison. Equivalent formulas in unindexed alternating-pencil, Hall-polynomial, or self-dual-quiver literature cannot be excluded; no independent mathematical review has been performed.

## References

- M. Boos and G. Cerulli Irelli, *On degenerations and extensions of symplectic and orthogonal quiver representations*, arXiv:2106.08666v1, first posted June 16, 2021; especially the sections on symmetric representations and isotropic subrepresentations.
- A. Brouwer, R. Gow, and J. Sheekey, *Counting Symmetric Nilpotent Matrices*, Electronic Journal of Combinatorics (2014), DOI: 10.37236/3810.
- J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, Annals of Combinatorics (2018), DOI: 10.1007/s00026-018-0390-4.
- R. Durán Díaz, V. Gayoso Martínez, L. Hernández Encinas, and J. Muñoz Masqué, *The Square-Zero Basis of Matrix Lie Algebras*, Mathematics **8** (2020), 1032, DOI: 10.3390/math8061032.
- Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566v1 (2021).

# Singular components and generic nodes of symmetric spider determinant hypersurfaces

## Finding

Let \(T\) be a labeled *spider*: one central vertex \(o\) with \(r\ge3\) simple path arms \(P_1,\ldots,P_r\) of lengths \(\ell_i\ge1\), where at least one \(\ell_i>1\). Write \(n=1+\sum_{i=1}^{r}\ell_i\). Let \(M_T\) be the generic symmetric \(n\times n\) matrix with independent entries \(a_v\) on its diagonal, independent entries \(b_e\) in the two symmetric positions indexed by each tree edge, and zeros elsewhere. Thus there are \(2n-1\) independent homogeneous coordinates. Put \(X_T=V(\det M_T)\subset\mathbb P^{2n-2}_{\mathbb C}\).

For each edge \(e\), let \(A_e,B_e\) be the two nonempty vertex sets of \(T-e\), and set
\[
Y_e=V\bigl(b_e,\det M_{A_e},\det M_{B_e}\bigr).
\]
For each triple \(1\le i<j<k\le r\) of different arms, set
\[
Z_{ijk}=V\bigl(\det M_{P_i},\det M_{P_j},\det M_{P_k}\bigr).
\]
Here \(M_S\) denotes the principal submatrix with vertices in \(S\), and every defining equation is interpreted in the ambient homogeneous coordinate ring.

**Theorem.** The hypersurface \(X_T\) is integral and normal, and its *reduced* singular locus is the union of precisely the distinct irreducible subvarieties
\[
\operatorname{Sing}(X_T)_{\mathrm{red}}=\bigcup_{e\in E(T)}Y_e\;\cup\;\bigcup_{1\le i<j<k\le r}Z_{ijk}.
\]
All these subvarieties are integral complete intersections of codimension three in \(\mathbb P^{2n-2}\), and hence dimension \(2n-5\). Consequently there are exactly \((n-1)+\binom r3\) components, of respective projective degrees
\[
\deg Y_e=|A_e||B_e|,\qquad \deg Z_{ijk}=\ell_i\ell_j\ell_k.
\]
At a general complex closed point of *each* component, the completed local hypersurface ring is
\[
\mathbb C[[u,v,w,z_1,\ldots,z_{2n-5}]]/(uv-w^2).
\]
Thus each component has a generic transverse ordinary double point of multiplicity two; the Jacobian scheme is generically reduced along every component. The degree of the reduced singular support is
\[
\sum_{e\in E(T)}|A_e||B_e|+\sum_{i<j<k}\ell_i\ell_j\ell_k=\binom{n+1}{3}.
\]
The aggregate binomial degree is already explained by the general class of the corank-two symmetric determinantal locus; the *component decomposition and degree allocation* are the points of interest here.

## Assumptions and scope

The ground field is \(\mathbb C\); all parameter entries are algebraically independent before taking the determinant. The graph is a single spider, not an arbitrary tree. Every arm has at least one vertex and the center is the only vertex of degree at least three. The star pattern, in which every arm has length one, is a known boundary specialization and is excluded from the fresh-family assertion. The two-arm path pattern is also an established boundary case, not claimed here. The schemes in the theorem are explicitly *reduced supports* except where generic Jacobian reducedness is stated.

## Proof

**1. Irreducibility.** For any connected nonempty tree \(S\), its generic symmetric sparse determinant \(f_S\) is irreducible in the polynomial ring over \(\mathbb C\). Induct on its number of vertices. If \(v\) is a leaf adjacent to \(w\), expansion at the leaf yields
\[
f_S=a_vf_{S-v}-b_{vw}^{2}f_{S-\{v,w\}}.
\]
By induction \(f_{S-v}\) is irreducible. It cannot divide the second coefficient: the latter uses a new variable \(b_{vw}\), while the remaining forest determinant has total degree two less than \(f_S\), and the two terms in the displayed expansion are coprime as coefficients of the degree-one polynomial in \(a_v\). Gauss's lemma proves irreducibility. The one-vertex base case is immediate. Hence \(X_T\) is integral.

**2. The singular rank criterion.** Differentiation with respect to each independent diagonal \(a_v\) gives the corresponding principal cofactor of \(M_T\). A matrix of corank at least two has zero adjugate, so gives a singular point. Conversely, if the symmetric matrix has corank one, its adjugate is a nonzero scalar multiple of \(qq^{\mathsf T}\) for a nonzero kernel vector \(q\). Some diagonal cofactor is then a nonzero multiple of \(q_v^2\); that coordinate derivative is nonzero. Therefore the singular locus, set-theoretically, is precisely the corank-at-least-two locus.

**3. Classification with no vanishing edge parameter.** For a path with every edge parameter nonzero, the equation \(Mq=0\) determines all coordinates of \(q\) successively from its first coordinate; its kernel has dimension at most one. If it has a nonzero kernel, that vector has nonzero first coordinate. For a spider with every edge parameter nonzero, let \(s\) be the number of arm principal matrices \(M_{P_i}\) that are singular. If \(s=0\), solving the arm equations in terms of the central coordinate shows overall nullity at most one. If \(s>0\), pairing a singular arm equation with its kernel forces the central coordinate of every global kernel vector to vanish. Each singular arm supplies one scalar kernel coefficient; all coefficients obey exactly one nonzero linear constraint from the central row. The global nullity is therefore \(s-1\). In particular, corank at least two holds precisely when at least three *whole-arm* determinants vanish.

**4. Classification with zero edge parameters.** Delete every edge whose coordinate is zero, and write the matrix as a direct sum along the resulting forest. If two distinct forest components are singular, take any zero edge on the original path separating them. Both sides of the associated partition have singular matrices, placing the point in \(Y_e\). Otherwise, for overall nullity at least two, its unique singular forest component must itself have nullity at least two. It cannot be a path, by the preceding recurrence; hence it contains the spider's center and consists of that center and initial truncated portions of some arms. The argument of paragraph 3 forces at least three of those truncated arms to have singular path matrices. Every corresponding *whole-arm* determinant vanishes, because it factors across the intervening zero edge parameters (if there are any). The point therefore lies in one of the \(Z_{ijk}\). This proves the displayed union exhaustively, including all intersections and coordinate-boundary degenerations. The converse inclusions follow from block nullity two on \(Y_e\), and from the three-dimensional space of arm kernel vectors subjected to one central linear constraint on \(Z_{ijk}\), even if other edges happen to vanish.

**5. Irreducible components and degrees.** Each ideal \((b_e,f_{A_e},f_{B_e})\) is prime: after imposing \(b_e=0\), the two irreducible determinant equations concern disjoint sets of variables, and their tensor product over \(\mathbb C\) is a geometrically integral coordinate ring. Similarly, the three path determinants defining \(Z_{ijk}\) involve disjoint sets of variables and form a prime regular sequence. Both types have codimension three and the displayed product degrees by the complete-intersection formula. They are distinct because a generic point of a \(Z_{ijk}\) has all edge coordinates nonzero, whereas \(Y_e\) lies in \(b_e=0\); different \(Y_e\) have different forced coordinate hyperplanes and different triples of arm determinants define different loci. Thus each listed irreducible variety is an actual maximal component. The combinatorial degree identity follows from
\[
\sum_{e\in E(T)}|A_e||B_e|=\sum_{i=1}^{r}\sum_{s=1}^{\ell_i}s(n-s)
\]
and the elementary-symmetric identity for the \(\ell_i\) with sum \(n-1\).

**6. Generic transverse ordinary double points.** At a generic point of any listed component, the matrix has corank exactly two. Locally an invertible principal block may be eliminated by a symmetric Schur complement, expressing the determinant, up to a unit, as the determinant of a symmetric \(2\times2\) matrix. Its linearization consists of the restrictions of varying matrix entries to the two-dimensional kernel; it yields a nondegenerate three-variable quadratic form whenever the restriction map onto \(\operatorname{Sym}^2(\ker M)^*\) is surjective. For \(Y_e\), the two principal-block diagonal deformations and the bridge deformation give respectively two independent squares and their cross term. For \(Z_{ijk}\), the three singular arm kernels have nonzero first coordinates and a single central linear relation with three nonzero coefficients. Diagonal variations in those three arms give three independent squares of three distinct linear forms on a two-dimensional space. In both cases the restriction map has rank three on a dense open set. The formal Morse lemma in characteristic zero yields the asserted completed ordinary-double-point product. Its transverse Jacobian ideal is \((u,v,w)\), so it is generically reduced.

**7. Normality.** The ambient projective singular locus has codimension three, hence codimension two in the integral hypersurface \(X_T\). The hypersurface is Cohen--Macaulay and therefore satisfies \(S_2\); its codimension-one points are regular, so it satisfies \(R_1\). Serre's criterion proves normality.

## Verification

The complete standalone code is `spider_checker.py`; its matching output is `spider_checker_output.txt`. Run `python3 spider_checker.py` with the Python standard library, without third-party packages. It checks the corank-two criterion against the displayed component equations for **218,700** configurations (over the field with 101 elements) for four spider shapes with up to six vertices, using entries from \(\{-1,0,1\}\). It separately builds exact-rational corank-two witnesses and verifies rank-three restriction maps for all edge and arm-triple components in five shapes, including \((2,2,2,1)\). These finite tests are not proofs of the universal theorem. The proof above supplies the unbounded, characteristic-zero argument.

## Relationship to prior work

Kerner--Vinnikov [1] provide the general setting for (symmetric) determinantal representations and essential corank-two singularities. The matrix-tree literature [2] explains why three resonant branches are natural in spectral multiplicity questions, but its Hermitian formulation and spectral assignments do not give complex projective singular-component equations or degree distributions. Huang [3] treats a different family of generic symmetric determinantal multilinear forms. The path/tridiagonal and star/arrowhead families are established specializations; this result addresses spiders with genuinely longer arms and classifies all coordinate-boundary strata without specializing those known patterns. The total degree \(\binom{n+1}{3}\) has a classical determinantal explanation, so it is not presented as new.

## Limitations

This is a classification of the **reduced** singular support and of generic transverse germs, not of the unreduced Jacobian scheme globally. No local-form assertion is made at intersections of components or higher-corank points. It does not apply to arbitrary trees with several high-degree vertices. The originality comparison does not exclude an unindexed historical starlike-tree computation, and independent external mathematical review has not been performed.

## References

[1] D. Kerner and V. Vinnikov, *Determinantal representations of singular hypersurfaces in projective space*, arXiv:0906.3012, first public 2009-06-16. https://arxiv.org/abs/0906.3012

[2] *Eigenvalue assignments and the two largest multiplicities in a Hermitian matrix whose graph is a tree*, *Discrete Applied Mathematics* (2010), DOI:10.1016/j.dam.2009.11.009. https://doi.org/10.1016/j.dam.2009.11.009

[3] J. Huang, *Determinantal Hypersurface from a Geometric Perspective*, Caltech doctoral thesis, 2013. https://thesis.caltech.edu/7656/

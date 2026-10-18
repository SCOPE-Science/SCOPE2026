# Sharp generic length of rank-one extreme-contraction decompositions

## Finding

For positive integers \(m,n\), consider the real operator space \(\mathcal L(\ell_1^n,\ell_\infty^m)\). Write \(\Lambda(T)\) for the smallest number of rank-one extreme contractions in a convex decomposition of a norm-one rank-one operator \(T\), with all coefficients strictly positive. Factor \(T=ab^{\mathsf T}\), normalized so that \(\|a\|_\infty=\|b\|_\infty=1\), and define
\[
r=|\{i:|a_i|=1\}|,\quad c=|\{j:|b_j|=1\}|,\quad
D=(m-r+1)(n-c+1)-1.
\]
Then \(1\le r\le m\), \(1\le c\le n\), and:

1. Every such \(T\) satisfies \(\Lambda(T)\le D+1\).
2. On each stratum with its \(r\) saturated rows and \(c\) saturated columns and their signs fixed, equality \(\Lambda(T)=D+1\) holds outside a finite union of proper algebraic hypersurfaces in the unsaturated factor parameters. In particular, it holds almost everywhere and on a dense open subset of that stratum.
3. For each stratum, equality is attained by an explicit rank-one matrix with positive factors: set all saturated factors to \(1\), let \(u=m-r\), \(v=n-c\), put \(\tau=e^{-1}\), and assign \(a_{r+i}=\tau^{2^{i-1}}\) for \(1\le i\le u\) and \(b_{c+j}=\tau^{2^{u+j-1}}\) for \(1\le j\le v\). For \(D=0\), the matrix is already a rank-one extreme contraction.

Consequently, the largest possible \(\Lambda(T)\) over norm-one rank-one operators is exactly \(mn\). It is achieved with strictly positive entries and just one saturated row and one saturated column. Thus matrix rank one does not imply an additive-size extreme-contraction representation: the generic minimal number is multiplicative in the input and output dimensions.

## Assumptions and scope

All scalars are real; \(m,n\ge1\); the operator norm is the standard one. A convex representation may use arbitrary nonnegative weights, but terms with zero coefficients and repeated identical terms are deleted when measuring \(\Lambda\). The minimum is over **rank-one extreme contractions**, not over arbitrary rank-one operators or arbitrary extreme contractions. Genericity is with respect to Lebesgue measure on the unsaturated factor parameters, after fixing the saturated index sets and signs. No assertion is made that every individual operator in a stratum needs the generic number.

## Proof

**1. Unit ball and its eligible vertices.** For \(T=(t_{ij})\), the operator norm is \(\|T\|=\max_{i,j}|t_{ij}|\), since the domain is \(\ell_1^n\) and the range \(\ell_\infty^m\). Thus its unit ball is the \(mn\)-coordinate cube. Its extreme contractions are the sign matrices; the rank-one extreme contractions are exactly \(S=uv^{\mathsf T}\) with \(u\in\{-1,1\}^m\), \(v\in\{-1,1\}^n\).

**2. The forced sign face.** Because \(\|T\|=1\), the factor normalization is possible and the saturated index sets \(I,J\) are nonempty. Every \((i,j)\in I\times J\) has \(t_{ij}=a_i b_j\in\{-1,1\}\). If \(T\) is a convex combination of sign matrices, equality at any such entry forces every positively weighted sign matrix to have exactly that entry. For rank-one sign matrices, after the harmless simultaneous sign change \((u,v)\mapsto(-u,-v)\), these constraints fix \(u_i=\operatorname{sgn}(a_i)\) on \(I\) and \(v_j=\operatorname{sgn}(b_j)\) on \(J\). Conversely, every rank-one sign matrix with these fixed row and column signs satisfies the constraints. The eligible-vertex polytope \(P_{I,J}\) is therefore a genuine face of the convex hull of rank-one sign matrices, and every admissible representation is supported in it.

**3. Its affine dimension.** Signed row and column flips reduce the calculation to saturated factors \(1\). Write \(u=m-r\), \(v=n-c\), and let \(x_1,\ldots,x_u\) and \(y_1,\ldots,y_v\) be the remaining signs. Independent affine coordinates of a vertex are
\[
(x_1,\ldots,x_u,\ y_1,\ldots,y_v,\ (x_i y_j)_{1\le i\le u,\ 1\le j\le v}).
\]
The \(1+u+v+uv\) functions \(1,x_i,y_j,x_i y_j\) are distinct Walsh characters on the sign cube, and hence are linearly independent. Therefore
\[
\dim\operatorname{aff}(P_{I,J})=u+v+uv=D.
\]

**4. Membership and the universal upper bound.** For each unsaturated row choose an independent sign \(X_i\) with \(\mathbb E X_i=a_i\); independently choose signs \(Y_j\) with \(\mathbb E Y_j=b_j\). Keep saturated factors deterministic. Then \(\mathbb E[(X_iY_j)]=a_i b_j\) and similarly for every block, so \(T\in P_{I,J}\). By Carathéodory's theorem in the actual affine dimension \(D\), \(T\) has a convex representation using at most \(D+1\) eligible rank-one sign matrices. When \(D=0\) this gives \(\Lambda(T)=1\).

**5. Generic sharpness.** Assume \(D\ge1\). Fix any collection of at most \(D\) eligible vertices. Its affine hull is a proper affine subspace of the \(D\)-dimensional affine hull of \(P_{I,J}\), so it lies in a nontrivial affine hyperplane. Parameterize the target matrices by their unsaturated real factors \(\alpha_i,\beta_j\in(-1,1)\), yielding coordinate map
\[
\Phi(\alpha,\beta)=(\alpha_i,\beta_j,\alpha_i\beta_j)_{i,j}.
\]
A nontrivial affine equation in these coordinates becomes a nonzero polynomial in the independent monomials \(1,\alpha_i,\beta_j,\alpha_i\beta_j\); it cannot vanish identically. Its zero set is closed, nowhere dense, and Lebesgue null in the parameter box. There are finitely many eligible vertices and therefore finitely many collections of at most \(D\) vertices. Avoiding their affine hulls forces every convex representation to use at least \(D+1\) vertices. This proves generic equality and, together with Step 4, the exact stratum maximum.

**6. Explicit sharpness.** Any affine hyperplane spanned by eligible sign vertices has a defining affine equation with rational coefficients. For \(\tau=e^{-1}\), the parameters specified in the Finding produce powers of the transcendental real number \(\tau\). The exponents of the constant, all individual parameters, and every cross product are distinct: each is a sum of zero, one, or two distinct binary powers from disjoint row and column exponent sets. Thus a nonzero rational affine equation becomes a nonzero polynomial in \(\tau\) and cannot vanish. The explicit matrix consequently lies in none of the forbidden vertex affine hulls and requires exactly \(D+1\) terms.

Taking \(r=c=1\) gives \(D+1=mn\). All other strata have \(D+1\le mn\). This proves the maximum.

## Verification

The standalone `checker.py` uses exact rational arithmetic and independently checks affine ranks and Bernoulli barycenters across all \(100\) pairs of dimensions \(1\le m,n\le4\) and all permitted saturation counts. It also verifies the four-term rational witness
\[
T=\begin{pmatrix}1&1/5\\1/3&1/15\end{pmatrix},
\]
whose unique eligible decomposition weights are \(2/15,1/5,4/15,2/5\), all positive. For
\[
T=\begin{pmatrix}1&1/5&1/7\\1/3&1/15&1/21\end{pmatrix}
\]
exact linear algebra excludes every decomposition with at most five eligible vertices, while the theorem supplies an upper bound of six. The checker successfully completed all tests. These finite checks corroborate small cases; they are not substitutes for the arbitrary-dimensional proof or the transcendence argument.

Reproduction: run `python checker.py` with Python 3 and SymPy installed. No external datasets are required.

## Relationship to prior work

Sohel–Sain–Paul (arXiv:2208.10184, first public 2022-08-22) identify the rectangular operator space with a coordinate cube and enumerate extreme contractions. Sain–Sohel–Paul (arXiv:2407.05545; published online in 2022) study the qualitative rank-invariant Krein–Milman problem and the geometry of rank-one extreme contractions. The rank-one decomposition's existence alone does not determine its smallest number of summands. The present result determines a sharp, saturation-sensitive **minimal-length** bound and proves that generic rank-one contractions require the full product number \(mn\) in the minimally saturated stratum.

The sign-vertex polytope is also a bipartite correlation or cut polytope in alternate coordinates. Huber–Marić (arXiv:1706.06182) analyze Bernoulli correlation polytopes, feasible correlations, and sampling. Their correlation-realizability results do not state the present generic minimal length of norm-one rank-one operator decompositions. Classical Carathéodory theory supplies the upper-bound step but not by itself the saturation face, rank-one representability, or sharp generic lower bound.

## Limitations

The theorem concerns the **real** space and the specific pair \(\ell_1^n\to\ell_\infty^m\). For exceptional parameter choices, minimal decomposition length may be strictly smaller; no complete formula for the exceptional points is claimed. Transcendence is used only for an explicit all-dimensional witness, not for the almost-everywhere statement. Related formulations in local correlation polytopes or convex-mixture complexity could predate this statement and require independent bibliographic scrutiny.

## References

1. S. Sohel, D. Sain, K. Paul, *On subspaces of \(\ell_\infty\) and extreme contraction in operator spaces*, arXiv:2208.10184v1 (2022-08-22). https://arxiv.org/html/2208.10184v1
2. D. Sain, S. Sohel, K. Paul, *Extreme contractions on finite-dimensional Banach spaces*, Colloq. Math. 172 (2023), 65–83; arXiv:2407.05545v1. https://arxiv.org/html/2407.05545v1
3. M. Huber, N. Marić, *Bernoulli Correlations and Cut Polytopes*, arXiv:1706.06182v2 (2017). https://arxiv.org/html/1706.06182v2
4. Classical Carathéodory convex-hull theorem, in standard finite-dimensional convexity references.

# Sharp resistance negative type on the nine-vertex ternary Cayley torus

## Finding
Let \(G=\mathbb F_3^2\). Its four one-dimensional subgroups, called *directions*, are \(L_1=\langle(1,0)\rangle\), \(L_2=\langle(0,1)\rangle\), \(L_3=\langle(1,1)\rangle\), and \(L_4=\langle(1,-1)\rangle\). Fix conductances \(w_i\ge0\), with at least two strictly positive, and put conductance \(w_i\) on every undirected pair whose difference lies in \(L_i\setminus\{0\}\). This defines a connected electrical graph on nine vertices. Let \(R\) be its effective-resistance metric, \(W=\sum_i w_i\), \(q_i=(W-w_i)^{-1}\), and
\[
r_i=\frac29\sum_{j\ne i}q_j.
\]
Then \(R(x,y)=r_i\) whenever \(y-x\in L_i\setminus\{0\}\). For every \(p>0\), the powered-distance matrix \(D_p=(R(x,y)^p)_{x,y\in G}\) has eigenvalue \(2\sum_i r_i^p\) on constants, and eigenvalue
\[
\mu_i(p)=3r_i^p-\sum_{j=1}^4r_j^p
\]
with multiplicity two in the character space annihilating \(L_i\), for each \(i=1,2,3,4\).

**Sharp Euclidean statement.** The centered Gram matrix \(B_2=-\tfrac12 J D_2J\), where \(J=I-\tfrac19\mathbf1\mathbf1^{\mathsf T}\), is strictly positive on the eight-dimensional zero-sum space, and obeys the sharp all-conductance bound
\[
\boxed{\lambda_{\min}(B_2\vert_{\mathbf1^\perp})\ge\frac{14}{81(W-w_{\min})^2}>0.}
\]
Equality holds **exactly** when precisely two directions have positive conductance. Hence effective resistance itself embeds isometrically as an affinely independent simplex in \(\mathbb R^8\), for every connected choice of the four direction weights.

**All-exponent statement.** Let \(r_*=\max_i r_i\), \(I=\{i:r_i=r_*\}\), and \(k=|I|\); equivalently, \(k\) is the number of conductance directions attaining \(w_{\min}\). If \(k\ge3\), the metric has strict \(p\)-negative type for every finite \(p>0\) and supremal generalized roundness \(\infty\). If \(k\in\{1,2\}\), the supremal exponent \(\wp\) is the unique solution \(p>2\) of
\[
\boxed{\sum_{i\notin I}\left(\frac{r_i}{r_*}\right)^p=3-k.}
\]
Negative type is strict for \(0<p<\wp\), non-strict at \(\wp\), and absent for \(p>\wp\). At \(p=\wp\), the zero-sum equality space consists of the two real Fourier modes for each \(i\in I\), hence has dimension \(2k\). The minimum Hilbert embedding dimension of \(R^{p/2}\) is \(8\) for \(p<\wp\), and \(8-2k\) at the finite endpoint; when \(k\ge3\), it is \(8\) for every finite \(p>0\).

In particular, for the unit-conductance Cartesian torus \(C_3\square C_3\) (two active directions),
\[
\boxed{\wp=\frac{\log 2}{\log(5/4)}=3.1062837195\ldots,}
\]
with minimum embedding dimension four at its critical snowflake exponent.

## Assumptions and scope
The vertex set is the additive group \(\mathbb F_3^2\), not a geometric continuous torus. Each of the four unordered direction pairs receives a single nonnegative conductance, constant under translations. At least two positive directions ensure connectivity because distinct lines span the group. All graph edges have electrical conductance \(w_i\); resistance distance is calculated from the combinatorial weighted Laplacian, not shortest-path length. Infinite exponent refers to all finite positive negative-type exponents, not a finite embedding exponent at infinity. The centered Gram matrix of \(R^{p/2}\) is \(-\tfrac12JD_pJ\).

## Proof
**(1) Resistance by Fourier inversion.** For each nontrivial additive character \(\chi\), its kernel is one of the four lines, say \(L_i\). Exactly one direction is annihilated, and its weighted Laplacian eigenvalue is
\[
\lambda_\chi=\sum_{j=1}^4w_j\sum_{s\in L_j\setminus\{0\}}(1-\chi(s))=3(W-w_i)>0.
\]
There are exactly two such nontrivial characters for each kernel line. The Moore–Penrose inverse therefore has group-convolution kernel \(g\) with Fourier coefficients \(\widehat g(\chi)=\lambda_\chi^{-1}\) for \(\chi\ne1\) and \(\widehat g(1)=0\). For nonzero \(z\in L_i\), each character pair with kernel \(L_j\ne L_i\) contributes \(3\) to \(\sum_\chi(1-\operatorname{Re}\chi(z))\), whereas the pair with kernel \(L_i\) contributes zero. Since \(R(0,z)=2(g(0)-g(z))\), this yields \(R(0,z)=\tfrac29\sum_{j\ne i}q_j=r_i\).

**(2) Complete powered spectrum.** On the constant character, each direction supplies two vertices and hence \(\widehat{R^p}(1)=2\sum_i r_i^p\). For a nontrivial character with kernel \(L_i\), the pair of nonzero points of \(L_i\) has character sum \(2\), and each other line has sum \(-1\). Thus \(\widehat{R^p}(\chi)=2r_i^p-\sum_{j\ne i}r_j^p=\mu_i(p)\). Orthogonality of the nine characters proves these are all eigenvalues, with the stated multiplicities. On \(\mathbf1^\perp\), the Gram eigenvalues are
\[
b_i(p)=\frac12\left(\sum_jr_j^p-3r_i^p\right),\qquad\text{each twice.}
\]
Consequently \(p\)-negative type, strictness, equality-space dimensions, and Euclidean embedding ranks can all be decided from these four scalar expressions.

**(3) Uniform strict \(2\)-negative type.** Relabel a smallest direction conductance as \(w_0=t\) and put \(w_j=t+a_j\), \(a_j\ge0\) for \(j=1,2,3\). Set \(S=a_1+a_2+a_3\), \(D=3t+S=W-t>0\), \(q_0=D^{-1}=\min_iq_i\), and \(x_j=q_j-q_0\ge0\). Write \(C=2/9\). The largest resistance is \(r_0=C(3q_0+x_1+x_2+x_3)\), while \(r_j=r_0-Cx_j\). Expanding gives the exact identity
\[
\sum_{i=0}^3r_i^2-3r_0^2=C^2\left(9q_0^2-2(x_1x_2+x_1x_3+x_2x_3)\right).
\]
Moreover,
\[
\frac{x_j}{q_0}=\frac{a_j}{D-a_j}\le\frac{a_j}{S-a_j}
\]
whenever the right denominator is nonzero. If at least two \(a_j\)'s are positive, direct multiplication shows
\[
\sum_{j<\ell}\frac{a_ja_\ell}{(S-a_j)(S-a_\ell)}
=1-\frac{2a_1a_2a_3}{(a_1+a_2)(a_1+a_3)(a_2+a_3)}\le1,
\]
with the obvious limiting interpretation when one \(a_j=0\). If fewer than two are positive, the left pair-sum is zero and the same inequality holds. Hence \(\sum_{j<\ell}x_jx_\ell\le q_0^2\), so
\[
\min_i b_i(2)=\frac12\left(\sum_ir_i^2-3r_0^2\right)
\ge\frac{14}{81}q_0^2=\frac{14}{81(W-w_{\min})^2}>0.
\]
For equality, both inequality stages must be equalities. With a connected graph, this means \(t=0\), exactly one of the three \(a_j\)'s is zero, and the other two are positive: precisely two active directions. Conversely any such graph has equality. This proves sharpness as well as strictness. Schoenberg's Gram criterion yields the full affine dimension eight.

**(4) Exponents and critical spaces.** Because \(q_i=(W-w_i)^{-1}\) increases strictly with \(w_i\), the maximum \(r_i\) occurs exactly at the minimum conductance. For fixed \(p\), the largest \(\mu_i(p)\) occurs for \(i\in I\). If \(k\ge3\), \(\sum_i r_i^p>3r_*^p\) for all finite \(p>0\), because at least three summands equal \(r_*^p\) and the remaining one is positive (or all four are equal). Thus all inequalities are strict. If \(k=1\) or \(2\), the function \(F(p)=\sum_{i\notin I}(r_i/r_*)^p\) decreases strictly continuously from \(4-k\) at \(p=0\) to zero as \(p\to\infty\), and therefore crosses \(3-k\) exactly once. Step (3) shows that crossing occurs strictly beyond \(2\). The signs of all four \(\mu_i(p)\) prove the type interval; at equality, precisely the characters with kernels in \(I\) have zero eigenvalue on the zero-sum space. Each line contributes two independent real Fourier modes, hence the stated dimensions. The constant row sum is always positive and does not affect conditional negative type.

For \(C_3\square C_3\), two weights are \(1\) and two are \(0\), so the four resistances are \(4/9,4/9,5/9,5/9\). The threshold equation is \(2(4/5)^p=1\), which gives the displayed logarithmic value. When \(k\ge3\), three directions have the same largest resistance; the remaining direction's cosets form the blocks of a two-level ultrametric (the all-equal case is equilateral).

## Verification
The standalone `verify_ternary_resistance.py` uses exact rational inversion of \(L+\tfrac19\mathbf1\mathbf1^{\mathsf T}\) to reconstruct resistances independently of the Fourier derivation. It tests 16 connected conductance profiles, including two-, three-, and four-direction networks and nonintegral weights, compares every one of the 81 pairwise resistances with the four-line formula, checks all four eigenspaces at \(p=1,2,3\), and verifies strictness, the sharp bound and its equality criterion with exact fractions. A separate exact check identifies the unit Cartesian torus's four line distances and its critical-mode multiplicity. These finite tests corroborate the proof; they do not establish it for arbitrary real weights or exponents. Execute `python3 verify_ternary_resistance.py`.

## Relationship to prior work
Fourier–Laplacian formulas for Cayley electrical resistance belong to an established literature, including Zhang–Yang (circulants) and Gao–Luo–Liu (finite abelian Cayley graphs). Jorgensen–Pearse establish the Hilbert geometry of **square-root** effective resistance, rather than the stronger claim that effective resistance itself is a Euclidean norm distance. Li–Weston and Sánchez establish general strict-negative-type and finite-metric threshold principles. The present calculation evaluates the four nontrivial character sectors of **powered effective resistance** on \(\mathbb F_3^2\), proves an explicit sharp Gram lower bound under all connected direction conductances, and determines every negative-type exponent and critical equality space. The full text of Gao–Luo–Liu (2011) was not accessible for a definitive comparison, so possible equivalent coverage there remains unresolved; the claim does not rest on a full-text noncoverage assertion.

## Limitations
The proof concerns exactly nine vertices and translation-invariant conductances constant on each nonzero direction pair; it does not cover arbitrary non-translation-invariant weighted graphs, other finite abelian groups or a general higher-dimensional torus. The universal lower bound is sharp across this family but is not an optimal bound expressed in all four weights separately. The critical exponent is implicit for general conductances; only the symmetric two-direction example has the displayed logarithmic closed form. Finite numerical checks cannot establish originality.

## References
- H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339; first online September 5, 2006, DOI: 10.1002/qua.21068.
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, initially January 6, 2009.
- P. E. T. Jorgensen and E. P. J. Pearse, *A Hilbert space approach to effective resistance metric*, arXiv:0906.2535, initially June 14, 2009.
- X. Gao, Y. Luo and W. Liu, *Resistance distances and the Kirchhoff index in Cayley graphs*, Discrete Applied Mathematics 159 (2011), 2050–2057, DOI: 10.1016/j.dam.2011.06.027; full-text comparison outstanding.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, initially August 2, 2011.

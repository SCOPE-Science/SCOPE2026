# Sharp fourth moments and coefficient rigidity for complete square-free quadratic Fourier polynomials

## Finding
Let \(n\ge4\), let \(z=(z_1,\ldots,z_n)\) belong to the probability Haar torus \(\mathbb T^n\), and take arbitrary complex coefficients \(a_{ij}\) for \(1\le i<j\le n\). Put
\[
 P_a(z)=\sum_{i<j}a_{ij}z_i z_j,\qquad S=\sum_{i<j}|a_{ij}|^2,\qquad N=\binom n2.
\]
The exact sharp fourth moment is
\[
 \boxed{\int_{\mathbb T^n}|P_a|^4\,dz\le C_n S^2,\qquad
 C_n=2-\frac1N+\frac{24\binom n4}{N^2}
 =\frac{6n^2-22n+22}{n(n-1)}.}
\]
For \(S>0\), equality occurs if and only if there are a nonzero complex \(t\) and unimodular \(u_1,\ldots,u_n\) such that \(a_{ij}=t u_i u_j\) for every \(i<j\). Thus the equal-magnitude complete graph packet is the only maximizer modulo vertex phases and common scaling. In particular, \(C_4=5/2\), \(C_5=31/10\), and \(C_n\to6\).

There is also a uniform global *magnitude-stability* estimate. With \(x_{ij}=|a_{ij}|^2\) and
\[
 \gamma_n=\min\left\{3,\ 1+\frac{(n-3)(n-4)}{n-1}\right\},
\]
we have for every coefficient array
\[
 \boxed{C_n S^2-\int_{\mathbb T^n}|P_a|^4\,dz
 \ \ge\ \gamma_n\sum_{i<j}\left(x_{ij}-\frac SN\right)^2.}
\]
This explicit positive stability coefficient is valid, not claimed optimal; it controls squared coefficient magnitudes, not their phases.

## Assumptions and scope
The coefficient field is complex, the monomials are exactly the distinct degree-two square-free characters \(z_i z_j\), and integration uses probability Haar measure. The bound holds for every integer \(n\ge4\), including arrays with zero coefficients. For \(S=0\), both sides vanish and the nonzero equality classification is vacuous. The theorem does not concern Boolean Walsh characters, repeated-index monomials, or general Fourier support graphs.

## Proof
**1. Exact torus convolution identity.** Write \(E=\binom{[n]}2\), indexing \(a_e\) and \(x_e=|a_e|^2\). Two edge pairs produce the same torus character precisely if they are the same unordered pair of edges, except that the three perfect matchings of four distinct vertices have identical character. Consequently, for each quadruple \(i<j<k<l\) set
\[
 X=a_{ij}a_{kl},\quad Y=a_{ik}a_{jl},\quad Z=a_{il}a_{jk}.
\]
Parseval, with the two orderings of every pair of distinct edges, gives the exact identity
\[
 \int|P_a|^4=2S^2-\sum_{e\in E}x_e^2
 +8\sum_{i<j<k<l}\Re(X\overline Y+X\overline Z+Y\overline Z). \tag{1}
\]
Set \(r_e=|a_e|\). The final sum is at most \(8\) times the sum of the three positive products \(|X||Y|+|X||Z|+|Y||Z|\) over every quadruple.

**2. Two complementary quadratic majorants.** Write \(e\sim f\) if distinct edges share a vertex, and \(e\perp f\) if they are disjoint. Each four-vertex block has three nonnegative perfect-matching products \(p,q,r\). First,
\[
 pq+pr+qr\le p^2+q^2+r^2
\]
by \(\sum(p-q)^2\ge0\). Each squared matching product is \(x_e x_f\) for disjoint edges; hence the total four-cycle term in (1) is bounded by
\[
 8\sum_{e\perp f}x_ex_f. \tag{2}
\]
Here and below an unordered edge pair is counted once.

Second, for any four positive edge magnitudes \(b_1,b_2,b_3,b_4\) along one four-cycle,
\[
 b_1b_2b_3b_4\le\frac14
 (b_1^2b_2^2+b_2^2b_3^2+b_3^2b_4^2+b_4^2b_1^2), \tag{3}
\]
by averaging the two opposite-pair arithmetic-geometric mean bounds. Across the three four-cycles on a quadruple, their twelve adjacent-edge pairs occur exactly once. Each pair of globally adjacent edges lies in exactly \(n-3\) four-vertex blocks. Thus the same four-cycle term is also bounded by
\[
 2(n-3)\sum_{e\sim f}x_ex_f. \tag{4}
\]
Both (2) and (4) are equalities for the uniform positive coefficient array.

**3. Strict spectral majorant.** Take the convex combination of (2) and (4) with weight
\[
 \alpha=\frac{n-4}{n-1}\in[0,1).
\]
Let \(L\) be the adjacency matrix of the line graph of the complete graph on \(n\) vertices, indexed by its \(N\) edges, let \(K\) be the complementary disjointness matrix, and let \(J\) be the all-ones matrix. Thus \(K=J-I-L\). Equations (1)--(4) imply
\[
 \int|P_a|^4\le U(x):=2S^2+x^THx,\quad
 H=-I+4\alpha K+(n-3)(1-\alpha)L. \tag{5}
\]
The eigenvalues of \(L\) are \(2(n-2)\) on constants, \(n-4\) on the \((n-1)\)-dimensional vertex-incidence difference space, and \(-2\) on the orthogonal complement of the vertex-incidence row space. To verify this directly, let \(B\) be the \(n\)-by-\(N\) unsigned incidence matrix. Then
\[
 L=B^TB-2I,\qquad BB^T=(n-2)I_n+J_n.
\]
Therefore the stated eigenvalues and multiplicities hold without any spectral-classification assumption. On the same three spaces, \(H\) has eigenvalues
\[
 h_0=-1+2(n-2)(n-3),\quad
 h_1=-1-\frac{(n-3)(n-4)}{n-1},\quad h_2=-3. \tag{6}
\]
In particular the two nonconstant eigenvalues are negative for every \(n\ge4\).

Put \(\mathbf 1=(1,\ldots,1)\) in edge coordinates, \(\bar x=(S/N)\mathbf1\), and \(y=x-\bar x\). Since \(y\perp\mathbf1\) and \(H\mathbf1=h_0\mathbf1\), spectral orthogonality gives
\[
 U(x)=\left(2+\frac{h_0}{N}\right)S^2+y^THy
 =C_nS^2+y^THy. \tag{7}
\]
Using (6) on the nonconstant spaces yields
\[
 -y^THy\ge\gamma_n\|y\|_2^2.
\]
Together with (5) and (7), this proves both the sharp fourth-moment inequality and the displayed stability estimate.

**4. Sharpness and all equality cases.** Choosing \(a_{ij}=1\) makes (1)--(4) equalities and makes \(y=0\); hence the constant is sharp. If a nonzero coefficient array gives equality, (6)--(7) force \(x_e=S/N\) for every edge. All magnitudes are then the same positive number. Equality in the first majorant, and (when \(n=4\)) in the second, forces each four-vertex triple \(X,Y,Z\) to have the same complex argument: under equal positive magnitudes, the exact real-part sum in (1) is maximized only when these three phases coincide.

To reconstruct vertex phases, normalize all edge coefficients to have modulus one and fix vertices \(1,2,3\). Choose \(u_1\) with \(u_1^2=a_{12}a_{13}/a_{23}\), and set \(u_j=a_{1j}/u_1\) for all \(j>1\). The matching-product identities on quadruples \((1,2,3,j)\) show \(a_{2j}=u_2u_j\); the identities on \((1,2,i,j)\) then show \(a_{ij}=u_iu_j\) for \(i,j>2\). The same argument applies when \(n=4\), with only one instance of each required quadruple. Restoring the common magnitude gives \(a_{ij}=t u_i u_j\) for a nonzero scalar \(t\). Conversely, such arrays are obtained from uniform coefficients by rotations of torus coordinates and scaling, and attain equality. This proves the classification.

## Verification
The standalone `checker.py` requires only the Python standard library. It uses Gaussian-integer arithmetic (not floating-point tolerance), independently computes fourth moments by a full convolution dictionary, and compares them to (1) for randomized integer coefficient arrays in dimensions \(4\) through \(9\). It also checks the line-graph spectral polynomial, uniform-coefficient sharpness, the displayed rational constants, the stability inequality, and exact vertex-phase equality examples. Running `python3 checker.py` produced 1,321 successful exact assertions; see `checker_output.txt`. These finite diagnostics do not substitute for the all-dimensional algebraic argument in the proof.

## Relationship to prior work
Gressman, Guo, Pierce, Roos, and Yung (2021) establish the strict majorant property for every even exponent; their Section 8 justifies the coefficient-phase reduction but does not determine the present sharp coefficient optimization, all-dimensional formula, or rigidity. Gressman, Pierce, Roos, and Yung (2022) provide general superorthogonality square-function estimates rather than exact sharp quadratic-chaos constants. Ivanisvili and Tkocz (2018) treat comparison bounds for Rademacher chaoses on the sign cube. The published result on complete quadratic **real Walsh** chaoses has different fourth-moment combinatorics and limiting constant \(15\), not the Steinhaus-torus constant \(6\), and cannot imply this sharp torus result. A previously recorded four-coordinate torus case is included in the statement but does not cover dimensions \(n\ge5\).

## Limitations
The theorem is for a complete square-free degree-two spectrum, not arbitrary graph-supported Fourier sums, higher-degree chaoses, or other product-group distributions. The numerical stability coefficient is certified, not claimed optimal; no quantitative coefficient-phase stability is proved. The literature comparisons establish best-knowledge novelty only; alternative unindexed invariant-theory or Fourier-chaos formulations remain a priority risk. No independent audit has been performed.

## References
1. P. T. Gressman, S. Guo, L. B. Pierce, J. Roos, P.-L. Yung, *On the strict majorant property in arbitrary dimensions*, arXiv:2106.12538v1 (first public date 2021-06-23), Section 8. https://arxiv.org/abs/2106.12538
2. P. T. Gressman, L. B. Pierce, J. Roos, P.-L. Yung, *A new type of superorthogonality*, arXiv:2212.08956v1 (first public date 2022-12-17), Theorem 1. https://arxiv.org/abs/2212.08956
3. P. Ivanisvili, T. Tkocz, *Comparison of moments of Rademacher chaoses*, arXiv:1807.04358v1 (first public date 2018-07-11), Theorem 2. https://arxiv.org/abs/1807.04358
4. *Sharp fourth moments and Euclidean distortion of complete quadratic Walsh chaoses*, published published-finding corpus record `2026/10/11/SCOPE-sharp-fourth-moments-and-euclidean-distortion-of-complete-quadra--5d09daee1c04`, Theorem and proof in `RESULT.md` (real sign-cube case, not the complex torus).

# Sharp fourth moments and Euclidean distortion of complete quadratic Walsh chaoses

## Finding

Let \(n\ge6\) be an integer, and let \(\varepsilon_1,\ldots,\varepsilon_n\) be independent, symmetric random signs. For arbitrary real edge coefficients \(a_{ij}\), define
\[
Q_a=\sum_{1\le i<j\le n}a_{ij}\varepsilon_i\varepsilon_j,\qquad
B=\sum_{1\le i<j\le n}a_{ij}^{2},\qquad m=\binom n2.
\]
Then the sharp fourth-moment bound, with an explicit nonnegative stability remainder, is
\[
\boxed{\mathbb E Q_a^4\ \le\ R_n B^2-2\sum_{i<j}\left(a_{ij}^{2}-\frac{B}{m}\right)^2,\qquad
R_n=\frac{15n^2-63n+68}{n(n-1)}.}
\]
In particular, for \(a\ne0\), equality in the sharp bound \(\mathbb E Q_a^4\le R_n B^2\) holds precisely when there are \(t\in\mathbb R\setminus\{0\}\) and signs \(\sigma_i\in\{-1,1\}\) such that \(a_{ij}=t\sigma_i\sigma_j\) for every \(i<j\). The coefficient \(2\) in the displayed stability remainder is an explicit valid coefficient; it is **not** claimed to be optimal.

Let \(X_{n,2}\subset L^4(\{-1,1\}^n;\mathbb R)\) be the full homogeneous quadratic Walsh space spanned by the \(m\) products \(\varepsilon_i\varepsilon_j\). Its exact multiplicative Banach–Mazur distance from Euclidean space is
\[
\boxed{d_{\rm BM}(X_{n,2},\ell_2^m)=R_n^{1/4}.}
\]
The constants tend to \(R_n\to15\), so the distances tend to \(15^{1/4}\). These assertions concern the **complete** degree-two chaos for every \(n\ge6\), not the analogous single fixed small-dimensional problem.

## Assumptions and scope

The probability measure on the sign cube is uniform, the coefficient field is \(\mathbb R\), the degree is exactly two, and \(L^4\) uses the probability normalization. There is no restriction on support, signs, or magnitudes of \(a\). Here \(d_{\rm BM}\) is the infimum, over invertible linear maps \(T:X_{n,2}\to\ell_2^m\), of \(\|T\|\,\|T^{-1}\|\). The first-public-source date used to identify the historical literature is the verified initial arXiv posting of Adamczak–Wolff, not its revision or journal date; earlier literature is cited separately.

## Proof

**Step 1: exact fourth-power expansion.** Put \(E=\binom{[n]}2\), \(b_e=a_e^2\), and \(B=\sum_{e\in E}b_e\). Let \(\mathcal C\) denote the set of unoriented simple four-cycles of the complete graph. For \(C\in\mathcal C\), write its four edges in cyclic order \(e_1,e_2,e_3,e_4\). Define the nonnegative quantities
\[
 A_C=(a_{e_1}a_{e_2}-a_{e_3}a_{e_4})^2+
     (a_{e_2}a_{e_3}-a_{e_4}a_{e_1})^2,
 \qquad D_C=(a_{e_1}a_{e_3}-a_{e_2}a_{e_4})^2.
\]
They are unchanged by cyclic rotation or reversal of the chosen edge order. Walsh orthogonality says that four edges contribute to \(\mathbb E Q_a^4\) exactly when their symmetric difference is empty. Such quadruples have either two pairs of repeated edges, one edge repeated four times, or four distinct edges forming a four-cycle. Counting their multiplicities gives
\[
 \mathbb E Q_a^4=3B^2-2\sum_{e\in E}b_e^2+
 24\sum_{C\in\mathcal C}\prod_{e\in C}a_e. \tag{1}
\]
Every pair of incident edges belongs as an adjacent pair to exactly \(n-3\) four-cycles, and every disjoint edge pair is opposite in exactly two four-cycles. Thus, writing \(e\sim f\) for distinct incident edges and \(e\perp f\) for disjoint edges, and counting each unordered pair once,
\[
\sum_C A_C=(n-3)\sum_{e\sim f}b_eb_f-4\sum_C\prod_{e\in C}a_e,
\quad
\sum_C D_C=2\sum_{e\perp f}b_eb_f-2\sum_C\prod_{e\in C}a_e. \tag{2}
\]

**Step 2: diagonalizing the magnitude remainder.** For each vertex put
\[
s_i=\sum_{j\ne i}b_{\{i,j\}},\qquad
u_i=\frac{s_i-2B/n}{n-2},\qquad
v_{ij}=b_{ij}-\frac{B}{m}-u_i-u_j.
\]
Then \(\sum_i u_i=0\), and \(\sum_{j\ne i}v_{ij}=0\) for every \(i\). The constant edge array, the arrays \(u_i+u_j\) with zero-sum \(u\), and the arrays \(v\) with zero vertex sums are mutually orthogonal in the ordinary Euclidean product on edge arrays.

The disjointness (Kneser) matrix \(G\), whose entry \(G_{ef}\) is one when \(e\perp f\), acts by the respective eigenvalues
\[
\binom{n-2}{2},\qquad -(n-3),\qquad 1
\]
on these three subspaces. Indeed, for the middle subspace summing \(u_k+u_l\) over edges avoiding \(\{i,j\}\) gives \(-(n-3)(u_i+u_j)\). For the last subspace, subtracting its zero total sum and the zero row sums from the sum over disjoint edges leaves \(v_{ij}\). This proves the spectral identities directly, without invoking a classification theorem.

Let
\[
\alpha=\frac{12}{n-1},\quad
\beta=\frac{12(n-3)}{n-1},\quad
\lambda=2+\frac{6(n-2)(n-3)}{n-1}
=\frac{2(3n^2-14n+17)}{n-1}.
\]
Combining (1) and (2), using \(-4\alpha-2\beta=-24\), reduces the remainder to the quadratic expression
\[
\left(R_n-3-\frac{\alpha(n-3)}2\right)B^2
+\left(2+\frac{\alpha(n-3)}2\right)\sum_e b_e^2
-\frac\beta2\langle b,Gb\rangle.
\]
On the three orthogonal eigenspaces above, its eigenvalues are respectively \(0\), \(\lambda\), and \(2\): substitution of \(\binom{n-2}{2}\), \(-(n-3)\), and \(1\) verifies the last two directly. The zero constant eigenvalue follows by evaluating \(b_e=1\) and positive uniform edge coefficients as below. Therefore the following is an **exact identity** for every real coefficient array:
\[
\boxed{
 R_n B^2-\mathbb E Q_a^4
=\alpha\sum_{C\in\mathcal C} A_C
+\beta\sum_{C\in\mathcal C} D_C
+\lambda\sum_{i<j}(u_i+u_j)^2
+2\sum_{i<j}v_{ij}^2.} \tag{3}
\]
To verify its constant component, set all \(b_e=1\). Then \(A_C=D_C=0\) for uniform positive coefficients, and \(\#\mathcal C=3\binom n4\). Formula (1) gives \(3m^2-2m+72\binom n4=R_n m^2\); hence (3) also vanishes on the constant component. The nonconstant eigenvalues are exactly \(\lambda\) and \(2\), respectively.

Since \(n\ge6\), all four terms on the right of (3) are nonnegative and \(\lambda>2\). Orthogonality gives
\[
\sum_{i<j}\left(b_{ij}-\frac{B}{m}\right)^2
=\sum_{i<j}(u_i+u_j)^2+\sum_{i<j}v_{ij}^2.
\]
This proves the displayed inequality and its remainder for all \(a\). No finite sampling or computer enumeration is used in this universal argument.

**Step 3: sharpness and equality.** The uniform coefficient choice \(a_{ij}=1\) makes every term in (3) zero. Each vertex-sign switching \(a_{ij}=t\sigma_i\sigma_j\) likewise does so. Conversely, equality in the sharp moment bound forces \(b_{ij}=B/m\) for all \(i<j\), since the two positive eigenspace terms in (3) vanish. For a nonzero array, all magnitudes are therefore the same and nonzero. Vanishing of the four-cycle squares forces the product of edge signs around **every** four-cycle to be positive. The products of signs on two triangles sharing an edge are therefore identical. The graph of triangles connected by sharing an edge is connected, so every triangle has one common sign \(\delta\). Fixing vertex \(1\), let \(\tau_i\) be the sign of edge \(\{1,i\}\) for \(i>1\); then \(\operatorname{sgn}(a_{ij})=\delta\tau_i\tau_j\) for \(i,j>1\). Taking \(\sigma_1=\delta\), \(\sigma_i=\tau_i\), and choosing \(t\) with sign \(\delta\) produces precisely \(a_{ij}=t\sigma_i\sigma_j\), as asserted.

**Step 4: optimal Euclidean coordinates.** The coefficient identification with \(\mathbb R^m\) makes the inherited \(L^2\) norm exactly \(\|a\|_2=B^{1/2}\). By monotonicity of probability \(L^p\) norms, \(\|Q_a\|_4\ge\|a\|_2\); equality occurs for a single nonzero edge. The just-proved sharp bound gives \(\|Q_a\|_4\le R_n^{1/4}\|a\|_2\), with equality for switched-uniform arrays. Thus the standard Euclidean coordinates have distortion exactly \(R_n^{1/4}\).

To see that no other ellipsoid improves the distortion, consider any positive-definite quadratic form \(H\) representing a competing Euclidean norm. If \(c\sqrt{a^THa}\le\|Q_a\|_4\le C\sqrt{a^THa}\) holds for all \(a\), the same inequalities hold after applying any sign switch of the underlying \(\varepsilon_i\) and any permutation of vertices. Averaging \(H\) over this finite isometry group preserves the two squared inequalities and the distortion \(C/c\). Vertex sign switches make every off-diagonal entry of the averaged matrix vanish, since distinct edges have distinct sign characters; vertex permutations then force all diagonal entries equal. The averaged matrix is a positive scalar multiple of the identity. Hence the Euclidean pullback is optimal and the stated Banach–Mazur formula follows.

## Verification

The standalone script `verify.py` uses only the Python standard library and exact integer/rational arithmetic. Run `python3 verify.py`. It reconstructs all unoriented four-cycles, directly enumerates the sign cubes in dimensions \(6,7,8\), compares their raw fourth moments with (1), and checks (3), orthogonality, the magnitude stability remainder, Kneser eigenvalues, and uniform-coefficient equality for exact integer test arrays. Successful output ends with `VERIFY_OK`. These finite checks are diagnostics of the **all-dimensional algebraic proof above** and do not replace the arguments establishing (1)–(3) for arbitrary dimension and coefficients.

## Relationship to prior work

The classical Bonami hypercontractive inequality, summarized in Blei–Janson, gives a degree-two fourth-moment bound \(\|Q_a\|_4\le3\|Q_a\|_2\), without the exact finite-dimensional ratio or equality classification. Adamczak–Wolff's Theorem 1.4 develops dimension-free concentration and moment bounds for general polynomials of independent sub-Gaussian variables, but does not supply this exact coefficient, stability remainder, or Euclidean distortion. Bhattacharya–Das–Mukherjee–Mukherjee analyze limit distributions and fourth-moment criteria for quadratic forms with **binary adjacency coefficients**, and their Proposition 1.11 extracts an asymptotic four-cycle condition; it is not an arbitrary-real-coefficient sharp finite-dimensional norm result.

The fixed five-sign full quadratic Walsh space has been considered separately. The present theorem is specifically an **all-dimension family for \(n\ge6\)**, with a uniform exact sum-of-squares identity and nontrivial stability and geometric conclusions. Its statements are not claimed for complex coefficients, higher chaos degrees, or general product distributions.

## Limitations

The stability coefficient displayed above is certified but not claimed best possible. No effective stability of coefficient **signs** under nearly extremal moments is claimed, only the exact equality characterization. The norm and Banach–Mazur formulas hold only for the real, complete, homogeneous degree-two Walsh subspace with uniform signs and \(n\ge6\). Broad-index bibliographic searches and inspected primary papers cannot exclude all unindexed equivalent results; no independent mathematical audit is represented here.

## References

1. R. Blei and S. Janson, “Rademacher chaos: tail estimates versus limit theorems,” *Arkiv för Matematik* 42 (2004), 13–29, DOI `10.1007/BF02432908`, author-publication PDF: `https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7831-11512_2006_Article_BF02432908.pdf`.
2. R. Adamczak and P. Wolff, “Concentration inequalities for non-Lipschitz functions with bounded derivatives of higher order,” arXiv `1304.1826v1`, first publicly posted 2013-04-05: `https://arxiv.org/abs/1304.1826` (Theorem 1.4 and Section 5).
3. B. B. Bhattacharya, S. Das, S. Mukherjee and S. Mukherjee, “Fluctuations of Quadratic Chaos,” arXiv `2203.02850v1`: `https://arxiv.org/abs/2203.02850` (Proposition 1.11 and Section 4).

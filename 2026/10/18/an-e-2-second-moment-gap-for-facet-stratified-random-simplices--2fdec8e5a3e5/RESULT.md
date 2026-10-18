# An \(e^2\) second-moment gap for facet-stratified random simplices

## Finding
Let \(n\ge2\), and let \(\Delta=\operatorname{conv}\{v_1,\ldots,v_n\}\) be any nondegenerate \((n-1)\)-dimensional simplex. Independently choose \(X_i\) uniformly with respect to intrinsic \((n-2)\)-volume on the facet opposite \(v_i\). Define its normalized sampled simplex volume
\[
Z_n=\frac{\operatorname{vol}_{n-1}(\operatorname{conv}\{X_1,\ldots,X_n\})}{\operatorname{vol}_{n-1}(\Delta)}.
\]
The exact squared-volume moment is independent of the shape of \(\Delta\):
\[
\boxed{\mathbb E Z_n^2=\frac{n!}{n^{n-1}(n-1)^n}.}
\]
By contrast, if \(Y_1,\ldots,Y_n\) are independent uniform *interior* points of the same simplex and \(W_n\) is their normalized hull volume, then
\[
\boxed{\mathbb E W_n^2=\frac{n!}{n^n(n+1)^{n-1}},\qquad
\frac{\mathbb E Z_n^2}{\mathbb E W_n^2}=\frac{n(n+1)^{n-1}}{(n-1)^n}\longrightarrow e^2.}
\]
Thus the root-mean-square normalized volume is larger by a factor tending to \(e\), not \(e^2\). These equations concern **second moments**, not expected unsigned volume.

Write \(X_i=\sum_j m_{ji}v_j\), let \(M=(m_{ji})_{j,i=1}^n\) and \(D_n=\det M\); then \(Z_n=|D_n|\). Moreover,
\[
\boxed{\mathbb E D_n=\frac{(-1)^{n-1}}{(n-1)^{n-1}},\qquad
\operatorname{Var}(D_n)=\frac{n!}{n^{n-1}(n-1)^n}-\frac1{(n-1)^{2n-2}}.}
\]
The orientation sign is negative almost surely at \(n=2\), positive almost surely at \(n=3\), and takes both signs with positive probability at every \(n\ge4\).

A combinatorial equivalent of the exact second moment is the identity, valid for every \(n\ge2\),
\[
\boxed{\sum_{\sigma,\tau\in\mathfrak D_n}
\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
2^{|\{i:\sigma(i)=\tau(i)\}|}=n\,n!,}
\]
where \(\mathfrak D_n\) is the set of fixed-point-free permutations of \(\{1,\ldots,n\}\). The identity is a derived form of the same moment result, not a separate unrelated claim.

## Assumptions and scope
Uniformity on each face means its normalized intrinsic Hausdorff measure; when \(n=2\), each facet is a vertex, and the sample is deterministic. The \(n\) face samples are independent and are *stratified*: exactly one point comes from each distinct opposite facet. The comparison experiment instead draws all \(n\) points independently from the interior, uniformly with respect to \((n-1)\)-volume. All simplex shapes are allowed. Affine transformations carry normalized uniform facet measures to normalized uniform facet measures, since the restricted Jacobian on a flat face is constant; therefore normalized volume laws are affine invariant. No assumption of a regular simplex is made.

## Proof
**Barycentric determinant.** Each column \(m_i\) of \(M\) has nonnegative entries summing to one and \(m_{ii}=0\). The homogeneous-coordinate change of basis between two ordered simplex vertex systems yields
\[
\frac{\operatorname{orientedvol}(X_1,\ldots,X_n)}{\operatorname{orientedvol}(v_1,\ldots,v_n)}=\det M,
\]
and therefore \(Z_n=|\det M|\). Each column's other \(n-1\) coordinates form a uniform Dirichlet \((1,\ldots,1)\) vector. In particular,
\[
\mathbb E m_i=\frac{\mathbf1-e_i}{n-1},\qquad
S_i:=\mathbb E(m_i m_i^{\mathsf T})=
\frac{P_i(I+\mathbf1\mathbf1^{\mathsf T})P_i}{n(n-1)},\quad P_i=I-e_ie_i^{\mathsf T}.
\]
The mean matrix is \((\mathbf1\mathbf1^{\mathsf T}-I)/(n-1)\). Its eigenvalues are \(1\) on \(\mathbf1\) and \(-1/(n-1)\) on the orthogonal complement. Column independence and determinant multilinearity give \(\mathbb E D_n=(-1)^{n-1}/(n-1)^{n-1}\).

**Second moment as a squarefree mixed determinant.** For independent random column vectors \(m_i\), expansion of the determinant twice, followed by independence, gives
\[
\mathbb E(\det M)^2=[t_1\cdots t_n]\det\left(\sum_{i=1}^n t_i S_i\right),
\]
where the bracket is the coefficient of the indicated squarefree monomial. To see this directly, the squarefree coefficient is multilinear in the \(n\) input matrices \(S_i\). Replacing them by \(m_i m_i^{\mathsf T}\) makes that coefficient \(\det M^2\), because
\(\det(\sum_i t_i m_i m_i^{\mathsf T})=(\det M)^2\prod_i t_i\). Taking expectations of the multilinear coefficient then replaces each rank-one matrix by \(S_i\); **this argument does not assert equality of the full expected determinant polynomials**.

Let \(T=\sum_i t_i\) and \(t=(t_1,\ldots,t_n)^{\mathsf T}\). Cancellation of diagonal terms in the displayed Dirichlet moments yields
\[
n(n-1)\sum_i t_i S_i=T(I+\mathbf1\mathbf1^{\mathsf T})-t\mathbf1^{\mathsf T}-\mathbf1t^{\mathsf T}.
\]
The matrix determinant lemma, applied as a rank-two perturbation of \(TI\), gives the polynomial identity
\[
\det\bigl(T(I+\mathbf1\mathbf1^{\mathsf T})-t\mathbf1^{\mathsf T}-\mathbf1t^{\mathsf T}\bigr)
=nT^{n-2}\left(T^2-\sum_i t_i^2\right).
\]
For completeness, when \(T\ne0\) write the perturbation as \(UV^{\mathsf T}\) with \(U=[\mathbf1,t]\) and \(V=[T\mathbf1-t,-\mathbf1]\). Then
\[
I_2+T^{-1}V^{\mathsf T}U=
\begin{pmatrix}n&(T^2-\sum_i t_i^2)/T\\ -n/T&0\end{pmatrix},
\]
whose determinant is \(n(T^2-\sum_i t_i^2)/T^2\); polynomial continuity handles \(T=0\). The squarefree coefficient of \(T^{n-2}\sum_i t_i^2\) vanishes, while that of \(T^n\) is \(n!\). Hence
\[
\mathbb E Z_n^2=\frac{n\,n!}{[n(n-1)]^n}=\frac{n!}{n^{n-1}(n-1)^n}.
\]
The variance follows on subtracting the squared first moment.

**Interior comparison.** A uniform interior simplex point has Dirichlet \((1,\ldots,1)\) barycentric vector of length \(n\) and second-moment matrix
\(S=(I+\mathbf1\mathbf1^{\mathsf T})/[n(n+1)]\). Independence of the interior samples and the same squarefree-coefficient argument give
\[
\mathbb E W_n^2=n!\det S=
\frac{n!}{n^n(n+1)^{n-1}}.
\]
Their ratio is exact as stated. Writing it as \((1+1/(n-1))(1+2/(n-1))^{n-1}\) gives the limit \(e^2\).

**Orientation threshold and derangements.** For \(n=2\), the sole allowable stochastic barycentric matrix is the transposition matrix and has negative determinant. For \(n=3\), the two derangement monomials are both positively signed, so every interior-of-face sample has positive determinant. For \(n=4\) there are fixed-point-free permutations of opposite parity: a four-cycle and two disjoint transpositions. For \(n=5\) one may take a five-cycle and a product of a disjoint transposition and three-cycle. Adding a disjoint transposition to both representatives extends the assertion inductively by two dimensions. Each such permutation matrix is in the closure of the columnwise facet sample support. Neighborhoods inside that support have strictly positive sample probability and retain the sign of its nonzero determinant. Therefore both signs occur with positive probability whenever \(n\ge4\).

Expanding \((\det M)^2\) by two permutations leaves only derangements because diagonal entries vanish. On each independent column, distinct off-diagonal entries have product expectation \(1/[n(n-1)]\), while a repeated entry has square expectation \(2/[n(n-1)]\). Thus
\[
\mathbb E D_n^2=[n(n-1)]^{-n}
\sum_{\sigma,\tau\in\mathfrak D_n}
\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
2^{|\{i:\sigma(i)=\tau(i)\}|},
\]
and comparison with the proven second-moment formula yields \(n\,n!\).

## Verification
The companion standalone `verify.py` uses exact integer arithmetic and `Fraction` to enumerate all derangement pairs for \(n=2,3,4,5,6,7\), independently computing the signed cancellation, first and second moments, interior comparison, and parity of available permutation matrices. It passes all six dimensions. Independently, the displayed rank-two polynomial determinant identity was tested symbolically for \(n=2,3,4,5\). Neither finite check is a substitute for the all-\(n\) proof above.

## Relationship to prior work
Turchi and Wespi (2017 preprint, 2018 journal paper) study intrinsic-volume fluctuations for random hulls with points uniformly sampled on smooth convex boundaries; their primary mathematical classification is 52A22, and they do not consider opposite-facet stratification. Reitzner, Schütt, and Werner (2019 preprint; 2023 journal) study random boundary polytopes of simple convex polytopes; Section 3.3 explicitly introduces facet-conditioned random-simplex volume moments and symbolic constants \(\mathcal E_{k,\mathbf f}\), without evaluating the exact distinct-facet, second-moment constant here. Rademacher (2010 preprint; 2012 journal) relates squared volumes of simplices formed by identically distributed interior points to a covariance determinant; his cited formula does not give the present nonidentical facet-conditioned moment. Standard mixed-determinant multilinearity is used as a proof technique rather than claimed as new. The numerical closed form, boundary/interior \(e^2\) comparison, and derangement-pair cancellation are the present proposed contributions.

## Limitations
No formula is claimed for \(\mathbb E Z_n\) (the first **unsigned** volume moment), the full distribution, or arbitrary facet sampling weights. The sign statement does not quantify the probabilities of positive and negative orientation for \(n\ge4\). The second-moment identity has a complete analytical proof, but its literature novelty requires independent bibliographic scrutiny, especially for differently titled work on random stochastic matrices or facet-conditioned simplices.

## References
1. N. Turchi and F. Wespi, *Limit theorems for random polytopes with vertices on convex surfaces*, arXiv:1706.02944 (first publicly available 2017-06-09), *Advances in Applied Probability* **50** (2018), 1227–1245, DOI: 10.1017/apr.2018.58.
2. M. Reitzner, C. Schütt, and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first publicly available 2019-11-14), *Discrete & Computational Geometry* **69** (2023), 453–504, DOI: 10.1007/s00454-022-00460-2; especially Section 3.3 and Lemma 3.1.
3. L. Rademacher, *On the monotonicity of the expected volume of a random simplex*, arXiv:1008.3944 (2010), *Mathematika* **58** (2012), 77–91; especially Lemma 4.
4. B. Reichenwallner, *Moments of volumes of lower-dimensional random simplices are not monotone*, *Monatshefte für Mathematik* **186** (2018), 481–501, DOI: 10.1007/s00605-017-1077-3; its interior and independently boundary-sampled models differ from fixed distinct-facet sampling.

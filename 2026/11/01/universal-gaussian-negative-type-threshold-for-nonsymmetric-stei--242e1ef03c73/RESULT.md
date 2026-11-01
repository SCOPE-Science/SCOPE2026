# Universal Gaussian negative-type threshold for nonsymmetric Steiner incidence metrics

## Finding

Let \(\mathcal D=(P,\mathcal B)\) be any finite simple Steiner \(2\)-\((v,k,1)\) design with \(k\ge2\), and let \(b=|\mathcal B|>v=|P|\). Equip the bipartite point–block incidence graph on \(X=P\sqcup\mathcal B\) with its shortest-path metric \(d\). Set \[p_*:=\log_2\!\left(\frac{k}{k-1}\right).\]
For real \(p\ge0\), define \(d(x,x)^p=0\), including \(p=0\), and \(d(x,y)^0=1\) for distinct points. Then, for every \(t>0\), the Gaussian-type kernel \(\exp[-t d(x,y)^p]\) is positive semidefinite exactly for \[\boxed{0\le p\le p_*.}\] In fact, for each fixed \(t>0\), all these kernels are strictly positive definite. At exponents \(0\le p<p_*\), the powered-distance matrix has strictly negative quadratic form on every nonzero zero-sum vector. At the endpoint, its zero-sum nullspace has dimension \[\boxed{\dim\ker(D_{p_*}|_{\mathbf1^\perp})=\begin{cases}b-v,&k\ge3,\\b-1,&k=2.\end{cases}}\] Here the notation means the nullspace of the centered restriction of the quadratic form, not the uncentered matrix. The minimum Euclidean dimension realizing \(d^{p_*}\) as squared distances is therefore \[\boxed{\begin{cases}2v-1,&k\ge3,\\v,&k=2.\end{cases}}\] For \(0\le p<p_*\) it is \(v+b-1\).

## Assumptions and scope

A simple Steiner \(2\)-\((v,k,1)\) design is a collection of distinct \(k\)-element blocks on \(v\) points such that every pair of distinct points occurs in exactly one block. Assume \(b>v\), which excludes symmetric designs; no geometric realization, transitivity, or resolvability is assumed. The number of blocks through each point is \(r=(v-1)/(k-1)\), and \(bk=vr\). These constraints imply \(r>k\), hence \(r\ge k+1\). The theorem includes pair-block systems with \(k=2\), cyclic Steiner triple systems, affine planes, and the point–line designs of projective spaces of dimension at least three. A design is considered only when it actually exists; no existence claim is made for arbitrary parameters.

For \(p>0\), negative type means that \(\sum_{x,y}c_xc_yd(x,y)^p\le0\) for every real coefficient vector with \(\sum_xc_x=0\). The positive-semidefinite-for-every-\(t\) kernel criterion is equivalent to this property (Schoenberg). The equality-space dimensions below refer to the zero-sum quadratic form.

## Proof

**Step 1: incidence identities and all metric distances.** Let \(M\) be the \(v\)-by-\(b\) point–block incidence matrix and \(A=M^{\mathsf T}M-kI_b\). Pair-uniqueness and regularity give
\[MM^{\mathsf T}=(r-1)I_v+J_v,\quad M\mathbf1_b=r\mathbf1_v,\quad M^{\mathsf T}\mathbf1_v=k\mathbf1_b.\]
Thus \(M\) has full row rank \(v\), and \(\dim\ker M=b-v\). Every two distinct points are distance two; a point and an incident/nonincident block are distance one/three; two distinct blocks are distance two if intersecting and distance four if disjoint. The latter distance is four because one can pass through a point in each block and their unique common block; disjointness precludes any path of length two.

Put \(a=2^p\) and \(z=3^p\). In point/block order, the powered-distance matrix is exactly
\[D_p=\begin{pmatrix}a(J_v-I_v)&zJ_{v,b}+(1-z)M\\ zJ_{b,v}+(1-z)M^{\mathsf T}&a^2(J_b-I_b)+(a-a^2)A\end{pmatrix}.\]
These formulas also cover the off-diagonal-power convention at \(p=0\).

**Step 2: orthogonal decomposition of the zero-sum quadratic form.** The zero-sum subspace has three mutually orthogonal components: \(\{0\}\oplus\ker M\) of dimension \(b-v\); \(v-1\) paired point/line directions based on the mean-zero left singular vectors of \(M\); and one constant-on-each-side contrast direction. The singular value of \(M\) on mean-zero point vectors is \(\sqrt{r-1}\). On \(\ker M\), the scalar value of the quadratic form is
\[\lambda_0(p)=(k-1)a^2-ka=a\big((k-1)a-k\big).\]
On each of the \(v-1\) two-dimensional paired spaces, the corresponding symmetric matrix is
\[H_p=\begin{pmatrix}-a&(1-z)\sqrt{r-1}\\(1-z)\sqrt{r-1}&(r-k-1)a-(r-k)a^2\end{pmatrix}.\]
For the contrast \(w=(\mathbf1_v,-v\mathbf1_b/b)\), the quadratic form divided by \(v\) is
\[C_p:=\frac{w^{\mathsf T}D_pw}{v}.\]
Because the partition is equitable, these three components are orthogonal for this quadratic form. Their dimensions sum to \((b-v)+2(v-1)+1=v+b-1\), so they exhaust the zero-sum subspace.

**Step 3: the sharp endpoint and exact nullities.** At \(p=p_*\), \(a=k/(k-1)\) and \(\lambda_0(p_*)=0\). On the two-dimensional components,
\[H_{p_*}=\begin{pmatrix}-a&(1-z)\sqrt{r-1}\\(1-z)\sqrt{r-1}&-a(r-1)/(k-1)\end{pmatrix},\quad \det H_{p_*}=(r-1)\left(\frac{a^2}{k-1}-(z-1)^2\right).\]
For \(k\ge3\), \(p_*<1\) and strict concavity yields \(z-1=3^{p_*}-1<2(2^{p_*}-1)=2/(k-1)\). As \(4(k-1)\le k^2\), the determinant is strictly positive; the diagonal entries are negative, so \(H_{p_*}\) is negative definite. For \(k=2\), \(p_*=1\), \(a=2\), \(z=3\), and \(H_{p_*}\) has one zero and one strictly negative eigenvalue for each of the \(v-1\) paired directions.

The contrast is strictly negative in both regimes. Direct expansion using \(b=vr/k\) gives
\[C_{p_*}=(r-1)\left[\frac{3k-2}{k-1}-2(k-1)(z-1)\right]-k.\]
For \(k=2\), this equals \(-2\). For \(k\ge3\), let \(u=1/(k-1)\in(0,1/2]\), and \(\beta=\log_2(3/2)>4/7\) (the latter follows from \(3^7>2^{11}\)). Since \(\beta(1-\beta)\le1/4\), Taylor's theorem applied to \((1+u)^\beta\) gives
\[(1+u)^\beta\ge1+\beta u-u^2/8\ge1+(\beta-1/16)u>1+u/2.\]
Now \(z=(1+u)^{1+\beta}\), so
\[z-1>(1+u)(1+u/2)-1=\frac{3k-2}{2(k-1)^2}.\]
Consequently \(C_{p_*}<-k<0\). The only endpoint null modes are therefore the \(b-v\) line-kernel directions for \(k\ge3\), plus \(v-1\) paired directions when \(k=2\), proving both nullity formulas.

**Step 4: below and above the endpoint.** The Schoenberg/Li–Weston strict-lower-exponent theorem says that a metric of positive \(p_*\)-negative type has *strict* \(p\)-negative type for each \(0\le p<p_*\), so no lower-exponent null directions exist. For \(p>p_*\), \(\lambda_0(p)>0\), and \(\ker M\ne0\) gives an explicit positive quadratic-form witness, hence the powered metric has no \(p\)-negative type. For such a witness \(c\) with zero sum, \(c^{\mathsf T}\exp(-tD_p)c=-t c^{\mathsf T}D_pc+O(t^2)<0\) for sufficiently small positive \(t\), proving failure of universal Gaussian positivity.

**Step 5: Gaussian strictness and embedding dimensions.** For allowed \(p\), the centered matrix \(-\frac12P D_pP\), where \(P=I_{v+b}-\mathbf1\mathbf1^{\mathsf T}/(v+b)\), is positive semidefinite and is the Gram matrix of a Euclidean squared-distance realization. Its rank is the zero-sum dimension \(v+b-1\) minus the computed nullity, giving exactly the claimed minimal embedding dimensions. All distinct graph vertices have positive distance, so their Euclidean images are distinct. A Gaussian kernel on distinct Euclidean points is strictly positive definite for every \(t>0\), establishing the strengthening of the universal-positive-semidefinite statement.

## Verification

A standalone Python checker, `check_steiner.py`, independently constructs five designs, verifies pair uniqueness and the matrix identities, computes all-pairs shortest paths rather than trusting the distance formula, and reconstructs the centered powered-distance spectrum at an interior exponent, the exact threshold, and a forbidden exponent. It also tests the endpoint contrast formula and the expected nullities. The examples are a cyclic \(2\)-\((13,3,1)\) triple system, \(\operatorname{AG}(2,3)\), the point–line design of \(\operatorname{PG}(3,2)\), and the pair designs on four and six points. All checks passed. These finite computations verify examples; they are **not** a proof for arbitrary designs. The analytic decomposition and inequalities above provide the all-parameter proof. The script requires Python, NumPy, and SciPy.

## Relationship to prior work

Schoenberg's negative-type/Gaussian correspondence and Li–Weston's strict-negative-type interpolation are pre-existing general results, used explicitly here. Sánchez gave a general finite-metric matrix criterion and applied it to complete bipartite path metrics; that framework does not supply the present design-independent decomposition or sharp parameter. Earlier analyses of affine-plane incidence metrics constitute special cases; a result restricted to affine planes does not imply the theorem for arbitrary nonsymmetric Steiner designs, including projective-space lines and nongeometric Steiner triple systems. The contribution assessed here is the uniform classification for every existing nonsymmetric Steiner \(2\)-design and the exceptional exact endpoint nullity for \(k=2\). It is not a claim that general positive-definite-kernel theory, Steiner incidence identities, or an affine-plane special case is new.

## Limitations

The conclusion assumes \(b>v\); symmetric designs, including projective planes, are excluded and can have different negative-type thresholds. No design-existence theorem is asserted. The numerical checks cover five examples only and rely on floating-point eigenvalue tests. This is an analytic self-review, not an independent mathematical audit. An equivalent older result in specialized design/finite-metric literature cannot be categorically ruled out by the bounded literature search.

## References

1. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first version 2009-01-06). General strict-lower-exponent and Gaussian/negative-type principles; https://arxiv.org/abs/0901.0695 .
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first version 2011-08-02). General finite-matrix and complete-bipartite methods; https://arxiv.org/abs/1108.0451 .

# Sharp centered–uncentered Hilbert maximal-norm equality on \(K_{2,3}\)

## Finding

Let \(G=K_{2,3}\), with unit edge lengths and counting measure. For real functions on its five vertices, let \(M_{\mathrm c}\) be the centered and \(M_{\mathrm u}\) the uncentered graph-distance-ball Hardy–Littlewood maximal operator, both averaging \(|f|\). Their exact attained strong \(\ell^2\) norms coincide:

\[
\boxed{\|M_{\mathrm c}\|_{\ell^2\to\ell^2}=\|M_{\mathrm u}\|_{\ell^2\to\ell^2}=\sqrt{\frac{8+\sqrt{55}}9}=1.3087822366653015\ldots.}
\]

Label the two-vertex class \(A=\{a_1,a_2\}\) and the three-vertex class \(B=\{b_1,b_2,b_3\}\). Every nonzero real extremizer for either operator has absolute values

\[
|f|=s(1,1,c,c,c),\qquad s>0,\quad c=\frac{\sqrt{55}-7}{3}=0.1387328290318877\ldots,
\]

in that vertex order. Independent coordinate signs are arbitrary. In particular, there is exactly one labeled nonnegative extremizing ray, fixed by all graph automorphisms.

## Assumptions and scope

The graph has every edge between \(A\) and \(B\), and no edge within either part. For \(v\in V\) and nonnegative integer \(r\), let \(B(v,r)=\{w:d_G(v,w)\le r\}\). Define

\[
(M_{\mathrm c} f)(v)=\max_{r\ge0}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|,
\quad
(M_{\mathrm u} f)(v)=\max_{B(z,r)\ni v}\frac{1}{|B(z,r)|}\sum_{w\in B(z,r)}|f(w)|.
\]

Radii greater than two add no new balls. The eleven distinct balls are the five singletons, the two closed neighborhoods of vertices in \(A\) (size four), the three closed neighborhoods of vertices in \(B\) (size three), and the whole vertex set (size five). All norms refer to ordinary counting-measure \(\ell^2(V)\).

Among finite connected bipartite graphs without cut vertices, the only graph with fewer than five vertices is the four-cycle (apart from trivial small conventions). On five vertices, minimum degree two and the forced bipartition of sizes two and three give \(K_{2,3}\). Thus this is the first irregular two-connected bipartite example for this question.

## Proof

**1. Exact finite linearization.** For every vertex \(v\), choose one graph ball \(S_v\) containing it, and let \(A_\sigma\) be the nonnegative matrix with row \(v\) equal to \(|S_v|^{-1}\mathbf1_{S_v}^{\mathsf T}\). Each vertex in \(A\) has six available distinct rows, and each vertex in \(B\) has five. There are therefore exactly \(6^2 5^3=4500\) configurations. For every real input \(f\), with \(x=|f|\), the rowwise maxima are independent, so

\[
\|M_{\mathrm u}f\|_2^2=\max_\sigma\|A_\sigma x\|_2^2.
\]

Each \(A_\sigma\) is entrywise nonnegative, hence its largest singular value is attained on a nonnegative right vector: replacing a real vector by its absolute values cannot decrease the output norm. Consequently,

\[
\|M_{\mathrm u}\|_{2\to2}^2=\max_\sigma\lambda_{\max}(A_\sigma^{\mathsf T}A_\sigma).
\]

This is an equality of operator norms, not an assumption that the maximizing input is symmetric.

**2. Distinguished selector and exact spectrum.** Choose singleton rows at \(a_1,a_2\), and at each \(b_j\) the size-three ball \(\{a_1,a_2,b_j\}\). In the stated vertex order this is

\[
A_0=\begin{pmatrix}
1&0&0&0&0\\0&1&0&0&0\\
1/3&1/3&1/3&0&0\\
1/3&1/3&0&1/3&0\\
1/3&1/3&0&0&1/3
\end{pmatrix}.
\]

The Gram operator \(A_0^{\mathsf T}A_0\) acts by eigenvalue \(1\) on the one-dimensional space of antisymmetric \(A\)-coordinates and by eigenvalue \(1/9\) on the two-dimensional space of zero-sum \(B\)-coordinates. On vectors \((a,a,b,b,b)\), its action corresponds to

\[
\begin{pmatrix}5/3&1/3\\2/9&1/9\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}.
\]

The remaining eigenvalues solve \(9\lambda^2-16\lambda+1=0\), so the simple top eigenvalue is \(\lambda_*=(8+\sqrt{55})/9\), with strictly positive eigenvector \(x_*=(1,1,c,c,c)\), where \(c=(\sqrt{55}-7)/3\). Direct substitution gives \(A_0^{\mathsf T}A_0x_*=\lambda_*x_*\).

**3. Complete global optimality certificate.** The exact standard-library Python program `verify_k23.py` constructs all eleven graph balls from the six edges, independently forms every legal selector, and sets \(T_\sigma=60A_\sigma\), an integer matrix. For each of the \(4499\) configurations other than \(A_0\), it checks all five leading principal determinants of the integer symmetric matrix

\[
R_\sigma=6156I-T_\sigma^{\mathsf T}T_\sigma.
\]

Every determinant is strictly positive, calculated by fraction-free integer elimination. Sylvester's criterion gives \(R_\sigma\succ0\); equivalently,

\[
\lambda_{\max}(A_\sigma^{\mathsf T}A_\sigma)<\frac{171}{100}
\qquad(\sigma\ne0).
\]

The threshold is strictly below the distinguished eigenvalue because \(\sqrt{55}>739/100\), or equivalently \(550000>739^2\). Therefore \(A_0\) is the unique maximizing selector, and its spectral radius determines the uncentered norm. This exhausts all legal ball choices; it is not statistical sampling.

**4. Attainment and centered equality.** Since \(0<c<1\), at each \(a_i\) the unique maximizing ball for \(x_*\) is the singleton \(\{a_i\}\); its average is \(1\). At each \(b_j\) the unique maximizing ball is \(\{a_1,a_2,b_j\}\); its average is \((2+c)/3\). Each is centered at the evaluation vertex. Indeed, every competing size-four and size-five average is strictly smaller, by direct comparison using \(c<1\). Hence \(M_{\mathrm c}x_*=M_{\mathrm u}x_*=A_0x_*\). Since \(M_{\mathrm c}\le M_{\mathrm u}\) pointwise, both norms equal \(\sqrt{\lambda_*}\).

**5. All extremizers.** Equality for \(M_{\mathrm u}\) requires a selector attaining the global spectral maximum. The strict certificate leaves only \(A_0\), whose top eigenvalue is simple and whose top eigenvector is the positive ray through \(x_*\). Every centered extremizer is also an uncentered extremizer because the two operator norms coincide. Finally both maximal maps depend only on \(|f|\), so all independent signs of that ray are allowed and no others occur.

## Verification

Run `python3 verify_k23.py` using Python 3 and only the standard library. It independently enumerates all graph balls by breadth-first search, checks the exact \(4500\)-selector count, verifies the spectral invariant subspaces of \(A_0\), and checks strict positivity of every integer Sylvester minor for all other selectors. Expected output:

`CERTIFICATE_OK selections=4500 strict=4499 exceptional=1 threshold=171/100 root=(8+sqrt55)/9`

The characteristic polynomial was also independently evaluated symbolically as \((\lambda-1)(9\lambda-1)^2(9\lambda^2-16\lambda+1)/729\); substituting \(x_*\) into the Gram eigenvector equation gave zero residual in exact algebra.

## Relationship to prior work

Soria and Tradacete introduced sharp graph-maximal estimates and obtained optimal results in the subunit exponent range, with centered graph-ball maximal operators [1]. González-Riquelme and Madrid studied sharp centered strong Hilbert norms on complete graphs and stars, as well as graph variation [2,3]. Their statements do not give the uncentered or centered strong Hilbert norm of this irregular bipartite graph. The later five-vertex graph census of González-Riquelme, Kovač, and Madrid concerns **centered edge-variation** inequalities, not the present strong \(\ell^2\) norm [4]. A 2025 fractional-graph-maximal article describes, in its accessible abstract, sharp Hilbert calculations for complete graphs and stars, not this graph [5]; its full text could not be verified. None of these comparisons establishes absolute publication priority.

## Limitations

The result concerns exactly the unweighted five-vertex complete bipartite graph with counting measure and graph-distance balls. The exhaustive selector certificate is specific to this finite graph and does not establish an exact formula for all \(K_{p,q}\), weighted vertices, arbitrary ball bases, or other \(\ell^p\) exponents. An indexed-literature and record search cannot rule out an unindexed equivalent computation; the fractional-maximal article [5] remains a particular full-text access limitation. Independent scientific audit has not been performed.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1, initially public 2014-10-22. https://arxiv.org/abs/1410.6204
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146. https://arxiv.org/abs/2005.03146
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630. https://arxiv.org/abs/2011.02630
4. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1. https://arxiv.org/abs/2603.12462
5. C. Xiang and F. Zhao, *Sharp constants for fractional Hardy–Littlewood maximal operators on finite graphs*, *Forum Mathematicum* (2025), DOI:10.1515/forum-2024-0406; comparison limited to accessible abstract.

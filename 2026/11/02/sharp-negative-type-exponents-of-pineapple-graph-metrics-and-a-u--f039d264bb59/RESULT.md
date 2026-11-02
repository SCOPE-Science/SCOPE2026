# Sharp negative-type exponents of pineapple graph metrics and a universal leaf asymptotic

## Finding
For every pair of integers \(m\ge3\) and \(n\ge2\), the shortest-path metric of the pineapple graph \(P_{m,n}\) has exact supremal negative-type exponent
\[
\boxed{\wp(P_{m,n})=\log_2 Q_{m,n}},\qquad
Q_{m,n}=2\left(1-U_m\beta_n+\sqrt{\frac{U_m}{n}+U_m^2\beta_n^2}\right),
\]
where \(U_m=m/[2(m-1)]\) and \(\beta_n=(n-1)/(2n)\). The root satisfies \(2<Q_{m,n}<2n/(n-1)\), so the exponent is strictly above one but below the exponent of the star with \(n\) leaves. Negative type is strict below the threshold, nonstrict with exactly one independent equality direction at the threshold, and false above it.

Both \(m\mapsto\wp(P_{m,n})\) and \(n\mapsto\wp(P_{m,n})\) are strictly decreasing. For all \(m\ge3\), uniformly as \(n\to\infty\),
\[
\boxed{\wp(P_{m,n})=1+\frac1{n\log 2}+\frac{2/m-3/2}{n^2\log2}+O(n^{-3})}.
\]
Thus the first-order effect of attaching many leaves at a common vertex is universal across clique sizes, while the next term detects the clique.

## Assumptions and scope
The graph \(P_{m,n}\) consists of a unit-edge clique \(K_m\) with a distinguished vertex \(o\), its other \(a=m-1\) vertices \(u_1,\ldots,u_a\), and \(n\) new vertices \(v_1,\ldots,v_n\), each joined only to \(o\) by a unit edge. The metric \(d\) is the shortest-path metric on all \(m+n\) vertices. In particular, distinct clique vertices are at distance one, as are \(o\) and every leaf; the distances between distinct leaves and between a leaf and an unmarked clique vertex are exactly two.

For real \(p\ge0\), define \(q=2^p\) and let \(d^p\) denote the matrix of powered distances, with diagonal entries zero (also for \(p=0\)). The metric has \(p\)-negative type exactly when \(\sum_{s,t}z_sz_td(s,t)^p\le0\) for every real vector \(z\) with \(\sum_s z_s=0\). Strictness means strict inequality for every nonzero such vector.

## Proof
**1. Exhaustive quadratic decomposition.** Write a zero-sum vector as a hub coefficient \(z_o=-S-T\), core coefficients \(x_i=S/a+\xi_i\), and leaf coefficients \(y_j=T/n+\eta_j\), with \(\sum_i\xi_i=\sum_j\eta_j=0\). The stated distances give the exact identity
\[
\begin{aligned}
\mathcal Q_p(z):=\sum_{s,t}z_sz_t d(s,t)^p
={}&-\sum_{i=1}^{a}\xi_i^2-q\sum_{j=1}^{n}\eta_j^2\\
&-\frac{m}{m-1}S^2+2(q-2)ST
+\left(\frac{n-1}{n}q-2\right)T^2.
\end{aligned}
\]
The contrast terms are strictly negative whenever nonzero. Hence negative type is completely determined by the two-variable matrix
\[
H(q)=\begin{pmatrix}-2U_m&q-2\\q-2&2\beta_n q-2\end{pmatrix}.
\]
Its upper-left entry is strictly negative. Thus it is negative semidefinite precisely when its determinant is nonnegative:
\[
F(q):=4U_m(1-\beta_n q)-(q-2)^2\ge0.
\]

**2. Exact threshold and no other obstruction.** For \(U_m\in(1/2,3/4]\) and \(\beta_n\in[1/4,1/2)\), one has \(F(1)>0\), \(F(2)=4U_m/n>0\), and \(F(1/\beta_n)=-(1/\beta_n-2)^2<0\). Because \(F\) is a concave quadratic with negative leading coefficient, it has exactly one zero \(Q_{m,n}>2\), given by
\[
Q_{m,n}=2\bigl(1-U_m\beta_n+\sqrt{U_m/n+U_m^2\beta_n^2}\bigr).
\]
Its second zero is below one. Therefore \(F(q)>0\) for \(1\le q<Q_{m,n}\), vanishes at the endpoint, and is negative for \(q>Q_{m,n}\). For the last case, the explicit choice \(T=1\) and \(S=(q-2)/(2U_m)\), with no contrast components, yields
\[
\mathcal Q_p(z)=-F(q)/(2U_m)>0,
\]
so the failure assertion is not an inference merely from numerics.

**3. Endpoint equality and affine embedding dimension.** Put \(s=(Q_{m,n}-2)/(2U_m)>0\). At the endpoint the only zero-sum equality directions are multiples of the vector assigning \(-(s+1)\) to \(o\), \(s/(m-1)\) to each unmarked clique vertex, and \(1/n\) to each leaf. Indeed, the contrasts must vanish, and \(H(Q_{m,n})\) has rank one with null vector \((S,T)=(s,1)\). The centered Gram matrix \(-\frac12 Jd^pJ\), with \(J=I-\mathbf1\mathbf1^{\mathsf T}/(m+n)\), has rank \(m+n-1\) below the threshold and rank \(m+n-2\) at the threshold. Schoenberg's finite-metric criterion therefore gives the stated minimum affine dimensions for the isometric Hilbert embeddings of \(d^{p/2}\).

**4. Strict monotonicity.** Increasing \(m\) decreases \(U_m\), while increasing \(n\) increases \(\beta_n\). At every critical root \(Q_{m,n}<1/\beta_n\), so \(\partial F/\partial U_m=4(1-\beta_n Q_{m,n})>0\) and \(\partial F/\partial\beta_n=-4U_m Q_{m,n}<0\). The unique upper-root comparison, together with \(F(2)>0\), proves strict decrease in either discrete parameter. In particular, attaching the clique reduces the exponent below that of the isolated \(n\)-leaf star, whose threshold is \(\log_2(2n/(n-1))\).

**5. Uniform large-leaf expansion.** Write \(\epsilon=1/n\) and \(Q_{m,n}=2+\delta\). Since \(\beta_n=(1-\epsilon)/2\), the exact critical equation becomes
\[
\delta^2+2U_m(1-\epsilon)\delta-4U_m\epsilon=0.
\]
For \(U_m\in[1/2,3/4]\) the implicit-function expansion is uniform, and elementary coefficient comparison gives
\[
\delta=2\epsilon+\left(2-\frac2{U_m}\right)\epsilon^2+O(\epsilon^3)
=2\epsilon+\left(-2+\frac4m\right)\epsilon^2+O(\epsilon^3).
\]
Expanding \(\log_2(2+\delta)\) gives the claimed exponent formula and its universal leading coefficient.

## Verification
The identities above are exact for all integer parameters in the stated ranges. The accompanying `check_pineapple.py` independently constructs each graph's shortest-path distance matrix by breadth-first search and checks the complete centered powered-distance spectrum below, at, and above the proposed threshold. The checker also evaluates the endpoint equality vector and monotonicity for a finite grid, completing 318 assertions. These finite tests are diagnostic; the proof of the infinite-family statement is the exhaustive symbolic quadratic decomposition and the concave polynomial sign argument.

Reproduce the supplementary computation using Python 3 with NumPy by running `python check_pineapple.py`.

## Relationship to prior work
Obata and Zakiyyah (2018) establish quadratic embedding for one-point graph gluing at exponent one. Młotkowski and Obata (2018, arXiv:1802.01214) analyze quadratic embedding constants for star products, again at the ordinary powered-distance exponent one. The pineapple graph is precisely a one-point gluing of a clique and a star, but these ordinary-exponent results do not determine the sharp threshold above one or its equality load. Sánchez (2011, arXiv:1108.0451) gives a general determinant method and computes a different graph family, complete bipartite graphs; Robertson (2023, arXiv:2309.16070) develops the general Hilbert-snowflake interpretation and distorted negative type. Neither inspected primary text states the present closed two-parameter pineapple classification. An adjacency-spectrum study of pineapple graphs (Kumar et al., 2024) concerns a different matrix and is not an established negative-type result. Generic finite-metric criteria could of course be applied to the present family, but the explicit root, unique endpoint load and uniform two-term asymptotic are additional calculations.

## Limitations
Only unit-edge pineapple graph metrics with one common attachment vertex and \(m\ge3,n\ge2\) are classified. The case \(m=2\) is the already-understood star and is excluded from the originality claim. The theorem does not treat arbitrary edge weights, attached longer paths, multiple attachment hubs, or Hilbert distortion beyond the isometric range. Historical mathematical priority is not independently certified, and unindexed alternative formulations may exist. Independent external mathematical validation has not been performed.

## References
1. W. Młotkowski and N. Obata, *On Quadratic Embedding Constants of Star Product Graphs*, arXiv:1802.01214 (first posted 2018-02-04), https://arxiv.org/abs/1802.01214 .
2. N. Obata and A. Y. Zakiyyah, *Distance Matrices and Quadratic Embedding of Graphs*, Electronic Journal of Graph Theory and Applications **6** (2018), 37–60, https://doi.org/10.5614/ejgta.2018.6.1.4 .
3. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (2011), https://arxiv.org/abs/1108.0451 .
4. G. Robertson, *Negative Type and Bi-lipschitz Embeddings into Hilbert Space*, arXiv:2309.16070 (2023), https://arxiv.org/abs/2309.16070 .
5. P. Kumar, S. Merajuddin, S. Pirzada, Y. Shang, *On the Spectral Redundancy of Pineapple Graphs*, Symmetry **16** (2024), 1267, https://doi.org/10.3390/sym16101267 .

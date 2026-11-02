# Sharp negative-type phase transition for clique-core books

## Finding

Let \(s\ge2\), \(m\ge2\), and let \(r_1,\ldots,r_m\) be positive integers. Form the finite simple graph
\[
G=K_s\vee\left(K_{r_1}\sqcup\cdots\sqcup K_{r_m}\right),
\]
where \(\vee\) denotes graph join, and give its vertices the unit-edge shortest-path metric \(d\). Thus a complete core of size \(s\) is adjacent to every vertex of \(m\) disjoint complete peripheral blocks, and different peripheral blocks are separated by distance two. Define
\[
F_{s,\mathbf r}(a)=\left(a-1-\frac1s\right)
\sum_{i=1}^m\frac{r_i}{r_i(a-1)+1},\qquad a>1+\frac1s.
\]
There is a unique \(a_*>1+1/s\) satisfying \(F_{s,\mathbf r}(a_*)=1\). The supremal negative-type exponent of \((V(G),d)\) is exactly
\[
\boxed{\wp(G)=\log_2 a_*}. \tag{1}
\]
For every real \(p\ge0\), the inequality \(\sum_{x,y}\xi_x\xi_y d(x,y)^p\le0\) holds for all real \(\xi\) summing to zero if and only if \(0\le p\le\wp(G)\). This inequality is strict for nonzero zero-sum \(\xi\) when \(0\le p<\wp(G)\), and its equality space at \(p=\wp(G)\) is exactly one-dimensional. One generator has weight \(-1/s\) at each core vertex and weight
\[
\frac{a_*-1-1/s}{r_i(a_*-1)+1}
\]
at each vertex of peripheral block \(i\). Consequently the least affine dimension of an isometric Hilbert embedding of the snowflake \(d^{p/2}\) is \(s+\sum_i r_i-1\) below the endpoint and \(s+\sum_i r_i-2\) at the endpoint.

At fixed \(s,m\) and total peripheral order \(N=\sum_i r_i\), the exponent in (1) is strictly minimized by the unique most balanced integer partition \((r_i)\), up to permutation, and strictly maximized by \((N-m+1,1,\ldots,1)\), up to permutation. Increasing \(s\), increasing any \(r_i\), or adjoining an additional nonempty peripheral clique strictly decreases \(\wp\).

For equal peripheral sizes \(r_i=r\), the formula simplifies to
\[
\boxed{\wp\bigl(K_s\vee(mK_r)\bigr)=
\log_2\left(1+\frac{m/s+1/r}{m-1}\right).} \tag{2}
\]
The powered metric has ordinary negative type at \(p=1\) exactly when \(m/s+1/r\ge m-1\). In the equal-size family \(s\ge2,m\ge2,r\ge1\), equality at \(p=1\) occurs at precisely five integer triples \((s,m,r)\):
\[
(2,3,2),\ (2,4,1),\ (3,2,3),\ (3,3,1),\ (4,2,2).\tag{3}
\]
For fixed \(s,r\), as \(m\to\infty\),
\[
\wp\bigl(K_s\vee(mK_r)\bigr)
=\log_2\left(1+\frac1s\right)
+\frac{1/s+1/r}{(1+1/s)\log 2}\frac1{m-1}
+O_{s,r}(m^{-2}).\tag{4}
\]
In particular, the sharp exponent approaches a positive value less than one for every fixed core size \(s\ge2\). This exhibits a strict qualitative difference from the one-hub clique bouquet.

## Assumptions and scope

All integers \(s,m,r_i\) have the ranges stated above. The graph is unweighted, finite, and simple, \(d\) is its graph geodesic distance, and \(d(x,x)^0=0\) for all vertices while \(d(x,y)^0=1\) for distinct vertices. Only real zero-sum test vectors are required for negative type; the resulting Hilbert embedding may be real. The leading MSC area is 46B85 (embedding questions for metric spaces).

## Proof

Write \(a=2^p\), let \(H\) denote the clique core and \(B_i\) the peripheral cliques, and put \(u=\sum_{x\in H}\xi_x\), \(t_i=\sum_{x\in B_i}\xi_x\), and \(T=\sum_i t_i=-u\), the last equality following from \(\sum_x\xi_x=0\). Every off-diagonal distance is either one (within a clique or between core and peripherals) or two (between different peripheral blocks). Expanding over these classes gives the exact identity
\[
Q_a(\xi):=\sum_{x,y}\xi_x\xi_y d(x,y)^p
=(a-1)T^2-(a-1)\sum_{i=1}^m t_i^2-\sum_{x\in V(G)}\xi_x^2.\tag{5}
\]
Decompose every vector into its constant block average and an orthogonal blockwise zero-sum contrast. For the core and peripheral blocks, the sum of squared coordinates becomes
\[
\sum_x\xi_x^2=\frac{T^2}{s}+\sum_i\frac{t_i^2}{r_i}
+\sum_{x\in H}(\xi_x+T/s)^2
+\sum_i\sum_{x\in B_i}(\xi_x-t_i/r_i)^2.
\]
Substitution into (5) yields
\[
Q_a(\xi)=\alpha(a)T^2-\sum_i\beta_i(a)t_i^2-\mathcal R(\xi),\tag{6}
\]
where \(\alpha(a)=a-1-1/s\), \(\beta_i(a)=a-1+1/r_i>0\) for \(a\ge1\), and \(\mathcal R\ge0\) is exactly the sum of the displayed block-contrast squares. This is an identity for every \(p\ge0\), including \(p=0\).

If \(\alpha(a)\le0\), (6) is strictly negative on nonzero zero-sum vectors. Otherwise weighted Cauchy–Schwarz gives
\[
T^2\le\left(\sum_i\beta_i t_i^2\right)
\left(\sum_i\frac1{\beta_i}\right),
\]
with equality precisely when \(t_i\) is proportional to \(1/\beta_i\). Consequently conditional negative semidefiniteness is equivalent to
\[
\alpha(a)\sum_i\frac1{\beta_i(a)}=F_{s,\mathbf r}(a)\le1.\tag{7}
\]
If the reverse inequality holds, choose constant coordinates on each block with \(t_i\propto1/\beta_i\) to obtain a strict positive witness. The core and peripheral fluctuations cannot contribute equality because \(\mathcal R\) is the sum of nonnegative squares.

For \(a>1+1/s\), each term
\[
\frac{(a-1-1/s)r_i}{r_i(a-1)+1}
\]
is strictly increasing, because its derivative is
\[
\frac{r_i(1+r_i/s)}{\bigl(r_i(a-1)+1\bigr)^2}>0.
\]
The function \(F\) is continuous, starts at zero at \(a=1+1/s\), and tends to \(m>1\) as \(a\to\infty\). It crosses one exactly once. At equality, all contrast vectors vanish and weighted Cauchy equality gives a one-dimensional kernel. Normalizing \(T=1\) gives \(t_i=\alpha(a_*)/\beta_i(a_*)\), and the advertised per-vertex weights. Schoenberg's finite-distance criterion and the standard centered Gram identity \(\langle\Phi(x)-\Phi(o),\Phi(y)-\Phi(o)\rangle=\bigl(d(x,o)^p+d(y,o)^p-d(x,y)^p\bigr)/2\) identify the minimal affine dimension with the rank of the centered Gram matrix, namely the order minus one below the threshold and minus two at equality.

For fixed \(a>1+1/s\), the map \(h_a(t)=t/[t(a-1)+1]\) has derivative \(h_a'(t)=1/[t(a-1)+1]^2>0\) and second derivative \(h_a''(t)=-2(a-1)/[t(a-1)+1]^3<0\). Thus the sum \(\sum_i h_a(r_i)\) is strictly Schur-concave in positive block sizes. At fixed integer total \(N\), balancing transfers strictly increase the sum and strictly lower the unique root \(a_*\); concentrating transfers do the converse. Increasing core size \(s\) increases \(\alpha(a)\); enlarging any block increases \(h_a\); appending a block adds a positive term. All strictly lower the root, which proves the asserted monotonicities.

When every \(r_i=r\), (7) becomes \((a-1-1/s)mr/[r(a-1)+1]=1\), giving (2). The condition \(p_*\ge1\) is equivalent to \(a_*\ge2\), or \(m/s+1/r\ge m-1\). For equality, the integer identity \(mr=s(r(m-1)-1)\), with \(s\ge2\), forces \(r(m-2)\le2\). Directly considering \(m=2,3,4\) gives exactly the five triples (3); no \(m\ge5\) is possible. Finally rewriting (2) as \(a_*=1+1/s+(1/s+1/r)/(m-1)\) and Taylor-expanding \(\log_2 a_*\) gives (4). This completes the proof.

## Verification

Run `python verify_multicore.py` with Python 3 and NumPy installed. The checker independently builds graph distances by graph shortest paths, projects every powered-distance matrix onto the zero-sum hyperplane, compares full eigenvalue spectra below/at/above the analytically determined threshold, checks the explicit null vector, verifies equal-size closed forms, and tests balancing transfers. It passed 6,570 supplementary assertions in the recorded run. These computations cover bounded integer sizes only and are not a substitute for the all-parameter proof above.

## Relationship to prior work

Lou, Obata and Huang studied ordinary quadratic embedding constants for graph joins, including homogeneous friendship graphs [1]. Sánchez gives general computational criteria for supremal negative type of a finite metric space [2]. Doust and Weston give general relations between polygonal equalities and negative type [3]. The 2025 work of Młotkowski and Obata analyzes ordinary quadratic embedding constants for broader joins and illustrates how distance-geometry spectral questions arise in graph joins [4]. Those sources provide context and methods; the present formula is a variable-exponent law for a clique of **at least two universal vertices**, heterogeneous peripheral cliques, and the accompanying finite parameter extremizers. The standard one-hub friendship/clique-bouquet cases, complete split-graph cases with every peripheral clique of size one, and ordinary \(p=1\) results are not claimed as novel standalone findings. The claim instead concerns the multi-vertex core and its parameter dependence.

## Limitations

The theorem applies only to finite unweighted core-clique joins with at least two core vertices and at least two nonempty complete peripheral components. It does not solve arbitrary graph-join negative type, nonclique peripheral blocks, weighted edges, non-Hilbert target spaces, or spectral negative type at powers beyond the stated metric. The literature comparison is not a proof of global novelty; a related generalized-windmill paper was unavailable in complete form, and equivalent historical formulas may exist.

## References

[1] Z. Lou, N. Obata, Q. Huang, “Quadratic Embedding Constants of Graph Joins,” arXiv:2001.06752 (first submitted 2020-01-19), especially the ordinary-distance friendship and regular-join examples.

[2] J. Sánchez, “On the supremal \(p\)-negative type of a finite metric space,” arXiv:1108.0451 (2011).

[3] I. Doust and A. Weston, “Polygonal equalities and \(p\)-negative type,” arXiv:2404.06658 (2024).

[4] W. Młotkowski and N. Obata, “Quadratic embedding constants of fan graphs and graph joins,” arXiv:2403.16348 (2024 preprint), Linear Algebra Appl. 709 (2025), pp. 58–91.

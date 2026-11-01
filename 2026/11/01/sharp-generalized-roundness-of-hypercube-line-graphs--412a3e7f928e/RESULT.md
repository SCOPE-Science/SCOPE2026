# Sharp generalized roundness of hypercube line graphs

## Finding

Let \(n\ge 2\) be an integer. Let \(Q_n\) be the graph on binary words of length \(n\), with two words adjacent when they differ in one coordinate. Let \(X_n\) be the \(n2^{n-1}\) vertices of its line graph \(L(Q_n)\), meaning the edges of \(Q_n\) endowed with the shortest-path metric \(\rho\) in the line graph. Define the generalized roundness exponent \(p_n\) as the supremum of real \(p\ge0\) such that
\[
 \sum_{e,f\in X_n}c_ec_f\rho(e,f)^p\le0
 \quad\text{whenever}\quad \sum_{e\in X_n}c_e=0,
\]
where \(\rho(e,e)^p=0\), including at \(p=0\).

**Theorem.** The sharp exponent \(p_n\) is the *unique* solution in \((0,1]\) of
\[
 \boxed{\displaystyle
 \sum_{h=0}^{n-2}\binom{n-2}{h}
 \left((h+2)^{p_n}-(h+1)^{p_n}\right)=1.}
\]
The negative-type inequality holds for every \(0\le p\le p_n\), strictly on nonzero zero-sum vectors for \(0\le p<p_n\), and fails for every \(p>p_n\). At equality the powered-distance quadratic form has a nullspace of dimension exactly \(n-1\) **within the zero-sum subspace**; every other zero-sum direction is strictly negative. Consequently the smallest Euclidean dimension realizing the squared distances \(\rho^{p_n}\) is exactly \(n2^{n-1}-n\), compared with \(n2^{n-1}-1\) for \(0<p<p_n\).

Moreover \(p_2=1\), \(p_3=\log 2/\log3\), the exponents strictly decrease with \(n\), and
\[
 \boxed{\displaystyle p_n\sim\frac{n}{2^{n-1}}\qquad(n\to\infty).}
\]
For example \(p_4=0.408241382949\ldots\) and \(p_5=0.261559743739\ldots\). The theorem is about graph distances *between cube edges*, not the ordinary Hamming metric between cube vertices.

## Assumptions and scope

The graph is finite, unweighted and undirected, and \(n\) is any integer at least two. Line-graph adjacency means that two distinct edges of \(Q_n\) share an endpoint. The base metric \(\rho\) is *intrinsic shortest-path distance* in this line graph. No infinite-dimensional limit or induced Euclidean edge-midpoint metric is used. The power \(p=0\) is interpreted as one off-diagonal and zero on the diagonal. For \(p>0\), the usual real powers are used.

The stated Euclidean dimension refers to an isometric realization of the metric \(\rho^{p_n/2}\), equivalently to a realization of \(\rho^{p_n}\) as squared Euclidean distances. It does not assert that \(\rho^{p_n}\) itself is a Euclidean distance metric.

## Proof

**1. Edge-distance geometry.** Label each cube edge by \((i,x)\), with \(i\in\{1,\ldots,n\}\), \(x\in\{0,1\}^n\), and the \(i\)-th bit of \(x\) equal to zero. It joins \(x\) to the vertex obtained by flipping bit \(i\). The distance between distinct cube edges in the line graph is one plus the shortest Hamming distance between their endpoint sets: a line-graph walk of length \(\ell\) provides an endpoint walk of length at most \(\ell-1\), and a shortest endpoint walk extends to a line-graph walk of length one more.

For parallel edges along axis \(i\), this distance is \(1\) plus Hamming distance between their fixed \(n-1\) bits. For edges with different axes \(i,j\), the distance is \(1\) plus Hamming distance between the bits outside \(\{i,j\}\); the free endpoint bits \(i,j\) may be selected to agree. Equal edges have distance zero.

**2. Exact Walsh sector reduction.** For integers \(0\le s\le m\) set
\[
 F_m(s,p)=\sum_{a=0}^{s}\sum_{b=0}^{m-s}
 (-1)^a\binom{s}{a}\binom{m-s}{b}(1+a+b)^p.
\]
This is the Walsh transform of the function \(u\mapsto(1+|u|)^p\) on \(\{0,1\}^m\), at a character of support size \(s\). Walsh characters of the cube edge coordinates partition the entire distance matrix into orthogonal sectors indexed by subsets \(S\subseteq\{1,\ldots,n\}\). In the sector for \(S\), put \(s=|S|\); the coordinate indices allowed as edge axes are precisely those not in \(S\), giving \(n-s\) coordinates.

In this basis the restriction of the powered-distance matrix has diagonal entries
\[
 a_s=F_{n-1}(s,p)-1
\]
and off-diagonal entries
\[
 b_s=2F_{n-2}(s,p)\quad(s\le n-2),\qquad b_{n-1}=0.
\]
The subtraction of one removes the unwanted self-distance \((1+0)^p\). The factor two in \(b_s\) sums the free bit on the source edge. Thus the eigenvalues in the sector are
\[
 a_s+(n-s-1)b_s\quad\text{(one direction)},
 \qquad a_s-b_s\quad\text{(\(n-s-1\) directions, when \(s\le n-2\)).}
\]
Each subset \(S\) gives one such block. In the sector \(S=\varnothing\), the one-dimensional first direction is the global constant vector, with a strictly positive distance-matrix eigenvalue. Its remaining \(n-1\) directions are constant on each axis family with axis-family coefficients summing to zero. These are zero-sum vectors.

**3. The only possible first obstruction.** Fix \(0<p<1\). The Bernstein identity
\[
 x^p=c_p\int_0^\infty(1-e^{-tx})t^{-p-1}\,dt,
 \qquad c_p=\frac{p}{\Gamma(1-p)}>0,
\]
implies that for \(1\le s\le m\),
\[
 F_m(s,p)=-J_m(s,p),\qquad
 J_m(s,p)=c_p\int_0^\infty e^{-t}
 (1+e^{-t})^{m-s}(1-e^{-t})^s t^{-p-1}\,dt>0.
\]
In every nonconstant sector \(s\ge1\), the one-direction eigenvalue is
\[
 a_s+(n-s-1)b_s
 =-1-J_{n-1}(s,p)-2(n-s-1)J_{n-2}(s,p)<0
\]
when \(s\le n-2\). For \(s=n-1\), it is \(-1-J_{n-1}(n-1,p)<0\).

For \(1\le s\le n-2\), the transverse eigenvalue satisfies
\[
 a_s-b_s=-1+J_{n-1}(s+1,p).
\]
This follows by substituting the integrals: the factor \(2-(1+e^{-t})\) becomes \(1-e^{-t}\). Since
\[
 \frac{J_{n-1}(s+1,p)}{J_{n-1}(1,p)}
 \quad\text{is a positive weighted average of}\quad
 \left(\frac{1-e^{-t}}{1+e^{-t}}\right)^s<1,
\]
we have the *strict* comparison \(J_{n-1}(s+1,p)<J_{n-1}(1,p)\).

In the empty-support sector, the transverse eigenvalue is exactly
\[
 \lambda_*(n,p)=a_0-b_0
 =-1+\sum_{h=0}^{n-2}\binom{n-2}{h}
 \big((h+2)^p-(h+1)^p\big)
 =-1+J_{n-1}(1,p).
\]
The first equality is an elementary splitting of the \(n-1\)-bit sum into one distinguished bit and the other \(n-2\) bits. Consequently *every other zero-sum eigenvalue is strictly smaller than zero whenever* \(\lambda_*(n,p)\le0\), and the empty-support transverse eigenspace of dimension \(n-1\) is the unique possible endpoint nullspace.

**4. Sharp cutoff, including endpoints.** Write
\[
 S_n(p)=\sum_{h=0}^{n-2}\binom{n-2}{h}
 \big((h+2)^p-(h+1)^p\big).
\]
Every summand is strictly increasing in \(p\ge0\), as the function \(x\mapsto x^p\log x\) increases for \(x\ge1\). Also \(S_n(0)=0\) and \(S_n(1)=2^{n-2}\). Hence for \(n\ge3\) a unique root \(p_n\in(0,1)\) of \(S_n(p)=1\) exists. Step 3 proves strict negative type below it and negative semidefiniteness with precisely \(n-1\) zero directions at it. For \(p>p_n\), the same explicit transverse eigenvector family has positive eigenvalue \(S_n(p)-1\), so negative type fails even when \(p\ge1\). At \(p=0\) the powered distance matrix is \(\mathbf1\mathbf1^{\mathsf T}-I\), strictly negative on zero-sum vectors. When \(n=2\), the line graph is a four-cycle and the same sector calculation directly gives \(\lambda_*=2^p-2\), yielding \(p_2=1\) and a one-dimensional endpoint nullspace; the other two zero-sum eigenvalues are negative.

The finite Schoenberg squared-distance criterion realizes \(\rho^p\) as squared Euclidean distances exactly when its powered distance matrix is conditionally negative semidefinite. The centered Gram matrix is \(-\tfrac12 HD_pH\), where \(H\) projects onto the zero-sum space. Its rank is \(n2^{n-1}-n\) at the endpoint and \(n2^{n-1}-1\) strictly below.

**5. Strict monotonicity and asymptotics.** The binomial identity gives
\[
 S_{n+1}(p)-S_n(p)=\sum_{h=0}^{n-2}\binom{n-2}{h}
 \big((h+3)^p-(h+2)^p\big)>0\qquad(p>0).
\]
Therefore \(p_{n+1}<p_n\). Put
\[
 B_n=\sum_{h=0}^{n-2}\binom{n-2}{h}\log\frac{h+2}{h+1}.
\]
With \(H_n\sim\operatorname{Bin}(n-2,1/2)\),
\[
 B_n=2^{n-2}\mathbb E\left[\log\left(1+\frac1{H_n+1}\right)\right]
 \sim\frac{2^{n-1}}n.
\]
Indeed, on \(H_n\ge n/4\) the integrand multiplied by \(n\) is bounded, and it converges in probability to \(2\); the discarded binomial lower tail is exponentially small even after multiplication by \(n\). Integrating \(p t^{p-1}\) on each unit interval yields, for \(0<p\le1\),
\[
 pB_n\le S_n(p)\le p n^p B_n.
\]
Substitution of \(S_n(p_n)=1\) first gives \(p_n\le B_n^{-1}=O(n2^{-n})\). Therefore \(n^{p_n}=1+o(1)\), and the two-sided bound forces \(p_nB_n\to1\). Hence \(p_n\sim n/2^{n-1}\).

## Verification

A standalone script `verify_hypercube_line_negative_type.py` builds the line graphs directly from cube-edge incidences, independently computes breadth-first-search distances, and checks the two coordinate-distance formulas. It then compares full dense powered-distance eigenvalue spectra against the Walsh-block predictions for dimensions \(2\) through \(5\) at five powers per dimension. It also checks the endpoint root equations and nullities at these sizes, and numerically locates the uniquely defined roots through dimension \(12\). Run with `OPENBLAS_NUM_THREADS=1 python3 verify_hypercube_line_negative_type.py` (NumPy required). A successful run prints `CUBE_LINE_POWERED_DISTANCE_OK 20 independent BFS/Gram spectral comparisons; n=2..12 roots`. These finite checks do *not* establish the theorem for arbitrary \(n\); that is the role of the Walsh and integral arguments above.

## Relationship to prior work

The generalized-roundness and negative-type framework is classical. Sánchez gives a general finite-space determinant criterion and explicitly treats complete bipartite path metrics, not these cube-edge line-graph metrics. Murugan proves a general vertex-transitivity criterion and develops the strict negative type of *subsets of Hamming cubes*; such subsets use the vertex Hamming metric, not the intrinsic edge-adjacency metric considered here. Earlier exact spectral information for exponential-distance kernels on cube line graphs also motivates the Walsh decomposition, which is **not itself claimed new**. Exponential-kernel positive definiteness at a fixed bandwidth does not state the sharp exponent for conditional negative definiteness of every powered distance, its endpoint multiplicity, or its dimension-asymptotic law. A direct implication from such existing general spectral machinery remains a relevant originality comparison.

## Limitations

The conclusion is limited to binary hypercube line graphs with their intrinsic unweighted graph distance. The asymptotic is a first-order equivalence, not a uniform error bound for every \(n\). Originality has been assessed against selected accessible articles, research records and previous relevant statements, not independently certified by exhaustive historical review. An independent mathematical audit has not been performed.

## References

1. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, first public 2011-08-02, https://arxiv.org/html/1108.0451v1. Especially §§1–3.
2. Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1, first public 2011-12-23, https://arxiv.org/abs/1112.5657. Especially §§2–4.

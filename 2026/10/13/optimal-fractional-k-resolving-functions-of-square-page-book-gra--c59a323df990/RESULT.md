# Optimal fractional \(k\)-resolving functions of square-page book graphs
## Finding
For every integer \(r\ge4\), let \(B_r\) be the book graph formed from \(r\) copies of \(C_4\) sharing the common edge \(xy\), with page \(i\) equal to
\[
x a_i b_i y x.
\]
Then
\[
\kappa(B_r)=4
\]
and for every real \(k\in[1,4]\),
\[
\dim_f^k(B_r)=\frac{rk}{2}.
\]

More strongly, write
\[
\alpha_i=g(a_i),\qquad \beta_i=g(b_i).
\]
A function \(g:V(B_r)\to[0,1]\) is a minimum \(k\)-resolving function if and only if
\[
g(x)=g(y)=0,
\]
\[
\alpha_i+\beta_i=\frac{k}{2}\qquad(1\le i\le r),
\]
and, for every \(i\),
\[
\beta_i+\sum_{j\ne i}\alpha_j\ge k,
\qquad
\alpha_i+\sum_{j\ne i}\beta_j\ge k.
\]

Consequently, when \(r=4\) the minimum function is unique for every \(k\in[1,4]\):
\[
g(x)=g(y)=0,
\qquad
g(a_i)=g(b_i)=\frac{k}{4}.
\]
For every \(r\ge4\), the minimum function is also unique at \(k=4\), where every internal page vertex has weight \(1\). In contrast, for every \(r\ge6\) and \(1\le k\le2\), asymmetric minimum functions exist.

## Assumptions and scope
All graphs are finite, simple, and connected. For distinct vertices \(u,v\), let
\[
R\{u,v\}=\{z:d(u,z)\ne d(v,z)\}.
\]
Following the standard fractional \(k\)-metric definition, a function \(g:V(G)\to[0,1]\) is \(k\)-resolving when
\[
g(R\{u,v\})\ge k
\]
for every distinct \(u,v\). The fractional \(k\)-metric dimension is the minimum total weight \(g(V(G))\), and
\[
\kappa(G)=\min_{u\ne v}|R\{u,v\}|.
\]

For \(B_r\), the vertices are the spine endpoints \(x,y\) and the internal page vertices \(a_i,b_i\), with edges \(xy,xa_i,a_ib_i,b_iy\).

## Proof
The distance table yields the following resolving neighborhoods for \(i\ne j\):
\[
R\{a_i,a_j\}=R\{b_i,b_j\}=\{a_i,b_i,a_j,b_j\},
\]
\[
R\{x,b_i\}=\{x,b_i\}\cup\{a_j:j\ne i\},
\]
\[
R\{y,a_i\}=\{y,a_i\}\cup\{b_j:j\ne i\}.
\]
Every other unordered vertex pair has resolving neighborhood equal to all of \(V(B_r)\). Since \(r\ge4\), the smallest displayed neighborhood has size four, so
\[
\kappa(B_r)=4.
\]

Let \(g\) be any \(k\)-resolving function. For every pair of distinct pages \(i,j\), the first resolving-neighborhood identity gives
\[
g(a_i)+g(b_i)+g(a_j)+g(b_j)\ge k.
\]
Summing these \(\binom r2\) inequalities, every internal vertex weight appears exactly \(r-1\) times. Hence
\[
(r-1)\sum_{i=1}^r\bigl(g(a_i)+g(b_i)\bigr)
\ge
\binom r2 k,
\]
so
\[
g(V(B_r))\ge\frac{rk}{2}.
\]

The uniform function
\[
g(x)=g(y)=0,
\qquad
g(a_i)=g(b_i)=\frac{k}{4}
\]
is feasible. The four-vertex resolving neighborhoods have weight exactly \(k\); each neighborhood \(R\{x,b_i\}\) or \(R\{y,a_i\}\) contains \(r\) internal vertices and therefore has weight \(rk/4\ge k\); and a full resolving neighborhood has total weight \(rk/2\ge k\). Thus
\[
\dim_f^k(B_r)=\frac{rk}{2}.
\]

Now suppose \(g\) is minimum. Equality in the lower bound forces
\[
g(x)=g(y)=0
\]
and
\[
\sum_i\bigl(g(a_i)+g(b_i)\bigr)=\frac{rk}{2}.
\]
The sum of the \(\binom r2\) page-pair inequalities is then exactly \(\binom r2k\). Because each individual inequality is at least \(k\), every one is equality. Writing
\[
p_i=g(a_i)+g(b_i),
\]
we obtain
\[
p_i+p_j=k
\]
for every \(i\ne j\), hence
\[
p_i=\frac{k}{2}
\]
for every page.

After these equalities are imposed, the only nonautomatic resolving constraints are those for \(R\{x,b_i\}\) and \(R\{y,a_i\}\). They are precisely
\[
g(b_i)+\sum_{j\ne i}g(a_j)\ge k,
\qquad
g(a_i)+\sum_{j\ne i}g(b_j)\ge k.
\]
This proves necessity. Conversely, the page equalities satisfy every four-vertex resolving neighborhood with total weight \(k\), the two displayed families are exactly the assumed inequalities, and all other resolving neighborhoods are the full vertex set of total weight \(rk/2\ge k\). Hence the conditions are sufficient.

For the uniqueness statement when \(r=4\), let
\[
A=\sum_i\alpha_i,
\qquad \beta_i=\frac{k}{2}-\alpha_i.
\]
The two cross inequalities become
\[
2\alpha_i\le A-\frac{k}{2},
\qquad
2\alpha_i\ge A-\frac{k}{2}.
\]
Thus all \(\alpha_i\) are equal. Summing gives \(A=k\), hence
\[
\alpha_i=\beta_i=\frac{k}{4}.
\]
At \(k=4\), every page sum equals \(2\), and the box constraints \(0\le g\le1\) force both internal weights on every page to equal \(1\), proving uniqueness for all \(r\ge4\).

Finally, for \(r\ge6\) and \(1\le k\le2\), choose any integer \(m\) with \(3\le m\le r-3\). Put
\[
(\alpha_i,\beta_i)=\left(\frac{k}{2},0\right)
\]
on \(m\) pages and
\[
(\alpha_i,\beta_i)=\left(0,\frac{k}{2}\right)
\]
on the remaining pages. The two cross inequalities hold exactly because both page classes have size at least three. These are asymmetric minima.

## Verification
The included checker constructs \(B_r\), computes all-pairs shortest-path distances, and reconstructs every resolving neighborhood directly from the definition.

For every \(4\le r\le10\), it verifies the complete resolving-neighborhood table and \(\kappa(B_r)=4\). It then checks the summed page-pair lower-bound certificate, verifies the uniform optimum for seven rational values of \(k\) between \(1\) and \(4\), replays the \(r=4\) uniqueness algebra exactly, and checks explicit asymmetric optima for \(r\ge6\) and \(k\le2\).

## Relationship to prior work
The 2017 paper introducing fractional \(k\)-metric dimension proves the general inequality
\[
\dim_f^k(G)\ge k\dim_f(G)
\]
and gives a sufficient condition for equality. It determines the scalar parameter for several graph classes, including trees, cycles, wheels, the Petersen graph, bouquets of cycles, complete multipartite graphs, and grids. Targeted inspection found no book or generalized-theta treatment.

The older fractional-metric literature contains Cartesian-product bounds. Since
\[
B_r\cong K_{1,r}\square K_2,
\]
those bounds already imply the scalar \(k=1\) value \(\dim_f(B_r)=r/2\) for \(r\ge4\). Combined with the general proportionality criterion and the uniform weight-\(1/4\) resolving function, prior theory can also recover the scalar formula \(rk/2\). The new content here is therefore not merely that value: it is the exact characterization of every minimum fractional \(k\)-resolving function, including the uniqueness regimes and explicit asymmetric optima.

## Limitations
The theorem is stated for square-page books with \(r\ge4\). The smaller books have different resolving-neighborhood minima and are not included. No claim is made for triangular books, longer-cycle books, or arbitrary generalized theta graphs. The finite verifier corroborates the symbolic argument but is not the proof of the all-parameter theorem. Literature search cannot exclude a differently named or non-indexed optimizer classification.

## References
1. C. X. Kang, I. G. Yero, E. Yi, “The fractional \(k\)-metric dimension of graphs,” arXiv:1706.05550v1, 17 June 2017; Applicable Analysis and Discrete Mathematics 13 (2019), 203–223, DOI 10.2298/AADM170712023K.
2. M. Feng, B. Lv, K. Wang, “On the fractional metric dimension of graphs,” arXiv:1112.2106v1, 9 December 2011; Discrete Applied Mathematics 170 (2014), 55–63, DOI 10.1016/j.dam.2014.01.006.

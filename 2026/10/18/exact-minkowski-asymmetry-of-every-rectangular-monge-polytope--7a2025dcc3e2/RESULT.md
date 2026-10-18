# Exact Minkowski asymmetry of every rectangular Monge polytope

## Finding
For any integers \(p,q\ge2\), let \(\mathcal M_{p,q}\) consist of all nonnegative real \(p\)-by-\(q\) matrices \(X=(x_{rs})\) with \(\sum_{r,s}x_{rs}=1\) and
\[
x_{ij}+x_{i+1,j+1}\le x_{i,j+1}+x_{i+1,j}
\quad(1\le i<p,\ 1\le j<q).
\]
The Minkowski asymmetry, defined by
\[
s(P)=\min_{c\in P}\inf\{s\ge1:-(P-c)\subseteq s(P-c)\},
\]
satisfies the exact formula
\[
\boxed{s(\mathcal M_{p,q})=\min(p,q)\,[\max(p,q)-1].}
\]
This is a complete affine-invariant classification, not a bound or an asymptotic statement. In the affine dimension \(pq-1\), the deficit from the universal simplex upper bound is precisely \(\min(p,q)-1\).

For \(p\le q\), put \(A_{ij}=i(q-j)\), \(B_{ij}=(p-i)j\), and \(w_{ij}=\min(A_{ij},B_{ij})\) for \(1\le i<p\), \(1\le j<q\). Let \(R^+_{ij}\) be the indicator matrix of the northeast rectangle \(\{1,\ldots,i\}\times\{j+1,\ldots,q\}\), and \(R^-_{ij}\) the indicator of the southwest rectangle \(\{i+1,\ldots,p\}\times\{1,\ldots,j\}\). Define
\[
V_{ij}=\begin{cases}
R^+_{ij}/A_{ij},&A_{ij}<B_{ij},\\
R^-_{ij}/B_{ij},&B_{ij}<A_{ij},\\
(R^+_{ij}+R^-_{ij})/(2w_{ij}),&A_{ij}=B_{ij}.
\end{cases}
\]
With \(J\) the all-ones matrix and \(T=p(q-1)+1\), one explicit minimizing center is
\[
\boxed{c_* =\frac1T\left(\frac{J}{p}+\sum_{i=1}^{p-1}\sum_{j=1}^{q-1}V_{ij}\right).}
\]
For \(p>q\), transpose this formula. No assertion of uniqueness of the center is made.

## Assumptions and scope
All matrices are real, normalized by the sum of their entries, and use the *nonnegative-cost* Monge convention displayed above, not the inverse-Monge convention or the distinct Kantorovich/transportation polytope. Both dimensions are at least two. The Monge inequalities for adjacent rows and columns are equivalent to all standard Monge inequalities; the source provides their full-dimensional facet description. Each \(V_{ij}\) is a normalized nonnegative Monge matrix, so the displayed \(c_*\) belongs to \(\mathcal M_{p,q}\).

For a homogeneous affine-facet slack \(h\ge0\) on a polytope with \(\min_P h=0\), the inclusion \(-(P-c)\subseteq s(P-c)\) is equivalent to \((s+1)h(c)\ge\max_P h\). We apply this equivalence to all coordinate slacks and adjacent Monge slacks. Transposition exchanges \(p\) and \(q\) and preserves asymmetry, so the proof assumes \(2\le p\le q\).

## Proof
**1. Exact facet maxima.** The vertices are normalized indicators of northeast corner rectangles, southwest corner rectangles, single entire rows, and single entire columns (Erickson–Kretschmann, Proposition 5.1). Their defining facets are \(x_{rs}\ge0\) and the adjacent Monge inequalities (Theorem 5.3). Define the adjacent slack
\[
h_{ij}(X)=x_{i,j+1}+x_{i+1,j}-x_{ij}-x_{i+1,j+1}.
\]
A normalized northeast or southwest corner rectangle contributes positive \(h_{ij}\) at exactly its own corner cut; a row or column strip contributes zero at every cut. Consequently
\[
\max_{X\in\mathcal M_{p,q}}h_{ij}(X)=\max\{1/A_{ij},1/B_{ij}\}=1/w_{ij}.
\]
For a fixed coordinate \((r,s)\), the maximum is the larger of \(1/p\), \(1/q\), the reciprocal area \(1/[r(q-s+1)]\) when a northeast corner rectangle can contain that cell, and the reciprocal area \(1/[(p-r+1)s]\) when a southwest rectangle can contain it. Missing rectangle types are omitted. As \(p\le q\), \(1/p\ge1/q\).

**2. Primal center certificate.** Put \(Y=J/p+\sum V_{ij}\). Each \(V_{ij}\) has entry sum one, hence \(\sum_{r,s}Y_{rs}=q+(p-1)(q-1)=T\). Every adjacent slack is exactly \(h_{ij}(Y)=1/w_{ij}\), thus equals its facet maximum.

We verify coordinate facets, including the tie case. Every entry of \(Y\) is at least \(1/p\). Suppose a northeast rectangle gives a larger coordinate value at \((r,s)\), i.e. \(A=r(q-s+1)<p\), with \(r<p\) and \(s>1\). Write \(b=q-s+1\). Since \(rb\le p-1\) and \(r(p-r)\ge p-1\), one has \(b\le p-r\). Then
\[
(p-r)(s-1)-rb=(p-r)q-pb\ge p(p-r-b)\ge0.
\]
Therefore the northeast rectangle at cut \((r,s-1)\) has area no greater than its southwest competitor. If strictly smaller, its entire normalized vertex occurs in \(Y\), giving \(Y_{rs}\ge1/A\). If the areas tie, \(A=rb=(q/p)r(p-r)\ge p-1\ge p/2\); the half-weight northeast term together with \(J/p\) gives \(Y_{rs}\ge1/p+1/(2A)\ge1/A\). The southwest case is symmetric in the two corners: a southwest rectangle of area \(B=(p-r+1)s<p\) satisfies \(s\le r-1\), so at cut \((r-1,s)\) the southwest area is no larger than the northeast area; an area tie similarly has \(B\ge p/2\). Thus \(Y_{rs}\) dominates **every** coordinate-facet maximum. Because all facet maxima are attained, \(c_*=Y/T\) satisfies \(T h(c_*)\ge\max h\) for every facet, and hence
\[
s(\mathcal M_{p,q})\le T-1=p(q-1).
\]

**3. Dual lower-bound certificate.** For \(0\le i\le p\) and \(0\le j\le q\), extend \(w_{ij}=\min\{i(q-j),(p-i)j\}\) to the boundary, where it vanishes. Set
\[
\lambda_{rs}=1+w_{rs}-w_{r,s-1}-w_{r-1,s}+w_{r-1,s-1}
\quad(1\le r\le p,\ 1\le s\le q).
\]
These coefficients are nonnegative. Indeed \(w_{ij}=i(q-j)-(iq-pj)_+\), and for \(u_{ij}=(iq-pj)_+\) one has \(\lambda_{rs}=u_{r,s-1}+u_{r-1,s}-u_{r,s}-u_{r-1,s-1}\ge0\), because the increment \(u_{r,j}-u_{r-1,j}\) is nonincreasing in \(j\). Direct coefficient collection gives the identity, valid for **every** real matrix \(Z\),
\[
\sum_{r,s}Z_{rs}=\sum_{r,s}\lambda_{rs}Z_{rs}
+\sum_{i=1}^{p-1}\sum_{j=1}^{q-1}w_{ij}h_{ij}(Z).
\]
Putting \(Z=J\) shows \(\sum\lambda_{rs}=pq\). If \(c\) is any Minkowski center with asymmetry at most \(s\), let \(Z=(s+1)c\). Each coordinate maximum is at least \(1/p\) (a complete-column vertex), so \(Z_{rs}\ge1/p\), and all adjacent slacks satisfy \(h_{ij}(Z)\ge1/w_{ij}\). The coefficient identity yields
\[
s+1=\sum Z_{rs}\ge\frac1p\sum\lambda_{rs}
+\sum_{i,j}w_{ij}\frac1{w_{ij}}
=q+(p-1)(q-1)=T.
\]
Hence \(s\ge p(q-1)\), matching the constructed center. Transposition proves the general formula.

## Verification
The included standalone script `verify_monge_asymmetry.py` uses exact rational arithmetic and independently regenerates all published vertex types, all facet maxima, the primal weighted-rectangle center, the dual nonnegative coefficients, and the dual identity on each ambient coordinate basis vector. Running `python3 verify_monge_asymmetry.py` checks all 60 dimension pairs \(2\le p\le9\), \(p\le q\le12\), encountering 4,452 explicit vertices and 4,392 facet inequalities. The exact verifier passed. These tests are finite corroboration; the proof above establishes every integer pair.

## Relationship to prior work
Erickson and Kretschmann [1] define the normalized generic Monge polytope, give its complete vertex/facet descriptions in Proposition 5.1 and Theorem 5.3, and compute its combinatorial edges and selected volumes. Those statements supply the input to our facet-maxima calculation but do not state the affine symmetry invariant, the dual weights \(w_{ij}\), or the optimal-center construction. Erickson and Jones [2] later give a volume/Ehrhart treatment of the same polytope using Delannoy paths; volume/Ehrhart formulas do not imply the Minkowski asymmetry or its minimizing center. This result instead converts the complete facet system into matching positive primal and dual certificates. The result is distinct from Euclidean inradius/incenter questions: the invariant and its optimization are affine, not metric.

## Limitations
The theorem does not classify every minimizing center, assert center uniqueness, or extend to inverse-Monge or unnormalized unbounded cones. Its bibliographic originality assessment is based on inspected relevant primary material and searches rather than an independent comprehensive priority certification. A general theorem elsewhere expressed under an equivalent submodular-grid or polyhedral asymmetry formulation might subsume the formula; no such dominating result was identified in the inspected sources. The proof uses the established full vertex/facet classification of the normalized Monge polytope and independently verifies the new inequalities and certificates.

## References
[1] W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, version 2, 2023. Original submission November 13, 2023. Relevant: Sections 1 and 5, Proposition 5.1, Theorem 5.3. https://arxiv.org/abs/2311.07522

[2] W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, 2026. Relevant: introduction and main-result statement on volume/Ehrhart series. https://arxiv.org/abs/2609.09508

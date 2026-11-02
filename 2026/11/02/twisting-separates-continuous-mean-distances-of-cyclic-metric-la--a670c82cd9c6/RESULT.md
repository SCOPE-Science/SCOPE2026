# Twisting separates continuous mean distances of cyclic metric ladders

## Finding
For each integer \(n\ge3\), give every edge of the two connected cubic graphs
\[
P_n=C_n\mathbin{\square}K_2,\qquad
M_{2n}=C_{2n}+\{\{i,i+n\}:0\le i<n\}
\]
unit length and their intrinsic shortest-path metrics. The second graph is the Möbius ladder obtained by attaching antipodal rungs to the length-\(2n\) cycle; the first is the circular prism ladder. Each has exactly \(3n\) edges and total arclength \(3n\). Independently choose two points uniformly from the total edge arclength, and denote their distances by \(D_P,D_M\).

**Theorem.** Their exact means are
\[
\mathbb E D_P=\frac n4+\frac{14}{27}+
\begin{cases}\frac1{27n},&n\text{ even},\\\frac1{108n},&n\text{ odd},\end{cases}
\qquad
\mathbb E D_M=\frac n4+\frac{14}{27}-
\begin{cases}\frac7{54n},&n\text{ even},\\\frac5{36n},&n\text{ odd}.\end{cases}
\]
Hence twisting strictly reduces the continuous mean distance, with the **exact sharp gap**
\[
\boxed{\mathbb E D_P-\mathbb E D_M=
\begin{cases}\frac1{6n},&n\text{ even},\\\frac4{27n},&n\text{ odd}.\end{cases}}
\]
For comparison, if points are sampled uniformly from vertices (including coincident ordered pairs), the discrete means satisfy
\[
\boxed{\mathbb E d_P(U,V)-\mathbb E d_M(U,V)=
\begin{cases}\frac1{2n},&n\text{ even},\\0,&n\text{ odd}.\end{cases}}
\]
Thus **odd-rung prisms and Möbius ladders are indistinguishable by their vertex-average distance but are strictly distinguished by their continuous arclength-average distance**. For even rung counts the continuous gap is exactly one third of the vertex-average gap. All formulas include every edge-interior point.

## Assumptions and scope
Edges are *intervals of length one*, with points on different edges identified only at common vertices. For vertices, sample independently and uniformly with replacement. For continuous sampling, use the probability measure given by arclength divided by \(3n\); vertices have measure zero. Each \(n\) is an integer with \(n\ge3\), and no planar embedding or extrinsic Euclidean metric is used. The notation \(M_{2n}\) refers only to the standard cubic, even-order Möbius ladder, not the degree-four graph sometimes called an odd Möbius ladder.

Call the \(2n\) edges of the original rim(s) **horizontal** and the \(n\) remaining edges **rungs**. An independent uniform point lies on a horizontal edge with probability \(2/3\), on a rung with probability \(1/3\). Accordingly, if \(H\!H,H\!V,V\!V\) are the three conditional mean distances (using ordered sampling), the total mean is
\[
\mu=\frac49\mu_{HH}+\frac49\mu_{HV}+\frac19\mu_{VV}.
\]

## Proof
### 1. Elementary integrals and circle mean
For independent \(U,V\sim\mathrm{Unif}[0,1]\), direct integration gives
\[
\mathbb E|U-V|=\frac13,\qquad
\mathbb E\min(U+V,2-U-V)=\frac23,
\]
\[
\mathbb E\max(|U+V-1|,|U-V|)=\frac12.
\]
The last identity follows from \(\max(|U+V-1|,|U-V|)=|U-1/2|+|V-1/2|\). The geodesic distance between two independent arclength-uniform points on a circle of circumference \(L\) has mean \(L/4\). The distance between two independent uniformly sampled vertices of an \(n\)-cycle has mean
\[
c_n=\frac n4-\frac{\varepsilon_n}{4n},\quad
\varepsilon_n=\begin{cases}1,&n\text{ odd},\\0,&n\text{ even}.\end{cases}
\]
These formulas apply without asymptotic approximations.

### 2. Untwisted circular ladder
For points on two horizontal edges, the same-layer case is exactly the length-\(n\) circle and has mean \(n/4\). The two layers occur equally often. For different layers, a shortest path must cross a rung. Usually a rung lies on a shortest projected circle arc, giving distance \(1+d_{C_n}(x,y)\). An exception occurs exactly when the projected points are in the same unit edge (probability \(1/n\)): a detour to an endpoint raises the mean horizontal component from \(\mathbb E|U-V|=1/3\) to \(\mathbb E\min(U+V,2-U-V)=2/3\). The different-layer mean is therefore \(1+n/4+1/(3n)\), and
\[
\mu_{HH}^{P}=\frac n4+\frac12+\frac1{6n}.
\]
For a horizontal point and a rung point, go along the first point's rim to the rung vertex, then a uniform mean distance of \(1/2\) along the rung. The projected horizontal point is uniform on the circle, whence
\[
\mu_{HV}^{P}=\frac n4+\frac12.
\]
For distinct rungs rooted at cycle vertices \(i,j\), the distance equals \(d_{C_n}(i,j)+\min(U+V,2-U-V)\). On the same rung the correct distance is \(|U-V|\), not the latter expression. The diagonal has probability \(1/n\). Hence
\[
\mu_{VV}^{P}=c_n+\frac23-\frac1{3n}.
\]
These expressions are exact, including the triangular case \(n=3\).

### 3. Twisted horizontal–horizontal distances
Identify the horizontal rim of \(M_{2n}\) with a circle of circumference \(2n\), marked by its integer vertices. A shortest path between two horizontal points can use **at most one rung**: any pair of rung traversals can be removed while replacing the intervening horizontal arc by its antipodal translate, saving two units. Let \(A\) denote the shorter circle distance between independent uniform horizontal points \(X,Y\). Then \(A\sim\mathrm{Unif}[0,n]\), and the antipodal-shifted circle distance is \(n-A\). If a shortest shifted circle arc contains an integer vertex, a rung can be placed there and the network distance is
\[
\min(A,n+1-A).
\]
This applies except when \(Y\) and the antipodal shift \(X+n\) lie in the **same elementary horizontal edge**, an event of probability \(1/(2n)\). In that event, with fractional edge coordinates \(U,V\), the ideal rung route \(1+|U-V|\) is unavailable; the actual shortest rung route is \(1+\min(U+V,2-U-V)\). For \(n\ge3\) that rung route never exceeds the direct circular route, so the correction in conditional expectation is exactly \(1/3\). Finally,
\[
\frac1n\int_0^n\min(a,n+1-a)\,da
=\frac n4+\frac12-\frac1{4n}.
\]
Applying the correction yields
\[
\mu_{HH}^{M}=\frac n4+\frac12-\frac1{4n}+\frac1{2n}\cdot\frac13
=\frac n4+\frac12-\frac1{12n}.
\]

### 4. Twisted horizontal–rung distances
By translation and antipodal symmetry fix the rung between horizontal coordinates \(0\) and \(n\). Put its point at coordinate \(V\in[0,1]\), and let \(x\) be a uniform point in \([0,n]\) on half of the horizontal rim; the other half has the same expected distance. The network distances from \(x\) to the rung endpoints are
\[
a(x)=\min(x,n-x+1),\quad b(x)=\min(n-x,x+1).
\]
The point-to-rung distance is \(\min(a(x)+V,b(x)+1-V)\). For \(0\le x\le(n-1)/2\) its average in \(V\) is \(x+1/2\); for \((n+1)/2\le x\le n\) it is \(n-x+1/2\). In the central interval, writing \(w=x-n/2\in[-1/2,1/2]\), it is \(n/2+1/4-w^2\). Integrating gives
\[
\mu_{HV}^{M}=\frac1n\left[2\int_0^{(n-1)/2}(x+1/2)\,dx
+\int_{-1/2}^{1/2}(n/2+1/4-w^2)\,dw\right]
=\frac n4+\frac12-\frac1{12n}.
\]
In particular, the twisted ladder has the exact (not generally edge-transitivity-based) identity \(\mu_{HH}^{M}=\mu_{HV}^{M}\).

### 5. Twisted rung–rung distances
Fix two rungs whose root indices differ by \(k\in\{0,\ldots,n-1\}\). For distinct rungs, the endpoint-distance matrix has the form
\[
\begin{pmatrix}a_k&b_k\\b_k&a_k\end{pmatrix},\qquad
a_k=\min(k,n-k+1),\quad b_k=\min(n-k,k+1).
\]
The values differ by one except when \(n\) is even and \(k=n/2\), when they are equal. If they differ by one, one pair of endpoint routes always dominates the other, so the average distance is \(\min(a_k,b_k)+2/3\). At the even central tie it is \(a_k+1/2\), a deficit of \(1/6\). For coincident rungs (probability \(1/n\)), their mean distance is \(1/3\), a deficit of \(1/3\) from the generic value. Since \(\min(a_k,b_k)=\min(k,n-k)\), averaging the root-index difference gives \(c_n\). Thus, with \(\eta_n=1-\varepsilon_n\),
\[
\mu_{VV}^{M}=c_n+\frac23-\frac1{3n}-\frac{\eta_n}{6n}.
\]

### 6. Aggregation and the discrete comparison
Substituting the three conditional means in \(\mu=(4\mu_{HH}+4\mu_{HV}+\mu_{VV})/9\) gives the two displayed continuous mean formulas and their positive gap for all \(n\ge3\). For vertices of the untwisted graph, distance is a cycle distance plus the indicator of differing layers, so its mean is \(c_n+1/2\). For vertices of the twisted graph, the distance from vertex \(0\) to vertex \(j\), writing \(\delta=\min(j,2n-j)\), is \(\min(\delta,n-\delta+1)\). Summing this expression over \(j=0,\ldots,2n-1\) gives \(c_n+1/2\) when \(n\) is odd and \(c_n+1/2-1/(2n)\) when \(n\) is even. This establishes the vertex comparison, finishing the proof.

## Verification
The accompanying standalone `verify_ladder_mean.py` uses only the Python standard library. It constructs each graph, obtains shortest vertex distances by breadth-first search, and integrates the exact minimum of the four affine endpoint-route distances for every **ordered pair of distinct edges**. The unit-edge diagonal uses \(\mathbb E|U-V|=1/3\). Rational polygon clipping and centroid integration are exact, using `fractions.Fraction` throughout. For each \(n=3,\ldots,18\), it independently compares the horizontal–horizontal, horizontal–rung, rung–rung, total continuous mean, and discrete vertex mean for both graphs against the closed formulas, then compares both gaps: 192 exact rational assertions passed. These are finite consistency tests; the proof above establishes the unrestricted integer range.

## Relationship to prior work
Guy and Harary introduced the Möbius ladder and studied its planar crossing number, not its continuous intrinsic mean distance [1]. Doyle and Graver studied continuous mean distance of selected network shapes [2]. Bose and collaborators studied farthest-point diagrams for edge-continuous network metrics [3]. Garijo, Márquez, and Silveira gave a general algorithm for computing the continuous mean on arbitrary weighted finite graphs, and explicit results for trees, cactus graphs, and complete graphs [4]. Baptista, Kennedy, and Mugnolo established broad metric-graph inequalities and explicit star, flower, and firework examples [5]. These results motivate the invariant and give algorithms or bounds, but the inspected material did not state the all-\(n\) Möbius-ladder mean formula or the exact parity-dependent twist gap. The untwisted prism mean formula is presented to state the comparison and is not independently claimed as new. General computability for each fixed \(n\) should not be confused with the closed all-parameter identity or the odd-parity distinction between vertex and arclength sampling.

## Limitations
All edges have the same positive length (normalized to one); the statement does not cover arbitrary edge weights. Only first moments are determined, not a stochastic ordering of the full distance distributions. Discrete sampling means uniform independent vertices with replacement. Historical priority is not mathematically certifiable by search; [2] was not inspected in full, and older literature may contain equivalent formulas. The 2013-04-06 bibliographic date supplied in structured metadata is the earliest **day-resolved** public source date verified for the continuous-network research anchor [3]; earlier foundational publications [1] and [2] have year/month evidence but not an independently verified first-public day. No assertion is made that the earliest historical publication of a network-distance concept was in 2013.

## References
[1] R. K. Guy and F. Harary, *On the Möbius Ladders*, Canadian Mathematical Bulletin 10(4), 493–496 (1967), doi:10.4153/CMB-1967-046-4.

[2] J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B: Planning and Design 9 (1982), doi:10.1068/b090177.

[3] P. Bose, K. Dannies, J.-L. De Carufel, C. Doell, C. Grimm, A. Maheshwari, S. Schirra and M. Smid, *Network Farthest-Point Diagrams*, arXiv:1304.1909v1 (first public 2013-04-06); Journal of Computational Geometry 4(1), 182–211 (2013).

[4] D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, arXiv:2103.11676v1 (2021); Results in Mathematics 78, 139 (2023), doi:10.1007/s00025-023-01902-w.

[5] L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean Distance on Metric Graphs*, arXiv:2312.04952v1 (2023); Journal of Geometric Analysis 34, 137 (2024), doi:10.1007/s12220-024-01574-0.

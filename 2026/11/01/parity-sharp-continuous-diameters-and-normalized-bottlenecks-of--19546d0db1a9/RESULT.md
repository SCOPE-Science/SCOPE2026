# Parity-sharp continuous diameters and normalized bottlenecks of metric wheel networks

## Finding

Let \(W_n(s)\) be a symmetric metric wheel of rim order \(n\ge3\): its rim is a cycle with \(n\) edges of length \(1\), and its hub joins each rim vertex by an edge of length \(s>0\). Distances are shortest-path lengths in the *entire continuous network*, including points inside each edge. Let \(D_n(s)\) denote its intrinsic diameter. Set

\[
m=\lfloor n/2\rfloor,\qquad M=\lceil n/2\rceil,
\qquad B_n(s)=\min\{2s+\tfrac12,\ s+\tfrac M2\}.
\]

Define

\[
A_n(s)=\begin{cases}
\min\{n/2,\,2s+1\},&n\text{ even},\\
\min\{n/2,\,2s+1,\,s+(n+1)/4\},&n\text{ odd}.
\end{cases}
\]

**Exact continuous diameter.** For every indicated \(n,s\),

\[
\boxed{D_n(s)=\max\{A_n(s),\,B_n(s)\}.}
\]

The total network length is \(\mathcal L_n(s)=n(1+s)\). **Sharp normalized diameter and its equality cases** are

\[
\boxed{
\sup_{s>0}\frac{D_n(s)}{n(1+s)}=
\begin{cases}
\tfrac13,&n=3,\\
\tfrac{2}{n+2},&n\ge4\text{ even},\\
\tfrac{2(n-1)}{n(n+1)},&n\ge5\text{ odd}.
\end{cases}}
\]

For \(n=3\), every \(s>0\) attains the bound. For even \(n\ge4\), the unique maximizing value is \(s=(n-2)/4\). For odd \(n\ge5\), the unique maximizing value is \(s=(n-3)/4\). Thus the worst-case distance divided by total network length has a strict order-parity effect and sharp spoke-to-rim transitions.

## Assumptions and scope

All edges are positive-length closed intervals with endpoints identified according to the combinatorial wheel. The rim vertices are labelled cyclically, the rim total length is \(n\), and the spoke lengths are all exactly \(s\). Paths are allowed through the hub or around the rim. The diameter is the maximum over *arbitrary points* in the graph, not merely its finite vertex set. Rotation symmetry and uniform scaling of all lengths do not change the normalized statement. No Euclidean embedding or straight-line realizability of the spokes is assumed.

For a rim point \(x\), let \(\delta(x)\in[0,1/2]\) be its rim distance to the nearest rim vertex. Let \(d_C\) denote shortest arclength distance on the rim cycle before the spoke shortcuts are considered.

## Proof

**1. Distances between rim points.** For rim points \(x,y\), every shortest path either stays on the rim or enters the hub exactly once. The latter route travels from \(x\) to a nearest rim vertex, traverses two spokes, and returns along the rim to \(y\). Hence

\[
d_W(x,y)=\min\{d_C(x,y),\ 2s+\delta(x)+\delta(y)\}.
\tag{1}
\]

If \(n=2m\) is even, the two terms in (1) are bounded respectively by \(m\) and \(2s+1\). Midpoints of diametrically opposite rim edges achieve \(d_C=m\) and \(\delta(x)+\delta(y)=1\); this proves that the maximum over rim-point pairs is exactly \(A_n(s)=\min\{m,2s+1\}\).

If \(n=2m+1\) is odd, still \(d_C\le m+1/2\) and \(\delta(x)+\delta(y)\le1\). Furthermore the midpoints of the rim edges containing \(x,y\) are at circular distance at most \(m\), while \(x,y\) are at distances \(1/2-\delta(x)\) and \(1/2-\delta(y)\) from these midpoints. The triangle inequality gives

\[
d_C(x,y)+\delta(x)+\delta(y)\le m+1.
\tag{2}
\]

Combining (1), (2), and \(\min\{a,b\}\le(a+b)/2\) yields

\[
d_W(x,y)\le \min\{m+1/2,\ 2s+1,\ s+(m+1)/2\}.
\tag{3}
\]

This bound is attained throughout all three regimes. Parametrize the rim by cyclic arclength modulo \(2m+1\), take \(x=1/2\) and \(y=m+1/2+t\) with \(0\le t\le1/2\). Then \(d_C(x,y)=m+t\) and \(\delta(x)+\delta(y)=1-t\), so (1) becomes

\[
d_W(x,y)=\min\{m+t,\ 2s+1-t\}.
\tag{4}
\]

For \(0<s\le(m-1)/2\), take \(t=0\), obtaining \(2s+1\). For \((m-1)/2\le s\le m/2\), take \(t=s-(m-1)/2\), obtaining \(s+(m+1)/2\). For \(s\ge m/2\), take \(t=1/2\), obtaining \(m+1/2\). The first regime is empty if \(m=1\). This proves the odd formula for \(A_n(s)\), including regime boundaries.

**2. A rim point and a spoke point.** Fix spoke endpoint \(v\) on the rim, and let \(z\) lie on that spoke at distance \(t\in[0,s]\) from the hub. For a rim point \(x\), write \(r=d_C(v,x)\) and \(\delta=\delta(x)\). A shortest path either comes from the hub or from \(v\), giving

\[
d_W(z,x)=\min\{t+s+\delta,\ s-t+r\}.
\tag{5}
\]

Every rim-edge midpoint is within rim distance \(M-1/2\) of \(v\). Moving from that midpoint to \(x\) requires distance \(1/2-\delta\), hence \(r+\delta\le M\). Since \(\delta\le1/2\), \(t\le s\), (5) gives

\[
d_W(z,x)\le\min\{2s+1/2,\ s+M/2\}=B_n(s).
\tag{6}
\]

Both bounds are sharp simultaneously at the relevant branch. Choose \(x\) to be the midpoint of a rim edge at distance \(M-1/2\) from \(v\). This gives \(r=M-1/2\) and \(\delta=1/2\). Choose \(t=\min\{s,(M-1)/2\}\). Substitution in (5) yields exactly \(B_n(s)\).

**3. Two spoke points.** On distinct spokes, let their distances from the hub be \(t,u\in[0,s]\), and let the rim distance between their endpoints be \(k\le m\). The only competitive simple routes are through the hub and through the rim, so

\[
d_W(z,z')=\min\{t+u,\ 2s-t-u+k\}
\le\min\{2s,\ s+k/2\}\le B_n(s).
\tag{7}
\]

For points on a common spoke, the distance is at most \(s<B_n(s)\). Thus the global diameter is the larger of the rim--rim and rim--spoke maxima from steps 1 and 2, proving the first boxed formula.

**4. Sharp normalization.** For \(n=2m\ge4\), write \(s_0=(m-1)/2\). Then \(A_n(s)=2s+1\) up to \(s_0\), after which \(A_n(s)=m\). Consequently \(A_n(s)/[n(1+s)]\) strictly increases to \(s_0\) and strictly decreases afterward; its maximum is \(1/(m+1)=2/(n+2)\). The two branches of \(B_n(s)\) cross at the same \(s_0\). Its normalized maximum is \((m-1/2)/[m(m+1)]\), strictly smaller than \(1/(m+1)\); when \(m=2\), the upper branch is constant after the crossing but remains below that value. Therefore the stated even-order maximizer is unique.

For \(n=2m+1\ge5\), set \(s_0=(m-1)/2\), \(s_1=m/2\). The rim--rim value \(A_n(s)\) equals \(2s+1\) up to \(s_0\), equals \(s+(m+1)/2\) between \(s_0,s_1\), and equals \(m+1/2\) above \(s_1\). Its normalized ratio strictly rises then strictly falls; at the unique maximum \(s_0\) it equals \(2m/[(2m+1)(m+1)]\). The normalized \(B_n(s)\) peaks at \(s_1\), with value \(1/(m+2)\). The strict comparison

\[
\frac{2m}{(2m+1)(m+1)}-\frac1{m+2}
=\frac{m-1}{(2m+1)(m+1)(m+2)}>0
\tag{8}
\]

shows the rim--rim maximum controls the global normalized optimum. If \(n=3\), direct substitution in the exact diameter formula gives \(D_3(s)=1+s\) identically. The sharp result and every equality case follow.

## Verification

The standalone Python 3 standard-library program `verify_wheel.py` independently constructs the metric graph for rational spoke lengths, computes shortest distances between vertices, and maximizes each pair-of-edge continuous-distance function over its exact rational polyhedral breakpoint set. It does not rely on the proved expressions when computing actual diameters. The checked output is:

```
PASS: 80 exactly enumerated parameter cases (n=3,...,11), independent path-pair maximization.
PASS: claimed sharp normalized peaks and equality witnesses.
LIMIT: finite cases are NOT an infinite proof; see the analytical argument.
```

Run `python3 verify_wheel.py` using only Python's standard library. The finite check also covers spoke-length transition values. The universal claims rest on (1)--(8), not numerical enumeration.

## Relationship to prior work

Bose and collaborators (2013) study shortest-path distances and farthest-point data structures for arbitrary continuous networks; their work defines the same all-edge-point diameter setting but does not give the parameterized wheel formula or its sharp normalized optimization. De Carufel and collaborators (2015) minimize continuous diameter by adding shortcuts to paths and cycles; their feasible networks and optimization target differ from a fixed wheel with \(n\) equal spokes. Ahn and collaborators (2026) prove general inequalities between metric-graph total length, cyclomatic number, and diameter; those inequalities do not determine the explicit wheel diameter or the maximizing spoke length. Classical descriptions of the *vertex-only* wheel graph diameter omit the potentially diametral edge-interior points.

The 1982 article by Chen and Garfinkel on generalized graph diameter predates the other references and is potentially relevant. Its bibliographic identification is verified, but its full text could not be materially examined; consequently an earlier occurrence of this specialization cannot be excluded. No priority claim is based on a failed title or keyword search.

## Limitations

The exact formula assumes all rim edges have equal length and all spokes have the same positive length. It does not classify arbitrary edge-weighted wheels or give the complete locus of diametral point pairs. The normalized extremum is a **maximum** of worst-case distance per unit length within this prescribed symmetric family, not an optimization over all graphs of the same cyclomatic number. Material access to the 1982 generalized-diameter paper remains incomplete. Finite verification alone cannot prove the infinite theorem.

## References

- P. Bose, K. Dannies, J.-L. De Carufel, C. Doell, C. Grimm, A. Maheshwari, S. Schirra, and M. Smid, *Network Farthest-Point Diagrams and their Application to Feed-Link Network Extension*, arXiv:1304.1909v1, first public 2013-04-06. https://arxiv.org/abs/1304.1909
- J.-L. De Carufel, C. Grimm, A. Maheshwari, and M. Smid, *Minimizing the Continuous Diameter when Augmenting Paths and Cycles with Shortcuts*, arXiv:1512.02257v1, first public 2015-12-07. https://arxiv.org/abs/1512.02257
- H.-K. Ahn, S. Cabello, O. Cheong, D. Garijo, and J. Moon, *Diameter and Length of Metric Graphs*, arXiv:2608.08716v1, first public 2026-08-09. https://arxiv.org/abs/2608.08716
- C. K. E. Chen and R. S. Garfinkel, *The generalized diameter of a graph*, Networks 12 (1982), 335--340. DOI 10.1002/net.3230120310. Historical coverage unresolved because full text was not accessible.

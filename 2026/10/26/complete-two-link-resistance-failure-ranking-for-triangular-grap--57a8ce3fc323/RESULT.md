# Complete two-link resistance-failure ranking for triangular graphs

## Finding

Let \(n\ge5\) be an integer, and let the triangular (Johnson) graph \(T(n)=J(n,2)\) have the \(\binom n2\) unordered pairs from \([n]\) as vertices, with two vertices adjacent precisely when they intersect. Every existing graph edge is a unit conductance. For distinct edges \(e,f\), define
\[
\Delta(e,f)=\operatorname{Kf}(T(n)-\{e,f\})-\operatorname{Kf}(T(n)),
\]
where \(\operatorname{Kf}\) is the sum of effective resistances over all unordered vertex pairs. Every such two-edge deletion is connected.

Every unordered pair \(\{e,f\}\) belongs to exactly one of five damage classes, and the values satisfy the **strict universal order**
\[
\boxed{\Delta_{I_\triangle}>\Delta_{I_\circ}>\Delta_{D_2}>\Delta_{D_1}>\Delta_{D_0}.}
\]
The types are: \(I_\triangle\), two incident edges completing a triangle; \(I_\circ\), two incident edges whose other endpoints are nonadjacent; \(D_j\), two vertex-disjoint graph edges whose underlying two-element changing sets have intersection size \(j\), for \(j=2,1,0\). Here the changing set of \(\{\{a,b\},\{a,c\}\}\) is \(\{b,c\}\), independent of the orientation.

The number of unordered failed-edge pairs of each class is, respectively,
\[
\begin{aligned}
M_{I_\triangle}&=\frac{n(n-1)(n-2)^2}{2},\\
M_{I_\circ}&=\frac{n(n-1)(n-2)(n-3)}{2},\\
M_{D_2}&=\frac{n(n-1)(n-2)(n-3)}{4},\\
M_{D_1}&=\frac{n(n-1)(n-2)^2(n-3)}{2},\\
M_{D_0}&=\frac{n^2(n-1)(n-2)(n-3)(n-4)}{8}.
\end{aligned}
\]
Consequently, **precisely the pairs of edges lying in a common triangle maximize the Kirchhoff-index increase**. Their number is \(n(n-1)(n-2)^2/2\). The exact maximum is
\[
\boxed{
\Delta_{\max}(n)=\frac{(n^2+3n-2)(4n^2-7n-3)}{2(n-3)(2n+1)(2n^2-3n-1)}.}
\]
These assertions hold for all integers \(n\ge5\), with no numerical or asymptotic qualification.

## Assumptions and scope

The graph is simple, unweighted and undirected; conductances are one. Deleted edges are distinct, with no restriction that their endpoints be disjoint. The relevant objective is the sum of unordered-pair effective resistances *after simultaneous removal of exactly two edges*, not edge connectivity, path length, graph energy or conditional expected failure. The triangular graph is the line graph of \(K_n\); this is a natural pairwise-interaction network whose vertices encode pairs of an underlying set. The theorem does not claim a result for other Johnson graphs, weighted variants, three failures, or arbitrary strongly regular graphs.

For completeness the five exact values have a compact common expression. Let
\[
N=\binom n2,\quad
r=\frac{n+1}{n(n-1)},\quad
s=\frac{n^2+3n-2}{2n^2(n-1)^2},
\]
and for \(k,h\in\mathbb Z\) define
\[
 c_{k,h}=\frac{nk+h}{2n(n-1)},\qquad
 t_{k,h}=\frac{n^2k+(3n-2)h}{4n^2(n-1)^2},
\]
\[
F_n(k,h)=\frac{2N\{(1-r)s+c_{k,h}t_{k,h}\}}{(1-r)^2-c_{k,h}^2}.
\]
Then the five classes, in descending order, have exact values
\[
\begin{aligned}
\Delta_{I_\triangle}&=F_n(1,1), &
\Delta_{I_\circ}&=F_n(1,0),\\
\Delta_{D_2}&=F_n(0,2), &
\Delta_{D_1}&=F_n(0,1),\\
\Delta_{D_0}&=F_n(0,0).
\end{aligned}
\]
Thus the statement specifies the full damage distribution, not only an extremal value. For example, at \(n=5\), the five values are
\[
\frac{589}{374}>\frac{751}{506}>\frac{109}{78}>\frac{2141}{1566}>\frac{19}{14}.
\]

## Proof

**1. Spectral projectors.** Index the \(N\) vertices by unordered two-element subsets. Let \(B\) be the \(n\times N\) zero-one incidence matrix, whose column for \(\{i,j\}\) is \(\mathbf e_i+\mathbf e_j\). Then \(BB^{\mathsf T}=(n-2)I+J\) and the adjacency matrix of \(T(n)\) is \(A=B^{\mathsf T}B-2I\). Since every graph vertex has degree \(2(n-2)\), its Laplacian is
\[
L=2(n-1)I-B^{\mathsf T}B.
\]
The nonzero Laplacian eigenvalues are \(n\) on the rank-\((n-1)\) subspace \(\operatorname{im} B^{\mathsf T}\cap\mathbf1^\perp\) and \(2(n-1)\) on its orthogonal complement in \(\mathbf1^\perp\). The first projector is
\[
P_1=\frac{B^{\mathsf T}(I-J/n)B}{n-2},
\]
while \(P_2=I-J/N-P_1\). Thus
\[
L^+=\frac{P_1}{n}+\frac{P_2}{2(n-1)},\qquad
(L^+)^2=\frac{P_1}{n^2}+\frac{P_2}{4(n-1)^2}.
\]

**2. Two local integer invariants determine both transfer matrices.** Orient any edge \(e\) between \(\{a,b\}\) and \(\{a,c\}\), writing its incidence dipole as \(\mathbf d_e=\mathbf e_{\{a,b\}}-\mathbf e_{\{a,c\}}\). Then \(B\mathbf d_e=\mathbf e_b-\mathbf e_c\). For another oriented edge \(f\), define
\[
k=\mathbf d_e^{\mathsf T}\mathbf d_f,
\qquad h=(B\mathbf d_e)^{\mathsf T}(B\mathbf d_f).
\]
The projector identity gives \(\mathbf d_e^{\mathsf T}P_1\mathbf d_f=h/(n-2)\), while \(\mathbf d_e^{\mathsf T}\mathbf d_f=k\). Substitution, with no approximation, gives
\[
\mathbf d_e^{\mathsf T}L^+\mathbf d_f=c_{k,h},\qquad
\mathbf d_e^{\mathsf T}(L^+)^2\mathbf d_f=t_{k,h}.
\]
For \(e=f\), \((k,h)=(2,2)\), so the diagonal entries are the constants \(r,s\) above. For two distinct edges, reverse an orientation if needed to choose one of exactly the five types \((k,h)=(1,1),(1,0),(0,2),(0,1),(0,0)\). Indeed, if the edges have a common graph endpoint then \(k=1\) and the moving sets have signed overlap \(h=1\) exactly when the other two endpoints are adjacent, otherwise \(h=0\). If the edges are graph-disjoint then \(k=0\) and the absolute overlap of the two signed moving-pair vectors is \(2,1,0\) according as their changing sets intersect in \(2,1,0\) elements. All five possibilities occur for \(n\ge5\).

**3. Connectivity and the exact rank-two update.** Put \(U=[\mathbf d_e\ \mathbf d_f]\). On the zero-sum subspace, the deleted Laplacian is \(L-UU^{\mathsf T}\). The matrix \(I-U^{\mathsf T}L^+U\) has diagonal \(1-r\) and off-diagonal \(-c_{k,h}\). Because \(n\ge5\),
\[
1-r=\frac{n^2-2n-1}{n(n-1)}>
\frac{n+1}{2n(n-1)}\ge|c_{k,h}|,
\]
so this matrix is positive definite. Consequently the deletion leaves the Laplacian positive definite on \(\mathbf1^\perp\), proving connectivity as well as the validity of the Woodbury formula
\[
(L-UU^{\mathsf T})^+=L^++L^+U(I-U^{\mathsf T}L^+U)^{-1}U^{\mathsf T}L^+.
\]
Since \(\operatorname{Kf}(G)=|V(G)|\operatorname{tr}(L_G^+)\), tracing the update gives exactly \(\Delta=F_n(k,h)\).

**4. Exhaustive class counts.** Let \(E=n(n-1)(n-2)/2\) be the number of graph edges. Every edge lies in exactly \(n-2\) triangles, so the number of triangular incident pairs is \(E(n-2)\). A vertex has degree \(2(n-2)\), and subtracting triangular wedges from \(N\binom{2(n-2)}2\) counts the incident nontriangular pairs. For \(D_2\), choose the changing pair and then two distinct centers outside it, giving \(\binom n2\binom{n-2}2\). For \(D_1\), each edge has \(2(n-2)(n-3)\) disjoint partner edges with exactly one changing label in common: choose the shared moving label, the distinct replacement label, then a center that does not create an endpoint collision. Divide the product with \(E\) by two. The remaining disjoint pairs constitute \(D_0\); subtraction from \(\binom E2\) gives its displayed formula. Every count is positive for \(n\ge5\).

**5. Strict comparisons.** Straight rational reduction gives the following positive differences, with \(n\ge5\):
\[
\begin{aligned}
\Delta_{I_\triangle}-\Delta_{I_\circ}
&=\frac{n(n-1)(4n^3-11n^2+n+4)}{(n-3)(n-2)(2n+1)(2n^2-5n-2)(2n^2-3n-1)},\\[3pt]
\Delta_{I_\circ}-\Delta_{D_2}
&=\frac{(n-1)(n^4-11n^2+14n+8)}{2(n-2)(2n+1)(n^2-2n-2)(2n^2-5n-2)},\\[3pt]
\Delta_{D_2}-\Delta_{D_1}
&=\frac{3(n-1)(3n-4)(n^2-2n-1)}{2(n-2)(n^2-2n-2)(2n^2-4n-3)(2n^2-4n-1)},\\[3pt]
\Delta_{D_1}-\Delta_{D_0}
&=\frac{n(n-1)(3n-4)}{2(n^2-2n-1)(2n^2-4n-3)(2n^2-4n-1)}.
\end{aligned}
\]
All denominator factors are positive for \(n\ge5\). The first numerator's cubic is positive because \(4n^3-11n^2=n^2(4n-11)>0\), and the second numerator's quartic is positive because \(n^4-11n^2=n^2(n^2-11)>0\); all other numerator factors are manifestly positive. This proves the full order and the characterization and enumeration of maximizers.

## Verification

The included `verify.py` checks the symbolic difference inequalities, independently enumerates every unordered pair of existing edges and its invariant class for \(n=5,6,7,8,9\), verifies exact class counts, and recomputes the Kirchhoff-index increase by separate grounded-Laplacian inversions for all five representative types at \(n=5,6,7\). It has 15 independent exact rational matrix comparisons, 25 exhaustive class-profile checks and four symbolic positivity comparisons. Run `python verify.py` after installing the dependency in `requirements.txt`. This finite checker is not substituted for the proof at arbitrary \(n\).

## Relationship to prior work

Ellens, Spieksma, Van Mieghem, Jamakovic and Kooij (2011) motivate Kirchhoff index as a network robustness measure and study global spectral formulas and edge-addition design, not two-edge losses of triangular graphs. Schaub, Lehmann, Yaliraki and Barahona (2013/2014) establish Laplacian-pseudoinverse descriptions of failure-induced edge-to-edge flow redistribution, not the present simultaneous two-outage Kirchhoff-index ordering. Brouwer and Haemers provide the classical spectrum of triangular graphs. These facts provide the context and ingredients, not the five-class result.

A previous exact five-motif failure classification for balanced complete multipartite graphs covers the exceptional \(T(4)=K_{2,2,2}\). The present claim therefore begins at \(n=5\). For \(n\ge5\), \(T(n)\) is *not* complete multipartite: its strongly regular parameters give degree \(2(n-2)\) and nonadjacent common-neighbor count \(4\), whereas in a complete multipartite graph that count equals the degree. Results about complete-graph edge deletions do not directly imply results about deleting edges from the line graph of a complete graph. No claim of methodological priority for spectral projectors or Woodbury updates is made.

## Limitations

The originality comparison is bounded by accessible scholarly text and indexed records; unindexed work could contain an equivalent triangular-graph damage classification. The proof relies on unit weights, exactly two distinct failures and \(n\ge5\). Neither larger failures nor general Johnson graphs are resolved. No independent mathematical audit is asserted.

## References

1. W. Ellens, F. M. Spieksma, P. Van Mieghem, A. Jamakovic and R. E. Kooij, "Effective graph resistance," *Linear Algebra and its Applications* 435 (2011), 2491–2506, doi:10.1016/j.laa.2011.02.024. First publicly available online 17 March 2011.
2. M. T. Schaub, J. Lehmann, S. N. Yaliraki and M. Barahona, "Structure of complex networks: Quantifying edge-to-edge relations by failure-induced flow redistribution," arXiv:1303.6241 (first submitted 25 March 2013), *Network Science* 2 (2014), 66–89.
3. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, Springer, 2012; see also A. E. Brouwer's public Johnson-graph reference at https://aeb.win.tue.nl/graphs/Johnson.html.

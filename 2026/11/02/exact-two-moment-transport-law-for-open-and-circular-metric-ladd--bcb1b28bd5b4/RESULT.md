# Exact two-moment transport law for open and circular metric ladders

## Finding

For every integer \(n\ge3\), give every edge of the combinatorial ladder \(L_n=P_n\mathbin{\square}K_2\) length one and every edge of the circular ladder (prism) \(C_n^\square=C_n\mathbin{\square}K_2\) length one. Both are compact length-metric graphs. Sample points \(X,Y\) independently from normalized arclength, allowing points in edge interiors, and put \(D=d(X,Y)\). Write \(\mu=\mathbb E D\) and \(\nu=\mathbb E D^2\).

For the open ladder, whose total length is \(3n-2\), both moments are
\[
\boxed{\mu_L(n)=\frac{n(9n^2-4n-4)}{3(3n-2)^2}},\qquad
\boxed{\nu_L(n)=\frac{27n^4-16n^3+42n^2-38n-12}{18(3n-2)^2}}.
\]
For the circular ladder, whose total length is \(3n\), the exact moments are
\[
\boxed{\mu_C(n)=\begin{cases}
\displaystyle\frac n4+\frac{14}{27}+\frac1{27n},&n\text{ even},\\
\displaystyle\frac n4+\frac{14}{27}+\frac1{108n},&n\text{ odd},
\end{cases}}
\]
and
\[
\boxed{\nu_C(n)=\begin{cases}
\displaystyle\frac{9n^3+28n^2+48n+20}{108n},&n\text{ even},\\
\displaystyle\frac{9n^3+28n^2+45n+16}{108n},&n\text{ odd}.
\end{cases}}
\]
In particular, \(\mu_C(n)<\mu_L(n)\) for every \(n\ge3\). The two networks differ by only two unit edges, but their normalized distance laws have distinct nondegenerate limits. If \(U,V\) are independent uniform points on \([0,1]\), then there exist couplings satisfying
\[
\left|\frac{D_L}{n}-|U-V|\right|\le\frac4n,
\qquad
\left|\frac{D_C}{n}-\min\{|U-V|,1-|U-V|\}\right|\le\frac4n
\]
almost surely. Thus \(D_L/n\) converges to the triangular-distance law \(|U-V|\), whereas \(D_C/n\) converges to the uniform law on \([0,1/2]\). Their means and variances obey
\[
\lim_{n\to\infty}\frac{\mu_C(n)}{\mu_L(n)}=\frac34,
\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(D_C)}{\operatorname{Var}(D_L)}=\frac38.
\]
Here variance is obtained exactly as \(\nu-\mu^2\); the limiting variances after division by \(n^2\) are \(1/18\) for the open ladder and \(1/48\) for the circular ladder. The additional two edges constitute a vanishing fraction \(2/(3n-2)\) of the original total length, yet change the limiting transport distribution.

## Assumptions and scope

The simple path \(P_n\) has \(n\) vertices, the simple cycle \(C_n\) has \(n\ge3\) vertices, and \(K_2\) is the two-vertex edge. The Cartesian product has two rail copies and \(n\) transverse spokes (rungs). The open ladder has \(2(n-1)\) rail edges and \(n\) rungs; the circular ladder has \(2n\) rail edges and \(n\) rungs. Every edge is a distinct unit interval joined to its incident vertices. This is the intrinsic shortest-path distance, not ambient Euclidean distance and not the vertex-only graph distance. Arclength gives every unit edge equal mass; vertices have measure zero. All assertions concern integer \(n\ge3\), with no hidden asymptotic assumption in the formulas or inequalities.

## Proof

**Elementary distance kernels.** Use coordinates \(u,v\in[0,1]\) for points on a rung or in one rail cell, and let \(Z=\min\{u+v,2-u-v\}\). For independent uniform \(u,v\), the variable \(Z\) has density \(2z\) on \([0,1]\), hence
\[
\mathbb E Z=\frac23,\quad \mathbb E Z^2=\frac12,
\quad\mathbb E|u-v|=\frac13,\quad\mathbb E|u-v|^2=\frac16.
\]
For two different rungs at columns \(i,j\), geodesic distance is their shortest rail-column separation plus \(Z\). For two points on opposite rail copies lying in the *same* unit cell, it is \(1+Z\), not \(1+|u-v|\); this yields local corrections \(1/3\) in the first moment and \(1\) in the second moment. For opposite rails in different cells, the distance is one plus the shortest horizontal separation. For rail-to-rung pairs, distance is the shortest horizontal separation plus the rung height to the appropriate rail. These statements follow by considering all possible top/bottom endpoint routes; a route with an extra complete rung cannot improve a shortest path.

**Open ladder.** Set \(m=n-1\) and denote by \(R\) a uniform point on the union of the two rails and by \(S\) a uniform point on the union of the rungs. If \(H\) is the horizontal coordinate of \(R\), then \(H\) is uniform on \([0,m]\), and the column of \(S\) is uniform on \(\{0,\dots,m\}\). Directly from the distance kernels, the conditional first and second moments are

| Pair type | First moment | Second moment |
|---|---|---|
| \(R,R\) | \(m/3+1/2+1/(6m)\) | \(m^2/6+m/3+1/2+1/(2m)\) |
| \(R,S\) | \((m+2)/3\) | \((m^2+3m+3)/6\) |
| \(S,S\) | \((n^2+2n-2)/(3n)\) | \((n^2-1)/6+4(n^2-1)/(9n)+1/2-1/(3n)\) |

For completeness, \(\mathbb E|H-J|=(2m+1)/6\), \(\mathbb E(H-J)^2=m(m+1)/6\), \(\mathbb E|J-J'|=(n^2-1)/(3n)\), and \(\mathbb E(J-J')^2=(n^2-1)/6\), where \(J,J'\) are independent uniform rung-column indices. For distinct columns, use the \(Z\) moments above; for equal columns, use \(|u-v|\). For opposite rail copies, the same-cell event has probability \(1/m\), giving the indicated corrections. The ordered arclength-pair weights for the three types are respectively \(4m^2,4mn,n^2\), divided by \((3m+1)^2\). Substitution and polynomial simplification yield the two displayed formulas for \(L_n\).

**Circular ladder.** Replace horizontal differences by the shorter circular separation \(\delta_n(x,y)=\min\{|x-y|,n-|x-y|\}\). A uniform point on a circle of length \(n\) has \(\delta_n\)-distance from any fixed point uniform on \([0,n/2]\), of mean \(n/4\) and second moment \(n^2/12\). Opposite-rail pairs acquire the same-cell corrections with probability \(1/n\). If \(K\) is the shorter circular separation between two independent uniformly sampled rung indices, then
\[
\mathbb E K=\begin{cases}n/4,&n\text{ even},\\(n^2-1)/(4n),&n\text{ odd},\end{cases}
\qquad
\mathbb E K^2=\begin{cases}(n^2+2)/12,&n\text{ even},\\(n^2-1)/12,&n\text{ odd}.\end{cases}
\]
The conditional moment table becomes

| Pair type | First moment | Second moment |
|---|---|---|
| \(R,R\) | \(n/4+1/2+1/(6n)\) | \(n^2/12+n/4+1/2+1/(2n)\) |
| \(R,S\) | \(n/4+1/2\) | \(n^2/12+n/4+1/3\) |
| \(S,S\) | \(\mathbb EK+2/3-1/(3n)\) | \(\mathbb EK^2+(4/3)\mathbb EK+1/2-1/(3n)\) |

The ordered arclength-pair weights are \(4:4:1\), divided by \(9\). Evaluating these combinations yields the stated parity-dependent mean and second moments. The odd-even corrections arise only from the discrete spacing of the rungs on the circle.

**Strict comparison.** The larger of the two possible expressions for \(\mu_C(n)\) is \(n/4+14/27+1/(27n)\). Direct subtraction gives
\[
\mu_L(n)-\left(\frac n4+\frac{14}{27}+\frac1{27n}\right)
=\frac{Q(n)}{108n(3n-2)^2},
\]
where, writing \(t=n-3\ge0\),
\[
Q(n)=81t^4+648t^3+1842t^2+2128t+725>0.
\]
Therefore \(\mu_L(n)>\mu_C(n)\) for every permissible \(n\).

**Strongly coupled limits.** Sample each point using a fresh uniform \(U\in[0,1]\) and an independent choice of rail/rung according to its arclength weight. In the open graph, place rail points at horizontal coordinate \((n-1)U\), and rung points on column \(\lfloor nU\rfloor\), choosing the vertical position independently uniformly. Then the horizontal coordinate divided by \(n\) differs from \(U\) by at most \(1/n\). Any intrinsic distance differs from the absolute horizontal separation by a nonnegative quantity at most \(2\). Using independent \(U,V\), the first displayed \(4/n\) coupling bound follows. In the closed graph, put rail points at circular coordinate \(nU\) and rung points on column \(\lfloor nU\rfloor\). The circle distance is 1-Lipschitz separately in its two circle coordinates, and the intrinsic distance differs from this horizontal circle distance by between \(0\) and \(2\). This gives the second \(4/n\) coupling bound. The law of \(\min\{|U-V|,1-|U-V|\}\) is uniform on \([0,1/2]\), while \(|U-V|\) has density \(2(1-t)\) on \([0,1]\). Their variances are \(1/48\) and \(1/18\), establishing both limiting ratios.

## Verification

A standalone standard-library-only script, `verify_ladders.py`, constructs each graph, computes all endpoint shortest-path distances using breadth-first search, and independently integrates the minimum of four affine endpoint-route functions over every pair of unit edges. It clips each unit square into rational polygons and integrates each affine function and its square exactly via rational triangle formulas. Same-edge moments are integrated analytically. Exact equality, not floating-point tolerance, was checked for both moments of each network at every integer \(3\le n\le9\). The 14 graphs comprised 2,401 unordered edge pairs and 4,802 exact moment comparisons, all passing. These finite checks corroborate the universal symbolic decomposition above; they are not used to extrapolate to arbitrary \(n\).

Run with `python verify_ladders.py` in a Python 3 environment. It needs no packages beyond the Python standard library, no internet, and no input files.

## Relationship to prior work

The continuous network metric and farthest-point formalism are used in Bose et al., *Network Farthest-Point Diagrams* (2013; first public version 2013-04-06; arXiv:1304.1909). Doyle and Graver, *Mean Distance for Shapes* (1982), introduced mean distance for graph-shaped domains and worked out several special families, but the published later literature enumerates those families as paths, stars, cycles, and restricted configurations, not the two regular ladders here. Garijo, Márquez and Silveira, *Continuous Mean Distance of a Weighted Graph* (2021 preprint; 2023 publication; arXiv:2103.11676), give algorithms for arbitrary fixed weighted graphs and closed formulas for certain structural classes, including complete graphs; no symbolic open-/circular-ladder pair or second-moment/limit theorem appears in its accessible full text. Baptista, Kennedy and Mugnolo, *Mean Distance on Metric Graphs* (2023 preprint; 2024 publication; arXiv:2312.04952), establish global mean-distance inequalities and spectral relations; their general bounds do not determine these moment formulas. Earlier formulas for the *vertex-only* Wiener index or Wiener polynomial of prisms (e.g., Sagan, Yeh and Zhang, 1996) concern a different sampling space and do not give the present arclength moments or two limiting laws. General finite-graph algorithms can in principle evaluate the mean for each fixed \(n\), but do not directly state these uniform-in-\(n\) formulas, the variance, or the vanishing-edge-fraction macroscopic change.

## Limitations

Only equal unit edge lengths are treated; arbitrary spoke weights, nonuniform arclength sampling, ladder graphs with additional diagonals, and more than two rails are outside the claim. The only asymptotic limit is \(n\to\infty\) through integers. The old full text of Doyle and Graver (1982) could not be obtained despite lawful open-access attempts and a separate institutional-access attempt, so historical-priority uncertainty remains. Its families are characterized by the fully accessible 2023 article, but that secondary account cannot replace inspection of the original. A general method that computes any fixed graph's mean is prior art and is not claimed as new. The present work does not assert an independent audit or prove an optimal-network design theorem beyond the explicit comparison made here.

## References

1. P. Bose, K. Dannies, J.-L. De Carufel, C. Doell, C. Grimm, A. Maheshwari, S. Schirra and M. Smid, *Network Farthest-Point Diagrams*, arXiv:1304.1909 (first version 2013-04-06), DOI:10.20382/jocg.v4i1a8.
2. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI:10.1002/jgt.3190060410.
3. J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B 9 (1982), 177–179, DOI:10.1068/b090177.
4. D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, arXiv:2103.11676 (2021), DOI:10.1007/s00025-023-01902-w.
5. L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean Distance on Metric Graphs*, arXiv:2312.04952 (2023), DOI:10.1007/s12220-024-01574-0.
6. B. E. Sagan, Y.-N. Yeh and P. Zhang, *The Wiener Polynomial of a Graph*, International Journal of Quantum Chemistry 60 (1996), 959–969; discrete vertex-distance polynomial, not an arclength-distance distribution.

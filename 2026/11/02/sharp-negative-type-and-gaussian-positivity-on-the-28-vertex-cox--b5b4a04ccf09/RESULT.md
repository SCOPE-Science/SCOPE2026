# Sharp negative type and Gaussian positivity on the 28-vertex Coxeter graph

## Finding

Let \(G\) be the 28-vertex Coxeter graph and let \(d\) be its unweighted shortest-path metric. Define \(\alpha\) as the unique positive zero of
\[
F(p)=(-1+\sqrt2)-2\sqrt2\,2^p-2\,3^p+(2+\sqrt2)4^p.
\]
Then \(0<\alpha<1\) (numerically \(\alpha\approx0.570406337320575\)). For every real \(p\ge0\), put \(D_p(u,v)=d(u,v)^p\) for distinct vertices and \(D_p(u,u)=0\); in particular, \(D_0=J-I\). For every \(t>0\), put \(K_{t,p}(u,v)=\exp(-tD_p(u,v))\). The exact classification is
\[
\boxed{K_{t,p}\succeq0\text{ for every }t>0\quad\Longleftrightarrow\quad0\le p\le\alpha.}
\]
For every \(p\) in this closed range and every fixed \(t>0\), \(K_{t,p}\) is **strictly** positive definite; above the range, \(K_{t,p}\) has a negative eigenvalue for all sufficiently small positive \(t\). Equivalently, the supremal negative-type exponent (generalized roundness) of the Coxeter graph metric is \(\alpha\).

At \(p=\alpha\), the symmetric form \(D_p\) restricted to the 27-dimensional zero-sum subspace has nullity exactly \(6\); all other 21 directions are strictly negative. Thus the minimum dimension of a Euclidean realization with squared interpoint distances \(d(u,v)^\alpha\) is exactly \(21\). For \(0\le p<\alpha\), this dimension is \(27\).

## Assumptions and scope

One explicit, unambiguous construction uses the Fano plane on \(\mathbb Z/7\mathbb Z\) with seven lines \(\{i,i+1,i+3\}\), where coordinates are modulo \(7\). Take as vertices all three-element subsets **other than** those seven lines, and join two vertices when the subsets are disjoint. This gives 28 vertices and the Coxeter graph. Graph distance is the least number of edges in a path. The graph is distance-transitive under its finite automorphism group \(\mathrm{PGL}(2,7)\), so its radial kernels are zonal positive-definite kernels on a finite homogeneous space. The distance shells around each vertex have sizes \((1,3,6,12,6)\), and the intersection array is \(\{3,2,2,1;1,1,1,2\}\). All graph distances are integers at most four.

A function \(D_p\) is conditionally negative semidefinite (CND) when \(\sum_{u,v}c_uc_vD_p(u,v)\le0\) for all real \((c_u)\) with \(\sum_uc_u=0\). The finite Schoenberg theorem identifies this with positive semidefiniteness of \(\exp(-tD_p)\) for every \(t>0\). The diagonal convention above avoids the undefined expression \(0^0\) at \(p=0\). All assertions concern this single finite metric and **all** real exponents and kernel scales specified; they do not claim a theorem for every cubic graph or every Coxeter-like graph.

## Proof

**1. Distance algebra.** Write \(A\) for graph adjacency and \(A_r\) for the indicator matrix of pairs at distance \(r\), with \(A_0=I\). The intersection-array recurrence determines \(A_r=P_r(A)\), where
\[
\begin{aligned}
P_0(x)&=1,&P_1(x)&=x,\\
P_2(x)&=x^2-3,&P_3(x)&=x^3-5x,\\
P_4(x)&=\tfrac12(x^4-x^3-7x^2+5x+6).
\end{aligned}
\]
In particular \(D_p=\sum_{r=1}^4 r^pP_r(A)\). The relevant adjacency eigenvalues (with multiplicities) are
\[
3^{[1]},\qquad2^{[8]},\qquad(-1)^{[7]},\qquad(-1+\sqrt2)^{[6]},\qquad(-1-\sqrt2)^{[6]}.
\]
These classical Coxeter graph data also follow directly from the Fano construction: the exact finite checker confirms the distance recurrence and the square-free adjacency annihilator \((A-3I)(A-2I)(A+I)(A^2+2A-I)=0\). The traces \(\operatorname{tr}(A^k)=(28,0,84,0)\) for \(k=0,1,2,3\), together with the rationality of traces and the irrational conjugate pair, force the displayed multiplicities uniquely. Thus no approximate eigenvalue computation is needed for the graph spectrum.

**2. The four zero-sum spectral branches.** Evaluating \(P_r\) on each nonconstant adjacency eigenspace, and setting \(z=2^p\), \(w=3^p\), \(y=4^p\), gives
\[
\begin{array}{c|c|c}
\text{adjacency eigenvalue}&\text{multiplicity}&\text{eigenvalue of }D_p\\\hline
2&8&2+z-2w-2y\\
-1&7&-1-2z+4w-2y\\
-1-\sqrt2&6&-1-\sqrt2+2\sqrt2 z-2w+(2-\sqrt2)y\\
-1+\sqrt2&6&F(p).
\end{array}
\]
These are all directions orthogonal to constants, since \(A\) and \(D_p\) are symmetric and share eigenspaces. For \(p=0\), all four branches equal \(-1\).

**3. The first three branches stay strictly negative on \([0,1]\).** First \(2+z-2w-2y<0\), since \(z\le2\), \(w,y\ge1\), and equality in the crude bound cannot hold simultaneously. Next, for \(0\le p\le1\) the function \(s\mapsto s^p\) is concave. Its central second difference satisfies
\[
0\le2\cdot3^p-2^p-4^p\le \max_{2\le s\le4}p(1-p)s^{p-2}\le\tfrac18.
\]
(The second-difference identity is the weighted integral, or mean-value, form of the second derivative with unit step.) Therefore the branch at \(-1\) is at most \(-3/4\).

For the branch at \(-1-\sqrt2\), concavity implies \(2w\ge z+y\). Since \(y=z^2\) and \(1\le z\le2\), that branch is bounded above by
\[
Q(z)=-1-\sqrt2+(2\sqrt2-1)z+(1-\sqrt2)z^2.
\]
Its derivative is decreasing, but \(Q'(2)=3-2\sqrt2>0\), so \(Q\) increases on \([1,2]\). Hence this branch is at most \(Q(2)=1-\sqrt2<0\).

**4. The last branch has exactly one crossing.** Direct evaluation gives \(F(0)=-1\) and \(F(1)=1+\sqrt2>0\). Its first derivative at zero is \(F'(0)=2\log(4/3)>0\). Moreover for every \(p\ge0\), using \(2^p,3^p\le4^p\) and \(\log3<2\log2\),
\[
\begin{aligned}
F''(p)&=(2+\sqrt2)(\log4)^2\,4^p-2\sqrt2(\log2)^2\,2^p-2(\log3)^2\,3^p\\
&\ge4^p\left((8+2\sqrt2)(\log2)^2-2(\log3)^2\right)\\
&>2\sqrt2(\log2)^2\,4^p>0.
\end{aligned}
\]
Thus \(F\) is strictly increasing for all \(p\ge0\), has a unique positive root \(\alpha\) in \((0,1)\), is strictly negative before it, and strictly positive after it. Combined with Step 3, this proves the CND range for \(0\le p\le\alpha\); when \(p>\alpha\), the six-dimensional last eigenspace is a positive direction, proving failure of CND without requiring analysis of other modes above one.

**5. Gaussian kernels and embedding rank.** For a finite zero-diagonal real symmetric matrix, Schoenberg's equivalence gives \(D_p\) CND precisely when \(e^{-tD_p}\) is positive semidefinite for every \(t>0\). For \(p>\alpha\), an eigenvector \(v\perp\mathbf1\) with \(v^TD_pv>0\) satisfies \(v^TK_{t,p}v=-t v^TD_pv+O(t^2)<0\) as \(t\downarrow0\). For admissible \(p\), CND makes \(D_p\) a squared Euclidean distance matrix; distinct graph vertices map to distinct Euclidean points because every off-diagonal \(D_p\) is positive. A Gaussian kernel on distinct Euclidean points is strictly positive definite for every positive scale. Finally, the centered Gram matrix \(-\tfrac12JD_pJ\), with \(J=I-\mathbf1\mathbf1^T/28\), has rank \(27\) below the threshold and \(27-6=21\) at the threshold, which is exactly the minimum Euclidean embedding dimension.

## Verification

Run the included standard-library program `python3 artifacts/verify.py` from the directory containing these files. It constructs the Fano-plane model from seven modular triples, obtains all 28 vertices and 42 edges, and uses breadth-first search to determine every distance. It checks the intersection shells, distance polynomials as exact integer matrix identities, the square-free adjacency annihilator and trace moments, and numerical probes of the four powered-distance branches. Successful execution prints `COXETER_EXACT_GRAPH_AND_DISTANCE_SPECTRUM_OK` and `COXETER_SHARP_EXPONENT_NUMERIC_CHECK_OK`. Numerical probes are only consistency tests; the real-exponent claims follow from the analytic inequalities in Steps 3–5.

## Relationship to prior work

Sánchez (2011, arXiv:1108.0451v1) gives the general distance-matrix method for computing supremal negative type, and explicitly treats complete bipartite graphs and several five-vertex examples. His general characterization is applicable to this 28-vertex graph but does not furnish its distance-powered harmonic eigenvalues, sharp radical-exponential crossing, uniqueness proof, or endpoint six-dimensional obstruction. The classical Coxeter graph intersection array and adjacency spectrum are recorded in the DistanceRegular.org database and MathWorld. Orel and Višnjić (arXiv:2404.17067v1) identify the Coxeter graph as the three-dimensional member of a binary-symmetric-matrix family and study graph-distance formulas; their inspected abstract, introduction, and distance discussion do not state a negative-type or Gaussian-positivity exponent. These graph and metric tools are inputs, not claimed contributions. The contribution assessed here is their exact combination into the sharp kernel/embedding classification for the Coxeter metric. No exhaustive historical-priority assertion is made.

## Limitations

The theorem concerns the specific 28-point Coxeter shortest-path metric; it does not classify negative type for arbitrary distance-transitive graphs or general Coxeter-like graphs. The polynomial equation defines a transcendental exponent; the decimal expansion is approximate, not a symbolic closed form. The checker exhaustively verifies graph identities but samples only finitely many real exponents; the infinite assertion relies on the displayed inequalities. A direct result in older specialized association-scheme, radial positive-definiteness, or distance-regular embedding literature could be equivalent, notwithstanding the cited comparisons. Independent external mathematical validation has not been performed.

## References

1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first publicly posted 2011-08-02, especially Definition 1.1, Corollary 2.4, and Section 3. https://arxiv.org/pdf/1108.0451 .
2. DistanceRegular.org, *Coxeter graph*, graph intersection array and spectrum, https://www.math.mun.ca/distanceregular/graphs/coxeter.html (accessed 2026-10-29).
3. E. W. Weisstein, *Coxeter Graph*, MathWorld, https://mathworld.wolfram.com/CoxeterGraph.html (accessed 2026-10-29).
4. M. Orel and D. Višnjić, *The distance function on Coxeter-like graphs and self-dual codes*, arXiv:2404.17067v1, first publicly posted 2024-04-25, especially abstract and Section 1; https://arxiv.org/pdf/2404.17067 .

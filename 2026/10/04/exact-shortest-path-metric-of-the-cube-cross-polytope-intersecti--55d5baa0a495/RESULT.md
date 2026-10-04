# Exact shortest-path metric of the cube–cross-polytope intersection balls

## Finding
For integers \(d\ge 2\) and \(1\le k<d\), define
\[
P_{d,k}=(kB_1^d)\cap[-1,1]^d.
\]
The vertices are exactly the vectors in \(\{-1,0,1}\^d\) with exactly \(k\) nonzero coordinates. For vertices \(u,v\), write
\[
a(u,v)=|\{i:u_i=v_i\ne0\}|,\qquad
r(u,v)=|\{i:u_i\ne0,\ v_i\ne0\}|.
\]
Then
\[
\operatorname{dist}_{P_{d,k}}(u,v)=
\begin{cases}
0,&u=v,\\
k-a(u,v),&r(u,v)<k,\\
k-a(u,v)+1,&r(u,v)=k,\ u\ne v.
\end{cases}
\]
Two vertices are adjacent exactly when \(\langle u,v\rangle=k-1\). Hence the one-skeleton is the Johnson-type graph \(J_{\pm}(d,k,k-1)\), and
\[
\operatorname{diam}P_{d,k}=k+1.
\]
For any fixed vertex, the number \(N_j\) of vertices at distance \(j\) is \(N_0=1\), \(N_{k+1}=1\), and, for \(1\le j\le k\),
\[
N_j=
\binom{k}{j}
\sum_{c=1}^{\min(j,d-k)}
\binom{j}{c}\binom{d-k}{c}2^c
+\mathbf 1_{\{j\ge2\}}\binom{k}{j-1}.
\]
For \(k=d\), the body is the cube \([-1,1]^d\); the graph metric is sign Hamming distance and the diameter is \(d\).

## Assumptions and scope
Here \(B_1^d=\{x\in\mathbb R^d:\sum_i|x_i|\le1\}\). The nontrivial formula is for integers \(1\le k<d\). Deza, Hiriart-Urruty, and Pournin identify the polar optimization ball with \((kB_1^d)\cap[-1,1]^d\) and, by polarity, identify its vertices as the \(k\)-sparse sign vectors. The classification is indexed under primary MSC 52B05, the class for combinatorial properties of polytopes including shortest paths.

## Proof
Let \(V_{d,k}\) be the set of \(k\)-sparse sign vectors.

First determine the edges. A linear functional \(c\cdot x\) on \(P_{d,k}\) is maximized on vertices obtained by selecting \(k\) coordinates with largest \(|c_i|\) and taking the signs of \(c_i\). If its maximizing face is one-dimensional, then exactly \(k-1\) signed coordinates are forced above the cutoff and exactly two coordinates tie at the cutoff for the last position. Therefore the endpoints agree in exactly \(k-1\) signed coordinates and differ by replacing one occupied coordinate by one previously zero coordinate. Conversely, any such pair is exposed as an edge by choosing large coefficients on their common signed coordinates, equal smaller absolute coefficients on the two exchanged coordinates with the endpoint signs, and still smaller coefficients elsewhere. Thus
\[
u\sim v\quad\Longleftrightarrow\quad
\langle u,v\rangle=k-1.
\]

Now fix a target vertex \(v\). Each edge replaces one signed coordinate, so the number of target signed coordinates already present can increase by at most one. Starting from \(u\), this gives the lower bound \(k-a(u,v)\). If \(u\) and \(v\) have the same support but are unequal, the first edge must leave that support because an edge exchanges two distinct coordinate positions. It therefore cannot increase the number of correct signed coordinates, and the lower bound improves to \(k-a(u,v)+1\).

These bounds are attained. If the supports differ, let \(c=k-r(u,v)\ge1\) be the number of source-only, and hence target-only, coordinates, and let \(b=r(u,v)-a(u,v)\) be the number of common coordinates carrying opposite signs. If \(b=0\), directly exchange the \(c\) source-only coordinates for the \(c\) target-only coordinates. If \(b>0\), use one target-only coordinate to open a chain: remove the first wrong-sign common coordinate and insert that target-only coordinate; successively remove each remaining wrong-sign coordinate and insert the corrected sign of the preceding one; close the chain by removing one source-only coordinate and inserting the corrected sign of the last wrong-sign coordinate. Exchange the remaining source-only coordinates directly. The path has \(b+c=k-a(u,v)\) edges.

If the supports agree and \(u\ne v\), then \(b=k-a(u,v)>0\). Since \(k<d\), choose one coordinate outside the common support. Insert it while removing the first wrong-sign coordinate, propagate corrected signs along the wrong-sign coordinates, and finally remove the temporary outside coordinate while inserting the final corrected sign. This gives \(b+1=k-a(u,v)+1\) edges.

The diameter is therefore \(k+1\), attained by antipodal vertices with the same support. The shell formula follows by counting, relative to a fixed vertex, \(a\) same-sign common coordinates, \(b\) opposite-sign common coordinates, and \(c\) exchanged support coordinates. For \(c>0\), distance \(j=b+c\); choosing the \(j\) nonmatching source coordinates, then the \(c\) exchanged ones, their new positions, and their signs gives the first summand. For \(c=0\) and \(b>0\), distance is \(b+1\), giving the second summand.

## Verification
The standalone checker in `artifacts/verify_metric.py` generates all vertices and all graph edges directly by signed-coordinate exchange, performs breadth-first search from every vertex for all \(2\le d\le7\) and \(1\le k<d\), and compares every computed pair distance with the closed formula. It also checks the degree \(2k(d-k)\), diameter \(k+1\), and the closed distance-shell counts. The saved replay output is in `artifacts/VERIFY_OUTPUT.txt`.

This finite replay is corroborative only. The proof above establishes the formulas for every admissible integer \(d,k\).

## Relationship to prior work
Cherkashin and Kiselev introduced the general graphs \(J_{\pm}(n,k,t)\) on the same constant-support ternary vectors and study independence numbers, principally for nonpositive scalar-product parameters. Their use of “diameter” concerns Hamming diameter of vertex families in an isodiametric inequality, not shortest-path diameter of \(J_{\pm}(n,k,k-1)\).

Deza, Hiriart-Urruty, and Pournin identify \(P_{d,k}\) as the polar optimization ball, determine its vertex set by polarity, and compute face numbers and volumes. Their article notes an application to monotone-path computation, but does not give an all-pairs one-skeleton metric or diameter formula.

Takhanov and Yun later use the name signed Johnson graph for exactly the adjacency condition \(\langle u,v\rangle=k-1\), with their stated results directed at maximum independent sets and kissing arrangements. Exact-title, graph-distance, shortest-path, and diameter searches did not locate a prior statement of the metric above. The full text of that 2026 preprint was not retrievable in the present inspection, so an unindexed observation there remains a residual bibliographic risk.

## Limitations
The theorem concerns the graph metric of the integer-parameter balls \(P_{d,k}\); it does not describe weighted shortest paths, noninteger parameters, or distances in other face-adjacency graphs. The finite checker reaches dimension seven and is not used as an infinite proof. The originality assessment is literature-search based and retains the explicit residual risk attached to the inaccessible 2026 full text.

## References
1. Danila Cherkashin and Sergei Kiselev, *Independence numbers of Johnson-type graphs*, arXiv:1907.06752, first posted 2019-07-15; Bulletin of the Brazilian Mathematical Society, 2023.
2. Antoine Deza, Jean-Baptiste Hiriart-Urruty, and Lionel Pournin, *Polytopal balls arising in optimization*, arXiv:2011.05607, first posted 2020-11-11; Contributions to Discrete Mathematics 16(3), 2021, DOI 10.55016/ojs/cdm.v16i3.71526.
3. Rustem Takhanov and Stanislav Yun, *Classification of independent sets in signed Johnson graphs and applications to kissing arrangements*, arXiv:2606.03299, 2026.

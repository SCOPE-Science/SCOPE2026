# Exact 2-WL stabilization depth of path graphs
## Finding
For the finite simple undirected path \(P_n\), standard ordered-pair two-dimensional Weisfeiler--Leman refinement from the atomic equality/edge/nonedge coloring has strict-refinement depth
\[
\rho_2(P_n)=\begin{cases}
0,&n\le 2,\\
\lfloor\log_2(n-1)\rfloor,&n\ge 3.
\end{cases}
\]
There is also an exact description of every intermediate color class. Label the vertices \(0,1,\ldots,N\), where \(N=n-1\). Put \(A_r=2^r-1\), \(B_r=2^r\), and \(\tau_t(s)=\min\{s,t\}\). After \(r\) rounds, a diagonal pair \((i,i)\) is classified by the unordered pair
\[
\{\tau_{A_r}(i),\tau_{A_r}(N-i)\}.
\]
For \(i\ne j\), set \(\varepsilon=+1\) when \(i<j\) and \(\varepsilon=-1\) otherwise, and define
\[
L=\min\{i,j\},\qquad M=|i-j|-1,\qquad R=N-\max\{i,j\}.
\]
Then the round-\(r\) color is exactly the reflected profile class of
\[
(\varepsilon,\tau_{A_r}(L),\tau_{B_r}(M),\tau_{A_r}(R)),
\]
where reflection identifies
\[
(\varepsilon,L,M,R)\sim(-\varepsilon,R,M,L).
\]

## Assumptions and scope
The graph is the uncolored simple path \(P_n\). The refinement is the classical two-dimensional Weisfeiler--Leman procedure on ordered vertex pairs. Round \(0\) is the atomic partition into equality, adjacency, and distinct nonadjacency. A round is counted as strict only when its induced partition is strictly finer than the preceding partition. The statement concerns stabilization on one graph, not the number of rounds needed to distinguish two different graphs.

## Proof
Let \(c_r(i,j)\) denote the pair color after \(r\) rounds. Define the profile partition \(\Pi_r\) by the clipped data in the Finding. We prove by induction that \(c_r\) and \(\Pi_r\) induce the same partition of ordered pairs.

At \(r=0\), \(A_0=0\) and \(B_0=1\). Thus all outer gaps are clipped to \(0\), while the middle gap distinguishes exactly \(M=0\) from \(M\ge1\). This is precisely the equality/edge/nonedge partition.

For the induction step, consider the Weisfeiler--Leman update signature
\[
\Sigma_r(i,j)=\left(c_r(i,j),\left\{\!\left\{(c_r(i,z),c_r(z,j)):0\le z\le N\right\}\!\right\}\right).
\]
The relative position of \(z\) with respect to \(i\) and \(j\) falls into finitely many interval cases. In each case, the induction hypothesis expresses both colors inside the multiset solely through clipped distances from \(z\) to the adjacent marked point or endpoint. Moving \(z\) one step through an outer gap produces two boundary runs of unsaturated types of length \(A_r\); they overlap exactly when that outer gap has length below \(2A_r+1\). Hence the new signature recovers an outer gap exactly below \(2A_r+1\) and otherwise records only saturation. Likewise, moving \(z\) through the interval between the two marked vertices produces two boundary runs of length \(B_r\), so the middle gap is recovered exactly below \(2B_r\) and otherwise only as saturated. Deep saturated positions contribute the same saturated signature types; their total multiplicity is fixed by \(L+M+R=N-1\), so it gives no extra distinction beyond the unsaturated boundary runs. Reflection exchanges the two outer runs and reverses \(\varepsilon\), and no other identification occurs. Therefore the update of \(\Pi_r\) is exactly \(\Pi_{r+1}\), because
\[
2A_r+1=2^{r+1}-1=A_{r+1},\qquad 2B_r=2^{r+1}=B_{r+1}.
\]
This proves the profile formula for every round.

It remains to locate stabilization. Let \(N\ge1\) and put \(r=\lfloor\log_2N\rfloor\), so \(2^r\le N<2^{r+1}\). In any distinct-pair profile, the three gap lengths satisfy \(L+M+R=N-1\). At round \(r\), an outer gap is saturated only from \(2^r-1\) onward and the middle gap only from \(2^r\) onward. Because \(N<2^{r+1}\), two independently variable saturated gaps cannot occur: the only boundary possibility with two saturated outer gaps is the unique symmetric profile \(L=R=2^r-1\), \(M=0\). Consequently the clipped profile together with the fixed total \(N-1\) recovers the full reflected profile, so no later round can refine it.

For strictness one round earlier, assume \(r\ge1\). The diagonal round-\((r-1)\) profile clips the distance to the nearer endpoint at \(2^{r-1}-1\). Since \(N\ge2^r\), the path contains vertices at near-endpoint distances \(2^{r-1}-1\) and \(2^{r-1}\); these lie in distinct reflection orbits but have the same round-\((r-1)\) diagonal color. Round \(r\) separates them. Thus the last strict round is exactly \(r\). The cases \(n=1,2\) are already stable at round \(0\).

## Verification
The standalone script `verify_path_wl.py` implements standard ordered-pair two-dimensional Weisfeiler--Leman refinement independently from the closed form. For every \(1\le n\le40\), it checks the complete round-by-round pair partition against the stated clipped-profile formula and checks the stabilization-depth formula. The run returned `VERIFY_OK paths=1..40 profile_checks=218 depth_checks=40`.

## Relationship to prior work
Pikhurko and Verbitsky explain the logarithmic-depth distance-doubling trick and obtain a logarithmic first-order upper bound for defining paths, but they do not state this exact two-dimensional Weisfeiler--Leman round law or the pair-profile classification. Lichter, Ponomarenko, and Schweitzer study the iteration number of two-dimensional Weisfeiler--Leman in general and prove an \(O(n\log n)\) upper bound; a full-text search of their paper finds no occurrence of `path` or `Path`. The present result gives a closed-form logarithmic benchmark on the simplest nonregular tree and identifies every intermediate pair color, not only the terminal round count.

## Limitations
The induction is specialized to paths and uses their three-gap decomposition. It does not claim the same formula for arbitrary trees, interval graphs, or bounded-treewidth graphs. The computational check is finite evidence only; the infinite statement rests on the proof above. The literature comparison cannot exclude an unindexed or differently phrased prior occurrence.

## References
1. Oleg Pikhurko and Oleg Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first submitted 25 March 2010.
2. Moritz Lichter, Ilia Ponomarenko, and Pascal Schweitzer, *Walk refinement, walk logic, and the iteration number of the Weisfeiler-Leman algorithm*, arXiv:1905.03008, 2019.

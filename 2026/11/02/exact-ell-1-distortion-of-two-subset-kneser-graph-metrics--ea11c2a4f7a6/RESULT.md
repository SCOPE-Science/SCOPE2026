# Exact \(\ell_1\) distortion of two-subset Kneser graph metrics

## Finding
For every integer \(n\ge 6\), let \(G_n=KG(n,2)\) have vertex set \(X_n=\binom{[n]}2\), with an edge precisely when its two vertex-labels are disjoint. Equip \(G_n\) with its unit-edge shortest-path metric \(d_n\). Its least distortion into a real \(\ell_1\) space is exactly
\[
\boxed{c_{\ell_1}(X_n,d_n)=\frac{2(n-4)}{n-3}=2-\frac{2}{n-3}.}
\]
For every \(n\ge6\), equality is attained by the nonnegative cut metric obtained by averaging the cuts indexed by the edges of Hamiltonian cycles of the complete graph on \([n]\). This construction simultaneously saturates a sharp conditional-negative-definiteness obstruction carried by the \((n-1)\)-dimensional incidence subspace. The exact distortions increase strictly from \(4/3\) at \(n=6\) toward the limiting value \(2\). The case \(n=5\), where \(G_5\) is the Petersen graph and its distortion equals \(1\), is a previously known boundary and is not part of the novelty assertion.

## Assumptions and scope
All graphs here are finite, simple, undirected, and unweighted. Fix \(n\ge6\) and put \(N=\binom n2\). For distinct \(e,f\in X_n\), their graph distance is
\[
d_n(e,f)=\begin{cases}1,&e\cap f=\varnothing,\\2,&e\cap f\ne\varnothing.\end{cases}
\]
Indeed disjoint pairs are adjacent, while intersecting pairs admit a common disjoint two-subset whenever \(n\ge5\). The distance from a vertex to itself is zero.

For any finite metric space \((X,d)\), define its real \(\ell_1\) distortion as the least \(D\ge1\) for which an embedding \(F:X\to\ell_1^M\) exists, for some finite \(M\), such that after a common positive scaling,
\[
d(x,y)\le \|F(x)-F(y)\|_1\le D\,d(x,y)\quad(x,y\in X).
\]
Finite \(\ell_1\) distance matrices are nonnegative linear combinations of cut semimetrics. Conversely, a cut metric has a finite-dimensional \(\ell_1\) representation by the cut indicators. Either characterization suffices below. The graph metric is distinct from the usual Hamming/Johnson distance on two-subsets: in the latter, intersecting labels are closer, whereas here disjoint labels are closer.

## Proof
**1. A negative-type obstruction for every candidate embedding.** Every finite real \(\ell_1\) semimetric \(\rho\) is *conditionally negative semidefinite*: for any real vector \(z\) with \(\sum_{e\in X_n}z_e=0\),
\[
\sum_{e,f\in X_n} z_ez_f\rho(e,f)\le0.
\]
For a cut semimetric of a set \(S\subseteq X_n\), the left side is \(-2(\sum_{e\in S}z_e)^2\); a nonnegative sum or limit of such cut semimetrics preserves the inequality. Thus no unproved Hilbert-embedding hypothesis is needed.

Suppose \(\rho\) is a candidate \(\ell_1\) distance matrix with \(d_n\le\rho\le Dd_n\). Average \(\rho\) over the permutation group of \([n]\). Convexity and permutation invariance of the cut cone preserve its \(\ell_1\) character and the same distortion inequalities. Because pairs of distinct two-subsets have exactly two permutation orbits, the averaged matrix has some value \(u\) on disjoint label pairs and some value \(v\) on intersecting label pairs, with
\[
1\le u\le D,\qquad 2\le v\le2D.
\]
Write \(B\) for the \(n\times N\) unsigned vertex-edge incidence matrix of the complete graph \(K_n\), so \(B_{i,e}=1\) exactly when \(i\in e\). Let \(A\) be the adjacency matrix of the *triangular* graph on the two-subsets, joining labels that intersect. On all of \(\mathbb R^{X_n}\),
\[
A=B^{\mathsf T}B-2I_N.
\]
Take any nonzero \(a\in\mathbb R^n\) satisfying \(\sum_i a_i=0\), and put \(z=B^{\mathsf T}a\), that is \(z_{\{i,j\}}=a_i+a_j\). The matrix identity
\[
BB^{\mathsf T}=(n-2)I_n+J_n
\]
shows that \(z\ne0\), \(\sum_ez_e=0\), and \(Az=(n-4)z\). In matrix form the averaged distance matrix is
\[
R=u(J_N-I_N)+(v-u)A.
\]
Consequently,
\[
z^{\mathsf T}Rz=\big((n-4)v-(n-3)u\big)\,\|z\|_2^2\le0.
\]
Since \(n\ge6\), it follows that \(u\ge\tfrac{n-4}{n-3}v\). Combining this with the distortion inequalities yields
\[
\boxed{D\ge u\ge\frac{n-4}{n-3}v\ge\frac{2(n-4)}{n-3}.}
\]
The test vector exists for every \(n\ge6\) (take, for example, \(a=(1,-1,0,\ldots,0)\)). This bound applies to all finite-dimensional \(\ell_1\) embeddings and, by finite restriction, to embeddings in arbitrary real \(L_1\) spaces as well.

**2. Hamiltonian-cycle cuts attain the obstruction.** Fix the Hamiltonian cycle of \(K_n\) with edge set
\[
S_0=\big\{\{1,2\},\{2,3\},\ldots,\{n-1,n\},\{n,1\}\big\}\subset X_n.
\]
For a subset \(S\subset X_n\), let \(\delta_S(e,f)=|\mathbf1_S(e)-\mathbf1_S(f)|\). For uniformly distributed \(\pi\in S_n\), consider the averaged cut metric
\[
\bar\delta(e,f)=\frac1{n!}\sum_{\pi\in S_n}\delta_{\pi(S_0)}(e,f).
\]
By permutation transitivity it takes two values: \(p_I\) on intersecting label pairs and \(p_D\) on disjoint label pairs. These values can be obtained by double-counting crossing pairs for the fixed cycle \(S_0\).

There are \(n\binom{n-1}{2}\) unordered pairs of distinct members of \(X_n\) that intersect. Each of the \(n\) chosen cycle edges intersects \(2(n-2)\) other edges of \(K_n\), of which exactly two are in the same cycle. Hence the number of intersecting pairs crossing \(S_0\) is \(2n(n-3)\), and
\[
p_I=\frac{2n(n-3)}{n\binom{n-1}{2}}=\frac{4(n-3)}{(n-1)(n-2)}.
\]
There are \(3\binom n4\) disjoint unordered edge pairs. The complement of \(S_0\) in the edges of \(K_n\) has \(n(n-3)/2\) members. For each selected cycle edge, precisely \((n-3)(n-4)/2\) complement edges are disjoint from it. Thus the number of disjoint pairs crossing \(S_0\) is \(n(n-3)(n-4)/2\), giving
\[
p_D=\frac{n(n-3)(n-4)/2}{3\binom n4}=\frac{4(n-4)}{(n-1)(n-2)}.
\]
Scale the averaged cut metric by
\[
w=\frac{2}{p_I}=\frac{(n-1)(n-2)}{2(n-3)}.
\]
The resulting finite-dimensional \(\ell_1\) metric \(\rho_*=w\bar\delta\) satisfies
\[
\rho_*(e,f)=\begin{cases}
\dfrac{2(n-4)}{n-3},&e\cap f=\varnothing,\\[5pt]
2,&e\cap f\ne\varnothing,
\end{cases}\qquad(e\ne f).
\]
In particular, for \(n\ge6\) it obeys \(d_n\le\rho_*\le\frac{2(n-4)}{n-3}\,d_n\). One explicit embedding is
\[
F(e)=\frac{w}{n!}\big(\mathbf1_{\pi(S_0)}(e)\big)_{\pi\in S_n}\in\ell_1^{n!}.
\]
The lower and upper estimates coincide, proving the theorem. (The factorial-dimensional representation is canonical but not claimed to be dimension-minimal.)

**3. Why the spectral obstruction is sharp, not merely necessary.** The optimal metric satisfies \(v/u=(n-3)/(n-4)\) and hence makes the quadratic form in Step 1 vanish for the entire nonzero incidence subspace \(\{B^{\mathsf T}a:\sum_i a_i=0\}\), of dimension \(n-1\). The explicit Hamiltonian-cycle cut representation certifies that *all* cut-cone inequalities hold at this very ratio. Conditional negative type alone would not generally prove membership in the cut cone; the construction closes that gap here.

## Verification
The standalone Python 3 checker `verify_kneser.py` uses only the standard library and rational arithmetic. Run `python3 verify_kneser.py` from the extracted package directory. It independently reconstructs all-pairs shortest-path distances on \(KG(n,2)\) for \(5\le n\le11\), checks the unsigned incidence identity, verifies that the zero-sum spectral witness vanishes at the sharp ratio and is positive above it, reconstructs the Hamiltonian-cycle cut and both orbitwise crossing counts, and checks the final scaling. For \(5\le n\le7\) it additionally enumerates all \(n!\) permutations rather than relying on the crossing-count formulas. The recorded replay returned `CHECK_OK 8462 exact finite assertions; n=5..11; permutation orbit n=5..7`. These are finite checks, not an exhaustive verification over all integers; the proof in Steps 1–2 covers all \(n\ge6\).

## Relationship to prior work
Ducey, Hill and Sin (2017), *The critical group of the Kneser graph on 2-subsets of an n-element set*, study precisely the graphs \(KG(n,2)\), their strongly regular parameters, and their Laplacian/critical groups. Their established spectral structure is compatible with the lower-bound witness, but their studied invariant does not yield a matching \(\ell_1\) cut representation or the exact distortion. Baudier, Lancien, Motakis and Schlumprecht (2020) study generalized Hamming-type metrics on subsets and their Banach embeddings; the usual Hamming distance on pairs orders the two intersection classes oppositely to the present disjointness-graph shortest-path metric. Their general theory does not imply the displayed exact cut-cone optimum.

A published exact cut-cone census for six small cubic-symmetric graph metrics establishes that the Petersen graph \(KG(5,2)\) embeds isometrically into \(\ell_1\); this known boundary is not represented as new. Its six particular graphs do not include \(KG(n,2)\) for any \(n\ge6\) and do not state the formula here. A separate published all-\(n\) theorem about the Euclidean John/Löwner ellipsoids of the \(1\)-eigenpolytope of \(KG(n,2)\) concerns the same Kneser family and uses its unsigned incidence matrix; its claims concern spectral-polytopal radii and fractional matching facets, not the shortest-path metric's least \(\ell_1\) distortion. The lower-bound eigenvalue by itself also does not entail the existence of the present cycle-orbit cut construction.

These are implication comparisons, not a claim that lack of a matching title proves novelty. A previously unlocated equivalent metric-embedding theorem, possibly phrased via the complement of the triangular graph or a two-class association scheme, remains a historical-priority risk.

## Limitations
The theorem concerns **only** unit-edge graph distances on two-subset Kneser graphs for \(n\ge6\), not arbitrary positive edge weights, higher-order Kneser graphs \(KG(n,k)\) with \(k\ge3\), general strongly regular graphs, or optimal target dimension. The displayed finite-dimensional cut construction establishes existence but not uniqueness of optimal embeddings. It does not assert that the general negative-type criterion is sufficient for other metrics. The exact value is mathematically verified by the argument given; historical originality remains subject to further independent bibliographic scrutiny. No independent audit is asserted.

## References
1. J. E. Ducey, I. Hill and P. Sin, *The critical group of the Kneser graph on 2-subsets of an n-element set*, arXiv:1707.09115v1, first public 2017-07-28, https://arxiv.org/abs/1707.09115.
2. F. P. Baudier, G. Lancien, P. Motakis and T. Schlumprecht, *The geometry of Hamming-type metrics and their embeddings into Banach spaces*, arXiv:2004.04805v1, first public 2020-04-09, https://arxiv.org/abs/2004.04805.
3. F. P. Baudier, P. Motakis, T. Schlumprecht and A. Zsák, *On the bi-Lipschitz geometry of lamplighter graphs*, arXiv:1902.07098v1, first public 2019-02-19, https://arxiv.org/abs/1902.07098.
4. *Exact L1-distortion census for six small cubic-symmetric graphs*, 2026, https://github.com/Resultary/2026/blob/main/2026/9/11/SCOPE004/RESULT.md.
5. *Parity-controlled John and Löwner ellipsoids of Kneser pair-eigenpolytopes*, 2026, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-parity-controlled-john-and-l-wner-ellipsoids-of-kneser-pair-eige--71ae72613d53/RESULT.md.

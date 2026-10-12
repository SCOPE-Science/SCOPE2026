# Six vertices are the sharp density–spectral epidemic-ranking reversal boundary
## Finding
Consider two finite connected simple contact networks on the same number
\[
n
\]
of vertices.

A homogeneous-mixing approximation uses average degree
\[
\bar d=\frac{2|E|}{n}
\]
and the associated threshold proxy
\[
\tau_{\mathrm{avg}}=\frac1{\bar d}.
\]

The adjacency-spectral SIS mean-field threshold is
\[
\tau_{\mathrm{spec}}=\frac1{\rho(A)},
\]
where \(A\) is the adjacency matrix and \(\rho(A)\) is its spectral radius.

Smaller threshold means greater epidemic vulnerability in both summaries.

For every
\[
n\le5,
\]
no two connected simple graphs receive opposite strict vulnerability rankings from these two thresholds.

At
\[
n=6,
\]
strict reversal is possible for the first time.

Take the star
\[
K_{1,5}
\]
and the cycle
\[
C_6.
\]

For the star,
\[
\bar d(K_{1,5})=\frac53,
\qquad
\rho(K_{1,5})=\sqrt5.
\]
Hence
\[
\tau_{\mathrm{avg}}(K_{1,5})=\frac35,
\qquad
\tau_{\mathrm{spec}}(K_{1,5})=\frac1{\sqrt5}.
\]

For the cycle,
\[
\bar d(C_6)=2,
\qquad
\rho(C_6)=2,
\]
so
\[
\tau_{\mathrm{avg}}(C_6)=\tau_{\mathrm{spec}}(C_6)=\frac12.
\]

Therefore homogeneous mixing ranks the cycle as more vulnerable,
\[
\frac12<\frac35,
\]
while the spectral threshold ranks the star as more vulnerable,
\[
\frac1{\sqrt5}<\frac12.
\]

The same mechanism persists for every
\[
n\ge6.
\]
Indeed, compare
\[
K_{1,n-1}
\]
with
\[
C_n.
\]
Then
\[
\frac{2(n-1)}n<2,
\]
but
\[
\sqrt{n-1}>2.
\]
Thus the cycle is always denser, while the star always has the lower spectral epidemic threshold once \(n\ge6\).

## Assumptions and scope
The networks are finite, simple, undirected, connected, and have the same vertex count.

The homogeneous threshold is used only as the classical average-connectivity approximation
\[
1/\bar d.
\]
The spectral threshold is the adjacency-eigenvalue threshold of the SIS mean-field framework,
\[
1/\rho(A).
\]

The result is about reversal between two deterministic network summaries. It does not claim that either threshold is the exact extinction threshold of the finite stochastic SIS Markov chain.

The finite stochastic SIS process has an absorbing all-susceptible state. The spectral threshold here belongs to the deterministic or mean-field approximation described in the cited network-epidemic literature.

## Proof
At fixed \(n\), average degree is strictly increasing in edge count. Thus an opposite strict ranking can occur only if two connected graphs \(G,H\) satisfy
\[
|E(G)|<|E(H)|
\]
but
\[
\rho(G)>\rho(H).
\]

For
\[
2\le n\le5,
\]
all connected simple graphs are exhaustively generated from the
\[
2^{\binom n2}
\]
labeled adjacency patterns and reduced only after generation by exact relabeling canonicalization.

The numbers of connected unlabeled classes recovered are
\[
1,2,6,21
\]
for
\[
n=2,3,4,5,
\]
respectively.

For every class, the adjacency characteristic polynomial is computed exactly over the integers. Its largest real root is isolated by a rational interval. For every pair with different edge counts, the isolating intervals certify
\[
|E(G)|<|E(H)|
\Longrightarrow
\rho(G)\le\rho(H).
\]
Hence no strict density–spectral reversal exists below six vertices.

At six vertices, the star and cycle give a symbolic witness. The star spectrum has largest eigenvalue
\[
\sqrt5,
\]
while the cycle has spectral radius
\[
2.
\]
Since
\[
\sqrt5>2
\]
but
\[
5<6
\]
in edge count, the two rankings reverse.

For arbitrary
\[
n\ge6,
\]
\(K_{1,n-1}\) has \(n-1\) edges and spectral radius \(\sqrt{n-1}\), whereas \(C_n\) has \(n\) edges and spectral radius \(2\). The inequalities
\[
n-1<n
\]
and
\[
\sqrt{n-1}>2
\]
complete the persistent-family proof.

## Verification
The embedded `verify_epidemic_density_spectral_boundary.py` uses exact graph generation and SymPy exact characteristic polynomials with rational real-root isolation.

It generates every labeled simple graph for each
\[
2\le n\le5,
\]
filters for connectivity, and only then collapses label duplicates by testing every permutation.

It recovers the standard connected unlabeled graph counts
\[
1,2,6,21.
\]

For every connected class it computes the adjacency characteristic polynomial exactly and obtains a rational isolating interval for the spectral radius. Every pair whose edge counts differ is checked in the only direction capable of producing a reversal.

The script also checks the star-cycle persistent family for every
\[
6\le n\le100.
\]
The all-\(n\) statement itself is symbolic and does not depend on this finite replay.

The verification environment used SymPy 1.14.0 from the installed package path printed by the script.

Run:

`python3 verify_epidemic_density_spectral_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Wang, Chakrabarti, Wang, and Faloutsos contrast the classical homogeneous threshold based on inverse average connectivity with an arbitrary-graph epidemic threshold governed by the largest adjacency eigenvalue. Their paper explicitly gives the star threshold as the reciprocal square root of the hub degree.

Van Mieghem, Omic, and Kooij later formulate the N-intertwined SIS mean-field model and state the sharp mean-field threshold
\[
\tau_c=\frac1{\lambda_{\max}(A)}.
\]

Those sources establish why average connectivity and spectral radius are epidemiologically distinct summaries. They do not state the finite extremal question answered here: the smallest connected network order on which edge density can rank two networks in the opposite strict order from the spectral epidemic threshold.

Targeted searches using average degree, spectral radius, epidemic threshold, denser network, rank reversal, star, cycle, \(K_{1,5}\), and \(C_6\) did not locate this six-vertex boundary.

The mathematical ingredients that a cycle has spectral radius \(2\) and a star has spectral radius \(\sqrt{n-1}\) are standard. The accepted claim is the sharp universal minimum over all connected simple graphs, together with the persistent star-cycle family.

## Limitations
The finite lower-bound step is a complete exact census only through five vertices; the proof of existence at six vertices and persistence thereafter is symbolic.

The claim compares graphs of equal order. If graph order is allowed to vary, average degree and spectral radius can disagree in other trivial ways.

The result uses simple undirected unweighted contact networks. Directed, weighted, temporal, multilayer, or adaptive contact networks have different epidemic operators.

The spectral threshold is a mean-field threshold, not an exact phase transition of the finite stochastic SIS process.

An unindexed teaching example may contain the same star-cycle contrast even though the sharp six-vertex universal minimum was not located.

## References
1. Y. Wang, D. Chakrabarti, C. Wang, and C. Faloutsos, “Epidemic Spreading in Real Networks: An Eigenvalue Viewpoint,” *22nd Symposium on Reliable Distributed Systems*, 25–34, 6–8 October 2003. DOI: 10.1109/RELDIS.2003.1238052.
2. P. Van Mieghem, J. Omic, and R. Kooij, “Virus Spread in Networks,” *IEEE/ACM Transactions on Networking* 17(1), 1–14, 2009. DOI: 10.1109/TNET.2008.925623.

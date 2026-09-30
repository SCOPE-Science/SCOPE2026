# Exact small-order even-intersecting permutation families
## Finding
For permutations \(\sigma,\tau\in S_n\), let
\[
a(\sigma,\tau)=\bigl|\{i\in[n]:\sigma(i)=\tau(i)\}\bigr|.
\]
Call \(\mathcal F\subseteq S_n\) even-intersecting when \(a(\sigma,\tau)\) is even for every two distinct \(\sigma,\tau\in\mathcal F\), and let \(M(n)\) be the largest possible size of such a family. Then
\[
M(3)=3,\qquad M(4)=8,\qquad M(5)=13,\qquad M(6)=48.
\]
Moreover, there are exactly \(240\) labeled maximum even-intersecting families in \(S_5\), and they form a single orbit under independent relabeling of values and positions, namely the action
\[
\mathcal F\longmapsto \{\alpha\circ\sigma\circ\beta:\sigma\in\mathcal F\},\qquad \alpha,\beta\in S_5.
\]
A representative maximum family in \(S_5\), written in one-line notation, is
\[
\begin{aligned}
\{&(1,2,3,4,5),(1,2,4,5,3),(1,3,4,2,5),(2,3,1,4,5),\\
 &(2,5,1,3,4),(2,5,3,4,1),(3,4,5,1,2),(4,1,2,5,3),\\
 &(4,2,3,5,1),(4,5,2,3,1),(5,1,2,3,4),(5,1,4,2,3),\\
 &(5,3,1,2,4)\}.
\end{aligned}
\]

## Assumptions and scope
All permutations act on \([n]=\{1,\ldots,n\}\), and agreement means equality of images in the same position. The classification statement concerns labeled families as subsets of \(S_5\), with equivalence under the displayed left-right action. No claim is made here about \(M(n)\) for \(n\ge7\), or about a structural classification of all maximum families for \(n=4\) or \(n=6\).

## Proof
Common left composition preserves agreement counts. Thus, from any nonempty even-intersecting family, choose \(\tau\in\mathcal F\) and replace every \(\sigma\) by \(\tau^{-1}\circ\sigma\). The resulting family contains the identity. A permutation is compatible with the identity exactly when its number of fixed points is even.

For each \(n\), form a graph \(G_n\) whose vertices are the nonidentity permutations with an even number of fixed points, joining two vertices exactly when the corresponding permutations have an even number of agreements. Then normalization gives the exact reduction
\[
M(n)=1+\omega(G_n).
\]
The supplied verifier constructs \(G_n\) without pruning any vertices. It finds respectively \(2,15,64,415\) normalized candidates for \(n=3,4,5,6\). An exact branch-and-bound maximum-clique search uses a greedy proper coloring of each residual graph as an upper bound; every recursive branch either includes a chosen vertex or is subsequently explored after that vertex is excluded. The certified clique numbers are
\[
\omega(G_3)=2,\qquad \omega(G_4)=7,\qquad \omega(G_5)=12,\qquad \omega(G_6)=47,
\]
which proves the four exact values.

For the lower bounds at even orders, the pair-block wreath product \(S_2\wr S_{n/2}\) is even-intersecting: the quotient of any two members preserves the partition into pairs, so each fixed pair contributes either zero or two fixed points. Its size is \(2^{n/2}(n/2)!=n!!\), giving sizes \(8\) and \(48\) at \(n=4,6\). At \(n=3\), the cyclic subgroup of order three is even-intersecting. The displayed thirteen-element family supplies the lower bound at \(n=5\).

For the \(n=5\) classification, a second exhaustive Bron--Kerbosch routine on the same explicitly constructed graph enumerates exactly \(26\) maximum normalized families containing the identity. Left translation of these families produces exactly \(240\) distinct labeled maximum families. The verifier then applies all \(120^2\) left-right relabelings to one representative and obtains precisely this complete set of \(240\) families, proving that there is one left-right orbit.

## Verification
Running `python3 verify_even_intersecting.py` rebuilds every permutation and compatibility edge from the definition, redoes the exact maximum-clique computations for \(3\le n\le6\), enumerates the normalized \(n=5\) maxima, reconstructs all labeled maxima by translation, checks the single left-right orbit, and ends with `VERIFY_OK`. The recorded output is supplied in `verify_output.txt`.

## Relationship to prior work
Banerjee, Dewan, and Mishra introduced the current formulation and notation \(M(n)\), proving general asymptotic bounds for even \(n\), constructions for odd \(n\), and identifying the problem as a permutation analogue of Eventown. Their public abstract does not state the exact values above or the \(S_5\) maximum-family classification. The values \(M(4)=8\) and \(M(6)=48\) show that their general even-order construction is sharp at the first two nontrivial even orders; \(M(5)=13\) gives an exact first small odd-order benchmark beyond the elementary cases.

## Limitations
The upper bounds are finite exhaustive results, not a general formula. The \(S_5\) orbit classification is under the stated left-right action and does not assert a description of the full automorphism group of the compatibility graph. The closest 2026 source was available through its public abstract and metadata; exact-term literature searches found no matching small-order values, but section-level comparison with the full 31-page text could not be completed through the available public interface. Thus the novelty statement is best-of-knowledge rather than an absolute priority claim.

## References
[1] A. Banerjee, A. Dewan, R. Mishra, “Even-Intersecting Families of Permutations,” arXiv:2609.21645v1, first public version 2026-09-18.

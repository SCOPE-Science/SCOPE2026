# Exact face vector on the \(n=k+6\) squared-cycle cut-complex diagonal
## Finding
For every integer \(k\ge3\), let \(W_{k+6}=C_{k+6}^2\) be the square of the cycle on \(k+6\) vertices and let \(\Delta_k(W_{k+6})\) be its ordinary \(k\)-cut complex. Then its face vector is \[\left(\binom{k+6}{1},\binom{k+6}{2},\binom{k+6}{3},\binom{k+6}{4},\frac{k(k+6)(k^2+3k+8)}6,\frac{(k-1)(k+6)(3k^2-k+8)}{12}\right),\] and its reduced Euler characteristic is \[\widetilde\chi(\Delta_k(W_{k+6}))=-\frac{k^4+2k^3-21k^2+18k+8}{8}.\] Consequently, if the published shellability conjecture for \(\Delta_k(W_n)\) at \(n\ge k+6\) holds on this first diagonal, then \[\Delta_k(W_{k+6})\simeq\bigvee^{b(k)}S^5,\qquad b(k)=\frac{k^4+2k^3-21k^2+18k+8}{8}.\]

## Assumptions and scope
For an integer \(n\ge5\), write \(W_n=C_n^2\) for the graph on \(\mathbb Z/n\mathbb Z\) in which two vertices are adjacent exactly when their cyclic distance is one or two. For a graph \(G\), the ordinary \(k\)-cut complex \(\Delta_k(G)\) is the simplicial complex whose facets are complements of disconnected induced \(k\)-vertex subgraphs. Here \(n=k+6\) and \(k\ge3\), so every facet has six vertices and the complex is pure of dimension five.

Represent a six-set \(F\subseteq\mathbb Z/n\mathbb Z\) by its cyclic binary word, with a one at each vertex of \(F\). A **one-run** is a maximal cyclic block of consecutive ones.

## Proof
Let \(S=V(W_n)\setminus F\). Passing across a one-run of length one is possible inside \(W_n[S]\): the two surviving vertices on its sides have cyclic distance two and hence are adjacent. Passing across a one-run of length at least two is impossible, because the two surviving vertices on its sides have cyclic distance at least three. Therefore \(W_n[S]\) is disconnected exactly when the cyclic word of \(F\) has at least two one-runs of length at least two.

For a six-set, let \(r\) be the number of one-runs. The number of ordered compositions of six into \(r\) positive run lengths having at least two parts at least two is respectively \(3,7,6\) for \(r=2,3,4\), and zero otherwise. The \(k\) zeros are split into \(r\) positive cyclic gaps in \(\binom{{k-1}}{{r-1}}\) ways. For fixed ordered one-run and zero-gap compositions, there are \((k+6)/r\) cyclic binary words, because each word has \(r\) possible distinguished one-run starts. Hence the number of facets is
\[
f_5=\frac{k+6}{2}3\binom{k-1}{1}+\frac{k+6}{3}7\binom{k-1}{2}+\frac{k+6}{4}6\binom{k-1}{3}
=\frac{(k-1)(k+6)(3k^2-k+8)}{12}.
\]

Now consider a five-set \(R\). It fails to be a face exactly when no added vertex turns it into a six-set with two long one-runs. There are precisely two such types. First, if \(R\) is one run of length five, adding one vertex leaves at most one long run. Second, if all five vertices of \(R\) are isolated on the cycle, adding one vertex can create at most one long run. Conversely, every other five-set has either two long runs already or one long run together with another run; because the number of zeros is \(k+1\ge4\), one can add a zero adjacent to a suitable other run without merging away the existing long run. Thus the nonfaces of size five are the \(k+6\) cyclic intervals of length five together with the independent five-sets of \(C_{{k+6}}\). The latter number is
\[
\frac{k+6}{k+1}\binom{k+1}{5}.
\]
Therefore
\[
f_4=\binom{k+6}{5}-(k+6)-\frac{k+6}{k+1}\binom{k+1}{5}
=\frac{k(k+6)(k^2+3k+8)}6.
\]

Every four-set is contained in a facet. Indeed, if it already has two long runs, extend it while avoiding a gap vertex that would merge them. If it has exactly one long run and at least one other run, add a vertex next to a different run. If it is a single run of length four, the complement contains a cyclic interval of at least five zeros, so two adjacent interior zeros create a second long run. If it is independent, two suitable neighboring zeros extend two distinct isolated vertices to two long runs. These constructions use at most two added vertices. Consequently every set of size at most four is also a face, giving
\[
f_j=\binom{k+6}{j+1}\qquad(0\le j\le3).
\]
Substitution in the reduced Euler sum yields
\[
\widetilde\chi=-1+f_0-f_1+f_2-f_3+f_4-f_5
=-\frac{k^4+2k^3-21k^2+18k+8}{8}.
\]

A pure shellable five-dimensional complex is homotopy equivalent to a wedge of five-spheres. Thus, conditional on the published shellability conjecture at \(n=k+6\), the number of spheres must be \(-\widetilde\chi\), which is the displayed \(b(k)\).

## Verification
The accompanying `artifacts/verify.py` independently constructs \(W_{k+6}\), tests induced connectivity for every six-subset, takes the full downward closure, and checks the stated six-entry face vector and reduced Euler characteristic for every \(3\le k\le14\). The saved replay output ends with `VERIFY_OK`.

The finite replay is only a cross-check. The theorem for every \(k\ge3\) is proved by the cyclic-run characterization and counting argument above.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced these cut complexes and, for squared cycles, conjectured that \(\Delta_k(W_n)\) is shellable for \(n\ge k+6\). Their paper reports finite computational support but does not state the all-\(k\) face vector on the first diagonal \(n=k+6\).

Chauhan, Shukla, and Vinayak proved the squared-cycle shellability conjecture when the cut size is three. At \(k=3\), their theorem is compatible with the present formula, which gives one five-sphere for \(W_9\); their result does not imply the uniform formulas for \(k\ge4\).

The closest published database finding located for the same graph family gives the face vector and Euler characteristic on the adjacent diagonal \(n=k+5\). That statement has five-dimensional complements of size five rather than six and does not imply the formulas here. The present diagonal is structurally distinct because it is the first diagonal lying in the published shellability conjecture.

## Limitations
This result does not prove shellability for \(k\ge4\), nor does it determine attaching maps independently of that conjecture. The sphere-wedge statement is explicitly conditional. Finite enumeration through \(k=14\) is not used as an infinite proof. A differently phrased or non-indexed duplicate remains a residual bibliographic risk.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675; SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675, DOI 10.1137/23M1569034. First public version: 2023-04-26.
2. P. Chauhan, S. Shukla, and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979. First public version: 2024-06-04.

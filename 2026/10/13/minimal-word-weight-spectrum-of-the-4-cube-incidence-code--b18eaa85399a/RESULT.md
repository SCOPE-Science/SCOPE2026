# Minimal-word weight spectrum of the \(4\)-cube incidence code
## Finding
Let \(Q_4\) be the four-dimensional binary hypercube, let \(B\) be its \(16\times32\) vertex-edge incidence matrix over \(\mathbb F_2\), and let
\[
C=\operatorname{rowsp}[I_{16}\mid B]\le \mathbb F_2^{48}.
\]
The complete Hamming-weight enumerator of the nonzero minimal codewords of \(C\) is
\[
\begin{aligned}
M_C(z)={}&16z^{5}+32z^{8}+96z^{11}+24z^{12}+256z^{14}+192z^{15}+105z^{16}\\
&+656z^{17}+704z^{18}+704z^{19}+2072z^{20}+2640z^{21}+2584z^{22}\\
&+4752z^{23}+5992z^{24}+5040z^{25}+4800z^{26}+3520z^{27}\\
&+1556z^{28}+1024z^{29}+480z^{30}+48z^{31}.
\end{aligned}
\]
In particular, \(C\) is a binary \([48,16,5]\) code and has exactly \(37{,}293\) nonzero minimal codewords.

## Assumptions and scope
The vertices of \(Q_4\) are the binary four-tuples, with two vertices adjacent when they differ in one coordinate. For a nonempty vertex set \(T\subseteq V(Q_4)\), write \(c_T\) for the sum of the rows of \([I_{16}\mid B]\) indexed by \(T\). A nonzero codeword is minimal when no nonzero codeword has strictly smaller support contained in its support.

The statement is a complete finite classification for this one canonical code. It does not assert a general closed formula for the corresponding code of \(Q_d\) when \(d\ge5\).

## Proof
The identity block of \(c_T\) is the characteristic vector of \(T\). In the incidence block, an edge coordinate is nonzero exactly when the edge has one endpoint in \(T\) and one endpoint outside \(T\). Thus the second block is the characteristic vector of the edge boundary \(\delta(T)\), and
\[
\operatorname{wt}(c_T)=|T|+|\delta(T)|.
\]
Since \(Q_4\) is four-regular, if \(e(T)\) is the number of edges induced by \(T\), then
\[
|\delta(T)|=4|T|-2e(T),
\qquad
\operatorname{wt}(c_T)=5|T|-2e(T).
\]

For graph-incidence codes of the form \([I\mid B]\), the incidence-code characterization identifies minimal codewords with connected induced vertex sets. In this case the equivalence is also verified directly: because the identity part of any codeword records its row-index set, a support-contained nonzero codeword below \(c_T\) must be \(c_S\) for a nonempty proper subset \(S\subset T\). Exhaustive support-containment testing over all \(2^{16}-1\) nonzero row sums agrees exactly with the independent connectivity test on \(Q_4[T]\).

Enumerating every nonempty \(T\subseteq V(Q_4)\), retaining exactly those for which \(Q_4[T]\) is connected, and tallying \(5|T|-2e(T)\) gives the coefficients displayed above. The coefficient sum is
\[
\sum_w [z^w]M_C(z)=37{,}293.
\]
A singleton vertex gives weight \(5\), so the minimum distance is \(5\).

## Verification
The standalone verifier constructs the \(32\) edges of \(Q_4\), constructs all \(65{,}535\) nonzero codewords from their row-index masks, and performs two finite checks.

First, it tests connectivity of every induced vertex set and tallies its codeword weight both directly and from \(5|T|-2e(T)\). Second, independently of connectivity, it checks minimality by testing every nonempty proper submask for support containment. The two accepted-mask lists agree exactly. The verifier then compares the resulting spectrum against the embedded expected coefficients and terminates with `VERIFY_OK`.

The connected-set count by cardinality is also checked and sums to \(37{,}293\), matching the independently catalogued total number of connected induced subgraphs of \(Q_4\).

## Relationship to prior work
Kim's incidence-matrix paper proves the graph-to-minimal-codeword correspondence and gives exact counts for paths, cycles, complete bipartite and multipartite graphs, and ladders. The full article does not give a hypercube specialization or a Hamming-weight distribution for the minimal words.

The total \(37{,}293\) connected induced subgraphs of \(Q_4\) is already catalogued as OEIS A290758 and is therefore not claimed as new. The contribution here is the refinement by the codeword weight \(|T|+|\delta(T)|\), equivalently by the joint vertex-count/internal-edge statistic through \(5|T|-2e(T)\).

Kurz studies the analogous construction obtained by adjoining an identity matrix to a graph adjacency matrix. That is a different binary code from the incidence-matrix code considered here and does not imply this spectrum. General work on counting connected sets in regular graphs likewise controls totals rather than the displayed incidence-code weight refinement.

## Limitations
This is an exact finite result for \(Q_4\), not an asymptotic theorem or a formula for all hypercubes. The exhaustive computation proves the stated finite spectrum but does not by itself establish any pattern in higher dimension. The total number of minimal words was previously known via connected-subgraph enumeration; only the weight-resolved refinement is asserted here. An unindexed older enumeration of connected \(Q_4\) subsets by edge boundary could contain equivalent numerical data; no such table was found in the inspected primary sources or targeted searches.

## References
1. B. Kim, *Minimal binary codewords derived from the incidence-matrix approach*, Computational and Applied Mathematics 45 (2026), article 200. DOI: 10.1007/s40314-025-03580-6. Published online 5 January 2026.
2. OEIS Foundation, A290758, *Number of (non-null) connected induced subgraphs in n-hypercube Q_n*.
3. S. Cambie, J. Goedgebeur, and J. Jooken, *The maximum number of connected sets in regular graphs*, arXiv:2311.00075.
4. S. Kurz, *On the number of minimal codewords in codes generated by the adjacency matrix of a graph*, arXiv:2006.02975.

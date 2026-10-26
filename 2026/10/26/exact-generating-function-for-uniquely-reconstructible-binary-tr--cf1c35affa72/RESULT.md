# Exact generating function for uniquely reconstructible binary trigram multispectra

## Finding
For each binary word \(w\) of length \(n\ge3\), its **trigram multispectrum** is the eight-vector of occurrence counts of every contiguous binary substring of length three, overlaps included. Let \(U_n\) be the number of \(w\) whose multispectrum has exactly one preimage among length-\(n\) binary words. Then
\[
\sum_{t\ge1} U_{t+2}z^t=\frac{2z(4+3z+6z^2+6z^3+7z^4-11z^7-8z^8-4z^9-z^{10}+z^{11}+2z^{12}+z^{13})}{(1-z)^3(1+z)(1+z^2)(1+z+z^2)}.
\]
In particular \(U_n=\tfrac12n^2+14n+O(1)\). At \(n=3,\ldots,15\), the counts are \(8,14,26,46,74,92,124,142,166,196,224,240,280\), respectively.

## Assumptions and scope
Words are linear, not cyclic, over \(\{0,1\}\). Multiplicities of all eight trigrams are retained, and factors overlap in the usual way. Two distinct words are treated as different even when related by reversal or alphabet complementation. The theorem holds for every integer \(n\ge3\); there is no claim about longer read lengths or noisy observations. All generating functions are formal power series over rational numbers.

## Proof
Represent the eight trigrams by the directed edges of the order-two binary de Bruijn graph, whose vertices are \(00,01,10,11\), in this order, and whose edges in lexicographic order are
\[
00\to00,\ 00\to01,\ 01\to10,\ 01\to11,\ 10\to00,\ 10\to01,\ 11\to10,\ 11\to11.
\]
An observed vector fixes the corresponding directed edge multiplicities. Every compatible binary word is exactly a directed Euler trail in that multigraph, where parallel copies of an edge type are indistinguishable. The beginning and ending two-bit blocks are the trail endpoints.

If all vertex degrees are balanced and the support contains at least two vertices, beginning the same Euler circuit at different active vertices produces different words. If its support has one vertex, the spectrum arises from exactly one of the two constant words; together these contribute \(2z/(1-z)\), where \(z\) tracks the number of trigram windows. Otherwise a uniquely reconstructible word must have a unique start vertex \(s\) and a distinct unique terminal vertex \(t\), with imbalance \(+1\) at \(s\), \(-1\) at \(t\), and zero elsewhere.

For an unbalanced feasible edge-multiplicity vector, the last-exit decomposition of directed Euler trails gives a root-directed in-arborescence on active vertices toward \(t\), obtained by marking each nonterminal vertex's final outgoing edge type. Conversely every such arborescence, together with an ordering of outgoing edge types at each vertex having the marked edge as final exit, reconstructs a trail; repeated parallel edges are indistinguishable. Therefore exactly one trail exists if and only if the *edge-type support* admits exactly one such arborescence, the terminal vertex has at most one outgoing type, and, at every other vertex with two outgoing types, the unique tree's outgoing type has multiplicity exactly one. Indeed the local number of orderings at a nonterminal vertex with a marked type of multiplicity \(i\) and another type of multiplicity \(j\) is \(\binom{i+j-1}{i-1}\); at the terminal vertex it is \(\binom{i+j}{i}\). These factors all equal one exactly under the stated conditions. When there are multiple arborescences their associated last-exit edge-type choices yield distinct trails.

The complete exact symbolic enumeration is implemented by `derive_gf.py` and `supports.py`, provided here in full. Let \(a,b,c,d,e,f,g,h\) denote trigram multiplicities in lexicographic order, and let \(\delta_v=\mathbf1_{v=s}-\mathbf1_{v=t}\). The degree-imbalance equations solve as
\[
b=e+\delta_{00},\quad g=d+\delta_{11},\quad f=c+d-e-\delta_{00}-\delta_{01}.
\]
Thus the number of windows is
\[
a+h+2c+3d+e+\delta_{11}-\delta_{01}.
\]
Enumerate the \(2^8\) possible edge-type supports; for each active terminal vertex test support-arborescences by direct enumeration of one nonloop exit per nonterminal vertex; retain exactly one rooted arborescence, the stated outgoing-type restrictions, and each distinct active start vertex. Each multiplicity on a selected edge is positive, each absent edge has multiplicity zero, and a marked last-exit type at a branching vertex has multiplicity one. The three independent variables \(c,d,e\) then run over explicit ranges, subject to the one remaining condition on \(f\). The evaluator uses the identity
\[
\sum_{e=L}^{\infty}z^e\mathbf1_{\{e\le c+d-K\}}=\frac{z^L-z^{c+d-K+1}}{1-z}\mathbf1_{\{c+d\ge K+L\}}
\]
with its finite-range analogue. It counts exactly 136 feasible nonzero support/start/end generating-function cases. Add the balanced constant-word contribution. Exact cancellation of the resulting finite rational sum against the displayed closed form is checked by the last assertion in `derive_gf.py`; this is an all-length symbolic identity, not interpolation from initial data.

At \(z=1\), the other three denominator factors have product \(12\), while the numerator takes value \(12\). The coefficient of \((1-z)^{-3}\) is consequently \(1\), and that of \((1-z)^{-2}\) is \(29/2\). Extracting coefficients with \(t=n-2\) gives \(U_n=n^2/2+14n+O(1)\); the remaining simple poles occur at roots of unity and contribute only bounded fluctuations.

## Verification
Run `python derive_gf.py` with Python 3 and SymPy installed to independently reconstruct and cancel the complete rational generating-function identity from the 256 possible supports. It prints `EXACT_GF_PASS` and the count 136 only after exact symbolic equality succeeds. Run `python verify.py` using only Python's standard library; it enumerates *all* binary words at each length 3 through 18, computes their trigram multispectrum multiplicities directly, counts singleton fibers, and compares each exact count to the proposed rational-series coefficients. Both scripts were run against the files embedded with this result and passed.

## Relationship to prior work
The substring-multispectrum reconstruction model is studied by Gabrys and Milenkovic (2018), whose paper focuses on constructing uniquely reconstructible codebooks and read-length scaling rather than counting every uniquely reconstructible word at a fixed read length of three. Bals, Pissis, and Tinca (2026) study exact enumeration of node-distinct Euler trails in a supplied directed multigraph; their Euler-trail viewpoint underlies the reconstruction, but their results do not enumerate singleton binary trigram fibers over all word lengths. Chakraborty and coauthors (2026) address related *presence-only* spectrum-preserving string-set questions, not multisets with multiplicities. This theorem counts singleton fibers, which differs from the number of all distinct trigram spectra and the maximum size of a code selecting one representative from each spectrum.

## Limitations
No independent external mathematical audit has been performed. This is a self-reviewed mathematical proof plus reproducible symbolic and finite checks. The literature search did not establish absolute priority: equivalent formulas in unindexed combinatorics-on-words or genome-assembly literature remain possible. The bound applies to exact, noiseless linear binary trigram multispectra only. The symbolic derivation requires SymPy, while the direct verifier uses only the Python standard library.

## References
1. M. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (first public 2018-04-12), https://arxiv.org/abs/1804.04548.
2. A. Bals, S. P. Pissis, and M. Tinca, *Optimal Enumeration of Eulerian Trails in Directed Graphs*, arXiv:2603.12894 (first public 2026-03-13), https://arxiv.org/abs/2603.12894.
3. D. Chakraborty, R. Grossi, D. Kimura, N. Punzi, K. Sadakane, and H. Zuba, *Variations on the Problem of Identifying Spectrum-Preserving String Sets*, arXiv:2602.19408 (first public 2026-02-23), https://arxiv.org/abs/2602.19408.

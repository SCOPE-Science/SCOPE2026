# Exact rational generating function for binary trigram-count spectra

## Finding
For a binary word \(w\) of length \(n\geq3\), its **trigram-count spectrum** is the eight-vector recording the number of occurrences of each contiguous length-three word, with overlaps and multiplicities. Let \(M_n\) be the number of different such eight-vectors realized by binary words of length \(n\). Put \(M_2=1\) as the empty-spectrum convention. Then
\[
\sum_{t\geq0}M_{t+2}z^t
=\frac{1+5z-6z^2+5z^3-z^4+6z^5+3z^6+z^7-z^8-2z^9+2z^{10}}{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.
\]
The first values for \(n=3,4,\ldots,16\) are
\[
8,15,28,52,92,151,240,363,532,757,1048,1416,1880,2449.
\]
The asymptotic is \(M_n\sim\frac{13}{288}n^4\) as \(n\to\infty\). Equivalently, \(M_n\) is the maximum cardinality of a binary length-\(n\) code in which no two codewords produce the same *multiplicity-aware length-three read spectrum*.

## Assumptions and scope
Words are linear, not circular. Their length-three windows overlap; the recorded spectrum retains multiplicities but forgets window order. Distinct words with the same spectrum count once. The code interpretation is a **noiseless complete-multiset observation channel**, not an edit-correction assertion. The formula applies for every integer \(n\geq3\) and is not a numerical extrapolation.

## Proof
Construct the binary order-two de Bruijn digraph with vertices \(A=00\), \(B=01\), \(C=10\), \(D=11\). The eight possible trigram edges in their word order are
\[
000:A\to A,\quad001:A\to B,\quad010:B\to C,\quad011:B\to D,\quad
100:C\to A,\quad101:C\to B,\quad110:D\to C,\quad111:D\to D.
\]
Name their nonnegative multiplicities \(a,b,c,d,e,f,g,h\), respectively. An eight-vector is realized by a binary word exactly when its positive-multiplicity directed multigraph admits an Euler trail. Such a trail traverses one edge per contiguous trigram; conversely its initial two bits followed by each new edge bit spell a realizing word. The directed Euler criterion is: all nonisolated vertices have connected underlying undirected support and vertex imbalances (outdegree minus indegree) are either all zero or \(+1\) and \(-1\) at two distinct vertices.

Specify imbalances at \((A,B,D)\) as \((\alpha,\beta,\delta)\), and hence at \(C\) as \(-\alpha-\beta-\delta\). The allowable pattern set \(\mathcal P\) consists of the zero pattern and the twelve distinct ordered start/end vertex differences. Flow conservation determines
\[
b=e+\alpha,\qquad g=d+\delta,\qquad c=e+f-d+\alpha+\beta.
\]
Let \(k=\alpha+\beta\), \(C=2\alpha+\beta+\delta\), \(E=\max(0,-\alpha)\), and \(D_0=\max(0,-\delta)\). The six nonloop edges are thus specified exactly once by integers satisfying
\[
e\geq E,\qquad d\geq D_0,\qquad f\geq0,\qquad d\leq e+f+k,
\]
with nonloop total \(s=3e+d+2f+C\). Every *nonempty* nonloop support so obtained is connected: disconnection on four vertices would require the two disjoint edge supports \(AB\) and \(CD\), or \(AC\) and \(BD\). In either case all four vertices have nonzero imbalance, contradicting membership in \(\mathcal P\). Thus the degree condition is sufficient as well as necessary.

The loop at \(A\) may have positive multiplicity only if \(b+e>0\); likewise the loop at \(D\) only if \(d+g>0\), except when that loop alone is the entire graph. For a nonloop core, let \(F_{\alpha\beta\delta}(z)\) count its admissible \((e,d,f)\) with weight \(z^s\), and let \(F_A,F_D,F_{AD}\) denote the restrictions where the corresponding endpoint is unvisited (respectively \(b=e=0\), \(d=g=0\), and both). Summation of the two possible loop counts gives
\[
G_{\alpha\beta\delta}(z)
=\frac{F_{\alpha\beta\delta}(z)-zF_A(z)-zF_D(z)+z^2 F_{AD}(z)}{(1-z)^2}.
\]
The numerator corrects for forbidden loops; at the zero-edge core it leaves precisely the empty vector, not two disconnected loops. The two nonempty loop-only spectra contribute separately \(2z/(1-z)\).

Here are finite expressions for every restricted series, making the rational-function evaluation reproducible for all lengths. Define
\[
U_{p,q}(E,R;z)=z^{pE}\left(
\frac{1}{(1-z^p)(1-z^q)}
-\sum_{\substack{i,j\geq0\\i+j<R}}z^{pi+qj}\right).
\]
The finite sum is empty if \(R=0\). Set \(R=\max(0,D_0-k-E)\) and \(L_A=\max(0,D_0-k)\). Geometric summation first over \(d\), then over \(e,f\), yields
\[
F_{\alpha\beta\delta}(z)=
\frac{z^{C+D_0}U_{3,2}(E,R;z)-z^{C+k+1}U_{4,3}(E,R;z)}{1-z}.
\]
When \(\alpha=0\),
\[
F_A(z)=\frac{1}{1-z}\left(
\frac{z^{C+D_0+2L_A}}{1-z^2}-
\frac{z^{C+k+1+3L_A}}{1-z^3}\right);
\]
otherwise \(F_A(z)=0\). When \(\delta=0\),
\[
F_D(z)=z^C U_{3,2}\big(E,\max(0,-k-E);z\big);
\]
otherwise \(F_D(z)=0\). Finally, if \(\alpha=\delta=0\),
\[
F_{AD}(z)=\frac{z^{C+2\max(0,-k)}}{1-z^2};
\]
otherwise \(F_{AD}(z)=0\). In each formula the only possible negative powers in intermediate terms cancel, since it enumerates nonnegative edge counts. The expressions follow directly from the displayed inequalities, so no experimental pattern recognition is used.

Summing the thirteen explicitly defined patterns and collecting rational terms,
\[
\frac{2z}{1-z}+\sum_{(\alpha,\beta,\delta)\in\mathcal P}G_{\alpha\beta\delta}(z)
=\frac{1+5z-6z^2+5z^3-z^4+6z^5+3z^6+z^7-z^8-2z^9+2z^{10}}{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.
\]
This proves the generating function for every length. Its unique pole of highest order at \(z=1\) has leading term \((13/12)(1-z)^{-5}\); therefore \(M_n\sim (13/12)n^4/4!=13n^4/288\). Other roots of unity have poles of smaller order.

## Verification
Run `python3 verify.py` in the directory containing this document and the script. It independently enumerates admissible lattice flows through \(30\) nonloop-window counts and directly enumerates all binary words at lengths \(3\) through \(17\). Both agree coefficientwise with the rational generating function; the program prints `VERIFY_OK`. The formula itself is established by the preceding Euler-trail proof and rational identities, not by these finite checks. A computer algebra expansion of the thirteen displayed rational terms is an optional supplementary check.

## Relationship to prior work
En Gad (2026) uses substring-count vectors in binary error-correcting code constructions, motivating exact enumeration of fixed-length spectra, but does not supply this length-three spectral cardinality generating function. The classical rationality theorem of Cassaigne–Karhumäki–Puzynina–Whiteland (2017) counts the *finer* equivalence requiring all factor counts of lengths at most three, not the current length-three-only observation. For example, `0101` and `1010` have equal trigram multispectra but different bigram counts. The earlier Bernadini–Conte–Gabory–Grossi–Loukides–Pissis–Punzi–Sweering (2022) problem uses **sets** of length-\(k\) factors without multiplicity and optimizes shortest realizing strings, so its invariant also differs. Prior degree-two spectrum enumeration does not imply the present four-degree quasipolynomial.

## Limitations
This theorem counts spectra, not reconstruction ambiguity-class sizes, error-correcting code rates, or higher-order spectra. It establishes no formula for arbitrary trigram alphabet size or window length. The closest rationality paper's full publisher version was not accessed during comparison, so an equivalent unindexed special enumeration cannot be absolutely excluded. No independent external scientific audit is asserted.

## References
- E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, first public 16 September 2026, https://arxiv.org/abs/2609.19493.
- J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *k-Abelian Equivalence and Rationality*, Fundamenta Informaticae 154 (2017), 65–94, https://doi.org/10.3233/FI-2017-1553.
- G. Bernardini et al., *On Strings Having the Same Length-k Substrings*, CPM 2022, https://doi.org/10.4230/LIPIcs.CPM.2022.16.

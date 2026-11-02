# Exact ternary adjacent-pair frequency-profile enumerator

## Finding

For a linear word \(w=w_1\cdots w_n\) on the labeled ternary alphabet \(\Sigma=\{0,1,2\}\), let \(M(w)=(m_{ij})_{i,j\in\Sigma}\) record the number of adjacent occurrences of each **ordered** pair \(ij\). Let \(A_n\) be the number of distinct matrices \(M(w)\) realized by words of length \(n\). With the transition-count variable \(z\), define \(G(z)=\sum_{t\ge0}A_{t+1}z^t\). Then, for every \(n\ge1\),

\[
G(z)=\frac{1+5z-8z^2+8z^3+13z^4-4z^5-10z^6-8z^7+11z^8+2z^9-5z^{10}+2z^{11}}{(1-z)^7(1+z)^2(1+z+z^2)}.
\]

In particular \((A_1,\ldots,A_{16})=(1,9,24,65,156,342,683,1272,2226,3708,5919,9120,13625,19827,28188,39269)\) and

\[
A_n\sim \frac{7}{8640}(n-1)^6\quad(n\to\infty).
\]

Equivalently, the maximum number of ternary length-\(n\) words with mutually distinct ordered adjacent-pair count vectors is exactly \(A_n\): select one representative from each realizable profile.

## Assumptions and scope

The alphabet has precisely three distinct labeled symbols, and the words are **linear**, not circular. Every adjacent pair contributes once, with no wraparound pair. The two-gram profile is a vector of nine nonnegative integers. The empty edge multiset at \(n=1\) yields a single profile, even though there are three possible singleton words. Two words have the same profile precisely when their nine pair counts agree; their initial symbols are not separately part of the observation. No distributional or stochastic assumptions are imposed.

## Proof

**1. Euler-trail characterization.** Interpret \(m_{ij}\) as the multiplicity of the directed arc \(i\to j\), loops included, in a three-vertex directed multigraph. A matrix with \(t=\sum_{i,j}m_{ij}\) is realized by a linear word with \(t+1\) letters if and only if its arcs can be traversed in an Euler trail. For \(t>0\), the necessary and sufficient conditions are: (a) the vertices incident with positive-degree arcs induce a weakly connected graph, and (b) their outdegree-minus-indegree vector is either zero or \(\mathbf e_a-\mathbf e_b\) for distinct vertices \(a,b\). Sufficiency follows by adjoining one \(b\to a\) arc in the latter case, obtaining a balanced connected directed multigraph with an Euler circuit, then removing that added arc. The Euler circuit criterion remains valid with loops and parallel arcs. For \(t=0\), the zero matrix is realized by all singleton words but counted once.

**2. Support partition.** Ignore loops to define the *off-diagonal active set*: a symbol is active when it is incident with an arc whose endpoints differ. If it is empty, the only realizable positive-length arc matrices are the three single-symbol pure-loop profiles, with generating function \(3z/(1-z)\). If the off-diagonal active set has exactly two vertices, there are three choices of the unordered pair and two types of trail. For a closed trail, the opposite arc counts coincide and are positive, contributing \(3z^2/((1-z^2)(1-z)^2)\). For an open trail, their counts differ by exactly one; there are six ordered endpoint choices, contributing \(6z/((1-z^2)(1-z)^2)\). Only the two active vertices may bear loops, accounting for the factor \((1-z)^{-2}\). Loops at a third isolated vertex would destroy weak connectivity and are excluded.

**3. All three vertices active.** Orient the triangle as \(0\to1\to2\to0\). Let \(f_{01},f_{12},f_{20}\) be the differences of forward-minus-reverse arc multiplicities. Fixing one integer net flow \(f\) across an unordered pair contributes \(z^{|f|}/(1-z^2)\), because an arbitrary number of opposite arc pairs can be added. For zero divergence, all three net flows equal one common integer \(k\), so the off-diagonal generating function before connectivity restriction is

\[
C(z)=\frac{\sum_{k\in\mathbb Z}z^{3|k|}}{(1-z^2)^3}
=\frac{1+z^3}{(1-z^3)(1-z^2)^3}.
\]

The off-diagonal balanced matrices that fail to activate all three vertices consist of the zero matrix and exactly three two-vertex families with \(h\ge1\) opposite arcs in each direction. Hence the generating function for balanced matrices with all three vertices active is \(C(z)-1-3z^2/(1-z^2)\).

For divergence \(\mathbf e_0-\mathbf e_1\), the three net flows are \((k,k-1,k-1)\), where \(k\in\mathbb Z\). Splitting the integer sum into \(k\le0\) and \(k\ge1\) gives

\[
O(z)=\frac{\sum_{k\in\mathbb Z}z^{|k|+2|k-1|}}{(1-z^2)^3}
=\frac{z+z^2}{(1-z^3)(1-z^2)^3}.
\]

The only two-vertex off-diagonal profiles for these prescribed endpoints have arc counts \((h+1,h)\), \(h\ge0\), and generating function \(z/(1-z^2)\). Therefore \(O(z)-z/(1-z^2)\) counts profiles with all three vertices active for these endpoints. By ternary-label symmetry there are six possible ordered endpoint pairs. Every all-three-active off-diagonal support is weakly connected, and arbitrary loops at all three vertices contribute \((1-z)^{-3}\).

**4. Combination and simplification.** These classes are disjoint, because a nonzero divergence determines its ordered endpoints, while the balanced case has zero divergence. Counting matrices rather than Euler trails avoids multiplicity from different traversals. Thus

\[
G(z)=1+\frac{3z}{1-z}
+\frac{3z^2+6z}{(1-z^2)(1-z)^2}
+\frac{C(z)-1-\frac{3z^2}{1-z^2}+6\left(O(z)-\frac{z}{1-z^2}\right)}{(1-z)^3}.
\]

Multiplication of rational functions and cancellation yields the displayed rational function. The numerator evaluates to \(7\) at \(z=1\) and the two other denominator factors there multiply to \(12\), so the leading pole is \((7/12)(1-z)^{-7}\). Its coefficients are therefore \(\frac{7}{12}\binom{t+6}{6}+O(t^5)\); all other poles have lower order and lie at roots of unity. For \(t=n-1\), this proves the asymptotic and all exact coefficients. Every step is an identity of formal power series; no asymptotic argument is used to infer any finite coefficient. This finishes the proof.

## Verification

Two separate standard-library Python programs independently check the displayed formula and its supporting finite cases. `verify_words.py` enumerates all \(3^n\) ternary words for \(1\le n\le11\), collects their nine-entry adjacent-pair vectors, and compares their cardinalities with the coefficient recurrence derived from the rational function. `verify_matrices.py` independently enumerates all nine-entry nonnegative matrices of total arc count \(t\le14\), tests the Euler-trail conditions including weak connectivity, and matches the resulting counts to an independent integer-net-flow summation. Both programs completed with all equality assertions passing. Their actual recorded outputs accompany the programs. These finite computations corroborate, but are not substituted for, the proof above.

To reproduce in Python 3: run `python3 verify_words.py` and `python3 verify_matrices.py` in the extracted artifact directory. Both are standalone and require only the Python standard library.

## Relationship to prior work

Jacquet, Knessl and Szpankowski (2012) study exactly these finite-alphabet first-order Markov transition-frequency types. Section 2.3 distinguishes linear and circular strings and gives a relation between their counts, while deriving **asymptotic**, not the complete exact ternary linear-type sequence. Their ternary asymptotic coefficient equals the leading coefficient derived here. Their exact rational generating function for *unrestricted balanced matrices* is not the generating function here for **Euler-trail-realizable linear matrices**; graph connectivity and nonzero imbalance are included here exactly. This is an explicit exact refinement, not a claim to have introduced Markov types or the Eulerian-graph representation.

He, Kari and Millan Arias (2025) show how prescribed adjacent-substring frequency data can be realized through Eulerian paths, motivating exact counts of attainable observations. Their reconstruction algorithm does not give this enumeration. A separate binary two-gram spectrum enumeration covers alphabet size two, not three.

## Limitations

The closed form is specialized to the three-symbol alphabet and length-two ordered factors. It does not enumerate equivalence classes after retaining a separate initial symbol, or profiles from cyclic rather than linear words, and does not furnish a corresponding formula for general alphabet sizes or longer factors. Priority is based on inspected sources and searches, not a guarantee that an unindexed earlier formula does not exist. The exact coefficient formula is proved internally; its originality and priority have not been independently audited.

## References

1. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, February 15, 2012 manuscript (IEEE Transactions on Information Theory): https://www.cs.purdue.edu/homes/spa/papers/it12-types.pdf . In particular Sections 1, 2.3 and 3.1.
2. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings (2010): https://dmtcs.episciences.org/en/articles/2768/download .
3. H. He, L. Kari and P. Millan Arias, *Bridging Chaos Game Representations and k-mer Frequencies of DNA Sequences*, arXiv:2506.22172v1, first public June 27, 2025: https://arxiv.org/html/2506.22172v1 .

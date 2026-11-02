# Exact singleton ternary two-composition decks and their rational census

## Finding

Fix the labeled alphabet \(\Sigma=\{0,1,2\}\). For a word \(w=w_0\cdots w_m\) of length \(m+1\), let its *unoriented adjacent-pair deck* be the six-component vector
\[
D(w)=(a_0,a_1,a_2,b_{01},b_{02},b_{12}),
\]
where \(a_i\) is the number of adjacent \(ii\) pairs and \(b_{ij}\), for \(i<j\), is the combined number of adjacent \(ij\) and \(ji\) pairs. Thus \(D(w)\) records the multiset of compositions of precisely the length-two contiguous substrings, with multiplicity, but not the source's endpoints. Reversal preserves this deck.

For \(m\ge1\), call a realizable deck *singleton* when every length-\(m+1\) realizing word is equal to one given realizing word or its reversal. Write \(U_m\) for the number of singleton decks and \(H_m\) for the total number of realizable decks.

**Complete singleton classification.** Form the looped undirected multigraph on \(\{0,1,2\}\) having \(a_i\) loops at vertex \(i\) and \(b_{ij}\) ordinary edges between \(i\) and \(j\). A nonempty realizable deck is singleton if and only if exactly one of the following disjoint conditions holds:

1. All ordinary edge counts vanish and exactly one loop count is positive.
2. Exactly one ordinary edge type \(\{i,j\}\) has positive multiplicity \(t\), the third vertex has no loop, and either \(t=1\) (arbitrary loops at \(i,j\)) or \(t\ge3\) is odd and both endpoints have no loops.
3. Exactly two ordinary edge types occur, forming a path \(A-B-C\) with respective positive multiplicities \(p\) and \(q\). Either \(p=q=1\), with arbitrary loops; or \(\{p,q\}=\{1,2\}\), with loops permitted at the two leaves but not at \(B\); or \(\{p,q\}=\{1,t\}\) for \(t\ge3\), with loops permitted only at the leaf incident to the multiplicity-one edge.

No deck with all three ordinary edge types present is singleton. For \(m=0\), the one possible empty deck has three one-letter realizing words and is not singleton.

**Exact census.** The complete generating function is
\[
\boxed{\sum_{m\ge1}U_mz^m=
\frac{3z}{1-z}+\frac{3z}{(1-z)^2}
+\frac{3z^3}{1-z^2}+\frac{3z^2}{(1-z)^3}
+\frac{6z^3}{(1-z)^2}+\frac{6z^4}{(1-z)^2}.}
\]
In particular, \(U_1=6\), \(U_2=12\), and for every \(m\ge3\),
\[
\boxed{U_m=\frac{3m^2+27m}{2}-27+3\mathbf1_{\{m\text{ odd}\}}.}
\]
The first values for \(m=1,\ldots,11\) are \(6,12,30,51,81,108,144,177,219,258,306\).

For comparison, the total deck enumerator is
\[
\sum_{m\ge0}H_mz^m=1+\frac{3z}{1-z}+\frac{3z}{(1-z)^3}
+\frac{3z^2}{(1-z)^5}+\frac{z^3}{(1-z)^6},
\]
and, for \(m\ge1\),
\[
H_m=3+3\binom{m+1}{2}+3\binom{m+2}{4}+\binom{m+2}{5},
\]
with binomial coefficients outside their natural ranges interpreted as zero. Consequently,
\[
\frac{U_m}{H_m}\sim\frac{180}{m^3}.
\]
These are counts of observation profiles, not probabilities under a uniform random source word.

## Assumptions and scope

The letters are distinct and labeled, their order is observed only through consecutive length-two compositions, and every consecutive pair is recorded exactly once with its multiplicity. Reads are noncyclic; no endpoint, orientation, or single-letter count is provided. The source length is known and is \(m+1\). Singleton refers to uniqueness **up to global reversal**, since reversal is unobservable. No probabilistic or noisy channel is assumed.

## Proof

**1. Euler reduction and feasibility.** Interpret consecutive letters of a word as a walk in the above looped multigraph; each step consumes one edge. Conversely, an Euler trail of the multigraph gives precisely a realizing word by reading its vertex sequence (parallel edges are indistinguishable in the observation). For \(m\ge1\), the multigraph has an Euler trail exactly when its positive-degree support is connected and it has zero or two odd-degree vertices. There are at most three vertices, so the handshaking lemma makes the parity condition automatic. Thus connectivity alone characterizes realizability. It follows that zero ordinary edge types permit loops at only one vertex; one ordinary edge type permits loops only at its endpoints; and two or three distinct ordinary edge types connect all three vertices and permit any loops.

**2. Suppress loops to classify vertex skeletons.** Erase consecutive duplicate letters from a realizing word. The resulting skeleton is a loop-free walk with prescribed ordinary-edge multiplicities. For any fixed oriented skeleton, the original word is recovered by assigning the \(a_i\) loop steps among visits to vertex \(i\). When the oriented skeleton has distinct first and last vertices, fixing one of those two endpoint labels as the first removes reversal ambiguity. Every positive loop count at a vertex visited at least twice then admits two inequivalent placements; a vertex visited exactly once admits just one placement.

If no ordinary edge occurs, the sole active vertex has one visit, giving condition 1. If exactly one ordinary edge type \(\{i,j\}\) occurs \(t\) times, the skeleton alternates between \(i\) and \(j\). For even \(t\ge2\), the two choices of start vertex give distinct reversal orbits (both skeletons start and end at the same letter). For odd \(t\), the skeleton is unique up to reversal, with different endpoint letters; at \(t=1\) each letter is visited once, while at every odd \(t\ge3\) both are visited at least twice. This proves condition 2, including the loop restrictions.

**3. Two ordinary edge types.** Relabel the underlying path \(A-B-C\). If both edge multiplicities \(p,q\) are even, there are distinct circuit skeletons starting at \(A\) and \(C\), which cannot be reversals. If both are odd and at least three, fix the direction from \(A\) to \(C\): after the first \(A-B\) step, a two-edge excursion through \(A\) and a two-edge excursion through \(C\) may be performed in either order. The two resulting skeletons are different and cannot be reversals because the oriented endpoints are distinct. If \(p\) is odd and at least three while \(q\) is even and at least two, start at \(A\) and end at \(B\); one \(A\)-excursion and one \(C\)-excursion can again be interchanged. The opposite parity case is symmetric. Thus \(p,q\ge2\) never yields a singleton skeleton.

If \(p=q=1\), the only skeleton up to reversal is \(A-B-C\), and all three vertices are visited once. If \(p=1\) and \(q\ge2\), the unique skeleton (oriented from \(A\)) consists of \(A-B\) followed by exactly \(q\) traversals alternating between \(B\) and \(C\). When \(q=2\), the leaves \(A,C\) are visited once and \(B\) twice. When \(q\ge3\), only \(A\) is visited once. Loop placement therefore yields precisely condition 3, including the symmetric case \(q=1\).

**4. Three ordinary edge types.** If all three vertices have even degree, an Euler circuit can start at any of the three vertices; different starts produce different source words not related by reversal, even after allowing loops. Otherwise exactly two vertices, say \(A,B\), have odd degree. The third vertex \(C\) is joined to both, and \(A-B\) is also present. Starting at \(A\), either an \(A-B\) step or an \(A-C\) step can be followed by an Euler trail of the remaining graph ending at \(B\): after deleting either chosen edge the remaining non-loop support stays connected and its degree parity has the requisite form. These two distinct skeletons have the same fixed starting and ending labels, so cannot be reversals. Inserting loops does not identify their different skeletons. Hence none of these profiles is singleton.

**5. Enumerate singleton profiles.** Conditions 1, 2 and 3, respectively, contribute
\[
\frac{3z}{1-z};\qquad
\frac{3z}{(1-z)^2}+\frac{3z^3}{1-z^2};\qquad
\frac{3z^2}{(1-z)^3}+\frac{6z^3}{(1-z)^2}+\frac{6z^4}{(1-z)^2}.
\]
The exponent of \(z\) counts the number of adjacent pairs; each permitted loop multiplicity supplies a factor \((1-z)^{-1}\). These cases are disjoint and exhaustive. Adding them yields the displayed rational series, and coefficient extraction gives the exact formula for \(m\ge3\), with \(m=1,2\) checked directly.

**6. Count all decks.** Partition connected edge-multisets by the number \(0,1,2,3\) of positive ordinary edge types. The four contributions are, respectively,
\[
1+\frac{3z}{1-z},\qquad\frac{3z}{(1-z)^3},\qquad
\frac{3z^2}{(1-z)^5},\qquad\frac{z^3}{(1-z)^6}.
\]
The final two terms use the fact that any two different ordinary edge types on three vertices meet and connect all vertices. Summing yields \(H_m\). The highest-order poles show \(U_m=\frac32m^2+O(m)\) and \(H_m=\frac1{120}m^5+O(m^4)\), proving the ratio.

## Verification

Run the standalone Python 3 program `verify.py` using only the standard library. It constructs all ternary words of lengths \(1\) through \(12\), groups each by its literal six-component adjacent-composition deck, and counts **distinct reversal orbits** in each fiber. It separately evaluates the stated structural classification and both closed-form counts. The run examined \(797{,}160\) source words, corresponding to \(9{,}901\) distinct observed profiles across the twelve lengths, and reported `VERIFY_OK` with no disagreements. This finite computation corroborates the theorem; the all-length result rests on the Euler-trail and excursion arguments above.

## Relationship to prior work

Ye and Elishco (2022, arXiv:2208.14963) develop composition-based reconstruction and introduce bounded-length composition decks; their relevant general-alphabet section gives code constructions rather than an exact classification of singleton ternary length-two decks. Published work on binary two-read and binary length-at-most-two reconstruction establishes separate two-letter results; a quaternary unordered-bigram enumerator establishes realizable-profile counts for four letters but not the ternary singleton-reconstruction classification. The standard undirected Euler-trail criterion is the proof's classical starting point, not itself claimed as new. The distinct contribution assessed here is the complete **ternary singleton classification and exact rational census**, including the polynomial-versus-quintic scarcity law. The auxiliary total profile count is included for context, not presented as a new general graph-enumeration principle.

## Limitations

The theorem is restricted to three labeled letters and exact length-two **unoriented** contiguous reads. It does not characterize all individual fiber sizes, noisy-channel codes, or higher-length decks. Other combinations of lengths and endpoint side information may behave differently. The originality assessment is literature-based rather than a mathematical proof of priority; an equivalent specialization of a general unique-Euler-trail classification is a residual possibility.

## References

- Zuo Ye and Ohad Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, first public August 31, 2022, arXiv:2208.14963, https://arxiv.org/abs/2208.14963.
- G. Punzi, A. Conte, R. Grossi, and R. Rizzi, *Refined Bounds on the Number of Eulerian Tours in Undirected Graphs*, Algorithmica (2024), https://doi.org/10.1007/s00453-023-01162-8. This concerns counts/bounds of tours, not the stated ternary profile census.
- Classical Euler-trail criterion for finite undirected multigraphs with loops (connectivity and at most two odd-degree vertices).

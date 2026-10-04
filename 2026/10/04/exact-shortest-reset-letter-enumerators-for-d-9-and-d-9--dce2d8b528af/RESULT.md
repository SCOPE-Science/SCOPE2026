# Exact shortest-reset letter enumerators for \(D'_9\) and \(D''_9\)
## Finding
For the nine-state colorings \(D'_9\) and \(D''_9\) of the Ananichev–Gusev–Volkov digraph \(D_9\), define the shortest-reset letter enumerator
\[
P_{\mathcal A}(z)=\sum_{w} z^{|w|_a},
\]
where the sum is over all shortest reset words \(w\) of \(\mathcal A\), and \(|w|_a\) counts occurrences of the input letter \(a\). Then
\[
P_{D'_9}(z)=z^8(1+z)^{30}(2+z)^6
\]
and
\[
P_{D''_9}(z)=z^7(1+z)^{30}(1+z+z^2)^6.
\]
The corresponding reset thresholds are respectively \(58\) and \(56\). Evaluating at \(z=1\) gives, for each automaton,
\[
2^{30}3^6=782{,}757{,}789{,}696
\]
shortest reset words. Every shortest reset word of \(D'_9\) resets to state \(2\); every shortest reset word of \(D''_9\) resets to state \(1\).

## Assumptions and scope
The state set is \(Q=\{1,\ldots,9\}\), with alphabet \(\{a,b\}\). The transitions are those in Figure 4 of Ananichev, Gusev and Volkov. Explicitly, for \(1\le i\le7\), both letters send \(i\) to \(i+1\). At state \(8\), both colorings have \(a:8\mapsto1\) and \(b:8\mapsto9\). At state \(9\), \(D'_9\) has \(a:9\mapsto2\), \(b:9\mapsto1\), while \(D''_9\) has \(a:9\mapsto1\), \(b:9\mapsto2\).

The claim is finite and exact for these two nine-state automata. It does not assert the analogous factorization for arbitrary \(n\).

## Proof
For a deterministic automaton and a word \(w\), the image \(Qw\) is a nonempty subset of \(Q\). Hence all reset questions for a nine-state automaton can be decided in its power automaton, which has at most \(2^9-1=511\) nonempty subset states.

Start breadth-first search at \(Q\). For every reached subset \(S\) at its minimum distance, attach the polynomial
\[
F_S(z)=\sum_{w:\,Qw=S,\,|w|=d(S)}z^{|w|_a}.
\]
If an \(a\)-edge from \(S\) reaches a subset \(T\) in the next BFS layer, add \(zF_S(z)\) to \(F_T(z)\); if a \(b\)-edge does so, add \(F_S(z)\). Edges that do not advance one BFS layer cannot belong to a shortest path and are omitted from the shortest-path dynamic program. The first layer containing a singleton is therefore exactly the reset threshold, and summing \(F_T\) over singleton targets in that layer counts every shortest reset word exactly once by its number of \(a\)'s.

For \(D'_9\), the first singleton layer is \(58\). The exact coefficient vector produced by this recurrence equals the coefficient vector of
\[
z^8(1+z)^{30}(2+z)^6,
\]
and the only singleton target in that layer is \(\{2\}\). For \(D''_9\), the first singleton layer is \(56\); its coefficient vector equals that of
\[
z^7(1+z)^{30}(1+z+z^2)^6,
\]
and the only singleton target is \(\{1\}\). These coefficient identities are integer equalities, not numerical fits.

A second implementation, using immutable state sets rather than bit masks and propagating complete \(a\)-weight histograms layer by layer, independently reproduces both first-singleton layers, both coefficient vectors and both unique targets. Thus the search is exhaustive over the finite power automata, and the displayed factorizations follow by exact coefficient comparison.

## Verification
Run `python3 verify.py`. It reconstructs both transition tables, performs the bit-mask BFS with polynomial shortest-path counting, performs an independent set-based layer propagation, expands the two claimed factorizations by integer arithmetic, and checks equality of all coefficients. The expected terminal line is `VERIFY_OK`.

For \(D'_9\), the nonzero coefficients occur from \(z^8\) through \(z^{44}\); for \(D''_9\), from \(z^7\) through \(z^{49}\). The verifier also checks that each coefficient sum is exactly \(782{,}757{,}789{,}696\).

## Relationship to prior work
Ananichev, Gusev and Volkov introduced the two colorings and proved reset thresholds \(n^2-3n+4\) for \(D'_n\) and \(n^2-3n+2\) for \(D''_n\). Their exhaustive experiment generated all initially connected two-letter automata through nine states and recorded reset-length statistics, but the published result does not give shortest-reset-word multiplicities or letter-composition enumerators for these two automata.

Kisielewicz, Kowalski and Szykuła later gave an exact shortest-reset-word algorithm and proved polynomial running time on the slowly synchronizing families containing \(D'_n\) and \(D''_n\). That algorithmic coverage does not state the two nine-state enumerators above. Targeted searches for the exact total, the two factorizations, the automaton aliases and shortest-reset multiplicity did not locate a published statement implying these enumerators.

The nine-state instance is mathematically motivated rather than an arbitrary slice: nine states are the endpoint of the complete exhaustive census reported in the defining paper. The enumerators refine that census from a single reset threshold to the complete distribution of letter use among all optimal controls, and reveal that the two colorings have the same enormous number of shortest reset words despite different thresholds and different composition laws.

## Limitations
This is a finite exact result for \(n=9\), not a proof of an infinite-family formula. Exhaustive power-automaton computation proves the stated finite identities but by itself does not establish a symbolic factorization for general \(n\). Originality is supported by targeted database and literature comparisons rather than a proof of absence from every possible source. Ancillary or unpublished computations could in principle contain equivalent counts even though no such statement was found.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, “Slowly synchronizing automata and digraphs,” arXiv:1005.0129v1, first posted 2010-05-02; see Figure 4, Theorem 4 and Section 5.
2. A. Kisielewicz, J. Kowalski, M. Szykuła, “Computing the shortest reset words of synchronizing automata,” *Journal of Combinatorial Optimization* 29 (2015), 88–124, DOI:10.1007/s10878-013-9682-0; see Section 5.2.

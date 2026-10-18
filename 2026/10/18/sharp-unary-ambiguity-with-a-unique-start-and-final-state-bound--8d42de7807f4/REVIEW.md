# Scientific review

## Correctness — PASS
The proof first shows that bounded ambiguity forces every cyclic strongly connected component to be a simple directed cycle and forbids an accepting path through two different cyclic components. A run can therefore be counted by its visited subset of singleton components and, at most, one cyclic segment. When neither endpoint is cyclic this gives \((1+a)2^{n-a-2}\le2^{n-2}\), and equality is excluded separately. With one cyclic endpoint the bound is \(2^{n-c-1}\), attaining the target only for a singleton self-loop. Exhausting every visited subset forces a complete ordered DAG and determines all equality cases. The converse exhibits one run per subset at all sufficiently large lengths. The checker exhaustively confirms all two- through four-state transition digraphs and the candidate constructions through ten states.

## Originality — PASS within checked evidence
The most pertinent comparison is Kiefer et al. (2026, arXiv:2610.08525): it states a unary **lower** example of \(2^{n-2}\) while proving general exponential growth bounds, but supplies no matching singleton-endpoint upper bound or equality-case classification. Weber–Seidl (1991) state the exact more permissive unary optimum \(2^{n-1}\) with multiple initial/final states, which cannot imply the stricter theorem. Literature searches for precise singleton-endpoint extremizers, the 2025 algorithmic-ambiguity work, and pertinent research-record queries found no statement that subsumes all three parts of the new theorem. Remaining priority risk: an earlier digraph or automata treatment may have already established the special singleton-endpoint bound, especially in historical sources underlying Weber–Seidl's Table 1.

## Value — PASS
The one-initial/one-final convention is the basic NFA model, while previous extremal ambiguity results often allow multiple initials and finals. Establishing an exact state-by-state extremum together with rigidity and counting of every optimizer identifies which graph structures force the sharp multiplicity rather than merely reproducing an easy construction. The theorem sharpens the broader unary comparison and provides a reusable component/subset counting technique.

Self-review: passed. Independent audit: not yet performed.

# Independent mathematical audit

## correctness

PASS

For each nonempty vertex set T in Q4, the binary incidence code row sum [I16|B] is (1_T,1_{delta(T)}), so its Hamming weight is |T|+|delta(T)|=5|T|−2e(T). Support-minimality is equivalent to connected induced Q4[T]: if disconnected, a component codeword has support contained; if connected, each proper nonempty submask has an internal crossing edge absent from delta(T), preventing support containment. Independently checked all 65535 nonzero masks by connectivity, internal edges and exact weight, yielding the complete 22-term spectrum claimed; its coefficient sum is 37293 and minimum distance is five. The finite enumeration is exhaustive for exactly this 16-vertex graph, not a claim for Qd generally.

## originality

PASS

Kim's 2026 full 17-page paper (read completely, pages 1–17) proves the incidence-matrix minimal-codeword/connected-induced-set correspondence and families such as ladders, but no Q4 hypercube Hamming-weight spectrum. OEIS A290758 already lists the 37293 connected-set TOTAL; this is credited. The asserted contribution is the entire weight-resolved distribution by |T|+|delta(T)|, not the known count. Kurz's graph-adjacency construction is a different code.

## value

PASS

For the canonical [48,16,5] Q4 graph-incidence code, the exact weight spectrum of all minimal words is a natural complete classification of its minimal supports by Hamming weight, relevant to codeword/support geometry and secret-sharing access structures. The exact 22-level refinement is not determined by the known ungraded count and is feasible to use as a complete benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.

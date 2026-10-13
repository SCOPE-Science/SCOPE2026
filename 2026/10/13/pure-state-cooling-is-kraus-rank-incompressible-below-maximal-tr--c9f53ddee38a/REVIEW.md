# Self-review

## Correctness
**PASS.** A minimal Stinespring dilation with environment dimension \(r\) gives \(A=V^\dagger(P\otimes I_r)V\) of rank at most \(r\). If \(r<d\), a kernel input has zero target overlap, hence output support orthogonal to the pure target and trace-norm error exactly \(2\). The exact pure replacer has Kraus rank \(d\), so the threshold is sharp. The fermionic mode consequence follows from \(2^m\) bath dimension versus \(2^N\) system dimension.

## Originality
**PASS.** The recent cooling paper supplies the motivating single-contact, pure-bath construction but no minimum bath-mode statement. The closest general compression paper, Lancien--Winter, treats uniform output-norm approximation with reduced Kraus rank and leaves channel-dependent optimal approximating rank open; its inspected text does not give the pure-replacer threshold. Standard Stinespring references identify Kraus rank with minimal environment dimension but do not state that every rank reduction below \(d\) incurs maximal statewise error \(2\).

## Value
**PASS.** The result determines a natural exact resource invariant for the new cooling architecture: approximation does not buy even one environment dimension below the exact pure-replacer threshold until the error reaches the trivial maximum. For \(N\) fermionic modes this gives a sharp linear lower bound of \(N\) coherent bath modes and places the source's \(2N\)-mode construction within a factor two of the unconstrained information-theoretic minimum. This comparison is meaningful while remaining explicit about the absence of a locality-constrained converse.

Closest literature and limitations are detailed in `RESULT.md`. The principal residual risk is an older channel-approximation note stating the same pure-replacer special case under different terminology; targeted searches and inspection of the closest general compression literature did not locate one.

Self-review: passed. Independent audit: not yet performed.

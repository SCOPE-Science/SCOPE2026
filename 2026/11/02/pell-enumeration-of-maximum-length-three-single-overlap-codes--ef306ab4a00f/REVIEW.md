# Self-review

**Correctness — PASS.** The sharp upper bound follows from the partition into nonconstant rotation triples. The partition representation follows from the disjoint prefix/suffix context sets. Equality forces every directed triple to contain both binary colors. The repeated-letter cases force ties into a matching; orientations to outside symbols are coherent; the quotient tournament is transitive. The converse construction and the first-singleton-only reconstruction ambiguity yield the exact labeled-code count. Two independent finite programs checked every context matrix or every prescribed block construction through alphabet size five, including deduplicated code sets. The general proof does not rest on a finite cutoff.

**Originality — PASS, with residual priority risk.** Yang and Ding's full text addresses interval-restricted codes via generalized constructions; its Theorem 3.4 counts sizes of that construction, not the optimality and full equality census for isolated length-two overlaps at word length three. The abstract of Wang–Fang–Feng has a different combination of restrictions. Targeted searches for the exact recurrence, Pell counts, de Bruijn directed cuts, and two-overlap-free codes did not identify an equivalent classification. The simple numerical upper bound may have been observed elsewhere; the main claimed contribution includes all extremizers and exact counting. Indirect coverage by older graph-theoretic directed-cut work cannot be excluded.

**Value — PASS.** A complete all-alphabet classification of optimal synchronization codes is a natural structural invariant, not an arbitrary finite slice. The pair-block theorem explains all equality cases, and the Pell recurrence produces an exact labeled optimizer count while correcting the overcount from binary context partitions. These properties are not provided by the elementary orbit bound alone.

**Limits.** Overlap length two at word length three only, not interval overlap constraints. Finite tests at alphabet sizes one through five. The older graph-theoretic literature remains a specific priority risk. No independent audit.

Self-review: passed. Independent audit: not yet performed.

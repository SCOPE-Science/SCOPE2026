# Self-review

**Correctness — PASS.** The finite universe and subsequence convention are fixed. The explicit code covers all 128 targets, independently counted by direct deletion. The lower bound follows from an exhaustive branching search over all 64 candidate centers; the branching lemma and both exact pruning inequalities are reconstructed in the proof, and the compiled standalone verifier returns the expected unsatisfiable 19-center result. Unlike a timeout or an optimization log, the computation terminates and its control flow proves completeness.

**Originality — PASS, with residual risk.** The statement \(I(2,6,1)=20\), also \(S(2,7,6)=20\), was compared with general insertion-covering literature, exact different-parameter small-alphabet tables, relevant published records, and the synonymous sequence-covering formulation. Inspected primary results give asymptotic bounds or ternary-center examples, not this exact binary length-six result. A historical table not indexed by the searched sources might already contain the value.

**Value — PASS.** This is a natural, fully determined finite covering number at a nontrivial length: 64 possible centers cover 128 required targets, the elementary ball-size bound is only 16, and the exact optimum is 20. The witness is simple while proving optimality requires a nontrivial exhaustive covering argument. The result quantifies the exact redundancy penalty at a fixed synchronization-error length; it is neither a cosmetic reformulation nor a known table recomputation in the inspected sources.

**Closest literature and limitations.** Xie--Sun--Ge (arXiv:2606.15379), Lenz--Rashtchian--Siegel--Yaakobi (arXiv:1911.09944), and Pikhurko--Verbitsky--Zhukovskii (arXiv:2409.06425) treat general insertion covering and density bounds; Grozea's reported exact table concerns three-symbol centers and alphabet sizes two to five. A prior unindexed exact value remains possible. No larger-length or uniform theorem is claimed.

Self-review: passed. Independent audit: not yet performed.

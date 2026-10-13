# Scientific assessment

**Correctness — PASS.** A complete finite proof consists of explicit codebooks, eight exact rational dual inequalities, and a complete 729-vertex clique search with safe greedy-coloring pruning. The verifier replayed all codebooks and constraints and returned `VERIFY_OK`; the C++ clique search tested 1,680,903 recursive nodes. The theorem asserts only a lower bound, not the exact list-two capacity at six.

**Originality — PASS, with risks.** Published search and comparison of arXiv:2609.26650, arXiv:1502.02727v3 and arXiv:2306.02868 did not identify this first ternary threshold or the 24-word construction. Le–Nguyen's Appendix B computes only generalized Helberg residue-code sizes, not unrestricted maxima. Lin's 2026 result concerns binary asymptotics. The Lin and Liu full texts were not accessible in this comparison, and unindexed finite tables remain a genuine risk. No negative whole-document claim is made for inaccessible sources.

**Value — PASS.** The first strict capacity gap proves a structural obstruction to obtaining optimal ternary list-two deletion codes merely by pooling two unique-deletion codes; it identifies the shortest blocklength where this happens, not an arbitrary parameter slice. The finite numerical gap is meaningful because it changes the capacity-composition property.

Self-review: passed. Independent audit: not yet performed.

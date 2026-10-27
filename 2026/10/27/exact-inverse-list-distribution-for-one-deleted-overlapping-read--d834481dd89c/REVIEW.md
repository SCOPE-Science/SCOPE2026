# Scientific review

**Correctness: PASS.** Each possible missing-read location is classified: endpoint insertions give two groups of \(q\) parents with one collision only for a constant reconstructed source; interior insertion is possible exactly on constant overlaps of length \(\ell-1\), with one new parent per sufficiently long strictly interior maximal run. Inconsistent outputs have at most one source. Maximal-run packing proves and attains the sharp upper bound. A run-composition calculation proves the rational generating function. Counting adjacent equal read windows proves the inconsistent-output formula. Exhaustive independent enumeration of the finite tested regimes confirms all claims; its scope is not presented as an infinite proof.

**Originality: PASS (best-knowledge, residual risk).** The closest primary source, Ye and Ge, arXiv:2606.26434, gives the adapter-protected channel and periodic-substring characterization, not the unpadded full distribution or the explicit worst-case parent bound. The current theorem must not be described as a wholly new local insertion mechanism; its contribution is the global multiplicity law, sharp run-packing extremum, and full coefficient enumeration. Xie and Chen, arXiv:2601.21236, use known adapters; Banerjee et al., arXiv:2401.15939, use Hamming-weight reads. The accessible comparison does not eliminate equivalent formulations in unindexed work or inaccessible appendices.

**Value: PASS.** Source ambiguity after losing a single read is a basic metric of synchronization-channel reconstruction. The exact maximum, the attainable spectrum, and the all-length/all-alphabet histogram distinguish worst-case from typical receiver behavior and supply finite counting data that the published redundancy bounds do not determine. The generating-function result is a substantive global enumeration over all possible source run structures, rather than merely rephrasing a code construction.

**Scope:** Exactly one read deleted; ordered full-length overlapping reads; no protected adapters. No assertion for multiple deletions, different read maps, or higher coding rate.

Self-review: passed. Independent audit: not yet performed.

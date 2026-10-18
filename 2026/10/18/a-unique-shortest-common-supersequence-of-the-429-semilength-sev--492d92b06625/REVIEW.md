# Scientific review

**Correctness — PASS.** The supplied finite proof enumerates all \(2^{21}+2^{22}\) candidate hosts, with complete recursive enumeration of the \(429\) Dyck targets and a provably correct greedy subsequence check. It finds no length-21 host and exactly one length-22 host, and monotonicity under padding rules out all shorter hosts. An independent BFS over prefix-embedding progress vectors reconstructs both the minimum and unique optimum. Both were compiled from the attached sources and executed.

**Originality — PASS against accessible evidence; residual risk remains.** Clifford et al., arXiv:1004.0424, study fixed-resource restricted common supersequence optimization rather than the particular complete Dyck target set. Standard generic SCS complexity does not imply the 22-letter optimum or unique-host census. Targeted published-record searches, terminology variants, a source-scope comparison and accessible historical titles found no equivalent/stronger exact result. An unindexed table or differently formulated result might still cover it; this is not absolute novelty certification.

**Mathematical value — PASS.** At semilength seven the target family has 429 structured, Catalan-enumerated members. Its shortest scattered-subsequence cover is a well-defined natural compression/coverage invariant. The complete classification, including uniqueness of the extremal host, is a nontrivial exact finite cutoff established through millions of candidate host checks, not a small arithmetic substitution. Earlier semilength optima have varying multiplicities; the exact one-host phenomenon is a meaningful boundary datum without asserting a general formula.

**Scientific limitations.** Computational exhaustion is finite and no theorem for larger semilengths is claimed. Independent audit remains to be performed. Earlier unindexed exact coverage cannot be excluded.

Self-review: passed. Independent audit: not yet performed.

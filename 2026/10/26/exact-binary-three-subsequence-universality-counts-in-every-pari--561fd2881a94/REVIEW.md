# Scientific review

**Correctness — PASS.** The proof classifies exactly six forbidden length-three patterns, lists each avoidance family as a one-per-parameter run form, and enumerates all overlaps. Their inclusion–exclusion yields the exact fiber census. A separate case analysis proves there are at most two exceptions per fiber, and summing the six families gives exactly \(3(a+b)-6\) exceptions. The standalone program checks every binary word for multiplicities at least three and combined length at most fifteen. Finite testing is only corroboration.

**Originality — PASS within examined literature.** The closest accessible primary paper is Fazekas, Huang, and Mercaş, arXiv:2610.06717, especially Section 4 on length-three avoidance and Section 5 on class-size Gaussian polynomials. It does not supply the exact conditional universality enumeration. The known unconditioned length-only universality generating function cannot recover fixed Parikh-matrix class counts. Searches for scattered-subword, inversion, Parikh-matrix, and Gaussian-binomial formulations did not identify a covering statement. A hidden or implicit equivalent result remains possible; this review does not establish historical priority.

**Mathematical value — PASS.** The theorem determines a full natural three-parameter conditional distribution, strengthens yes/no universality criteria to exact counts, and exposes a surprising sharp bound of two nonuniversal words per class. It concerns a motivated invariant, not an arbitrary finite census.

**Limitations.** Both letter counts must be at least three; no result about longer patterns or larger alphabets is claimed. The proof and computational checker are supplied, but independent validation is not performed.

Self-review: passed. Independent audit: not yet performed.

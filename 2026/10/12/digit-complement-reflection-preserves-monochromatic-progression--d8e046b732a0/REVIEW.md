# Scientific review: complementary digit-pattern progression maxima

## Correctness
**PASS.** For a padded base-\(b\) digit expansion, interior occurrences correspond exactly under digitwise complementation, while the boundary contribution is the single, explicitly characterized residue-independent constant \(\chi(\bar v)\). Reflection about \(b^K-1\) reverses an arithmetic progression without changing its positive difference. These facts give both directions of the fixed-difference length-preservation result. The proof treats all starting integers, differences, pattern lengths, bases and moduli, including a possible infinite supremum. The standalone checker passes 158,464 count identities and 142,800 trace transfers; they supplement, rather than replace, the general argument.

## Originality
**PASS, subject to an unindexed-equivalence risk.** Sobolewski's *On monochromatic arithmetic progressions in binary words associated with pattern sequences* (arXiv:2204.05287, §6 Problem 4) explicitly conjectures the binary mixed-pattern statement rather than proves it. Relevant progression results of Aedo et al. (arXiv:2302.12908) and Joshi--Rust (arXiv:2501.05830) concern substitution families or individual words, not the all-pattern reflection identity. Equivalent digital-reflection descriptions might exist outside indexed literature. No claim of exhaustive global priority verification is made.

## Value
**PASS.** The result resolves a concrete conjectured all-pattern phenomenon in published literature and generalizes it to all integer bases and moduli. The explicit trace transfer provides a reusable mechanism, not only matching individual computed maxima.

## Limitations
The theorem excludes the two extreme constant-digit patterns and does not preserve origin-constrained progression lengths. It does not evaluate individual common maxima. The finite checks are diagnostics; no independent audit has been completed.

Self-review: passed. Independent audit: not yet performed.

# Scientific review: Complete rooted LZ78 phrase spectrum of binary order-five de Bruijn cycles

## Correctness — PASS

The object is specified without a hidden choice of root or parsing rule: exactly one period of a binary order-five de Bruijn necklace is read at each of its thirty-two roots, and even a previously seen residual terminal phrase is counted. The source-to-feedback bijection forces all admissible cyclic objects to arise from one of the sixteen-bit binary feedback tables. Independently, the order-four de Bruijn graph Euler-tour construction exhausts the same objects by edge usage. The two separately constructed sets agree word for word and contain exactly 2,048 members. Two algorithmically independent dictionary implementations agree at all 65,536 roots and the complete counters are reproduced by the standalone checker. The critical `verify.py` file was actually executed and printed `VERIFY_OK`. The result is an exhaustive finite proof with an explicit completeness argument, not a sample or a heuristic. An outside review remains unperformed.

## Originality — PASS (with residual historical-priority risk)

Cohn–Helfgott (1997) is particularly close in *objects and method*: their author-uploaded full manuscript proves LZ78 forward/reverse separation for words assembled by concatenating successively truncated de Bruijn strings. Their construction yields asymptotic phrase-count bounds for concatenations of length far greater than one cycle. It does not assert a root-by-root joint distribution on the 2,048 order-five necklaces, and its implications cannot determine that distribution. The inspected 1978 Ziv–Lempel work introduces the incremental parsing scheme and general compression bounds but no such finite spectrum. Dutta et al. (2013) treat random access to LZ78 representations, not cyclic de Bruijn families; its relevant original text (Section 2) describes the parser. Targeted database and literature searches under aliases such as de Bruijn, LZ78, dictionary parsing, circular rotation, and finite phrase census returned no covering result. This is evidence of distinction from the closest *inspected* sources, not a proof of uniqueness in all literature. An obscure published table may still exist.

## Value — PASS

De Bruijn cycles have exactly the same multiplicities of all circular factors of length at most five, so differences in incremental LZ78 phrase counts are not explained by elementary local factor frequencies. They reveal sensitivity to the *ordering* and *root* of a maximally diverse fixed-content string. Order five is the first moderate full family with 2,048 cycles rather than a handful. The complete rooted distribution, the exact six-type minimum/maximum classification, and the thirty root-invariant cycles are natural finite benchmarks for dictionary-based parsing and circular string analysis. They provide complete exact data, not arbitrary slices or one-example gains. The precise order-five fact does not require a downstream all-order theorem to be meaningful.

## Closest literature and limitations

- J. Ziv and A. Lempel, *Compression of Individual Sequences via Variable-Rate Coding* (1978), original LZ78 compression framework.
- M. Cohn and H. A. Helfgott, *Asymmetry in Ziv/Lempel '78 Parsing* (1997), de Bruijn-based concatenation construction and reversal separation, DOI 10.1109/SEQUEN.1997.666926.
- A. Dutta, R. Levi, D. Ron and R. Rubinfeld, *A simple online competitive adaptation of Lempel-Ziv compression with efficient random access support* (2013), arXiv:1301.2495, introductory and parsing preliminaries.
- J. Ziv, *A Constrained-Dictionary version of LZ78...* (2014), arXiv:1409.1323, context for dictionary variants.

The classification applies only to binary order-five cycles and to the declared terminal-suffix phrase convention. It measures phrase count rather than actual encoded bit length. Full historical exhaustiveness and independent mathematical audit have not been established.

Self-review: passed. Independent audit: not yet performed.

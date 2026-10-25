# Scientific review: five-run prefix-normal enumeration

## Correctness — PASS

The all-length proof uses the gap-window characterization (proved directly), classifies the two nonzero gaps into three length regimes, partitions positive compositions into two nonoverlapping parameter regions, and sums their ordinary generating functions. The rational expression and leading constant are obtained symbolically, with an independent exponential-simplex derivation of the limiting ratio. For every length from \(5\) through \(27\), the standalone verifier examined each five-run word using a direct factor-window test and matched the rational coefficients, testing \(80{,}730\) words. Risks: the finite verifier alone proves no infinite statement; the written gap and generating-function proofs are the basis for correctness.

## Originality — PASS (run-refined enumeration only)

The general prefix-normal position/gap test is already present in Burcsi et al., arXiv:1611.09017, Lemma 8; the specialized run-length criterion is **not** claimed as a novel general principle. The investigated literature gives global asymptotics (Balister–Gerke, arXiv:1903.07957), fixed-one-count generating functions (Burcsi et al.), a Gray-code/membership algorithm (Burcsi et al., arXiv:2003.03222), and studies of collapsing classes (Fleischmann et al., arXiv:1905.11847). None of their inspected statements or examples provides the exact five-run generating function or its conditional density. Targeted published-finding corpus and web searches also found no direct equivalent. Remaining risk: equivalent finite-run enumeration could be contained in a less-indexed source or be an unlabelled worked instance of known polyhedral methods. No independent priority determination is claimed.

## Mathematical value — PASS

The five-run class is the first alternating class with three separated blocks of ones and a genuine comparison between the two zero gaps; merely bounding the lengths of later one runs is insufficient. The exact rational counting function and \(7/24\) density resolve a natural finite-run stratum of the broader prefix-normal enumeration problem. This is a complete exact enumerative classification, not a generic existence claim or a routine numerical table. Its scope remains narrow and is not presented as a global prefix-normal counting solution.

Self-review: passed. Independent audit: not yet performed.

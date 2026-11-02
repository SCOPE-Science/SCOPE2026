# Scientific review

**Correctness:** PASS. Distinct-output two-deletion incidence is the exact code constraint. The explicit fifteen-word code is feasible, primal-dual rational vectors prove the LP optimum \(2188/135\), and a complete 205-node inclusion/exclusion proof with 103 rational-leaf upper bounds excludes every sixteen-word code. Exact verification is reproduced by `verify.py` with `CERTIFICATE.json` and needs no numerical solver. Previously known shorter lengths are checked by integer witnesses and rational upper bounds. No asymptotic extrapolation is involved.

**Originality:** PASS subject to explicit historical priority risk. Lin (arXiv:2609.26650v1) gives asymptotic list-deletion bounds and a hypergraph model, while Guruswami–Håstad (arXiv:2007.10592) treats asymptotic explicit construction. Earlier exact six- and seven-bit maxima do not determine the length-eight LP/integer separation. Equivalent coverage in an unindexed table or the uninspected portions of the older primary source remains possible.

**Value:** PASS. The new result identifies the first finite-block integrality-rounding failure of a natural deletion-hypergraph packing relaxation and provides a reusable exact proof certificate for its occurrence. It is not merely a routine next-block maximum-size computation.

**Limitations:** Binary alphabet, two deletions, list size two; one exact finite-block separation only. No general bound or algorithmic decoding claim. Independent priority and proof audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.

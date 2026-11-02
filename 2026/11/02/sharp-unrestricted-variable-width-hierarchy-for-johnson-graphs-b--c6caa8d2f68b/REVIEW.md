# Self-review

## Correctness — PASS

The proof starts from the exact Johnson distance and uses a three-variable recursive definition of every fixed distance. The upper-bound game matches nonempty ordered Venn-cell populations of at most \(p-1\) retained \(r\)-subsets, with at least \(r\) fresh ground elements on both sides at \(n,m\ge pr\). This extends through every move, regardless of quantifier depth. The lower-bound formulas for \(t=jr+i\), where \(2\le j\le p-1\) and \(1\le i\le r\), have at most \(p\) variables and force union size precisely \(t\); they distinguish every consecutive order below \(pr\). Different normalized ranks are separated by definable graph diameter. The two standalone programs check finite cases, but the all-parameter proof is mathematical.

## Originality — PASS (qualified)

The precise new content is the unrestricted \(p\)-variable classification with \(p\ge4\) and \(r\ge3\). The three-variable consequence of distance regularity and the rank-two triangular graph result are prior cases, not claimed here. Earlier marked-Johnson counting-refinement results identify stabilizer orbits, not uncounted higher-width theories. Chepoi 2015 treats isometric embeddings; Grohe and Otto 2012 treat general pebble game equivalence; merged Johnson graph literature treats automorphisms; Adler, Benediktsson and Macpherson treat adjacency VC complexity. Inspected material does not cover the sharp multiway Venn-cell \(pr\) boundary. A stronger general theorem about set-system interpretations could imply it; the 2005 paper was not read in full.

## Mathematical value — PASS

The theorem determines a natural exact logical-width hierarchy across all higher widths for uniform-matroid basis graphs, with \((p-2)r+1\) theories at fixed rank, exact consecutive distinguishability below \(pr\), and the smallest stable representative \(\binom{pr}{r}\). These are structural model-theoretic resources rather than isolated experimental values. The explicit extension invariant may aid comparisons of higher-rank subset systems, though no further downstream theorem is asserted.

## Limitations

This is a within-family classification in the pure adjacency language without counting; it does not apply automatically to other graph families, richer signatures, bounded-depth questions, or counting logic. Independent mathematical evaluation and exhaustive historical-priority verification are not complete.

Self-review: passed. Independent audit: not yet performed.

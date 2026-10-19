# Scientific review: sharp reentry of optimal tree seed

## Correctness — PASS

The expected spread formula \(F_v(p)=\sum_w p^{d_T(v,w)}\) follows by linearity from independent edge transmission along unique tree paths. The lower bound is a full computer-assisted finite theorem: all unlabelled tree shapes through \(14\) are enumerated with checked counts, comparisons are transformed to exact rational-polynomial sign certificates, and every remaining relevant crossing is isolated exactly rather than sampled on a floating-point mesh. The \(15\)-vertex witness is reconstructed from its complete edge list. Only origins \(1\) and \(2\) can maximize, because origin \(1\) strictly dominates every other origin. Their exact difference is \(p(1-p)(p^4+p^3+p^2-3p+1)\), with exactly two roots in \((0,1)\). See the proof and `verify_reentry.py` for precise certificates and reproduction.

**Risk:** This is a finite computer-assisted proof whose exhaustive enumeration depends on a standard third-party unlabelled-tree generator and symbolic libraries. The counts agree with the known classification but no independent implementation of tree enumeration was produced. The result does not claim an infinitary graph classification or external proof certification.

## Originality — PASS, subject to independently unresolved literature

Tsakas (2016) gives the motivating one-threshold empirical perspective. Coroničová Hurajová, Gago and Madaras (2018) already prove **arbitrary pairwise** decay-crossing phenomena in constructed trees and count all *fully decay-stable* unlabelled trees through order \(20\). Neither is the sharp minimum for **reentry of the global maximizer**: even repeatedly crossing vertex scores need not attain the maximum of all scores at any parameter, and a fully unstable ordering may still have an unchanged top-ranked vertex. Riveros–Salas–Skibski (2023) study which centralities root trees, another inequivalent invariant. Rupnik Poklukar–Žerovnik (2025) give ranking-stability criteria and path-product counterexamples, not the new reentry bound. Related published results and aliases have been checked, with four explicit implication comparisons recorded in `AUDIT.json`.

**Risk:** The full text of a potentially relevant 2026 article on decay-unstable trees could not be inspected through lawful available access. Its visible abstract establishes a different large-tree property, but the unseen body could contain stronger coverage. Literature searches cannot prove global novelty; this is a self-review.

## Value — PASS

The result gives the smallest possible tree-shaped social network exhibiting a nonmonotone optimal-source policy as transmission reliability changes, rather than an arbitrary nonoptimal pairwise rank reversal. The minimum-size boundary and explicit exact switches test a common single-threshold targeting intuition without relying on heuristics or sampled scenarios.

**Limits:** Uniform independent edge successes, tree topology, expected total cascade and one seed only. No statement about directed or cyclic networks, weighted link reliability, multiple seeds, observed data, or finite-sample statistical uncertainty.

## Closest original sources

The closest direct sources are N. Tsakas (2016), *On Decay Centrality*, https://papers.econ.ucy.ac.cy/RePEc/papers/04-16.pdf , and J. Coroničová Hurajová et al. (2018), *On Decay Centrality in Graphs*, https://journals.msp.org/mscand/article/download/263/262/291 . A related full-text comparison is C. Riveros et al. (2023), https://doi.org/10.4230/LIPIcs.ICDT.2023.12 , and D. Rupnik Poklukar–J. Žerovnik (2025), https://www.preprints.org/manuscript/202502.2148 . Unread 2026 article: https://doi.org/10.2140/mscand.2026.132.1 .

Self-review: passed. Independent audit: not yet performed.

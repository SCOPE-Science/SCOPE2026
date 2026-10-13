# Scientific review: binary length-\(15\), weight-\(3\) deletion capacity

**Correctness — PASS.** Every possible input has at least unit weight among its distinct one-deletion descendants, as shown by an exact three-run-type analysis. The weighted output family totals exactly \(37\). The supplied \(37\)-word code is pairwise deletion-unambiguous, verified with direct string removal and independent index-shift representations for all \(455\) possible input words. These establish a rigorous sharp inequality and construction. Limits: only one deletion and the stated composition/length.

**Originality — PASS, with residual bibliographic risk.** The closest primary studies are Cullina–Kulkarni–Kiyavash (ISIT 2012, arXiv:1211.4056), which prove a chromatic number of \(13\) for this weight layer and construct its checksum classes of size \(35\), and Kulkarni–Kiyavash (arXiv:1211.3128), which supplies general LP fractional-transversal methods and unrestricted/constrained upper bounds. The exact maximum \(37\), its attaining code, and the specialized matching dual weight of \(37\) do not follow from the published coloring theorem alone or from the stated generic bound. Sloane's older single-deletion work and possible unindexed code catalogues pose residual coverage risk; this is not a claim of proven global historical uniqueness.

**Value — PASS.** The sharp value answers a natural exact deletion-code capacity question at length \(15\), sparse composition \(3\). It isolates a substantive coloring-versus-independent-set gap: all \(13\) classes of the familiar optimal coloring have size \(35\), while a stronger size-\(37\) code exists and is provably best. The dual construction supplies a compact structural reason for optimality beyond a solver output. No extension to other lengths/weights or decoding efficiency is asserted.

The primary full texts, search aliases, implication comparisons, and residual risks are recorded in `AUDIT.json`. Independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.

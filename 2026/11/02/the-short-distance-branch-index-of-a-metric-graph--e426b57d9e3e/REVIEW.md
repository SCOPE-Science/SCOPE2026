# Mathematical review

## Correctness — PASS

The stated finite connected simple metric-graph hypotheses ensure a positive shortest-edge length and exclude loops/parallel edges. For all indicated radii, short geodesics connect either points on one edge or points on two edges meeting at one vertex; the precise integration areas are \(2\ell_e r-r^2\) and \(r^2\) per unordered adjacent-edge pair. Their sum proves the claimed exact CDF and derivatives. Handshaking and tree degree identities rigorously establish subdivision invariance, the Betti relation, exact degree-three branch recovery and sharp extremal cases. The independent rational half-plane integration in `verify.py` passes, but finite tests are not relied upon to prove the theorem.

## Originality — PASS (provisional priority)

Searches compared the local CDF coefficient against aliases involving metric-network K-functions, short distance distributions, valence square sums, first Zagreb index, trivalent branch counts, edge-pair incidence and distance tomography. The closest identified network-statistics papers develop K-functions and pair correlations, not an explicit subdivision-invariant inverse branch signature in their accessible statements. The complete accessible paper by Eckardt and Mateu develops different edge-count-based network intensities and distinguishes their distances from shortest paths weighted by edge lengths. Related known metric-star distance inversion, cactus cycle singularities, and controlled edge-selective network tomography do not imply the universal unlabeled uniform-arclength short-range identity. An earlier exact coefficient could be hidden in inaccessible full texts, so historical priority remains provisional; the evidence is not a proof of global novelty.

## Value — PASS

The branch index is an intrinsic, length-independent graph statistic accessible without graph labels or edge-specific experiments, despite arbitrary edge-length variation and degree-two subdivision. This gives an exact *inverse* consequence of a natural population measurement, not just a forward quadrature formula. The subcubic-tree branch-count characterization and the sharp path/star bounds explain what the statistic distinguishes and what it cannot distinguish; such branch information is motivated by unlabeled geometric network sensing. No finite-sample guarantee or whole-graph uniqueness is asserted.

## Literature and limits

Closest framework sources: Baddeley et al., *Stat* (2017), DOI 10.1002/sta4.135; Rakshit et al., *Spatial Statistics* (2017), DOI 10.1016/j.spasta.2017.10.002; Rakshit et al., *J. Stat. Softw.* (2019), DOI 10.18637/jss.v090.i01. The full accessible text of Eckardt and Mateu, *TEST* (2020 online), DOI 10.1007/s11749-020-00720-4, was compared at Section 2.3. The two 2017 complete manuscripts and the 2019 PDF were inaccessible; the absence of an equivalent therein is not certified. Scope is finite connected simple graphs, strictly positive lengths, exact uniform population measurements and the specified small-radius interval.

Self-review: passed. Independent audit: not yet performed.

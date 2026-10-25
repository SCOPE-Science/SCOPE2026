# Scientific review

**Correctness — PASS.** Exact normal equations for a two-column Euclidean least-squares correction reduce to \(Q=uvxz\) and \(y(ux+vz)=-Q\). Because \(xz>0\), eliminating the normalized residual gives the exact one-variable frontier. Attainment and divergence at both ends prove necessity and sufficiency, not just a numerical witness. Compactness gives a uniform contraction below threshold. An exact rational-radical example and a balanced polynomial factorization verify the sharp boundaries. The accompanying checker replays the symbolic facts and numerical constructions, but finite checks are not used as an infinite proof.

**Originality — PASS (bounded source search).** The algorithm and the equal-weight Jordan stagnation theorem are established prior work. The claimed new portion is the prescribed unequal two-edge Euclidean frontier, exact same-product balanced-versus-anisotropic reversal, and its direct first-cycle consequence for the motivating accelerator. Diagonal similarity to a Jordan block is not unitary and does not transport Euclidean GMRES minima. The strongest reviewed GMRES history and arbitrary-matrix construction results do not impose the two prescribed weights. Searches of related primary literature and mathematical result records found no stronger statement covering this weight-specific sharp criterion, with residual risk from unindexed or older weighted-bidiagonal work.

**Value — PASS.** This exact classification exposes a hidden failure mode of residual-minimizing acceleration: matrices with identical eigenvalues and identical coupling products can be respectively safe or stalled according to anisotropy, even while the underlying elementary fixed-point scheme solves in three steps. The weight-ratio frontier supplies a precise diagnostic for a natural three-site prototype rather than an arbitrary numerical example.

**Closest literature.** Adler–He–Hu–Lefebvre (2026) supply the two-grid algorithm, Tichý–Liesen (2006) the equal-coupling Jordan theory, and Soodhalter (2026) general prescribed stagnation phenomena. None of these inspected sources supplies the ratio-dependent prescribed-weight law. This does not certify global uniqueness.

**Limitations.** Real three-dimensional positive upper links, exact arithmetic, Euclidean residual, and one specified accelerator cycle; no higher-dimensional or floating-point stability guarantee. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.

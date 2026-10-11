# Scientific review: prime-square parabolic Fourier fourth moments

## Correctness — PASS
The exact fourth moment is reconstructed from the ordered pair-sum map over the ring \(\mathbb Z/p^2\mathbb Z\), with counting-measure input and probability-measure output. Distinct residue classes have only the two symmetry-related lifts of each pair; equal residue classes collapse to one cyclic convolution on \(\mathbb F_p\). The resulting separated formula and cyclic Parseval identity yield the nonnegative quartic deficit without an inequality loss. Since \(p-2>0\), its zero set is exactly the union of the residue-character lines. The quantitative stability estimate follows by concentrating residue mass and then Fourier mass; it has been checked with the stated normalization.

The standalone checker tests the pair fibers and deficit for Gaussian-integer inputs at \(p=3,5,7\), all character packets at those primes, four direct fourth moments from Fourier synthesis, and sample stability inequalities. The universal conclusion rests on the proof, not the finite experiments. The proof requires odd \(p\); no characteristic-two extension is inferred.

## Originality — PASS, with a defined residual risk
Mockenhaupt–Tao, arXiv:math/0204234, Section 5, supplies the established even-moment maximum-fiber method. It can recover the **upper bound and sharp norm** here once the elementary fiber maximum is known; the norm itself is not presented as a standalone novelty. Hickman–Wright, arXiv:1801.03176, Sections 2–3, explicitly develops local-ring parabolic wave packets, but the examined results do not state their **necessity** for equality in this sharp fourth moment or the global two-term defect. González-Riquelme–Oliveira e Silva, arXiv:2405.16647, treats sharp extension on finite fields, not this nilpotent ring. A separate inspected published finite-field moment-curve stability theorem concerns constant-modulus profiles rather than residue-character localization. These comparisons are implication-based and do not rest on title mismatches.

The main unresolved originality risk is a historical wave-packet equality argument, perhaps implicit in \(p\)-adic restriction or finite-local-ring additive-energy literature, that was not indexed by the searches. This is a search limitation, not evidence of mathematical independence.

## Mathematical value — PASS
The first nonfield prime-power modulus exhibits a natural obstruction absent for fields: the parabola becomes affine on each prime-residue packet. The new statement gives the complete optimizer geometry, an orthogonal basis of \(p^2\) extremal rays, and an exact two-mechanism defect that distinguishes residue mixing from internal Fourier dispersion. The global distance-to-packet estimate makes this structural classification useful for detecting near-saturation of the sharp inequality. Neither a better constant in the distance estimate nor extension to higher prime powers is claimed.

Same-model review: passed. Independent audit: not yet performed.

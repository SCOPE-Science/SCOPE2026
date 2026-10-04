# Review

## Correctness
PASS. The claim has a finite, explicit domain: all nonempty proper row subsets of the order-10 DFT. Published results supply necessity of uniform distribution and affine/complement invariance. Uniform row sets reduce to seven affine representatives through cardinality 5. Consecutive representatives are Vandermonde full spark; the only nonconsecutive candidate \(\{0,1,3\}\) has determinant
\[
-\,(x_1-x_2)(x_1-x_3)(x_2-x_3)(x_1+x_2+x_3),
\]
and the last factor cannot vanish for distinct tenth roots because a three-term unit-circle zero sum would force a primitive cube-root ratio. The exceptional \(\{0,1,3,4\}\) has the published zero minor on columns \(\{0,1,2,6\}\). Exact exhaustive cyclotomic arithmetic reproduces every case and the complement counts.

Risk: the proof relies on the cited published invariance and necessity theorems. The included verifier checks the order-10 finite consequences directly for uniformly distributed sets, but it does not reprove the general theorem that nonuniform sets cannot be full spark.

## Originality
PASS on the evidence inspected. The closest source, Alexeev--Cahill--Mixon, gives the order-10 counterexample and explicitly leaves the general composite characterization open; it does not classify every order-10 row set. Achanta et al. characterize several structured one-missing-row families and revisit the same counterexample, but do not give a complete order-10 affine-orbit census. Tang still presents the arbitrary-composite sufficiency problem as unresolved in 2017. Targeted published-finding corpus and web searches for the exact order-10 classification, aliases, affine formulations, and stronger covering statements returned no prior statement implying the final classification.

Residual risk: a differently phrased or poorly indexed complete order-10 classification could exist. Search non-detection is evidence, not a novelty proof.

## Value
PASS. Order 10 is the smallest highlighted non-prime-power case where uniform distribution is known not to suffice. A complete classification identifies the obstruction sharply: exactly one affine orbit at cardinality 4 and its complement at cardinality 6. This converts an isolated counterexample into a natural exact boundary theorem for full-spark harmonic frames and Fourier sparse-recovery designs.

Same-model review: passed. Independent audit: not yet performed.

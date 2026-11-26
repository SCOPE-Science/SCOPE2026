# Independent mathematical audit

## correctness

PASS

Cornelio–de Oliveira's Eqs. (1), (6), and (7) give the stated cut, convex roof, and concurrence formula at α=2. With the frozen qubit order the coefficients for the large cut are the diagonal (3,2,6,3)/√58, not a 2×2 Schmidt matrix. Squaring and normalizing gives reduced purity 737/1682. In either direct-pair reduction only the |00⟩,|11⟩ block survives, with diagonal 13/58 and 45/58 (interchanged for the other pair) and coherence 24/58. For such a positive 2×2 block with entries a,d,z, the square roots of the nonzero spin-flip eigenvalues are √(ad)±|z|, so concurrence equals 2|z|=24/29. Each convex-roof factor is 1−C²/2=553/841. The residual log₂[(553/841)²/(737/1682)] is log₂(611618/619817), strictly negative by integer comparison. Tracing either crossed pair leaves distinct traced-out labels and a separable diagonal state. Independent exact bit-index partial traces and arithmetic replayed with `python3 /workspace/branches/independent-checks.py 4` give these fractions and −0.0192114588808 bits; the uploaded checker was read, not executed. This establishes a witness, not optimality, a result at other orders, or the general monogamy equivalence.

## originality

PASS

The existence of four-qubit order-two violations and the concurrence formula are prior work. The relevant distinct claim is the explicit elementary four-term state with a fully exact violation. Its large-cut spectrum differs from the published numerical witness at the stated precision, so that example is not identical up to cut-local unitaries. No inspected source gives or implies this exact state and residual as a particular instance without a separate witness calculation.

## value

PASS

This answers a concrete gap left by the numerical counterexample: a short state whose violation can be checked strictly and by hand. The shared Schmidt labels let one read off global purity, while a repeated corner amplitude gives equal nonzero direct-pair coherences, producing the sign by a rational comparison. The example can be used as an exact benchmark for the convex-roof formula and for the inequality without accepting a numerical search or tolerance. It is not valued as a slight numerical improvement or a new violation phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.

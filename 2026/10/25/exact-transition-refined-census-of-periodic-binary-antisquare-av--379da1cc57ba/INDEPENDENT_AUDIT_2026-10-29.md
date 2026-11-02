# Independent mathematical audit

## correctness

PASS

Read entire RESULT.md and verify_cyclic_good.py. Baranwal et al Theorem11 gives the minimal antisquare basis, and Proposition18 shows a bi-infinite good word with 001011 must be a nonperiodic one-defect word, excluding it and its reversal/complement on any period. Thus periodic good words are exactly eight-factor avoiders. Cyclic XOR difference p maps those eight to 010,101,11111,01110. Any nonzero good p consists of alternating 0-runs length>=2 and 1-runs length2 or4; total number of ones is even, yielding two lifts to bits. With block GF B=z²/(1-z)*(u²z²+u⁴z⁴), marking 1-run starts yields 2n/r * [z^n u^t]B^r, i.e. F=-2z*d_z log(1-z-u²z⁴-u⁴z⁶). Coefficient extraction proves full bivariate finite sum; rotation stabilizers are handled by marked position double counting. Periodic inversion yields primitive necklace a_n=(1/n)sum mu(d)g_(n/d), and factoring denominator (1+z³)(1-z-z³) gives growth 2psi^n+O(1). Fresh independent exhaustive 8190 periodic binary words lengths1..12 were tested for true antisquares up to sufficient order and the four differences and rational census; source checker independently covers n1..15. Neither finite range implies all-n result, which follows from cited structural rigidity and run counting.

## originality

PASS

Qualified PASS for bivariate periodic-point GF, exact transition histogram and necklace counts. Baranwal et al Theorem11, Proposition18, and Theorem19 already supply the forbidden factors, the Pansiot-code run structure and the dominant growth constant, so none of those building blocks is claimed new. Their inspected Theorem19 counts linear finite words, not periodic points by exact circumference and transitions. Some exact periodic formulas might follow routinely from their transfer grammar or older zeta-function literature; this is a meaningful residual priority/value concern.

## value

PASS

A complete multivariate census by circumference and number of cyclic transitions for a natural symbolic-dynamics language of good antisquare-free infinite periodic points is a useful exact invariant; it also determines all primitive and imprimitive necklaces. This extends published linear-word asymptotic growth information to exact periodic-point zeta-type data, not just an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

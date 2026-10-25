# Mathematical review: sharp pluriharmonic Bohr radius asymptotics

## Correctness

**PASS.** For the normalized class and the sharp root from Majumder, Banerjee, Panja and Pramanik (arXiv:2607.27272v1), set \(x=nr\), \(\tau=n(1-\alpha)\), \(S(x)=-\log(1-x)-x\), and \(T_n=\log(1+1/n)-1/n\). The defining equation is \(x+2\tau S(x)=1+2\tau T_n\). Since \(\tau<n\), its right correction is uniformly \(O(1/n)\). Strict root monotonicity yields \(x\to\xi(\tau)\) for a finite limiting \(\tau\), with \(\xi(0)=1\). When \(\tau\to\infty\), \(x\to0\) and \(\tau x^2\to1\). For fixed \(a=1-\alpha\), matching the first two powers of \(n^{-1/2}\) and using the exact derivative proves
\[
r_{n,\alpha}=a^{-1/2}n^{-3/2}-\frac{5}{6a}n^{-2}+O_a(n^{-5/2}).\]
The original source proves the sharpness of this root; these arguments establish its asymptotics. Independent high-precision roots and symbolic series coefficients corroborate the proof, without serving as an infinite-dimensional certificate.

## Originality

**PASS, best of knowledge.** The defining preprint's Theorem 4.1 and surrounding full-text discussion contain an exact sharp equation, a uniqueness proof, and plots for dimensions one through four, but not the dimension-dependent expansion or the crossover profile. The asymptotic analysis is a new conclusion drawn from that established premise. Das (arXiv:2303.14257) studies powered norm-based Bohr radii; Halder (arXiv:2601.12608) studies second vector-valued Bohr radii; and Bayart, Pellegrino and Seoane-Sepúlveda (arXiv:1310.2834) study the classical bounded-holomorphic polydisc radius. Their different hypotheses do not directly yield this normalized sharp-root asymptotic. A later preprint revision or unindexed equivalent result remains a priority risk.

## Mathematical value

**PASS.** The classification identifies a crossover at \(1-\alpha\asymp n^{-1}\), a nonconstant limiting profile, and a sharp fixed-parameter second term. These characterize how an already-established sharp invariant depends on its two natural parameters. The required analysis is elementary implicit-root asymptotics, and its contribution should not be overstated as a new sharp-radius inequality.

## Scope

Integers \(n\ge1\) and parameters \(0<\alpha<1\). The fixed-parameter error is not uniform at \(\alpha\uparrow1\). No claim is made about the distinct classical holomorphic or powered vector-valued Bohr radii. No formal proof assistant verification or expert attestation is claimed.

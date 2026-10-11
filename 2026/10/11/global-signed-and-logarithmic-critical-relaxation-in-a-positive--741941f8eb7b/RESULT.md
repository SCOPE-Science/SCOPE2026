# Global signed and logarithmic critical relaxation in a positive rational flip map

## Finding
Ohmori and Yamazaki's positivity-preserving rational discretization has a flip threshold at \(\tau=2\). Exactly at that threshold, define
\[
 f(x)=\frac{2x^2+x+8}{8x^2+3},\qquad x>0,\qquad x_{j+1}=f(x_j).
\]
For every \(x_0>0\), \(x_0\ne1\), put \(\sigma=\operatorname{sgn}(x_0-1)\). All iterates remain positive, approach \(1\), and alternate sides of \(1\). Moreover, there exists a finite real constant \(C(x_0)\) such that
\[
\boxed{\frac{1}{(x_{2n}-1)^2}=\frac{112}{121}n-\sigma\frac{40\sqrt7}{121}\sqrt n+\frac{15}{121}\log n+C(x_0)+o(1).}
\]
The assertion uses the **unmodified physical discrete time**: \(x_{2n}\) denotes exactly \(2n\) original iterations. The universal signed \(\sqrt n\) and logarithmic terms refine the familiar leading algebraic relaxation at period doubling.

## Assumptions and scope
The map is defined on the full positive half-line. Fix \(x_0\in(0,\infty)\setminus\{1\}\). The claim concerns \(n\to\infty\) over positive integers. The sign \(\sigma\) is fixed by the initial value, not chosen at each step. The constant \(C(x_0)\) is allowed to depend on the initial condition. The theorem is at the single critical parameter \(\tau=2\), not uniform in a varying parameter and not about the supercritical attracting two-cycle.

## Proof
**1. Exact positive dynamics.** Direct rational simplification gives
\[
 f(x)-1=-\frac{(x-1)(6x+5)}{8x^2+3}.
\]
Thus positive inputs map to positive outputs and an orbit not starting at \(1\) changes side of \(1\) at each step. Set \(g=f\circ f\). Polynomial composition and factorization give
\[
 g(x)-x=-\frac{56(x-1)^3(4x^2+3x+4)}{Q(x)},
\]
\[
 g(x)-1=\frac{(x-1)(6x+5)(52x^2+6x+63)}{Q(x)},
\qquad Q(x)=224x^4+32x^3+408x^2+128x+539.
\]
Every factor other than \((x-1)\) and \((x-1)^3\) has the indicated positive sign for \(x>0\). Hence \(g\) preserves each side of \(1\) and moves monotonically toward \(1\) without crossing it. The monotone bounded sequence \(x_{2n}\) converges to a fixed point of \(g\); the formula shows its only positive fixed point is \(1\). Hence the entire orbit converges to \(1\), and no denominator below vanishes.

**2. Exact local jet.** Write \(u=x-1\). Taylor expansion of the *exact rational* second iterate at \(u=0\) gives
\[
 g(1+u)-1=u-\frac{56}{121}u^3+\frac{280}{1331}u^4+\frac{224}{1331}u^5-\frac{3136}{14641}u^6+O(u^7).
\]
Squaring and reciprocating gives the more directly useful identity
\[
 \frac{1}{[g(1+u)-1]^2}-\frac1{u^2}
 =A+Bu+C_2u^2+O(u^3),
\]
\[
 A=\frac{112}{121},\qquad B=-\frac{560}{1331},\qquad C_2=\frac{4480}{14641}.
\]
The remainder is uniform for real \(u\) in a sufficiently small punctured neighborhood of zero, since the rational difference after cancellation is analytic there.

**3. Summation with a summable remainder.** Put \(u_n=x_{2n}-1\) and \(w_n=u_n^{-2}>0\). By Step 1, \(u_n\to0\) with constant sign \(\sigma\). Step 2 becomes
\[
 w_{n+1}-w_n=A+\sigma B w_n^{-1/2}+C_2w_n^{-1}+O(w_n^{-3/2}). \tag{1}
\]
The left increment tends to \(A>0\); summation (or Stolz--Cesàro) gives \(w_n/n\to A\). Equation (1) now yields \(w_n=An+O(\sqrt n)\), since its error after \(A\) is \(O(n^{-1/2})\). Therefore
\[
 w_{n+1}-w_n=A+\frac{\sigma B}{\sqrt A}\,n^{-1/2}+O(n^{-1}),
\]
which, upon summation, sharpens to
\[
 w_n=An+\sigma p\sqrt n+O(\log n),\qquad p=\frac{2B}{\sqrt A}=-\frac{40\sqrt7}{121}.
\]
Substitute this estimate back into (1), using the Taylor expansion of \(w_n^{-1/2}\), to obtain
\[
 w_{n+1}-w_n=A+\frac{\sigma p}{2\sqrt n}+\frac{q}{n}+O\!\left(\frac{1+\log n}{n^{3/2}}\right),
\]
where
\[
 q=\frac{C_2}{A}-\frac{B^2}{A^2}=\frac{15}{121}.
\]
Meanwhile the forward difference of \(An+\sigma p\sqrt n+q\log n\) has exactly the three displayed leading terms and error \(O(n^{-3/2})\). Thus the forward differences of
\[
 R_n=w_n-An-\sigma p\sqrt n-q\log n
\]
are absolutely summable (majorized by a multiple of \((1+\log n)n^{-3/2}\)). It follows that \(R_n\to C(x_0)\in\mathbb R\), completing the proof. This yields a true \(o(1)\) residual, stronger than an unbounded logarithmic-error estimate.

## Verification
The companion `verify.py` checks the two rational factorizations, the local jet and inverse-square coefficients over \(\mathbb Q\), and the symbolic identities giving \(p\) and \(q\); it additionally runs noncertifying finite-orbit checks for initial states on both sides of \(1\). Run `python verify.py` with Python 3 and SymPy. The proof of convergence and the summability argument above establish the quantifiers for all positive initial values; the numerical output is not used to infer the asymptotic law.

## Relationship to prior work
Ohmori and Yamazaki (2022, arXiv:2212.03455v1, Section 3.1, equation 19) introduced this exact map and found its flip threshold at \(\tau=2\), together with the two-cycle above threshold. Those are established results, not new claims. Leonel, Ferreira and Oliveira (2026, arXiv:2602.04091v1, Section 2) describe the generic leading \(n^{-1/2}\) relaxation and crossover near a flip; this theorem does **not** claim novelty for that critical exponent or the generic crossover. The additional content is the exact signed subleading term, the nonzero logarithmic coefficient, and a finite constant remainder valid from every nonfixed positive initial state for this concrete positive rational map. General Fatou-coordinate expansions for parabolic germs (Mardešić et al., arXiv:1710.01268) explain why power/log asymptotics can arise in a much broader local setting, but do not tabulate these coefficients or establish this example's global positive-basin conclusion. A generic parabolic-series method could in principle rederive the local expansion, so priority of these particular constants should not be considered externally certified.

## Limitations
No uniform estimate in a noncritical discretization parameter is asserted. The additive constant \(C(x_0)\) is proved to exist but is not given by a closed elementary formula. The result is in the source's positive state coordinate, so the signed correction is coordinate dependent; it measures the non-symmetric relaxation in precisely that model, not a conjugacy invariant. General parabolic theory and undiscovered model-specific calculations are residual publication-priority risks. Independent verification has not been performed.

## References
1. S. Ohmori and Y. Yamazaki, *Relation of stability and bifurcation properties between continuous and ultradiscrete dynamical systems via discretization with positivity: one dimensional cases*, arXiv:2212.03455v1 (public 2022-12-07), https://arxiv.org/html/2212.03455v1, especially Section 3.1.
2. E. Leonel, C. Ferreira and J. Oliveira, *A phenomenological description of critical slowing down at period-doubling bifurcations*, arXiv:2602.04091v1, https://arxiv.org/html/2602.04091v1, especially Section 2.
3. P. Mardešić, M. Resman, J.-P. Rolin and V. Županović, *The Fatou coordinate for parabolic Dulac germs*, arXiv:1710.01268v2, https://arxiv.org/html/1710.01268v2, Introduction and Section 2.

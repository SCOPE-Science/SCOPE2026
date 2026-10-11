# Sharp quarter-zero law and extremizer dichotomy for positive three-atom Fourier transforms on dyadic cycles

## Finding
Let \(N=2^k\) with integer \(k\ge2\). Every strictly positive three-atom measure on \(\mathbb Z_N\), with three distinct atoms, has **at most \(N/4\) vanishing Fourier coefficients**. The bound is attained for every \(N\). More precisely, all Fourier-zero counts and all maximizers admit the following geometric-arithmetic description.

After translating an atom to \(0\), write
\[
\mu=w_0\delta_0+w_1\delta_a+w_2\delta_b,\qquad
w_0,w_1,w_2>0,\quad 0<a<b<N.
\]
Put \(g=\gcd(N,a,b)\), \(m=N/g\), \(u=a/g\), \(v=b/g\). Thus \(m\ge4\) is a power of two, and \(\gcd(m,u,v)=1\). The number of Fourier zeros is always **exactly one of** \(0,g,2g\). The nonzero cases are exhaustive:

1. **Collinear cancellation:** exactly \(g\) zeros occur if the weight at the unique atom in one parity class of \(\{0,u,v\}\bmod2\) equals the sum of the two weights in the other class. This is the entire degenerate-triangle case. The zeros are the \(g\) frequencies \(t\equiv m/2\pmod m\).
2. **Genuine triangular cancellation:** exactly \(2g\) zeros occur if for some \(t\in\{1,\ldots,m-1\}\), the three points
   \[
   1,\quad e^{-2\pi iut/m},\quad e^{-2\pi ivt/m}
   \]
   have the origin strictly inside their triangle and the positive projective weight triple is
   \[
   (w_0:w_1:w_2)=
   \left(
   \left|\sin\frac{2\pi(v-u)t}{m}\right|:
   \left|\sin\frac{2\pi vt}{m}\right|:
   \left|\sin\frac{2\pi ut}{m}\right|
   \right).
   \]
   The zero frequencies are precisely \(t\pmod m\) and \(-t\pmod m\), each with \(g\) lifts.
3. Every remaining positive weight triple has no Fourier zeros.

In particular, **every maximizer** comes from exactly one of two mutually exclusive mechanisms: \(m=4\) and collinear cancellation, or \(m=8\) and genuine triangular cancellation. An extremizer of the first type, valid for all \(N\), is
\[
\mu=\delta_0+2\delta_{N/4}+\delta_{N/2},\qquad
\widehat\mu(t)=\left(1+e^{-\pi i t/2}\right)^2.
\]
For \(N\ge8\), another extremizer of the second type is
\[
\mu=\delta_0+\sqrt2\,\delta_{N/8}+\delta_{N/4},
\]
whose Fourier transform vanishes precisely when \(t\equiv3\) or \(5\pmod8\).

## Assumptions and scope
The cyclic Fourier transform is unnormalized:
\[
\widehat\mu(t)=\sum_{x\in\mathbb Z_N}\mu(\{x\})e^{-2\pi i tx/N}.
\]
Its normalization does not change zeros. All three weights are strictly positive real numbers; coefficients of arbitrary complex phase or a fourth nonzero atom are excluded. Translation and multiplication of all weights by a common positive scalar do not change Fourier-zero counts. The normalized support \(\{0,u,v\}\) contains three distinct residues because the original atoms are distinct.

## Proof
**Reduction to primitive differences.** Translation multiplies \(\widehat\mu(t)\) by a nonzero unimodular number. With the notation above,
\[
\widehat\mu(t)=w_0+w_1e^{-2\pi iut/m}+w_2e^{-2\pi ivt/m}.
\]
This depends only on \(t\bmod m\). Every zero in \(\mathbb Z_m\) lifts to exactly \(g\) zeros in \(\mathbb Z_N\). Moreover the homomorphism
\[
\Phi:\mathbb Z_m\longrightarrow\mathbb T^2,\qquad
\Phi(t)=\left(e^{-2\pi iut/m},e^{-2\pi ivt/m}\right)
\]
is injective because \(\gcd(m,u,v)=1\). Since there are three distinct atoms, \(m\ge4\).

**Triangle rigidity.** Consider the complex equation
\[
 w_0+w_1X+w_2Y=0,\qquad |X|=|Y|=1.
\]
The side lengths satisfy all triangle inequalities. If they are strict, then the identity \(|w_0+w_1X|=w_2\) gives
\[
 \operatorname{Re}X=\frac{w_2^2-w_0^2-w_1^2}{2w_0w_1}\in(-1,1).
\]
Consequently there are exactly two possible \(X\)'s, complex conjugates, and each determines the unique \(Y=-(w_0+w_1X)/w_2\). Thus there are exactly two possible phase pairs, again complex conjugates. Injectivity of \(\Phi\) implies at most two frequency residues. If a frequency \(t\) occurs, \(-t\) also occurs because the weights are real. The residues cannot coincide: \(t\equiv0\) yields three positive terms, while \(t\equiv m/2\) gives only real phases \(\pm1\) and would force a degenerate triangle. Therefore strict-triangle cancellation occurs at exactly two distinct frequency residues, i.e. \(2g\) lifted zeros.

For a fixed frequency \(t\), a positive solution exists precisely when the origin lies strictly inside the triangle with the three displayed unit vertices. Equivalently, those vertices are not contained in any closed semicircle. The null vector of the two-row matrix of real and imaginary parts is proportional to
\[
\left(\sin\frac{2\pi(v-u)t}{m},
-\sin\frac{2\pi vt}{m},
\sin\frac{2\pi ut}{m}\right)
\]
(up to simultaneous sign reversal according to the Fourier-sign convention). On the interior-triangle branch these three components have the same nonzero sign after a common reversal. Their absolute values therefore yield exactly the claimed projective positive weights, proving the full strict-triangle classification.

**Degenerate triangles.** If one weight exceeds the sum of the other two, no cancellation is possible by the triangle inequality. If the largest equals the sum of the other two, equality in that inequality forces the two smaller vectors to coincide and point opposite the largest. Since the first phase is \(1\), both \(X\) and \(Y\) must belong to \(\{1,-1\}\), and at least one must be \(-1\). Hence \(2ut\equiv2vt\equiv0\pmod m\). The primitive gcd condition implies \(2t\equiv0\pmod m\), so the only possible nonzero frequency is \(t=m/2\). At this frequency the three phases are \(1,(-1)^u,(-1)^v\). Since \(u,v\) are not both even, exactly one atom is in the singleton parity class; cancellation occurs exactly when its weight equals the sum of the other two. It then yields exactly \(g\) lifted zeros. This also proves that no other zero-count possibility exists.

**Sharp quarter bound and extremizers.** If \(m\ge8\), triangle rigidity gives at most \(2g=2N/m\le N/4\). If \(m=4\), any three distinct fourth roots of unity contain an antipodal pair, and the origin lies on an edge, never in the triangle's interior. Strict-triangle cancellation is therefore impossible. Only the degenerate case remains, giving at most \(g=N/4\) zeros. The displayed first extremizer has transform \((1+e^{-\pi it/2})^2\), vanishing precisely for \(t\equiv2\pmod4\), and realizes the upper bound for every \(N\).

For equality, \(m>8\) is impossible because \(2N/m<N/4\). At \(m=4\), equality requires degenerate parity cancellation. At \(m=8\), equality requires strict-triangle cancellation, with the weights and frequencies classified above. These cases are disjoint. Finally, for the second displayed example set \(z=e^{-2\pi it/8}\); its transform is \(1+\sqrt2 z+z^2\), which vanishes exactly at \(z=e^{\pm3\pi i/4}\), corresponding to \(t\equiv3,5\pmod8\). This completes the sharp result and the extremizer dichotomy.

## Verification
The self-contained file `verify_positive_three_sparse.py` checks Fourier sums exactly in the cyclotomic integer ring \(\mathbb Z[X]/(X^{N/2}+1)\), for dyadic orders \(N\). It exhaustively tests 35,658 rational-weight/support cases through \(N=64\), verifies the permitted zero counts and the \(N/4\) bound, and separately checks 24,816 strict-geometry cases using integer circular gaps. It also verifies both displayed infinite families at each dyadic order through \(256\); for the second family it represents \(\sqrt2\) exactly as the sum of two eighth roots, avoiding floating-point zero decisions. Execute `python3 verify_positive_three_sparse.py`; the expected output begins `VERIFY_OK`. These finite computations corroborate rather than replace the general proof.

## Relationship to prior work
Meshulam's finite-group uncertainty inequalities and the published *Exact three-point Fourier uncertainty on every cyclic group* give the sharp bound \(N/2\) on the number of Fourier zeros for unrestricted **complex-valued** three-atom signals on \(\mathbb Z_{2^k}\). That result is attained by choosing complex coefficients, and it does not imply the present positivity-constrained \(N/4\) bound or its two geometric extremizer mechanisms.

The published *Fourier-zero rigidity for unimodular three-point signals on cyclic groups* treats coefficients of equal magnitude but freely varying phases, not independently variable strictly positive magnitudes. Its two-orientation method is related geometrically, but its arithmetic conclusion does not classify positive weighted signals. The published *Dyadic shell classification of Fourier zeros for four-point indicators* concerns four equal coefficients; it does not cover the three-weight theorem.

Tan and Zhang's 2026 theorem concerns nonnegative polynomials divisible by an entire cyclotomic polynomial and the resulting support-diameter restriction. Divisibility by \(\Phi_N\) forces vanishing at **all** primitive \(N\)-th roots. In contrast, \(1+\sqrt2z+z^2\) vanishes at exactly two of the four primitive eighth roots and has degree two, so the cyclotomic-divisibility theorem cannot yield the present sharp bound. This is a distinct positive-coefficient Fourier-zero question, motivated by the separation between positivity and unrestricted Fourier uncertainty.

## Limitations
This theorem concerns three distinct atoms with strictly positive real weights on cyclic groups of dyadic order \(N\ge4\). It does not claim the same constant for groups with odd factors, more atoms, arbitrary complex coefficients, or approximate Fourier zeros. The originality comparison includes three directly relevant publicly available mathematical results in full; the complete Tan--Zhang preprint and some older sparse-cyclotomic papers were unavailable for full-text inspection. Thus an unindexed equivalent result is a residual literature risk.

## References
- H. Tan and Y. Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646, first publicly posted 2026-09-07.
- *Exact three-point Fourier uncertainty on every cyclic group*, published research record dated 2026-10-04, identifier `2026/10/4/SCOPE-exact-three-point-fourier-uncertainty-on-every-cyclic-group--cf7d7124f263`.
- *Fourier-zero rigidity for unimodular three-point signals on cyclic groups*, published research record dated 2026-10-04, identifier `2026/10/4/SCOPE-fourier-zero-rigidity-for-unimodular-three-point-signals-on-cycl--a8ba65401394`.
- *Dyadic shell classification of Fourier zeros for four-point indicators*, published research record dated 2026-10-04, identifier `2026/10/4/SCOPE-dyadic-shell-classification-of-fourier-zeros-for-four-point-indi--68cf8ce2dd05`.
- R. Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first posted 2003-12-22.
- T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, arXiv:math/9511209, first posted 1995-11-13.

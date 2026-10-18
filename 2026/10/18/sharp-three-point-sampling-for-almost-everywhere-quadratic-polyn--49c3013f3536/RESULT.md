# Sharp three-point sampling for almost-everywhere quadratic polynomial phase retrieval

## Finding
Let \(\omega=\exp(2\pi i/3)\). For a complex quadratic \(P(z)=a+bz+cz^2\), record the six squared magnitudes
\[
I_j=|P(\omega^j)|^2,\qquad J_j=|P'(\omega^j)|^2,\qquad j=0,1,2.
\]
For Lebesgue-almost every \((a,b,c)\in\mathbb C^3\), these data determine \(P\) among **all** complex polynomials of degree at most two, up to multiplication by a constant of modulus one. Three roots per channel are sharp: one or two roots per channel fail almost-everywhere recovery. This is not all-signal recovery: the two nonproportional polynomials
\[
P(z)=7+6z+2z^2,\qquad Q(z)=8+4z+3z^2
\]
have identical three samples in both channels, namely \((I_0,I_1,I_2)=(225,21,21)\) and \((J_0,J_1,J_2)=(100,28,28)\).

More precisely, on the full-measure nondegenerate locus \(bc\ne0\) and \(|b|/|c|\notin\{1,2,4\}\), every measurement fiber contains at most two phase classes, given by the explicit algebraic two-branch rule below; one class is selected for almost every input by a single energy-consistency equation.

## Assumptions and scope
All coefficients are unrestricted complex numbers. The derivative \(P'\) means the usual complex derivative \(dP/dz\). The original analytic trigonometric polynomial \(x\mapsto P(e^{2\pi ix})\) has derivative of magnitude \(2\pi|P'(e^{2\pi ix})|\), so replacing the derivative in the observation with that real-variable derivative only rescales the second intensity channel by the known constant \(4\pi^2\). Uniqueness is modulo a single global unimodular scalar, not independent rotations of individual coefficients. Almost-everywhere refers to six-dimensional real Lebesgue measure on \(\mathbb C^3\), not a distribution over sample locations. For the lower bound at smaller sample counts, use the \(M\)-th roots of unity for \(M=1,2\).

## Proof
**Step 1: exact recovery of cyclic moments.** Define
\[
H_r=\frac13\sum_{j=0}^2 I_j\omega^{-rj},\qquad K_r=\frac13\sum_{j=0}^2 J_j\omega^{-rj}\quad(r=0,1).
\]
Expanding both squared magnitudes and reducing exponents modulo three gives the four identities
\[
\begin{aligned}
H_0&=|a|^2+|b|^2+|c|^2,\\
H_1&=b\overline a+c\overline b+a\overline c,\\
K_0&=|b|^2+4|c|^2,\\
K_1&=2c\overline b.
\end{aligned}
\]
The remaining cyclic Fourier coefficients are complex conjugates of the first moments, so these four identities contain all six real observed numbers.

**Step 2: complete two-branch inversion away from degeneracy.** When \(c\ne0\), fix its global phase so that \(c>0\) is real. Write \(t=c^2\). Eliminating \(b\) between the last two identities gives
\[
4t^2-K_0t+\frac{|K_1|^2}{4}=0.
\]
For each positive root \(t\), set
\[
c=\sqrt t,\quad b=\frac{\overline{K_1}}{2\sqrt t},\quad S=H_1-c\overline b.
\]
The equation \(c a+b\overline a=S\) is real-linear and, provided \(t\ne|b|^2\), has the unique solution
\[
a=\frac{cS-b\overline S}{t-|b|^2}.
\]
Retain a branch if and only if its coefficients satisfy \(H_0=|a|^2+|b|^2+t\). The two real roots of the displayed quadratic are precisely \(|c|^2\) and \(|b|^2/4\) for the original signal. Thus no other phase classes can appear away from the listed degeneracies.

**Step 3: the alternative energy equation is not identically satisfied.** Fix \(b,c\) after the positive-\(c\) phase convention and suppose \(b\ne0\) and \(|b|/c\notin\{1,2,4\}\). The other branch has \(c_*=|b|/2\) and \(b_*=2cb/|b|\). Both real-linear equations determining \(a\) and \(a_*\) are invertible: their determinants are \(c^2-|b|^2\) and \(|b|^2/4-4c^2\). Accordingly \(a_*\) is a homogeneous real-linear function of \(\Re a,\Im a\). The difference between the reconstructed and original energies,
\[
\Delta(a)=|a_*|^2+|b_*|^2+c_*^2-(|a|^2+|b|^2+c^2),
\]
is a real quadratic polynomial in \(\Re a,\Im a\). At \(a=0\), the two linear equations give \(a_*=0\) and
\[
\Delta(0)=\frac34(4c^2-|b|^2)\ne0.
\]
Hence its zero set has planar Lebesgue measure zero. The excluded conditions on \((b,c)\) are themselves proper real-algebraic hypersurfaces or coordinate hyperplanes. Applying Fubini's theorem (including the unimodular phase parameter before normalizing \(c\)) proves almost-everywhere uniqueness over \(\mathbb C^3\).

**Step 4: sharp sample count.** On the open gauge chart \(c>0\), the coefficient space modulo global phase has five real dimensions. With \(M\le2\) sample roots per channel, the measurement map takes values in \(\mathbb R^{2M}\), of dimension at most four. It is real polynomial on that chart. On the open dense set where its Jacobian has maximal rank \(r\le 2M<5\), the constant-rank theorem gives positive-dimensional local fibers of dimension \(5-r\). The complement of this set has measure zero, since a nonzero maximal Jacobian minor is a polynomial. Thus almost-everywhere injectivity fails for each \(M\le2\), completing sharpness.

**Step 5: exact nongeneric ambiguity.** The given integer polynomials have equal cyclic moments \((H_0,H_1,K_0,K_1)=(89,68,52,24)\), obtained by direct integer arithmetic. Inverting the three-point DFT yields the two displayed intensity triples. Their leading coefficients and constant coefficients have different ratios, so they are not scalar multiples. They demonstrate why almost-everywhere cannot be replaced by all-signal recovery.

## Verification
The standalone `checker.py` reproduces the integer witness without floating-point assumptions, verifies the two energy branches for the test input \((a,b,c)=(0,3,1)\) (original energy \(10\), false-branch energy \(25/4\)), numerically reconstructs the original cyclic moments from the six intensities, and tests the two-branch algorithm on 1,000 deterministic pseudorandom complex triples. Run with `python checker.py`; the corresponding captured output is in `checker.out`. Finite numerical tests supplement rather than establish the measure-theoretic proof, whose only genericity step is the nonzero quadratic energy polynomial.

## Relationship to prior work
Jaming and Rathmair, *Uniqueness of phase retrieval from three measurements* (arXiv:2205.08753v1, first public 18 May 2022), Section 3.1, Proposition 3.2, prove recovery for all degree-at-most-two analytic trigonometric polynomials using five equally spaced points in each channel; Lemma 3.3 and Proposition 3.4 give uniform-recovery counterexamples with four points, and Question 3.5 asks precisely about almost-everywhere uniqueness at smaller sampling budgets. Their all-signal threshold neither proves nor precludes the present three-point almost-everywhere result. Huang, Rong, Wang and Xu, *Almost Everywhere Generalized Phase Retrieval* (arXiv:1909.08874v1), establish a generic six-measurement sufficiency theorem for complex three-dimensional phase retrieval, but genericity there is over measurement operators and does not establish that this fixed, derivative-weighted Fourier measurement array is injective almost everywhere. The present algebraic inversion is specific to that fixed array.

## Limitations
The classification of singular or degenerate coefficients is not attempted; in particular, no claim of all-signal injectivity is made. The result does not extend automatically beyond degree two or to arbitrary sample meshes, nor does it supply quantitative stability near the quadratic exceptional locus. Literature searches, including semantic-record checks, cannot prove absolute uniqueness of the result in all unpublished or unindexed work. No independent external mathematical audit is claimed.

## References
1. P. Jaming and M. Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753v1 (2022), Section 3.1, Proposition 3.2, Lemma 3.3, Proposition 3.4, Question 3.5. https://arxiv.org/html/2205.08753v1
2. M. Huang, Y. Rong, Y. Wang and Z. Xu, *Almost Everywhere Generalized Phase Retrieval*, arXiv:1909.08874v1 (2019), Sections 1 and 3--4. https://arxiv.org/html/1909.08874v1

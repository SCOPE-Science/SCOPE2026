# Directional mutation–selection has escaping finite equilibria but no infinite equilibrium

## Finding

For the countably infinite mutation–selection system introduced by Pollett [1], a natural class of directional, bounded mortality profiles has no nonzero equilibrium for **any** birth rate, despite admitting positive equilibria on all sufficiently large finite trait cutoffs whenever the birth rate exceeds limiting mortality. Those finite equilibria retain positive total population density but shed their mass from every fixed set of traits. The limiting critical birth rate is exactly the limiting mortality, and a finite-cutoff spectral quantity gives an explicit bound on spurious mass within any fixed trait window.

Precisely, write \(p_k=(1-r)r^{|k|}/(1+r)\) for \(k\in\mathbb Z\) and \(0<r<1\). Assume
\[
0<\mu_\infty<\mu_i\le M<\infty\quad(i\in\mathbb Z),\qquad
\lim_{i\to+\infty}\mu_i=\mu_\infty.
\]
For any \(\lambda>0\), define \((Px)_i=\sum_{j\in\mathbb Z}p_{i-j}x_j\), \(m(x)=\sum_i x_i\), and the infinite equations
\[
\dot x_i=\lambda(1-m(x))(Px)_i-\mu_i x_i,
\qquad x\in\ell^1_+(\mathbb Z),\quad 0\le m(x)\le1.
\]
**Theorem.** The only equilibrium of this infinite system is \(x=0\).

For \(I\ge0\), put \(J_I=\{-I,\ldots,I\}\), \(P_I=(p_{i-j})_{i,j\in J_I}\), \(D_I=\operatorname{diag}(\mu_i:i\in J_I)\), and \(L_I=D_I^{-1}P_I\). Let \(\rho_I>0\) be its Perron eigenvalue, and let its positive Perron vector \(\phi^{(I)}\) have coordinate sum one. Then
\[
0<\rho_I<\frac1{\mu_\infty},\qquad
\rho_I\nearrow\frac1{\mu_\infty}.
\]
For every finite nonempty \(F\subset\mathbb Z\), once \(F\subset J_I\), the **quantitative escape bound** is
\[
\sum_{i\in F}\phi_i^{(I)}\le
\frac{\rho_I^{-1}-\mu_\infty}{\min_{i\in F}(\mu_i-\mu_\infty)}
\longrightarrow0.
\]
If the mortality profile is nonincreasing, this strengthens, for each fixed integer \(K\), to
\[
\sum_{-I\le i\le K}\phi_i^{(I)}\le
\frac{\rho_I^{-1}-\mu_\infty}{\mu_K-\mu_\infty}\longrightarrow0,
\]
so the Perron trait mass escapes specifically toward \(+\infty\). Both the arctan and logistic directional-selection profiles in [1] meet these assumptions.

For the absorbing-boundary finite system
\[
\dot x_i=\lambda\Big(1-\sum_{j\in J_I}x_j\Big)
\sum_{j\in J_I}p_{i-j}x_j-\mu_i x_i,\qquad i\in J_I,
\]
there is no nonzero equilibrium if \(\lambda\le\mu_\infty\). If \(\lambda>\mu_\infty\), every sufficiently large cutoff has exactly one nonzero equilibrium, namely
\[
x^{(I)}=\left(1-\frac1{\lambda\rho_I}\right)\phi^{(I)},
\qquad
\|x^{(I)}\|_1\longrightarrow1-\frac{\mu_\infty}{\lambda}>0,
\]
while every fixed coordinate \(x_i^{(I)}\) tends to zero. Thus the finite equilibrium sequence has no strong \(\ell^1\) limit even though its total densities converge to a positive number.

## Assumptions and scope

All rates \(\lambda\), \(\mu_\infty\), and \(r\) are fixed, with \(\lambda>0\), \(\mu_\infty>0\), \(0<r<1\). The mortality sequence is bounded and strictly above its right-hand limiting infimum at every finite trait. It need not be monotone except for the one-sided escape conclusion. The system is deterministic, on nonnegative absolutely summable trait distributions of mass at most one. The finite sections suppress births whose mutant traits fall outside \(J_I\); they do **not** renormalize the mutation kernel. The claim does not identify long-time limits of infinite-system trajectories.

In particular, [1] studies \(\mu_i=\mu_\infty+(c-\mu_\infty)(1/2-\arctan(i/e)/\pi)\) or \(\mu_i=\mu_\infty+(c-\mu_\infty)/(1+\exp(i/e))\), for \(c>\mu_\infty\), \(e>0\). Each is strictly decreasing, bounded, greater than \(\mu_\infty\), and approaches \(\mu_\infty\) as \(i\to+\infty\).

## Proof

**1. The infinite equilibrium obstruction.** Suppose a nonzero equilibrium \(x\) exists. Put \(m=\sum_i x_i>0\), \(a=\lambda(1-m)\), and \(y=Px\). Since every \(\mu_i>0\), the equilibrium equation forces \(m<1\), hence \(a>0\). The discrete Laplace kernel is a probability mass function with every coefficient strictly positive. Consequently \(y_i>0\) for all \(i\), and \(y\in\ell^1_+(\mathbb Z)\). The equilibrium equation is \(a y_i=\mu_i x_i\). Summing over \(i\), using \(\sum_i y_i=m\), yields
\[
a=\frac{\sum_i\mu_i x_i}{m}>\mu_\infty,
\]
where strictness follows since every \(\mu_i>\mu_\infty\). All sums are finite because \(\mu_i\le M\) and \(x\in\ell^1\).

The elementary Green-kernel identity
\[
(1+r^2)p_k-r(p_{k-1}+p_{k+1})=(1-r)^2\mathbf 1_{\{k=0\}}
\]
gives, by convolution and the equilibrium relation,
\[
y_{i+1}-2y_i+y_{i-1}
=\frac{(1-r)^2}{r}\left(1-\frac a{\mu_i}\right)y_i.
\]
Because \(\mu_i\to\mu_\infty<a\), the right side is strictly negative for all sufficiently large positive \(i\). Therefore the positive sequence \(y_i\) is strictly concave on a right half-line. Yet \(y\in\ell^1\) implies \(y_i\to0\). A positive sequence tending to zero cannot have decreasing first differences throughout a half-line: if all such differences are nonnegative it cannot tend to zero, whereas one negative difference and subsequent monotone decrease eventually force negative values. This contradiction proves the infinite nonexistence theorem.

**2. Finite spectral cutoff.** The matrix \(L_I\) is strictly positive. Via the diagonal similarity \(H_I=D_I^{-1/2}P_ID_I^{-1/2}\), its Perron eigenvalue equals the largest Rayleigh eigenvalue of a real symmetric matrix. Since convolution by the symmetric probability kernel is an \(\ell^2\) contraction, \(\|P_I\|_2\le1\), and therefore \(\rho_I\le1/\mu_\infty\); strict inequality follows from finite support and \(\min_{i\in J_I}\mu_i>\mu_\infty\). The \(H_I\) are nested principal submatrices as \(I\) increases, so the Rayleigh principle makes \(\rho_I\) nondecreasing.

For the reverse asymptotic inequality, fix \(\varepsilon>0\) and a block \(B\) consisting of \(N\) consecutive integers sufficiently far to the right that \(\mu_i\le\mu_\infty(1+\varepsilon)\) on \(B\). Once \(B\subset J_I\), use the trial vector with entries \(\sqrt{\mu_i}\) on \(B\) and zero elsewhere in the Rayleigh quotient for \(H_I\). It gives
\[
\rho_I\ge\frac{\sum_{i,j\in B}p_{i-j}}{\sum_{i\in B}\mu_i}
\ge\frac1{\mu_\infty(1+\varepsilon)}
\sum_{|k|<N}\left(1-\frac{|k|}{N}\right)p_k.
\]
For \(N\to\infty\), the last sum tends to one by dominated convergence for the probability kernel. Then let \(\varepsilon\downarrow0\). Hence \(\rho_I\to1/\mu_\infty\).

**3. Escape estimate.** With \(\sum_i\phi_i^{(I)}=1\), the eigen-equation reads \(P_I\phi^{(I)}=\rho_I D_I\phi^{(I)}\). Sum its coordinates: because each column of \(P_I\) sums to at most one,
\[
\rho_I\sum_{i\in J_I}\mu_i\phi_i^{(I)}
=\sum_{j\in J_I}\phi_j^{(I)}\sum_{i\in J_I}p_{i-j}\le1.
\]
Subtract \(\mu_\infty\) times the normalization to obtain
\[
\sum_{i\in J_I}(\mu_i-\mu_\infty)\phi_i^{(I)}
\le\rho_I^{-1}-\mu_\infty.
\]
Restrict this nonnegative sum to any finite \(F\), on which the mortality gap has positive minimum, to get the first bound. If \(\mu_i\) is nonincreasing, the same bound restricted to \(i\le K\) gives the one-sided assertion. The spectral limit drives both right-hand sides to zero.

**4. Finite equilibria.** Any nonzero equilibrium of the finite system is strictly positive by the positive matrix \(P_I\), hence its normalized profile is the unique Perron vector \(\phi^{(I)}\). Its total mass must equal \(1-1/(\lambda\rho_I)\), which is positive precisely when \(\lambda\rho_I>1\). Since \(\rho_I<1/\mu_\infty\), this is impossible for \(\lambda\le\mu_\infty\); if \(\lambda>\mu_\infty\), it holds for all sufficiently large \(I\). Conversely substitution directly verifies the stated positive equilibrium. Its total mass tends to \(1-\mu_\infty/\lambda\), while the escape bound sends each fixed coordinate to zero.

## Verification

The accompanying `verifier.py` checks the discrete Laplace Green-kernel identity exactly with rational arithmetic, and computes finite symmetric Perron problems for the logistic mortality profile with \(\mu_\infty=1\), \(c=2\), \(e=1\), \(r=2/5\), \(\lambda=3\). It tests the finite equilibrium equations, strict spectral bounds, and the one-sided escape inequality on five truncation sizes. Executing the actual bundled script produced `VERIFY_OK`.

The infinite theorem rests on the analytic argument above. The finite numerical calculations are illustrative and cannot establish its infinite-dimensional quantifiers.

## Relationship to prior work

Pollett [1] states the countable-trait deterministic equations and discrete Laplace mutation kernel, rigorously treats constant mortality and the confining-mortality case, and numerically studies the two directional-selection profiles. In Section 6, the bounded-mortality regime remains unresolved; finite-dimensional threshold values for directional selection are explicitly described as diagnostics, not a proven infinite-system equilibrium threshold. The present result proves nonexistence for the stated directional bounded class and rigorously distinguishes the limiting finite-section spectral radius from a genuine equilibrium eigenvector. The extra local-mass inequality quantifies this distinction.

Pollett [2] treats only two traits, and Ackleh and Hu [3] work with finite-dimensional selection–mutation structures. The general measure-valued stationary mutation–selection framework of Bürger and Bomze [4] is relevant background. Its available abstract describes existence and structure under hypotheses not resolved here by full-text comparison; no claim is made to refute or supersede that general framework.

## Limitations

The theorem concerns equilibrium existence and the limit of **absorbing-boundary finite sections** with the full infinite-support mutation kernel. It does not establish the actual time-asymptotic trajectory, the rate of trait drift, stochastic extinction probabilities, or behavior under the source's separately renormalized finite-displacement mutation kernel. The mass-escape bound is an upper bound, not an asserted sharp asymptotic rate. The comparisons to [4] and potentially unindexed spectral literature have residual originality risk because complete textual comparison with [4] was unavailable.

## References

[1] P. Pollett, “Mutation–selection balance on an infinite trait space: confinement, drift and equilibrium,” arXiv:2609.02086v1 (first publicly posted 2026-09-02), https://arxiv.org/abs/2609.02086.

[2] P. Pollett, “Persistence, Thresholds, and Trait Composition in a Regulated Mutation–Selection Model,” arXiv:2606.31146v1 (2026), https://arxiv.org/abs/2606.31146.

[3] A. S. Ackleh and B. G. Hu, “Comparison between stochastic and deterministic selection-mutation models,” *Mathematical Biosciences and Engineering* 4 (2007), 133–154, https://doi.org/10.3934/mbe.2007.4.133.

[4] R. Bürger and I. M. Bomze, “Stationary distributions under mutation-selection balance: structure and properties,” *Advances in Applied Probability* 28 (1996), 227–251, https://doi.org/10.1017/S0001867800027348.

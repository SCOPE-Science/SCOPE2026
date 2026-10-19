# A sharp recommendation exponent and two-channel ignition threshold in an attention-limited cascade map

## Finding

In the two-channel heterogeneous mean-field incidence recurrence of Romero Moreno, Robu and La Poutré, restricted to symmetric self-transmission, the *local activity growth threshold* admits an exact finite-cutoff formula. For a truncated power-law degree distribution with exponent \(2<\tau<3\), recommendation mediation has a sharp infinite-cutoff boundary at \(\alpha_c=\tau-2\). Above this boundary the critical content appeal vanishes by an explicit power law; at the boundary it vanishes logarithmically; below it the limit is strictly positive. Two other consequences describe the same local threshold: under full attention suppression \(\alpha=0\), increasing the degree cutoff strictly *raises* the exact threshold, and for any finite cutoff sufficiently strong bidirectional leakage turns two individually subcritical channels into a jointly growing one.

Here and throughout, threshold and growth refer **only to the linearized mean-field incidence recurrence near its fully inactive state**, not to a theorem on global outbreaks, finite random graphs, or the original stochastic cascade.

Write \(H_{L,s}=\sum_{d=1}^L d^{-s}\) and
\[
 B_L(z;\alpha,\tau)=\frac{1}{H_{L,\tau-1}}\sum_{d=1}^L d^{2-\tau}\left[-\log\left(1-\frac{z}{d^{1-\alpha}}\right)\right].
\]
For each integer \(L\ge1\) and \(\lambda\in[0,1]\), a unique critical appeal
\(r_L^*(\alpha,\lambda,\tau)\in(0,(1+\lambda)^{-1})\) is characterized by
\[
 B_L(r_L^*;\alpha,\tau)+B_L(\lambda r_L^*;\alpha,\tau)=1.
\]
The incidence Perron multiplier lies below, at, or above one as \(r\) lies below, at, or above this appeal threshold, within the physical range \(0<r<(1+\lambda)^{-1}\).

As \(L\to\infty\):
\[
\begin{aligned}
0\le\alpha<\tau-2 &: \quad r_L^*\longrightarrow r_\infty^*\in(0,(1+\lambda)^{-1}),\\
\alpha=\tau-2 &: \quad r_L^*\sim\frac{\zeta(\tau-1)}{(1+\lambda)\log L},\\
\tau-2<\alpha\le1 &: \quad r_L^*\sim \frac{(\alpha-\tau+2)\zeta(\tau-1)}{1+\lambda}\,L^{-(\alpha-\tau+2)}.
\end{aligned}
\]
The positive limit in the first case is the unique solution of the same threshold equation with the finite sums in \(B_L\) replaced by absolutely convergent infinite sums and \(H_{L,\tau-1}\) by \(\zeta(\tau-1)\).

For every \(\lambda\in[0,1]\) and fixed \(2<\tau<3\),
\[
 r_1^*(0,\lambda,\tau)<r_2^*(0,\lambda,\tau)<\cdots<r_\infty^*(0,\lambda,\tau).
\]
Finally, at \(\alpha=0\) and \(r=1/2\), define \(b_L=B_L(1/2;0,\tau)\). Then \(1/2<b_L\le\log2<1\) and the equation
\[
 B_L(\lambda_c/2;0,\tau)=1-b_L
\]
has a unique solution \(0<\lambda_c<1\). For every \(\lambda_c<\lambda<1\), each uncoupled channel has linear multiplier \(b_L<1\), while the coupled system has Perron multiplier greater than one. For \(L=1\), the exact leakage threshold is \(\lambda_c=2-4/e\).

## Assumptions and scope

Fix an integer degree cutoff \(L\ge1\), exponent \(2<\tau<3\), mediation parameter \(0\le\alpha\le1\), leakage \(0\le\lambda\le1\), and self-retransmission appeal \(0<r<(1+\lambda)^{-1}\). Degree probabilities are \(p_d=d^{-\tau}/H_{L,\tau}\) for \(1\le d\le L\). Both message channels have equal self-transmission probability \(r\), and equal cross-transmission probability \(\lambda r\). Degree-\(d\) incoming message probabilities are divided by \(d^{1-\alpha}\). These restrictions ensure that the two exclusive per-contact response probabilities sum to less than one.

For each degree \(d\), let \(I^{(d)}\) be the inactive fraction and \(\Delta S^{(d)},\Delta D^{(d)}\) be newly activated spreader and denier fractions. Set
\[
 \Theta^S=\frac{\sum_d d p_d\Delta S^{(d)}}{\sum_d d p_d},\qquad
 \Theta^D=\frac{\sum_d d p_d\Delta D^{(d)}}{\sum_d d p_d}.
\]
The studied two-channel incidence update is
\[
\begin{aligned}
\Delta S_+^{(d)}&=I^{(d)}\left[1-\left(1-\frac r{d^{1-\alpha}}\right)^{d\Theta^S}\left(1-\frac{\lambda r}{d^{1-\alpha}}\right)^{d\Theta^D}\right],\\
\Delta D_+^{(d)}&=I^{(d)}\left[1-\left(1-\frac{\lambda r}{d^{1-\alpha}}\right)^{d\Theta^S}\left(1-\frac r{d^{1-\alpha}}\right)^{d\Theta^D}\right].
\end{aligned}
\]
It is the published HMF map with the published degree-dependent attention modification, evaluated at the **fully inactive state** \(I^{(d)}=1\), \(\Theta^S=\Theta^D=0\). The inactive-coordinate dynamics have their own neutral directions; only the active incidence block is classified. For nonzero leakage the dominant eigenvector is \((1,1)\); for zero leakage both active channels have the same growth multiplier.

## Proof

**1. Exact Jacobian.** Differentiate the two exponential products at \(\Theta^S=\Theta^D=0\). For a degree \(d\) node, the derivative with respect to the supplying channel is exactly \(-d\log(1-z/d^{1-\alpha})\), not the small-appeal approximation \(z d^\alpha\). Multiplying by its endpoint edge weight \(d p_d/\sum_j j p_j\) and summing gives the symmetric active-incidence matrix
\[
 J_L=\begin{pmatrix}B_L(r)&B_L(\lambda r)\\B_L(\lambda r)&B_L(r)\end{pmatrix}.
\]
Its eigenvalues are \(B_L(r)\pm B_L(\lambda r)\), so its spectral radius is their sum because all entries are nonnegative. This is an exact derivative of the specified recurrence, not an exact stochastic network reproduction number.

**2. The unique admissible finite cutoff.** On \((0,(1+\lambda)^{-1})\), the Perron sum \(R_L(r)=B_L(r)+B_L(\lambda r)\) is continuous and strictly increasing from zero. For \(0<z<1\), \(-\log(1-z)>z\). If \(\lambda>0\), then at \(r=(1+\lambda)^{-1}\) (interpreted as a one-sided limit),
\[
 R_L(r)> (1+\lambda)r\frac{H_{L,\tau-1-\alpha}}{H_{L,\tau-1}}\ge1,
\]
since \(\alpha\ge0\). For \(\lambda=0\), the degree-one term diverges as \(r\uparrow1\). The intermediate-value theorem proves one and only one root inside the physical interval. The signs of \(R_L(r)-1\) give the asserted local active stability classification.

**3. Sharp infinite-cutoff boundary.** Define \(\delta=1-\alpha\) and \(M_L=H_{L,\tau-1-\alpha}\). For \(0\le r\le1/2\), the elementary bound
\[
 0\le-\log(1-u)-u\le\frac{u^2}{2(1-u)}\qquad(0\le u<1)
\]
and \(d^{-\delta}\le1\) imply uniformly in \(L\)
\[
 R_L(r)=\frac{(1+\lambda)rM_L}{H_{L,\tau-1}}\,[1+O(r)].
\]
The constant in the relative \(O(r)\) can be chosen uniformly for \(\lambda\in[0,1]\), \(0\le\alpha\le1\), and \(2<\tau<3\), because the quadratic numerator sum is at most \(M_L\). If \(\alpha\ge\tau-2\), then \(M_L\to\infty\) while \(H_{L,\tau-1}\to\zeta(\tau-1)\). At any fixed positive appeal the Perron multiplier therefore diverges, forcing \(r_L^*\to0\). The displayed uniform estimate applies at \(r=r_L^*\) and yields
\[
 r_L^*\sim\frac{H_{L,\tau-1}}{(1+\lambda)M_L}.
\]
Now \(M_L\sim\log L\) when \(\alpha=\tau-2\), and \(M_L\sim L^{\alpha-\tau+2}/(\alpha-\tau+2)\) when \(\alpha>\tau-2\), giving both sharp constants. If \(\alpha<\tau-2\), the numerator series defining \(R_L\) converges uniformly on compact appeal intervals below the physical endpoint by comparison with \(\sum d^{1+\alpha-\tau}\). Its limit is continuous and increasing, starts at zero, and exceeds one at the endpoint by the same strict lower bound (or diverges if \(\lambda=0\)). The roots therefore converge to the unique strictly positive limiting root.

**4. Degree-cutoff reversal at \(\alpha=0\).** For fixed \(0<z<1\), set \(g_x(z)=-x\log(1-z/x)\) for \(x\ge1\). Differentiating gives
\[
 \frac{\partial g_x(z)}{\partial x}=-\log(1-z/x)-\frac{z}{x-z}<0,
\]
using \(-\log(1-u)<u/(1-u)\). At \(\alpha=0\), \(R_L(r)\) is the edge-weighted mean of \(g_d(r)+g_d(\lambda r)\) over \(1\le d\le L\). Adding the new largest degree strictly decreases this mean, so \(R_{L+1}(r)<R_L(r)\) at every admissible \(r>0\). Strict monotonicity in appeal then implies \(r_{L+1}^*>r_L^*\). This effect originates from the logarithm in the given HMF approximation; its linear small-appeal term is degree-independent.

**5. Two individually subcritical channels can grow together.** Again set \(\alpha=0\). Since \(g_d(1/2)\) decreases with \(d\), and its limit as \(d\to\infty\) is \(1/2\), each \(g_d(1/2)\) lies in \((1/2,\log2]\). Thus their edge-weighted mean \(b_L\) obeys \(1/2<b_L\le\log2<1\). The continuous strictly increasing function \(\lambda\mapsto B_L(\lambda/2)\) runs from zero to \(b_L>1-b_L\); hence the unique threshold \(\lambda_c\) exists inside \((0,1)\). For \(\lambda>\lambda_c\), the Perron multiplier exceeds one while each diagonal eigenvalue \(b_L\) is strictly less than one; both exclusive per-contact response probabilities sum to less than one when \(\lambda<1\). For \(L=1\), solve \(-\log(1-\lambda_c/2)=1-\log2\) to obtain \(\lambda_c=2-4/e\). This finishes all claims.

## Verification

The standalone standard-library program `check.py` computes the exact weighted logarithmic incidence Jacobian independently by finite differencing of the displayed nonlinear recurrence, checks finite-root identities and strict cutoff ordering, compares coupled and isolated multipliers, and checks the logarithmic/power finite-size scaling at selected degree cutoffs. Run `python3 check.py` from the extracted package directory. These finite calculations are corroboration; the quantified infinite-cutoff statements and all-parameter inequalities rely on the analytic proof above.

## Relationship to prior work

Romero Moreno, Robu and La Poutré give the two-channel HMF recurrence (their equation (2)), its small-appeal decoupled threshold (equation (3)), and simulation evidence that limited attention suppresses hub advantages while recommendation mediation can restore them (Section 3.3). They also describe backfire from counter-information. Those qualitative statements are credited; the present exact finite-appeal, coupled matrix, cutoff-dependent ordering and three-regime parameter frontier are distinct. In particular, equation (3) replaces the logarithms by their first-order approximations and cannot yield the strict cutoff reversal at finite appeal.

Connectivity-dependent contact saturation and power-law threshold shifts are well established, including Joo and Lebowitz's SIS-with-saturation model, Giuraniuc and colleagues' topology-dependent interactions, and earlier equal-infectivity network models. General co-contagion and backlash are also known; the review by Hébert-Dufresne and colleagues surveys them. The general degree-moment criterion and the principle of a two-type spectral threshold are **not** new. The narrower contribution is the exact critical appeal and finite-cutoff effects within the specified attention-modified *published incidence map*, including its noninfinitesimal logarithmic derivative and the coexistence of individually subcritical channels with coupled active growth.

## Limitations

This is a local deterministic linearization, not a theorem on the probability of a macroscopic cascade, the final cascade size, or equilibrium stability of all inactive coordinates. The HMF ansatz uses fractional exposure counts and logarithmic contact probabilities; its local multiplier at appreciable appeal may differ from the exact physical independent-cascade branching factor. The special results on cutoff reversal and the explicit leakage window require \(\alpha=0\). The power-law asymptotics require \(2<\tau<3\), degree support starting at one, symmetry of self-appeals, and the stated degree-dependent receiving probability. Assortativity, repeated contacts, correlated messages, unequal appeals, and random-graph finite-size corrections are not covered. Historical-priority assessment is limited by source accessibility and the possibility of a more general theorem subsuming these exact calculations.

## References

1. G. Romero Moreno, V. Robu, and H. La Poutré, *Modelling the complex dynamics of online disinformation cascades*, arXiv:2610.13839v1 (public 9 October 2026), especially Sections 2.1, 3.2 and 3.3; https://arxiv.org/html/2610.13839v1.
2. J. Joo and J. L. Lebowitz, *Behavior of susceptible-infected-susceptible epidemics on heterogeneous networks with saturation*, arXiv:cond-mat/0402065 (2004); https://arxiv.org/abs/cond-mat/0402065.
3. C. V. Giuraniuc et al., *Criticality on networks with topology-dependent interactions*, Phys. Rev. E 74, 036108 (2006), arXiv:cond-mat/0603689; https://arxiv.org/abs/cond-mat/0603689.
4. R. Yang et al., *Epidemic spreading on heterogeneous networks with identical infectivity*, arXiv:physics/0609150 (2006); https://arxiv.org/abs/physics/0609150.
5. L. Hébert-Dufresne et al., *One pathogen does not an epidemic make: a review of interacting contagions, diseases, beliefs, and stories*, npj Complexity 2, 26 (2025), arXiv:2504.15053; https://www.nature.com/articles/s44260-025-00050-2.

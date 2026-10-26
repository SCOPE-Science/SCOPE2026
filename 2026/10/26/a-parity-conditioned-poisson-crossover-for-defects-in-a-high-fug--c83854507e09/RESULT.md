# A parity-conditioned Poisson crossover for defects in a high-fugacity hard-core ring

## Finding

Let \(C_n\), \(n\ge3\), be the cycle with vertices \(0,\ldots,n-1\), and let \(\eta_i\in\{0,1\}\) be distributed by the grand-canonical nearest-neighbor hard-core law
\[
 \mathbb P_{n,z}(\eta)=\frac{z^{\sum_i\eta_i}}{Z_n(z)}\mathbf1\{\eta_i\eta_{i+1}=0\text{ for all }i\},\qquad z>0,
\]
with indices modulo \(n\). An *empty-bond defect* is a bond \(i\) with \(\eta_i=\eta_{i+1}=0\). Set \(K_n=\sum_i\mathbf1\{\eta_i=\eta_{i+1}=0\}\) and the defect point measure \(\Xi_n=\sum_{i:\eta_i=\eta_{i+1}=0}\delta_{i/n}\) on the unit circle.

**Theorem (finite-size topological crossover).** Fix \(c\in(0,\infty)\), and suppose \(z_n/n^2\to c\). Along the even-size subsequence, \(\Xi_n\) converges in distribution to a homogeneous Poisson point process on the unit circle, of intensity
\[
 \lambda=\frac{1}{2\sqrt c},
\]
conditioned to contain an **even** number of points. Along the odd-size subsequence, the limit is the same Poisson process conditioned to contain an **odd** number of points. In particular, if \(p\in\{0,1\}\) denotes the eventual parity of \(n\), then for \(k\ge0\) with \(k\equiv p\pmod2\),
\[
 \lim\mathbb P(K_n=k)=\begin{cases}\lambda^k/(k!\cosh\lambda),&p=0,\\\lambda^k/(k!\sinh\lambda),&p=1,\end{cases}
\]
and all other counts have probability zero. Conditional on each fixed admissible positive count \(k\), the rescaled defect locations converge to \(k\) independent uniform points on the circle, considered without labels. The empty configuration of defects is allowed only for even \(n\).

**Macroscopic two-point consequence.** For any integer distances \(1\le d_n<n\) satisfying \(d_n/n\to x\in(0,1)\),
\[
 4(-1)^{d_n}\operatorname{Cov}(\eta_0,\eta_{d_n})\longrightarrow H_p(x),
\]
where
\[
 H_0(x)=\frac{e^{-2\lambda x}+e^{-2\lambda(1-x)}}{1+e^{-2\lambda}},\qquad
 H_1(x)=\frac{e^{-2\lambda x}-e^{-2\lambda(1-x)}}{1-e^{-2\lambda}}.
\]
The even-cycle profile is a symmetric sum of two exponentials; the odd-cycle profile is antisymmetric about half the circumference and records the unavoidable topological defect. Both are consequences of the *same* spatial point-process limit.

## Assumptions and scope

The model is an equilibrium hard-core lattice gas with uniform strictly positive activity, not an irreversible adsorption process. Each \(\eta_i\) is a binary occupation variable; adjacent occupations are forbidden. All limits are taken along a specified cycle parity, with \(n\to\infty\), \(z_n>0\), and \(z_n/n^2\to c\in(0,\infty)\). Convergence of \(\Xi_n\) is weak convergence of random finite point measures on the compact circle; no statistical independence of finite-size defect bonds is asserted. The Poisson limit refers to macroscopic positions after taking \(n\to\infty\).

## Proof

**1. Defect parity and allowed locations.** Every bond is either \(01\), \(10\), or \(00\), since \(11\) is forbidden. Writing \(S_i=2\eta_i-1\), a nondefect bond reverses the sign of \(S\), while a defect \(00\) preserves it. Going once around the ring gives \((-1)^{n-K_n}=1\), hence \(K_n\equiv n\pmod2\), and summing the occupied-to-empty transitions yields \(\sum_i\eta_i=(n-K_n)/2\). For \(k\ge1\), a set of distinct defect bonds \(0\le i_1<\cdots<i_k<n\) comes from precisely one allowed configuration if and only if each of its \(k\) successive cyclic gaps \(i_{j+1}-i_j\), with \(i_{k+1}=i_1+n\), is odd. Indeed, after each \(00\) bond the spins alternate until the next \(00\); odd inter-defect bond distance is necessary and sufficient to restore the value \(-1\) at the next defect. For \(k=0\), precisely two configurations exist when \(n\) is even, and none when \(n\) is odd.

**2. Exact defect-count enumerator.** Standard cyclic-gap counting gives, for \(k\equiv n\pmod2\) and \(0\le k\le n\),
\[
 a_{n,k}=\#\{\eta:K_n=k\}=\frac{2n}{n+k}\binom{(n+k)/2}{k}.
\]
To check this directly, set \(j=(n-k)/2\). For \(1\le j\le\lfloor n/2\rfloor\), cyclic independent sets with \(j\) occupied sites are enumerated by \(\frac{n}{j}\binom{n-j-1}{j-1}=\frac{n}{n-j}\binom{n-j}{j}\), which equals the displayed expression; the empty occupation and the even perfect alternating states cover the boundaries. Consequently,
\[
 \frac{Z_n(z_n)}{z_n^{n/2}}=\sum_{\substack{0\le k\le n\\ k\equiv n\;(2)}}a_{n,k}z_n^{-k/2}.
\]
For each fixed admissible \(k\), \(a_{n,k}/n^k\to 2^{1-k}/k!\). Moreover \(a_{n,k}\le 2n^k/k!\), and \(n/\sqrt{z_n}\) remains bounded. Thus dominated convergence applies to the full nonnegative series; the normalization tends to \(2\cosh\lambda\) on even sizes and \(2\sinh\lambda\) on odd sizes. Taking normalized coefficient ratios proves the displayed parity-projected Poisson count distribution and tightness of \(K_n\).

**3. Spatial convergence, not merely convergence of counts.** Fix \(k\ge1\) of the appropriate parity. Within strictly ordered defect locations \(0\le i_1<\cdots<i_k<n\), requiring the first \(k-1\) gaps to be odd forces their lattice parities to alternate. The closing gap is automatically odd because \(k\equiv n\pmod2\). Exactly two out of the \(2^k\) possible microscopic parity patterns are admitted. Each parity pattern becomes equidistributed in every fixed macroscopic box as the mesh tends to zero. Therefore, for any bounded continuous function \(F\) on the ordered simplex,
\[
 \frac1{n^k}\sum_{\substack{0\le i_1<\cdots<i_k<n\\\text{all cyclic gaps odd}}}F(i_1/n,\ldots,i_k/n)
 \longrightarrow 2^{1-k}\!\int_{0<x_1<\cdots<x_k<1}F(x_1,\ldots,x_k)\,dx_1\cdots dx_k.
\]
The diagonal and boundary strips have vanishing volume. Dividing by the corresponding asymptotic count shows that, conditional on \(K_n=k\), the positions tend to the order statistics of \(k\) independent uniforms. The preceding tightness then allows mixing over all \(k\), proving point-process convergence. For \(k=0\), the point measure is simply empty.

**4. Two-point law.** For any \(1\le d<n\), the bond characterization gives the exact identity
\[
 S_0S_d=(-1)^d(-1)^{\Xi_n([0,d/n))}.
\]
Also \(\sum_i S_i=-K_n\); rotation invariance and tightness imply \(\mathbb E S_i=-\mathbb EK_n/n\to0\). In a rate-\(\lambda\) Poisson process, the numbers of points in two complementary arcs of lengths \(x\) and \(1-x\) are independent. Conditioning the total count to be even gives
\[
 \mathbb E[(-1)^{N_x}\mid N_1\text{ even}]
 =\frac{e^{-2\lambda x}+e^{-2\lambda(1-x)}}{1+e^{-2\lambda}},
\]
while conditioning it to be odd changes the plus to a minus in both numerator and denominator. Since \(\eta_i=(1+S_i)/2\), the claimed covariance limits follow. The endpoints of a fixed macroscopic arc have zero probability of containing a limiting Poisson point, justifying passage to the counting functional.

**5. Why the activity scale is quadratic.** The exact transfer matrix \(T_z=\left(\begin{smallmatrix}1&z\\1&0\end{smallmatrix}\right)\) has eigenvalues \(r_\pm=(1\pm\sqrt{1+4z})/2\), so \(Z_n(z)=r_+^n+r_-^n\). The eigenvalue competition is controlled by \(n/\sqrt z\): when \(z\asymp n^2\), both modes contribute on the same scale and the two parity-conditioned limits persist. When \(z/n^2\to\infty\), the defect count concentrates on zero for even \(n\) and on one for odd \(n\), with the latter defect asymptotically uniform. Thus the quadratic scale is the finite-volume crossover between perfect alternation and a delocalized frustrated bond.

## Verification

The standalone `verify.py` enumerates every admissible configuration on cycles of sizes \(3\) through \(17\), compares its defect count with the independent closed combinatorial formula, and separately evaluates the grand partition function by integer transfer-matrix multiplication. It also checks the parity-conditioned count asymptotics at four larger sizes and checks exact two-point covariances against an independently derived finite-transfer expression by exhaustive enumeration on smaller rings. The current execution produced `PASS 297 independent exact and asymptotic checks`. The finite checks are consistency tests; the limit theorem rests on the proof above.

Run with `python verify.py` using Python's standard library only.

## Relationship to prior work

The hard-core cycle partition polynomial and its transfer eigenvalues are **known**, explicitly in Scott and Sokal's Example 3.3 (equations (3.23) and (3.25)); these are *not* claimed as new. The count asymptotics follow from those known coefficients and are included to normalize the spatial limit. The new assessed content is the finite-size **spatial** point-process convergence with parity projection, including the odd-cycle frustrated sector and the macroscopic covariance profiles at the quadratic activity scale. The spatial law requires microscopic cyclic-gap parity equidistribution, not simply evaluation of a scalar partition polynomial.

Denisov and Hänggi analyze domain statistics for a finite **free-boundary** ferromagnetic Ising chain, rather than defects in a periodic hard-core gas. The 1986 work of Tanaka, Morita, and Hiroike addresses one-dimensional lattice-gas correlation functions, but its full text could not be inspected; it is a residual priority risk, particularly for broad transfer-matrix correlation formulas. A general rare-defect or low-temperature Ising-chain theorem might imply the spatial crossover after a nontrivial reduction; no such dominating theorem was verified in the accessible checks. No claim of exhaustive priority is made.

## Limitations

The theorem concerns a single species, nearest-neighbor hard-core exclusion, a uniform grand-canonical fugacity, a one-dimensional ring, and the stated quadratic high-fugacity scaling. It does not cover mixtures, site disorder, nonequilibrium kinetics, correlation limits with microscopic separations, or dynamics of defects. All statements are analytic asymptotics with a self-review only; no independent scientific audit has been performed.

## References

1. A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, first arXiv version dated 2003-09-15, arXiv:cond-mat/0309352; J. Stat. Phys. 118 (2005), 1151–1261. See especially Example 3.3, equations (3.23)–(3.25). https://arxiv.org/abs/cond-mat/0309352
2. S. I. Denisov and P. Hänggi, *Domain statistics in a finite Ising chain*, Phys. Rev. E 71, 046137 (2005), DOI:10.1103/PhysRevE.71.046137. https://opus.bibliothek.uni-augsburg.de/opus4/files/52968/52968.pdf
3. K. Tanaka, T. Morita, and K. Hiroike, *Correlation functions of a one-dimensional lattice gas with interactions up to third-nearest neighbors*, Prog. Theor. Phys. Suppl. 87 (1986), 214–228, DOI:10.1143/PTPS.87.214. Full text was not accessible for this check.

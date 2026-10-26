# Reentrant cyclic heavy-ball stability and a reshuffling-induced mean-square explosion

## Finding
For the standard componentwise heavy-ball update on two scalar, centered, strictly convex quadratic losses, the exact stable learning-rate set of either *fixed* component order can consist of two separated intervals. Any nonzero curvature mismatch also splits the set of spectrally rate-optimal fixed-order learning rates into two bands. Yet independently reshuffling the order each epoch can have exponentially **growing expected squared error even when both frozen orders converge**. An exact rational example has a frozen-order spectral radius of \(1/2\) per two-gradient epoch for both orders, while every nonzero starting state under independent uniform epoch reshuffling satisfies \(\mathbb E\|Z_k\|_2^2\ge(49/2)^k\|Z_0\|_2^2\).

## Assumptions and scope
Fix \(a,b>0\), momentum \(0\le\beta<1\), and learning rate \(\eta>0\). Let the two losses be \(f_1(x)=a x^2/2\) and \(f_2(x)=b x^2/2\). At each inner step, for the selected component curvature \(c\in\{a,b\}\), perform
\[
x_{j+1}=x_j-\eta c x_j+\beta(x_j-x_{j-1}).
\]
The unreset momentum carries across epoch boundaries; \(Z_j=(x_j,x_{j-1})^{\mathsf T}\). An epoch contains exactly one gradient evaluation for each loss, in order \((a,b)\) or \((b,a)\). **Frozen order** means the same order is used in all epochs; **reshuffling** means that the two orders are sampled uniformly and independently for each epoch, independently of the current state. This is an exact-arithmetic analysis of the iterates, not a theorem about decreasing-step-size convergence, nonscalar Hessians, or noninterpolating component losses.

Write
\[
T_c=\begin{pmatrix}1+\beta-\eta c&-\beta\\1&0\end{pmatrix},\quad P=T_bT_a,\quad Q=T_aT_b,\quad
\tau(\eta)=1+\beta^2-(1+\beta)(a+b)\eta+ab\eta^2,
\]
and define the positive upper endpoint \(H=(1+\beta)(a+b)/(ab)\). "Frozen-order stability" means \(\rho(P)<1\), equivalently \(\rho(Q)<1\), so every deterministic starting state decays geometrically along the epoch subsequence.

## Proof
**1. Exact frozen-order frontier.** Matrix multiplication gives \(\operatorname{tr}P=\operatorname{tr}Q=\tau(\eta)\) and \(\det P=\det Q=\beta^2\). For \(0\le\beta<1\), the elementary degree-two Schur criterion gives strict unit-disc roots if and only if
\[
1+\beta^2-\tau(\eta)>0,\qquad 1+\beta^2+\tau(\eta)>0.
\]
The first inequality is exactly \(0<\eta<H\); the second is
\[
q(\eta):=ab\eta^2-(1+\beta)(a+b)\eta+2(1+\beta^2)>0.
\]
Put \(\delta=|a-b|/(a+b)\). The discriminant of \(q\) is
\[
\Delta=(a+b)^2\bigl[2(1+\beta^2)\delta^2-(1-\beta)^2\bigr].
\]
If \(\Delta<0\), the whole interval \((0,H)\) is stable. If \(\Delta=0\), exactly its midpoint \(H/2\) is excluded (a multiplier is \(-1\)). If \(\Delta>0\), define
\[
\eta_\pm=\frac{(1+\beta)(a+b)\pm\sqrt{\Delta}}{2ab}.
\]
Then the stable set is exactly \((0,\eta_-)\cup(\eta_+,H)\). Indeed \(0<\eta_-<\eta_+<H\), since their sum is \(H\), their product is \(2(1+\beta^2)/(ab)>0\), and \(q(H)=2(1+\beta^2)>0\). Thus the stable set disconnects precisely when
\[
\delta>\frac{1-\beta}{\sqrt{2(1+\beta^2)}}.
\]
Equality gives an isolated neutral point, not an open unstable interval.

**2. Exact fastest-rate bands.** Assume \(0<\beta<1\). The determinant bound forces \(\rho(P)\ge\beta\); equality holds exactly when both eigenvalues have modulus \(\beta\), equivalent to \(|\tau(\eta)|\le2\beta\). For \(a<b\), define
\[
L=\frac{(1+\beta)(a+b)-\sqrt{(1+\beta)^2(a+b)^2-4ab(1-\beta)^2}}{2ab},
\quad
R=\frac{(1+\beta)(a+b)+\sqrt{(1+\beta)^2(a+b)^2-4ab(1-\beta)^2}}{2ab}.
\]
The two roots of \(\tau=-2\beta\) are exactly \((1+\beta)/b\) and \((1+\beta)/a\); the two roots of \(\tau=2\beta\) are \(L\) and \(R\). Their strict ordering is
\[
0<L<\frac{1+\beta}{b}<\frac{1+\beta}{a}<R<H.
\]
Hence the complete set of learning rates attaining the smallest possible fixed-order asymptotic factor \(\beta\) is
\[
\left[L,\frac{1+\beta}{b}\right]\ \cup\ \left[\frac{1+\beta}{a},R\right].
\]
At endpoints with repeated eigenvalues, the spectral factor remains \(\beta\), although matrix powers may include a polynomial prefactor. Thus disconnected optimal-rate bands occur for *every* unequal-curvature pair, even below the threshold at which the stability region itself disconnects. If \(a=b\), the two inner endpoints coincide and the optimal-rate set is one interval. The case \(\beta=0\) is intentionally excluded from this optimal-band assertion.

**3. Exact opposite behavior under fresh reshuffling.** Set \(a=1\), \(b=10\), \(\beta=1/2\), and \(\eta=31/20\). Direct multiplication gives
\[
P=\begin{pmatrix}1/5&7\\-1/20&-1/2\end{pmatrix},\qquad
Q=\begin{pmatrix}1/5&1/40\\-14&-1/2\end{pmatrix}.
\]
Both have trace \(-3/10\) and determinant \(1/4\), hence the two simple eigenvalues \((-3\pm i\sqrt{91})/20\), each of modulus \(1/2\). The two fixed-order iterations therefore converge geometrically for every initial two-state vector.

For independent equiprobable reshuffling, conditioned on any current epoch state \(Z\),
\[
\mathbb E[\|Z_{\rm next}\|_2^2\mid Z]=Z^{\mathsf T}KZ,\quad
K=\frac{P^{\mathsf T}P+Q^{\mathsf T}Q}{2}
=\begin{pmatrix}78433/800&843/200\\843/200&79201/3200\end{pmatrix}.
\]
The symmetric matrix \(K-(49/2)I\) has first diagonal entry \(58833/800>0\) and determinant \(1643697/2560000>0\), so it is positive definite. Thus \(\mathbb E[\|Z_{\rm next}\|_2^2\mid Z]\ge(49/2)\|Z\|_2^2\). Iterated conditional expectation yields
\[
\mathbb E\|Z_k\|_2^2\ge(49/2)^k\|Z_0\|_2^2
\]
for every deterministic \(Z_0\ne0\) and integer \(k\ge0\). This proves mean-square divergence and makes no assertion about almost-sure divergence of individual reshuffled trajectories.

## Verification
Run `python3 verify.py` using the accompanying standalone standard-library file. It reconstructs the actual two step matrices in exact rational arithmetic, their trace, determinant, characteristic discriminant, the positive-definite mean-square certificate, and 1536 additional rational parameter identities. The expected output starts `VERIFY_OK`. The Schur, interval, and conditional-expectation arguments above establish the universal assertions analytically; finite tests alone are not offered as infinite proofs.

## Relationship to prior work
Qiu and Milzarek, arXiv:2404.18452 (first posted 2024-04-29; subsequently revised with Ma), introduce and analyze random reshuffling with per-component heavy-ball momentum, including the update analyzed here in its scalar, two-sample, no-Nesterov specialization. Their results address complexity and convergence under step-size controls; the sharp two-component constant-step stability and random-vs-frozen separation here are not asserted there. Wu, Yun, and Sra, arXiv:2302.12444, exhibit a separation between single-shuffle and epoch-reshuffling SGD **with batch normalization** in the opposite stability direction; their normalization-dependent model has no heavy-ball mechanism and does not imply the present rational witness. Chen and Bruna (PMLR 202:4330–4391, 2023) analyze nonconvex single-objective two-step gradient dynamics beyond the edge of stability, not fresh permutation switching of two component Hessians with momentum. Tran, Nguyen, and Tran-Dinh (ICML 2021) introduce a distinct shuffling-momentum-gradient scheme whose momentum state is not the per-inner-update heavy-ball recurrence here. This is a best-knowledge statement comparison, not a claim of exhaustive historical priority.

## Limitations
The phenomenon depends on momentum, curvature heterogeneity, the specified constant step size, and the distinction between a frozen and an independently redrawn epoch permutation. Frozen-order spectral stability alone does not imply arbitrary-switching stability. The theorem does not prove almost-sure divergence, instability for every parameter outside the special witness, or analogous effects for distinct component minimizers, batch normalization, Nesterov momentum, nonquadratic losses, or multidimensional state spaces. The four-source comparison and database search cannot exclude an unlocated periodic-matrix or stochastic-heavy-ball formulation; independent novelty and proof review have not been performed.

## References
1. J. Qiu and A. Milzarek, *Random Reshuffling with Momentum for Nonconvex Problems: Iteration Complexity and Last Iterate Convergence*, arXiv:2404.18452, first public version 2024-04-29; subsequent manuscript *Random Reshuffling with Momentum: Complexity Bounds and Last-iterate Convergence* (with B. Ma), https://arxiv.org/abs/2404.18452.
2. D. X. Wu, C. Yun, and S. Sra, *On the Training Instability of Shuffling SGD with Batch Normalization*, arXiv:2302.12444, https://arxiv.org/abs/2302.12444.
3. L. Chen and J. Bruna, *Beyond the Edge of Stability via Two-step Gradient Updates*, Proceedings of Machine Learning Research 202 (2023), 4330–4391, https://proceedings.mlr.press/v202/chen23b.html.
4. T. H. Tran, L. M. Nguyen, and Q. Tran-Dinh, *SMG: A Shuffling Gradient-Based Method with Momentum*, Proceedings of Machine Learning Research 139 (2021), 10379–10389, https://proceedings.mlr.press/v139/tran21b.html.

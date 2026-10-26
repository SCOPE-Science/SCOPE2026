# Exact two-mode volatility clustering in a noncommuting open quantum walk

## Finding
For the one-dimensional noncommuting open quantum random walk (OQRW) of Dhahri, Ko, Mukhamedov and Yoo, Example 3.10 [1], the signed displacement process is a martingale with pairwise uncorrelated increments, but the **squared step lengths have strictly positive, exactly two-mode memory**. With stationary internal initialization, writing \(S_j=(X_j-X_{j-1})^2\), for every integer \(j\ge1\) and \(\ell\ge1\),
\[
\operatorname{Cov}(S_j,S_{j+\ell})=\frac{25}{32}\left(\frac34\right)^{\ell-1}+\frac9{32}\vartheta^{\ell-1},\qquad \vartheta=\frac14+\frac1{2\sqrt2}.
\]
For accumulated squared jump lengths \(Q_n=\sum_{j=1}^n S_j\) and every integer \(n\ge1\),
\[
\operatorname{Var}(Q_n)=\frac{43n}{16}+\frac{25}{16}G_n\left(\frac34\right)+\frac9{16}G_n(\vartheta),\quad G_n(u)=\frac{(n-1)-nu+u^n}{(1-u)^2}.
\]
Thus the precise asymptotic variance per step is
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(Q_n)}n=\frac{43}{16}+\frac{25}{16(1-3/4)}+\frac9{16(1-\vartheta)}=10.3563543593342\ldots.
\]
The same one-step jump distribution but independent successive jumps would have asymptotic quadratic-variation variance \(43/16=2.6875\) per step: **the actual fluctuations are \(3.85352720347\ldots\) times larger in variance**, despite vanishing correlations between signed steps. The two decay factors are distinct and both coefficients are strictly positive.

A companion exact finite-time transport identity holds for any initial internal qubit state \(\rho_0=(I+x\sigma_x+y\sigma_y+z\sigma_z)/2\), with \(x^2+y^2+z^2\le1\):
\[
\mathbb E_{\rho_0}X_n=0,\qquad \operatorname{Var}_{\rho_0}(X_n)=\frac54 n+\frac58(x+z)U_n(3/4)+\frac38(x-z)U_n(\vartheta),
\]
where \(U_n(u)=(1-u^n)/(1-u)\). In particular, the sharp state-uniform interval is \(\frac54n-A_n\le \operatorname{Var}_{\rho_0}(X_n)\le\frac54n+A_n\), where
\[
A_n=\frac1{\sqrt2}\sqrt{\left(\frac54 U_n(3/4)\right)^2+\left(\frac34 U_n(\vartheta)\right)^2},
\]
and both bounds are attained by opposite pure initial qubit states.

## Assumptions and scope
Let \(\mathcal H=\mathbb C^2\) and \(P=\left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)\), \(Q=\frac12\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\), \(H=(I-(P+Q)/2)^{1/2}\), where the square root is the unique positive one. Associate five jump-labelled Kraus operators to increments \(s\in\{-2,-1,0,1,2\}\): \(L_{\pm1}=P/2\), \(L_{\pm2}=Q/2\), \(L_0=H\). Their completeness relation is \(\sum_s L_s^\dagger L_s=I\). In each step, the observed jump \(s\) occurs with probability \(\operatorname{Tr}(L_s\rho L_s^\dagger)\), and conditional internal state is \(L_s\rho L_s^\dagger\) divided by this probability (for nonzero probability). Starting position is zero. For squared-step stationarity and the correlation and \(Q_n\) formulas, the initial internal density is \(\rho_\infty=I/2\); the formula for \(X_n\) and its sharp envelope permits arbitrary normalized qubit states. Discrete-time observation is after every full instrument step, not merely final-position measurement. The outcome process is neither asserted independent nor Markov by itself.

## Proof
**Channel decomposition.** Define \(\Phi(Z)=\sum_s L_s Z L_s^\dagger\), which is trace preserving and unital. The invariant internal state is \(I/2\). For Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\), direct multiplication using \(H^2=I-(P+Q)/2\) gives
\[
\Phi(\sigma_x+\sigma_z)=\tfrac34(\sigma_x+\sigma_z),\quad\Phi(\sigma_x-\sigma_z)=\vartheta(\sigma_x-\sigma_z),\quad \Phi(\sigma_y)=\tfrac1{2\sqrt2}\sigma_y.
\]
These identities can also be obtained from \(H=cI+d(\sigma_x+\sigma_z)\) with \(c>0\) and \(d<0\), \(H^2\) as prescribed, and the fact that \(P,Q\) are rank-one projections; no asymptotic or independence assertion is used here.

**Signed steps.** Because \(L_{-s}=L_s\), for every normalized conditioned state and history the conditional mean of the next signed increment is zero. Therefore \(X_n=\sum_{j=1}^n\xi_j\) is a martingale and \(\mathbb E(\xi_i\xi_j)=0\) for \(i<j\). Its predictable second moment operator is
\[
M:=\sum_s s^2 L_s^\dagger L_s=\tfrac12 P+2Q=\tfrac54 I+\sigma_x+\tfrac14\sigma_z.
\]
Thus \(\mathbb E\xi_j^2=\operatorname{Tr}[M\Phi^{j-1}(\rho_0)]\). Resolve \(\rho_0\) along the two displayed eigendirections and sum the finite geometric series. This gives exactly the stated formula for \(\operatorname{Var} X_n\). The state-dependent correction is a Euclidean linear functional of \((x,z)\); maximizing its magnitude over the unit Bloch disk gives \(A_n\), with equality at the unique aligned antipodal pure states. Explicitly, set \(\alpha=\frac54U_n(3/4)\), \(\beta=\frac34U_n(\vartheta)\), and take \((x,y,z)=\pm((\alpha+\beta),(0),(\alpha-\beta))/(\sqrt{2(\alpha^2+\beta^2)})\).

**Squared-step correlations.** Write \(\Phi_2(Z)=\sum_s s^2 L_s ZL_s^\dagger=\frac12PZP+2QZQ\). The stationary one-step mean is \(\mathbb E S_j=\operatorname{Tr}(M I/2)=5/4\); the fourth signed moment is \(\mathbb E\xi_j^4=\operatorname{Tr}[(\frac12 P+8Q)I/2]=17/4\), giving \(\operatorname{Var}(S_j)=43/16\). Direct evaluation yields
\[
\Phi_2(I/2)=\frac54\frac I2+\frac5{16}(\sigma_x+\sigma_z)+\frac3{16}(\sigma_x-\sigma_z).
\]
For any \(\ell\ge1\), the quantum instrument's joint moments are exactly
\[
\mathbb E(S_j S_{j+\ell})=\operatorname{Tr}\bigl[M\Phi^{\ell-1}\Phi_2(I/2)\bigr].
\]
Since \(\operatorname{Tr}[M(\sigma_x+\sigma_z)]=5/2\) and \(\operatorname{Tr}[M(\sigma_x-\sigma_z)]=3/2\), removing \((5/4)^2\) gives \(\operatorname{Cov}=25(3/4)^{\ell-1}/32+9\vartheta^{\ell-1}/32\). The channel identity ensures time-stationarity of all the displayed joint moments, despite outcome dependence.

**Quadratic-variation variance.** Expand \(\operatorname{Var}(\sum_{j=1}^n S_j)\) as \(n\operatorname{Var}(S_1)+2\sum_{\ell=1}^{n-1}(n-\ell)\operatorname{Cov}(S_1,S_{1+\ell})\). The exact geometric convolution is \(\sum_{\ell=1}^{n-1}(n-\ell)u^{\ell-1}=G_n(u)\) for \(0\le u<1\), giving the claimed finite formula. Finally \(G_n(u)/n\to(1-u)^{-1}\); substituting \(u=3/4,\vartheta\) proves the exact limiting constant. All formulas include \(n=1\) and \(\ell=1\). The variance-inflation ratio is the exact limiting constant divided by \(43/16\).

## Verification
Run `python verify.py` with NumPy and SciPy installed. The independent numerical evaluation builds \(H\) using the matrix square root, checks channel eigendirections, enumerates all \(5^n\) labelled instrument histories for \(1\le n\le6\) for five admissible initial states, reproduces signed displacement mean/variance and stationary quadratic-variation variance, checks 29 delayed squared-step covariance values, and checks 50 sharp-state-envelope cases. These finite checks support the explicit identities, not the proofs for all integers; the preceding algebra and geometric sums establish their unrestricted ranges.

## Relationship to prior work
Dhahri, Ko, Mukhamedov and Yoo [1], Example 3.10, define exactly this noncommuting Kraus family, establish its primitive stationary channel, note that individual output jumps are not independent, prove centered Gaussian spreading with variance coefficient \(5/4\), and give recurrence and potential-kernel conclusions. In contrast, our specific claim concerns **the full, two-mode, all-lag autocovariance of squared output steps**, an exact finite-horizon quadratic-variation variance, its limiting inflation versus independent increments, and the sharp arbitrary-initial-state finite-time transport envelope. Those statistics are not stated in the inspected source's Example 3.10, limiting theorems, conclusions or appendices. General bounds on output fluctuations of quantum Markov processes are developed by Girotti, Garrahan and Guţă [2], but their generic concentration statements do not determine these two exact decay rates and constants for this particular instrument. All underlying instrument operators, trace formalism, and general methods are prior knowledge. An independently unknown published specialization could still cover the formula; this comparison establishes best-knowledge originality, not literature-wide priority.

## Limitations
The autocovariance and quadratic-variation statements require stationary internal preparation \(I/2\), and concern observed squared step lengths, not the variance of a freely coherent unitary quantum walk. The finite-horizon displacement variance formula admits any initial qubit, but no general arbitrary-initial-state quadratic-variation covariance formula is claimed. The model has a fixed five-outcome instrument in one spatial dimension; no claim is made for arbitrary Kraus operators, time-dependent environments, detector coarse-graining or observation noise. Computation checks finitely many cases only. No independent external scientific review or formal certification has been conducted.

## References
[1] A. Dhahri, C. K. Ko, F. Mukhamedov, H. J. Yoo, *Ballistic Speed and Potential-Theoretic Recurrence for Homogeneous Open Quantum Random Walks*, arXiv:2610.01844v1, publicly posted 2026-10-01, especially Section 3.2, Example 3.10. https://arxiv.org/html/2610.01844v1

[2] F. Girotti, J. P. Garrahan, M. Guţă, *Concentration Inequalities for Output Statistics of Quantum Markov Processes*, Annales Henri Poincaré **24** (2023), 2799–2832, arXiv:2206.14223; https://doi.org/10.1007/s00023-023-01286-1

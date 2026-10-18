# A sharp one-epoch reshuffling reversal on strongly convex quadratics

## Finding
For every \(0<b,p<1\), define \(P=\operatorname{diag}(0,b)\), \(Q=\frac p2\begin{pmatrix}1&1\\1&1\end{pmatrix}\), \(H_1=I-P\), \(H_2=I-Q\), \(f_i(x)=\frac12x^\top H_i x\), and \(f=(f_1+f_2)/2\). From \(x_0=(1,0)^\top\), apply two unit-stepsize component-gradient updates, either using a uniformly random permutation of both components (RR) or two independent uniform choices with replacement (IID). Then
\[
\mathbb E_{\mathrm{RR}}f(x_2)-\mathbb E_{\mathrm{IID}}f(x_2)
=\frac{p^2}{128}\bigl(-2b^3-b^2p+4b^2+2bp^2+4p^3-8p^2\bigr).
\]
The displayed cubic is strictly increasing in \(b\in[0,1]\), has a negative value at \(b=0\), and changes sign inside \((0,1)\) precisely for \(0<p<p_*\), where \(p_*\in(0,1)\) is the unique zero of \(4p^3-6p^2-p+2\). Consequently there is a unique sharp parameter boundary \(b_*(p)\in(0,1)\) for such \(p\): RR has *higher* expected objective error exactly when \(b>b_*(p)\). For \(p\ge p_*\), RR is strictly better for all \(0<b<1\). At \(p=1/2\), the gap is \((4b-3)(1+b-b^2)/1024\), and RR is worse exactly when \(b>3/4\). The RR-to-IID expected objective ratio is always less than \(2\) in this family and approaches \(2\) as \(b\uparrow1\), \(p\downarrow0\).

## Assumptions and scope
All computations use real exact arithmetic. Both component Hessians are positive definite, with eigenvalues \(\{1,1-b\}\) and \(\{1,1-p\}\); each component has gradient Lipschitz constant \(L=1\), so stepsize \(\eta=1=1/L\) is within its standard nonexpansive gradient range. The common minimizer is \(0\). The two sampling schemes each consume two component-gradient evaluations. Statements compare *one-epoch, pointwise, expected objective gaps*, not asymptotic or worst-case convergence rates.

## Proof
Let \(u=(1,0)^\top\). One gradient step for component 1 or 2 multiplies the current iterate by \(P\) or \(Q\), respectively. Since \(Pu=0\), the four ordered IID outcomes \(P^2u\), \(QPu\), \(PQu\), \(Q^2u\) reduce to two zero vectors and the two nonzero vectors \(PQu=(0,bp/2)^\top\) and \(Q^2u=(p^2/2,p^2/2)^\top\). RR uses only \(PQu\) and \(QPu=0\). Put \(H=(H_1+H_2)/2=I-(P+Q)/2\) and \(F(v)=v^\top Hv/2\). Direct enumeration therefore gives
\[
\mathbb E_{\mathrm{RR}} F(x_2)=\tfrac12F(PQu),\qquad
\mathbb E_{\mathrm{IID}}F(x_2)=\tfrac14F(PQu)+\tfrac14F(Q^2u).
\]
Since \(H_{22}=1-b/2-p/4\), substitution yields
\[
\mathbb E_{\mathrm{RR}}F(x_2)=\frac{b^2p^2(4-2b-p)}{64},\qquad
\mathbb E_{\mathrm{IID}}F(x_2)=\frac{p^2(-2b^3-b^2p+4b^2-2bp^2-4p^3+8p^2)}{128}.
\]
Subtracting gives the stated polynomial. Define \(T_p(b)=-2b^3-b^2p+4b^2+2bp^2+4p^3-8p^2\). Then \(T_p'(b)=-6b^2+(8-2p)b+2p^2\). This quadratic is concave as a function of \(b\), so its minimum on \([0,1]\) is attained at an endpoint; these values are \(2p^2>0\) and \(2(1-p+p^2)>0\). Thus \(T_p\) increases strictly. Moreover \(T_p(0)=4p^2(p-2)<0\), while \(T_p(1)=4p^3-6p^2-p+2\). The last polynomial has derivative \(12p^2-12p-1<0\) on \([0,1]\) and changes sign from \(2\) to \(-1\), proving uniqueness of \(p_*\) and all phase claims. At \(p=1/2\), factor \(T_{1/2}(b)\) to obtain the displayed threshold. Finally positivity of \(H\) implies \(F(Q^2u)>0\), and the enumerated expectations give
\[
\frac{\mathbb E_{\mathrm{RR}} F(x_2)}{\mathbb E_{\mathrm{IID}} F(x_2)}=\frac{2F(PQu)}{F(PQu)+F(Q^2u)}<2.
\]
As \(p\downarrow0\) with \(b\uparrow1\), the first term is of order \(p^2\) and the second is of order \(p^4\), so the ratio tends to \(2\). This proves all assertions.

## Verification
The standalone file `verify_reshuffling.py` independently enumerates both RR permutations and all four IID choices using exact rational matrix arithmetic for 3,795 rational parameter pairs, including the sharp \(b=3/4\) equality case. It also checks the Euclidean-error formula as a separate cross-check. The unlimited-domain conclusion follows from the written algebra, not from finite tests.

## Relationship to prior work
Das, Schölkopf, and Muehlebach (2022) study stronger asymptotic rate advantages for sampling without replacement in finite-sum minimax algorithms, and compare random reshuffling with independent sampling. Koloskova and collaborators (2024) establish convergence-rate bounds for shuffled and incremental methods. Liu (2026) develops finite-epoch convergence-rate guarantees with favorable RR bounds. These comparisons are bounds on algorithms under their own conditions; none of the inspected accessible statements asserts a *pointwise, all-instances, exact first-epoch objective inequality at stepsize \(1/L\)*. The claim here is a sharp finite-instance boundary, not a challenge to any established upper bound.

## Limitations
This is a two-dimensional, two-component interpolation family and compares the expected objective only after two updates at a fixed stepsize. No universal claim about RR versus IID, arbitrary objectives, asymptotic convergence, or optimizer-independent performance is made. A recent source has a strong headline about RR dominance, but its full original manuscript could not be accessed in this run; its exact theorem conditions remain a residual originality risk. The exact one-epoch formula does not determine later-epoch ordering or optimal step-size tuning.

## References
1. A. Das, B. Schölkopf, and M. Muehlebach, *Sampling without Replacement Leads to Faster Rates in Finite-Sum Minimax Optimization* (2022), arXiv:2206.02953 (first public June 7, 2022), https://arxiv.org/abs/2206.02953.
2. A. Koloskova, N. Doikov, S. U. Stich, and M. Jaggi, *On Convergence of Incremental Gradient for Non-Convex Smooth Functions* (2024), arXiv:2305.19259, https://arxiv.org/abs/2305.19259.
3. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent* (2026), PMLR 336, https://proceedings.mlr.press/v336/liu26d.html (abstract and publication page consulted; full original PDF not accessible).

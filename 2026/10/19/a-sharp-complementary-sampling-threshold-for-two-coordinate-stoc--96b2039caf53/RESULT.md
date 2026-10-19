# A sharp complementary-sampling threshold for two-coordinate stochastic extragradient

## Finding
For unbiased *single-scalar-coordinate* extragradient on the simplest bilinear saddle, mean-square convergence depends sharply on **how the first and second oracle coordinates are paired**, even though each oracle call separately has the same uniform coordinate law.

Write \(r=\Pr(j\ne i)\) for the probability of complementary sampling and \(\eta\) for the constant stepsize. The exact squared-error factor is
\[
q_r(\eta)=1+(2-4r)\eta^2+8r\eta^4.
\]
For every nonzero deterministic initialization, the iterates converge in mean square if and only if
\[
r>\tfrac12,\qquad 0<\eta<\sqrt{\frac{2r-1}{4r}}.
\]
Independent stage coordinates have \(r=1/2\) and diverge in mean square for *every* positive constant step, whereas complementary pairing \(r=1\) gives contraction throughout \(0<\eta<1/2\). The independent-stage mean iterate nevertheless converges to the saddle for \(0<\eta<1\), revealing a strict separation between mean and mean-square behavior.

## Assumptions and scope
Consider the unconstrained zero-sum game \(\min_{x\in\mathbb R}\max_{y\in\mathbb R}xy\), with unique equilibrium \(z_*=0\). Set
\[
z=(x,y)^{\mathsf T},\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad F(z)=Jz.
\]
Let \(P_1=\operatorname{diag}(1,0)\), \(P_2=\operatorname{diag}(0,1)\). Each coordinate oracle is \(G_i(z)=2P_iJz\); uniformly sampled \(i\) gives \(\mathbb E_i G_i(z)=Jz\). Fix \(r\in[0,1]\) and \(\eta\ge0\). Each iteration draws a pair \((i,j)\in\{1,2\}^2\) with
\[
\Pr(i=j=1)=\Pr(i=j=2)=\frac{1-r}{2},\qquad
\Pr(i=1,j=2)=\Pr(i=2,j=1)=\frac r2.
\]
Pairs are independent and identically distributed across iterations and independent of the initial state. Both stage indices are marginally uniform. The *same pair* is used in the two-stage update
\[
z_{k+1/2}=z_k-\eta G_i(z_k),\qquad
z_{k+1}=z_k-\eta G_j(z_{k+1/2}).
\]
Only one scalar coordinate of \(F\) is queried per stage. No projection, regularization, averaging, diminishing stepsizes, or additive oracle noise is included. All statements below hold for every integer \(k\ge0\) and every deterministic initial vector \(z_0\in\mathbb R^2\).

## Proof
Define \(A_i=2P_iJ\), so that each update is multiplication by
\[
T_{ij}=I-\eta A_j+\eta^2A_jA_i.
\]
Write \(h=\eta\). The complete four possible matrices, ordered by the **predictor** index \(i\) then the **corrector** index \(j\), are
\[
\begin{aligned}
T_{11}&=\begin{pmatrix}1&-2h\\0&1\end{pmatrix},&
T_{22}&=\begin{pmatrix}1&0\\2h&1\end{pmatrix},\\
T_{12}&=\begin{pmatrix}1&0\\2h&1-4h^2\end{pmatrix},&
T_{21}&=\begin{pmatrix}1-4h^2&-2h\\0&1\end{pmatrix}.
\end{aligned}
\]
Direct multiplication gives the two symmetry-paired Gram identities
\[
\frac{T_{11}^{\mathsf T}T_{11}+T_{22}^{\mathsf T}T_{22}}2
 =(1+2h^2)I,
\]
\[
\frac{T_{12}^{\mathsf T}T_{12}+T_{21}^{\mathsf T}T_{21}}2
 =(1-2h^2+8h^4)I.
\]
Averaging with the specified pair law therefore yields the exact matrix identity
\[
\mathbb E[T_{ij}^{\mathsf T}T_{ij}]
 =\big[(1-r)(1+2h^2)+r(1-2h^2+8h^4)\big]I
 =q_r(h)I.
\]
Conditioning on the past and using the independence of successive pairs,
\[
\mathbb E[\|z_{k+1}\|_2^2\mid z_k]=q_r(h)\|z_k\|_2^2.
\]
Iterated expectation proves \(\mathbb E\|z_k\|_2^2=q_r(h)^k\|z_0\|_2^2\) without a distributional or asymptotic approximation. For \(h>0\),
\[
q_r(h)-1=2h^2(1-2r+4rh^2).
\]
For \(r\le1/2\) this is strictly positive. For \(r>1/2\) it is strictly negative exactly when \(h^2<(2r-1)/(4r)\), zero at the positive endpoint, and positive above. Thus the stated mean-square trichotomy is necessary and sufficient for nonzero starts. At \(h=0\) the iterate is fixed.

For the mean, explicitly average the four transition matrices to obtain
\[
\mathbb E[T_{ij}]=(1-2rh^2)I-hJ=:B_r(h).
\]
Since the stage pairs are independent over time, \(\mathbb E z_k=B_r(h)^kz_0\) exactly. Since \(J^{\mathsf T}=-J\) and \(J^2=-I\),
\[
B_r(h)^{\mathsf T}B_r(h)
 =\big[(1-2rh^2)^2+h^2\big]I.
\]
At independent stage sampling \(r=1/2\), this squared mean factor is \(1-h^2+h^4<1\) precisely for \(0<h<1\), although \(q_{1/2}(h)=1+4h^4>1\) for all \(h>0\). With opposite-coordinate pairing \(r=1\), the mean-square factor is \(1-2h^2+8h^4<1\) precisely for \(0<h<1/2\). This completes all assertions.

## Verification
The supplied standalone `check_pair.py` constructs all four matrices with exact rational arithmetic, enumerates the full \(2\times2\) Gram products for 4,864 rational \((r,\eta)\) combinations, and checks both expected transition identities. Run `python3 check_pair.py` using the Python standard library. The program also reports exact factors at selected boundary cases; in particular \(r=1/2\), \(\eta=1/2\) yields mean-square factor \(5/4\) versus squared-mean factor \(13/16\), while \(r=1\), \(\eta=1/2\) gives the exact mean-square boundary factor \(1\).

These finite checks test the formulas but **do not constitute the proof for all real parameters**; that proof is the explicit four-matrix identity above.

## Relationship to prior work
Beznosikov et al. introduced a coordinate extragradient method in Algorithm 4 and Appendix A.4 of [1]. Its predictor evaluates the full operator \(F(w)\), and its corrector uses a variance-reduced *single-coordinate difference plus the full reference operator*. The present two-stage update instead draws one unbiased scalar coordinate in **each** stage, coupled with a controllable conditional law; its exact mean-square behavior cannot be obtained by substituting parameters into [1].

Gorbunov et al. [2] analyzed independent- and same-sample stochastic extragradient, including arbitrary sampling assumptions. Their independent-sample results provide general conditions and bounds, rather than the exact stage-coupling threshold for rank-one coordinate oracles on a pure skew saddle. Chavdarova et al. [3, Theorem 1 and Appendix C.1] already proved that stochastic extragradient can diverge in bilinear games. In their construction each sampled component updates the *matched two-player coordinates together*, so the important predictor/corrector overlap is \(I\cap J\). Here one sampled component updates **one player's coordinate only**, so the useful feedback instead requires the two sampled player coordinates to differ. The independent-sampling divergence *by itself* is therefore not claimed as new. Emmanouilidis et al. [4] studied random reshuffling of sampled components **across successive extragradient steps**, using the same component for the predictor and corrector within an individual step; this is not a coupled pair of different scalar-coordinate oracles within one step. General bilinearly coupled stochastic saddle methods [5] address a broader stochastic oracle setting but do not supply this exact single-coordinate pair law.

The distinguishing claim is the complete necessary-and-sufficient complementary-pairing threshold with an exact fourth-degree mean-square factor and simultaneous mean/moment separation, not a generic statement that stochastic extragradient may diverge.

## Limitations
This is an exactly solvable two-dimensional homogeneous bilinear model with uniform coordinate marginals, i.i.d. balanced pair laws, and a fixed shared stepsize. It does not establish a convergence theorem for higher-dimensional games, strongly monotone regularizations, unbalanced marginal sampling, almost-sure trajectories, random reshuffling across steps, or additive oracle noise. The formula specifies a moment criterion, not pathwise convergence or sample complexity for arbitrary stochastic variational inequalities.

## References
[1] A. Beznosikov, A. Gasnikov, K. Zainulina, A. Maslovskiy, and D. Pasechnyuk, *A Unified Analysis of Variational Inequality Methods: Variance Reduction, Sampling, Quantization and Coordinate Descent* (first public arXiv version 28 January 2022), arXiv:2201.12206, Algorithm 4 and Appendix A.4, https://arxiv.org/abs/2201.12206.

[2] E. Gorbunov, H. Berard, G. Gidel, and N. Loizou, *Stochastic Extragradient: General Analysis and Improved Rates* (first public 16 November 2021), arXiv:2111.08611, Sections 3--4 and Appendix F, https://arxiv.org/abs/2111.08611.

[3] T. Chavdarova, G. Gidel, F. Fleuret, and S. Lacoste-Julien, *Reducing Noise in GAN Training with Variance Reduced Extragradient* (first public 18 April 2019), arXiv:1904.08598, Theorem 1 and Appendix C.1, https://arxiv.org/abs/1904.08598.

[4] K. Emmanouilidis, R. Vidal, and N. Loizou, *Stochastic Extragradient with Random Reshuffling: Improved Convergence for Variational Inequalities* (first public 11 March 2024), arXiv:2403.07148, Algorithms 1--3, https://arxiv.org/abs/2403.07148.

[5] S. S. Du, G. Gidel, M. I. Jordan, and C. J. Li, *Optimal Extragradient-Based Bilinearly-Coupled Saddle-Point Optimization* (first public 17 June 2022), arXiv:2206.08573, https://arxiv.org/abs/2206.08573.

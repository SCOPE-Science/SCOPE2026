# A near-disconnected Sinkhorn crossover with a Riccati flux profile

## Finding
Consider two-atom Sinkhorn scaling with the symmetric positive kernel
\[
K_\delta=\begin{pmatrix}1&\delta\\\delta&1\end{pmatrix},\qquad 0<\delta<1,
\]
row masses \(r=(a,1-a)\), column masses \(c=(b,1-b)\), and \(a,b\in(0,1)\). One *complete sweep* updates \(u=r/(K_\delta v)\) and then \(v^+=c/(K_\delta^{\mathsf T}u)\), componentwise. Normalize the column scaling by its positive ratio \(x=v_1/v_2\). Every sweep obeys the exact fractional-linear map
\[
 x^+=F_\delta(x)=\frac{b}{1-b}\,
 \frac{(1-a+a\delta^2)x+\delta}{\delta x+a+(1-a)\delta^2}.
\]
Define \(A=1-a+a\delta^2\), \(C=a+(1-a)\delta^2\), \(B=b/(1-b)\), \(S=BA+C\), \(D=\sqrt{(BA-C)^2+4B\delta^2}\), and
\[
z_\pm=\frac{BA-C\pm D}{2\delta},\qquad q_\delta=\frac{S-D}{S+D}.
\]
For all parameters above, \(z_+>0>z_-\), \(0<q_\delta<1\), and every \(x_0>0\) satisfies the **exact finite-sweep identity**
\[
\frac{x_n-z_+}{x_n-z_-}=q_\delta^n\frac{x_0-z_+}{x_0-z_-}.
\]
In particular \(z_+\) is the unique positive attracting projective fixed point.

**Critical compatibility window.** Fix \(a\in(0,1)\), \(\kappa\in\mathbb R\), and an initial ratio \(x_0>0\) independent of \(\delta\). For \(b_\delta=a+\kappa\delta\in(0,1)\), define \(X\) by
\[
X'(t)=\frac{a+\kappa X(t)-(1-a)X(t)^2}{a(1-a)},\qquad X(0)=x_0.
\]
Then, for each finite \(T>0\),
\[
\sup_{0\le t\le T}\left|x_{\lfloor t/\delta\rfloor}-X(t)\right|=O_T(\delta).
\]
Put \(w=\sqrt{\kappa^2+4a(1-a)}\) and \(\zeta_\pm=(\kappa\pm w)/(2(1-a))\). The limiting trajectory is explicit:
\[
\frac{X(t)-\zeta_+}{X(t)-\zeta_-}
=e^{-wt/[a(1-a)]}\frac{x_0-\zeta_+}{x_0-\zeta_-}.
\]
Furthermore, the row-normalized matrix after the initial half-sweep has off-diagonal entries \(P_{12}(x)=a\delta/(x+\delta)\) and \(P_{21}(x)=(1-a)\delta x/(1+\delta x)\). Their entire critical trajectories converge uniformly on \([0,T]\):
\[
\delta^{-1}P_{12}(x_{\lfloor t/\delta\rfloor})\longrightarrow \frac{a}{X(t)},\qquad
\delta^{-1}P_{21}(x_{\lfloor t/\delta\rfloor})\longrightarrow (1-a)X(t).
\]
Since the column-one sum of this row-normalized matrix is \(a-P_{12}+P_{21}\), its **actual column residual** in the critical window satisfies, uniformly on compact times,
\[
\delta^{-1}\bigl((a-P_{12}+P_{21})-b_\delta\bigr)\longrightarrow(1-a)X(t)-a/X(t)-\kappa.
\]
The exact projective rate admits the **joint imbalance/small-kernel crossover** for every \(b_\delta\to a\):
\[
-\log q_\delta\sim
\frac{\sqrt{(b_\delta-a)^2+4a(1-a)\delta^2}}{a(1-a)}.
\]
In particular, for the critical window,
\[
-\log q_\delta=\frac{w}{a(1-a)}\delta+O(\delta^2).
\]
For every fixed contraction target \(0<\theta<1\), the exact number of complete sweeps needed to reduce the projective cross-ratio magnitude by a factor \(\theta\) (when the starting ratio is not at equilibrium) is \(N_\theta(\delta)=\lceil \log(1/\theta)/(-\log q_\delta)\rceil\), and
\[
\delta N_\theta(\delta)\longrightarrow\frac{a(1-a)}{w}\log(1/\theta).
\]

## Assumptions and scope
The result is for *unrelaxed*, deterministic row-then-column Sinkhorn scaling of the specified strictly positive two-by-two kernel. The column marginal depends on the small kernel entry only in the critical-window statements. All divisions are componentwise; the ratio after each complete sweep is used. \(x_0\) is any fixed positive finite number. The finite-parameter conjugacy allows arbitrary \(a,b,\delta\) in their open ranges. No assertion is made for zero kernel entries \(\delta=0\), where scaling may be infeasible for mismatched marginals, nor for general matrix dimensions or overrelaxed/annealed algorithms. The speed statement is *projective error reduction*, not an absolute column-residual stopping-cost bound.

## Proof
**1. Exact map and its projective spectrum.** By homogeneity use \(v=(x,1)\). The row scaling equals
\[
u_1=\frac a{x+\delta},\qquad u_2=\frac{1-a}{1+\delta x}.
\]
The column update gives \(v_1^+=b/(u_1+\delta u_2)\) and \(v_2^+=(1-b)/(\delta u_1+u_2)\). Clearing the positive denominator \((x+\delta)(1+\delta x)\) proves the displayed map. Its representing matrix is \(M=\begin{psmallmatrix}BA&B\delta\\\delta&C\end{psmallmatrix}\), whose determinant is \(B(AC-\delta^2)=Ba(1-a)(1-\delta^2)^2>0\). Thus the two eigenvalues \((S\pm D)/2\) are strictly positive, the fixed-point equation has roots \(z_+>0>z_-\), and their eigenvalue ratio is \(q_\delta\). A direct fractional-linear identity at each fixed point gives
\[
\frac{F_\delta(x)-z_+}{F_\delta(x)-z_-}=q_\delta\frac{x-z_+}{x-z_-}.
\]
Iteration proves the exact formula. Since \(F_\delta\) is strictly increasing and maps positive reals into positive reals, \(x_n\) moves monotonically from \(x_0\) toward \(z_+\), remaining between them.

**2. Uniform critical flow.** With \(b=a+\kappa\delta\), a Taylor expansion of the *full map* on every fixed compact interval \(0<m\le x\le M<\infty\) yields, uniformly with one derivative,
\[
F_\delta(x)=x+\delta f(x)+O(\delta^2),\qquad
f(x)=\frac{a+\kappa x-(1-a)x^2}{a(1-a)}.
\]
The positive fixed point \(z_+(\delta)\) converges to \(\zeta_+>0\), so for sufficiently small \(\delta\), all iterates from \(x_0\) lie in a compact positive interval independent of \(\delta\). The ODE is locally Lipschitz there; it is likewise monotone toward \(\zeta_+\) and stays in a compact interval. The standard explicit-Euler local-error bound \(O(\delta^2)\), followed by the discrete Gronwall inequality for at most \(T/\delta\) sweeps, yields the stated uniform \(O_T(\delta)\) error. The floor introduces at most another \(O(\delta)\) time-discretization error.

**3. Riccati solution and observable flux.** Factoring the right-hand side gives \(f(X)=-(X-\zeta_+)(X-\zeta_-)/a\); differentiation of the logarithm of the cross-ratio gives the constant \(-w/[a(1-a)]\). This proves the displayed solution, including the equilibrium case by continuity. The row-normalized off-diagonal entries follow directly from \(u\) and \(v\). Uniform positive lower bounds on \(X\) and \(x_n\) make division continuous, so the rescaled flux limits follow from Step 2. The column-one residual is exactly \(P_{21}-P_{12}-(b_\delta-a)\), which proves the residual trajectory by subtracting the fixed marginal discrepancy.

**4. Joint sharp rate and iteration law.** Since \(b_\delta\to a\), the quantities above satisfy
\[
BA-C=\frac{b_\delta-a}{1-b_\delta}+O(\delta^2),\quad
B=\frac a{1-a}+o(1),\quad S=2a+o(1).
\]
Consequently
\[
D=\frac{1+o(1)}{1-a}\sqrt{(b_\delta-a)^2+4a(1-a)\delta^2}.
\]
This comparison is valid even if the two terms have different orders because their squared sum is bounded below by a positive multiple of \(\delta^2\) and the omitted \(O(\delta^2)\) correction is negligible relative to that scale. Using \(\log[(S+D)/(S-D)]=2D/S+O((D/S)^3)\) proves the joint crossover. If \(b_\delta=a+\kappa\delta\), the same expansions have a one-order-higher remainder and give the explicit coefficient. Finally the cross-ratio identity makes the required contraction factor \(q_\delta^n\) exactly, proving the ceiling expression and its limit.

## Verification
The standalone standard-library Python program `verify_sinkhorn.py` checks the exact row/column update and determinant identities using rational arithmetic; compares the cross-ratio conjugacy, Euler flow and off-diagonal formulas at finite parameters; and spot-checks the joint spectral crossover. Execute `python3 verify_sinkhorn.py`. The program reports 1,692 successful assertions. These finite tests check algebra and examples, while the proofs of uniform convergence and sharp asymptotics are the analytic arguments above.

## Relationship to prior work
The local convergence spectrum of standard Sinkhorn scaling is established in Knight (2008) and explicitly used by Lehmann, von Renesse, Sambale, and Uschmajew (2020). The eigenvalue ratio alone is therefore not claimed as new. Brossard and Leuridan (2016) analyze convergence and structural support conditions for iterated proportional fitting. Chen et al. (2022) accelerate convergence by changing the regularization schedule, rather than analyzing a fixed singular kernel. Deb et al. (2023) derive a continuum Wasserstein flow for smooth marginals with time proportional to inverse entropic regularization; its hypotheses and scale do not contain the present two-atom near-disconnection with \(n\delta\) held fixed. The contribution examined here is the complete joint marginal-mismatch/singular-kernel boundary layer: a uniform entire-trajectory Riccati limit, explicit small cross-flux profiles and the sharp projective iteration constant in this regime.

## Limitations
The kernel has two atoms and one symmetric off-diagonal parameter. The convergence window assumes the column marginal approaches the row marginal at exactly the indicated rate for the Riccati profile; the general rate asymptotic only assumes \(b_\delta\to a\). There is no multidimensional generalization or claim that this is the first appearance of the general Möbius-to-Riccati limiting mechanism. The theorem excludes arbitrary initial ratios depending on \(\delta\), and makes no bound on floating-point underflow when \(\delta\) is extremely small. A classical special-case formulation in matrix scaling, iterative proportional fitting or projective dynamics remains a possible publication-precedence risk; an independent literature review is not represented as performed.

## References
1. P. A. Knight, *The Sinkhorn–Knopp algorithm: convergence and applications*, SIAM J. Matrix Anal. Appl. 30 (2008), 261–275. https://doi.org/10.1137/060659624 ; author preprint https://strathprints.strath.ac.uk/19685/1/skapp.pdf .
2. T. Lehmann, M.-K. von Renesse, A. Sambale, A. Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm* (first public preprint December 23, 2020), https://arxiv.org/abs/2012.12562 .
3. J. Chen, L. Chen, Y. P. Liu, R. Peng, A. Ramaswami, *Exponential Convergence of Sinkhorn Under Regularization Scheduling* (2022), https://arxiv.org/abs/2207.00736 .
4. N. Deb, Y.-H. Kim, S. Pal, G. Schiebinger, *Wasserstein Mirror Gradient Flow as the Limit of the Sinkhorn Algorithm* (2023), https://arxiv.org/abs/2307.16421 .
5. E. Brossard and C. Leuridan, *Iterated proportional fitting procedure and infinite products of stochastic matrices* (2016), https://arxiv.org/abs/1606.09126 .

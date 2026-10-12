# Two sharp sampling thresholds for inconsistent equiangular Kaczmarz

## Finding

Consider a least-squares problem whose three unit row vectors form the regular planar three-vector tight frame. Its normal matrix is a scalar multiple of the identity, yet independent random reshuffling and independent sampling with replacement can exhibit opposite mean-square terminal-error orderings. The following gives exact recurrences and a complete classification for a least-squares initialization, with distinct sharp one-epoch and stationary thresholds.

Let \(u_1=(1,0)^\mathsf T\), \(u_2=(-1/2,\sqrt3/2)^\mathsf T\), and \(u_3=(-1/2,-\sqrt3/2)^\mathsf T\). Let \(U\in\mathbb R^{3\times2}\) have these row vectors, let \(b\in\mathbb R^3\), and put
\[
x_\star=\mathop{\rm argmin}_{x\in\mathbb R^2}\|Ux-b\|_2^2=\frac23U^\mathsf T b,
\qquad \delta=\frac{b_1+b_2+b_3}{3}.
\]
For a fixed relaxation \(0<\eta<2\), both methods make the same row-action update
\[
x^+=x+\eta(b_i-u_i^\mathsf T x)u_i.
\]
One method selects an independent uniform permutation of all three rows at the beginning of each epoch (RR). The other selects a row uniformly and independently for each of its three updates (IID). All epoch permutations and indices are independent of preceding iterates. Set \(e_k=x_{3k}-x_\star\) and \(S_k=\mathbb E\|e_k\|_2^2\); the common \(x_0\) is deterministic (the results also hold for a common independent random initialization with a finite second moment).

Define
\[
q=1-\eta+\frac{\eta^2}{2},\quad c_I=q^3,\quad d_I=\eta^2\delta^2(1+q+q^2),
\]
\[
c_R=1-3\eta+3\eta^2-\eta^3+\frac{\eta^6}{32},\qquad
 d_R=\frac{\eta^4\delta^2(\eta^2+6\eta+12)}{16}.
\]
For **every** epoch count \(k\ge0\) and every deterministic start, the exact identities are
\[
S_{k+1}^{I}=c_I S_k^{I}+d_I,\qquad
S_{k+1}^{R}=c_R S_k^{R}+d_R,\qquad
S_0^I=S_0^R=\|x_0-x_\star\|_2^2.
\]
In particular, both coefficients lie strictly between zero and one, and \(c_R<c_I\) for every \(0<\eta<2\): reshuffling always has the faster *homogeneous mean-square contraction* in this model.

Suppose now that \(\delta\ne0\), so the system is inconsistent. Define \(\eta_1\) as the unique root in \((0,2)\) of
\[
3\eta^4-22\eta^3+28\eta^2-48\eta+48=0,
\qquad \eta_1\approx1.1803110213,
\]
and \(\eta_\infty\) as the unique root in \((0,2)\) of
\[
\eta^3+2\eta^2+6\eta-12=0,
\qquad \eta_\infty\approx1.2126391135.
\]
They are distinct, with \(\eta_1<\eta_\infty\). The one-epoch *noise injection* satisfies \(d_R<d_I\) for \(\eta<\eta_1\), equality at \(\eta_1\), and \(d_R>d_I\) for \(\eta>\eta_1\). However, the stationary mean-square errors \(V_R=d_R/(1-c_R)\) and \(V_I=d_I/(1-c_I)\) satisfy \(V_R<V_I\) for \(\eta<\eta_\infty\), equality at \(\eta_\infty\), and \(V_R>V_I\) for \(\eta>\eta_\infty\). Furthermore,
\[
\lim_{\eta\uparrow2}\frac{V_R}{V_I}=\frac73.
\]

For the **least-squares initialization** \(x_0=x_\star\), the full finite-epoch ordering is sharp:

- \(0<\eta<\eta_1\): RR has strictly smaller mean-square error for all integers \(k\ge1\). At \(\eta=\eta_1\), the first epoch ties and RR strictly improves for every \(k\ge2\).
- \(\eta_1<\eta<\eta_\infty\): RR is worse after one epoch, but strictly better for all sufficiently large epochs. The ratio of RR to IID errors decreases strictly with the positive real epoch argument, so its crossing of one is unique; integer epoch counts may include a single tie.
- \(\eta_\infty\le\eta<2\): RR has strictly larger mean-square error at every finite integer epoch \(k\ge1\).

For general common initialization, RR is still no worse than IID at every epoch whenever \(\eta\le\eta_1\). Statements of universal RR inferiority at larger relaxation parameters are **not** asserted for arbitrary initial errors.

A concrete temporal reversal occurs at \(\eta=6/5\) and \(x_0=x_\star\):
\[
S_1^R-S_1^I=\frac{1512}{15625}>0,
\qquad S_2^R-S_2^I=-\frac{1832976}{48828125}<0
\]
when \(\delta=1\); for other nonzero residual magnitudes both differences scale by \(\delta^2\).

## Assumptions and scope

The row frame is exactly the stated planar regular triangle (or an orthogonal image and/or relabeling thereof), the right-hand side is arbitrary but fixed, the updates use a constant common \(\eta\in(0,2)\), and each new permutation or IID row draw is fresh and independent. A complete epoch always means exactly three row updates. The objective is the expected **squared Euclidean distance** from the least-squares solution at epoch endpoints, not an averaged iterate, almost-sure Lyapunov exponent, residual norm during epochs, or wall-clock cost. The right-hand-side perturbation is fixed across repeated visits to the same row, not resampled independently on every visit.

Since \(\sum_i u_i=0\) and \(\sum_i u_i u_i^\mathsf T=\tfrac32 I_2\), every possible least-squares residual is of the form \(b-Ux_\star=\delta(1,1,1)^\mathsf T\), not just the equal-right-hand-side example. The normal matrix has condition number one. The strict phase changes require \(\delta\ne0\). In the consistent case \(\delta=0\), both noise terms vanish and RR has strictly stronger mean-square contraction for every nonzero initial error.

## Proof

**1. Center at the least-squares solution.** The preceding tight-frame identities give \(x_\star=(2/3)U^\mathsf T b\). The orthogonal complement of the range of \(U\) is the span of the all-ones vector, and averaging the residual gives \(b-Ux_\star=\delta\mathbf1\). Hence with \(e=x-x_\star\), each selected row produces
\[
e^+=A_i e+\eta\delta u_i,\qquad A_i=I_2-\eta u_i u_i^\mathsf T.
\]
This proves the claimed extension to arbitrary fixed \(b\), not merely a special right-hand side.

**2. Exact IID recursion.** Uniform sampling yields \(\mathbb E_i A_i^\mathsf T A_i=qI_2\) by \(A_i^2=I_2-\eta(2-\eta)u_i u_i^\mathsf T\). Its cross term vanishes because \(\sum_i A_i u_i=(1-\eta)\sum_i u_i=0\). Therefore
\[
\mathbb E_i\bigl[\|e^+\|_2^2\mid e\bigr]=q\|e\|_2^2+\eta^2\delta^2.
\]
Three independent updates give \(c_I=q^3\) and \(d_I=\eta^2\delta^2(1+q+q^2)\) exactly, without any isotropy hypothesis on the iterate.

**3. Exact reshuffling recursion.** For an order \(\pi=(\pi_1,\pi_2,\pi_3)\), write one epoch as \(e^+=M_\pi e+\delta v_\pi\), where
\[
M_\pi=A_{\pi_3}A_{\pi_2}A_{\pi_1},\quad
v_\pi=\eta\bigl(u_{\pi_3}+A_{\pi_3}u_{\pi_2}+A_{\pi_3}A_{\pi_2}u_{\pi_1}\bigr).
\]
For the order \((1,2,3)\), direct multiplication gives
\[
M_{123}=\frac18\begin{pmatrix}
(\eta-1)(\eta^2+4\eta-8)&\sqrt3\eta^2\\
\sqrt3\eta^2(\eta-1)&3\eta^2-12\eta+8
\end{pmatrix},\qquad
v_{123}=-\frac{\eta^2}{8}\begin{pmatrix}\eta+6\\\sqrt3(\eta+2)\end{pmatrix}.
\]
The dihedral symmetries of the three row vectors act transitively on the six orders. Thus the norms \(\|v_\pi\|_2\) and Frobenius norms \(\|M_\pi\|_F\) do not depend on \(\pi\). The cyclic rotations additionally imply
\[
\frac16\sum_\pi M_\pi^\mathsf T v_\pi=0,
\qquad \frac16\sum_\pi M_\pi^\mathsf T M_\pi=
\frac{\|M_{123}\|_F^2}{2}I_2.
\]
Here the latter average is symmetric and commutes with a nontrivial planar rotation, so it is scalar. Taking the displayed matrix's Frobenius norm and vector's squared norm yields respectively
\[
\frac{\|M_{123}\|_F^2}{2}=1-3\eta+3\eta^2-\eta^3+\frac{\eta^6}{32}=c_R,
\quad \|v_{123}\|_2^2=\frac{\eta^4(\eta^2+6\eta+12)}{16}.
\]
The RR conditional squared-norm recurrence follows. Independence of each new permutation justifies iteration of that scalar recurrence over every epoch.

**4. Exact contraction and stability.** Factoring the difference gives
\[
c_R-c_I=-\frac{3\eta^2(2-\eta)^4}{32}<0.
\]
Put \(Q(\eta)=\eta^4+2\eta^3+4\eta^2-24\eta+48\). Then
\[
1-c_R=\frac{\eta(2-\eta)Q(\eta)}{32}.
\]
To verify \(Q>0\) on \((0,2)\), set \(t=\eta/(2-\eta)>0\); direct expansion gives
\[
(1+t)^4Q\!\left(\frac{2t}{1+t}\right)
=48t^4+96t^3+160t^2+144t+48>0.
\]
Also \(q=((\eta-1)^2+1)/2\in(0,1)\). Thus \(0<c_R<c_I<1\); positivity of \(c_R\) follows from its positive mean-square matrix-product representation, including at \(\eta=1\), where adjacent nonorthogonal rank-one projections give a nonzero product.

**5. Two distinct and unique thresholds.** With \(P_4(\eta)=3\eta^4-22\eta^3+28\eta^2-48\eta+48\),
\[
d_R-d_I=-\frac{\eta^2\delta^2}{16}P_4(\eta).
\]
Under the same positive change of variable,
\[
(1+t)^4P_4\!\left(\frac{2t}{1+t}\right)
=-64t^4-48t^3+112t^2+96t+48.
\]
The descending coefficient list has precisely one sign change, so Descartes' rule gives at most one positive zero; opposite endpoint signs give exactly one. The bounds \(P_4(59/50)>0\), \(P_4(119/100)<0\) place \(\eta_1\) between \(1.18\) and \(1.19\).

The stationary values exist by Step 4 and simplify to
\[
V_I=\frac{2\eta\delta^2}{2-\eta},\qquad
V_R=\frac{2\eta^3\delta^2(\eta^2+6\eta+12)}{(2-\eta)Q(\eta)},
\quad \frac{V_R}{V_I}=\frac{\eta^2(\eta^2+6\eta+12)}{Q(\eta)}.
\]
Since \(\eta^2(\eta^2+6\eta+12)-Q(\eta)=4P_3(\eta)\) for \(P_3(\eta)=\eta^3+2\eta^2+6\eta-12\), and \(P_3'(\eta)=3\eta^2+4\eta+6>0\), there is a unique stationary threshold \(\eta_\infty\). The exact signs \(P_3(121/100)<0\) and \(P_3(61/50)>0\) put it between \(1.21\) and \(1.22\), strictly beyond \(\eta_1\). Evaluating the displayed ratio at \(\eta=2\) gives the limit \(7/3\).

**6. All finite-epoch comparisons.** Solving each recurrence gives, for \(j\in\{R,I\}\),
\[
S_k^j=c_j^k S_0+V_j(1-c_j^k),\quad k\ge0.
\]
If \(\eta\le\eta_1\), both \(c_R<c_I\) and \(d_R\le d_I\); induction on these recurrences with common \(S_0\ge0\) establishes the stated RR dominance for every start. When \(S_0=0\) and \(\delta\ne0\),
\[
\frac{S_k^R}{S_k^I}=\frac{V_R}{V_I}\,
\frac{1-c_R^k}{1-c_I^k}.
\]
For real \(k>0\), the latter factor decreases strictly; its value at \(k=1\) is \((1-c_R)/(1-c_I)>1\) and its limit as \(k\) tends to infinity is \(1\). To prove monotonicity, write \(c_R=e^{-a}\), \(c_I=e^{-b}\), so \(a>b>0\), and differentiate its logarithm to obtain \(a/(e^{ak}-1)-b/(e^{bk}-1)<0\). This proves the claimed one-crossing regime when \(\eta_1<\eta<\eta_\infty\), and the never-crossing regime when \(\eta\ge\eta_\infty\). The example at \(\eta=6/5\) is immediate from the exact recurrences.

## Verification

Execute `python verify.py` in the same directory as this document; the standalone script requires Python 3 and SymPy. It independently composes and averages all six affine permutation maps, checks the exact matrix and vector moment identities, verifies all critical polynomial factorizations and rational sign brackets, and directly enumerates every length-three IID index path. It also enumerates all 36 two-epoch reshuffling histories and all 729 six-step IID histories, each at two initial conditions, using exact rational arithmetic in the basis whose second coordinate is a rational multiple of \(\sqrt3\). This is an algebraic check and finite falsification test; the all-parameter and all-epoch conclusions follow from the proof, not the finite enumeration.

## Relationship to prior work

Gan and Wu [1] analyze randomized Kaczmarz and related methods for fixed noisy and inconsistent linear systems, deriving convergence-to-neighborhood estimates for independently sampled updates. Their results motivate an exact comparison of row-order dependence but do not specify RR versus IID epoch-terminal moments or the two phase boundaries derived here.

Han and Xie [2] analyze the genuine RRK update, but their central linear-convergence theorem explicitly assumes that the equations are consistent. Thus their homogeneous contraction results do not imply the noisy affine forcing terms or the reversal for arbitrary inconsistent right-hand sides. Recht and Ré [3] compare noncommutative sampling and even formulate a noisy finite-sum model, but their displayed noise-risk decomposition averages *independent zero-mean Gaussian row noises* and does not determine the present fixed, perfectly correlated least-squares residual mode. Ferreira, Acebrón, and Monteiro [4] empirically compare with- and without-replacement Kaczmarz, including a row-shuffling-per-cycle implementation, without the present exact noisy phase diagram. Epperly, Goldshlager, and Webber [5] use tail averaging to remove an inconsistent-system error floor; an averaged estimator is not the raw epoch-terminal objective studied here.

Prior analyses of exact-noise or homogeneous matrix products may motivate the algebraic moment decomposition, but none of the inspected statements provides these two nonidentical thresholds, their strict separation, and the unique finite-to-stationary reversal for the regular three-row least-squares system.

## Limitations

The result is exact for the three-row, two-variable regular tight frame, independent epoch reshuffles, fixed data, one common constant relaxation, and mean-square errors at epoch endpoints. It is not a universal RR-versus-IID comparison for arbitrary row frames, random per-visit noise, shuffled-once ordering, row probabilities other than uniform, varying stepsizes, or time averages. Stationary mean-square error is not almost-sure convergence of the individual iterates. The uniqueness and novelty assessment is necessarily relative to the inspected literature; a differently parameterized or unindexed equivalent calculation remains possible.

## References

[1] Y. Gan and G. Wu, *On Convergence Behavior of Randomized Kaczmarz-type Methods for Solving Doubly Noisy Linear Systems*, arXiv:2608.22259, first posted 2026-08-23. https://arxiv.org/abs/2608.22259

[2] D. Han and J. Xie, *A Simple Linear Convergence Analysis of the Randomized Reshuffling Kaczmarz Method*, arXiv:2410.01140, journal DOI:10.1007/s40305-025-00623-x. https://arxiv.org/abs/2410.01140

[3] B. Recht and C. Ré, *Beneath the Valley of the Noncommutative Arithmetic-Geometric Mean Inequality: Conjectures, Case-Studies, and Consequences*, arXiv:1202.4184. https://arxiv.org/abs/1202.4184

[4] A. Ferreira, J. A. Acebrón, and J. Monteiro, *Survey of a Class of Iterative Row-Action Methods: The Kaczmarz Method*, Numerical Algorithms (2024), DOI:10.1007/s11075-024-01945-2. https://link.springer.com/article/10.1007/s11075-024-01945-2

[5] E. N. Epperly, G. Goldshlager, and R. J. Webber, *Randomized Kaczmarz with Tail Averaging*, arXiv:2411.19877. https://arxiv.org/abs/2411.19877

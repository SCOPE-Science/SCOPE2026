# Exact multistability staircase and memory-rate ceiling for diagonal RMSProp

## Finding
For the autonomous, uncorrected, coordinatewise RMSProp map below on a strictly convex diagonal quadratic, the prime-period-two cycles admit an exact stability classification. Let \(k\) be the number of coordinates whose scalar threshold has been crossed. The underlying census of \((3^k-1)/2\) prime-period-two orbits is an immediate diagonal specialization of Loh et al., Theorem 5.2. Away from threshold equalities, exactly \(2^{k-1}\) are locally exponentially attracting when \(k>0\), whereas the others are unstable. In particular, once all thresholds are crossed there are \(2^{d-1}\) coexisting hyperbolic attracting two-cycles; each persists for all sufficiently small symmetric off-diagonal perturbations of the Hessian.

The return spectrum is explicit, including the multipliers for coordinates identically zero on the orbit. For an all-active cycle (nonzero in every coordinate, possible only when \(h>\max_i\theta_i\)), the two-step spectral radius has the memory-determined lower bound \(\beta\). For \(0<\beta<1/9\), this bound is attainable at one common stepsize for all coordinates if and only if
\[
\frac{a_{\max}}{a_{\min}}\le
\frac{(1+3\sqrt\beta)(1-\sqrt\beta)}{(1-3\sqrt\beta)(1+\sqrt\beta)}.
\]
For \(1/9\le\beta<1\), every sufficiently large stepsize realizes the optimum. These are statements about the two-step *linear spectral radius*, not about a uniform norm bound at a defective endpoint.

## Assumptions and scope
Fix an integer \(d\ge1\), positive diagonal curvatures \(a_1,\ldots,a_d\), stepsize \(h>0\), outside-square-root regularization \(\varepsilon>0\), and memory coefficient \(0<\beta<1\). Define \(L(x)=\tfrac12\sum_{i=1}^{d}a_ix_i^2\) and the state space \(\mathbb R^d\times[0,\infty)^d\). The autonomous discrete-time map is, simultaneously for each coordinate,
\[
 v_i^+=\beta v_i+(1-\beta)a_i^2x_i^2,\qquad
 x_i^+=x_i-\frac{h a_i x_i}{\sqrt{v_i^+}+\varepsilon}.
\]
There is no bias correction, momentum, stochastic gradient, time-varying stepsize, or weight decay. A prime two-cycle means two distinct states exchanged by the full map, counted once under exchange. Set
\[
 \theta_i=\frac{2\varepsilon}{a_i},\quad I_h=\{i:h>\theta_i\},\quad k=|I_h|,
 \quad r_i=\frac h2-\frac\varepsilon{a_i}\quad (i\in I_h).
\]
Local exponential attraction refers to the full state in the relative topology of this half-space. Stability classification of boundary cycles below excludes equality \(h=\theta_i\), but the exact *count* does not. For the spectral statements concerning all-active cycles require \(h>\max_i\theta_i\).

## Proof
**1. Scalar two-cycles (the diagonal instance of the prior reduction).** In Loh et al., Theorem 5.2, Eq. (22), take \(X=x/h\), scaled memory \(W=\sqrt v/h\) coordinatewise, and \(c=\varepsilon/h\). The reduced equation is \(2X_i=a_iX_i/(a_i|X_i|+c)\) in the diagonal setting. Thus each coordinate is zero or has absolute value \(1/2-c/a_i>0\); global sign reversal describes the same orbit. For completeness, this reduction has the following short scalar proof. Consider any period-two state \((x_0,v_0)\leftrightarrow(x_1,v_1)\). If \(x_0=0\), then \(x_1=0\), and the geometric memory update forces \(v_0=v_1=0\). Otherwise the two position increments have opposite signs, so \(x_0,x_1\) have opposite signs. By reversing the labels, write \(x_0=p>0\), \(x_1=-r<0\). Solving the two memory equations gives
\[
 v_1=\frac{a^2(p^2+\beta r^2)}{1+\beta},\qquad
 v_0=\frac{a^2(r^2+\beta p^2)}{1+\beta}.
\]
The two position increments imply
\[
 p(\sqrt{v_0}+\varepsilon)=r(\sqrt{v_1}+\varepsilon).
\]
If \(p>r\), then \(\sqrt{v_0}>ar\) while \(\sqrt{v_1}<ap\); consequently the left-hand side is strictly larger than the right-hand side, a contradiction. The case \(r>p\) is symmetric. Therefore \(p=r\), \(v_0=v_1=a^2p^2\), and the position update gives \(p=h/2-\varepsilon/a\). This is positive exactly for \(h>2\varepsilon/a\). Thus each coordinate contributes only the zero fixed state or a unique sign-flipping pair of nonzero states.

**2. Product census and stability.** Every full two-cycle is a product of these scalar choices, with at least one active coordinate nonzero. The \(k\) available positions are independently labeled \(-,0,+\). Full time advance exchanges all signs, with no fixed nonzero sign pattern, giving exactly \((3^k-1)/2\) distinct two-cycles.

At a nonzero scalar point the memory is positive, and direct differentiation of the one-step map yields
\[
 J_+=\begin{pmatrix}
 -1+4(1-\beta)r/h&2\beta/(a^2h)\\
 2(1-\beta)a^2r&\beta
 \end{pmatrix},\quad
 J_-=P J_+P,\quad P=\operatorname{diag}(-1,1).
\]
Writing \(K=PJ_+\), the return derivative is \(K^2\), the sign-symmetry factorization also used by Loh et al. in the proof of Theorem 5.7. Here the diagonal scalar block yields exact coefficients at every crossed threshold:
\[
 \det K=\beta,\qquad
 \operatorname{tr}K=s=-1+3\beta+\frac{2(1-\beta)}q,
 \quad q=\frac{ha}{2\varepsilon}>1.
\]
Because \(3\beta-1<s<1+\beta\), the three strict Schur conditions \(1-\beta>0\), \(1-s+\beta>0\), and \(1+s+\beta>0\) hold. Thus both eigenvalues of \(K\), and hence those of \(K^2\), lie strictly inside the unit disk for *every* \(q>1\).

At the scalar zero state, the relative derivative is \(\operatorname{diag}(1-ha/\varepsilon,\beta)\): the position error after subtracting the linear term is \(O(|x|\sqrt{v^+})=o(\|(x,v)\|)\). A zero coordinate therefore contributes \((1-ha/\varepsilon)^2\) and \(\beta^2\) to the two-step spectrum. For \(h>2\varepsilon/a\), the position multiplier has modulus bounded below by a number greater than one in a sufficiently small neighborhood; a state there with \(x\ne0\) cannot stay in that neighborhood forever. For \(0<h<2\varepsilon/a\), choose a sufficiently small rectangle \(|x|\le r_0,\ 0\le v\le V_0\) with \(a^2r_0^2\le V_0\) in which the multiplier has modulus bounded by \(\eta<1\). The rectangle is invariant and the forced geometric recurrence for \(v\) decays exponentially together with \(x\). Coordinatewise independence now shows that, for stepsizes avoiding all threshold equalities, exactly the patterns nonzero in every crossed coordinate attract; their number is \(2^{k-1}\) for \(k>0\). Any omitted crossed coordinate is unstable. When all thresholds are crossed, every state coordinate of an attracting cycle has strictly positive memory. The map is smooth nearby and its return derivative has no unit-modulus eigenvalues. The implicit-function theorem applied to the return equation proves persistence, as distinct attracting cycles, under sufficiently small symmetric off-diagonal Hessian perturbations (within the positive-definite cone).

**3. Exact spectral plateau and condition-number obstruction.** Let \(\zeta_{\pm}\) solve \(\zeta^2-s\zeta+\beta=0\). The two-step spectral radius in one active coordinate is \(\rho(q)=\max(|\zeta_+|^2,|\zeta_-|^2)\). Since the product of the two return eigenvalues equals \(\beta^2\), necessarily \(\rho(q)\ge\beta\). Equality holds precisely for \(|s|\le2\sqrt\beta\), namely
\[
 q\ge q_-=\frac{2(1+\sqrt\beta)}{1+3\sqrt\beta}
 \quad\text{and, if }0<\beta<1/9,\quad
 q\le q_+=\frac{2(1-\sqrt\beta)}{1-3\sqrt\beta}.
\]
For \(\beta\ge1/9\) there is no finite upper restriction. Every all-active two-cycle has the same coordinatewise block spectrum and hence common two-step spectral radius \(R(h)=\max_i\rho(ha_i/(2\varepsilon))\). The lower bound \(R(h)\ge\beta\) is attained exactly when every ratio lies in the allowable band. Since \(q\) increases with curvature, this requires \(h\ge2\varepsilon q_-/a_{\min}\) and, when \(\beta<1/9\), \(h\le2\varepsilon q_+/a_{\max}\). The latter interval is nonempty precisely under the displayed sharp curvature-ratio bound. If the ratio bound fails, compactness together with \(R(h)\to1\) as \(h\downarrow2\varepsilon/a_{\min}\) and \(\lim_{h\to\infty}R(h)>\beta\) gives even \(\inf_{h>2\varepsilon/a_{\min}}R(h)>\beta\). For \(\beta\ge1/9\), any \(h\ge2\varepsilon q_-/a_{\min}\) attains the optimum.

## Verification
Run `python verify.py` with Python 3 from the same directory. The standalone test checks 40 exact-period scalar returns against independently differentiated one- and two-step Jacobians and Schur traces/determinants, finite combinatorial counts for one through five active coordinates, and the sharp example \(\beta=1/16\), \(q_-=10/7\), \(q_+=6\), allowable curvature ratio \(21/5\). The deterministic output is in `verify_output.txt`. These are finite numerical checks; the all-dimensional statements, instability classification, and persistence are proved above, not inferred from finite tests.

For instance with \(\varepsilon=1\), \(\beta=1/16\), curvatures \((4,2,1)\), and \(h=2.9\), there are \(13\) prime two-cycles, exactly \(4\) attracting, and every attracting cycle has two-step spectral radius \(1/16\). With curvatures \((5,1)\) and \(\beta=1/16\), no all-active cycle can reach that optimal common radius at any stepsize, because \(5>21/5\).

## Relationship to prior work
Loh, Mireles James, Xu, and Tao, *The Dynamics of RMSProp Beyond the Stability Threshold* (arXiv:2610.30078v1, October 21, 2026), give an exact reduction of **all** period-two orbits for the same update (Theorem 5.2, Eq. (22)). The diagonal orbit census above is its immediate corollary, not a distinct contribution. Their proof of Theorem 5.7 also supplies the sign-symmetry factorization and a general derivative formula, used there for near-threshold branch stability and a critical multiplier expansion. Their large-stepsize corner results (Theorems 5.9–5.10) already give a branch for each diagonal sign corner up to global sign. The distinct claim here is the exact all-step attracting/unstable classification off thresholds and, quantitatively, the sharp all-active spectral-radius plateau and condition-number obstruction, not the underlying orbit reduction, large-step branch existence or symmetry device. Regis and Chewi (arXiv:2605.06821v1, §5 and Appendix D.2.2) study componentwise RMSProp and continuous rod flow, and Dereich and Jentzen (arXiv:2608.30382v1) study stochastic convergence bounds. Neither comparison supplies this discrete spectral plateau.

## Limitations
The classification applies to deterministic autonomous RMSProp with coordinatewise second moments and strictly diagonal positive curvature. It does not assert a complete two-cycle census for nondiagonal Hessians, global attraction, exclusion of longer cycles, or the stability character at exact coordinate thresholds \(h=2\varepsilon/a_i\). Under Hessian perturbations only the already-hyperbolic all-active cycles are asserted to persist; the diagonal count need not persist. At a repeated Floquet eigenvalue on the plateau boundary, the spectral radius \(\beta\) need not imply a pure \(O(\beta^n)\) norm bound. Independent mathematical and historical-priority assessments have not been performed.

## References
Regis, E., Chewi, S., *A Rod Flow Model for Adam at the Edge of Stability*, arXiv:2605.06821v1 (first posted 2026-05-07), Sections 5 and Appendix D.2.2. https://arxiv.org/html/2605.06821v1

Dereich, S., Jentzen, A., *Convergence rates for the RMSprop optimizer with full control of the hyperparameters*, arXiv:2608.30382v1 (first posted 2026-08-31). https://arxiv.org/abs/2608.30382

Loh, K., Mireles James, J. D., Xu, Z., Tao, M., *The Dynamics of RMSProp Beyond the Stability Threshold*, arXiv:2610.30078v1 (posted 2026-10-21), Sections 5 and 8. https://arxiv.org/abs/2610.30078

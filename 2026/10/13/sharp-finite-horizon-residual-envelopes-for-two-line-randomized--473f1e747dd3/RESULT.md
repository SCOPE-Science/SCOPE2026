# Sharp finite-horizon residual envelopes for two-line randomized Kaczmarz

## Finding

Let \(u_1,u_2\in\mathbb R^2\) be linearly independent unit vectors. Change a row sign if necessary and write their absolute inner product as \(c=|u_1^{\mathsf T}u_2|\in[0,1)\). Consider the consistent homogeneous system \(u_i^{\mathsf T}e=0\). At every iteration choose either row independently with probability \(1/2\), and update
\[
e_{t+1}=(I-u_{J_t}u_{J_t}^{\mathsf T})e_t.
\]
Set \(H=(u_1u_1^{\mathsf T}+u_2u_2^{\mathsf T})/2\) and measure the *expected squared mean-row residual*
\[
F_t(c,e_0)=\mathbb E[e_t^{\mathsf T}He_t],\qquad\|e_0\|_2=1.
\]
For every integer \(t\ge1\) and every initial error, the **exact** expression is
\[
F_t(c,e_0)=\frac{1-c^2}{2}\left(\frac{1+c^2}{2}\right)^{t-1}e_0^{\mathsf T}(I-H)e_0.
\]
Consequently, the worst initial direction at fixed coherence is a minimum-eigenvalue eigenvector of \(H\), and
\[
G_t(c):=\max_{\|e_0\|_2=1}F_t(c,e_0)
=\frac{(1-c)(1+c)^2}{4}\left(\frac{1+c^2}{2}\right)^{t-1}.
\]
At every integer horizon \(t\ge1\), the maximum of \(G_t\) over **all** \(c\in[0,1)\) occurs at a *unique* interior coherence \(c_t\), the unique root in \((0,1)\) of
\[
1+(2t-5)c_t+c_t^2-(2t+1)c_t^3=0.
\]
These maximizers move strictly toward parallel rows as the horizon increases:
\[
c_1=\frac13,\qquad \max_cG_1(c)=\frac8{27},\qquad
c_{t+1}>c_t,\qquad
\lim_{t\to\infty}t(1-c_t)=1,
\quad\lim_{t\to\infty}tG_t(c_t)=\frac1{\mathrm e}.
\]
Thus \(1/\mathrm e\) is the **sharp leading constant** for this two-row, unit-initial-error last-iterate residual envelope; it is not a claimed universal constant for arbitrary row systems.

There is a distinct *transient* phenomenon. The maximum possible ratio of the first residual to the initial residual is
\[
\sup_{e_0\ne0}\frac{F_1(c,e_0)}{F_0(c,e_0)}=\frac{(1+c)^2}{2}.
\]
Hence, for **every** initial error the expected residual is nonincreasing at the first step if and only if \(c\le\sqrt2-1\). Above this threshold some errors exhibit an expected residual increase; the largest possible increase factor tends to \(2\) as \(c\uparrow1\). Nevertheless \(F_{t+1}=((1+c^2)/2)F_t\) for every \(t\ge1\), so every later expected residual step strictly contracts whenever the preceding residual is nonzero.

## Assumptions and scope

All statements are in exact real arithmetic on \(\mathbb R^2\), with exactly two independent normalized equations, equal independent row probabilities, full orthogonal projection (no relaxation), and a common exact solution. The Euclidean initial-error norm is fixed at one when taking the finite-horizon envelope. The loss is \(\mathbb E[(|u_1^{\mathsf T}e_t|^2+|u_2^{\mathsf T}e_t|^2)/2]\), not the expected squared Euclidean error. The coefficient \(c=1\) is excluded because the two rows become dependent; all extrema occur at \(c_t<1\).

## Proof

**Exact residual law.** For either row \(j\), after applying its projector \(P_j=I-u_ju_j^{\mathsf T}\), the error lies in the one-dimensional orthogonal complement of \(u_j\). Every vector \(v\) on that line satisfies
\[
v^{\mathsf T}Hv=\frac{1-c^2}{2}\|v\|_2^2.
\]
Conditioning on the first independent uniform draw gives \(\mathbb E\|e_1\|_2^2=e_0^{\mathsf T}(I-H)e_0\). Subsequently, for a vector already on one of the two perpendicular lines, the next draw leaves the vector unchanged with probability \(1/2\), and contracts its squared norm by \(c^2\) with probability \(1/2\). Hence \(\mathbb E\|e_t\|_2^2=((1+c^2)/2)^{t-1}e_0^{\mathsf T}(I-H)e_0\). Multiplication by \((1-c^2)/2\) yields the first formula. The two eigenvalues of \(H\) are \((1-c)/2\) and \((1+c)/2\), giving \(G_t\).

**Sharp coherence optimizer.** Differentiation on \((0,1)\) yields
\[
\frac{d}{dc}\log G_t(c)=\frac{h_t(c)}{(1-c)(1+c)(1+c^2)},
\qquad h_t(c)=1+(2t-5)c+c^2-(2t+1)c^3.
\]
The denominator is positive, \(h_t(0)=1\), and \(h_t(1)=-4\). For \(t=1\), \(h_1(c)=(1-3c)(1+c^2)\); for \(t=2\), \(h_2'(c)=-1+2c-15c^2<0\) on the real line. For every integer \(t\ge3\), the ordered coefficients of \(h_t\) have exactly one sign change, so Descartes' rule of signs gives at most one positive zero. Each case therefore has exactly one zero in \((0,1)\). Since \(G_t(1)=0\) by continuous extension and the derivative changes from positive to negative, this root is the unique global maximizer.

**Moving optimizer and sharp asymptotic.** The identity
\[
h_{t+1}(c)-h_t(c)=2c(1-c^2)>0\qquad(0<c<1)
\]
forces \(c_{t+1}>c_t\) by the uniqueness of the sign-changing zero. Thus \(c_t\) increases to some limit in \((0,1]\). Using \(h_t=h_1+2(t-1)c(1-c^2)\), a limit below one would make \(h_t(c_t)>0\) for large \(t\), a contradiction. Thus \(c_t\uparrow1\). At its zero,
\[
2(t-1)c_t(1+c_t)(1-c_t)=-h_1(c_t)\longrightarrow4,
\]
and therefore \(t(1-c_t)\to1\). In \(G_t\), the prefactor satisfies \(t(1-c_t)(1+c_t)^2/4\to1\), while \(((1+c_t^2)/2)^{t-1}\to\mathrm e^{-1}\), giving the asserted limiting constant. The stated value at \(t=1\) follows by substituting \(c_1=1/3\).

**Initial residual transition.** Because \(F_0=e_0^{\mathsf T}He_0\) and \(F_1=(1-c^2)e_0^{\mathsf T}(I-H)e_0/2\), the generalized Rayleigh quotient \(F_1/F_0\) is largest on the \((1-c)/2\) eigenvector of \(H\). The ratio there is \((1+c)^2/2\), which exceeds one exactly when \(c>\sqrt2-1\). After the first projection, the exact scalar recurrence already proved establishes all subsequent contraction claims.

## Verification

The accompanying standalone script `verify.py` uses only Python's standard library. Run `python3 verify.py`. It uses rationally parameterized pairs of unit row vectors, enumerates all independent choices for horizons \(1\) through \(7\), and tests the exact residual law for three initial errors. It also verifies the derivative identity with rational arithmetic, numerically tracks the critical cubic root through 500 horizons, and checks its asymptotic scale at four longer horizons. The exact finite enumeration supports but cannot replace the proofs for every real \(c\) and every integer \(t\).

## Relationship to prior work

Agaskar, Wang, and Lu (2014) obtain a general Kronecker-operator identity for expected squared *solution error* in randomized Kaczmarz; Bai and Wu (2018) establish additional exact mean-square-error representations and convergence estimates. Those frameworks can serve as starting points for fixed-system moment calculations. The new statement concerns a specific **different observable** (mean-row squared residual), its exact maximization over both initial error and all two-row geometries at every horizon, uniqueness and motion of the extremal coherence, the asymptotic sharp coefficient, and the residual-overshoot threshold.

Dereziński and Dong (2026, arXiv:2604.09909) investigate last-iterate residual guarantees for general stochastic contraction processes. Their later arXiv:2606.29593 proves a general last-iterate bound of order \(1/t\); therefore the *rate order* itself is not claimed as new. Neither analysis supplies the present two-row sharp value, optimizer, or transient threshold. Dereziński, Epperly, Needell, and Xue (2026, arXiv:2605.17185) treat numerical stability and iterative refinement of Kaczmarz, a distinct issue in finite precision.

## Limitations

The result does not cover unequal row probabilities, non-normalized rows without equivalent importance weighting, relaxed updates, more than two equations, nonhomogeneous inconsistent systems, or floating-point effects. The limiting coefficient \(1/\mathrm e\) concerns a minimax over two-row geometries that may change with the horizon; each fixed \(c<1\) converges geometrically. This work does not improve the known general \(1/t\) convergence order. A fully exhaustive historical search cannot be certified, and mathematically equivalent angular specializations of older moment-operator formulas may exist.

## References

1. M. Dereziński, X. Dong, *Last-Iterate Convergence of Randomized Kaczmarz and SGD with Greedy Step Size*, arXiv:2604.09909 (first submitted 10 April 2026), Sections 2–3 and appendices. https://arxiv.org/abs/2604.09909
2. M. Dereziński, E. N. Epperly, D. Needell, A. Xue, *Numerical Instabilities in the Kaczmarz Method and Stabilization by Iterative Refinement*, arXiv:2605.17185 (first submitted 16 May 2026), Sections 1–3; MSC 65F10. https://arxiv.org/abs/2605.17185
3. M. Dereziński, X. Dong, arXiv:2606.29593 (first submitted 28 June 2026), Theorem 3.1 and Section 3 (general \(1/t\) bound). https://arxiv.org/abs/2606.29593
4. A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities* (2014), Proposition 1. https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content
5. Z.-Z. Bai, W.-T. Wu, *On convergence rate of the randomized Kaczmarz method*, Linear Algebra and its Applications 553 (2018), 252–269, DOI:10.1016/j.laa.2018.05.009 (exact MSE analysis).

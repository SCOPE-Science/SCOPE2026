# An all-gain sampling transition and attracting two-cycles in a scalar feedback network

## Finding

A mixed advanced–retarded, piecewise-constant sampling mechanism has an exact **gain-independent stability region**: sampling after a computable fraction of the interval makes an entire class of monotone negative-feedback systems contractive for every finite feedback gain. Before that sampling threshold, the stability limit is sharp for the whole activation class. For the sigmoidal activation \(f(y)=\tanh y\), the limit is also a nonlinear bifurcation threshold: critical trajectories have inverse-square-root mesh decay, and each larger gain produces a locally attracting, antisymmetric two-cycle.

Write \(t_k=kh\), where \(a,b,h>0\), and let \(s\in[0,1)\). On each half-open sampling interval let

\[
 x'(t)=-a x(t)-b f\bigl(x(t_k+sh)\bigr),\quad t_k\le t<t_{k+1}.
\]

Assume throughout that \(f:\mathbb R\to\mathbb R\) is continuous, nondecreasing, globally Lipschitz with constant \(L>0\), and satisfies \(f(0)=0\). Introduce

\[
 \alpha=e^{-ash},\quad \beta=e^{-ah},\quad r=b/a,\quad d=2\alpha-1-\beta,
 \qquad s_*=\frac{1}{ah}\log\frac{2}{1+e^{-ah}}.
\]

Then \(d\le0\) exactly when \(s\ge s_*\). The equilibrium \(x\equiv0\) is globally exponentially attracting for every finite gain \(b\) whenever \(s\ge s_*\). If \(s<s_*\), the sufficient condition is exactly

\[
 rL<\frac{1+\beta}{d}.
\]

These are **sharp activation-uniform bounds**: when \(s<s_*\), the admissible linear function \(f(y)=Ly\) ceases to have exponential stability at equality and is unstable above it.

For \(f(y)=\tanh y\) and \(s<s_*\), put \(r_c=(1+\beta)/d\). Then the origin is globally exponentially attracting for \(r<r_c\), globally asymptotically attracting (not exponentially) for \(r=r_c\), and linearly unstable for \(r>r_c\). At the critical gain, any nonzero mesh trajectory that does not eventually hit zero satisfies

\[
 |x(t_k)|\sim(2c k)^{-1/2},\qquad
 c=\frac{(1+\beta)d^3}{3\alpha(1-\beta)^3}>0.
\]

For every \(r>r_c\) there is exactly one positive amplitude \(X\) generating an *antisymmetric* prime two-cycle \(X\mapsto-X\mapsto X\). It is defined by

\[
 X=\frac{1-\beta}{d}\,z,\qquad \frac{\tanh z}{z}=\frac{r_c}{r},\quad z>0.
\]

The equation uniquely determines \(z\), and the resulting orbit is locally exponentially attracting under the full sampled equation. Its birth amplitude is

\[
 X\sim\frac{1-\beta}{d}\sqrt{3\left(\frac r{r_c}-1\right)}\qquad(r\downarrow r_c).
\]

## Assumptions and scope

The equation uses the **same sampled value throughout each interval**. For \(0<s<1\) this value lies in the future during the first portion and in the past during the second. A solution is continuous across mesh points, continuously differentiable in the interiors, and has one-sided derivatives at mesh points. Its initial condition is a single real number \(x(0)\). The implicit future dependence is solved exactly and uniquely; no additional boundary condition or arbitrary continuation is needed. All exponential rates may depend on the fixed gain and sampling parameters. The two-cycle uniqueness refers only to antisymmetric cycles, not to every possible periodic orbit.

## Proof

**1. Exact well-posed mesh dynamics.** Let \(x_k=x(t_k)\) and \(z_k=x(t_k+sh)\). Integrating the linear in-interval differential equation gives

\[
 x(t_k+\tau)=e^{-a\tau}x_k-r(1-e^{-a\tau})f(z_k),\qquad0\le\tau\le h.
\]

Evaluating first at \(\tau=sh\) and then \(\tau=h\) yields

\[
 z_k+r(1-\alpha)f(z_k)=\alpha x_k,\qquad
 x_{k+1}=F(x_k)=\beta x_k-r(1-\beta)f(z_k).
\]

The left member of the equation for \(z_k\) is continuous, strictly increasing, and has limits \(\pm\infty\) at the two ends of the real line. It therefore has exactly one solution for every \(x_k\). Recursion constructs the unique global solution.

**2. A complete secant-multiplier formula.** For two different input mesh values, their sampled values are different. Put \(\sigma=[f(z_1)-f(z_2)]/(z_1-z_2)\in[0,L]\). Subtraction and elimination give the *exact* difference quotient

\[
 \frac{F(x_1)-F(x_2)}{x_1-x_2}
 =m(\sigma)=\frac{\beta-r(\alpha-\beta)\sigma}
                   {1+r(1-\alpha)\sigma}.
\]

Differentiation shows that \(m\) decreases strictly in \(\sigma\), because \(\alpha>0\), \(r>0\), and \(\beta<1\). Moreover \(m(0)=\beta\in(0,1)\), while

\[
 m(L)>-1\quad\Longleftrightarrow\quad
 1+\beta>rL(2\alpha-1-\beta)=rLd.
\]

If \(d\le0\), the strict inequality holds for all positive finite \(r\). If \(d>0\), it holds exactly below \(rL<(1+\beta)/d\). Thus the mesh map has a common Lipschitz contraction factor \(q=\max\{\beta,|m(L)|\}<1\); its unique fixed point is zero. In the interval interpolation, monotonicity of \(f\) implies \(|z_k|\le\alpha|x_k|\), so

\[
 \sup_{0\le\tau\le h}|x(t_k+\tau)|\le(1+rL\alpha)|x_k|,
\]

proving continuous-time global exponential convergence. Solving \(d=0\) proves the sampling cutoff \(s_*\). For \(f(y)=Ly\), the mesh map is exactly \(x_{k+1}=m(L)x_k\). At equality the multiplier is \(-1\) and beyond it is below \(-1\); hence the universal strict bound cannot be relaxed.

**3. The sigmoidal critical point.** Now take \(f(y)=\tanh y\) and \(d>0\). At zero the derivative is \(F'(0)=m(1)\), which moves from the interval \((-1,1)\) to \(-1\) at \(r=r_c\) and below \(-1\) thereafter. At \(r=r_c\), for every nonzero \(x\), the implicit sampled value \(z\) is nonzero and its secant slope to zero is \(\sigma=\tanh z/z\in(0,1)\). The strict monotonicity of \(m\) implies \(-1<m(\sigma)<\beta\), whence \(|F(x)|<|x|\). Therefore all mesh magnitudes decrease to zero: a positive limiting magnitude would contradict strict contraction at its accumulation point. The interpolation formula gives the same asymptotic attraction in continuous time.

The implicit equation is analytic near zero. Since \(\tanh z=z-z^3/3+O(z^5)\), writing \(D=1+r_c(1-\alpha)=\alpha(1-\beta)/d\) gives

\[
 F(x)=-x+\frac{r_c(1-\beta)\alpha^3}{3D^4}\,x^3+O(x^5)
 =-x+c x^3+O(x^5).
\]

For any orbit not eventually equal to zero, this implies

\[
 \frac1{|x_{k+1}|^2}-\frac1{|x_k|^2}=2c+O(|x_k|^2).
\]

The individual increments converge to \(2c\). Their Cesàro means therefore converge to \(2c\), giving \(|x_k|\sim(2ck)^{-1/2}\). In particular the critical fixed point is not exponentially attracting.

**4. Exact attracting nonlinear two-cycles.** The map is odd. Suppose \(X>0\) satisfies \(F(X)=-X\), and denote its sampled value by \(z>0\). Eliminating \(r\tanh z\) from the two mesh equations gives

\[
 r(1-\beta)\tanh z=(1+\beta)X,
 \qquad z=\frac{d}{1-\beta}X.
\]

Equivalently, \(\tanh z/z=r_c/r\). For \(z>0\), the function \(\tanh z/z\) decreases strictly and continuously from one to zero; hence it has one positive solution for every \(r>r_c\), none for \(r\le r_c\). It follows that the nonzero antisymmetric cycle exists and is unique in that class. Because \(\operatorname{sech}^2z<\tanh z/z\) for \(z>0\),

\[
 r\operatorname{sech}^2z<r_c,
 \qquad -1<m(\operatorname{sech}^2z)<\beta<1.
\]

The two-step multiplier is \(m(\operatorname{sech}^2z)^2<1\), proving local exponential attraction. The interpolation is also odd, producing a sign-reversing continuous trajectory with exact prime period \(2h\). Finally, \(\tanh z/z=1-z^2/3+O(z^4)\) yields the displayed square-root birth law.

## Verification

The standalone file `checker.py` is included and depends only on the Python standard library. Running `python checker.py` completes 2841 finite checks: exact rational secant identities, independent centered-difference derivatives, nonlinear two-cycle root equations and multipliers, and a long critical-orbit asymptotic test. The analytical inequalities and limit arguments above, not numerical convergence, establish the universal claims.

## Relationship to prior work

Oztepe and Karakoç (2026) study Hopfield-type networks with retarded piecewise constant arguments and conformable derivatives; their associated discrete systems and Lyapunov sufficient conditions motivate seeking sharp scalar tests. Chiu (2013) treats a broader impulsive mixed advanced–retarded neural system and proves sufficient global-exponential-stability conditions by a Gronwall inequality; those sufficient bounds do not give the present all-gain nonlinear interval or the stable two-cycle beyond an exact transition. Chiu, Pinto, and Jeng (2014) establish global convergence under sufficient hypotheses for recurrent neural systems with advanced and delayed arguments. Chiu and Jeng (2015) establish necessary-and-sufficient zero-stability results for scalar mixed-type arguments; the corresponding linear stability problem is antecedent, not presented as new here. The assessed contribution is the uniform **nonlinear monotone-feedback secant criterion**, its **sharp unbounded-gain sampling region**, and the **critical and supercritical sigmoidal dynamics**, not general existence, stepwise integration, or ordinary one-dimensional flip theory.

## Limitations

The model is scalar, has constant coefficients and a strictly periodic mesh, and assumes nondecreasing Lipschitz feedback with negative coupling. The bifurcation and critical-decay assertions are specific to hyperbolic-tangent activation. The nonlinear two-cycle is proved locally attracting, not globally attracting. The claim neither treats impulses nor network coupling across multiple neurons. The complete texts of the closely related Chiu–Jeng (2015) and Chiu–Pinto–Jeng (2014) articles were not accessible here, leaving residual historical-priority risk. No external independent audit has been performed.

## References

1. G. S. Oztepe and F. Karakoç, *Discrete-Time Stability Analysis of Neural Networks with Piecewise Constant Arguments*, Mathematics **14** (2026), article 2406, first publicly published 2026-07-05, DOI: https://doi.org/10.3390/math14132406. The article lists primary MSC2020 34D20.
2. K.-S. Chiu, *Existence and Global Exponential Stability of Equilibrium for Impulsive Cellular Neural Network Models with Piecewise Alternately Advanced and Retarded Argument*, Abstract and Applied Analysis (2013), article 196139, DOI: https://doi.org/10.1155/2013/196139.
3. K.-S. Chiu, M. Pinto, and J.-C. Jeng, *Existence and Global Convergence of Periodic Solutions in Recurrent Neural Network Models with a General Piecewise Alternately Advanced and Retarded Argument*, Acta Appl. Math. **133** (2014), 133–152, DOI: https://doi.org/10.1007/s10440-013-9863-y.
4. K.-S. Chiu and J.-C. Jeng, *Stability of Oscillatory Solutions of Differential Equations with General Piecewise Constant Arguments of Mixed Type*, Math. Nachr. **288** (2015), 1085–1097, DOI: https://doi.org/10.1002/mana.201300127.
5. K.-S. Chiu, *Existence and Global Exponential Stability of Periodic Solution for Cohen-Grossberg Neural Networks Model with Piecewise Constant Argument*, Hacettepe J. Math. Stat. **51** (2022), DOI: https://doi.org/10.15672/hujms.1001754.

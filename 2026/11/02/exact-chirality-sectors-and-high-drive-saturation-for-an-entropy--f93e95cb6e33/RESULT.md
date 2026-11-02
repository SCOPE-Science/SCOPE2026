# Exact chirality sectors and high-drive saturation for an entropy-optimal three-state cycle

## Finding

For a three-state continuous-time Markov jump process with fixed positive symmetric kinetic prefactors, fixed strictly positive instantaneous occupation probabilities, and a prescribed instantaneous probability velocity, the uniquely entropy-minimizing force is **exactly conservative on three explicit straight lines** in the two-dimensional velocity plane. Elsewhere its cycle affinity has a strict sign fixed by the sector and cannot change sign as the velocity is rescaled by any positive factor. Its weak-driving term is cubic, and along generic rays its large-driving limit is an explicit finite nonzero number in \((-2,2)\).

More precisely, orient the edges \(1\to2\), \(2\to3\), \(3\to1\). Fix \(p_i>0\) with \(\sum_i p_i=1\), and fixed \(\kappa_i>0\). Put \(\omega_i=\kappa_i\sqrt{p_i p_{i+1}}\), with cyclic indices. Given any \(b=(b_1,b_2,b_3)\in\mathbb R^3\) with \(\sum_i b_i=0\), define \(r=(-b_1,b_3,0)\), and the **linear-response current**
\[
L_i(b)=r_i-\frac{\sum_j r_j/\omega_j}{\sum_j1/\omega_j}.
\]
Let \(\mathscr A_*(b)\) be the sum of the three thermodynamic edge forces at the entropy-production minimizer. Then, for every \(b\),
\[
\mathscr A_*(b)=0\quad\Longleftrightarrow\quad L_1(b)L_2(b)L_3(b)=0,
\]
and whenever the product is nonzero,
\[
\operatorname{sgn}\mathscr A_*(b)=\operatorname{sgn}(L_1(b)L_2(b)L_3(b)).
\]
The three exceptional straight lines are
\[
\frac{b_1}{\omega_1}=\frac{b_3}{\omega_2},\qquad
\frac{b_2}{\omega_2}=\frac{b_1}{\omega_3},\qquad
\frac{b_2}{\omega_1}=\frac{b_3}{\omega_3}.
\]
They divide the velocity plane into six open sectors, with alternating signs of the optimal chirality. On each line, and only there, entropy minimization and conservative driving coincide **at every drive magnitude**.

For fixed \(\beta\) with \(\sum_i\beta_i=0\), the small-drive law is
\[
\mathscr A_*(\varepsilon\beta)
=\frac{\varepsilon^3}{8}\prod_{i=1}^{3}\frac{L_i(\beta)}{\omega_i}
+O(\varepsilon^5),\qquad \varepsilon\to0.
\]
If all three \(\beta_i\ne0\), let \(r=(-\beta_1,\beta_3,0)\), and order the offsets \(r_\ell<r_m<r_h\), retaining the associated edge weights \(\omega_\ell,\omega_m,\omega_h\). Define
\[
R=\frac{(r_h-r_m)/\omega_h}{(r_m-r_\ell)/\omega_\ell}>0.
\]
There is a unique real \(u\) satisfying \(u+\tanh u=-\log R\), and the exact strong-drive limit is
\[
\boxed{\lim_{\varepsilon\to\infty}\mathscr A_*(\varepsilon\beta)=-2\tanh u.}
\]
This identifies not only the universal sharp upper bound \(|\mathscr A_*|<2\) but the actual saturation value for each generic forcing direction and each edge-kinetic geometry. That bound itself was established in earlier work; the direction-specific limit is the contribution here.

## Assumptions and scope

At the chosen instant, the directed rates on edge \(i\to i+1\) and its reverse are \(k_{i,i+1}=\kappa_i e^{A_i/2}\) and \(k_{i+1,i}=\kappa_i e^{-A_i/2}\), respectively. The controlled antisymmetric mechanical force is \(A_i\in\mathbb R\). The instantaneous thermodynamic force and clockwise current are
\[
F_i=A_i+\log(p_i/p_{i+1}),\qquad J_i=2\omega_i\sinh(F_i/2).
\]
All \(\kappa_i,p_i\) are fixed while optimizing; occupation probabilities are strictly interior, and no bound is imposed on \(A_i\). The imposed instant velocity obeys \(b_1=J_3-J_1\), \(b_2=J_1-J_2\), \(b_3=J_2-J_3\). This is a pointwise current-allocation theorem, not a claim about globally optimal paths between fixed endpoints. The entropy production rate (in Boltzmann units) is \(\sigma=\sum_iJ_iF_i\). An edge-force configuration is conservative precisely when \(\sum_iA_i=\sum_iF_i=0\).

## Proof

**1. Existence, uniqueness, and the minimizer equation.** Every current satisfying the continuity equations is of the form \(J_i=r_i+c\) with \(r=(-b_1,b_3,0)\), where \(c\in\mathbb R\). The strictly convex objective is
\[
\sigma(c)=2\sum_i(r_i+c)\operatorname{arsinh}\left(\frac{r_i+c}{2\omega_i}\right).
\]
Its derivative and positive second derivative are
\[
\sigma'(c)=\sum_i\left[2\operatorname{arsinh}\left(\frac{J_i}{2\omega_i}\right)+\frac{2J_i}{\sqrt{J_i^2+4\omega_i^2}}\right],
\]
\[
\sigma''(c)=2\sum_i\frac{J_i^2+8\omega_i^2}{(J_i^2+4\omega_i^2)^{3/2}}>0.
\]
The first derivative tends to negative and positive infinity at the corresponding ends of the real line. Hence exactly one minimizer \(c_*(b)\) exists. With \(x_i=F_i^*/2=\operatorname{arsinh}(J_i^*/(2\omega_i))\) it satisfies
\[
\sum_{i=1}^{3}[x_i+\tanh x_i]=0.\tag{1}
\]
The unique minimizer, its force and its affinity depend continuously and smoothly on the prescribed velocity.

**2. Exact conservative cases.** If the optimal force is conservative, then \(\sum_i x_i=0\); (1) also gives \(\sum_i\tanh x_i=0\). With three real numbers summing to zero, the addition identity for \(\tanh\) gives
\[
\sum_i\tanh x_i=-\prod_i\tanh x_i.
\]
Thus one \(x_i\) is zero. The other two are opposites. Conversely, a triple of the form \((u,-u,0)\) in any cyclic order satisfies (1) and has vanishing affinity. Its edge currents satisfy one vanishing current and \(\sum_iJ_i/\omega_i=0\), since \(\sinh\) is odd. Their velocity determines the same solution as \(L(b)\) by uniqueness of the linear divergence problem. Equivalently the conservative cases are precisely \(\prod_iL_i(b)=0\). Substituting \(r=(-b_1,b_3,0)\) into \(L_i=0\) yields the three displayed straight lines. The lines are distinct because all three weights are positive.

**3. No chirality reversal.** On any open ray \(\varepsilon\beta\), \(\varepsilon>0\), the optimal affinity is continuous. Part 2 shows it has no zero unless that ray lies on an exceptional line, so its sign is constant along the ray. The sign is therefore established by the cubic small-drive term of Part 4. This proves the stated sign formula globally. Alternatively, strict subadditivity \(\tanh(a+b)<\tanh a+\tanh b\) for \(a,b>0\), applied to (1), shows directly that \(\operatorname{sgn}\sum_i x_i=\operatorname{sgn}\prod_i x_i\) when none vanish.

**4. Cubic expansion with its coefficient.** Put \(J_i=\varepsilon L_i(\beta)+O(\varepsilon^3)\) by the odd analytic implicit-function theorem applied to \(\sigma'(c)=0\), and let \(y_i=J_i/\omega_i\). Uniformly as all currents tend to zero,
\[
F_i=y_i-\frac{y_i^3}{24}+O(y_i^5),\qquad
2\tanh(F_i/2)=y_i-\frac{y_i^3}{8}+O(y_i^5).
\]
Consequently stationarity gives \(\sum_i y_i=\frac1{12}\sum_i y_i^3+O(\varepsilon^5)\), while the cycle affinity becomes \(\sum_iF_i=\frac1{24}\sum_i y_i^3+O(\varepsilon^5)\). Since \(\sum_iL_i/\omega_i=0\), the identity \(\sum_i z_i^3=3z_1z_2z_3\) for \(\sum_i z_i=0\) gives the stated coefficient \(1/8\). All error terms concern fixed positive weights and a fixed velocity direction.

**5. Strong-drive limit.** Suppose the three components of \(\beta\) are nonzero, so the offsets \(r_i\) are pairwise distinct. Write the minimizing common shift as \(c_*(\varepsilon\beta)=-\varepsilon r_m+z_\varepsilon\). The stationarity equation \(\sum_i h(\operatorname{arsinh}(J_i/(2\omega_i)))=0\), with \(h(x)=x+\tanh x\), is strictly increasing in \(z_\varepsilon\). For any fixed finite \(z\), the high- and low-offset contributions converge in sum to \(\log R\), since their divergent \(\pm\log\varepsilon\) terms and \(\pm1\) hyperbolic-tangent terms cancel. Thus the equation converges, uniformly for \(z\) on compact intervals, to
\[
h\left(\operatorname{arsinh}(z/(2\omega_m))\right)+\log R=0.
\]
This limiting function is strictly increasing from negative infinity to infinity, so bracketing the unique root establishes convergence \(z_\varepsilon\to2\omega_m\sinh u\), where \(h(u)=-\log R\). The sum of all three forces similarly converges to \(2u+2\log R=-2\tanh u\). This completes the high-drive classification. The earlier known strict cycle-affinity bound \(|\mathscr A_*|<2\) also follows directly from (1): \(\sum_iF_i=-2\sum_i\tanh x_i\) and the three-term structure, though its priority is not claimed here.

## Verification

The self-contained script `check_triangle.py` uses only the Python standard library and numerically solves the strictly monotone scalar minimizer equation by bisection. With deterministic pseudorandom test cases, it checks continuity, exact conservation-line conditions, six-sector sign agreement, the cubic coefficient, the generic large-drive limit, and a rational example; **5,007 deterministic assertions passed** with the script extracted from the package. The proof above is analytic and does not rely on finite sampling.

For example, take \(\omega_1=\omega_2=\omega_3=1\) and \(\beta=(-3,1,2)\). Then \(L=(4/3,1/3,-5/3)\), so \(\mathscr A_*(\varepsilon\beta)=-5\varepsilon^3/54+O(\varepsilon^5)\). The ordered offsets are \((0,2,3)\), giving \(R=1/2\) and limiting affinity approximately \(-0.67911256\). In particular this ray never changes chirality while its drive magnitude increases.

## Relationship to prior work

The nearest-neighbor three-state chain studied by Muratore-Ginanneschi, Mejía-Monasterio, and Peliti (2012/2013) has no triangular cycle and hence no cycle affinity. The fixed-kinetic-prefactor Markov-jump optimization, entropy-production formula, one-dimensional cycle-current stationarity equation, nonconservative optimum in general, cubic *order* of discrepancy, and absolute affinity bound were established previously, notably in Remlein–Seifert (2021), van der Meer–Dechant (2026), and Dechant–van der Meer (2026). They are not claimed as discoveries here. The present claim refines that setting by completely describing the conservative locus as three velocity-space lines for arbitrary edge prefactors and strictly positive occupations; giving a global no-reversal sign rule and its exact weak-drive coefficient; and establishing a direction-resolved strong-current limit. The 2026 near-optimality paper has a three-state numerical illustration for a restricted probability-transfer direction, but no equivalent complete sector classification or direction-resolved asymptotic was located in its available full text. The renormalized-entropy paper treats a different objective when identifying universally conservative minimizers; its original entropy derivative supplies the already known starting equation.

## Limitations

This theorem concerns the instantaneous entropy-production minimizer, not globally minimizing a time-integrated endpoint-to-endpoint protocol. Every occupation and kinetic prefactor must be strictly positive and held fixed during the pointwise optimization. The strong-drive formula excludes rays where a prescribed velocity component vanishes (offset ties), although the global sign and exceptional-line results apply there without modification. No physical force bounds are assumed. A general analytic implicit-root construction in prior literature implies parts of the result, and broader unpublished or unlocated treatments could subsume the classification; no independent priority audit has been performed. Numerical tests are not a proof of the continuum of parameter values.

## References

- P. Muratore-Ginanneschi, C. Mejía-Monasterio and L. Peliti, *Heat release by controlled continuous-time Markov jump processes*, first public 2012-03-19, https://arxiv.org/abs/1203.4062 .
- B. Remlein and U. Seifert, *Optimality of non-conservative driving for finite-time processes with discrete states*, first public 2021-03-15, https://arxiv.org/abs/2103.08376 .
- J. van der Meer and A. Dechant, *Near-optimality of conservative driving in discrete systems*, first public 2026-02-20, https://arxiv.org/html/2602.18321v2 .
- A. Dechant and J. van der Meer, *Renormalized entropy production for optimal transport in jump processes: Make conservative forces optimal again*, first public 2026-05-01, https://arxiv.org/abs/2605.00656 .

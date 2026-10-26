# Exact conservative flux-cap feasibility for Active Flux total variation

## Finding

Consider \(n\ge2\) periodic scalar cells, frozen shared endpoint data \(y_i\), provisional averages \(a_i\), and \(\lambda>0\). Set
\[
\ell_i=\min(y_{i-1},y_i),\quad u_i=\max(y_{i-1},y_i),\quad V_y=\sum_i|y_i-y_{i-1}|.
\]
For signed interface-flux corrections \(|f_i|\le d\), set the corrected averages \(m_i=a_i+\lambda(f_{i-1}-f_i)\). All indices are modulo \(n\). Define
\[
V(d)=\min_{|f_i|\le d}\sum_i\bigl(|m_i-y_{i-1}|+|y_i-m_i|\bigr),\quad d\ge0.
\]
For a label \(s\in\{-1,0,1\}\), let \(r_i(-1)=\ell_i-a_i\), \(r_i(0)=0\), and \(r_i(1)=a_i-u_i\). Then the **exact variational identity** is
\[
\boxed{V(d)=V_y+2\max_{s\in\{-1,0,1\}^n}\left[\sum_i r_i(s_i)-\lambda d\sum_i|s_i-s_{i+1}|\right].}
\]
The maximum, and hence the **smallest attainable Active Flux total variation**, is evaluable in \(O(n)\) scalar arithmetic operations by a three-state cyclic dynamic program. In particular, there exists a conservative flux correction with \(|f_i|\le d\) and final total variation at most a prescribed \(B\) **if and only if** \(V(d)\le B\).

There is a particularly simple sharp threshold for achieving the endpoint-imposed lower bound \(V_y\). Put \(A=\sum_i a_i\), \(L=\sum_i\ell_i\), and \(U=\sum_i u_i\). If \(A\notin[L,U]\), no finite or unbounded correction can attain \(V_y\). Otherwise the least permissible uniform correction cap is
\[
\boxed{d_*=\frac1{2\lambda}\max\left\{0,\max_{I\ \mathrm{proper\ cyclic\ interval}}\sum_{i\in I}(\ell_i-a_i),\max_{I\ \mathrm{proper\ cyclic\ interval}}\sum_{i\in I}(a_i-u_i)\right\}.}
\]
The interval maxima can be found in \(O(n)\) operations using prefix sums and a monotone sliding deque, with interval length in \(\{1,\ldots,n-1\}\).

More generally, for any budget \(B\ge V_y\) let \(t=(B-V_y)/2\), \(R_s=\sum_i r_i(s_i)\), and \(C_s=\sum_i|s_i-s_{i+1}|\). A finite correction cap attaining \(B\) exists exactly when \(t\ge\max\{0,A-U,L-A\}\); in that case its minimum is
\[
 d_B=\max_{s:C_s>0}\frac{(R_s-t)_+}{\lambda C_s},
\]
where a maximum over the empty set is zero. For arbitrarily large caps, \(\inf_{d\ge0}V(d)=V_y+2\operatorname{dist}(A,[L,U])\).

These are exact global feasibility conditions for the stated *post-endpoint-update algebraic flux-correction problem*, not a claim of automatic TVD for arbitrary PDE timestepping.

## Assumptions and scope

The mesh is periodic and uniform, with \(n\ge2\), scalar real-valued endpoint data and provisional averages, and \(\lambda=\Delta t/\Delta x>0\). The new point values \(y_i\) are fixed before flux optimization, and the \(f_i\) are independent signed numerical flux *corrections* bounded only by a common symmetric amplitude \(d\). The correction preserves the sum of averages, \(\sum_i m_i=A\). We impose no local consistency, positive-speed, parametrization, or CFL restrictions on the \(f_i\) beyond those stated. For finite-precision implementation, the mathematical equalities are exact-real statements; rational inputs permit exact-rational computations.

## Proof

**1. Separate the unavoidable endpoint variation.** For every real \(z\), \(|z-y_{i-1}|+|z-y_i|=|y_i-y_{i-1}|+2\operatorname{dist}(z,[\ell_i,u_i])\). Thus \(V(d)-V_y\) is twice the minimum over the correction cube of \(\sum_i\operatorname{dist}(a_i+\lambda(f_{i-1}-f_i),[\ell_i,u_i])\).

**2. Exact dualization.** The interval distance has the dual representation
\[
\operatorname{dist}(z,[\ell,u])=\max_{p\in[-1,1]}\{pz-u\max(p,0)-\ell\min(p,0)\}.
\]
The expression is affine in the flux variables and concave in \(p\). The compact convex minimax theorem (or finite-dimensional linear-programming duality) exchanges minimum over the flux cube and maximum over \(p\in[-1,1]^n\). Minimizing the flux term uses \(\min_{|f_i|\le d}\lambda f_i(p_{i+1}-p_i)=-\lambda d|p_{i+1}-p_i|\). This yields
\[
\frac{V(d)-V_y}{2}=\max_{p\in[-1,1]^n}\left\{\sum_i[p_i a_i-u_i\max(p_i,0)-\ell_i\min(p_i,0)]-\lambda d\sum_i|p_i-p_{i+1}|\right\}.
\]

**3. Ternary reduction (the nonstandard step).** For every \(p\in[-1,1]^n\) and \(h\in(0,1)\), define \(s_i(h)=1\) if \(p_i>h\), \(s_i(h)=-1\) if \(p_i<-h\), and zero otherwise. Layer-cake integration gives \(p_i=\int_0^1s_i(h)\,dh\), \(p_i^+=\int_0^1\mathbf1_{s_i(h)=1}\,dh\), and \(p_i^-= -\int_0^1\mathbf1_{s_i(h)=-1}\,dh\). Importantly, the exact discrete coarea identity is
\[
|p_i-p_{i+1}|=\int_0^1|s_i(h)-s_{i+1}(h)|\,dh.
\]
Consequently the dual objective at any \(p\) is the average of objective values at ternary labels \(s(h)\), and cannot exceed their maximum. Conversely every ternary label is permitted in the real dual cube. This proves the boxed variational identity without relaxing the optimization domain.

**4. Dynamic program.** For each of the three possibilities \(s_0=t\), initialize the score at the first site by \(D_0(t)=r_0(t)\) and the other scores as negative infinity. Continue for \(i=1,\ldots,n-1\) with
\[
D_i(s)=r_i(s)+\max_{q\in\{-1,0,1\}}\{D_{i-1}(q)-\lambda d|q-s|\}.
\]
The fixed-first-state cycle value is \(\max_s[D_{n-1}(s)-\lambda d|s-t|]\). Maximizing over the three starting states gives the claimed value. The state set is fixed, so running time is linear in \(n\), with constant working memory for values.

**5. Exact zero-extra-variation cutoff.** The boxed identity attains its lower bound \(V_y\) if and only if \(R_s\le\lambda dC_s\) for every ternary \(s\). Constant nonzero labels have \(C_s=0\) and enforce \(A\le U\) and \(A\ge L\). For every nonconstant label, the sets of positive and negative cells decompose into disjoint, proper cyclic intervals. The edge cost splits exactly as \(C_s=\sum_i|\mathbf1_{s_i=1}-\mathbf1_{s_{i+1}=1}|+\sum_i|\mathbf1_{s_i=-1}-\mathbf1_{s_{i+1}=-1}|\). Every proper cyclic interval has precisely two boundary edges. Therefore, the two families of interval inequalities in the boxed formula suffice for all labelings. They are also necessary by selecting a label equal to \(+1\), respectively \(-1\), on a single proper cyclic interval and zero elsewhere. Their sharp maximum is exactly \(d_*\). A maximum-sum proper cyclic interval on \(n\) sites can be determined from doubled prefix sums with an allowed prefix-index window of length at most \(n-1\), implemented via a monotone deque, in \(O(n)\) time.

**6. General TV budget and unlimited correction.** Requiring the ternary maximum to be at most \(t\) separates the three constant labels from labels with positive transition cost, yielding exactly the stated feasibility criterion and \(d_B\). Without a cap, each zero-sum perturbation of \(a\) is the cyclic discrete divergence of some \(f\). Thus the only constraint on the corrected means is \(\sum m_i=A\); minimizing the sum of distances to the intervals has value \(\operatorname{dist}(A,[L,U])\), by the triangle inequality and a construction distributing any allowable total across the intervals (placing remaining surplus or deficit at one cell).

**7. Collective-bottleneck example.** For \(n=2m\) with even-size alternation \(y_i=0,1,0,1,\ldots\), every interval \([\ell_i,u_i]=[0,1]\). Set \(a_i=2\) in \(m\) consecutive cells and \(a_i=-1\) in the remaining \(m\), so \(A=m\in[0,2m]\). For the proper interval containing the first \(m\) cells, \(\sum(a_i-u_i)=m\). No cyclic interval can have a larger positive excess in either orientation, hence \(d_*=m/(2\lambda)\). In contrast any isolated-cell excess is only one. Therefore local one-cell clipping misses a linearly growing global flux-cap obstruction.

## Verification

The standalone `verify.py` implements the ternary cyclic dynamic program and the cyclic interval threshold using exact rational arithmetic, independently enumerates every ternary label for instances of size at most eight, and compares the calculated minimal variation to a primal linear program using SciPy HiGHS. Its deterministic run checks 504 random rational instances for both identities and a six-size collective-bottleneck family. The recorded `verification_output.txt` is the output of running this exact included code. Enumeration verifies only those finitely many instances; the proof establishes the universal statements. A future implementation can separately backtrack the dynamic program and solve the primal LP to construct a minimizing flux, but the theorem only asserts existence and value.

## Relationship to prior work

Barsukow, *A TVD Active Flux method for scalar conservation laws* (arXiv:2610.05920v1, 2026), introduces the same Active Flux definition of variation (Definition 1, Eq. (5)), conservatively updates cell averages (Eq. (13)), and proves Harten-type sufficient conditions; the present statement instead fixes updated interface values and characterizes the exact reachable global TV under an abstract uniform bound on signed flux *corrections*. It is not a substitute for Barsukow's physical flux parameterization or sufficient stability theorem. Lu and Hochbaum (2021) give general-purpose algorithms for one-dimensional separable convex difference-penalty minimization; generic convex-programming theory applies to the optimization here, but their formulation does not give the ternary Active Flux value identity, the sharp cap/interval threshold, or the stated exact linear-time evaluation. Weiss, Blanc-Féraud and Aubert (2009) treat general constrained variation minimization with iterative convergence guarantees; no specific equality matching the endpoint-conditioned conservative correction criterion was identified in the accessible abstract. Classical max-flow/min-cut theory explains why interval bottlenecks should govern conservation on a cycle, but the specific full variation-budget identity and its three-state exact linear-time algorithm are distinct claims.

## Limitations

Only an algebraic, single-step, periodic and scalar *post-endpoint-update* correction is analyzed; arbitrary independent signed numerical flux corrections may not be realizable by a particular high-order time quadrature, PDE flux, positivity limiter, or third-order-accurate update. The result does not establish stability for repeated steps, convergence to a conservation-law solution, or a CFL condition. When \(A\notin[L,U]\), the no-extra-variation case is genuinely impossible, but larger budgets may still be feasible as described. The theoretical linear-time count assumes constant-cost exact real arithmetic; bit complexity and floating-point robustness are not bounded. A broader graph-cut or convex-duality presentation might implicitly recover some specialized formulas; see the attached review for the remaining originality risk.

## References

1. W. Barsukow, *A TVD Active Flux method for scalar conservation laws*, arXiv:2610.05920v1, first public 2026-10-05, https://arxiv.org/html/2610.05920v1 . Sections 1, 3 and 5, especially Definition 1, Eq. (5) and the conservative update Eq. (13).
2. C. Lu and D. S. Hochbaum, *A unified approach for a 1D generalized total variation problem*, Mathematical Programming 194 (2022), 415–442, first online 2021-03-13, https://doi.org/10.1007/s10107-021-01633-2 . Sections 1, 5 and 8.
3. P. Weiss, L. Blanc-Féraud and G. Aubert, *Efficient Schemes for Total Variation Minimization Under Constraints in Image Processing*, SIAM Journal on Scientific Computing 31 (2009), https://doi.org/10.1137/070696143 . Abstract examined.
4. L. R. Ford Jr. and D. R. Fulkerson, *Maximal Flow Through a Network*, Canadian Journal of Mathematics 8 (1956), 399–404; classical max-flow/min-cut correspondence.

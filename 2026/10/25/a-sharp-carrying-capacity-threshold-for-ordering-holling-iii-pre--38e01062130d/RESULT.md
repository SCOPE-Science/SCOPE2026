# A sharp carrying-capacity threshold for ordering Holling-III predator treatments

## Finding

For fixed \(r,K,b>0\), let a strictly positive prey population obey
\[
\dot x=r x(1-x/K)-u(t)\frac{x^2}{1+b x^2},\qquad x(0)>0.
\]
A treatment consists of a constant pressure \(u_i\geq0\) applied for a prescribed duration \(d_i>0\). Every member of a finite multiset of treatments must be used exactly once, without gaps or overlap, and the objective is to minimize the prey population immediately after all treatments. Put \(B=bK^2\).

**Sharp universal ordering theorem.** If \(B\leq27\), the arrangement with pressures in nondecreasing chronological order minimizes terminal prey for every strictly positive initial population and every assignment of positive durations; the reverse order maximizes it. If two adjacent distinct pressures are exchanged, the inequalities are strict. The condition \(B\leq27\) is sharp as a universal scheduling guarantee: if \(B>27\), any two distinct pressures \(0\leq u_-<u_+\) admit initial populations and arbitrarily short *equal* durations for which ordering \(u_-\) then \(u_+\) increases terminal prey relative to the reverse order, and other initial populations for which it decreases terminal prey.

For \(B>27\), the two short-treatment ordering reversals occur precisely at the two positive roots \(0<y_-<1/3<y_+<1/2\) of
\[
B y^2(1-2y)=1,\qquad y=x(0)/K.
\]
Weak-then-strong is inferior for initial densities \(K y_-<x(0)<K y_+\), but superior below \(K y_-\) and above \(K y_+\), for all sufficiently small equal positive treatment durations (at each fixed density away from the two roots). At the threshold \(B=27\), the roots merge at \(y=1/3\); for \(B=27+\varepsilon\) as \(\varepsilon\downarrow0\),
\[
y_\pm=\frac13\pm\frac{\sqrt\varepsilon}{27}+O(\varepsilon).\]
This is a local-duration phase classification above the threshold, not a claim that either order is optimal for arbitrary finite durations there.

## Assumptions and scope

The positive constants \(r\), \(K\) and \(b\) are common across all treatment blocks. The coefficient \(u_i\) is an externally maintained predator pressure, not a dynamically changing predator population; the Type-III intake per unit of pressure is \(x^2/(1+b x^2)\). Durations are carried with their associated pressures during a permutation. No treatment block is split. The endpoint objective is scalar prey abundance; neither treatment cost nor ecological long-term performance is optimized. Solutions exist globally, remain positive and bounded on every finite horizon, and respect scalar order in their initial value.

The dimensionless quantity \(B=bK^2=(K/H)^2\) compares prey carrying capacity to the Type-III half-saturation density \(H=1/\sqrt b\). The theorem applies to any finite number of blocks, including two. For the sharp converse, only two blocks of equal, sufficiently short positive duration are required.

## Proof

**1. Coordinate reducing pressure to an additive control.** Define
\[
z=\Psi(x)=b x-\frac1x,\qquad \Psi'(x)=\frac{1+b x^2}{x^2}>0.
\]
This is a smooth increasing bijection from \((0,\infty)\) to \(\mathbb R\). A direct chain-rule calculation gives
\[
\dot z=F(z)-u(t),\qquad F(\Psi(x))=r\frac{(1-x/K)(1+b x^2)}{x}.
\]
Differentiating with respect to \(z\),
\[
F'(\Psi(x))=r\frac{-1+b x^2(1-2x/K)}{1+b x^2}.
\]
For \(y=x/K>0\), the numerator has the sign of \(-1+B y^2(1-2y)\). On \(y\geq1/2\) it is negative. On \(0<y<1/2\), the function \(y^2(1-2y)\) increases to its unique maximum \(1/27\) at \(y=1/3\) and then decreases. Thus \(F\) is nonincreasing throughout \(\mathbb R\) exactly when \(B\leq27\). At equality \(B=27\), its derivative vanishes only at one \(z\), so \(F\) remains strictly decreasing as a function.

**2. Comparing ordered schedules.** Put \(U(t)=\int_0^t u(s)\,ds\) and \(w(t)=z(t)+U(t)\). Then \(\dot w=F(w-U(t))\). Consider two schedules with equal total integrated pressure \(U_1(T)=U_2(T)\) and \(U_1(t)\leq U_2(t)\) at every intermediate time. If \(F\) is nonincreasing, the scalar comparison theorem gives \(w_1(T)\leq w_2(T)\): at a possible first crossing where \(w_1=w_2\), the derivative of \(w_1\) is no larger because \(w_1-U_1\geq w_2-U_2\). The same conclusion follows from first-contact comparison on each smooth piece. Subtracting the equal totals proves \(z_1(T)\leq z_2(T)\), and monotonicity of \(\Psi^{-1}\) gives \(x_1(T)\leq x_2(T)\).

For two blocks of pressures \(u_-<u_+\), with any positive durations carried with their pressures, placing \(u_-\) first gives no greater cumulative integrated pressure at any prefix time than placing \(u_+\) first, while the final totals coincide. The inequality is strict at some intermediate times and, because \(F\) is strictly decreasing, the endpoint inequality is strict. Repeated adjacent exchanges (bubble sorting) prove the claimed minimum and maximum for every finite multiset, including unequal durations.

**3. Exact local order defect.** Let \(v_u(x)=r x(1-x/K)-u x^2/(1+b x^2)\), and let \(\varphi_u^\tau\) be its time-\(\tau\) flow. Define \(L\) as weak-then-strong, \(\varphi_{u_+}^{\tau}\!\circ\varphi_{u_-}^{\tau}\), and \(R\) as strong-then-weak. Taylor's theorem for smooth flows, uniformly on a compact neighborhood of each positive initial \(x\), gives
\[
L(x)-R(x)=\tau^2\big(v_{u_+}'(x)v_{u_-}(x)-v_{u_-}'(x)v_{u_+}(x)\big)+O(\tau^3).
\]
Writing \(g=r x(1-x/K)\) and \(h=x^2/(1+b x^2)\), the bracket equals \((u_+-u_-)(h'g-g'h)\), hence
\[
L(x)-R(x)=\tau^2(u_+-u_-)r\frac{x^2[-1+b x^2(1-2x/K)]}{(1+b x^2)^2}+O(\tau^3).
\]
Therefore for \(B>27\) the sign is negative outside, and positive inside, the interval \((K y_-,K y_+)\), as asserted. Each nonzero leading coefficient fixes the strict sign for all sufficiently small \(\tau>0\). The two roots follow from the unique maximum of \(y^2(1-2y)\). Writing \(y=1/3+s\) gives the exact identity \(y^2(1-2y)=1/27-s^2-2s^3\); substitution of \(B=27+\varepsilon\) yields \(s=\pm\sqrt\varepsilon/27+O(\varepsilon)\). This completes the sharp converse and square-root boundary law.

**4. Exact biologically suppressive example.** With \(r=K=1\), \(b=54\), \(u_-=20\), \(u_+=30\), and initial prey \(x(0)=1/3\), both instantaneous velocities are strictly negative:
\[
v_{20}(1/3)=-2/21,\qquad v_{30}(1/3)=-16/63.
\]
Nevertheless the weak-then-strong terminal population exceeds the strong-then-weak terminal population by
\[
\frac{10}{441}\tau^2+O(\tau^3)>0
\]
for all sufficiently small positive \(\tau\). Initial prey \(x(0)=1/12\) or \(x(0)=3/4\) reverses that ordering. The thresholds for these parameters are \(y_-=1/6\) and \(y_+=(1+\sqrt3)/6\), both in \((0,1/2)\).

## Verification

The standalone Python 3 program `verify.py` uses only the standard library. Execute `python3 verify.py` to reproduce exact rational identities for the derivative numerator, threshold and suppressive witness, and independent fourth-order Runge--Kutta integration checks. A completed run reported 11 exact rational checks; three step-refined order-reversal integrations; 600 seeded randomly chosen two-block instances; and 60 three-block instances with all six permutations compared. The numerical checks are finite sanity tests and are not the proof of the universal assertion, which is analytic above.

## Relationship to prior work

The classical Holling-III sigmoidal functional response and its ecological interpretation are established background. Jiang and Wang (2013) analyze a harvested *two-population* Holling-III system, including equilibria, periodic orbits and harvesting; their full open-access article was examined. It supplies biological motivation but does not supply an arrangement theorem for prescribed fixed predator-pressure blocks. Denny (2014) discusses the classical Holling response family and its Type-III form. Prakash and Vamsi (2025) analyze a different two-population, additional-food model and its prey-nullcline shape transition, including a coefficient 27. Thus neither the sigmoidal response nor the appearance of 27 in a prey-nullcline geometry is claimed as novel here: the claim is the **if-and-only-if universal chronological treatment ordering**, its strict finite-block comparison, and the short-duration reversal regions in the specified scalar control model. The 2025 optimal-control problem also differs in both dynamics and the endpoint functional.

Kar and Matsuda (2007), concerning controllability and harvest in a Holling-III prey--predator model, is a plausible nearby source. Its complete text could not be inspected; accessible descriptions suggest two-population dynamics rather than fixed-block scalar scheduling, but absence of coverage by the full text is *not* claimed. General scalar flow-comparison and Lie-bracket arguments are known techniques; their specialized consequence for Holling-III scheduling is the candidate contribution. Closest accessible mathematical-record comparisons include noninterchangeable Holling-II treatment scheduling and Holling-III periodic Gause harvest balances; neither directly implies this sharp prescribed-block result under the present assumptions.

## Limitations

This is an idealized single-prey model with externally held predator-pressure levels; predator dynamics and intervention costs are excluded. For \(B>27\), only the existence and density locations of local-duration reversals are proved, not a global optimal permutation for arbitrary durations. The sharp threshold belongs to the stipulated Holling-III functional form and logistic growth; changing either can change it. Numerical experiments do not establish the theorem. The incomplete historical comparison of Kar and Matsuda (2007), and potentially broader known scalar-flow rearrangement results, remain originality risks. This finding has received no independent mathematical audit.

## References

1. Jiang, Z. and Wang, L. (2013), *Qualitative analysis of a harvested predator-prey system with Holling type III functional response*. Advances in Difference Equations, article 249. DOI: 10.1186/1687-1847-2013-249 (public 2013-08-20).
2. Denny, M. (2014), *Buzz Holling and the Functional Response*. Bulletin of the Ecological Society of America 95, 200–203. DOI: 10.1890/0012-9623-95.3.200.
3. Prakash, P. and Vamsi, K. (2025), *Global dynamics and time-optimal control studies for additional food provided holling type-III mutually interfering prey-predator systems with applications to pest management*. Discover Applied Sciences. DOI: 10.1007/s42452-025-07255-z.
4. Kar, T. K. and Matsuda, H. (2007), *Global dynamics and controllability of a harvested prey-predator system with Holling type III functional response*. Nonlinear Analysis: Hybrid Systems. DOI: 10.1016/j.nahs.2006.03.002 (complete text not inspected).

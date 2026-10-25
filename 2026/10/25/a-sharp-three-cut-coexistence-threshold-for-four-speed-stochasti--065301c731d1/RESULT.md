# A sharp three-cut coexistence threshold for four-speed stochastic sorting

## Finding

**Theorem (sharp symmetric four-class sorting phase diagram).** In the continuous-time four-species exclusion sorting process with speed vector \((0,1,1+r,2+r)\), where \(r>0\), start from \(3^n2^n1^n0^n\), allow a faster particle immediately to the left of a slower one to interchange with rate equal to their speed difference, and stop on reaching \(0^n1^n2^n3^n\). Write \(N=4n\) and \(J_N\) for the ordered pair of types in the final interchange. Define

\[
 k(r)=\frac4r+\frac4{r+2},\qquad
 h(r)=\min_{0<z<1}\left(\frac1z+\frac1{1-z}+\frac1{r+1-z}+\frac1{r+2-z}\right).
\]

There exists exactly one \(r_*\in(107/100,27/25)\) solving \(k(r_*)=h(r_*)\), with \(r_*=1.075949895621008\ldots\). The following constitute one sharp classification:

- If \(0<r<r_*\), then \(\Pr(J_N=(2,1))\to1\).
- If \(r>r_*\), then \(\Pr(J_N=(1,0))\to1/2\) and \(\Pr(J_N=(3,2))\to1/2\); all other final-interchange types have limiting probability zero.
- At \(r=r_*\), all three cut-sorting times have the same macroscopic limit. The limiting total sorting-time coefficient is \(\max\{k(r),h(r)\}/4\), continuous but not differentiable at \(r_*\): its right derivative is strictly larger than its left derivative.

In particular, throughout \(1<r<r_*\), both boundary speed gaps are smaller than the central speed gap, yet the central interchange is the asymptotically unique final type. No claim is made about the probabilities of individual final-interchange types at the exactly critical value \(r=r_*\).

## Assumptions and scope

The fixed four species have precisely \(n\) particles each; \(r>0\) is fixed independently of \(n\). The order of species indicates increasing speed; a neighboring pair of types \(i>j\) in that order exchanges at exponential rate \(v_i-v_j>0\), and there are no exchanges in the opposite orientation. Time is continuous; the total particle count is \(N=4n\), not \(n\). Final interchange is almost surely a uniquely timed event because the finite-state continuous-time chain has nonzero finite rates.

For each \(m\in\{1,2,3\}\), let \(T_{N,m}\) be the first time every particle of types \(m,\ldots,3\) has passed every particle of types \(0,\ldots,m-1\). These crossing requirements are preserved after completion, and \(T_N=\max_m T_{N,m}\). If the final exchange involves types \(i>j\), precisely the cuts \(j<m\le i\) can have their completion times equal \(T_N\).

The proof uses the already established multispecies exclusion cut-time shape theorem [1] as its probabilistic input, and proves the optimization, uniqueness, transversality and final-swap symmetry analytically. This is not a new proof of the underlying inhomogeneous last-passage shape theorem.

## Proof

**1. Reduction to three scalar variational quantities.** The cut-time shape theorem [1, Theorem 1.2] gives, in probability (and under an appropriate coupling almost surely),

\[
 \frac{T_{N,m}}N\longrightarrow
 L_m(r)=\frac14\inf_{v_{m-1}<z<v_m}
 \left(\sum_{i<m}\frac1{z-v_i}+\sum_{i\ge m}\frac1{v_i-z}\right).
\]

The speed reflection \(v_i+v_{3-i}=2+r\) yields \(L_1=L_3=h/4\), with the displayed \(h\). The middle-cut objective is strictly convex and invariant under reflection about \(z=1+r/2\); its unique minimum is at that midpoint. The distances to the two middle speeds are each \(r/2\), and the distances to the outer speeds are each \((r+2)/2\). Hence \(L_2=k/4\).

**2. Exactly one crossing.** For fixed \(r>0\), let

\[
 g_r(z)=\frac1z+\frac1{1-z}+\frac1{r+1-z}+\frac1{r+2-z},\qquad 0<z<1.
\]

Because \(g_r''(z)>0\) and \(g_r(z)\to\infty\) at both endpoints, there is exactly one minimizer \(z_r\in(0,1)\), depending smoothly on \(r\). By differentiating at the minimizer,

\[
 h'(r)=-\frac1{(r+1-z_r)^2}-\frac1{(r+2-z_r)^2}>-\frac2{r^2},
\]

whereas \(k'(r)=-4/r^2-4/(r+2)^2<-4/r^2\). Therefore \((k-h)'<-2/r^2<0\). For \(r=1\), \(k(1)=16/3\), whereas \(h(1)\le g_1(1/2)=76/15<16/3\). For \(r=2\), \(k(2)=3\) whereas \(h(2)\ge4\), since \(1/z+1/(1-z)\ge4\). Thus a unique crossing \(r_*\in(1,2)\) exists, separating \(L_2>L_1=L_3\) from \(L_1=L_3>L_2\).

For the explicit rational bracket, put \(z_0=1/2\). At \(r=107/100\), exact fraction arithmetic gives \(k(r)>g_r(z_0)\ge h(r)\). At \(r=27/25\), convexity gives \(g_r''(z)\ge32\), since the second derivative of \(1/z+1/(1-z)\) is at least 32. The standard supporting-quadratic inequality implies \(h(r)\ge g_r(z_0)-g_r'(z_0)^2/64>k(r)\), where the last inequality is also an exact rational comparison. These establish \(107/100<r_*<27/25\); the decimal shown is reproducible by solving \(g_r'(z_r)=0\) and \(k(r)=g_r(z_r)\).

**3. Last-interchange phases.** If \(0<r<r_*\), the middle cut has a fixed strictly larger limit coefficient. Hence \(\Pr(T_{N,2}>\max(T_{N,1},T_{N,3}))\to1\). A final exchange crossing cut 1 or cut 3 would then force its cut time to equal the total time, impossible on this event; the final exchange therefore must be type 2 passing type 1.

If \(r>r_*\), the middle cut is strictly subdominant. Hence \(\Pr(T_{N,2}<T_N)\to1\). Any final exchange crossing the middle cut would contradict this strict inequality. Since the final exchange must complete at least one cut, its only remaining possibilities are type 1 passing type 0 and type 3 passing type 2.

Define an involution on configurations by reversing their spatial order and replacing each type \(i\) with \(3-i\). Both initial and final configurations are invariant. A neighboring exchange \((i,j)\mapsto(j,i)\), with \(i>j\), maps to \((3-j,3-i)\mapsto(3-i,3-j)\). Its rate is unchanged because \(v_{3-j}-v_{3-i}=v_i-v_j\). Thus the full path law is invariant, and the probabilities of the two edge final-exchange types are equal for every finite \(n\). Together with their combined probability tending to 1, each probability tends to \(1/2\).

**4. Critical cusp.** The limit of \(T_N/N\) is \(F(r)=\max\{k(r),h(r)\}/4\). It equals \(k(r)/4\) just left of \(r_*\) and \(h(r)/4\) just right. Both branches agree at the crossing, while \(h'(r_*)>k'(r_*)\); their one-sided derivatives are unequal and satisfy \(F'_+(r_*)>F'_-(r_*)\). At the crossing all three cuts have the same limiting coefficient by Step 1. This completes the theorem.

## Verification

Running `python3 verify.py` with the Python standard library replays the two exact-rational threshold inequalities, equality identities at parameters 1 and 2, a rate-preserving reflection involution on every four-type state, and high-precision nested bisection of the stationary-point equation and critical comparison. Its actual output appears in `verification_output.txt`. A numerical computation can corroborate but cannot replace the strictly monotone analytic argument or the probabilistic theorem used in Step 1.

## Relationship to prior work

Maga and Tóth [1] establish the cut-time variational limit for arbitrary strictly increasing speeds and give central-cut examples for equally spaced and geometrically spaced velocities. Their Theorem 1.2 already implies the existence of the first-order coefficients used above. The new analysis evaluates an entire unequal-gap speed family, proves an exact *unique triple-coexistence ratio*, its transverse cusp, and a *two-edge limiting half/half law* for the type of final interchange. These are not explicitly stated in [1] and require a global cut comparison and an exact reflection argument; the general variational formula is correctly credited rather than presented as new.

Bates et al. [2] study permutation invariance and the Busemann process of exponential last-passage percolation; their results underlie the suppression invariance used in [1]. Emrah, Janjigian and Seppäläinen [3] give the inhomogeneous corner-growth variational theorem used in [1]. Neither is used as evidence of an independent four-class sorting-phase theorem. The full text of [3] was not obtained in this review, so potential historical overlap through another formulation of the same optimization remains a limitation.

## Limitations

The critical-value conclusion identifies equality of the three *macroscopic* cut times, not equality of their finite-sample distributions and not the critical final-swap probabilities. Rates are symmetric and equal population sizes are assumed throughout. The probability limits are first-order large-population consequences; no fluctuation scaling, convergence rate, or extension to a nonsymmetric four-speed vector is asserted. The threshold classification mathematically refines the already known general variational formula; its originality is the sharp phase resolution and associated exchange probabilities, not a new stochastic-shape theorem. The precise critical value is defined by an optimization equation and presented numerically for convenience, not as an algebraic closed form.

## References

[1] B. Maga and B. Tóth, *Microscopic sorting in a multispecies exclusion process*, arXiv:2610.08135v1, first public 2026-10-06. https://arxiv.org/html/2610.08135

[2] E. Bates, E. Emrah, J. Martin, T. Seppäläinen, and E. Sorensen, *Permutation invariance in last-passage percolation and the distribution of the Busemann process*, arXiv:2506.12641, 2025; *Probability Theory and Related Fields*, 2026. https://link.springer.com/article/10.1007/s00440-026-01516-7

[3] E. Emrah, C. Janjigian, and T. Seppäläinen, *Flats, spikes and crevices: the evolving shape of the inhomogeneous corner growth model*, arXiv:1908.09319, 2019; *Electronic Journal of Probability* 26 (2021). https://arxiv.org/abs/1908.09319

# Three disjoint positivity windows for two-stage Radau IIA diffusion on unit stars

## Finding

Let \(K_{1,m}\) be the unweighted star with \(m\ge1\) leaves, \(L_m\) its combinatorial graph Laplacian, and \(T_m(h)\) the **endpoint** update of the two-stage, third-order Radau IIA method for \(u'=-L_mu\), with timestep \(h\ge0\). Then \(T_m(h)\) is entrywise nonnegative for every \(h\ge0\) if and only if \(1\le m\le10\).

For each integer \(m\ge11\), define
\[
 a_m=\frac{m-2-\sqrt{m^2-10m-2}}{m+1},\qquad
 b_m=\frac{m-2+\sqrt{m^2-10m-2}}{m+1}
\]
and the polynomial
\[
 P_m(h)=(m+1)h^4+(-2m^2+2m+10)h^3
 +(6m^2+4m+16)h^2+(24m+12)h+36.
\]
It has exactly two positive roots \(c_m,d_m\), satisfying \(3<c_m<8<d_m\). The **entire**, sharp endpoint-positivity set is
\[
 \{h\ge0:T_m(h)\ge0\text{ entrywise}\}
 =[0,a_m]\cup[b_m,c_m]\cup[d_m,\infty).
\]
Here \(0<a_m<b_m<2<3<c_m<8<d_m\), so all three intervals are nonempty and separated by two genuine open positivity-failure intervals. The smallest star displaying these three separate windows has **twelve vertices** (eleven leaves). Its first forbidden interval is \((1/2,1)\); its second is \((6.068411604\ldots,11.764257595\ldots)\). This result concerns nonnegative end-of-step states for **every** nonnegative initial vector, not positivity of individual internal stages.

## Assumptions and scope

The graph is a simple undirected, unit-conductance star with one hub and \(m\) leaves, and \(L_m=D-A\) uses the usual nonnegative diagonal-degree convention. The heat generator is \(-L_m\). The two-stage Radau IIA tableau is
\[
\begin{array}{c|cc}
1/3&5/12&-1/12\\
1&3/4&1/4\\ \hline
 &3/4&1/4
\end{array}
\]
with scalar stability function
\[
R(z)=\frac{1+z/3}{1-2z/3+z^2/6},\qquad
r(t)=R(-t)=\frac{6-2t}{t^2+4t+6}.
\]
For every real \(h\ge0\), the denominator matrix \(I+(2h/3)L_m+(h^2/6)L_m^2\) is invertible because \(L_m\) is positive semidefinite. The update is
\[
T_m(h)=R(-hL_m)=\bigl(I-\tfrac h3L_m\bigr)
 \bigl(I+\tfrac{2h}3 L_m+\tfrac{h^2}6L_m^2\bigr)^{-1}.
\]
Entrywise nonnegativity is equivalent to preserving the nonnegative orthant for every nonnegative starting vector; row and column sums of \(T_m(h)\) are one for every step, whether or not it is nonnegative.

## Proof

Write \(n=m+1\), name the hub \(0\), and label leaves \(1,\ldots,m\). The spectrum of \(L_m\) is \(0\) (one dimension), \(1\) (multiplicity \(m-1\), absent when \(m=1\)), and \(n\) (one dimension). The corresponding orthogonal projections are
\[
 E_0=\frac1n\mathbf1\mathbf1^{\mathsf T},\quad
 E_n=\frac1{nm}(m,-1,\ldots,-1)^{\mathsf T}(m,-1,\ldots,-1),\quad
 E_1=I-E_0-E_n.
\]
Thus \(T_m(h)=E_0+r(h)E_1+r(nh)E_n\). There are precisely four symmetry-types of entries (the leaf-off-diagonal type is absent when \(m=1\)):
\[
\begin{aligned}
C_m(h)&=(T_m)_{00}=\frac{1+m r(nh)}n,\\
H_m(h)&=(T_m)_{0i}=(T_m)_{i0}=\frac{1-r(nh)}n,\\
D_m(h)&=(T_m)_{ii}=\frac1n+\frac{m-1}m r(h)+\frac{r(nh)}{mn},\\
F_m(h)&=(T_m)_{ij}=\frac1n-\frac1m r(h)+\frac{r(nh)}{mn},\quad i\ne j\ge1.
\end{aligned}
\]
Put \(U(h)=h^2+4h+6\) and \(V_m(h)=n^2h^2+4nh+6\); both are strictly positive for \(h\ge0\). Directly clearing denominators yields
\[
 C_m(h)=\frac{Q_m(h)}{V_m(h)},\qquad
 Q_m(h)=nh^2+(4-2m)h+6,
\]
\[
 D_m(h)=\frac{P_m(h)}{U(h)V_m(h)},\qquad
 F_m(h)=\frac{h^2\bigl(nh^2+(6m+12)h+18\bigr)}{U(h)V_m(h)}.
\]
The formula for \(H_m\) is positive for \(h>0\), because \(r(t)<1\) for \(t>0\); the formula for \(F_m\) is positive for \(h>0\). Hence exactly two diagonal types can obstruct positivity.

Differentiate \(r\):
\[
 r'(t)=\frac{2(t^2-6t-18)}{(t^2+4t+6)^2}.
\]
It has its global minimum on \([0,\infty)\) at \(t_*=3+3\sqrt3\), with value \(r_*=\frac{5-3\sqrt3}{2}\). Both diagonal formulas satisfy the common lower bound
\[
 C_m(h),D_m(h)\ \ge\ \frac{1+m r_*}{m+1}.
\]
For \(D_m\), this follows by adding its two nonconstant coefficients, \((m-1)/m+1/(mn)=m/n\). Since \(-1/r_*=5+3\sqrt3\in(10,11)\), this proves strict diagonal positivity and thus endpoint positivity for every \(1\le m\le10\), at every \(h\ge0\).

Now let \(m\ge11\). The discriminant of \(Q_m\) is \(4(m^2-10m-2)>0\), and its two positive roots are exactly \(a_m,b_m\). Since \(Q_m(0)=6>0\), \(Q_m(1)=11-m\le0\), \(Q_m(2)=18>0\), and its vertex lies to the left of one, \(0<a_m\le1\le b_m<2\), with strict \(a_m<b_m\). Consequently \(C_m(h)<0\) precisely on \((a_m,b_m)\).

For the other diagonal, \(r(h)\ge0\) throughout \([0,3]\). Since \(r(nh)\ge r_*>-1\), the expression
\[
 D_m(h)=\frac{1+r(nh)/m}{m+1}+\frac{m-1}{m}r(h)
\]
is strictly positive on \([0,3]\). At \(h=8\), clearing the positive denominators gives
\[
 P_m(8)=-4(160m^2-1392m-2593)<0\quad(m\ge11),
\]
where the quadratic in parentheses is positive at \(m=11\) and increasing for all \(m\ge11\). Finally, \(P_m(h)\) is positive for all sufficiently large \(h\), since its leading coefficient is \(m+1>0\). Its coefficient signs in decreasing order are \((+,-,+,+,+)\) for \(m\ge11\); Descartes' rule of signs gives at most two positive roots counted with multiplicity. The strict signs at \(h=3,8\), and for large \(h\) force exactly two distinct simple positive roots, \(3<c_m<8<d_m\), with \(D_m(h)<0\) precisely on \((c_m,d_m)\). These two forbidden intervals are disjoint because \(b_m<2<3<c_m\). The stated union and the sharpness of every endpoint follow.

For \(m=11\), \(Q_{11}(h)=6(2h-1)(h-1)\) and \(P_{11}(h)=6(2h^4-35h^3+131h^2+46h+6)\), giving the quoted threshold and numerical root approximations. The latter approximations are illustrative, not part of the exact proof.

## Verification

The standalone `verify.py` separately forms the Radau IIA rational matrix function and solves its linear systems using exact `fractions.Fraction` Gaussian elimination. It compares the entire update matrix with the four spectral entry expressions on \(192\) star/timestep combinations (\(1\le m\le16\), twelve rational timesteps each); every matrix has exact unit row sums, and the asserted signs are checked. Additional integer polynomial assertions cover \(11\le m\le1000\). All infinite-range assertions in this theorem are proved by the inequalities and Descartes argument above, **not** by the finite computations. Run `python3 verify.py`; only the Python standard library is needed.

## Relationship to prior work

The Radau IIA tableau and rational stability function are standard and tabulated by Ketcheson. Horváth's 1998 analysis derives general Runge–Kutta positivity radii, and his 2005 study explicitly tests the *two-stage Radau IIA* method on a one-dimensional Dirichlet heat discretization, establishing class-wide restrictions and positivity for selected smooth initial data. Neither its general bounds nor its restricted-cone results imply the complete all-initial-data positivity intervals on unit stars. The 2003 NUMDIFF-10 abstract of the latter work likewise discusses Radau IIA but not star-specific disconnected timestep windows. Hairer and Lubich analyze energy dissipation and Radau IIA eigenmode damping, without star-specific entrywise nonnegativity intervals. Blanes, Iserles and Macnamara explain why high-order standard numerical integrators generally face positivity obstacles on graph-Laplacian systems and construct different positivity-preserving schemes. The present result is a sharp *graph- and method-specific end-step* classification, neither a statement about energy contraction nor a claim of unconditional positivity for arbitrary graph generators. Relevant published comparisons are reported separately in `REVIEW.md` and `AUDIT.json`.

## Limitations

Only unit-edge undirected stars, a fixed two-stage Radau IIA endpoint map, and all-orthant entrywise positivity are covered. Internal RK stages need not be positive. The result makes no claim about arbitrary weighted stars, other graph families, variable timesteps, nonlinear equations, or higher-stage Radau schemes. An entrywise nonnegative large-timestep update does not imply accuracy at that timestep. Identical statements in unindexed literature remain a possible originality risk; no independent audit has occurred.

## References

1. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, doi:10.1016/S0168-9274(98)00050-6.
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, first online 2004-10-27, doi:10.1016/j.apnum.2004.08.026.
3. Z. Horváth, *On the positivity step-size threshold of Runge–Kutta methods*, NUMDIFF-10 abstract (2003), printed pp.25–26, https://sim.mathematik.uni-halle.de/numdiff10/heft.pdf.
4. E. Hairer and C. Lubich, *Energy-diminishing integration of gradient systems*, IMA Journal of Numerical Analysis 34 (2014), 452–461; first online 2013-10-03, doi:10.1093/imanum/drt031. Author preprint: https://www.unige.ch/~hairer/preprints/gradientflow.pdf.
5. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, Mathematical Modelling and Numerical Analysis; first arXiv version dated 2021-02-16, arXiv:2102.08242, https://arxiv.org/pdf/2102.08242.
6. D. I. Ketcheson, *Numipedia: Radau IIA2*, https://ketch.github.io/numipedia/methods/RadauIIA2.html (method tableau and stability function; undated web reference).

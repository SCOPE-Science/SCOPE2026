# Sharp invariant-interval and reentrant step-size frontiers for a doubly stabilized Allen–Cahn step

## Finding

For the homogeneous Allen–Cahn equation \(\dot u=u-u^3\), the doubly stabilized Crank–Nicolson method of Hou, Ju, and Qiao has an exact necessary-and-sufficient condition for preserving the physical interval \([-1,1]\). Write the first stabilization parameter as \(s\ge 2\), the second as \(v\ge0\), and the time step as \(h>0\). The one-step map preserves \([-1,1]\) for **every** input in that interval if and only if
\[
Q_{s,v}(h)=4+4(s-2)h+(s^2-8s+8)h^2+2vh^2(2+sh)\ge0.
\]
If the inequality fails, an open set of inputs arbitrarily close to \(1\) is mapped above \(1\). If it holds, every nonzero interior input moves strictly toward the equilibrium of the same sign, and repeated fixed-step iteration converges to that equilibrium.

The criterion has an exact stabilization and time-step phase diagram. Set \(s_c=4+2\sqrt2\). For \(s\ge s_c\), **first stabilization alone**, with \(v=0\), preserves the interval for all positive steps. For \(2\le s<s_c\) and \(v=0\), preservation holds precisely for
\[
0<h\le H_s=\frac{2}{2\sqrt{s-1}-(s-2)}.
\]
For \(2\le s<s_c\) and \(v>0\), let \(c_s=8s-s^2-8>0\), \(b_s=4(s-2)\), and let \(t_s>0\) be the unique positive root of
\[
16t^3+(20s-16)t^2+8s(s-2)t-sc_s=0.
\]
Define the exact second-stabilization threshold
\[
v_*(s)=\frac{t_s(c_s-b_st_s-4t_s^2)}{2(s+2t_s)}>0.
\]
If \(v\ge v_*(s)\), every positive step preserves the interval. If \(0<v<v_*(s)\), there are **exactly two positive** roots \(h_-(s,v)<h_+(s,v)\) of \(Q_{s,v}(h)=0\); preservation holds for \(h\in(0,h_-]\cup[h_+,\infty)\), but fails for every step strictly between the roots. Thus sufficiently small **and sufficiently large** steps are safe while intermediate steps violate the physical bound. In particular \(v_*(2)=1/4\).

## Assumptions and scope

The scalar problem is the spatially homogeneous, unit-mobility, unit-reaction-scale reduction of \(\partial_t\phi=\varepsilon^2\Delta\phi+\phi-\phi^3\). Constant spatial states are preserved by the central-difference Laplacian with periodic or homogeneous Neumann boundary conditions. No assertion of sufficient interval preservation for nonconstant spatial states is made.

Use the exact linear method in equations (2.11a)–(2.11b) of Hou–Ju–Qiao, with a stabilized half-step followed by the doubly stabilized Crank–Nicolson endpoint. Writing the input as \(u\), the stage and endpoint are, respectively,
\[
m=u+\delta u(1-u^2),\qquad\delta=\frac{h}{2+sh},\qquad
\Phi_{h,s,v}(u)=\frac{(a-s/2)u+(s+1)m-m^3}{a+s/2},\quad a=\frac1h+vh.
\]
These are exact-arithmetic equations, with \(s\ge2\), \(v\ge0\), \(h>0\), and \(u\in[-1,1]\). The denominator is strictly positive. The interval property means \(\Phi_{h,s,v}([-1,1])\subseteq[-1,1]\), not just that a particular numerical trajectory remains bounded.

## Proof

**Step 1: derive the source method.** For homogeneous input, the source BDF1 half-step equation is
\[
\frac{2(m-u)}h+(u^3-u)+s(m-u)=0,
\]
which gives the stated \(m\). The doubly stabilized endpoint solves
\[
\frac{\Phi-u}h+(m^3-m)+s\left(\frac{\Phi+u}{2}-m\right)+vh(\Phi-u)=0,
\]
so rearrangement gives the formula for \(\Phi\). The map is odd, and \(-1,0,1\) are fixed points.

**Step 2: locate the true worst input.** On \(0<u<1\), \(0<\delta<1/s\le1/2\) and hence \(0<u<m<1\). Direct subtraction yields
\[
\Phi(u)-u=\frac{s(m-u)+m-m^3}{a+s/2}>0.
\]
Define \(e(u)=\delta u(1+u)\). Then \(m=u+(1-u)e\). Factoring the increment gives the exact identity
\[
\Phi(u)=u+\frac{1-u}{a+s/2}R(u),\quad
R(u)=se(u)+m(u)(1+m(u))(1-e(u)).
\]
On \([0,1]\), one has \(0\le e\le2\delta<1\), \(0\le m\le1\), and
\[
e'(u)=\delta(1+2u)>0,\qquad
m'(u)=1+\delta(1-3u^2)\ge1-2\delta>0.
\]
Consequently,
\[
R'(u)=\bigl(s-m(1+m)\bigr)e'(u)
 +(1-e)(1+2m)m'(u)>0,
\]
because \(s\ge2\ge m(1+m)\). Therefore \(R\) attains its maximum at \(u=1\), where
\[
R(1)=2+2(s-2)\delta.
\]
The entire positive half-interval is invariant exactly when \(a+s/2\ge R(1)\). Multiplying the difference by the strictly positive factor \(2h(2+sh)\) yields \(Q_{s,v}(h)\) exactly. Oddness gives invariance of the negative half-interval. If \(Q<0\), then \(a+s/2<R(1)\), so continuity makes \(\Phi(u)>1\) for every sufficiently close \(u<1\), providing strict counterexamples. More explicitly,
\[
\Phi'(1)=\frac{Q_{s,v}(h)}{2h(2+sh)(a+s/2)}.
\]
The strict inward motion on \((0,1)\), the absence of interior nonzero fixed points, and interval preservation imply convergence to \(1\) under repetition; oddness gives convergence to \(-1\) from negative inputs. No convergence claim is made if the interval criterion fails.

**Step 3: classify the time steps.** Let \(c_s=8s-s^2-8\) and \(b_s=4(s-2)\). Then
\[
Q_{s,v}(h)=4+b_sh-c_sh^2+2vh^2(2+sh).
\]
For \(s\ge s_c\), \(c_s\le0\), so every term in this expression is nonnegative. For \(2\le s<s_c\), \(c_s>0\) and the equation \(4+b_sh-c_sh^2=0\) has exactly one positive root \(H_s\); rationalizing the quadratic formula gives the displayed closed form.

For \(s<s_c\), define
\[
F_s(h)=\frac{c_sh^2-b_sh-4}{2h^2(2+sh)}.
\]
Then \(Q_{s,v}(h)\ge0\) exactly when \(v\ge F_s(h)\). The function is negative before \(H_s\), strictly positive after it, and approaches \(0\) from above as \(h\to\infty\). With \(t=1/h\), write
\[
G_s(t)=F_s(1/t)=\frac{t(c_s-b_st-4t^2)}{2(s+2t)}.
\]
Its derivative has positive denominator \(2(s+2t)^2\) and numerator
\[
sc_s-2sb_st-(20s-16)t^2-16t^3.
\]
The numerator is strictly decreasing on \(t>0\), is positive at zero and tends to negative infinity; it has precisely one positive root \(t_s\), which must belong to \((0,1/H_s)\). Thus \(G_s\) has a unique positive maximum there. Comparing \(v\) with that maximum proves the two-root reentrant classification, including equality endpoints and the unconditional threshold. Substituting \(s=2\) shows \(t_s=1/2\) and \(v_*(2)=1/4\). This completes all asserted parameter ranges.

## Verification

The standalone standard-library program `verify.py` checks the original two stage equations and the closed map independently with exact rational arithmetic. It checks the polynomial equivalence, odd symmetry, representative safe/unsafe inputs, the critical boundary \((s,v,h)=(2,1/4,2)\), and the reentrant and large-stabilization regimes. Successful execution produces:

`VERIFY_OK: 1200 exact CN/stage/criterion tests, 9999 boundary tests, phase and rational witnesses`

An entirely explicit violating instance is \(s=4\), \(v=0\), \(h=2\), \(u=9/10\), for which
\[
\Phi_{2,4,0}(9/10)=\frac{313211996289}{312500000000}>1.
\]
The finite verification is not presented as a proof of the universal result; the preceding monotonicity and cubic-root arguments are the proof.

## Relationship to prior work

Hou, Ju, and Qiao introduce the *same* half-step and doubly stabilized endpoint in their 2023 preprint (equations (2.11a)–(2.11b)); these formulas and their sufficient maximum-bound theorem are credited. Their Theorem 2.1 supplies a sufficient condition \(S_2\ge(S_1/4+\varepsilon^2/h_{\rm grid}^2)^2\), or a small-step alternative when \(S_2=0\), for the full spatially discretized equation. The exact scalar necessity/sufficiency, large-\(S_1\) zero-\(S_2\) regime, and intermediate-step failure interval are not consequences of their sufficient bound, nor do their equations assert them as results.

Earlier stabilized Crank–Nicolson/Adams–Bashforth discretizations use a different extrapolation mechanism and generally a two-step recurrence; they do not specialize to the midpoint BDF1/CN map used here. The exact criterion supplies a **necessary** condition for any claim of uniform maximum-bound preservation for the full discrete method on a periodic/Neumann grid, because spatially constant input vectors reduce to the scalar map. It is *not* a sufficient condition for spatially nonconstant input vectors.

## Limitations

Only scalar constant-mobility, homogeneous modes of the specified source method are classified. The theorem does not prove PDE gridwise maximum-bound preservation at its improved thresholds, energy dissipation, local/global error bounds, or optimal behavior for alternative discretizations. The originality assessment is a documented best-knowledge comparison, not a claim that mathematically equivalent results cannot exist outside the inspected literature.

## References

- D. Hou, L. Ju, and Z. Qiao, *A linear doubly stabilized Crank-Nicolson scheme for the Allen-Cahn equation with a general mobility*, arXiv:2310.19663v1, first submitted 2023-10-30; original method (2.11a)–(2.11b), Theorem 2.1. https://arxiv.org/html/2310.19663v1
- D. Hou, L. Ju, and Z. Qiao, *Advances in Applied Mathematics and Mechanics* **16** (2024), 1009–1038, DOI:10.4208/aamm.OA-2023-0067.
- T. Hou and H. Leng, *Numerical analysis of a stabilized Crank–Nicolson/Adams–Bashforth finite difference scheme for Allen–Cahn equations*, *Applied Mathematics Letters* **102** (2020), 106150, DOI:10.1016/j.aml.2019.106150; a distinct two-level algorithm.
- X. Feng, T. Tang, and J. Yang, *Stabilized Crank–Nicolson/Adams–Bashforth schemes for phase field models*, *East Asian Journal on Applied Mathematics* **3** (2013), 59–80, DOI:10.4208/eajam.200113.220213a; a distinct earlier scheme.

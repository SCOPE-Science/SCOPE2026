# A redundant predation-strength condition in a multi-prey Holling-II extinction theorem

## Finding
Consider the dimensionless multiple-prey Holling-II model
\[
\dot x_i
= a_i x_i(1-x_i)-\frac{p_i x_i y}{1+\sum_{j=1}^n b_jx_j},
\qquad i=1,\ldots,n,
\]
\[
\dot y
= y\left(\frac{\sum_{j=1}^n c_jx_j}{1+\sum_{j=1}^n b_jx_j}-1\right),
\]
with \(a_i,p_i,b_i>0\) and \(c_i\ge0\). Suppose
\[
0\le c_i\le b_i\qquad(i=1,\ldots,n).
\]
Then for every solution with \(x_i(0)>0\) for all \(i\) and \(y(0)\ge0\),
\[
(x_1(t),\ldots,x_n(t),y(t))\longrightarrow(1,\ldots,1,0).
\]
In particular, the predator-free equilibrium is globally asymptotically stable in the positive-prey state space without any restriction on the predation coefficients \(p_i\) relative to the prey growth coefficients \(a_i\).

This strengthens Theorem 4 of Fatah, Mustafa, and Amin, whose sufficient hypotheses are the strict componentwise inequalities \(c_i<b_i\) together with
\[
p_i^2<4a_i\qquad(i=1,\ldots,n).
\]
The second family of inequalities is unnecessary, and equality \(c_i=b_i\) is also allowed.

More quantitatively, set
\[
M_i=\max\{1,x_i(0)\},\qquad
D_\max=1+\sum_{i=1}^n b_iM_i.
\]
Then
\[
y(t)\le y(0)e^{-t/D_\max}.
\]

## Assumptions and scope
The statement concerns system (2) in Fatah, Mustafa, and Amin, with the parameters and dimensionless variables used there. The convergence assertion is made for strictly positive prey coordinates \(x_i(0)>0\); this restriction is necessary because every face \(x_i=0\) is invariant, so a solution starting with a missing prey class cannot converge to \(x_i=1\).

The predator initial value may be zero. When \(y(0)=0\), the predator remains absent and each prey coordinate follows its logistic equation. No condition is imposed on the size of \(p_i\), beyond positivity.

## Proof
Write
\[
D(t)=1+\sum_{j=1}^n b_jx_j(t).
\]
Because \(c_i\le b_i\) and \(x_i\ge0\),
\[
\sum_{i=1}^n c_ix_i\le\sum_{i=1}^n b_ix_i=D-1.
\]
Therefore the predator per-capita growth rate satisfies
\[
\frac{\dot y}y
=\frac{\sum_i c_ix_i}D-1
\le\frac{D-1}D-1
=-\frac1D.
\]
For each prey coordinate,
\[
\dot x_i\le a_ix_i(1-x_i),
\]
so scalar comparison with the logistic equation gives
\[
0<x_i(t)\le M_i=\max\{1,x_i(0)\}.
\]
Consequently \(D(t)\le D_\max\), and hence
\[
\dot y\le-\frac1{D_\max}y.
\]
Gronwall's inequality yields
\[
y(t)\le y(0)e^{-t/D_\max},
\]
so \(y(t)\to0\).

Now define the nonnegative predation load
\[
q_i(t)=\frac{p_i y(t)}{D(t)}.
\]
The exponential bound on \(y\) implies \(q_i(t)\to0\). The prey equation is
\[
\dot x_i=x_i\bigl(a_i(1-x_i)-q_i(t)\bigr).
\]
The upper logistic comparison already gives
\[
\limsup_{t\to\infty}x_i(t)\le1.
\]
Fix \(\varepsilon\in(0,1)\). For all sufficiently large \(t\),
\[
q_i(t)\le a_i\varepsilon.
\]
Hence eventually
\[
\dot x_i\ge a_ix_i\bigl((1-\varepsilon)-x_i\bigr).
\]
Comparison with this logistic equation gives
\[
\liminf_{t\to\infty}x_i(t)\ge1-\varepsilon.
\]
Because \(\varepsilon>0\) is arbitrary,
\[
x_i(t)\to1.
\]
Thus every interior prey coordinate converges to carrying capacity while the predator becomes extinct.

Finally, the same componentwise assumption implies the source's local threshold condition automatically:
\[
R_0=\frac{\sum_i c_i}{1+\sum_i b_i}
\le\frac{\sum_i b_i}{1+\sum_i b_i}<1.
\]
So the equilibrium is locally asymptotically stable as well as globally attractive, yielding global asymptotic stability.

## Verification
The bundled `verify.py` checks the algebraic predator-growth bound symbolically for a generic finite list of nonnegative states, verifies the implied inequality \(R_0<1\), and numerically integrates a two-prey example in which both inequalities \(p_i^2<4a_i\) fail by large margins while \(c_i\le b_i\) holds. The numerical trajectory is used only as a consistency check; the proof above is analytic.

For the verification example,
\[
a=(1,3/2),\quad b=(1,2),\quad c=(4/5,3/2),\quad p=(10,12),
\]
so
\[
p_1^2=100>4a_1=4,\qquad p_2^2=144>4a_2=6.
\]
Despite violating the discarded condition, the integrated solution approaches \((1,1,0)\), as predicted by the theorem.

## Relationship to prior work
The source paper derives the multi-prey Holling-II system, its predator invasion threshold, and a global-stability theorem for the predator-free equilibrium. Its Theorem 4 assumes both \(c_i<b_i\) and \(p_i^2<4a_i\). The direct comparison argument above shows that the first family of inequalities already forces the predator per-capita growth rate to remain uniformly negative along every bounded trajectory, independently of \(p_i\). It also shows that the weak inequalities \(c_i\le b_i\) suffice.

The older two-prey/one-predator literature studies global stability and persistence for different interaction laws and parameterizations. Later papers citing the extended Holling-II construction add effects such as fear, disease, or delay and analyze their modified systems. Those works do not state the parameter-free-in-\(p_i\) extinction theorem above for the original \(n\)-prey system.

## Limitations
The result is a sufficient global extinction criterion, not a necessary characterization of predator extinction. If some \(c_i>b_i\), the theorem says nothing; the predator may still die out for particular parameter values or initial states. The argument also uses the autonomous deterministic model exactly as written in the source and does not cover delays, stochastic forcing, prey switching beyond the source functional response, or additional trophic effects.

The theorem is stated for strictly positive prey initial data. Boundary faces with \(x_i(0)=0\) are invariant and therefore cannot converge to the all-prey carrying-capacity equilibrium.

## References
1. S. Fatah, A. Mustafa, and S. Amin, “Predator and n-classes-of-prey model incorporating extended Holling type II functional response for n different prey species,” *AIMS Mathematics* 8 (2023), 5779–5788. DOI: 10.3934/math.2023291. First published 26 December 2022.
2. M. F. Elettreby, “Two-prey one-predator model,” *Chaos, Solitons & Fractals* 39 (2009), 2018–2027. DOI: 10.1016/j.chaos.2007.06.058.

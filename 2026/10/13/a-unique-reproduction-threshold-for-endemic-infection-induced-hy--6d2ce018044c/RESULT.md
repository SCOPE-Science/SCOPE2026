# A unique reproduction threshold for endemic infection-induced hydra effects

## Finding

In the discrete-time Ricker–Poisson susceptible–infectious model of Strube, Elgart and Childs [1], the total population of a positive endemic equilibrium can cross that of the positive disease-free equilibrium at most once as the Ricker reproductive capacity \(r\) increases with all other parameters fixed. Any isolated crossing is from smaller to larger. This is an equilibrium comparison, not a statement about infection trajectories or long-run population averages.

Put \(p=1-d\), \(\delta=d+p\mu\), \(c=\delta/d\), \(a=p/\delta\), and define
\[
\kappa=\beta a(c-w),\qquad r_c=d\exp\!\left(\frac{b\delta}{p\beta}\right).
\]
The positive endemic equilibrium exists exactly for \(r>r_c\), and is unique when it exists. Compare its total with \(\bar S(r)=\log(r/d)/b\):

- If \(w<1\) and \(b(1-w)\ge\kappa\), the endemic total is strictly larger throughout \(r>r_c\), including when \(b(1-w)=\kappa\).
- If \(w<1\) and \(b(1-w)<\kappa\), there is a unique \(r_H>r_c\). The endemic total is smaller on \((r_c,r_H)\), equal at \(r_H\), and larger on \((r_H,\infty)\).
- If \(w=1\) and \(\mu>0\), the endemic total is always smaller; if \(w=1\) and \(\mu=0\), the totals coincide throughout \(r>r_c\).

For \(d=1/4,\ \mu=w=0,\ \beta=b=1\), the crossing is at \(I_H=\log3,\ S_H=(\log 3)/2,\ r_H=3\sqrt3/4\), with \(r_c=e^{1/3}/4\). This crossing is on a locally attracting endemic branch.

## Assumptions and scope

The populations are nonnegative real numbers, the time index is discrete, and the map is [1, Eq. (2)]:
\[
S'=r(S+wI)e^{-b(S+wI)}+pSe^{-\beta I},\qquad
I'=pS(1-e^{-\beta I})+p(1-\mu)I.
\]
Here \(0<d<1\), \(r,b,\beta>0\), and \(w,\mu\in[0,1]\). The positive disease-free equilibrium exists for \(r>d\), which includes the entire endemic regime.

## Proof

At a fixed point with \(I>0\), the infectious equation is equivalent to \(pS(1-e^{-\beta I})=\delta I\). Consequently
\[
S=S(I)=\frac{\delta I}{p(1-e^{-\beta I})},\qquad z(I)=\frac{I}{S(I)}=a(1-e^{-\beta I}).
\]
The susceptible equation reduces to \(r(S+wI)e^{-b(S+wI)}=dS+\delta I\). Conversely, these two equations imply both original fixed-point equations. Thus positive endemic equilibria correspond exactly to \(I>0\) satisfying
\[
r=r(I)=d\frac{1+cz(I)}{1+wz(I)}e^{b(S(I)+wI)}.
\]
The derivative of \(S(I)\) is positive, as \(1-(1+u)e^{-u}>0\) for \(u=\beta I>0\). Also \(z\) increases and \(c\ge1\ge w\), so the ratio in \(r(I)\) is nondecreasing while the exponential is strictly increasing. The continuous function \(r(I)\) therefore increases strictly from \(r_c\), using \(S(0+)=\delta/(p\beta)\) and \(z(0+)=0\), to infinity, since \(S(I)\to\infty\).

Write \(L(I)=\log[(1+cz(I))/(1+wz(I))]\) and \(h(I)=b(1-w)I-L(I)\). Then the population difference is exactly \(h(I)/b\). We have \(h(0)=0\) by continuity and
\[
L'(I)=\frac{(c-w)a\beta e^{-\beta I}}{(1+cz(I))(1+wz(I))},\qquad L'(0)=\kappa.
\]
If \(c>w\), this derivative is positive and strictly decreases to zero: the numerator strictly decreases and neither denominator factor decreases. Thus \(h\) is strictly convex. Since \(0\le z(I)\le a\), \(L\) is bounded. For \(w<1\), this implies \(h(I)\to\infty\), and \(c>w\). If \(h'(0)\ge0\), then \(h(I)>0\) for every \(I>0\). Otherwise \(h\) is initially negative and has exactly one positive zero \(I_H\): \(h(I)/I\) strictly increases by strict convexity and \(h(0)=0\), and tends to \(b(1-w)>0\). The threshold is \(r_H=r(I_H)\), with the stated signs by monotonicity of \(r(I)\). For \(w=1\), \(h=-L\), which is strictly negative if \(\mu>0\) (so \(c>1\)), and identically zero if \(\mu=0\) (so \(c=1\)).

For the example, \(z(I)=3(1-e^{-I})\) and \(h(I)=I-\log(4-3e^{-I})\). With \(t=e^{-I}\in(0,1)\), \(h=\log[1/(t(4-3t))]\) has the same sign as
\[
1-t(4-3t)=1-4t+3t^2=(1-t)(1-3t).
\]
Thus \(t=1/3\) is the unique interior equality point and substitution yields the claimed \(I_H,S_H,r_H\). Put \(\ell=\log 3\). Differentiation of the map at that point gives
\[
J_H=\begin{pmatrix}1-3\ell/8&-\ell/8\\1/2&3/4+\ell/8\end{pmatrix},\qquad
T=\operatorname{tr} J_H=(7-\ell)/4,\quad D=\det J_H=3/4-3\ell/32-3\ell^2/64.
\]
The three Schur margins \(1-D,1-T+D,1+T+D\) have numerators \(16+6\ell+3\ell^2,\ \ell(10-3\ell),\ 224-22\ell-3\ell^2\), respectively, over denominator \(64\). All are strictly positive since \(1<\ell<2\); hence both eigenvalues lie strictly inside the unit disk. Continuity gives local attraction along the endemic branch on both sides sufficiently near \(r_H\).

## Verification and limitations

The fixed-point reduction and one-variable sign argument are the proof for all stated parameters. The packaged standard-library checker `verify.py` corroborates the example and finite residuals; it is not an all-parameter proof. The sign factorization above is exact. No global stability, trajectory comparison, or conclusion about attractor averages is asserted.

## Relationship to prior work

Strube, Elgart and Childs [1, §3.3] compare the same equilibrium totals. Their Lemma 4 treats endemic existence and uniqueness; Appendix B.5 gives the same existence threshold in its zero fecundity-reduction stratum. Their Theorem 5 gives sufficient conditions \(w<1-\beta/b\) and \(d\ge1/2\); it does not classify the sign over the entire reproductive-capacity range. The stable crossing above violates both sufficient conditions. Related same-form work of Jaramillo et al. [2] is known to study disease-induced hydra effects; its full text was not available for a statement-level comparison, so priority beyond the comparisons reported here is not claimed.

[1] L. F. Strube, S. Elgart and L. S. Childs, *Infection-induced increases to population size during cycles in a discrete-time epidemic model*, J. Math. Biol. 88 (2024), article 60. https://doi.org/10.1007/s00285-024-02074-z

[2] J. M. Jaramillo, J. Ma, P. van den Driessche and A.-A. Yakubu, *Disease-Induced Hydra Effect with Overcompensatory Recruitment*, Bull. Math. Biol. 84 (2022), article 17. https://doi.org/10.1007/s11538-021-00975-4

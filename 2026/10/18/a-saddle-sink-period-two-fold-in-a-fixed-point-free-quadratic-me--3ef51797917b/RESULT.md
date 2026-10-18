# A saddle–sink period-two fold in a fixed-point-free quadratic-memristor map

## Finding

For the two-dimensional map
\[
F_{A,B}(x,y)=\bigl(A\cos x+B(y^2-1)x,\;y+x\bigr),\qquad A>0,\ B>0,
\]
introduced as the quadratic-memristor FPFM1 map in [1], the following is an exact classification of **all real primitive period-two orbits** in a parameter neighborhood of the memory-gain threshold.

If \(0<B\le1\), no period-two orbit exists. For \(1<B\le4/3\), put
\[
R=\sqrt{1-B^{-1}},\qquad
G_B(u)=\frac{B u^2\sqrt{R^2-u^2/4}}{\cos u},\qquad 0<u<2R.
\]
There is a unique nondegenerate maximizer \(u_*(B)\) of \(G_B\). With \(A_*(B)=G_B(u_*(B))\), the exact number of distinct primitive period-two orbits (up to cyclic interchange) is
\[
N_2(A,B)=\begin{cases}
2,&0<A<A_*(B),\\
1,&A=A_*(B),\\
0,&A>A_*(B).
\end{cases}
\]
For every admissible solution \(G_B(u)=A\), the two points of the corresponding orbit are
\[
(u,z-u/2)\longleftrightarrow(-u,z+u/2),
\qquad z=\sqrt{R^2-u^2/4}>0.
\]
In the explicit subregion \(1<B\le9/8\), the orbit with smaller \(u\) is a hyperbolic saddle and the orbit with larger \(u\) is a hyperbolic sink. At equality \(A=A_*(B)\), the unique orbit has two-step multipliers \(1\) and \(d\), with \(0<d<1\); it is a nondegenerate saddle-node of period-two orbits. As \(B\downarrow1\),
\[
\boxed{A_*(B)=\frac{8}{3\sqrt3}(B-1)^{3/2}
\left(1+\frac56(B-1)+O((B-1)^2)\right).}
\]

## Assumptions and scope

All states \((x,y)\) are real and iteration is exact. The forcing amplitude \(A\) is positive. The theorem makes no orbit-count assertion for \(B>4/3\), and no attraction classification beyond \(B=9/8\). A hyperbolic sink is a locally attracting two-cycle, not necessarily a global attractor. No claim is made that the model is chaotic within the parameter region of the theorem.

## Proof

**1. Complete reduction.** For a two-cycle with consecutive states \((x,y)\) and \((x',y')\), the second update gives \(x+x'=0\). The possibility \(x=0\) is excluded because then the next first coordinate equals \(A\ne0\). After cyclic interchange, write \(x=u>0\), \(x'=-u\), \(y=z-u/2\), \(y'=z+u/2\). The two first-coordinate equations are equivalent to
\[
z^2+\frac{u^2}{4}=1-\frac1B=R^2,
\qquad A\cos u=B u^2z. \tag{1}
\]
For \(B\le1\), the first identity is impossible. For \(1<B\le4/3\), \(0<u<2R\le1<\pi/2\), so \(\cos u>0\). The second identity forces \(z>0\). Conversely every solution \(u\in(0,2R)\) of \(G_B(u)=A\), together with its positive \(z\), satisfies both original map equations. This is a bijection between positive roots and primitive period-two orbits. Neither endpoint gives an orbit for positive \(A\).

**2. Unique fold and complete count.** Write \(u=2Rt\), \(0<t<1\), and \(k=2R\le1\). Then
\[
G_B(2Rt)=\frac{4BR^3t^2\sqrt{1-t^2}}{\cos(kt)}.
\]
The second derivative of its logarithm with respect to \(t\) is
\[
-\frac2{t^2}-\frac{1+t^2}{(1-t^2)^2}+k^2\sec^2(kt).\tag{2}
\]
For \(t^2\le1/2\), the sum of the two negative magnitudes is at least \(5\); for \(t^2\ge1/2\), it is at least \(6\). Meanwhile \(k^2\sec^2(kt)\le\sec^2(1)\le4\), since \(\cos1\ge1/2\). Hence (2) is strictly negative. The positive function vanishes at both ends and is strictly log-concave, so it has one interior maximum, of negative second derivative, and each strictly lower positive level intersects exactly twice. The maximum is nondegenerate, giving the stated fold and root census.

**3. Two-step stability in the weak-gain region.** Let \(z=\sqrt{R^2-u^2/4}\), and define
\[
S=Bu z(1+u\tan u),\quad H=Bu z(3+u\tan u).
\]
At the two orbit points, the Jacobians of \(F_{A,B}\), in chronological order, are
\[
J_+=\begin{pmatrix}-1-S&2Buz-Bu^2\\1&1\end{pmatrix},\qquad
J_-=\begin{pmatrix}-1+S&-2Buz-Bu^2\\1&1\end{pmatrix}.
\]
These identities use (1) and \(A\sin u=Bu^2z\tan u\). Thus for the two-step derivative \(J_-J_+\),
\[
\operatorname{tr}=2-S^2-2Bu^2,\qquad
\det=(Bu^2-1)^2-H^2,\tag{3}
\]
with characteristic polynomial \(P(\lambda)=\lambda^2-\operatorname{tr}\lambda+\det\). Direct expansion gives
\[
P(1)=B^2u^2\bigl[u^2-4z^2(2+u\tan u)\bigr].\tag{4}
\]
But
\[
\frac{G_B'(u)}{G_B(u)}=\frac2u-\frac{u}{4z^2}+\tan u,
\]
so (4) is negative on the rising branch, zero at the fold, and positive on the falling branch.

If \(1<B\le9/8\), then \(u\le2/3\), \(Bu^2\le4(B-1)\le1/2\), and \(Bu z\le BR^2=B-1\le1/8\). Since \(\cos u\ge1-u^2/2\ge7/9\) and \(\sin u\le u\), it follows that \(\tan u\le2u\) and \(u\tan u\le8/9\). Consequently
\[
0<S\le17/72<1/4,\qquad 0<H\le35/72<1/2.
\]
Equation (3) now yields \(0<\det<1\) and \(\operatorname{tr}>15/16>0\). In particular \(P(-1)=1+\operatorname{tr}+\det>0\). On the ascending branch \(P(1)<0\), so one positive eigenvalue is greater than \(1\) and the other is in \((0,1)\): a saddle. On the descending branch \(P(1)>0\), and the three strict second-order Schur conditions \(1-\det>0\), \(P(1)>0\), \(P(-1)>0\) show both multipliers are inside the open unit disk: a sink. At the maximum, \(P(1)=0\) and the other eigenvalue is \(\det\in(0,1)\). More generally, throughout \(1<B\le4/3\) one has \(0<Bu^2<4(B-1)\le4/3<2\), hence \(\det<(Bu^2-1)^2<1\); the fold multiplier \(1\) is simple on the full counting region. Strict log-concavity, the nonzero dependence of (1) on \(A\), and the simple unit multiplier establish nondegenerate fold behavior.

**4. Sharp onset.** Set \(\varepsilon=B-1>0\), so \(R^2=\varepsilon/(1+\varepsilon)\). In the normalized variable \(t\),
\[
G_B(2Rt)=4\varepsilon^{3/2}t^2\sqrt{1-t^2}
\left[1+\varepsilon\left(2t^2-\frac12\right)+O(\varepsilon^2)\right],\tag{5}
\]
uniformly with derivatives on compact interior intervals. The unique maximum of the leading shape \(t^2\sqrt{1-t^2}\) occurs at \(t_0=\sqrt{2/3}\), with a nondegenerate second derivative. The maximizing point moves by \(O(\varepsilon)\), affecting the maximal value first at order \(\varepsilon^2\). Evaluating (5) at \(t_0\) gives the stated expansion and its coefficient \(5/6\).

## Verification

The included standalone program `verify.py` uses the Python 3 standard library. Running `python3 verify.py` checks reconstruction of both points, two-step recurrence, exact trace/determinant formulas, the characteristic identity (4), numerical localization of the unique fold, and both stability branches across eight memory-gain values, with additional checks of the two asymptotic coefficients. It completed 2,526 finite assertions. These tests are consistency checks; all quantified conclusions above depend on the analytical proof.

## Relationship to prior work

Almatroud and Pham [1, Eq. (5)] introduced this exact quadratic-memristance map, proved the absence of fixed points, and provided numerical Lyapunov/bifurcation evidence, particularly for gains higher than the near-threshold range studied here. Their complete openly accessible article was examined through the full-text transcription [2], including Sections 2–5 and the displayed equations and captions. The present theorem instead gives a global real phase-space enumeration of primitive two-cycles in an exact positive-parameter region, classifies the resulting saddle–sink pair, and derives the fold's singular onset exponent and coefficient. Neither the absence of fixed points nor a numerical bifurcation plot implies these conclusions. The earlier Bao–Li–Wu–Zhang–Chen discrete memristor model [3] has an entire fixed-point line and a different update law, so its dynamics do not cover the present classification. Related mathematical records retrieved by subject search treated distinct models; no equivalent theorem for [1, Eq. (5)] was identified. This is a best-knowledge priority assessment, not a proof of uniqueness in the literature.

## Limitations

This is a local-parameter, globally counted period-two theorem, not a classification of all dynamical behavior. In particular it does not assert chaoticity, global basins of attraction, absence of longer periodic orbits, or a sharp outer endpoint for the saddle–sink stability region. Priority remains uncertain for unindexed or differently described results. Numerical calculations are not substitutes for the global algebraic reduction and analytic concavity estimates.

## References

[1] O. A. Almatroud and V.-T. Pham, "Building Fixed Point-Free Maps with Memristor," *Mathematics* **11** (2023), article 1319, first published 2023-03-09. DOI: https://doi.org/10.3390/math11061319.

[2] Full-text transcription of [1], accessible via https://www.researchgate.net/publication/369126934_Building_Fixed_Point-Free_Maps_with_Memristor (publisher-supplied openly licensed full text; Sections 2–5 and bibliography inspected).

[3] B.-C. Bao, H. Li, H. Wu, X. Zhang, and M. Chen, "Hyperchaos in a second-order discrete memristor-based map model," *Electronics Letters* **56** (2020), 769–770. DOI: https://doi.org/10.1049/el.2020.1172.

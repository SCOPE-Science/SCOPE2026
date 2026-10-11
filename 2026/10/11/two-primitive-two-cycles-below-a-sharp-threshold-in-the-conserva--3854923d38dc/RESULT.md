# Two primitive two-cycles below a sharp threshold in the conservative Gumowski–Mira map

## Finding
For the rational planar map
\[
T_\mu(x,y)=\bigl(y+g_\mu(x),\;-x+g_\mu(y+g_\mu(x))\bigr),\qquad
 g_\mu(s)=\mu s+\frac{2(1-\mu)s^2}{1+s^2},\quad \mu\in\mathbb R,
\]
there are **exactly two distinct primitive period-two orbits if \(\mu<-1\)** and **none if \(\mu\geq-1\)**. Here distinct orbits are counted up to cyclic interchange of their two points. Every primitive period-two point has second coordinate zero. For \(\mu=-1-t\) with \(t>0\), write the negative coordinates of the two cycles as \(q_{\rm in}\) and \(q_{\rm out}\). Then
\[
q_{\rm out}<-\frac{1}{1+t}<q_{\rm in}<0.
\]
As \(t\downarrow0\), their points are respectively
\[
\begin{aligned}
(q_{\rm in},0)&=\bigl(-\tfrac14\sqrt t+O(t),0\bigr),&
T_\mu(q_{\rm in},0)&=\bigl(\tfrac14\sqrt t+O(t),0\bigr),\\
(q_{\rm out},0)&=\bigl(-2t^{-1/4}+2+O(t^{1/4}),0\bigr),&
T_\mu(q_{\rm out},0)&=\bigl(2t^{-1/4}+2+O(t^{1/4}),0\bigr).
\end{aligned}
\]
Thus one cycle collapses onto the origin while the other escapes to infinity as the threshold is approached.

## Assumptions and scope
All phase-space coordinates and parameters are real. The map is the conservative subfamily (zero coefficient of the additional \(y\)-nonlinearity) of the Gumowski–Mira recurrence in Ambika and Ambika. It is a smooth invertible area-preserving map of \(\mathbb R^2\): its Jacobian determinant is identically \(1\), and the scalar form is \(x_{n+2}+x_n=2g_\mu(x_{n+1})\). “Primitive period two” means exactly two iterates return to the point, but one iterate does not. For \(\mu\ne1\) the only fixed points are \((0,0)\) and \((1,0)\); when \(\mu=1\), the entire line \(y=0\) is fixed.

## Proof
**Reduction and sign obstruction.** A period-two scalar sequence alternates between \(p\) and \(q\), where \(p=g_\mu(q)\), \(q=g_\mu(p)\), and \(p\ne q\). Its planar points are precisely \((p,0)\) and \((q,0)\). When \(\mu\ne1\),
\[
g_\mu(s)-s=\frac{(\mu-1)s(s-1)^2}{1+s^2}.
\]
Neither \(p\) nor \(q\) can equal \(0\) or \(1\); multiplying the two equations for their differences gives \(pq<0\). Put \(S=p+q\), \(P=pq<0\), and \(K=(1+p^2)(1+q^2)=S^2+(P-1)^2\). Adding the period-two equations yields
\[
S=2\left(\frac{p^2}{1+p^2}+\frac{q^2}{1+q^2}\right)>0,
\qquad S(K-2S)=4P(P-1)>0.
\]
Subtracting the equations and dividing by \(p-q\) yields \((1+\mu)K=-2(1-\mu)S\). Consequently
\[
\mu=-\frac{K+2S}{K-2S}<-1.
\]
No primitive two-cycle exists for \(\mu\ge-1\) except possibly \(\mu=1\); there \(T_1(x,y)=(x+y,y)\), so \(T_1^2(x,y)=(x+2y,y)\), and all its period-two points are fixed.

**Existence and exact count.** Now set \(\mu=-1-t\), \(t>0\), and define
\[
N_t(x)=(-1-t)x(1+x^2)+2(2+t)x^2,\qquad
H_t(x)=(1+x^2)^2+N_t(x)^2>0.
\]
A direct rational identity is
\[
\bigl(g_\mu(g_\mu(x))-x\bigr)(1+x^2)H_t(x)
=x(\mu-1)(x-1)^2Q_t(x),
\]
where
\[
\begin{aligned}
Q_t(x)={}&-t(t+1)^2x^6+4t(t+1)(t+2)x^5
-t(6t^2+20t+19)x^4\\
&+2t(t+2)(2t+1)x^3+(-t^3+2t^2+13t+16)x^2\\
&-2t(t+2)x-t.
\end{aligned}
\]
For every \(t>0\), the signs are \(Q_t(0)=-t<0\), \(Q_t(x)\to-\infty\) as \(x\to-\infty\), and
\[
Q_t\!\left(-\frac1{1+t}\right)=\frac{2(t^4+4t^3+8t^2+8t+8)}{(1+t)^4}>0.
\]
The intermediate-value theorem therefore supplies a negative root on each side of \(-1/(1+t)\). To prove there are no more, substitute \(x=-u\) with \(u>0\). Reading \(Q_t(-u)\) from the leading term down to the constant term gives sign pattern \((-,-,-,-,\ast,+,-)\), where \(\ast\) is arbitrary (and zero terms are omitted). Every possible pattern has precisely two sign changes, so Descartes' rule gives at most two positive roots of \(Q_t(-u)\), counted with multiplicity. Hence these are the only two negative roots and both are simple. For any such negative root \(q\), \(g_\mu(q)>0\), and \(g_\mu(g_\mu(q))=q\); it therefore produces a primitive two-cycle. Conversely, every primitive two-cycle has a negative member by the sign obstruction. This proves the exact count.

**Two contrasting limiting scales.** The inner negative root follows by setting \(x=\sqrt t\,u\) in \(Q_t(x)=0\):
\[
\lim_{t\downarrow0}\frac{Q_t(\sqrt t\,u)}{t}=16u^2-1.
\]
The simple negative root \(u=-1/4\) persists, and its partner is obtained by applying \(g_{-1-t}\). For the outer root put \(t=\varepsilon^4\), \(x=v/\varepsilon\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^2 Q_{\varepsilon^4}(v/\varepsilon)
=-v^2(v^2-4)(v^2+4).
\]
The simple root \(v=-2\) persists. With \(x=-2/\varepsilon+w\), the first nonvanishing coefficient of \(\varepsilon^2Q_{\varepsilon^4}(x)\) is \(128(w-2)\varepsilon\); thus \(w=2+O(\varepsilon)\). Applying \(g_{-1-\varepsilon^4}\) gives the companion asymptotic. These are asymptotics of genuine exact roots, not numerical orbit approximations.

## Verification
The companion `verify.py` symbolically checks the full rational factorization, the two endpoint signs, every sign needed for Descartes' rule, and the inner/outer asymptotic expansions. Execute `python -m pip install -r requirements.txt` followed by `python verify.py`. The exact polynomial sign proof and the implicit-function argument above establish the infinite parameter claim; the checker supplies reproducible algebra but no external proof certification.

## Relationship to prior work
The identical rational nonlinearity appears in Ambika and Ambika, arXiv:nlin/0606005v1, Section 2, but the study's reported low-period windows use a nonzero dissipative parameter and a different range of \(\mu\). Prasad, Meena, and Ansari (2020) give numerical dynamical indicators for another nonconservative parameter regime. The integrable Gumovski–Mira equations studied by Cima, Gasull, and Mañosa (arXiv:1106.0318) use an odd rational nonlinearity rather than the even-plus-odd \(g_\mu\) above. The quartic-integrable additive class of Bastien and Rogalski (2007) has a numerator of degree at most two over a quadratic denominator, whereas \(2g_\mu\) has an essential cubic numerator when \(\mu<-1\). Kulenović, Nurkanović, and Pilav (2014) study the distinct \(a s/(1+s^2)\) nonlinearity. The exact global count and both contrasting threshold asymptotics were not implied by the checked statements of those works.

## Limitations
This is a complete classification of primitive period-two orbits only, not of all periods, chaotic invariant sets, or the elliptic/hyperbolic stability types of the two cycles. It does not assert anything about their basins or long-term attraction. Original Gumowski–Mira publications, including the 1980 monograph and a 1985 article, were not fully accessible in this review; an equivalent historical statement in unexamined portions remains a literature risk.

## References
1. G. Ambika and K. Ambika, “Intermittency and Synchronisation in Gumowski-Mira Maps,” arXiv:nlin/0606005v1 (first submitted 2006-06-01), https://arxiv.org/html/nlin/0606005v1.
2. S. N. Prasad, K. R. Meena, and A. A. Ansari, “Complexity Dynamics of Gumowski-Mira Map,” *Applications and Applied Mathematics* 15 (2020), 273–281, https://digitalcommons.pvamu.edu/aam/vol15/iss1/15/.
3. A. Cima, A. Gasull, and V. Mañosa, “Non-autonomous 2-periodic Gumovski-Mira difference equations,” arXiv:1106.0318 (2011), https://arxiv.org/abs/1106.0318.
4. M. R. S. Kulenović, Z. Nurkanović, and E. Pilav, “Birkhoff Normal Forms and KAM Theory for Gumowski-Mira Equation,” *Scientific World Journal* 2014, 819290, https://doi.org/10.1155/2014/819290.
5. G. Bastien and M. Rogalski, “On the algebraic difference equations \(u_{n+2}+u_n=\psi(u_{n+1})\) in \(\mathbb R\), related to a family of elliptic quartics in the plane,” *Journal of Mathematical Analysis and Applications* 326 (2007), 822–844, https://doi.org/10.1016/j.jmaa.2006.02.095.
6. I. Gumowski and C. Mira, *Recurrences and Discrete Dynamic Systems*, Lecture Notes in Mathematics 809 (1980), historical reference not available for full-text comparison.
7. I. Gumowski and C. Mira, “Nonconstant Dynamic States and Their Bifurcations,” *Environment and Planning B* 12 (1985), 85–101, https://doi.org/10.1068/b120085 (abstract consulted; full text unavailable).

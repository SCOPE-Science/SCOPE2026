# Exact smoothing and stability phase diagram for the Hénon–Lozi prime two-cycle

## Finding

Let \(0<b<1\), put \(c=1-b\), assume \(a>c\), and let \(\varepsilon>0\). Define
\[
F_{a,b,\varepsilon}(x,y)=\bigl(1-aS_\varepsilon(x)+y,\ bx\bigr),\qquad
S_\varepsilon(x)=\begin{cases}|x|,&|x|\ge\varepsilon,\\ (x^2+\varepsilon^2)/(2\varepsilon),&|x|\le\varepsilon.\end{cases}
\]
The original published family takes \(0<\varepsilon<1\); the same formula remains well-defined for every \(\varepsilon>0\). Define three exact thresholds
\[
\varepsilon_1=\frac{a-c}{a^2+c^2},\qquad
\varepsilon_2=\frac{a}{a^2-ac+2c^2},\qquad
\varepsilon_*=\frac{2a}{a^2+3c^2},\qquad
0<\varepsilon_1<\varepsilon_2<\varepsilon_*.
\]
**Theorem.** Exactly one distinct prime two-cycle exists when \(0<\varepsilon<\varepsilon_*\), and none exists when \(\varepsilon\ge\varepsilon_*\). Write the two points as \(P=(u,bv)\) and \(Q=(v,bu)\), with \(u<v\). Its exact coordinates are:

* For \(0<\varepsilon\le\varepsilon_1\),
\[
u=\frac{c-a}{a^2+c^2},\qquad v=\frac{c+a}{a^2+c^2}.
\]
* For \(\varepsilon_1<\varepsilon<\varepsilon_2\),
\[
u=\frac{c^2\varepsilon-\sqrt{\varepsilon[2a^2(a-c)-(a^4-c^4)\varepsilon]}}{a^2},
\qquad v=\frac{1-cu}{a}.
\]
* For \(\varepsilon_2\le\varepsilon<\varepsilon_*\),
\[
u=\frac{c\varepsilon}{a}-d,\qquad
v=\frac{c\varepsilon}{a}+d,\qquad
d=\sqrt{\frac{2\varepsilon}{a}-\varepsilon^2\left(1+\frac{3c^2}{a^2}\right)}.
\]
The formulas agree at both interface values. There is exact persistence of the unsmoothed orbit throughout \((0,\varepsilon_1]\). With \(\delta=\varepsilon-\varepsilon_1\downarrow0\), its first motion is quadratic:
\[
u=\frac{c-a}{a^2+c^2}+\frac{a^2}{2(a-c)}\delta^2+O(\delta^3),\qquad
v=\frac{c+a}{a^2+c^2}-\frac{ac}{2(a-c)}\delta^2+O(\delta^3).
\]
At the terminal boundary,
\[
v-u=2\sqrt{\frac2a}\sqrt{\varepsilon_*-\varepsilon}
+O\bigl((\varepsilon_*-\varepsilon)^{3/2}\bigr).
\]
The merger is a flip collision with a fixed point whose one-step multipliers are \(-1\) and \(b\).

**Stability refinement.** Let \(W=(1+b)^2\), and let \(M=DF(Q)DF(P)\) be the two-step derivative. For each existing two-cycle, \(\det M=b^2\), while \(\operatorname{tr}M=2b+R(\varepsilon)\), with
\[
R(\varepsilon)=\begin{cases}
-a^2,&0<\varepsilon\le\varepsilon_1,\\
a^2u/\varepsilon,&\varepsilon_1<\varepsilon<\varepsilon_2,\\
a^2+4c^2-2a/\varepsilon,&\varepsilon_2\le\varepsilon<\varepsilon_*.
\end{cases}
\]
This function is continuous, constant on the first regime, then strictly increasing to \(c^2\). The two-cycle is linearly attracting exactly when \(R(\varepsilon)>-W\); at equality a return eigenvalue is \(-1\), and below it the orbit is a saddle.

If \(a<1+b\), it is attracting for every \(0<\varepsilon<\varepsilon_*\). If \(a=1+b\), its return has a neutral multiplier \(-1\) up to \(\varepsilon_1\) and is attracting afterwards. If \(a>1+b\), the unique saddle-to-attractor transition occurs at
\[
\varepsilon_s=\begin{cases}
\displaystyle\frac{2a^2(a-c)}{a^4+W^2+2c^2W},&a^2-2ac\le W,\\
\displaystyle\frac{2a}{a^2+4c^2+W},&a^2-2ac>W,
\end{cases}
\qquad \varepsilon_1<\varepsilon_s<\varepsilon_*.
\]
The orbit is a saddle below \(\varepsilon_s\), neutral at \(\varepsilon_s\), and attracting above it (before the terminal collision).

## Assumptions and scope

All assertions quantify over real \(a,b,\varepsilon\) with \(0<b<1\), \(a>1-b\), and \(\varepsilon>0\). The original smooth-map literature uses \(0<\varepsilon<1\); restricting the conclusions to that range requires only intersection of these intervals. No assertions are made for \(b\le0\), \(b\ge1\), or \(a\le1-b\). Stability here means all eigenvalues of the two-step Jacobian have modulus less than one, and a saddle means exactly one exceeds one in modulus. A neutral eigenvalue does not determine nonlinear stability.

## Proof

**1. Reduction to a single level.** The orbit equations \(F(P)=Q\), \(F(Q)=P\) are precisely
\[
cv=1-aS_\varepsilon(u),\qquad cu=1-aS_\varepsilon(v).
\]
Set \(g(x)=aS_\varepsilon(x)-cx\). Subtracting the orbit equations gives \(g(u)=g(v)=k\); adding them then gives \(k+c(u+v)=1\). Because \(a>c>0\), the function \(g\) is strictly decreasing from \(+\infty\) to its unique minimum at \(x_0=c\varepsilon/a\), then strictly increasing to \(+\infty\). Every level \(k>g(x_0)\) therefore has exactly two ordered preimages \(u(k)<x_0<v(k)\). Put \(H(k)=k+c(u(k)+v(k))\).

**2. Global uniqueness and sharp existence.** Both preimages lie in the quadratic core for \(g(x_0)<k\le g(\varepsilon)\), and the quadratic-root sum is \(u+v=2c\varepsilon/a\), so \(H'(k)=1\). For \(g(\varepsilon)<k<g(-\varepsilon)\), the left preimage is in the core with \(u\le(2c/a-1)\varepsilon\) and the right preimage is outer. Thus \(|g'(u)|\ge a-c=g'(v)\), giving
\[
H'(k)=1+c\left(\frac1{g'(u)}+\frac1{a-c}\right)\ge1.
\]
For \(k>g(-\varepsilon)\), the outer slopes are \(-(a+c)\) and \(a-c\), and hence \(H'(k)=1+c[(a-c)^{-1}-(a+c)^{-1}]>1\). Continuous matching makes \(H\) strictly increasing on its full domain. At the lower endpoint,
\[
H(g(x_0))=\frac{\varepsilon(a^2+3c^2)}{2a},
\]
and \(H(k)\to\infty\). Therefore the equation \(H(k)=1\) has exactly one level with two distinct preimages if and only if \(\varepsilon<\varepsilon_*\). At equality the two preimages coincide and no prime two-cycle remains.

**3. Two exact switching thresholds.** Evaluating \(H\) at the two branch-transition levels gives
\[
H(g(-\varepsilon))=\frac{(a^2+c^2)\varepsilon}{a-c},\qquad
H(g(\varepsilon))=\frac{(a^2-ac+2c^2)\varepsilon}{a}.
\]
The comparisons with \(1\) yield the branch regimes separated by \(\varepsilon_1,\varepsilon_2\). Indeed,
\[
\varepsilon_2-\varepsilon_1=\frac{2c(a^2-ac+c^2)}{(a^2+c^2)(a^2-ac+2c^2)}>0,
\qquad
\varepsilon_*-\varepsilon_2=\frac{a(a-c)^2}{(a^2+3c^2)(a^2-ac+2c^2)}>0.
\]
Solving the two linear outer equations gives the first displayed coordinate pair. In the mixed regime, \(v=(1-cu)/a\), and substituting into the other orbit equation gives
\[
a^2u^2-2c^2\varepsilon u+a^2\varepsilon^2-2(a-c)\varepsilon=0.
\]
The smaller root is the unique admissible left preimage, giving the second formula. In the central regime, writing \(u=t-d\) and \(v=t+d\), the equal-level equation forces \(t=c\varepsilon/a\), and the summed orbit equations yield the displayed formula for \(d\). Uniqueness from Step 2 rules out all other prime two-cycles, including combinations across other outer branches. The formulas match continuously at the two transitions.

**4. Boundary laws.** At \(\varepsilon=\varepsilon_1\), the mixed quadratic solution has \(u=-\varepsilon_1\). Its implicit polynomial has nonzero derivative in \(u\), zero first \(\varepsilon\)-derivative, and second \(\varepsilon\)-derivative \(2a^2\). Hence \(u'(\varepsilon_1+)=0\), \(u''(\varepsilon_1+)=a^2/(a-c)\), and the corresponding expansion of \(v=(1-cu)/a\) follows. The central expression can be rewritten
\[
d^2=\frac{2\varepsilon}{a}\left(1-\frac{\varepsilon}{\varepsilon_*}\right),
\]
which proves the terminal square-root law. At the collision \(x_0=c\varepsilon_*/a\), \(aS'_{\varepsilon_*}(x_0)=c\). The one-step Jacobian has characteristic polynomial \(\lambda^2+c\lambda-b=(\lambda+1)(\lambda-b)\), giving multipliers \(-1,b\).

**5. Stability.** At abscissa \(x\), write \(m(x)=aS'_\varepsilon(x)\); the Jacobian is \(J(x)=\begin{pmatrix}-m(x)&1\\b&0\end{pmatrix}\). Direct multiplication gives \(\operatorname{tr}(J(v)J(u))=2b+m(u)m(v)\) and \(\det(J(v)J(u))=b^2\). Substituting the three branch expressions yields the stated \(R(\varepsilon)\). In the mixed regime,
\[
\frac{u}{\varepsilon}=\frac{c^2}{a^2}-\frac1{a^2}\sqrt{\frac{2a^2(a-c)}{\varepsilon}-(a^4-c^4)},
\]
which increases strictly; in the core regime \(R'(\varepsilon)=2a/\varepsilon^2>0\). Consequently \(R\) rises from \(-a^2\) to \(c^2\). The two-dimensional Schur conditions for determinant \(b^2<1\) are
\[
-(1+b^2)<2b+R(\varepsilon)<1+b^2.
\]
The upper inequality is strict for every genuine two-cycle since \(R<c^2=(1-b)^2\). The lower one reduces to \(R>-(1+b)^2\). Its unique possible crossing, obtained by substituting \(u=-W\varepsilon/a^2\) in the mixed quadratic or \(R=a^2+4c^2-2a/\varepsilon\) in the central formula, gives exactly \(\varepsilon_s\) in its two cases. The comparison of \(R(\varepsilon_2)=2ac-a^2\) with \(-W\) decides which case applies. The classification follows.

## Verification

The companion `verify.py` checks symbolic threshold differences, matching-level identities, the terminal amplitude derivative, the central return-trace identity, and return equations across a grid of rational and floating-point parameters. It prints `VERIFY_OK` when all checks succeed. These checks corroborate but do not substitute for the global monotonic-level proof above.

## Relationship to prior work

Aziz-Alaoui, Robert and Grebogi introduced this precise \(C^1\) quadratic smoothing of the Lozi map and analyzed fixed points and their comparison with the unsmoothed system. Their publisher-accessible introduction, generalities and numerical-investigation section distinguish rigorous fixed-point analysis from simulations of more complex dynamics. The present claim is an exact *global prime-two-cycle* and stability classification, not the introduction of the map or of its fixed-point analysis. Earlier work by Aharonov, Devaney and Elias treats an area-preserving piecewise-linear system and a different analytic smoothing, without providing an implication to the dissipative quadratic-core phase diagram here. These comparisons are limited by access to the complete original manuscripts; see the associated review for the remaining priority risk.

## Limitations

No conclusions are made about prime periods above two, global basins, chaotic attractors, or nonlinear stability at neutral multipliers. The formulas classify two-cycles even if they lie outside a physically selected attractor. The terminal square-root asymptotic is a limit in the naturally extended \(\varepsilon>0\) family; for the original published restriction \(\varepsilon<1\), it is directly accessible only when \(\varepsilon_*\le1\). Published priority requires independent assessment because the original article and an associated 1999 preprint could not be checked in full.

## References

1. M. A. Aziz-Alaoui, C. Robert, C. Grebogi, “Dynamics of a Hénon–Lozi-type map,” *Chaos, Solitons & Fractals* **12** (2001), 2323–2341, DOI: 10.1016/S0960-0779(00)00192-2. Publisher sections available at https://doi.org/10.1016/S0960-0779(00)00192-2.
2. D. Aharonov, R. L. Devaney, U. Elias, “The dynamics of a piecewise linear map and its smooth approximation,” *International Journal of Bifurcation and Chaos* **7** (1997), 351–372, DOI: 10.1142/S0218127497000236.
3. M. A. Aziz-Alaoui, author-maintained article record, https://lmah.univ-lehavre.fr/~alaoui/paper_ARG99.html (records a January 1999 preprint whose exact public day is not independently verified).

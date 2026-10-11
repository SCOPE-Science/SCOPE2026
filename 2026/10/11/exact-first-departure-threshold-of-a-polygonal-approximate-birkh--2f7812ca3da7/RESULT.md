# Exact first-departure threshold of a polygonal approximate Birkhoff–James profile
## Finding
Let \(X\) be the real polygonal Banach plane from Example 6 of Fang--Xu--Liu--Gu--Li, with
\[
\|(s,t)\|_X=\max\left\{|s+t/10|,\frac{|250s+95t|}{257},\frac{5|s+t|}{7},\frac{|95s+250t|}{257},|s/10+t|,|s-t|\right\}.
\]
For unit vectors \(x,y\), write
\[
d_X(x,y)=\inf_{\lambda\in\mathbb R}\|x-\lambda y\|_X,
\qquad
m_X(x,y)=\min\{\|x+y\|_X,\|x-y\|_X\}.
\]
The focal paper proves \(J_{\perp}(X)=331/206\). Put \(c=331/206\). Then the exact largest directed distance among pairs that already improve on the orthogonal endpoint is
\[
D_*:=\sup\{d_X(x,y):x,y\in S_X,\ m_X(x,y)>c\}
=\frac{18910336411}{19465125400}.
\]
Therefore
\[
J_B^{\varepsilon}(X)=\frac{331}{206}
\quad\Longleftrightarrow\quad
0\le\varepsilon\le\frac{554788989}{19465125400}.
\]
Numerically, the sharp first-departure threshold is \(0.02850169097806069\ldots\). It lies strictly above the focal paper's test value \(1/40\) and strictly below its saturation threshold \(100999/3009900\).

## Assumptions and scope
The space is real and two-dimensional. The approximate Birkhoff--James relation is the focal paper's convention
\[
x\perp_{B,\varepsilon}y
\quad\Longleftrightarrow\quad
d_X(x,y)\ge 1-\varepsilon,
\]
for unit vectors \(x,y\). The profile is
\[
J_B^{\varepsilon}(X)=\sup\{m_X(x,y):x,y\in S_X,\ x\perp_{B,\varepsilon}y\}.
\]
The claim concerns only the polygonal plane \(X\) from Example 6 and only the initial interval on which this profile remains equal to its exact-orthogonality value. It does not determine the entire profile after first departure.

## Proof
The focal paper reduces the relevant first-quadrant geometry to the parameter \(q\in[-1,1]\), with a boundary function \(S(q)\). In the only two branches needed once \(m_X(x,y)>c\), write
\[
S_2(q)=\frac{514-155q}{345}
\quad\left(\frac15\le q\le\frac{89}{100}\right),
\qquad
S_3(q)=\frac{20-9q}{11}
\quad\left(\frac{89}{100}\le q\le1\right).
\]
After the symmetries used in Example 6, a pair with \(m_X(x,y)>c\) yields parameters \(u\ge v>0\) satisfying
\[
u+v>c,
\qquad
S(u)+S(v)>\frac75c,
\]
and its directed distance is bounded by, and on the relevant facet configuration equals,
\[
D(u,v)=\frac{S(u)v+uS(v)}{S(v)+v}.
\]
Because \(u+v>c>1+1/5\), one has \(v>1/5\). The branch \(S_3/S_3\) is impossible: even at its left endpoint,
\[
2S_3(89/100)<\frac75c.
\]
Thus only \(S_2/S_2\) and \(S_3/S_2\) remain.

For the \(S_2/S_2\) cell, the second feasibility inequality is equivalent to
\[
u+v<Q:=\frac{10379}{6386}.
\]
Here
\[
D_{22}(u,v)=\frac{257(u+v)-155uv}{257+95v},
\]
which is strictly increasing in \(u\). Hence the upper envelope is obtained by taking \(u=89/100\) until the line \(u+v=Q\) becomes active, and then by taking \(u=Q-v\). On the first segment the derivative is positive. On the second segment its sign is the sign of
\[
9403385v^2+50877262v-66685075,
\]
which is negative throughout that segment. The unique cell maximum is therefore the junction value
\[
D_{22}^{\max}=rac{29270497}{30250300}.
\]

For the mixed \(S_3/S_2\) cell,
\[
D_{32}(u,v)=\frac{2827u+3450v-2405uv}{11(95v+257)},
\]
which is again strictly increasing in \(u\). The active \(S\)-sum boundary is
\[
u=U(v):=\frac{827521-351230v}{639630}.
\]
Its feasible interval begins where \(U(v)=c-v\), namely
\[
v_0=\frac{100117}{144200},
\qquad
u_0=\frac{131583}{144200},
\]
and ends where \(U(v)=89/100\). Along \(u=U(v)\), the derivative has the sign of
\[
23532925v^2+127325510v-123687932,
\]
which is negative throughout the feasible interval. Hence the mixed-cell supremum is its left endpoint value
\[
D_{32}^{\sup}=D(u_0,v_0)=\frac{18910336411}{19465125400}.
\]
It strictly exceeds \(D_{22}^{\max}\), so it is the global upper bound among improving pairs.

The endpoint itself has \(u_0+v_0=c\) and \(S_3(u_0)+S_2(v_0)=7c/5\), so it lies on the boundary rather than in the strict improving set. Sharpness is obtained by taking, for sufficiently small \(\delta>0\),
\[
u_{\delta}=u_0-\delta,
\qquad
v_{\delta}=v_0+\frac65\delta.
\]
Then \(u_{\delta}+v_{\delta}>c\) and \(S_3(u_{\delta})+S_2(v_{\delta})>7c/5\), while the parameters remain in the same two facets. Using the source parameterization
\[
z(q)=\left(\frac{S(q)+q}{2},\frac{S(q)-q}{2}\right),
\]
the pairs \(x_{\delta}=z(u_{\delta})\), \(y_{\delta}=z(-v_{\delta})\) satisfy \(m_X(x_{\delta},y_{\delta})>c\) and
\[
d_X(x_{\delta},y_{\delta})\longrightarrow D_*.
\]
Thus the displayed upper bound is the exact supremum.

Finally, if \(\varepsilon\le1-D_*\), every pair with \(d_X(x,y)\ge1-\varepsilon\) has \(m_X(x,y)\le c\), while an exactly Birkhoff-orthogonal maximizing pair gives \(J_B^{\varepsilon}(X)\ge c\). Hence \(J_B^{\varepsilon}(X)=c\). If \(\varepsilon>1-D_*\), the sharpness family has both \(d_X(x_{\delta},y_{\delta})>1-\varepsilon\) and \(m_X(x_{\delta},y_{\delta})>c\) for small enough \(\delta\), so the profile is strictly larger than \(c\). Since
\[
1-D_*=rac{554788989}{19465125400},
\]
the claimed plateau is exact.

## Verification
The companion `activation_threshold_check.py` uses exact rational arithmetic to reconstruct all rational constants in the two-cell optimization. It verifies the feasibility endpoints, the derivative-sign endpoint tests, the strict comparison \(D_* > D_{22}^{\max}\), the identity \(1-D_*=554788989/19465125400\), and a rational member of the boundary-approaching sharpness family. Its SHA-256 digest is `2861b4e3c591a6dc2287a398df59da8ca9d7aba34a6c5151bcee82090d2ad146`.

The checker is supplementary. The proof of the infinite statement is the analytic monotonicity and boundary argument above; no finite sampling or timeout is used as a substitute for proof.

## Relationship to prior work
Fang--Xu--Liu--Gu--Li define the approximate Birkhoff--James profile and, for this same polygonal plane \(X\), prove \(J_B^{1/40}(X)=331/206\). Their Example 6 also computes the saturation threshold \(100999/3009900\), where the profile reaches the ordinary James constant. The inspected proof bounds the directed distance of every improving pair by \(39/40\); it does not optimize that bound to determine the exact first-departure point.

A published exact calculation of the orthogonal James constant for a different mixed Euclidean--taxicab plane determines only \(J_{\perp}\) for that other norm and explicitly leaves approximate-Birkhoff profiles outside its scope. The weighted Birkhoff-orthogonal James constant of Qi--Yin--Liu--Li varies coefficient weights under exact Birkhoff orthogonality rather than the approximation parameter considered here. Baronti--Papini provides the earlier exact-orthogonality background.

## Limitations
The result determines only the initial plateau of \(J_B^{\varepsilon}(X)\). It does not compute the intervening profile between first departure and saturation, does not determine the analogous first-departure threshold for the companion polygonal plane \(Y\), and does not claim a general formula for polygonal Banach planes. The proof relies on the facet reduction established in Example 6 of the focal source and then independently performs the exact optimization of that reduction. Because the focal paper is recent, an unindexed equivalent derivation under different terminology remains a residual literature risk.

## References
1. Z. Fang, Y. Xu, Q. Liu, Z. Gu, and Y. Li, *James-type constants for Birkhoff--James orthogonality and approximate isosceles*, arXiv:2609.37502v1, first submitted 2026-09-26.
2. *Exact orthogonal James constant of a mixed Euclidean--taxicab Banach plane*, published record `2026/10/4/SCOPE-exact-orthogonal-james-constant-of-a-mixed-euclidean-taxicab-ban--d257b41cb57c`.
3. M. Baronti and P. L. Papini, *Parameters in Banach spaces and orthogonality*, Constructive Mathematical Analysis 5 (2022), 37--45, DOI:10.33205/cma.1067323.
4. J. Qi, Z. Yin, Q. Liu, and Y. Li, *A weighted Birkhoff orthogonal James-type constant*, arXiv:2606.01068.

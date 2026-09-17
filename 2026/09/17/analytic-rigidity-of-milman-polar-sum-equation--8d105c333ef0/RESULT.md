# Analytic rigidity for Milman's polar-sum equation in the plane

## Result

For a planar convex body \(K\) containing the origin in its interior, write
\[
F_K(u)=h_K(u)-\frac1{\rho_K(u)},\qquad u\in S^1,
\]
where \(h_K\) and \(\rho_K\) are the support and radial functions.

Call \(K\) \(C^\omega_+\) if, in angular coordinates, its support function \(h_K(\theta)\) is real analytic and
\[
h_K(\theta)+h_K''(\theta)>0
\]
everywhere. This is the usual strictly positive-curvature analytic class.

**Theorem (analytic planar rigidity).**  
If \(K,L\subset\mathbb R^2\) are \(C^\omega_+\) convex bodies containing the origin and
\[
F_K=F_L,
\]
then \(K=L\).

Equivalently, if \(K,T\subset\mathbb R^2\) are \(C^\omega_+\) and
\[
K+T=K^\circ+T^\circ,
\]
then
\[
K=T^\circ.
\]

A stronger smooth obstruction holds.

**Flat-contact theorem.**  
Let \(K,L\) be \(C^\infty_+\) planar convex bodies with \(F_K=F_L\). If \(K\ne L\), then there is a direction \(\theta_*\in S^1\) at which
\[
\frac{d^j}{d\theta^j}\bigl(h_K-h_L\bigr)(\theta_*)=0
\qquad\text{for every }j\ge0.
\]
Thus any nontrivial positively curved smooth counterexample must contain an infinite-order support-function contact. Real analyticity excludes this possibility.

## Context

Segal introduced the same functional \(F_K\) in the study of Milman's equation
\[
K+T=K^\circ+T^\circ.
\]
After replacing \(T\) by \(L^\circ\), this equation is equivalent to
\[
K+L^\circ=K^\circ+L,
\]
hence to \(F_K=F_L\). Segal proved injectivity of \(F\) on polytopes and constructed non-injective examples among general convex bodies; the planar counterexamples are infinite polygons. The result here gives a different rigidity regime: positive curvature plus real analyticity in dimension two.

## Proof

Set
\[
\Delta=h_K-h_L,\qquad F=F_K=F_L.
\]
The argument uses Segal's support-to-radial monotonicity, together with a local calculation for polarity.

### 1. Monotone alternating directions

Suppose \(\Delta\not\equiv0\). Starting from a direction \(u_0\) with \(\Delta(u_0)\ne0\), use the unique support point of \(K\) when \(\Delta(u_j)>0\), and the unique support point of \(L\) when \(\Delta(u_j)<0\). Let \(u_{j+1}\) be the radial direction of that support point.

Segal's Lemma 7 gives
\[
\operatorname{sgn}\Delta(u_{j+1})=-\operatorname{sgn}\Delta(u_j)
\]
and
\[
F(u_{j+1})>F(u_j).
\]
Hence \(F(u_j)\) increases to a finite limit.

We need one quantitative refinement. Let \(A\) denote whichever of \(K,L\) is used at a given step. If \(x=r v\in\partial A\) is the support point with outer normal \(u\), put
\[
c=\langle u,v\rangle,\qquad h=h_A(u)=rc.
\]
Since \(h_A(v)\ge r\) and \(\rho_A(u)\le h_A(u)=h\),
\[
\begin{aligned}
F_A(v)-F_A(u)
&\ge \left(r-\frac1r\right)-\left(h-\frac1h\right)\\
&=(r-h)\left(1+\frac1{rh}\right)\\
&\ge r(1-c).
\end{aligned}
\]
If
\[
r_*=\min\{\min_{S^1}\rho_K,\min_{S^1}\rho_L\}>0,
\]
then
\[
F(u_{j+1})-F(u_j)\ge r_*\bigl(1-\langle u_j,u_{j+1}\rangle\bigr).
\]
Because the left side tends to zero, the angular distance between consecutive \(u_j\)'s tends to zero.

Choose a convergent subsequence of one parity, say \(u_{2j_k}\to u_*\). Then also
\[
u_{2j_k+1}\to u_*,\qquad u_{2j_k+2}\to u_*.
\]
The signs of \(\Delta\) alternate, so continuity gives \(\Delta(u_*)=0\). Continuity of the support-to-radial direction maps gives that, for both bodies, the support point with normal \(u_*\) lies on the ray \(u_*\).

Rotate coordinates so that \(u_*\) has angular coordinate \(0\). Writing \(h\) for either support function, a boundary point with normal angle \(\beta\) is
\[
x(\beta)=h(\beta)n(\beta)+h'(\beta)t(\beta).
\]
Its radial direction equals its normal exactly when \(h'(\beta)=0\). Therefore
\[
h_K(0)=h_L(0)=a>0,\qquad h_K'(0)=h_L'(0)=0.
\]

### 2. The second jets also agree

For a \(C^\infty_+\) support function \(h\), put
\[
q(\alpha)=h_{K^\circ}(\alpha)=\frac1{\rho_K(\alpha)}.
\]
With
\[
r(\beta)=\sqrt{h(\beta)^2+h'(\beta)^2},
\]
the radial angle of \(x(\beta)\) is
\[
\alpha(\beta)=\beta+\arctan\frac{h'(\beta)}{h(\beta)},
\qquad
q(\alpha(\beta))=\frac1{r(\beta)}.
\]
At a direction where \(h'(0)=0\), write
\[
a=h(0),\qquad b=h''(0),\qquad R=a+b>0.
\]
Direct differentiation gives
\[
\alpha'(0)=\frac Ra,\qquad
q''(0)=-\frac{b}{aR}.
\]
Consequently
\[
F''(0)=b+\frac{b}{a(a+b)}.
\]
For fixed \(a>0\), the right-hand side is a strictly increasing function of \(b>-a\), since its derivative is
\[
1+\frac1{(a+b)^2}>0.
\]
Because \(F_K=F_L\) and the two bodies have the same \(a\), we obtain
\[
h_K''(0)=h_L''(0).
\]
Let their common curvature radius there be
\[
R=a+h_K''(0)=a+h_L''(0)>0.
\]

### 3. A finite-order contact is impossible

Assume that \(\Delta=h_K-h_L\) is not flat at \(0\). Since its first two derivatives vanish, let \(m\ge3\) be the first order with nonzero coefficient:
\[
\Delta(\theta)=c\,\theta^m+o(\theta^m),\qquad c\ne0.
\]

We compare the polar support functions
\[
q_K=\frac1{\rho_K},\qquad q_L=\frac1{\rho_L}.
\]
For every positively curved planar body,
\[
q(\alpha)=\max_{\beta}\frac{\cos(\alpha-\beta)}{h(\beta)}.
\]
Near \((\alpha,\beta)=(0,0)\), the maximizing normal is unique and nondegenerate. Its expansion is
\[
\beta(\alpha)=\frac aR\,\alpha+O(\alpha^2).
\]
Because \(h_K-h_L\) first differs in order \(m\), the two maximizing normals differ only by \(O(\alpha^{m-1})\). Stationarity of the maximization implies that this displacement changes the maximal value only by \(O(\alpha^{2m-2})=o(\alpha^m)\).

Thus the leading difference comes from evaluating the reciprocal support functions at the common leading maximizer:
\[
\begin{aligned}
q_K(\alpha)-q_L(\alpha)
&=
-\frac{1}{a^2}\,
c\left(\frac aR\alpha\right)^m
+o(\alpha^m)\\
&=
-\frac{a^{m-2}}{R^m}\,c\,\alpha^m+o(\alpha^m).
\end{aligned}
\]
But \(F_K=F_L\) is exactly
\[
h_K-h_L=q_K-q_L.
\]
Comparing the first nonzero coefficient would require
\[
c=-\frac{a^{m-2}}{R^m}c,
\]
which is impossible because \(a,R>0\) and \(c\ne0\).

Therefore \(\Delta\) is flat at \(u_*\). This proves the flat-contact theorem.

If \(h_K,h_L\) are real analytic, a flat difference at one point vanishes in a neighborhood, hence everywhere on the connected circle. Thus \(h_K=h_L\) and \(K=L\).

Finally, in the original Milman equation, set \(L=T^\circ\). Positive curvature and real analyticity are preserved by polarity, so
\[
K+T=K^\circ+T^\circ
\quad\Longleftrightarrow\quad
F_K=F_{T^\circ}.
\]
The analytic rigidity theorem gives \(K=T^\circ\).

## Significance

The known general counterexamples show that Milman's equation is not rigid on all convex bodies, while the polytope theorem shows rigidity at the opposite combinatorial extreme. The result above identifies a second rigid regime in dimension two and, more sharply, shows that any \(C^\infty_+\) failure of rigidity must be invisible to every finite support-function jet at at least one contact direction.

This separates the analytic positive-curvature class from the known infinite-polygon mechanism and narrows any search for smooth counterexamples to genuinely non-analytic, infinite-order behavior.

## Limitations

- The theorem is two-dimensional.
- Positive curvature is assumed. It does not cover analytic convex bodies with degenerate curvature directions.
- The flat-contact theorem does not rule out \(C^\infty_+\) counterexamples with infinite-order contact.
- It does not classify translated self-polar bodies individually.
- Originality is to the best of our knowledge. The motivating preprint is very recent, so unindexed concurrent work remains a residual risk.

## Reference

1. Alex Segal, *Self-dual sets up to a translation: a negative answer to Milman's question*, arXiv:2609.12685 (2026). https://arxiv.org/abs/2609.12685

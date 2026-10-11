# Two-end asymptotics of the nonquadratic sharp functional Santaló extremizer

## Finding

For every integer \(n\ge2\), let \(a_n\in(0,1)\) be the unique maximizing parameter in the sharp slab Santaló theorem of Artstein-Avidan and set
\[
k_n=2\sqrt{a_n(1+a_n)^n}.
\]
Let \(r_n\) be the balanced equality profile oriented so that \(r_n(-1)=0\) and \(r_n(1)>0\). Let \(\varphi_n:\mathbb R^n\to[0,\infty)\) be the radial equality function whose projective body is
\[
K(r_n)=\{(x,t):\lVert x\rVert_2\le r_n(t),\ -1\le t\le1\}.
\]
Write
\[
\varphi_n(x)=h_n(\lVert x\rVert_2),
\qquad
c_{0,n}=\frac{k_n^{1/n}}{\sqrt2},
\qquad
c_{\infty,n}=\frac{\sqrt2}{k_n^{1/n}}.
\]
Then the equality function has the following exact two-end asymptotics:
\[
h_n(\rho)
=
c_{0,n}\rho
+\frac{\rho^{n+1}}{n(n+1)c_{0,n}^{n-1}}
+o(\rho^{n+1})
\qquad(\rho\downarrow0),
\]
and
\[
h_n(\rho)
=
c_{\infty,n}\rho
-\frac{(n+1)^{n/(n+1)}}{n}
c_{\infty,n}^{(2n+1)/(n+1)}
\rho^{1/(n+1)}
+o(\rho^{1/(n+1)})
\qquad(\rho\to\infty).
\]

In particular, \(\varphi_n\) is globally Lipschitz and its exact Lipschitz constant is \(c_{\infty,n}\). Its one-sided directional slope at the origin is \(c_{0,n}\). These slopes satisfy
\[
c_{0,n}c_{\infty,n}=1,
\qquad
c_{0,n}<c_{\infty,n}.
\]
Therefore the scalar maximizer obeys the strict constraint
\[
k_n<2^{n/2},
\qquad
 a_n(1+a_n)^n<2^{n-2}.
\]

The Legendre dual \(\mathcal L\varphi_n\) has
\[
\{\mathcal L\varphi_n=0\}=c_{0,n}B_2^n,
\qquad
\operatorname{dom}(\mathcal L\varphi_n)=c_{\infty,n}\operatorname{int}B_2^n.
\]
Thus the new nonquadratic equality pair has a precise primal-dual boundary geometry: the primal extremizer is conical to first order both at the origin and at infinity, with reciprocal slopes, while the dual extremizer has a flat zero ball and a bounded effective domain. The first nonlinear corrections occur at the sharply different powers \(n+1\) and \(1/(n+1)\).

## Assumptions and scope

The statement uses the balanced radial representative of the equality class. General equality functions are obtained from the two orientations by invertible linear changes of variables. Under such a change the Euclidean balls in the final display become the corresponding ellipsoids.

Only the exact equality functions from the recent theorem are considered. No stability estimate for near-extremizers is asserted. The expansion at infinity determines the entire effective domain of the Legendre dual: the boundary sphere is excluded because the negative sublinear correction makes the conjugate diverge there.

## Proof

The source proves that the balanced profile satisfies, on \((-1,1)\),
\[
-r_n''=r_n^{n-1}(r_n-tr_n')^{n+2},
\]
with endpoint data
\[
r_n(-1)=0,
\qquad
r_n'(-1+)=k_n^{-1/n},
\qquad
r_n(1)=k_n^{1/n},
\qquad
r_n'(1-)=-\infty.
\]
The projective correspondence in the source gives the radius \(R_n(z)\) of the sublevel ball \(\{\varphi_n\le z\}\):
\[
R_n(z)=\frac{1+z}{\sqrt2}\,
r_n\!\left(\frac{z-1}{z+1}\right),
\qquad z\ge0.
\]

Set \(a=k_n^{-1/n}\) and \(s=t+1\). From the endpoint data,
\[
r_n(t)=as+o(s),
\qquad
r_n'(t)=a+o(1),
\qquad
r_n(t)-tr_n'(t)\longrightarrow a.
\]
The profile equation therefore gives
\[
r_n''(t)=-a^{2n+1}s^{n-1}+o(s^{n-1}).
\]
Twice integrating from \(s=0\) yields
\[
r_n(-1+s)
=
as-\frac{a^{2n+1}}{n(n+1)}s^{n+1}+o(s^{n+1}).
\]
Since
\[
s=1+t=\frac{2z}{1+z},
\]
substitution into the projective radius gives
\[
R_n(z)
=
\sqrt2\,a z
-\frac{2^{n+1/2}a^{2n+1}}{n(n+1)}z^{n+1}
+o(z^{n+1})
\qquad(z\downarrow0).
\]
Inverting this strictly increasing sublevel-radius relation gives
\[
h_n(\rho)
=
\frac{\rho}{\sqrt2\,a}
+\frac{\rho^{n+1}}{n(n+1)(1/(\sqrt2 a))^{n-1}}
+o(\rho^{n+1}),
\]
which is the first expansion because \(1/(\sqrt2 a)=c_{0,n}\).

For the opposite endpoint put \(t=1-s\), \(q(t)=-r_n'(t)\), and \(b=k_n^{1/n}\). Then \(q(t)\to\infty\), \(r_n(t)\to b\), and
\[
\frac{q'(t)}{q(t)^{n+2}}
=
r_n(t)^{n-1}
\left(\frac{r_n(t)+tq(t)}{q(t)}\right)^{n+2}
\longrightarrow b^{n-1}.
\]
Consequently
\[
q(t)
\sim
\bigl((n+1)b^{n-1}(1-t)\bigr)^{-1/(n+1)}.
\]
Integrating once gives
\[
r_n(1-s)
=
b+
\frac{(n+1)^{n/(n+1)}}{n}
b^{-(n-1)/(n+1)}
s^{n/(n+1)}
+o\left(s^{n/(n+1)}\right).
\]
Using \(1-t=2/(1+z)\) in the projective formula gives
\[
R_n(z)
=
\frac{b}{\sqrt2}z
+B_n z^{1/(n+1)}+o\left(z^{1/(n+1)}\right)
\]
for an explicit positive coefficient \(B_n\). Inverting this relation and simplifying the coefficient gives
\[
h_n(\rho)
=
c_{\infty,n}\rho
-\frac{(n+1)^{n/(n+1)}}{n}
c_{\infty,n}^{(2n+1)/(n+1)}
\rho^{1/(n+1)}
+o\left(\rho^{1/(n+1)}\right).
\]

Since \(h_n\) is convex, radial, and vanishes at zero, its radial derivative is nondecreasing. The limiting derivative at infinity is therefore its exact global Lipschitz constant \(c_{\infty,n}\), while the derivative at the origin is \(c_{0,n}\). Their product is immediate from the definitions. If they were equal, convexity would force \(h_n(\rho)=c\rho\) for every \(\rho\ge0\). Its projective profile would then be affine in \(t\), contradicting the source endpoint fact \(r_n'(1-)=-\infty\). Hence \(c_{0,n}<c_{\infty,n}\), which is equivalent to the displayed strict bounds on \(k_n\) and \(a_n\).

Finally, for a proper closed convex function with \(\varphi_n(0)=0\), the zero set of the Legendre transform is exactly \(\partial\varphi_n(0)\). Radiality and the first expansion give
\[
\partial\varphi_n(0)=c_{0,n}B_2^n.
\]
If \(\lVert y\rVert_2<c_{\infty,n}\), the second expansion makes \(x\mapsto\langle x,y\rangle-\varphi_n(x)\) coercive from above, so \(\mathcal L\varphi_n(y)<\infty\). If \(\lVert y\rVert_2>c_{\infty,n}\), taking \(x\) on the ray through \(y\) makes the same expression tend to \(+\infty\). At the boundary \(\lVert y\rVert_2=c_{\infty,n}\), the negative correction in the second expansion gives \(\langle x,y\rangle-\varphi_n(x)=D_n\lVert x\rVert_2^{1/(n+1)}+o(\lVert x\rVert_2^{1/(n+1)})\) along the matching ray, with \(D_n>0\), so the conjugate again diverges. Hence the effective domain is exactly \(c_{\infty,n}\operatorname{int}B_2^n\).

## Verification

The proof uses exact endpoint data and the profile differential equation proved in the source. The two asymptotic integrations use limits of continuous expressions, not numerical fitting. The projective change of variables is the source identity
\[
t=\frac{z-1}{z+1}.
\]
The packaged checker independently verifies the coefficient simplifications for dimensions \(2\le n\le40\), the reciprocal-slope identity, and the equivalence between the strict slope inequality and \(a_n(1+a_n)^n<2^{n-2}\).

The checker is only an algebraic consistency test. The infinite family of asymptotic statements is proved analytically above.

## Relationship to prior work

Artstein-Avidan proves the sharp slab and functional Santaló inequalities, classifies their equality cases, derives the profile differential equation and its endpoint values, and gives the projective sublevel-set formula. The source also explicitly notes that one orientation vanishes only at the origin while the reflected orientation vanishes on a full-dimensional ellipsoid. It does not state either two-term functional asymptotic expansion, an exact global Lipschitz constant, the reciprocal pair of endpoint slopes, the exact effective domain of the Legendre dual, or the resulting strict inequality for the scalar maximizer \(a_n\).

A prior record derived the exponential-in-dimension size of the sharp constant relative to the quadratic benchmark from the same source. That statement concerns \(M_n\) and does not determine the local or large-radius geometry of an equality function, the exponents of its nonlinear corrections, or the parameter inequality above.

Targeted literature and statement-level searches using the source identifier together with “asymptotic expansion,” “Lipschitz,” “zero set,” “effective domain,” and the exponents \(n+1\) and \(1/(n+1)\) did not locate an equivalent statement. General facts about Legendre transforms explain the last domain interpretation once the new asymptotics are known, but do not supply those asymptotics.

## Limitations

The result is an exact analysis of the canonical radial equality representative. It does not provide a closed form for \(a_n\), and the bound \(a_n(1+a_n)^n<2^{n-2}\) is a consequence of the endpoint geometry rather than a sharp numerical localization of \(a_n\).

The expansion is transported to arbitrary equality functions by invertible linear changes, but no coordinate-free higher-order tensor expansion is claimed. No quantitative stability statement for near-equality functions is proved. The literature search is targeted; an equivalent asymptotic calculation in an unindexed note remains a residual originality risk.

## References

1. S. Artstein-Avidan, *A sharp Santaló inequality in a slab with centrally symmetric sections*, arXiv:2609.38041v1, first public 29 September 2026. Primary MSC 52A40.
2. S. Artstein-Avidan, B. Klartag, and V. Milman, *The Santaló point of a function, and a functional form of the Santaló inequality*, Mathematika 51 (2004), 33--48, DOI 10.1112/S0025579300015497.

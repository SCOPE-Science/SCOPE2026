# Sharp contact order at the diagonal end of Kim's Minkowski profiles

## Finding

Let \(m,n\ge1\). Consider a nontrivial \(O(m)\times O_1(n)\)-invariant zero-mean-curvature profile curve
\[
\gamma=(x,y)
\]
from Kim's classification whose phase trajectory tends to
\[
p_4=\left(\frac{\pi}{2},\frac{\pi}{4}\right).
\]
This is the phase point corresponding to a profile end approaching the origin with tangent angle \(\pi/4\).

On the branch with \(x>0\), there is a constant \(C>0\), depending only on the dilation of the profile, such that
\[
\boxed{
y(x)=x+C x^{2(m+n)+1}
+o\!\left(x^{2(m+n)+1}\right)
\qquad (x\downarrow0).
}
\]
Consequently the contact order with the diagonal ray \(y=x\) is exactly
\[
\boxed{2(m+n)+1.}
\]

Equivalently, if
\[
q=\frac{y'}{x'},
\qquad
r=\frac yx,
\]
then along this end
\[
\boxed{
\lim_{(x,y)\to(0,0)}
\frac{q-1}{r-1}
=
2(m+n)+1.
}
\]

Thus the angle statement \(y/x\to1\) from the classification hides a dimension-dependent high-order tangency: the deviation from the diagonal first appears at degree \(2(m+n)+1\).

## Assumptions and scope

Kim uses the phase coordinates
\[
\csc a=\frac{y'}{x'},
\qquad
\tan b=\frac yx,
\]
and the planar vector field
\[
a'=-\cos a\bigl(n\sin a\cos b+m\sin b\bigr),
\]
\[
b'=\sin b\cos b\bigl(\cos b-\sin a\sin b\bigr).
\]
The point
\[
p_4=\left(\frac{\pi}{2},\frac{\pi}{4}\right)
\]
is a saddle.

The claim concerns the nontrivial phase branch tending to \(p_4\), not the coordinate boundary orbit. The corresponding geometric profile is one of the classified curves with an end at the origin and angle \(\pi/4\).

The coefficient \(C\) is not scale invariant: dilating the profile changes \(C\). The exponent \(2(m+n)+1\), and the ratio limit above, are scale invariant.

## Proof

Put
\[
M=m+n,
\qquad
\alpha=a-\frac{\pi}{2},
\qquad
\beta=b-\frac{\pi}{4}.
\]
Taylor expansion of the source vector field at \(p_4\) gives
\[
\alpha'
=
\frac{M}{\sqrt2}\alpha
+
O\!\left(|\alpha\beta|+|\alpha|^3\right),
\]
and
\[
\beta'
=
-\frac1{\sqrt2}\beta
+
\frac1{4\sqrt2}\alpha^2
+
O\!\left(|\alpha|^3+|\alpha\beta|+\beta^2\right).
\]
Hence the eigenvalues are
\[
\lambda_u=\frac{M}{\sqrt2},
\qquad
\lambda_s=-\frac1{\sqrt2},
\]
so \(p_4\) is hyperbolic.

The nontrivial branch that tends to \(p_4\) in backward phase time is the local unstable manifold. Since its tangent is the \(\alpha\)-axis, write it as
\[
\beta=c\alpha^2+O(|\alpha|^3).
\]
Substitution in the invariance equation
\[
\frac{d\beta}{d\alpha}\,\alpha'=\beta'
\]
gives, at order \(\alpha^2\),
\[
\frac{2Mc}{\sqrt2}
=
\frac{1/4-c}{\sqrt2}.
\]
Therefore
\[
c=\frac1{4(2M+1)},
\]
and
\[
\boxed{
\beta=
\frac{\alpha^2}{4(2M+1)}
+
O(|\alpha|^3).
}
\]

Now convert back to the geometric quantities. Since
\[
q=\csc a
=\sec\alpha,
\]
we have
\[
q-1=\frac{\alpha^2}{2}+O(\alpha^4).
\]
Also
\[
r=\tan b
=
\tan\left(\frac\pi4+\beta\right),
\]
so
\[
r-1=2\beta+O(\beta^2)
=
\frac{\alpha^2}{2(2M+1)}
+
O(|\alpha|^3).
\]
Thus
\[
\frac{q-1}{r-1}\longrightarrow 2M+1.
\]

Because \(y=xr\),
\[
q=\frac{dy}{dx}=r+x\frac{dr}{dx}.
\]
Writing
\[
w=r-1>0
\]
on the nontrivial local branch, the preceding expansions give
\[
q-1=(2M+1)w+O(w^{3/2}).
\]
Therefore
\[
x\frac{dw}{dx}
=
q-r
=
2Mw+O(w^{3/2}).
\]
Equivalently,
\[
\frac{d\log w}{d\log x}
=
2M+O(w^{1/2}).
\]

Since the source classification gives \(x\downarrow0\) and \(w\to0\) at this end, the differential equation first implies two-sided power bounds
\[
x^{2M+\varepsilon}\ll w\ll x^{2M-\varepsilon}
\]
for every fixed small \(\varepsilon>0\). Hence the error term \(O(w^{1/2})\) is integrable with respect to \(d\log x\). It follows that
\[
\log\frac{w}{x^{2M}}
\]
has a finite limit. The nontriviality of the unstable branch makes the limiting multiplicative constant positive, so
\[
w=Cx^{2M}+o(x^{2M})
\]
for some \(C>0\). Since \(y=x(1+w)\),
\[
y=x+Cx^{2M+1}+o(x^{2M+1}),
\]
as claimed.

## Verification

The bundled symbolic checker reconstructs the two-variable Taylor expansion of the exact source vector field and verifies the unstable-manifold coefficient
\[
\frac1{4(2(m+n)+1)}.
\]
It independently verifies the induced leading coefficients of
\[
\csc a-1
\]
and
\[
\tan b-1,
\]
and therefore the ratio \(2(m+n)+1\).

No finite sampling is used to infer the theorem. The passage from the local phase expansion to the geometric power law is analytic and uses the exact identity
\[
\frac{dy}{dx}
=
\frac yx+x\frac{d}{dx}\left(\frac yx\right).
\]

## Relationship to prior work

Daehwan Kim classifies the relevant \(O(m)\times O_1(n)\)-invariant zero-mean-curvature profile curves. The paper introduces the coordinates
\[
\csc a=\frac{y'}{x'},
\qquad
\tan b=\frac yx,
\]
derives the phase vector field above, identifies \(p_4=(\pi/2,\pi/4)\) as a saddle, and states geometrically that the corresponding profile end approaches the origin with angle \(\pi/4\).

The inspected material does not give a higher-order expansion at that end. The result here refines the qualitative angle statement to the exact scale-invariant contact exponent \(2(m+n)+1\), together with a ratio limit that determines the exponent.

Targeted searches for the source identifier, the \(O(m)\times O_1(n)\) profile, higher-order diagonal asymptotics, contact order, and the explicit exponent found no covering result.

## Limitations

The coefficient \(C\) is not universal because the zero-mean-curvature equation and the profile family admit dilations. The theorem identifies the universal exponent and proves only that \(C>0\).

The result concerns the phase branch tending to \(p_4\). It does not provide corresponding higher-order expansions for every other node or saddle in the classification.

The publisher's downloadable PDF was not openly accessible during verification. The relevant phase equations and classification statements were available through the publisher-indexed text, and the bibliographic novelty conclusion retains the residual risk that a differently phrased higher-order calculation may occur in material not exposed by those indexed passages.

## References

1. Daehwan Kim, *Zero mean curvature submanifolds as generalizations of rotational surfaces in Minkowski space*, Annales Polonici Mathematici 136 (2026), 101--122, DOI 10.4064/ap250309-25-8, published online 9 March 2026.

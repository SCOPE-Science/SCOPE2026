# The universal endpoint-chord law for the Steiner inellipse of a triangle

## Finding

Let \(T\) be a nondegenerate Euclidean triangle, \(E\) its Steiner inellipse, and \(G\) their common centroid. Take two independent Euclidean arclength-uniform points \(X,Y\) on \(\partial T\). Let \(E_s=G+s(E-G)\) for \(0\le s\le1\), and let \(p_i\) be side length divided by perimeter. Write \(\sigma=\sum_i p_i^2\). For the **closed-segment, closed-ellipse** intersection event,
\[
 P_s=\Pr([X,Y]\cap E_s\ne\varnothing)=(1-\sigma)Q(s)+\frac{\sigma}{2}\,\mathbf1_{\{s=1\}}.
\]
Here \(Q(s)\) is the universal conditional probability for endpoints on different sides. For \(0<s<1\), put
\[
 \eta=\frac{\sqrt3s}{\sqrt{4-s^2}},\qquad a=(1-\eta)/2,\quad b=(1+\eta)/2,\qquad D(t)=t^2-t+1,
\]
\[
 F(t)=\left(1-\frac1t\right)\sqrt{D(t)}+\frac12\left[\operatorname{arsinh}\left(\frac{2t-1}{\sqrt3}\right)-\operatorname{arsinh}\left(\frac{2/t-1}{\sqrt3}\right)\right].
\]
Then
\[
 Q(s)=\frac{(8-s^2)(b-a)+(s^2-2)\log(b/a)+(1+s^2)(1/b-1/a)}9-\frac{2s}9\bigl(F(a)+F(b)\bigr).
\]
It is continuous on \([0,1]\), strictly increasing there, and satisfies
\[
 Q(0)=0,\qquad Q_*:=Q(1)=\frac23+\frac{2\log2}{9},\qquad
 Q(s)=\frac29\bigl(\sqrt3+\log(2+\sqrt3)\bigr)s+O(s^3)\quad(s\downarrow0),
\]
\[
 Q_*-Q(s)=\frac{1-s}{3}\log\frac1{1-s}+O(1-s)\quad(s\uparrow1).
\]
Thus \(P_s\) has a jump of size \(\sigma/2\) at full scale; the cusp describes its approach to the **left limit** after multiplication by \(1-\sigma\). For every fixed \(0<s\le1\) the hitting probability is strictly Schur-concave in the side fractions, with a unique maximum at the equilateral triangle and an unattained sharp infimum approached only at permutations of \((1/2,1/2,0)\). For \(0<s<1\), these extrema are \(2Q(s)/3\) and \(Q(s)/2\), respectively. At full scale the sharp range is
\[
 \frac7{12}+\frac{\log2}{9}<P_1\le \frac{11}{18}+\frac{4\log2}{27}.
\]

## Assumptions and scope

The sampling is independent Euclidean arclength on the perimeter, not an isotropic random-line model. The ellipse is its filled closed region and the segment includes its endpoints; contact counts, even without entering the ellipse's interior. The scale zero body is \(\{G\}\). The result does not optimize over other inellipses or assert the law for other boundary shapes or endpoint measures.

## Proof

**Different sides and affine reduction.** Condition on a particular ordered pair of distinct sides and place their common vertex at the origin in the affine reference triangle with vertices \((0,0),(1,0),(0,1)\). Conditional arclength-uniform positions become independent uniform coordinates \((u,0),(0,v)\), \(u,v\in(0,1)\). The Steiner inellipse is affinely natural and in the reference triangle its center is \(c=(1/3,1/3)\) and its equation is \(x_0^2+y_0^2+x_0y_0\le1/12\) in centered coordinates. Its support-radius matrix is \(B=\tfrac19\left(\begin{smallmatrix}1&-1/2\\-1/2&1\end{smallmatrix}\right)\). The chord line \(x/u+y/v=1\) cuts the triangle precisely in the chord; because \(E_s\) lies in the triangle, testing intersection with that line is exact. The normal \((1/u,1/v)\) gives
\[
 (3uv-u-v)^2\le s^2(u^2+v^2-uv).\tag{1}
\]
This criterion applies identically to each ordered distinct-side pair.

**Integration.** By symmetry use \(u=tz,v=z\) on \(u\le v\) with Jacobian \(z\). The allowed interval in \(z\) is \([z_-,z_+]\cap[0,1]\) with \(z_\pm=(1+t\pm s\sqrt{D(t)})/(3t)\). For \(0<s<1\) both endpoints are positive. They meet 1 at \(t=a\) for \(z_-\) and \(t=b\) for \(z_+\): squaring \(2t-1=\pm s\sqrt{D(t)}\) gives the stated roots, and their signs select the two branches. The interval is empty below \(a\), clipped at 1 on \([a,b]\), and unclipped beyond \(b\). Thus
\[
 Q(s)=\int_a^b\left[1-\frac{(1+t-s\sqrt{D(t)})^2}{9t^2}\right]dt+\frac{4s}{9}\int_b^1\!\frac{(1+t)\sqrt{D(t)}}{t^2}\,dt.\tag{2}
\]
Direct differentiation gives \(F'(t)=(1+t)\sqrt{D(t)}/t^2\), \(F(1)=0\). The nonradical integrand in the first term has primitive \(((8-s^2)t+(s^2-2)\log t+(1+s^2)/t)/9\). Its radical part contributes \(2s[F(b)-F(a)]/9\), and the second integral contributes \(-4sF(b)/9\). This gives the stated expression.

**Conditional endpoint behavior.** At 0 the equality in (1) has area zero. At 1 the difference of the sides of (1) factors as \(3uv(3uv-2u-2v+1)\). For \(u\ge1/2\) every \(v\in(0,1)\) succeeds; for \(0<u<1/2\), success requires \(v\ge(1-2u)/(2-3u)\). Integrating the excluded area gives \(1-Q_*=\int_0^{1/2}(1-2u)/(2-3u)\,du=1/3-2\log(2)/9\). The level sets in (1) have area zero, which gives continuity by dominated convergence. Strict increase between any two levels in \([0,1]\) follows because on \(u=v=w\) the tested scale is \(|3w-2|\), taking every value in \((0,1)\) for \(w\in(1/3,2/3)\); a point strictly between the two levels therefore has an open neighborhood counted only at the larger level.

At small \(s\), \(a,b=1/2\mp\sqrt3s/4+O(s^3)\), and \(F(1/2)=-[\sqrt3+\log(2+\sqrt3)]/2\). The nonradical integrand is \((8-s^2+(s^2-2)/t-(1+s^2)/t^2)/9\); on the symmetric short interval its constant term at \(s=0,t=1/2\) is zero, the linear term in \(t-1/2\) integrates to zero, and the remaining integral is \(O(s^3)\). Also \(F(a)+F(b)=2F(1/2)+O(s^2)\). Near 1 write \(\delta=1-s\). Then \(a=2\delta/3+O(\delta^2)\), \(b=1-a\), and elementary expansion gives
\[
 F(a)=-1/a+(\log a)/2+3/2-\log2+O(a),\qquad F(b)=O(a).
\]
The coefficient of \(1/a\) in the closed form is \(-\delta^2/9\), so this term is \(O(\delta)\). The coefficient of \(\log a\) is \((2-s^2-s)/9=\delta/3+O(\delta^2)\); the remaining terms consist of a constant and \(O(\delta)\). Continuity identifies the constant as \(Q_*\), proving the cusp.

**Same sides, endpoint jump, and shape.** The probability of different sides is \(1-\sigma\). At \(s<1\) same-side chords cannot hit because \(E_s\) is in the interior. At \(s=1\) the only point of a side belonging to \(E\) is its midpoint, and a same-side chord hits it exactly when the endpoints straddle that midpoint, up to zero-measure equality cases. The two possible endpoint orders have combined conditional probability \(2(1/2)(1/2)=1/2\). Summing over same sides gives exactly \(\sigma/2\). This explains why a single tangency point per side does not imply a zero contribution from segments. For \(0<s<1\), \(P_s\) has strictly negative coefficient of \(\sigma\) since \(Q(s)>0\); at 1 the coefficient is \(1/2-Q_*<0\). The sum of squares is strictly Schur-convex, with minimum \(1/3\) precisely at equal thirds and supremum \(1/2\) approached only at permutations of \((1/2,1/2,0)\) on the closure of the triangle-inequality domain \(0<p_i<1/2,\sum_i p_i=1\). This gives the sharp shape assertions and range.

## Verification

Run `python3 checker.py` with NumPy, SciPy and SymPy for symbolic and independent finite numerical checks. The checker integrates sections of the incidence polynomial at fixed first endpoint and separately checks the full closed-segment event by directly minimizing the ellipse quadratic along sampled physical segments. Same-side pairs are included; deliberately straddling and nonstraddling examples test tangency. The finite computations corroborate the proof, not its continuum quantifiers. For highly cancellation-prone \(s\) near 1, use (2) or high-precision arithmetic.

## Relationship to prior work

The Steiner inellipse, its midpoint tangencies, and its maximal-area property are classical. Steinerberger's kinematic random lines [1] and the isotropic-uniform sections of van der Jagt, Jongbloed and Vittorietti [2] do not have the independent boundary-endpoint law used here. The explicit conditional distribution, its logarithmic cusp and the sharp shape comparison for the closed intersection event concern the particular ellipse and sampling model above. Older equivalent calculations cannot be excluded.

## References

1. S. Steinerberger, *Quadratic Crofton and sets that see themselves as little as possible*, https://arxiv.org/abs/2211.03259, kinematic line model.
2. T. van der Jagt, G. Jongbloed and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, https://arxiv.org/abs/2305.02864, Definitions 1–2.
3. *Steiner Inellipse*, Wolfram MathWorld, https://mathworld.wolfram.com/SteinerInellipse.html, side-midpoint tangencies and centroid.

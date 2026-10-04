# Sharp anticanonical-volume maxima for canonical and terminal two-heavy weighted projective spaces
## Finding
For every integer \(r\ge2\), set
\[
X_{r,a,b}=\mathbb P(\underbrace{1,\ldots,1}_{r},a,b),\qquad 1\le a\le b,
\]
and write \(n=r+1\). Among the members with at worst canonical singularities,
\[
(-K_X)^n\le 6^r r^{r-1}.
\]
For \(r\ge3\), equality holds only for
\[
(a,b)=(2r,3r),
\]
whereas for \(r=2\) it holds exactly for \((a,b)=(1,3)\) and \((4,6)\).

Among the terminal members, the sharp maximum is \(64\) when \(r=2\), attained only by \((a,b)=(1,1)\). For every \(r\ge3\),
\[
(-K_X)^n\le \frac{(6r-5)^{r+1}}{6(r-1)^2},
\]
with equality only for
\[
(a,b)=(2r-2,3r-3).
\]

## Assumptions and scope
The base field is \(\mathbb C\), and \(r\ge2\). The spaces are ordinary well-formed weighted projective spaces; the result does not concern fake weighted projective spaces with additional class-group torsion. The anticanonical volume is the usual rational top self-intersection.

## Proof
Put \(d=b-a\). The two non-smooth affine charts have cyclic quotient types
\[
\frac1a(1^r,b),\qquad \frac1b(1^r,a).
\]
For \(d>0\), the Reid--Tai ages on the \(b\)-chart have numerators \(rk+[-kd]_b\), and those on the \(a\)-chart have numerators \(rk+[kd]_a\). The same elementary residue argument in the equal-weight case gives
\[
\text{canonical}\iff 0\le d\le r\ \text{ and }\ 1\le a\le r+d,
\]
\[
\text{terminal}\iff 0\le d<r\ \text{ and }\ 1\le a<r+d.
\]
Indeed, on the \(b\)-chart the element \(k=1\) forces \(d\le r\), while if \(rk<b\) then \([-kd]_b=b-kd\), so the age numerator is \(b+k(r-d)\). On the \(a\)-chart, when \(rk<a\), one has \([kd]_a=kd\), reducing the condition to \(a\le r+d\). Strict inequalities give terminality.

For weighted projective space,
\[
(-K_X)^n=\frac{(r+a+b)^{r+1}}{ab}.
\]
Thus, with \(b=a+d\), define
\[
V_r(a,d)=\frac{(r+2a+d)^{r+1}}{a(a+d)}.
\]
For fixed \(d\), differentiation gives
\[
\operatorname{sgn}\!\left(\frac{\partial}{\partial a}\log V_r(a,d)\right)
=\operatorname{sgn} q_{r,d}(a),
\]
where
\[
q_{r,d}(a)=2(r-1)a^2+2((r-1)d-r)a-d(d+r).
\]
Since \(r\ge2\), this quadratic opens upward and has exactly one positive zero (with the evident limiting interpretation at \(d=0\)). Hence on every allowed interval in \(a\), the maximum of \(V_r\) is attained at an endpoint.

For the canonical region the endpoint functions are
\[
L_r(d)=V_r(1,d)=\frac{(r+d+2)^{r+1}}{d+1},
\]
\[
U_r(d)=V_r(r+d,d)=\frac{3^{r+1}(r+d)^r}{r+2d}.
\]
Their logarithmic derivatives satisfy
\[
\frac{d}{dd}\log L_r(d)=\frac{rd-1}{(r+d+2)(d+1)},
\]
so the maximum of \(L_r\) on \(0\le d\le r\) occurs at \(d=0\) or \(d=r\), while
\[
\frac{d}{dd}\log U_r(d)=
\frac{r(r-2)+2d(r-1)}{(r+d)(r+2d)}\ge0.
\]
Therefore the upper endpoint is maximized at \(d=r\), where
\[
U_r(r)=6^r r^{r-1}.
\]
The lower endpoint at \(d=r\) satisfies
\[
\frac{6^r r^{r-1}}{L_r(r)}
=\frac1{2r}\left(\frac{3r}{r+1}\right)^r
\ge \frac{2^{r-1}}r\ge1,
\]
with equality only at \(r=2\). At \(d=0\),
\[
\frac{6^r r^{r-1}}{L_r(0)}
=\frac1{r(r+2)}\left(\frac{6r}{r+2}\right)^r
\ge\frac{3^r}{r(r+2)}>1.
\]
The last inequality follows from \(3^r>r(r+2)\) for \(r\ge2\). This proves the canonical bound and all equality cases.

For terminal spaces, when \(r=2\) the allowed pairs are exactly \((1,1)\), \((1,2)\), and \((2,3)\), with volumes \(64\), \(125/2\), and \(343/6\), respectively.

Assume now \(r\ge3\). The terminal upper endpoint is \(a=r+d-1\), giving
\[
T_r(d)=\frac{(3r+3d-2)^{r+1}}{(r+d-1)(r+2d-1)},\qquad 0\le d\le r-1.
\]
After clearing the positive denominator, the sign of its logarithmic derivative is the sign of
\[
6(r-1)d^2+(9r^2-21r+8)d+3(r-1)(r^2-3r+1),
\]
which is positive for \(r\ge3\) and \(d\ge0\). Hence \(T_r\) is strictly increasing and its maximum is
\[
T_r(r-1)=\frac{(6r-5)^{r+1}}{6(r-1)^2}.
\]
The other endpoint is again \(L_r(d)\), whose maximum on \(0\le d\le r-1\) lies at \(d=0\) or \(d=r-1\). At \(d=0\), comparison with \(T_r(r-1)\) reduces to
\[
\frac1{6(r-1)^2}\left(\frac{6r-5}{r+2}\right)^{r+1}>1;
\]
this holds at \(r=3\), and the weaker base bound \((6r-5)/(r+2)\ge5/2\) reduces this to \((5/2)^{r+1}>6(r-1)^2\); the ratio of successive left-to-right quotients is \((5/2)((r-1)/r)^2>1\) for \(r\ge3\). At \(d=r-1\), the ratio is
\[
\frac{r}{6(r-1)^2}\left(\frac{6r-5}{2r+1}\right)^{r+1}>1.
\]
For \(r=3\) this is \(28561/19208>1\); for \(r\ge4\), the base is at least \(2\), and \(r\,2^{r+1}/(6(r-1)^2)>1\); the latter holds at \(r=4\) and its successive ratio is \(2(r+1)(r-1)^2/r^3>1\). Thus no lower-endpoint case ties the upper endpoint, proving the terminal bound and uniqueness.

## Verification
The proof is symbolic. The accompanying script `verify_volume_two_heavy.py` independently enumerates the canonical and terminal parameter regions for every \(2\le r\le100\), evaluates the exact rational volume, and checks the two sharp formulas and all equality cases. It returns `VERIFY_OK r=2..100`. This finite sweep is a regression test, not the proof of the infinite statement.

## Relationship to prior work
Kasprzyk's work on fake weighted projective spaces gives general constraints on ordered weights for canonical and terminal singularities and explicitly relates those constraints to anticanonical degree. Those general results do not state the sharp two-heavy extremal formulas above or their equality cases.

Bäuerle later proved sharp anticanonical-degree bounds for fake weighted projective spaces in terms of dimension and Gorenstein index. That is a different optimization problem: the present theorem fixes the two-heavy shape \(\mathbb P(1^r,a,b)\), imposes only canonical or terminal singularities, and obtains closed formulas with exact extremizers in every dimension.

Targeted published-finding corpus searches located work on reflexive weighted-projective simplices and Ehrhart thresholds, but no statement implying these family-specific anticanonical-volume maxima.

## Limitations
The theorem is restricted to the family with exactly two possibly non-unit weights. It does not claim a global volume bound among all weighted projective spaces of a fixed dimension. The originality assessment is search-based; an equivalent elementary optimization could exist under different notation in older literature. The finite checker is corroborative only.

## References
1. A. M. Kasprzyk, *Bounds on Fake Weighted Projective Space*, arXiv:0805.1008, first posted 2008-05-07.
2. A. Bäuerle, *Sharp degree bounds for fake weighted projective spaces*, arXiv:2207.01709, first posted 2022-07-04.
3. M. Reid, *Young person's guide to canonical singularities*, Proc. Sympos. Pure Math. 46 (1987), 345--414.

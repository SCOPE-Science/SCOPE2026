# A sharp uniform toroidal basin certificate for an attracting polynomial-field cycle

## Finding
For every \(\mu>0\), put
\[
\dot q=-2\mu q P(q,w),\qquad \dot w=\frac{q}{10}-w,\qquad
P(q,w)=21q^2-125q+400w^2+100.
\]
For each \(0<\delta\le 11/25\), define the balanced rectangle
\[
\mathcal R_\delta=[4-\delta,4+\delta]\times
\left[\frac{4-\delta}{10},\frac{4+\delta}{10}\right].
\]
It is positively invariant and every solution starting in it tends to \((q,w)=(4,2/5)\). The bound \(\delta\le11/25\) is exact within this whole prescribed rectangle family: any \(11/25<\delta<4\) yields an outward-pointing vector on its left edge. In the cylindrical realization \(q=x^2+y^2\), \(w=-z\), this gives a parameter-uniform, full-azimuth basin certificate for the attracting circular orbit at \(x^2+y^2=4\), \(z=-2/5\).

## Assumptions and scope
The positive scalar \(\mu\) is unrestricted. Solutions obey the displayed smooth autonomous two-dimensional polynomial equations. The rectangle family is chosen by centering on the equilibrium and making the vertical endpoints equal to one tenth of the horizontal endpoints, following the exact relaxation nullcline \(w=q/10\). The assertion of *sharpness* concerns only this geometrically motivated family, not all possible trapping regions or the entire attraction basin. The lift assumes the published rotational realization whose radial/height equations coincide with the displayed system and whose invariant circle is periodic; angular dynamics play no role in the basin calculation.

## Proof
Set \(a=4-\delta\), \(b=4+\delta\), \(c=a/10\), and \(d=b/10\). As \(0<\delta\le11/25\), all four endpoints are positive, and \(P\) increases strictly with \(w\) there. Direct expansion gives
\[
P(a,d)=\delta(25\delta-11)\le0,\qquad
P(b,c)=\delta(25\delta+11)>0.
\]
Therefore \(\dot q\ge0\) along the left edge \(q=a\), and \(\dot q<0\) along the right edge \(q=b\). Along \(w=c\), \(\dot w=(q-a)/10\ge0\); along \(w=d\), \(\dot w=(q-b)/10\le0\). The rectangle is positively invariant, including its possibly tangent upper-left corner at \(\delta=11/25\). Its compactness and local Lipschitz continuity give global forward existence for all starts inside.

The only equilibria with \(q>0\) satisfy \(w=q/10\) and
\[
P(q,q/10)=25(q-1)(q-4)=0.
\]
The smaller equilibrium \((1,1/10)\) is outside the rectangle, so \((4,2/5)\) is its unique equilibrium. Its Jacobian is
\[
J=\begin{pmatrix}-344\mu&-2560\mu\\1/10&-1\end{pmatrix},
\qquad \operatorname{tr}J=-344\mu-1<0,\quad \det J=600\mu>0.
\]
It is a strict sink for every \(\mu>0\).

To exclude all periodic orbits in the rectangle, compute
\[
\operatorname{div}(\dot q,\dot w)=-1-2\mu E(q,w),\quad
E(q,w)=63q^2-250q+400w^2+100.
\]
Throughout \(\mathcal R_\delta\), \(\partial_q E=126q-250>0\) and \(\partial_wE=800w>0\), so its minimum occurs at \((a,c)\) and is
\[
E(a,c)=67\delta^2-286\delta+172\ge
E(4-11/25,(4-11/25)/10)=\frac{36957}{625}>0.
\]
The inequality follows since the quadratic is decreasing on \([0,11/25]\). Thus the divergence is strictly negative on an open neighborhood of the rectangle, and the Bendixson criterion excludes interior periodic orbits. No periodic orbit can be supported on the boundary, because every non-tangent edge has inward pointing flow and the only tangent corner immediately enters the interior. The Poincaré–Bendixson alternative on this compact positively invariant planar set, which contains only one equilibrium and that equilibrium is a sink, now implies convergence of every trajectory to \((4,2/5)\).

Finally, if \(11/25<\delta<4\), at the included upper-left corner \((a,d)\),
\[
\dot q=-2\mu a\,\delta(25\delta-11)<0.
\]
The horizontal component points strictly outside the rectangle, so positive invariance fails. This proves the exact threshold. Under \(q=x^2+y^2\), \(w=-z\), convergence of the reduced variables is exactly convergence in distance to the invariant circle, regardless of angular phase.

## Verification
The independent algebraic boundary expansions, equilibrium polynomial, Jacobian trace/determinant, and divergence margin can be checked with the included stand-alone exact-arithmetic program `VERIFY.py` using Python and SymPy. These computations check polynomial identities; the all-time convergence is established by the planar proof above, not by finite integration. The packaged checker is run from the package itself.

## Relationship to prior work
Castañeda and Rebollo-Perdomo (arXiv:2610.09176v1, first public 6 October 2026) construct a rotational polynomial vector field with two circular orbits and identify the outer one as attracting. The accessible mathematical account states the same planar radial/height reduction and reports local stability. The present statement is a quantitative global-initial-data certificate for that orbit, valid for all positive radial parameters, with a sharp width in a canonical balanced box. Local orbital attraction alone does not specify such a parameter-uniform set or its sharp boundary. General basin approximation methods and Bendixson criteria do not supply this family-specific threshold without the explicit edge calculation. The complete full text of the originating preprint was not accessible, so detailed priority against any unpublished or unindexed basin estimate is not established.

## Limitations
This is not an exact characterization of the full basin. The sharpness is only among the displayed centered, nullcline-balanced rectangles. No claim is made about global Hurwitzness of the entire parameter half-line, nor about angular frequencies away from the periodic circle. Prior-art comparison is best-effort rather than certified: the originating preprint's full mathematical text was inaccessible, and the available secondary summary may omit relevant results. No independent audit has been performed.

## References
Castañeda, Á., and Rebollo-Perdomo, S., *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1, first submitted 6 October 2026, https://arxiv.org/abs/2610.09176.

Giesl, P., and Wendland, H., *Approximating the basin of attraction of time-periodic ODEs by meshless collocation*, Discrete and Continuous Dynamical Systems 25 (2009), 1249–1274, DOI:10.3934/dcds.2009.25.1249.

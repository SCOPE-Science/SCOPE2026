# Boundary attractors and exact degeneration rates for largest-dihedral-angle bisection

## Result

Consider the tetrahedral family
\[
T_c(t,b)=\operatorname{conv}\{O,P,A,B\},
\]
with
\[
O=(0,0,0),\qquad P=(0,0,1),\qquad
A=(tb,0,0),\qquad B=(bc,bs,0),
\]
where \(0<c<1\), \(s=\sqrt{1-c^2}\), \(b>0\), and \(t>0\).  This is the natural one-parameter extension of the invariant family used by Korotov--Michaud for their largest-dihedral-angle-bisection (LAB) counterexample.

If \(t<c\), the edge \(PA\) is the unique edge carrying an obtuse internal dihedral angle, while the other five dihedrals are acute or right. Hence \(PA\) is the unique LAB edge. Retaining the child incident to \(OP\) and relabeling the two base rays gives the exact recurrence
\[
 b^+=tb,
 \qquad
 t^+=F_c(t,b):=
 \frac{1}{t+\sqrt{1+t^2-2ct+(1-c^2)t^2b^2}}.
\tag{1}
\]

The recurrence has a sharp boundary-attractor regime.

**Theorem.** Let
\[
\frac1{\sqrt2}<c<1.
\]
There is a unique \(\tau=\tau(c)\in(1/\sqrt2,c)\) satisfying
\[
\boxed{\;2c\tau^3-3\tau^2+1=0.\;}
\tag{2}
\]
There are \(\varepsilon>0\) and \(b_*>0\) such that every initial condition
\[
|t_0-\tau|<\varepsilon,\qquad 0<b_0<b_*,
\]
generates an infinite tie-free LAB branch under (1), and for some orbit-dependent constant \(C\in(0,\infty)\),
\[
\boxed{\;b_n=C\tau^n(1+o(1)),\qquad t_n\to\tau.\;}
\tag{3}
\]
More precisely,
\[
\boxed{
 t_n-\tau\sim K(c)b_n^2,
 \qquad
 K(c)=
 -\frac{(1-c^2)\tau^4}{q_*(2\tau^2+1)}<0,
 \qquad
 q_*:=\frac{1-\tau^2}{\tau}.
}
\tag{4}
\]
The boundary fixed point has the universal transverse multiplier
\[
\boxed{\;f_c'(\tau)=-\frac12,\;}
\qquad
f_c(t):=F_c(t,0).
\tag{5}
\]

Thus the counterexample dynamics are asymptotically self-similar rather than merely trapped between two geometric bounds.

## A continuum of exact degeneration rates

Solving (2) for \(c\) gives
\[
\boxed{
 c=c(\tau)=\frac{3\tau^2-1}{2\tau^3}.
}
\tag{6}
\]
On \(\tau\in(1/\sqrt2,1)\), this function is strictly increasing from \(1/\sqrt2\) to \(1\). Consequently every asymptotic per-cut aspect-ratio multiplier
\[
\boxed{\;\Lambda\in(1,\sqrt2)\;}
\]
is realized by this LAB mechanism, by choosing \(\tau=1/\Lambda\) and then \(c\) from (6).

The threshold \(c=1/\sqrt2\) is exact for this boundary-fixed-point mechanism: for \(c>1/\sqrt2\), the fixed point obeys \(\tau<c\), so \(PA\) remains the uniquely obtuse LAB edge near the attractor; at \(c=1/\sqrt2\), one has \(\tau=c\), and that strict selected-edge margin disappears. For \(c<1/\sqrt2\), equation (2) has no fixed point in the regime \(0<\tau<c\). This is a threshold for this invariant-family construction, not a classification of all LAB orbits.

## Sharp geometric asymptotics

Let \(r_n\), \(h_n\), \(V_n\), and \(\varphi_n\) denote respectively the inradius, diameter, volume, and the face angle \(\angle OPA_n\) of the branch tetrahedron. With \(s=\sqrt{1-c^2}\), (3) implies
\[
 a_n=t_nb_n\sim C\tau^{n+1},
 \qquad
 \varphi_n=\arctan a_n\sim C\tau^{n+1},
\tag{7}
\]
\[
 h_n-1\sim\frac{C^2}{2}\tau^{2n},
 \qquad
 V_n\sim\frac{sC^2\tau}{6}\tau^{2n}.
\tag{8}
\]
The exact inradius formula is
\[
 r_n=
 \frac{a_nb_ns}{a_n+b_n+a_nb_ns+W_n},
\qquad
 W_n=b_n\sqrt{1+t_n^2-2ct_n+s^2t_n^2b_n^2},
\tag{9}
\]
so
\[
\boxed{
 r_n\sim
 \frac{\tau^2s}{1+\tau}\,C\tau^n.
}
\tag{10}
\]
Since \(h_n\to1\),
\[
\boxed{
 \frac{h_n}{r_n}
 \sim
 \frac{1+\tau}{C\tau^2s}\,\tau^{-n}.
}
\tag{11}
\]
In particular the true asymptotic growth factor of the diameter-to-inradius ratio is exactly \(1/\tau\), not merely a lower-bound base.

The limiting dihedral geometry is also rigid. From the exact dihedral formulas,
\[
 \cos\theta_{PB}\to x:=\frac{1-c\tau}{q_*},
 \qquad
 \cos\theta_{PA}\to y:=\frac{\tau-c}{q_*}.
\]
Equation (2) implies
\[
 y=2x^2-1.
\]
Since \(\theta_{PB}\in(0,\pi/2)\) and \(\theta_{PA}\in(\pi/2,\pi)\),
\[
\boxed{\;\theta_{PA}^{(\infty)}=2\theta_{PB}^{(\infty)}.\;}
\tag{12}
\]
Thus the degenerate boundary attractor is an angle-bisector equilibrium: the selected limiting dihedral is exactly twice the adjacent limiting dihedral that replaces it after relabeling.

## Specialization to the published counterexample

Korotov--Michaud fix
\[
c=\frac78,\qquad s=\frac{\sqrt{15}}8,
\]
and prove that the rectangle
\[
\frac34\le t\le\frac45,
\qquad
0<b\le\frac14
\]
is invariant under (1), with a unique LAB edge at every step. On this whole rectangle,
\[
|\partial_tF_c(t,b)|<\frac{16}{25},
\]
so every orbit in the rectangle converges to the same boundary attractor. Here
\[
\boxed{\;7\tau^3-12\tau^2+4=0,\;}
\]
with
\[
\tau=0.7835533375134631256254383986\ldots,
\qquad
\tau^{-1}=1.276237305265537021379018886\ldots.
\tag{13}
\]
For the paper's seed \((t_0,b_0)=(3/4,1/4)\),
\[
C=0.2398563383657047471865642657\ldots,
\]
\[
K=-0.0804857780204679713556608052\ldots,
\]
and
\[
\frac{\tau^2s}{1+\tau}=0.1666505190405041528322233389\ldots.
\]
Hence
\[
\boxed{
 \frac{h_n}{r_n}
 \sim
 25.0173975461904455576\ldots\,(1.2762373052655370214\ldots)^n.
}
\tag{14}
\]
This sharpens the published lower bound proportional to \((5/4)^n\). The limiting relevant dihedrals are
\[
\theta_{PB}\to 50.34832520938\ldots^\circ,
\qquad
\theta_{PA}\to100.69665041876\ldots^\circ.
\tag{15}
\]

## Proof

For the family above, the outward-normal formulas used in the source paper remain valid with arbitrary \(c\in(0,1)\) and \(s=\sqrt{1-c^2}\). If \(t<c\), then
\[
\cos\theta_{PA}\propto t-c<0,
\]
while
\[
1-ct>1-c^2>0
\]
for the \(PB\) dihedral, and the remaining dihedrals are acute or right. Hence \(PA\) is uniquely largest. The spatial angle-bisector formula then gives (1).

At \(b=0\), a fixed point \(\tau\in(0,1)\) obeys
\[
\frac1\tau=\tau+\sqrt{1+\tau^2-2c\tau}.
\]
Squaring gives (2). Put \(p_c(t)=2ct^3-3t^2+1\). For \(c>1/\sqrt2\),
\[
p_c(1/\sqrt2)>0,
\qquad
p_c(c)=(c^2-1)(2c^2-1)<0,
\]
and
\[
p_c'(t)=6t(ct-1)<0\qquad(0<t<c).
\]
Therefore there is a unique root \(\tau\in(1/\sqrt2,c)\).

At the fixed point,
\[
q_*:=\sqrt{1+\tau^2-2c\tau}=\frac{1-\tau^2}{\tau}.
\]
Differentiating \(f_c(t)=F_c(t,0)\) gives
\[
f_c'(\tau)
=-\tau^2\frac{1-c\tau}{1-\tau^2}.
\]
Equation (2) is equivalent to
\[
2\tau^2(1-c\tau)=1-\tau^2,
\]
which proves (5).

Because \(-1/2\) is strictly inside the unit disk and \(\tau<c<1\), continuity provides a rectangle around \((\tau,0)\), contained in \(t<c\), on which \(F_c\) contracts in the \(t\)-direction and \(b^+=tb\) contracts in the \(b\)-direction. Shrinking the rectangle if necessary makes it forward invariant. Moreover
\[
F_c(t,b)-F_c(t,0)=O(b^2)
\]
uniformly there. Standard contraction estimates therefore give \(t_n\to\tau\), \(b_n\to0\), and \(\sum_n|t_n-\tau|<\infty\). Since
\[
\frac{b_n}{\tau^n}=b_0\prod_{k=0}^{n-1}\frac{t_k}{\tau},
\]
the logarithm of the product converges absolutely, proving (3) with \(C>0\).

For the next term, set \(\delta_n=t_n-\tau\) and \(u_n=b_n^2\). Taylor expansion of (1) at \((\tau,0)\) gives
\[
\delta_{n+1}
=-\frac12\delta_n+g u_n+o(|\delta_n|+u_n),
\qquad
 g=-\frac{(1-c^2)\tau^4}{2q_*}.
\]
Also \(u_{n+1}/u_n=t_n^2\to\tau^2\). Because \(\tau^2>1/2\), the forcing scale \(u_n\) decays more slowly than the homogeneous multiplier \(1/2\). Dividing by \(u_{n+1}\) yields an asymptotic affine contraction for \(\delta_n/u_n\), whose fixed point is
\[
K=\frac{g}{\tau^2+1/2},
\]
which is (4).

Equations (7)--(11) follow from the coordinate formulas, \(b_n\sim C\tau^n\), and the tetrahedral identity \(r=3V/S\). Finally, substituting (2) into the limiting dihedral cosines gives
\[
\frac{\tau-c}{q_*}
-
\left(2\left(\frac{1-c\tau}{q_*}\right)^2-1\right)=0,
\]
which proves (12).

For \(c=7/8\), the source paper already proves invariance of the larger rectangle. On that rectangle the numerator in
\[
\partial_t(t+Q)=1+\frac{t-c+(1-c^2)tb^2}{Q}
\]
is negative after the leading 1 but the full derivative remains positive; hence the bracket in \(|\partial_tF|=F^2\partial_t(t+Q)\) lies in \((0,1)\). Since \(F\le4/5\), \(|\partial_tF|<16/25\), which extends convergence to the full published invariant rectangle.

## Relation to prior work and originality boundary

Korotov--Michaud (arXiv:2609.18788) introduce the fixed value \(c=7/8\), derive the exact recurrence, prove the invariant rectangle, and obtain the geometric bounds
\[
b_n\in\left[\frac14(3/4)^n,\frac14(4/5)^n\right]
\]
together with a lower bound on \(h_n/r_n\) proportional to \((5/4)^n\). Their paper does not state the boundary fixed point, the cubic rate, the universal multiplier \(-1/2\), the second-order law (4), the general \(c\)-family, the \((1,\sqrt2)\) continuum of exact degeneration multipliers, or the limiting angle-doubling relation.

Related longest-edge-bisection work studies tetrahedral refinement as a discrete dynamical system and exhibits attracting, elliptic, or degenerating behavior, but it concerns a different edge-selection and midpoint-bisection rule. Those dynamical ideas are prior context, not claimed as new here.

To the best of our knowledge, searches by the source identifier and title, by the exact cubic and numerical root, and by synonymous combinations of largest-dihedral-angle bisection, fixed points, attractors, asymptotic degeneration rates, and tetrahedral mesh regularity did not locate these formulas or the general rate family. Because the source paper is extremely recent, simultaneous follow-up work remains a material residual originality risk.

## Limitations

The general theorem concerns the invariant geometric family above and a local basin near its degenerate boundary fixed point. It does not prove that a full-dimensional open set in the complete tetrahedral shape space degenerates, nor does it classify all LAB branches or all possible rates. The threshold \(c=1/\sqrt2\) is sharp only for this boundary-fixed-point mechanism. The asymptotic constants are exact in exact arithmetic; no finite-precision mesh-generation analysis is given.

## Reproducibility

`artifacts/verify_asymptotics.py` performs exact symbolic checks of the fixed-point and angle-doubling identities and high-precision numerical checks of the source specialization and representative general-parameter examples. `artifacts/verification_output.txt` records its output.

## References

1. S. Korotov and J. Michaud, *Largest-dihedral-angle bisection algorithm does not preserve mesh regularity for tetrahedral partitions*, arXiv:2609.18788 (2026). https://arxiv.org/abs/2609.18788
2. K. A. Adiprasito, D. Kalmanovich, and Y. Solomon, *Degenerating orbits of the Longest Edge Bisection process*, arXiv:2609.08846 (2026). https://arxiv.org/abs/2609.08846
3. J. Michaud and S. Korotov, *On the orbits of similarity classes of tetrahedra generated by the longest-edge bisection algorithm*, Applications of Mathematics 71 (2026), 137--162. https://doi.org/10.21136/AM.2026.0277-25

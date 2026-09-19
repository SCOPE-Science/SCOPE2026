# A universal self-similar degeneration rate for largest-dihedral-angle bisection

## Result

Korotov and Michaud (arXiv:2609.18788) exhibit an invariant two-parameter family for largest-dihedral-angle bisection (LAB). With
\[
c=\frac78,\qquad s=\frac{\sqrt{15}}8,
\]
the family is
\[
T(a,b)=\operatorname{conv}\{O,P,A,B\},\qquad
A=(a,0,0),\quad B=(bc,bs,0),
\]
where
\[
0<b\le \frac14,\qquad \frac34\le t:=\frac ab\le\frac45.
\]
The retained LAB child again belongs to the family and satisfies
\[
b_{n+1}=t_n b_n,
\]
\[
t_{n+1}=F(t_n,b_n):=
\frac{1}{t_n+\sqrt{1+t_n^2-2ct_n+s^2t_n^2b_n^2}}.
\]
The source paper uses the invariant interval to obtain coarse geometric bounds. The recurrence in fact has a unique universal asymptotic profile throughout this invariant family.

Let \(\tau\) be the unique root in \((3/4,4/5)\) of
\[
\boxed{7\tau^3-12\tau^2+4=0.}
\]
Numerically,
\[
\boxed{\tau=0.7835533375134631256\ldots},\qquad
\boxed{\tau^{-1}=1.2762373052655370214\ldots}.
\]
Then for every initial \((t_0,b_0)\) in the invariant region,
\[
\boxed{t_n\to\tau}
\]
and there is a constant \(C=C(t_0,b_0)>0\) such that
\[
\boxed{b_n\sim C\tau^n,\qquad a_n\sim C\tau^{n+1}.}
\]
Thus the entire invariant family, not only the published seed, has the same asymptotic geometric contraction factor.

There is also a universal second-order shape law:
\[
\boxed{t_n=\tau+K b_n^2+o(b_n^2),}
\]
where
\[
\boxed{
K=-\frac{s^2\tau^5}{(1-\tau^2)(2\tau^2+1)}
=-0.08048577802046797\ldots .
}
\]
In particular the normalized shape ratio approaches its limit from below eventually, at the slower forcing scale \(b_n^2\), rather than at the linearized fixed-point scale alone.

## Exact geometric consequences

For \(T(a,b)\), put
\[
Q=\sqrt{1+t^2-2ct+s^2t^2b^2}.
\]
The four face areas give the exact inradius
\[
\boxed{
r(T(a,b))=
\frac{tbs}{1+t+Q+tbs}.
}
\]
Since at the limiting fixed point
\[
Q_* = \sqrt{1+\tau^2-2c\tau}=\frac1\tau-\tau,
\]
we obtain
\[
\boxed{
\frac{r_n}{b_n}\longrightarrow
R_*:=\frac{s\tau^2}{1+\tau}
=0.16665051904050415\ldots .
}
\]
The diameter is \(h_n=\sqrt{1+b_n^2}\to1\). Hence
\[
\boxed{
\frac{(h_{n+1}/r_{n+1})}{(h_n/r_n)}\to\tau^{-1}
=1.2762373052655370\ldots,
}
\]
and more precisely
\[
\boxed{
\frac{h_n}{r_n}\sim
\frac{1+\tau}{s\tau^2 C}\,\tau^{-n}.
}
\]
The source paper proves the lower bound \(h_n/r_n\geq (64/\sqrt{15})(5/4)^n\) for its seed. The exact asymptotic growth base is therefore \(1/\tau\approx1.27624\), strictly larger than the lower-bound base \(5/4\).

The vanishing face angle and volume also have exact rates:
\[
\angle OPA_n=\arctan(a_n)\sim C\tau^{n+1},
\]
\[
\operatorname{vol}(T_n)=\frac{a_nb_ns}{6}
\sim \frac{s\tau C^2}{6}\,\tau^{2n}.
\]
Consequently
\[
\frac{\angle OPA_{n+1}}{\angle OPA_n}\to\tau,
\qquad
\frac{r_{n+1}}{r_n}\to\tau,
\qquad
\frac{\operatorname{vol}(T_{n+1})}{\operatorname{vol}(T_n)}\to\tau^2.
\]

For the specific seed of arXiv:2609.18788,
\[
t_0=\frac34,\qquad b_0=\frac14,
\]
the asymptotic amplitude is numerically
\[
C=0.23985633836570475\ldots .
\]
Thus
\[
b_n\sim0.23985633836570475\,\tau^n,
\]
while
\[
\frac{h_n}{r_n}\sim25.0173975462\ldots\,\tau^{-n}.
\]

## Limiting dihedral profile

The degeneration is asymptotically self-similar in its nonvanishing angular data. From the source formulas,
\[
\cos\theta_{PA,n}=\frac{t_n-c}{Q_n},\qquad
\cos\theta_{PB,n}=\frac{1-ct_n}{Q_n}.
\]
At the fixed point these converge to
\[
\theta_{PA,*}=100.6966504188\ldots^\circ,
\qquad
\theta_{PB,*}=50.3483252094\ldots^\circ,
\]
and in fact
\[
\boxed{\theta_{PA,*}=2\theta_{PB,*}.}
\]
The other limiting dihedrals are
\[
\theta_{OP}=\arccos(7/8)=28.9550243719\ldots^\circ,
\qquad
\theta_{OA}=\theta_{OB}=\theta_{AB,*}=90^\circ.
\]
Thus the branch loses shape regularity at an exactly quantifiable exponential rate while its internal dihedral geometry converges to a nondegenerate fixed angular profile.

## Proof

Define the limiting one-dimensional map
\[
F_0(t):=F(t,0)
=\frac1{t+q(t)},\qquad
q(t)=\sqrt{1+t^2-2ct}.
\]
On \(I=[3/4,4/5]\), one has \(t<c\) and \(q(t)>|t-c|\). Therefore
\[
F_0'(t)
=-F_0(t)^2\left(1+\frac{t-c}{q(t)}\right),
\]
with the parenthetical factor strictly between zero and one. Since \(F_0(t)\le4/5\), \(F_0\) is a strict contraction on \(I\). Its fixed point satisfies
\[
1=t^2+tq(t).
\]
Because \(q(t)=t^{-1}-t\) at a fixed point, squaring gives
\[
3t^2-2ct^3=1,
\]
which for \(c=7/8\) is exactly
\[
7t^3-12t^2+4=0.
\]
This cubic is strictly decreasing on \([3/4,4/5]\) and changes sign there, so the fixed point \(\tau\) is unique.

The invariant-range result of arXiv:2609.18788 gives
\[
b_n\le b_0(4/5)^n\to0.
\]
Moreover, uniformly for \(t\in I\),
\[
F(t,b)-F_0(t)=O(b^2),
\]
because the only \(b\)-dependence is the additive term \(s^2t^2b^2\) under a square root bounded away from zero. The perturbed-contraction recurrence therefore gives \(t_n\to\tau\); in fact \(\sum_n|t_n-\tau|<\infty\). Since
\[
b_n=b_0\prod_{j=0}^{n-1}t_j,
\]
the convergent product
\[
C=b_0\prod_{j=0}^{\infty}\frac{t_j}{\tau}
\]
exists and is positive, yielding \(b_n\sim C\tau^n\) and \(a_n=t_nb_n\sim C\tau^{n+1}\).

For the second-order law, expand about \((\tau,0)\):
\[
t_{n+1}-\tau
=A(t_n-\tau)+C_*b_n^2
+o(|t_n-\tau|+b_n^2),
\]
where
\[
A=F_0'(\tau),\qquad
C_*=-\frac{s^2\tau^4}{2Q_*}.
\]
The fixed-point identity implies exactly
\[
A=-\frac12.
\]
Also \(b_{n+1}^2/b_n^2=t_n^2\to\tau^2>1/2\). Dividing the expansion by \(b_{n+1}^2\) and using the resulting asymptotic affine contraction gives
\[
\frac{t_n-\tau}{b_n^2}\to
\frac{C_*}{\tau^2-A}
=-\frac{s^2\tau^5}{(1-\tau^2)(2\tau^2+1)}.
\]

For the inradius formula, the tetrahedron has volume \(abs/6\) and face areas
\[
\frac{abs}{2},\quad \frac a2,\quad \frac b2,\quad \frac W2,
\]
where \(W=bQ\). Since \(r=3V/S\), substitution gives the displayed exact formula. All geometric asymptotics follow directly.

Finally, at \(b=0,t=\tau\), let \(\alpha=\theta_{PA,*}\), \(\beta=\theta_{PB,*}\). Substituting \(Q_*=(1-\tau^2)/\tau\) into \(\cos\alpha-(2\cos^2\beta-1)\) reduces it to
\[
-\frac{(7\tau-8)(7\tau^3-12\tau^2+4)}{32(1-\tau^2)^2}=0.
\]
The angle ranges force \(\alpha=2\beta\).

## Reproducibility

`artifacts/verify_lab_asymptotics.py` uses only the Python standard library. It computes the algebraic fixed point, iterates the exact recurrence for the published seed and three additional initial points in the invariant family, evaluates the second-order coefficient and inradius limit, and checks the consecutive geometric ratios and limiting dihedral relation. `artifacts/verification_output.txt` is the captured output.

## Originality boundary

The invariant family, exact LAB recurrence, unique-largest-dihedral property, conforming realization, and the published coarse degeneration bounds are due to Korotov and Michaud. Dynamical-systems viewpoints for longest-edge bisection, including projective and similarity-class dynamics, are also prior art. The present claim is restricted to the source-specific LAB recurrence: the universal attracting fixed profile throughout its invariant region, the algebraic contraction factor \(\tau\), the second-order shape law, and the resulting exact asymptotic rates for inradius, quality ratio, vanishing face angle, volume, and limiting dihedral profile.

Searches for the source title and identifier together with `fixed point`, `self-similar`, `attractor`, `asymptotic`, and equivalent mesh-degeneration terminology did not locate these conclusions. The inspected source itself states the recurrence and coarse bounds but does not state a fixed point or asymptotic-rate theorem. Related longest-edge-bisection literature concerns a different refinement rule. To the best of our knowledge, the result above is not covered there.

## Limitations

The theorem applies to the explicit invariant LAB family with fixed base-ray angle \(\arccos(7/8)\); it does not prove attraction from an open neighborhood in the full tetrahedral shape space. It is an asymptotic characterization of the already-degenerating branch, not a repair of LAB and not a statement about every branch from every tetrahedron. The constant \(C\) depends on the initial point and is represented by a convergent product rather than a closed elementary form.

## References

1. S. Korotov and J. Michaud, *Largest-dihedral-angle bisection algorithm does not preserve mesh regularity for tetrahedral partitions*, arXiv:2609.18788, 2026. https://arxiv.org/abs/2609.18788
2. K. A. Adiprasito, D. Kalmanovich, and Y. Solomon, *Degenerating orbits of the Longest Edge Bisection process*, arXiv:2609.08846, 2026. https://arxiv.org/abs/2609.08846
3. S. Korotov, *The longest-edge bisection algorithm may produce degenerating tetrahedra*, arXiv:2608.23139, 2026. https://arxiv.org/abs/2608.23139
4. J. Michaud and S. Korotov, *On the orbits of similarity classes of tetrahedra generated by the longest-edge bisection algorithm*, Applications of Mathematics 71 (2026), 137–162. https://doi.org/10.21136/AM.2026.0277-25

# Correcting the optimal reversal strength in an environment-assisted entanglement-restoration scheme

## Finding

Consider the third environment-assisted weak-measurement-reversal scheme of Xu, Cheng, Liu, Su, Wang, and Zhang. Both qubits undergo equal amplitude damping of strength
\[
d\in(0,1),
\]
the environment of the second qubit is measured, and a reverse weak measurement of strength
\[
q\in[0,1]
\]
is applied to that qubit after the favorable environmental outcome.

Write
\[
r=1-d,
\qquad
y=1-q.
\]
The source's own equations for this scheme reduce to
\[
C_3(q)=\frac{2r\sqrt y}{r+y},
\qquad
P_3(q)=\frac{r+y}{2},
\]
where \(C_3\) is the concurrence and \(P_3\) is the success probability.

The concurrence has the unique global maximum
\[
\boxed{q_*=d}
\]
with
\[
\boxed{C_{3,\max}=\sqrt{1-d}}
\]
and
\[
\boxed{P_3(q_*)=1-d}.
\]

The source instead states
\[
q_{\mathrm{pub}}=2d-d^2.
\]
At that value,
\[
1-q_{\mathrm{pub}}=(1-d)^2=r^2,
\]
so the source's reported "optimal" values are
\[
C_{\mathrm{pub}}=\frac{2r}{1+r},
\qquad
P_{\mathrm{pub}}=\frac{r(1+r)}{2}.
\]
For every
\[
0<d<1,
\]
the corrected point is strictly better in both coordinates:
\[
C_{3,\max}-C_{\mathrm{pub}}
=
\frac{\sqrt r(1-\sqrt r)^2}{1+r}>0
\]
and
\[
P_3(q_*)-P_{\mathrm{pub}}
=
\frac{r(1-r)}{2}>0.
\]

The complete concurrence-success Pareto frontier of this one-parameter scheme is also explicit. The dominated branch is
\[
d<q\le1.
\]
The efficient branch is
\[
0\le q\le d.
\]
Equivalently, on writing \(P=P_3(q)\), the Pareto frontier is
\[
r\le P\le\frac{1+r}{2},
\qquad
C_{\mathrm{Pareto}}(P)
=
\frac{r\sqrt{2P-r}}{P}.
\]

Hence the reversal strength identified as optimal in the source lies strictly inside the dominated branch for every nontrivial damping strength. Any later comparison in that paper that substitutes the stated scheme-three optimum must therefore be recomputed with \(q=d\).

## Assumptions and scope

The result concerns only the source's third scheme, with equal amplitude-damping strengths on the two qubits and the source's single reverse weak measurement after a favorable environment measurement. The open range
\[
0<d<1
\]
is used to make the strict inequalities nondegenerate.

The concurrence and success-probability formulas are the source formulas for both Bell-state families treated in that scheme. The result does not change the definitions of the first or second scheme and does not assert global optimality over all environment-assisted operations, all weak-measurement protocols, or all quantum channels.

The statement that subsequent comparisons require recomputation is limited to calculations that explicitly substitute the source's scheme-three "optimal" concurrence or corresponding success probability. No claim is made here about the final sign or ranking of every such recomputed comparison.

## Proof

The source gives, for its third scheme,
\[
C_3
=
\frac{2(1-d)\sqrt{1-q}}
{(1-d)+(1-q)}
\]
and
\[
P_3
=
\frac{(1-q)+(1-d)}{2}.
\]
Set
\[
r=1-d\in(0,1),
\qquad
y=1-q\in[0,1].
\]
Then
\[
C_3(y)=\frac{2r\sqrt y}{r+y}.
\]
For
\[
y>0,
\]
direct differentiation gives
\[
\frac{dC_3}{dy}
=
\frac{r(r-y)}
{\sqrt y\,(r+y)^2}.
\]
Therefore \(C_3\) is strictly increasing on
\[
0<y<r
\]
and strictly decreasing on
\[
r<y\le1.
\]
Its unique global maximum is at
\[
y=r,
\]
which is exactly
\[
q=d.
\]
Substitution yields
\[
C_{3,\max}
=
\frac{2r\sqrt r}{2r}
=
\sqrt r
=
\sqrt{1-d}
\]
and
\[
P_3(q=d)
=
\frac{r+r}{2}
=
r
=
1-d.
\]

The value printed in the source is
\[
q_{\mathrm{pub}}
=
2d-d^2
=
1-r^2.
\]
Hence
\[
y_{\mathrm{pub}}=r^2
\]
and
\[
C_{\mathrm{pub}}
=
\frac{2r^2}{r+r^2}
=
\frac{2r}{1+r},
\]
while
\[
P_{\mathrm{pub}}
=
\frac{r+r^2}{2}
=
\frac{r(1+r)}2.
\]

The concurrence difference simplifies as
\[
\sqrt r-\frac{2r}{1+r}
=
\frac{\sqrt r(1+r)-2r}{1+r}
=
\frac{\sqrt r(1-\sqrt r)^2}{1+r},
\]
which is strictly positive for \(0<r<1\). Likewise,
\[
r-\frac{r(1+r)}2
=
\frac{r(1-r)}2>0.
\]
Thus the corrected optimum strictly dominates the published point in both concurrence and success probability.

For the Pareto statement, observe that \(P_3\) is strictly increasing in \(y\). On
\[
0\le y<r
\]
both \(P_3(y)\) and \(C_3(y)\) strictly increase as \(y\) increases, so every such point is dominated by the point \(y=r\). On
\[
r\le y\le1,
\]
the success probability increases while the concurrence decreases, so no two distinct points dominate one another. Hence the efficient set is exactly
\[
r\le y\le1,
\]
equivalently
\[
0\le q\le d.
\]
Since
\[
P=\frac{r+y}{2},
\]
we have
\[
y=2P-r,
\]
and substitution into the concurrence formula gives
\[
C_{\mathrm{Pareto}}(P)
=
\frac{r\sqrt{2P-r}}{P}.
\]

## Verification

`verify_scheme3_optimum.py` independently evaluates the source formulas, the analytic derivative, the corrected optimum, the published point, and the Pareto inequalities on a dense deterministic grid of damping and reversal strengths. It also reconstructs the source concurrence from the normalized \(X\)-state formula for the representative Bell-state branch.

The finite checks are supplementary. The all-parameter conclusion follows from the derivative and strict inequalities proved above.

## Relationship to prior work

Xu, Cheng, Liu, Su, Wang, and Zhang derive the third-scheme concurrence and success probability as their equations (25a) and (25b). Immediately afterward they state equations (26a) and (26b) as the optimal concurrence and corresponding success probability and select
\[
q^O=2d-d^2
\]
in their equation (27). Their later scheme-three comparisons explicitly use those stated optimal quantities.

The correction above starts from the source's displayed equations (25a) and (25b) without changing the physical model. The derivative shows that equation (27) does not maximize equation (25a). In fact, the corrected point \(q=d\) also has a strictly larger success probability, so the discrepancy is not a fidelity-versus-yield convention.

A later survey of weak-measurement protection schemes cites the 2015 paper as part of the environment-assisted weak-measurement literature. Targeted searches for the paper's DOI together with the corrected condition \(q=d\), the published value \(2d-d^2\), concurrence optimization, errata, and correction terminology did not locate a published correction of this scheme-three optimization.

## Limitations

This is a correction and exact Pareto analysis of one displayed one-parameter scheme, not a new entanglement-restoration architecture. It does not show that the corrected third scheme globally dominates the source's first two schemes or every earlier weak-measurement protocol.

The literature search cannot exclude an unindexed correction, private note, thesis, or equivalent observation written with a different parameter convention. The direct source itself is nevertheless decisive about the formulas and the value it labels optimal.

The exact first public date used for the source metadata is the dated author-uploaded full text. Bibliographic databases also record later journal-publication dates; those later dates are not used as the archive anchor.

## References

1. X.-M. Xu, L.-Y. Cheng, A.-P. Liu, S.-L. Su, H.-F. Wang, and S. Zhang, “Environment-assisted entanglement restoration and improvement of the fidelity for quantum teleportation,” *Quantum Information Processing* 14 (2015), 4147–4162, DOI: 10.1007/s11128-015-1111-0.
2. S. Harraz, S. Cong, and J. J. Nieto, “Comparison of quantum state protection against decoherence via weak measurement, a survey,” *International Journal of Quantum Information* 20 (2022), 2250007, arXiv:2109.12842, DOI: 10.1142/S0219749922500071.

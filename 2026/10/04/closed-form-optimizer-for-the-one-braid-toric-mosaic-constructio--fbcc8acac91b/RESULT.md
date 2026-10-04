# Closed-form optimizer for the one-braid toric-mosaic construction
## Finding
For coprime integers \(2\le p<q\), let \(N_1(p,q)\) be the minimum of \(q-h-v\) over nonnegative integer pairs \((h,v)\) satisfying the one-braid inequalities of Heiney--Kipe--Pezzimenti--Pontes--Ta: \(q-2(h+v+p)+4\ge0\), \(h+3v\le q-3p+4\), \(3h+v\le q-p+4\), and \(h\ge v\). The feasible set is nonempty exactly when \(q\ge3p-4\). On that domain, \(N_1(p,q)=3p-4\) for \(3p-4\le q\le4p-4\), while for \(q\ge4p-3\), \(N_1(p,q)=p-2+\lceil q/2\rceil+\mathbf 1_{q\equiv2\pmod4}\). Consequently their Theorem 1 gives the explicit solver-free bound \(m_T(T(p,q))\le N_1(p,q)\).

Equivalently, the optimal one-braid size is
\[
N_1(p,q)=
\begin{cases}
3p-4, & 3p-4\le q\le 4p-4,\\
p-2+\lceil q/2\rceil+\mathbf 1_{q\equiv2\pmod 4}, & q\ge4p-3.
\end{cases}
\]
The second branch has a genuine residue-class penalty: when \(q\equiv2\pmod4\), the integer optimum is one tile larger than the naive half-integral relaxation suggests.

## Assumptions and scope
Here \(T(p,q)\) is a torus knot with coprime integers \(2\le p<q\), and \(m_T\) is the toric mosaic number in the longitudinal convention of Heiney--Kipe--Pezzimenti--Pontes--Ta. The quantity \(N_1(p,q)\) is the exact optimum of their *one-braid* integer program, not a claim that the actual toric mosaic number equals this upper bound. If \(q<3p-4\), the one-braid system has no nonnegative integer solution; this does not preclude other toric-mosaic constructions.

For \(3p-4\le q\le4p-4\), an optimal pair is
\[
(h,v)=(q-3p+4,0).
\]
For \(q\ge4p-3\), explicit optimal pairs are
\[
(h,v)=
\begin{cases}
(q/4+1,\;q/4-p+1), & q\equiv0\pmod4,\\
((q+3)/4,\;(q-4p+3)/4), & q\equiv1\pmod4,\\
((q+2)/4,\;(q-4p+2)/4), & q\equiv2\pmod4,\\
((q+1)/4,\;(q-4p+5)/4), & q\equiv3\pmod4.
\end{cases}
\]

## Proof
Write \(s=h+v\). The published system contains
\[
2s\le q-2p+4,\qquad h+3v\le q-3p+4,\qquad 3h+v\le q-p+4,
\]
with \(h\ge v\ge0\).

First, \(h+3v\ge0\), so feasibility forces \(q\ge3p-4\). Conversely, if \(q\ge3p-4\), the pair \((0,0)\) is feasible, proving the exact feasibility threshold.

Suppose \(3p-4\le q\le4p-4\). Since \(v\ge0\),
\[
s=h+v\le h+3v\le q-3p+4.
\]
The pair \((h,v)=(q-3p+4,0)\) attains equality. Its remaining two inequalities reduce to \(q\le4p-4\). Hence \(s_{\max}=q-3p+4\) and \(N_1=q-s_{\max}=3p-4\).

Now suppose \(q\ge4p-3\). The first displayed inequality gives
\[
s\le\left\lfloor\frac{q-2p+4}{2}\right\rfloor.
\]
If \(q\not\equiv2\pmod4\), the appropriate pair in the residue-class display above is nonnegative, satisfies \(h\ge v\), and attains this upper bound on \(s\). Substitution verifies the other two inequalities.

It remains to explain the extra unit when \(q\equiv2\pmod4\). Put \(t=h-v\). If equality held in \(2s\le q-2p+4\), then the other inequalities become \(t\le p\) and \(t\ge p\), so \(t=p\). But integral \(h=(s+t)/2\) and \(v=(s-t)/2\) require \(s\equiv t\pmod2\). For \(q\equiv2\pmod4\), the equality value \(s=q/2-p+2\) has parity opposite to \(p\), a contradiction. Thus one must have \(s\le q/2-p+1\). The displayed \(q\equiv2\pmod4\) pair attains that value, so the penalty is exactly one. Subtracting \(s_{\max}\) from \(q\) gives the stated formula for \(N_1\).

## Verification
The accompanying `artifacts/verify_one_braid_closed_form.py` independently enumerates the published integer constraints for all \(2\le p\le30\) and \(p<q\le150\), compares every optimum with the closed form, checks the explicit witnesses, reproduces all entries of the source paper's \(p=3\) Table 1, and checks the source's \(p=2\) and \(p=4\) corollaries. It reports `VERIFY_OK`. This finite replay is a consistency check; the proof above establishes the infinite statement.

## Relationship to prior work
Heiney--Kipe--Pezzimenti--Pontes--Ta state the four one-braid inequalities and minimize \(q-(h+v)\), but describe the optimum as obtained by integer linear programming. They give a general \(p=2\) corollary, a finite \(p=3\) table, and a general \(p=4\) corollary. Their companion `toric.py` implements the same four constraints with an integer solver. The formula here solves that published integer program for every admissible \(p\) and \(q\), revealing both the feasibility threshold and the \(q\equiv2\pmod4\) parity correction.

Targeted searches for the formula, its residue-class form, the feasibility threshold, and the phase transition did not locate a prior statement of this all-parameter optimizer. Nearby indexed knot-theory findings concern different invariants such as layered torus-knot triangulations and stick numbers, and do not imply this one-braid toric-mosaic optimum.

## Limitations
This result does not prove that \(N_1(p,q)\) is the toric mosaic number. The source paper's full-braid construction can improve the one-braid bound for infinitely many \(p=2\) knots, and other constructions may improve it elsewhere. Originality checks covered the primary manuscript, its companion implementation, targeted statement searches, and a semantic research index; uncatalogued parallel work remains a residual risk.

## References
1. K. Heiney, M. Kipe, S. Pezzimenti, K. Pontes, and L. Ta, *Constructions of and Bounds on the Toric Mosaic Number*, arXiv:2504.02265v1, first posted 2025-04-03; Topology and its Applications 377 (2026), 109657, DOI 10.1016/j.topol.2025.109657.
2. Companion implementation: `margekk/toric-mosaics-2025`, `toric.py`, blob `c643508b97694371a35d1ccf3a96adf2bf765b42`.

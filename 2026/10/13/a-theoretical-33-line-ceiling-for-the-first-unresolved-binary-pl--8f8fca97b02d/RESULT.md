# A theoretical \(33\)-line ceiling for the first unresolved binary plane-cap parameter
## Finding

Let
\[
n_2(5,2,2;2)
\]
denote the maximum size of a multiset of lines in
\[
\operatorname{PG}(4,2)
\]
such that every plane contains at most two line copies.

Then
\[
32\le n_2(5,2,2;2)\le33.
\]

The lower bound \(32\) is already present in the recent source. The new contribution is the theoretical upper bound \(33\), improving the source interval
\[
32\le n_2(5,2,2;2)\le34.
\]

There is also a rigidity statement at the remaining unresolved value. Any hypothetical \(33\)-line configuration is necessarily simple: no geometric line can occur twice.

For such a hypothetical simple configuration, write
\[
d_P
\]
for the number of selected lines through a point \(P\), and put
\[
S=\sum_P\binom{d_P}{2}.
\]
Then
\[
111\le S\le115.
\]
If \(x_j\) is the number of planes containing exactly \(j\) selected lines, the only possible occupancy triples are
\[
(x_0,x_1,x_2)
\in
\{
(35,9,111),
(36,7,112),
(37,5,113),
(38,3,114),
(39,1,115)
\}.
\]

Thus only one integer value remains open, and a putative \(33\)-line extremizer is forced into a narrow simple incidence regime.

## Assumptions and scope

The definition is the one used by D'haeseleer and Kurz:
\[
n_q(r,h,f;s)
\]
is the largest cardinality of a multiset of \((h-1)\)-spaces in
\[
\operatorname{PG}(r-1,q)
\]
such that every codimension-\(f\) subspace contains at most \(s\) multiset elements.

For
\[
(q,r,h,f,s)=(2,5,2,2,2),
\]
the objects are lines in
\[
\operatorname{PG}(4,2),
\]
and the constrained subspaces are planes.

The source proves
\[
32\le n_2(5,2,2;2)\le34.
\]
Its upper bound is obtained through its general inequalities together with an integer linear program in the simple case.

The argument below handles line multiplicities directly and uses only incidence counts in
\[
\operatorname{PG}(4,2).
\]

## Proof

The space
\[
\operatorname{PG}(4,2)
\]
has \(31\) points and \(155\) planes. Every line contains \(3\) points and lies in \(7\) planes.

Let \(\mathcal L\) be an admissible multiset of \(m\) line copies. For each point \(P\), let
\[
d_P
\]
be the number of line copies through \(P\), and define
\[
S=\sum_P\binom{d_P}{2}.
\]

For each plane \(\pi\), let
\[
y_\pi\in\{0,1,2\}
\]
be its line-copy occupancy, and define
\[
J=\sum_\pi\binom{y_\pi}{2}.
\]

Let \(D\) be the number of unordered pairs of copies that are copies of the same geometric line. Since every plane has occupancy at most two, no geometric line can have multiplicity larger than two.

Consider one unordered pair of selected line copies.

If the copies lie on two distinct intersecting geometric lines, the pair contributes \(1\) to \(S\) and \(1\) to \(J\): the lines share one point and span one plane.

If they are copies of the same geometric line, the pair contributes \(3\) to \(S\), because the line has three points, and \(7\) to \(J\), because the line lies in seven planes.

If the two geometric lines are skew, they contribute to neither sum.

Therefore
\[
J=S+4D.
\]

Now suppose
\[
m=34.
\]
Counting line-point incidences gives
\[
\sum_P d_P=3m=102.
\]
Among \(31\) nonnegative integers of total \(102\), convexity of
\[
d\longmapsto\binom d2
\]
gives the minimum by making the degrees differ by at most one:
\[
S\ge
22\binom32+9\binom42
=
120.
\]
Thus
\[
J\ge120.
\]

On the other hand, counting line-plane incidences gives
\[
\sum_\pi y_\pi=7m=238.
\]
Since every
\[
y_\pi\in\{0,1,2\},
\]
one has
\[
\binom{y_\pi}{2}\le\frac{y_\pi}{2},
\]
and hence
\[
J\le\frac{238}{2}=119.
\]
This contradiction proves
\[
m\le33.
\]

It remains to establish the rigidity assertion. Suppose
\[
m=33
\]
and a geometric line occurs twice. No other selected line can meet that doubled line, because the plane spanned by the two geometric lines would then contain the two copies of the doubled line and at least one further line copy.

Hence the three points on the doubled line each have degree exactly \(2\). The remaining \(28\) points carry total degree
\[
99-6=93.
\]
Convexity gives
\[
S
\ge
3\binom22+
19\binom32+
9\binom42
=
114.
\]
Since \(D\ge1\),
\[
J=S+4D\ge118.
\]
But
\[
\sum_\pi y_\pi=7\cdot33=231
\]
and therefore
\[
J\le\left\lfloor\frac{231}{2}\right\rfloor=115,
\]
a contradiction. Thus every \(33\)-line configuration is simple.

In the simple case
\[
D=0,
\qquad
J=S.
\]
Convexity applied to the total point degree
\[
\sum_Pd_P=99
\]
gives
\[
S\ge
25\binom32+6\binom42
=
111,
\]
while the plane-incidence bound gives
\[
S=J\le115.
\]

Finally,
\[
x_1+2x_2=231,
\qquad
x_2=J=S,
\qquad
x_0+x_1+x_2=155.
\]
Thus
\[
x_1=231-2S,
\qquad
x_0=S-76.
\]
For
\[
S\in\{111,112,113,114,115\},
\]
this gives exactly the five occupancy triples in the Finding.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It constructs
\[
\operatorname{PG}(4,2)
\]
from the nonzero vectors of
\[
\mathbb F_2^5.
\]
It independently enumerates all \(155\) lines, all \(155\) planes, and all \(31\) solids, and verifies that every line contains three points and lies in seven planes.

The verifier checks the numerical inequalities used in the proof, including the sharp convexity minima for \(m=34\) and for the doubled-line subcase at \(m=33\).

It also verifies a bundled explicit set of \(32\) distinct lines. Every bundled triple is checked to be a projective line, and every one of the \(155\) planes is tested directly. The witness has plane-occupancy distribution
\[
43\text{ planes of occupancy }0,
\qquad
112\text{ planes of occupancy }2,
\]
so it certifies the known lower bound \(32\) without relying on an external solver.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

D'haeseleer and Kurz introduce the general quantities
\[
n_q(r,h,f;s)
\]
and their dual blocking parameters, motivated by generalized Hamming weights of additive codes. Their Lemma 7.6 records
\[
32\le n_2(5,2,2;2)\le34.
\]
For the simple maximum-multiplicity-one case, the source explicitly uses integer linear programming to obtain the upper bound \(34\).

The new argument sharpens the upper endpoint to \(33\) by a direct two-level pair count: point-pair multiplicities are compared with plane-pair multiplicities, with repeated lines contributing an exact correction. The same accounting also shows that a hypothetical \(33\)-line configuration must be simple and restricts its plane occupancy spectrum to five possibilities.

Focused searches for this exact parameter, for \(33\)-line plane-capped sets in
\[
\operatorname{PG}(4,2),
\]
and for equivalent generalized-Hamming-weight formulations did not locate a prior \(33\) upper bound or the rigidity statement.

## Limitations

The exact value remains unresolved between
\[
32
\]
and
\[
33.
\]
The argument does not classify the known \(32\)-line witnesses or decide whether a \(33\)-line configuration exists.

The result is specific to the first binary parameter
\[
n_2(5,2,2;2).
\]
The same pair-counting method may yield inequalities for other parameters, but no general formula is claimed.

The lower bound \(32\) is prior work. The supplied witness serves only as a self-contained verification anchor; novelty is claimed for the theoretical upper bound \(33\) and the necessary structure of a possible \(33\)-line extremizer.

## References

1. Jozefien D'haeseleer and Sascha Kurz, *Generalized Hamming weights of additive codes and geometric counterparts*, arXiv:2512.16327v1, first public version 18 December 2025; Designs, Codes and Cryptography (2026), DOI 10.1007/s10623-026-01889-9.

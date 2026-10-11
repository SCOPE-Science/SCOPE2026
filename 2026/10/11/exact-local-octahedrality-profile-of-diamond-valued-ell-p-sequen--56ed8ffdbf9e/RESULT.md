# Exact local-octahedrality profile of diamond-valued \(\ell_p\) sequence spaces
## Finding
Let \(\Gamma\) be an infinite set and let
\[
1\le p<\infty.
\]
Put
\[
Z_p=\ell_p(\Gamma;\ell_1^2).
\]
For \(x\in S_{Z_p}\), define
\[
\sigma_{Z_p}(x)
=
\sup_{y\in S_{Z_p}}
\min\{\|x+y\|,\|x-y\|\}.
\tag{1}
\]
For every \(\gamma\in\Gamma\) and every
\[
z=(z_1,z_2)\in S_{\ell_1^2},
\]
the complete one-coordinate profile is
\[
\boxed{
\sigma_{Z_p}(e_\gamma\otimes z)
=
\max\left\{
2^{1/p},
2\|z\|_\infty
\right\}.
}
\tag{2}
\]

The associated quantitative local-octahedrality index
\[
s(X)=\inf_{x\in S_X}\sigma_X(x)
\tag{3}
\]
therefore satisfies
\[
\boxed{
s(Z_p)=2^{1/p}.
}
\tag{4}
\]
The infimum in (4) is attained at every one-coordinate point
\[
e_\gamma\otimes z
\]
with
\[
|z_1|=|z_2|=\frac12.
\]

## Assumptions and scope
All scalars are real. The fibre is exactly the two-dimensional diamond
\[
\ell_1^2.
\]
The index set \(\Gamma\) is infinite. The quantity in (3) is the sharp numerical version of the locally octahedral condition
\[
\forall x\in S_X\ \forall\varepsilon>0\ \exists y\in S_X:
\quad
\min\{\|x+y\|,\|x-y\|\}\ge s(X)-\varepsilon.
\]

The proof separates a two-dimensional fibre lemma from the outer \(\ell_p\) geometry.

## Proof
Fix
\[
z=(z_1,z_2)\in S_{\ell_1^2}.
\]
By coordinate permutations and sign changes in \(\ell_1^2\), it is enough to write
\[
z=(\alpha,\beta),
\qquad
\beta=1-\alpha,
\qquad
0\le\alpha\le\frac12.
\tag{5}
\]
Thus
\[
\|z\|_\infty=\beta.
\]

For
\[
0\le a\le1,
\]
define
\[
m_z(a)
=
\sup_{\|u\|_1=a}
\min\{\|z+u\|_1,\|z-u\|_1\}.
\tag{6}
\]
We first prove
\[
\boxed{
m_z(a)=1+\max\{0,a-2\alpha\}.
}
\tag{7}
\]

If
\[
0\le a\le2\alpha,
\]
take
\[
u=\left(\frac a2,-\frac a2\right).
\]
Both norms in (6) are exactly \(1\). If
\[
2\alpha\le a\le1,
\]
take
\[
u=(a-\alpha,-\alpha).
\]
Then both norms in (6) equal
\[
1+a-2\alpha.
\]
These give the lower bound in (7).

For the upper bound, write
\[
u=(s,t),
\qquad
|s|+|t|=a.
\]
Replacing \(u\) by \(-u\) swaps the two norms and leaves their minimum unchanged, so assume
\[
s\ge0.
\]
Put
\[
L=1+\max\{0,a-2\alpha\}.
\]

Suppose first that
\[
t\ge0.
\]
If
\[
s\le\alpha
\quad\text{and}\quad
t\le\beta,
\]
then
\[
\|z-u\|_1=1-a\le L.
\]
If
\[
s>\alpha,
\]
then automatically \(t<\beta\), and
\[
\|z-u\|_1
=
1-2\alpha+s-t.
\]
Since
\[
s-t\le a,
\]
this is at most \(L\): for \(a\le2\alpha\) it is at most \(1\), and for \(a\ge2\alpha\) it is at most \(1+a-2\alpha\).
If instead
\[
t>\beta,
\]
then \(s<\alpha\) and
\[
\|z-u\|_1
=
a+2\alpha-1-2s
\le
a+2\alpha-1.
\]
For \(a\le2\alpha\), the last quantity is at most
\[
4\alpha-1\le1;
\]
for \(a\ge2\alpha\), it is at most
\[
1+a-2\alpha
\]
because \(\alpha\le1/2\).

Now suppose
\[
t<0
\]
and write
\[
q=-t,
\qquad
s+q=a.
\]
If
\[
s\le\alpha
\quad\text{and}\quad
q\le\beta,
\]
then
\[
\|z+u\|_1=1+s-q,
\qquad
\|z-u\|_1=1-s+q,
\]
so their minimum is
\[
1-|s-q|\le1\le L.
\]
If
\[
s\le\alpha
\quad\text{and}\quad
q>\beta,
\]
then
\[
\|z+u\|_1
=
a+2\alpha-1
\le L
\]
by the same two-range estimate as above.
Finally, if
\[
s>\alpha,
\]
then \(q<\beta\) and
\[
\|z-u\|_1
=
1+a-2\alpha,
\]
which is at most \(L\), with equality in the second range. This completes the upper bound and proves (7).

Now fix
\[
x=e_\gamma\otimes z.
\]
For arbitrary
\[
y=(y_\delta)_{\delta\in\Gamma}\in S_{Z_p},
\]
put
\[
u=y_\gamma,
\qquad
a=\|u\|_1.
\]
The remaining coordinates have total \(p\)-mass
\[
\sum_{\delta\ne\gamma}\|y_\delta\|_1^p
=
1-a^p.
\]
Hence
\[
\min\{\|x+y\|^p,\|x-y\|^p\}
=
1-a^p+
\min\{\|z+u\|_1,\|z-u\|_1\}^p.
\tag{8}
\]
For each fixed \(a\), equation (7) is attainable, and the complementary mass
\[
1-a^p
\]
can be placed on any other outer coordinate. Therefore
\[
\sigma_{Z_p}(x)^p
=
\max_{0\le a\le1}
\left[
1-a^p+
\left(1+\max\{0,a-2\alpha\}\right)^p
\right].
\tag{9}
\]

On
\[
0\le a\le2\alpha,
\]
the bracket in (9) is
\[
2-a^p\le2.
\]
On
\[
2\alpha\le a\le1,
\]
it is
\[
1-a^p+(1+a-2\alpha)^p.
\tag{10}
\]
Its derivative is
\[
p\left[
(1+a-2\alpha)^{p-1}-a^{p-1}
\right]\ge0.
\]
Thus the only competing endpoint values in (9) are
\[
2
\quad\text{and}\quad
(2-2\alpha)^p.
\]
Since
\[
1-\alpha=\|z\|_\infty,
\]
equation (2) follows.

It remains to minimize over the whole unit sphere. Let
\[
x=(x_\delta)_{\delta\in\Gamma}\in S_{Z_p}
\]
be arbitrary. Since \(\Gamma\) is infinite and
\[
\sum_{\delta\in\Gamma}\|x_\delta\|_1^p=1,
\]
for every \(\eta>0\) there is a coordinate \(\delta\) with
\[
\|x_\delta\|_1<\eta.
\]
Choose any
\[
v\in S_{\ell_1^2}
\]
and let \(y\) be supported at \(\delta\) with \(y_\delta=v\). By the reverse triangle inequality,
\[
\|x_\delta\pm v\|_1
\ge
1-\|x_\delta\|_1.
\]
Consequently
\[
\|x\pm y\|^p
\ge
1-\|x_\delta\|_1^p+
\left(1-\|x_\delta\|_1\right)^p.
\]
Letting \(\eta\downarrow0\) gives
\[
\sigma_{Z_p}(x)\ge2^{1/p}
\]
for every \(x\in S_{Z_p}\).

Finally, take
\[
z=\left(\frac12,\frac12\right).
\]
Equation (2) gives
\[
\sigma_{Z_p}(e_\gamma\otimes z)=2^{1/p}.
\]
This proves (4).

## Verification
The bundled `verify.py` checks the fibre identity (7) by exact rational boundary enumeration, verifies the scalar maximization in (9) for representative integer exponents, and checks the balanced and coordinate extreme fibres.

The finite mesh is only a reproducibility check. The case analysis proving (7), the monotonicity in (10), and the fresh-coordinate argument are analytic and cover all real
\[
1\le p<\infty.
\]

## Relationship to prior work
Hardtke's work on local octahedrality studies how locally octahedral and related properties behave under absolute sums. The inspected 2018 article states the equivalent condition
\[
\forall x\in S_X\ \forall\varepsilon>0\ \exists y\in S_X:
\quad
\|x\pm y\|\ge2-\varepsilon,
\]
and develops qualitative permanence and summand results for absolute direct sums. It does not give the pointwise quantitative profile (2) or the exact sub-octahedral value (4).

The closest exact quantitative comparison located is the Hilbert-fibre formula
\[
s\bigl(\ell_p(\Gamma;H)\bigr)
=
2^{1/\min\{p,2\}}
\]
for infinite \(\Gamma\) and real Hilbert fibres of dimension at least two. That statement does not cover the diamond fibre. In fact, for every
\[
p>2,
\]
the two exact values differ strictly:
\[
2^{1/p}<\sqrt2.
\]
Thus (4) is not a corollary of the Hilbert-fibre theorem; the fibre geometry is quantitatively visible.

The pointwise formula (2) also shows a phase transition inside a single copy of the diamond fibre: a one-coordinate point is controlled by the outer fresh-coordinate mechanism when
\[
2\|z\|_\infty\le2^{1/p},
\]
and by an in-fibre witness otherwise.

## Limitations
The exact pointwise formula is proved here for one-coordinate points in
\[
\ell_p(\Gamma;\ell_1^2).
\]
Only the global infimum is determined for arbitrary points.

No corresponding formula is claimed for
\[
\ell_p(\Gamma;\ell_1^n)
\]
with \(n\ge3\), where the fibre optimization acquires additional partition geometry, or for arbitrary polyhedral fibres.

The literature search cannot prove absolute novelty. An equivalent formula may exist under thickness, thinness, or quantitative-octahedrality terminology not captured by the searched sources.

## References
1. J.-D. Hardtke, “Summands in locally almost square and locally octahedral spaces,” *Acta et Commentationes Universitatis Tartuensis de Mathematica* 22 (2018), 149--162, doi:10.12697/ACUTM.2018.22.13. First public preprint: arXiv:1705.06610, 18 May 2017.
2. J.-D. Hardtke, “On Certain Geometric Properties in Banach Spaces of Vector-Valued Functions,” *Journal of Mathematical Physics, Analysis, Geometry* 16 (2020), 119--137, doi:10.15407/mag16.02.119. First public preprint: arXiv:1702.05050.

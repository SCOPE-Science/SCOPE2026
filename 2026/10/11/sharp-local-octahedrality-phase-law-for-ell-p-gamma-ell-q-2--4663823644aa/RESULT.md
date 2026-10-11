# Sharp local-octahedrality phase law for \(\ell_p(\Gamma;\ell_q^2)\)
## Finding
Let \(\Gamma\) be an infinite index set, let
\[
1\le p<\infty,
\qquad
2\le q\le\infty,
\]
and put
\[
Z_{p,q}=\ell_p(\Gamma;\ell_q^2).
\]
For
\[
x\in S_{Z_{p,q}},
\]
define
\[
\sigma_{Z_{p,q}}(x)
=
\sup_{y\in S_{Z_{p,q}}}
\min\{\|x+y\|,\|x-y\|\},
\]
and define the quantitative local-octahedrality index
\[
s(Z_{p,q})
=
\inf_{x\in S_{Z_{p,q}}}\sigma_{Z_{p,q}}(x).
\]
Then
\[
\boxed{
s(Z_{p,q})
=
2^{1/\min\{p,q\}}
}
\tag{1}
\]
with the convention
\[
\min\{p,\infty\}=p.
\]

Thus there is a sharp phase transition at
\[
p=q.
\]
If
\[
p\le q,
\]
the outer \(\ell_p\)-geometry controls the index:
\[
s(Z_{p,q})=2^{1/p}.
\]
If
\[
p\ge q,
\]
the two-dimensional fiber controls it:
\[
s(Z_{p,q})=2^{1/q}.
\]

## Assumptions and scope
All spaces are real.

For finite \(q\),
\[
\|(u,v)\|_q
=
\left(
|u|^q+|v|^q
\right)^{1/q},
\]
and
\[
\|(u,v)\|_\infty=\max\{|u|,|v|\}.
\]

Hardtke's local-octahedrality characterization says that a Banach space is locally octahedral exactly when every unit vector admits unit witnesses whose two symmetric chord lengths can be made arbitrarily close to \(2\). The quantity \(s(X)\) used here records the exact worst-base-point value of that same symmetric-chord problem.

## Proof
We prove matching lower and upper bounds.

First, every
\[
x=(x_\gamma)_{\gamma\in\Gamma}\in S_{Z_{p,q}}
\]
satisfies
\[
\sigma_{Z_{p,q}}(x)\ge2^{1/p}.
\tag{2}
\]
Indeed, because
\[
\sum_{\gamma\in\Gamma}\|x_\gamma\|_q^p=1,
\]
there are coordinates with arbitrarily small \(\|x_\gamma\|_q\); if the support is finite, there is an unused coordinate. Choose such a coordinate \(\gamma\) and a unit fiber vector \(u\), and let \(y\) be supported only at \(\gamma\) with value \(u\). If
\[
a=\|x_\gamma\|_q,
\]
then the reverse triangle inequality gives
\[
\|x_\gamma\pm u\|_q\ge1-a.
\]
Hence
\[
\|x\pm y\|^p
\ge
1-a^p+(1-a)^p.
\]
Letting \(a\downarrow0\) gives (2).

For the second lower bound, first suppose
\[
2\le q<\infty.
\]
For each nonzero coordinate write
\[
x_\gamma=a_\gamma z_\gamma,
\qquad
a_\gamma=\|x_\gamma\|_q,
\qquad
z_\gamma=(r_\gamma,s_\gamma)\in S_{\ell_q^2}.
\]
Set
\[
u_\gamma=(s_\gamma,-r_\gamma).
\]
Then
\[
u_\gamma\in S_{\ell_q^2}
\]
and
\[
\|z_\gamma+u_\gamma\|_q^q
=
\|z_\gamma-u_\gamma\|_q^q
=
|r_\gamma+s_\gamma|^q+|r_\gamma-s_\gamma|^q.
\]
The scalar Clarkson inequality for
\[
q\ge2
\]
gives
\[
|r+s|^q+|r-s|^q
\ge
2\left(|r|^q+|s|^q\right).
\]
Therefore
\[
\|z_\gamma\pm u_\gamma\|_q\ge2^{1/q}.
\tag{3}
\]

Define
\[
y_\gamma=a_\gamma u_\gamma
\]
when \(a_\gamma>0\), and \(y_\gamma=0\) otherwise. Then
\[
\|y\|^p=\sum_\gamma a_\gamma^p=1.
\]
Using (3) coordinatewise,
\[
\|x\pm y\|^p
=
\sum_\gamma
a_\gamma^p
\|z_\gamma\pm u_\gamma\|_q^p
\ge
2^{p/q}.
\]
Thus
\[
\sigma_{Z_{p,q}}(x)\ge2^{1/q}.
\tag{4}
\]
For \(q=\infty\), the lower bound corresponding to (4) is just
\[
\sigma_{Z_{p,\infty}}(x)\ge1,
\]
which is automatic.

Combining (2) and (4),
\[
s(Z_{p,q})
\ge
\max\{2^{1/p},2^{1/q}\}
=
2^{1/\min\{p,q\}}.
\tag{5}
\]

For the upper bound, fix
\[
\gamma_0\in\Gamma
\]
and take the one-coordinate unit vector
\[
x_{\gamma_0}=(1,0),
\qquad
x_\gamma=0
\quad
(\gamma\ne\gamma_0).
\tag{6}
\]
Let \(y\in S_{Z_{p,q}}\), and write
\[
a=\|y_{\gamma_0}\|_q.
\]
Then
\[
\sum_{\gamma\ne\gamma_0}\|y_\gamma\|_q^p
=
1-a^p.
\tag{7}
\]

Assume first \(q<\infty\), and write
\[
y_{\gamma_0}=(c,d).
\]
Choose the sign \(\varepsilon\in\{-1,1\}\) so that
\[
\varepsilon c\le0.
\]
Since \(a\le1\),
\[
|1+\varepsilon c|=1-|c|.
\]
Therefore
\[
\|(1,0)+\varepsilon(c,d)\|_q^q
=
(1-|c|)^q+|d|^q
\le
1+|c|^q+|d|^q
=
1+a^q.
\]
Together with (7),
\[
\min\{\|x+y\|,\|x-y\|\}^p
\le
(1+a^q)^{p/q}+1-a^p.
\tag{8}
\]

Put
\[
b=a^q,
\qquad
r=\frac pq.
\]
If \(p\le q\), then \(0<r\le1\), so subadditivity of \(t^r\) gives
\[
(1+b)^r\le1+b^r.
\]
Thus the right side of (8) is at most
\[
2.
\]
If \(p\ge q\), then \(r\ge1\), and
\[
h(b)=(1+b)^r+1-b^r
\]
is increasing on \([0,1]\), because
\[
h'(b)
=
r\left((1+b)^{r-1}-b^{r-1}\right)\ge0.
\]
Hence
\[
h(b)\le h(1)=2^r.
\]
Consequently
\[
\sigma_{Z_{p,q}}(x)
\le
\max\{2^{1/p},2^{1/q}\}.
\tag{9}
\]

For \(q=\infty\), choose the sign so that
\[
|1+\varepsilon c|\le1.
\]
Because
\[
|d|\le a\le1,
\]
one has
\[
\|(1,0)+\varepsilon(c,d)\|_\infty\le1.
\]
Thus
\[
\min\{\|x+y\|,\|x-y\|\}^p
\le
1+1-a^p
\le2,
\]
and therefore
\[
\sigma_{Z_{p,\infty}}(x)\le2^{1/p}.
\tag{10}
\]

The lower bound (5) and upper bounds (9)--(10) prove (1).

## Verification
The bundled `verify.py` checks the two scalar mechanisms used in the proof on representative exponents:

1. the rotated-fiber witness
\[
(r,s)\longmapsto(s,-r)
\]
gives both local chord norms at least \(2^{1/q}\) for \(q\ge2\);

2. the one-coordinate upper envelope
\[
(1+a^q)^{p/q}+1-a^p
\]
never exceeds
\[
\max\{2,2^{p/q}\}.
\]

The checker also verifies representative finite-\(q\) and \(q=\infty\) instances of the claimed phase law. These finite tests are supplementary; the theorem is proved for the full parameter ranges by the scalar Clarkson inequality, subadditivity for \(p/q\le1\), and monotonicity for \(p/q\ge1\).

## Relationship to prior work
Hardtke studied local octahedrality under absolute sums and recorded the standard symmetric-chord characterization: local octahedrality means that, at every unit base point, one can find unit vectors for which both symmetric chords approach length \(2\). His paper is qualitative and does not state the quantitative formula (1).

The closest indexed quantitative result found is the Hilbert-fiber case
\[
\ell_p(\Gamma;H),
\]
where
\[
s=2^{1/\min\{p,2\}}.
\]
That is exactly the boundary case \(q=2\) of (1). It does not imply the \(q>2\) theorem: the phase transition moves from \(p=2\) to the intrinsic fiber exponent \(p=q\), and the proof requires a different sharp fiber estimate.

A separate exact result for diamond-valued sums
\[
\ell_p(\Gamma;\ell_1^2)
\]
has a different pointwise mechanism and gives global index \(2^{1/p}\). It does not cover the super-Hilbert fiber range \(q>2\).

## Limitations
The theorem treats two-dimensional fibers
\[
\ell_q^2
\]
for
\[
2\le q\le\infty.
\]
It does not determine the corresponding index for higher-dimensional \(\ell_q\) fibers.

The sub-Hilbert fiber range
\[
1<q<2
\]
has a different scaled pointwise profile; no formula for that regime is claimed here.

Bibliographic and semantic-index searches cannot establish absolute novelty. An equivalent formula could exist under another quantitative formulation of local octahedrality.

## References
1. J.-D. Hardtke, “Summands in locally almost square and locally octahedral spaces,” *Acta et Commentationes Universitatis Tartuensis de Mathematica* 22 (2018), 149--162, doi:10.12697/ACUTM.2018.22.13. First public preprint: arXiv:1705.06610v1, 18 May 2017. Mathematics Subject Classification: 46B20.

# A cube-extension law for the weak covering index
## Finding
Let \(K\subset\mathbb R^d\) be any convex body and let \(C^r\) be an \(r\)-dimensional parallelotope lying in a complementary linear subspace. Then
\[
\boxed{
\operatorname{coin}_{\mathrm w}(K\oplus C^r)
\ge
2^r\operatorname{coin}_{\mathrm w}(K)
}.
\tag{1}
\]

If the weak covering index of \(K\) is attained by an \(m\)-covering number at a ratio
\[
\lambda_*=\gamma_m(K)\in[1/2,1),
\qquad
\operatorname{coin}_{\mathrm w}(K)
=
\frac{m}{1-\lambda_*},
\tag{2}
\]
then (1) is an equality:
\[
\boxed{
\operatorname{coin}_{\mathrm w}(K\oplus C^r)
=
2^r\operatorname{coin}_{\mathrm w}(K)
}.
\tag{3}
\]

Two exact infinite families follow immediately from the base values in Bezdek--Khan. For a triangle \(\Delta^2\) and an affine-regular centrally symmetric hexagon
\[
H=\Delta^2+(-\Delta^2),
\]
their source gives
\[
\operatorname{coin}_{\mathrm w}(\Delta^2)
=
\operatorname{coin}_{\mathrm w}(H)
=
9,
\qquad
\gamma_3(\Delta^2)
=
\gamma_3(H)
=
\frac23.
\tag{4}
\]
Hence, for every integer \(r\ge1\),
\[
\boxed{
\operatorname{coin}_{\mathrm w}(\Delta^2\oplus C^r)
=
\operatorname{coin}_{\mathrm w}(H\oplus C^r)
=
9\cdot2^r.
}
\tag{5}
\]

At \(r=1\), (5) closes two entries that were left only as upper estimates in the source table:
\[
\operatorname{coin}_{\mathrm w}(\Delta^2\oplus\ell)
=
\operatorname{coin}_{\mathrm w}(H\oplus\ell)
=
18.
\tag{6}
\]

## Assumptions and scope
For a convex body \(K\), let
\[
\gamma_m(K)
=
\inf\left\{
\lambda>0:
K\text{ is covered by }m\text{ translates of }\lambda K
\right\}.
\]
Bezdek--Khan define
\[
\operatorname{coin}_{\mathrm w}(K)
=
\inf_{\substack{m\ge1\\\gamma_m(K)<1}}
\frac{m}{1-\gamma_m(K)}.
\tag{7}
\]

For \(0<\lambda<1\), let
\[
N_\lambda(K)
\]
be the smallest number of translates of \(\lambda K\) needed to cover \(K\).

The operation \(K\oplus L\) is the direct vector sum in complementary subspaces. In coordinates it is affinely equivalent to a Cartesian product. A parallelotope \(C^r\) is an affine image of the direct sum of \(r\) line segments.

The equality statement (3) assumes actual attainment as in (2). No general assertion is made that every convex body has an attaining pair with ratio at least \(1/2\).

## Proof
We first record a useful exact reformulation of (7):
\[
\operatorname{coin}_{\mathrm w}(K)
=
\inf_{0<\lambda<1}
\frac{N_\lambda(K)}{1-\lambda}.
\tag{8}
\]

To prove the lower inequality in (8), fix \(\lambda\) and put
\[
m=N_\lambda(K).
\]
Then
\[
\gamma_m(K)\le\lambda,
\]
and therefore
\[
\frac{N_\lambda(K)}{1-\lambda}
=
\frac{m}{1-\lambda}
\ge
\frac{m}{1-\gamma_m(K)}
\ge
\operatorname{coin}_{\mathrm w}(K).
\tag{9}
\]

For the reverse inequality, fix any \(m\) with \(\gamma_m(K)<1\). For every sufficiently small \(\varepsilon>0\), the definition of \(\gamma_m(K)\) gives an \(m\)-homothet cover with ratio below
\[
\gamma_m(K)+\varepsilon.
\]
Hence
\[
N_{\gamma_m(K)+\varepsilon}(K)\le m,
\]
so
\[
\inf_{0<\lambda<1}\frac{N_\lambda(K)}{1-\lambda}
\le
\frac{m}{1-\gamma_m(K)-\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) and then taking the infimum over \(m\) proves (8).

A line segment \(\ell\) is tightly covered in the sense of Bezdek--Khan, and
\[
N_\lambda(\ell)=\left\lceil\frac1\lambda\right\rceil.
\tag{10}
\]
Their exact direct-sum covering formula therefore gives, for all \(0<\lambda<1\),
\[
N_\lambda(K\oplus C^r)
=
N_\lambda(K)
\left\lceil\frac1\lambda\right\rceil^r.
\tag{11}
\]
Here one applies the formula to \(K\) together with the \(r\) tightly covered segment factors.

Combining (8) and (11),
\[
\operatorname{coin}_{\mathrm w}(K\oplus C^r)
=
\inf_{0<\lambda<1}
\left[
\frac{N_\lambda(K)}{1-\lambda}
\left\lceil\frac1\lambda\right\rceil^r
\right].
\tag{12}
\]
Since
\[
\left\lceil\frac1\lambda\right\rceil\ge2
\qquad(0<\lambda<1),
\]
equations (8) and (12) give (1).

Now assume (2). At
\[
\lambda_*=\gamma_m(K),
\]
we have
\[
N_{\lambda_*}(K)\le m.
\]
On the other hand, (9) and (2) force
\[
\frac{N_{\lambda_*}(K)}{1-\lambda_*}
\ge
\operatorname{coin}_{\mathrm w}(K)
=
\frac{m}{1-\lambda_*}.
\]
Thus
\[
N_{\lambda_*}(K)=m.
\]
Because
\[
\lambda_*\in[1/2,1),
\]
we have
\[
\left\lceil\frac1{\lambda_*}\right\rceil=2.
\]
Evaluating (12) at \(\lambda_*\) gives
\[
\operatorname{coin}_{\mathrm w}(K\oplus C^r)
\le
2^r\operatorname{coin}_{\mathrm w}(K),
\]
which combines with (1) to prove (3).

Finally, the source values (4) satisfy the attainment hypothesis with
\[
m=3,\qquad\lambda_*=\frac23.
\]
Substitution into (3) proves (5) and (6).

## Verification
The proof is exact and requires no numerical experiment. The two external premises used from Bezdek--Khan were checked directly in the full text:

1. their Proposition 4.2 states the exact product formula for \(N_\lambda\) of direct sums when all but one factors are tightly covered, and explicitly records that a segment is tightly covered with
\[
N_\lambda(\ell)=\left\lceil\frac1\lambda\right\rceil;
\]
2. their weak-index table records
\[
\operatorname{coin}_{\mathrm w}(\Delta^2)
=
\operatorname{coin}_{\mathrm w}(H)
=
9
\]
at
\[
m=3,\qquad\gamma_m=\frac23,
\]
while listing only
\[
\operatorname{coin}_{\mathrm w}(\Delta^2\oplus\ell)\le18,
\qquad
\operatorname{coin}_{\mathrm w}(H\oplus\ell)\le18.
\]

The new deductions are the variational identity (8), the universal lower law (1), and the attainment criterion yielding equality.

## Relationship to prior work
Bezdek--Khan introduced the weak covering index and proved that the direct-sum machinery for covering numbers carries over to it. Their paper explicitly says that no suitable weak analogue of their ordinary cylinder corollary is available and therefore gives only estimates for one-codimensional cylinders. In Table 2 they list
\[
\operatorname{coin}_{\mathrm w}(H\oplus\ell)\le18
\]
and
\[
\operatorname{coin}_{\mathrm w}(\Delta^2\oplus\ell)\le18.
\]
The result above supplies the missing lower bound and extends the equality to every cube extension.

A later paper by Wu--Fan--He studies covering functionals of Minkowski and direct sums and gives general inequalities for \(\Gamma_m\). Its full text was checked at the direct-sum section; it does not discuss the weak covering index, and text searches found no triangle or prism specialization.

Targeted searches for weak covering index, triangular prisms, segment doubling, cube extensions, and the value \(18\) found the Bezdek--Khan source and later general covering-functional work, but no published statement implying (1)--(6).

## Limitations
The equality law requires an attaining weak-index ratio in
\[
[1/2,1).
\]
Without that hypothesis only the lower bound (1) is proved.

The result concerns direct vector sums with parallelotope factors. It does not give an analogous formula for Minkowski sums in the same ambient subspace.

The source ingredients make the argument short, so an unindexed observation deriving the same conditional cylinder law remains a historical originality risk.

No claim is made about maximizers or minimizers of the weak covering index in dimensions at least three.

## References
1. K. Bezdek and M. A. Khan, *On the covering index of convex bodies*, arXiv:1503.03111v1, 10 March 2015; later *Aequationes Mathematicae* 90 (2016), 879--903. DOI: 10.1007/s00010-016-0409-z.
2. S. Wu, B. Fan, and C. He, *Covering functionals of Minkowski sums and direct sums of convex bodies*, *Mathematical Inequalities & Applications* 23 (2020), 1145--1154. DOI: 10.7153/mia-2020-23-88.

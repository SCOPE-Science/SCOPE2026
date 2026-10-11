# Exponential high-order stabilization of powered Bohr–Rogosinski radii

## Finding

Let
\[
0<p\le2,\qquad N\in\mathbb N.
\]
For every
\[
m\in\mathbb N,
\]
let
\[
R_{m,N}^{(p)}\in(0,1)
\]
be the sharp radius determined by
\[
p\frac{1-r^m}{1+r^m}
=
\frac{2r^N}{1-r}.
\]

Define
\[
A_{p,N}\in(0,1)
\]
as the unique solution of
\[
p=\frac{2A_{p,N}^N}{1-A_{p,N}}.
\]

Then
\[
R_{m,N}^{(p)}
\]
is strictly increasing in \(m\),
\[
R_{m,N}^{(p)}<A_{p,N},
\]
and
\[
R_{m,N}^{(p)}\uparrow A_{p,N}.
\]
More precisely,
\[
A_{p,N}-R_{m,N}^{(p)}
\sim
\frac{2A_{p,N}(1-A_{p,N})}
{N-(N-1)A_{p,N}}
A_{p,N}^{m}.
\]

For the improved radius with
\[
N=1,
\]
this becomes
\[
A_{p,1}=\frac{p}{p+2}
\]
and
\[
\frac{p}{p+2}-R_{m,1}^{(p)}
\sim
\frac{4p}{(p+2)^2}
\left(\frac{p}{p+2}\right)^m.
\]

Thus high-order vanishing of the Schwarz mapping drives the sharp Bohr--Rogosinski radius toward the powered Bohr radius at an exactly determined exponential rate.

## Assumptions and scope

The radius family is the sharp family stated in Hamada--Honda--Kohr, *Analysis and Mathematical Physics* 15 (2025), Article 64, and reproduced as Theorem E/F in arXiv:2609.28357v1.

The 2026 paper proves an improved Bohr--Rogosinski inequality whose sharp radius is the specialization
\[
R_{m,1}^{(p)}.
\]

The parameters satisfy
\[
m,N\in\mathbb N,
\qquad
0<p\le2.
\]
No claim is made for other radius equations or for values of \(p\) outside the stated range.

## Proof

Put
\[
F_m(r)
=
p\frac{1-r^m}{1+r^m}
-
\frac{2r^N}{1-r}.
\]
For
\[
0<r<1,
\]
\[
F_m'(r)
=
-\frac{2pmr^{m-1}}{(1+r^m)^2}
-
\frac{2r^{N-1}(N-(N-1)r)}{(1-r)^2}
<0.
\]
Thus \(F_m\) is strictly decreasing and has the unique zero supplied by the sharp-radius theorem.

For fixed \(r\in(0,1)\), the quantity
\[
\frac{1-r^m}{1+r^m}
\]
strictly increases with \(m\). Hence
\[
F_{m+1}(r)>F_m(r),
\]
and the zero moves strictly to the right:
\[
R_{m+1,N}^{(p)}>R_{m,N}^{(p)}.
\]

At
\[
r=A_{p,N},
\]
the defining equation for \(A_{p,N}\) gives
\[
F_m(A_{p,N})
=
p\left(
\frac{1-A_{p,N}^m}{1+A_{p,N}^m}-1
\right)
=
-\frac{2pA_{p,N}^m}{1+A_{p,N}^m}<0.
\]
Since \(F_m\) decreases through zero,
\[
R_{m,N}^{(p)}<A_{p,N}.
\]

The increasing sequence therefore has a limit
\[
L\le A_{p,N}<1.
\]
Moreover,
\[
\left(R_{m,N}^{(p)}\right)^m
\le
A_{p,N}^m
\longrightarrow0.
\]
Passing to the radius equation gives
\[
p=\frac{2L^N}{1-L}.
\]
The right side is strictly increasing on
\[
(0,1),
\]
so
\[
L=A_{p,N}.
\]

For the exact rate, the mean value theorem yields a point
\[
\xi_m\in
\left(
R_{m,N}^{(p)},A_{p,N}
\right)
\]
such that
\[
A_{p,N}-R_{m,N}^{(p)}
=
\frac{
2pA_{p,N}^m/(1+A_{p,N}^m)
}{
-F_m'(\xi_m)
}.
\]
Since
\[
\xi_m\to A_{p,N},
\]
and
\[
0\le
m\xi_m^{m-1}
\le
mA_{p,N}^{m-1}
\longrightarrow0,
\]
the derivative satisfies
\[
-F_m'(\xi_m)
\longrightarrow
\frac{
2A_{p,N}^{N-1}
\left(
N-(N-1)A_{p,N}
\right)
}{
(1-A_{p,N})^2
}.
\]
Therefore
\[
\frac{
A_{p,N}-R_{m,N}^{(p)}
}{
A_{p,N}^m
}
\longrightarrow
\frac{
p(1-A_{p,N})^2
}{
A_{p,N}^{N-1}
\left(
N-(N-1)A_{p,N}
\right)
}.
\]
Using
\[
p=\frac{2A_{p,N}^N}{1-A_{p,N}}
\]
gives
\[
\frac{
A_{p,N}-R_{m,N}^{(p)}
}{
A_{p,N}^m
}
\longrightarrow
\frac{
2A_{p,N}(1-A_{p,N})
}{
N-(N-1)A_{p,N}
}.
\]

For
\[
N=1,
\]
the limiting equation gives
\[
A_{p,1}=\frac{p}{p+2},
\]
and substitution gives the stated corollary.

## Verification

The 2026 primary preprint was inspected at its classification data, its verbatim statement of the earlier sharp radius family, and its improved Theorem 2. The latter uses
\[
N=1
\]
and exactly the same root equation.

The 2021 Kayumov--Khammatova--Ponnusamy primary article was inspected at its Theorems 1 and 2. Those results give the endpoint cases corresponding to
\[
p=1
\]
and
\[
p=2,
\]
including their limiting radii as
\[
m\to\infty.
\]
They do not supply the exponential deficit coefficient proved here.

The proof above is exact. Representative root calculations for
\[
(p,N)=(1,1),(2,1),(3/2,2),(1/2,3)
\]
were used only as sanity checks; the theorem does not rely on numerical computation.

## Relationship to prior work

Kayumov, Khammatova, and Ponnusamy proved the classical
\[
p=1
\]
and squared
\[
p=2
\]
Bohr--Rogosinski radius formulas and identified their limiting radii as the Schwarz-map order tends to infinity.

Hamada, Honda, and Kohr introduced the powered family
\[
R_{m,N}^{(p)}
\]
for
\[
0<p\le2
\]
in the higher-dimensional Banach-space setting. Their exact theorem statement is reproduced in the 2026 primary source.

Zeng and Xiong's 2026 improved inequality has the same sharp root with
\[
N=1
\]
and recalls independently that the powered Bohr radius is
\[
p/(p+2).
\]

The present result links these two quantities quantitatively. It proves monotone convergence for all
\[
p,N
\]
and determines the exact exponentially small gap. In the fresh improved case it shows that
\[
p/(p+2)
\]
is approached with base
\[
p/(p+2)
\]
and prefactor
\[
4p/(p+2)^2.
\]

## Limitations

The theorem analyzes a sharp radius already characterized implicitly by prior work; it does not improve the underlying Bohr--Rogosinski inequality.

The complete 2025 publisher article was not available through the lawful full-text route used for this check. Its exact theorem statement was read from the 2026 primary paper, which reproduces it explicitly. An unindexed remark in the 2025 article giving the same rate remains a residual originality risk.

The result is asymptotic in the Schwarz-map order \(m\). It does not give a uniform error term in all three parameters \(p,N,m\).

## References

1. H. Hamada, T. Honda, and M. Kohr, *Bohr--Rogosinski radius for holomorphic mappings with values in higher dimensional complex Banach spaces*, Analysis and Mathematical Physics 15 (2025), Article 64, DOI: 10.1007/s13324-025-01061-x.
2. L. Zeng and L. Xiong, *Improved Bohr--Rogosinski radius for holomorphic mappings with values in complex Banach spaces*, arXiv:2609.28357v1, 2026.
3. I. R. Kayumov, D. M. Khammatova, and S. Ponnusamy, *Bohr--Rogosinski phenomenon for analytic functions and Cesáro operators*, Journal of Mathematical Analysis and Applications 496 (2021), 124824, DOI: 10.1016/j.jmaa.2020.124824.
4. I. R. Kayumov and S. Ponnusamy, *On a powered Bohr inequality*, Annales Academiae Scientiarum Fennicae Mathematica 44 (2019), 301--310.

# Sharp lattice Gauss envelope for symmetric unimodal laws

## Finding

Let \(X\) be integer-valued with a symmetric unimodal probability mass function:
\[
\Pr(X=j)=\Pr(X=-j),\qquad
\Pr(X=j)\ge \Pr(X=j+1)\quad(j\ge0).
\]
Write
\[
v=\operatorname{Var}(X),
\]
and fix an integer threshold \(a\ge1\).

For \(k\ge0\), let \(U_k\) denote the uniform law on
\[
\{-k,-k+1,\ldots,k\},
\]
with
\[
V_k=\operatorname{Var}(U_k)=\frac{k(k+1)}3.
\]
For \(k\ge a\), put
\[
T_k=\Pr(|U_k|\ge a)=\frac{2(k-a+1)}{2k+1}.
\]
Finally define
\[
\beta_a=\frac{6a-11+\sqrt{36a^2-36a+25}}8,
\qquad
\kappa_a=1+\lfloor\beta_a\rfloor.
\]

Then the exact maximum of \(\Pr(|X|\ge a)\) among all such laws of variance \(v\)
is the following continuous piecewise-linear function.

For
\[
0\le v\le V_{\kappa_a},
\]
\[
\boxed{
B_a(v)=\frac{T_{\kappa_a}}{V_{\kappa_a}}\,v
=
\frac{6(\kappa_a-a+1)}
{\kappa_a(\kappa_a+1)(2\kappa_a+1)}\,v.
}
\]

For \(v\ge V_{\kappa_a}\), let \(k\ge\kappa_a\) be the unique integer with
\[
V_k\le v\le V_{k+1}.
\]
Then
\[
\boxed{
B_a(v)=
T_k+
\frac{3(2a-1)}
{(k+1)(2k+1)(2k+3)}
\,(v-V_k).
}
\]

The bounds are attained by centered-uniform mixtures. On the first segment the
extremizer is
\[
\left(1-\frac{v}{V_{\kappa_a}}\right)U_0+
\frac{v}{V_{\kappa_a}}U_{\kappa_a}.
\]
For
\[
V_k\le v\le V_{k+1},
\]
the extremizer is
\[
(1-\lambda)U_k+\lambda U_{k+1},
\qquad
\lambda=\frac{v-V_k}{V_{k+1}-V_k}.
\]

There is also a clean continuum limit. If \(a\to\infty\) and
\[
\frac{v_a}{a^2}\to c>0,
\]
then
\[
B_a(v_a)\longrightarrow
\begin{cases}
\frac{4c}{9},&0<c\le\frac34,\\[4pt]
1-\frac{1}{\sqrt{3c}},&c\ge\frac34.
\end{cases}
\]
This is the classical sharp symmetric Gauss envelope after scaling.

## Assumptions and scope

Symmetric unimodality means the lattice masses are symmetric about zero and
nonincreasing away from zero. Hence zero is a mode and the mean is zero.

The variance \(v\) may be any nonnegative real number. No bounded-support
assumption is imposed.

The theorem concerns the two-sided lattice tail at an integer threshold. It
does not claim the exact corresponding envelope for asymmetric unimodal laws
or for arbitrary noninteger lattices.

## Proof

Write
\[
p_j=\Pr(X=j),\qquad j\ge0.
\]
By symmetry and unimodality,
\[
p_0\ge p_1\ge p_2\ge\cdots\ge0.
\]
Set
\[
\alpha_k=(2k+1)(p_k-p_{k+1}).
\]
Then \(\alpha_k\ge0\), summation by parts gives
\[
\sum_{k\ge0}\alpha_k=1,
\]
and for every \(j\ge0\),
\[
p_j=\sum_{k\ge j}\frac{\alpha_k}{2k+1}.
\]
Thus the law has the unique mixture representation
\[
X\sim\sum_{k\ge0}\alpha_kU_k.
\]

Variance and tail probability are linear in the mixing weights:
\[
v=\sum_{k\ge0}\alpha_kV_k,
\qquad
\Pr(|X|\ge a)=\sum_{k\ge0}\alpha_kT_k,
\]
where \(T_k=0\) for \(k<a\). Therefore the sharp bound is the upper concave
envelope of
\[
(V_k,T_k),\qquad k=0,1,2,\ldots.
\]

For \(k\ge a\), the slope from the origin is
\[
\rho_k=\frac{T_k}{V_k}
=
\frac{6(k-a+1)}{k(k+1)(2k+1)}.
\]
Direct subtraction gives
\[
\rho_{k+1}-\rho_k
=
\frac{
6(6ak+6a-4k^2-11k-6)
}{
k(k+1)(k+2)(2k+1)(2k+3)
}.
\]
The quadratic numerator changes sign at
\[
\beta_a=
\frac{6a-11+\sqrt{36a^2-36a+25}}8,
\]
so the integer sequence \(\rho_k\) is maximized at
\[
\kappa_a=1+\lfloor\beta_a\rfloor.
\]
Also,
\[
36a^2-36a+25-(2a+3)^2
=
16(2a-1)(a-1)\ge0,
\]
so \(\beta_a\ge a-1\) and \(\kappa_a\ge a\).

The slope between consecutive positive-tail points is
\[
\frac{T_{k+1}-T_k}{V_{k+1}-V_k}
=
\frac{3(2a-1)}
{(k+1)(2k+1)(2k+3)},
\]
which is strictly decreasing in \(k\). Since
\[
\rho_{\kappa_a+1}\le\rho_{\kappa_a},
\]
the first consecutive slope after the contact point is no larger than the
initial ray slope. Hence the upper hull consists exactly of the segment from
\((0,0)\) to \((V_{\kappa_a},T_{\kappa_a})\), followed by every consecutive
segment
\[
(V_k,T_k)\longrightarrow(V_{k+1},T_{k+1}),
\qquad k\ge\kappa_a.
\]
This proves the formulas and the displayed extremizing mixtures.

For the scaling limit,
\[
\frac{\kappa_a}{a}\longrightarrow\frac32,
\qquad
\frac{V_{\kappa_a}}{a^2}\longrightarrow\frac34.
\]
On the initial segment,
\[
\frac{T_{\kappa_a}}{V_{\kappa_a}}
\sim\frac{4}{9a^2},
\]
giving \(4c/9\). Above the breakpoint the relevant index satisfies
\[
\frac{k}{a}\longrightarrow\sqrt{3c},
\]
while
\[
T_k=\frac{2(k-a+1)}{2k+1}
\longrightarrow1-\frac1{\sqrt{3c}}.
\]
The interpolation error tends to zero, and the two branches agree at
\(c=3/4\).

## Verification

A standalone exact-rational checker accompanies the theorem. It verifies the
closed formulas, the maximizing-index rule, the consecutive hull slopes, the
concavity of the proposed envelope, exact attainment by rational mixtures, and
many random finite mixtures of centered discrete uniforms.

The computation is supplementary. The infinite-dimensional extremal problem is
settled analytically by the mixture representation and explicit upper-hull
calculation.

## Relationship to prior work

The classical Gauss inequality gives a sharp variance-tail envelope for
unimodal distributions. Dharmadhikari and Joag-Dev generalized the
Gauss--Tchebyshev inequality using convexity and a representation of unimodal
laws as mixtures of uniforms. Their full article was inspected; it works on
the real line and does not state the integer-lattice hull above.

Huber later studied discrete monotone and unimodal tail inequalities. His
discrete two-sided theorem bounds
\[
\Pr(|W-\mathbb EW|\ge a)
\]
by a smoothed Chebyshev expression and explicitly states that this discrete
unimodal inequality is not tight. His proof smooths an integer-valued law by a
continuous uniform variable rather than solving the exact lattice extremal
problem.

The present theorem restricts to the natural symmetric unimodal lattice class
and solves that problem exactly. The first contact index
\[
\kappa_a
=
1+\left\lfloor
\frac{6a-11+\sqrt{36a^2-36a+25}}8
\right\rfloor
\]
is a lattice correction to the continuous Gauss extremizer scale \(3a/2\).

Targeted searches for a sharp discrete Gauss inequality, symmetric unimodal
integer tail envelopes, and centered discrete-uniform mixture extremizers did
not locate this formula or breakpoint.

## Limitations

The theorem uses exact symmetry. General lattice-unimodal laws with separated
mode and mean can have more complicated moment geometry.

Only integer thresholds are parameterized directly. Noninteger thresholds
reduce to an integer tail event by rounding, but that reformulation is not
spelled out here.

The originality assessment used targeted database and web searches plus
full-text inspection of the closest classical and discrete sources. Older
lattice-probability literature could contain an equivalent hull description
under different terminology.

## References

1. S. W. Dharmadhikari and K. Joag-Dev, “The Gauss--Tchebyshev inequality for
   unimodal distributions,” *Theory of Probability and Its Applications* 30
   (1986), 867--871, DOI: 10.1137/1130111. The inspected record gives the
   English online-publication date 2006-07-28 and links the 1985 Russian
   original.
2. M. Huber, “Tail inequalities for restricted classes of discrete random
   variables,” arXiv:2101.03452, first submitted 2021-01-10.
3. R. A. Ion, C. A. J. Klaassen, and E. R. van den Heuvel, “Sharp inequalities
   of Bienaymé--Chebyshev and Gauß type for possibly asymmetric intervals
   around the mean,” *AStA Advances in Statistical Analysis* 107 (2023),
   201--233.

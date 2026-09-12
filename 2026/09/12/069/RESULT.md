# No interior Whitham speed collision on the symmetric genus-2 focusing mKdV family

## Context

The focusing modified Korteweg-de Vries (mKdV) equation admits finite-gap
solutions built from hyperelliptic spectral curves. Their slow modulations
obey the mKdV-Whitham system, whose characteristic speeds are ratios of the
quasienergy and quasimomentum differentials evaluated at the branch points.
For focusing problems the Whitham system can change type from hyperbolic to
elliptic when two speeds collide and form a complex pair, as is known in the
focusing NLS semiclassical regime. The admitted target asks whether such a
type-change threshold exists on one concrete symmetric genus-2 focusing mKdV
family, or whether no interior collision occurs.

## Definitions

Fix outer branch points $-3 &lt; -1 &lt; 1 &lt; 3$ and a middle parameter
$d \\in (0,1)$. Write $r = d$ for the normalized middle half-width. The
genus-2 spectral curve is

$$y^2 = R(E) := (E+3)(E+1)(E+d)(E-d)(E-1)(E-3)
= (E^2-9)(E^2-1)(E^2-d^2).$$

The bands (cuts) are $[-3,-1]$, $[-d,d]$, $[1,3]$; the finite gaps are
$(-1,-d)$ and $(d,1)$. The curve is invariant under $E \\mapsto -E$.
Let $u_r(x,t)$ be the real focusing mKdV finite-gap potential from
Baker-Akhiezer reconstruction; only the Whitham speeds are needed.

Put $s = E^2$ and

$$R(E) = E^6-(10+d^2)E^4+(9+10d^2)E^2-9d^2,$$

$$y = E^3 + e_1 E + O(E^{-1}), \\qquad
e_1 = -\\frac{10+d^2}{2}.$$

On $(1,3)$ define the positive weight $w(E) = 1/\\sqrt{|R(E)|}$ and the
moments

$$J_k = \\int_1^3 E^k w(E)\\,dE, \\qquad k = 1, 3, 5,$$

which converge since endpoint singularities are $|E-E_j|^{-1/2}$.

The mKdV Baker-Akhiezer exponent is odd in $E$, so the quasimomentum and
quasienergy differentials are odd meromorphic differentials of the second
kind with poles only at infinity:

$$dp = \\frac{T(E)\\,dE}{y}, \\quad T(E) = E^3 + bE,$$
$$d\\Omega = \\frac{Q(E)\\,dE}{y}, \\quad
Q(E) = c\\,(12E^5 + \\beta E^3 + \\delta E),$$

with an overall time-scaling constant $c \\ne 0$ irrelevant for collisions.
Since $T/y = 1 + O(E^{-2})$, $dp \\sim dE$ at infinity, and

$$\\frac{Q(E)}{y} = 12E^2 + (\\beta - 12e_1) + O(E^{-2}),$$

the standard mKdV principal part ($d\\Omega \\sim 12E^2\\,dE$ up to scale,
no constant term) forces

$$\\beta = 12e_1 = -6(10+d^2).$$

Normalization $\\oint_{a_j} dp = \\oint_{a_j} d\\Omega = 0$ over the
$a$-cycles encircling the three bands reduces by oddness to a single
condition: the middle-band integral of an odd differential vanishes
automatically and the two outer-band conditions coincide. Hence

$$b = -\\frac{J_3}{J_1}, \\qquad
\\delta = -\\frac{12J_5 + \\beta J_3}{J_1}.$$

At a branch point $E_j \\ne 0$ the Whitham characteristic speed is the
standard ratio

$$V_j = \\left.\\frac{d\\Omega}{dp}\\right|_{E_j}
= \\frac{Q(E_j)}{T(E_j)}
= \\frac{12s_j^2 + \\beta s_j + \\delta}{s_j + b},
\\qquad s_j = E_j^2.$$

By evenness $V(-E) = V(E)$, so there are three distinct reduced speeds at
$s \\in \\{9, 1, d^2\\}$:

$$V(s) = \\frac{12s^2 + \\beta s + \\delta}{s + b}.$$

The six-point system doubles each value by symmetry for every $d$; this
fixed degeneracy is not a bifurcation. Strict hyperbolicity below refers to
the symmetry-reduced $3 \\times 3$ system.

## Result

**Theorem (no interior collision).** For every $d \\in (0,1)$ the three
reduced speeds $V(3)$, $V(1)$, $V(d)$ are real, finite, and pairwise
distinct. The reduced genus-2 focusing mKdV-Whitham system is strictly
hyperbolic on all of $(0,1)$. There is no critical ratio $r^* \\in (0,1)$
at which two characteristic speeds collide, and hence no
hyperbolic-to-elliptic type change on this symmetric family.

## Proof / evidence

For $s_1 \\ne s_2$, with collision numerator

$$N = (12s_1^2+\\beta s_1+\\delta)(s_2+b)
- (12s_2^2+\\beta s_2+\\delta)(s_1+b),$$

direct expansion gives

$$N = (s_1-s_2)\\bigl[\\,12s_1s_2 + 12b(s_1+s_2) + b\\beta - \\delta\\,\\bigr].$$

This identity was verified symbolically
(`output/artifacts/verify_identity.py`). Substituting $b = -J_3/J_1$ and
$\\delta = -(12J_5+\\beta J_3)/J_1$, the terms in $\\beta$ cancel
identically:

$$H := 12s_1s_2 + 12b(s_1+s_2) + b\\beta - \\delta
= \\frac{12\\,G(s_1,s_2)}{J_1},$$

where

$$G(s_1,s_2) = \\int_1^3 E\\,(E^2-s_1)(E^2-s_2)\\,w(E)\\,dE.$$

Hence $V(s_1) = V(s_2)$ with finite denominators holds if and only if
$G(s_1,s_2) = 0$. The conclusion is independent of the flow-normalization
constants $c$ and $\\beta$.

On the open interval $(1,3)$: $E &gt; 0$, $(E^2-9) &lt; 0$, $(E^2-1) &gt; 0$,
$(E^2-d^2) &gt; 0$ (since $E &gt; 1 &gt; d$). Thus the integrands have strict
constant sign:

| pair $(s_1,s_2)$ | integrand sign on $(1,3)$ | $G$ |
|---|---|---|
| $(9,1)$ | $E \\cdot (-) \\cdot (+) &lt; 0$ | $G &lt; 0$ |
| $(9,d^2)$ | $E \\cdot (-) \\cdot (+) &lt; 0$ | $G &lt; 0$ |
| $(1,d^2)$ | $E \\cdot (+) \\cdot (+) &gt; 0$ | $G &gt; 0$ |

Zeros of the polynomial factors occur only at endpoints ($E = 1, 3$) or
outside $[1,3]$ ($E = d$), so each integrand is one-signed almost everywhere
and every $G \\ne 0$ strictly, for every $d \\in (0,1)$.

For denominators, $b = -J_3/J_1$ is minus the weighted mean of
$E^2 \\in (1,9)$ under the positive measure $Ew\\,dE$, so
$b \\in (-9,-1)$ strictly. Hence $9+b &gt; 0$, $1+b &lt; 0$,
$d^2+b &lt; 0$: all denominators are finite and nonzero.

Therefore all three reduced speeds are real, finite, and pairwise distinct
for every $d \\in (0,1)$.

Numeric illustration (band normalization, $\\beta = -6(10+d^2)$; computed
with 60-digit arithmetic in `output/artifacts/speed_scan.py` up to an
irrelevant overall flow scale):

| $d$ | $V(3)$ | $V(1)$ | $V(d)$ |
|---|---|---|---|
| 0.05 | 6.4306 | 2.5648 | 0.9117 |
| 0.5 | 6.2455 | 2.4083 | 1.1019 |
| 0.9 | 5.6923 | 2.0140 | 1.6004 |
| 0.99 | 5.2887 | 1.8592 | 1.8011 |

Ordering $V(3) &gt; V(1) &gt; V(d)$ throughout. The same integral-sign
mechanism also rules out collisions under the gap normalization
$\\int_d^1 = 0$; both conventions agree on the qualitative answer.

## Limitations

- Result is for the stated symmetric family (outer points $\\pm 3$,
  $\\pm 1$, middle $\\pm d$); non-symmetric deformations and higher genus
  are not addressed.
- Strict hyperbolicity refers to the symmetry-reduced three-speed system;
  the unreduced six-point spectrum carries a permanent $\\pm E$ doubling.
- Endpoint degenerations $d \\to 0, 1$ (gap closing) lie outside the open
  interval and are not classified here.
- The proof uses only positivity and continuity of $w$ on $(1,3)$; no
  certified interval arithmetic was needed since all inequalities are
  strict sign arguments, with numerics purely illustrative.

## Reproducibility

- `output/artifacts/verify_identity.py`: symbolic check of the collision
  numerator factorization and the $\\beta$-cancellation identity with
  SymPy.
- `output/artifacts/speed_scan.py`: high-precision quadrature scan of the
  Whitham speeds at $d = 0.05$ through $0.99$ with mpmath.

## References

- Y. Kodama, V. U. Pierce, F.-R. Tian, On the Whitham equations for the
  defocusing complex modified KdV equation, arXiv:0710.2632 (defocusing
  analogue with non-strict hyperbolicity; hypotheses differ).
- A. Tovbis, G. A. El, Semiclassical limit of the focusing NLS: Whitham
  equations and the Riemann-Hilbert problem approach, Physica D 333
  (2016), 171-184 (focusing NLS Whitham ellipticity; different equation).
- T. Kappeler, P. Topalov, On an Arnold-Liouville type theorem for the
  focusing NLS and the focusing mKdV equations (finite-gap background).
- G. A. El, A. Tovbis et al., soliton/breather-gas NDR via thermodynamic
  limits of quasimomentum and quasienergy differentials (related
  finite-gap technology; does not imply this claim).

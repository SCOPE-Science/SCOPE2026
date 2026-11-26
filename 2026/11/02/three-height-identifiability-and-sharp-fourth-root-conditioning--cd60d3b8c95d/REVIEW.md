# Independent mathematical audit

## correctness

PASS

I reconstructed the change of variables a=log(2A)−sH², s=1/(2σ²), t=2sH; it is bijective on a real, s>0, t≥0. In u=z² the unknown affine term cancels in the second divided difference. For t>0, differentiating g_t(u)=√u tanh(t√u) twice gives the numerator x sech²x−tanh x−2x² sech²x tanh x over 4u^(3/2), x=t√u. The first two terms are negative because tanh x−x sech²x vanishes at 0 and has positive derivative for x>0; the expansion g_t(u)=tu−t³u²/3+O(u³) handles a knot at zero. Thus F′(t)<0, and bounded error in log cosh(t√u)=t√u+O(1) together with strict concavity of √u gives F→−∞. A unique t therefore exists exactly for Δ≤0; subtraction fixes s, one log reading fixes a, and equality of divided differences fixes the third. A physical triple exists exactly when s>0 as well. With two log readings held fixed, s(t) and a(t) are determined for freely varied nearby t, remaining admissible by continuity, one-sided at zero. The u² Taylor term is −t⁴u²/12 and its divided difference is −t⁴/12. On the fixed-two-reading path, s(t)=s0+t²/2+O(t⁴), H is asymptotic to t/(2s0), and the third reading differs by (u2−u0)(u2−u1)F(t). The leading coefficient is nonzero, ruling out every larger exponent. Also |F′(t)|≥c t³ for sufficiently small t≥0, so integration gives |F(t)−F(t′)|≥c′|t−t′|⁴ and a pairwise local 1/4 estimate for t, then for H since s stays positive and is locally Lipschitz in t and the readings. This is local at physical ground points with positive finite σ, not a bound uniform as σ leaves that regime. The mpmath script is finite corroboration, not needed for any universal inference.

## originality

PASS

The reflected two-image forward factor is standard and is not original. The distinct claim is the global identifiability and explicit compatibility criterion for every prescribed three-height geometry with unknown common spread, together with minimality and the sharp boundary modulus for that finite-sample problem. The accessible competing results use different data, known spread or centers, or estimate different parameters. No inspected result covers the distinct claim.

## value

PASS

For a classical model with confounded amplitude, spread and height, determining whether a prescribed finite vertical profile is sufficient is meaningful rather than just counting parameters. Arbitrary distinct knots, including a surface knot, make the result independent of an optimized sensor design. The compatibility test and sharp boundary instability explain why exact uniqueness does not imply reliable near-ground height recovery. This is an idealized inverse-model result, not a guarantee under noise or model mismatch.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The power series gives Re q(w)≥Q(s)>0 and |q′(w)|≤c/A(s), for s=|w|. Applying Schwarz–Pick to ω(z)/z yields |zω′(z)−ω(z)|≤(r²−s²)/(1−r²), giving the proposed lower bound G_r(s) through the logarithmic derivative identity. The sign of −G′_r(s) is the sign of the stated affine H(r²). Independently, Q(s)=c arccos(s), so cA/Q>s follows from sin x>x cos x for x=arccos(s)>0. Thus H(1)=cA/Q−s>0, and H(s²)=(1−s²)Q+(1−s)²+s(cA/Q−s)>0. This also resolves the harmless strict-inequality slip at s=0 in RESULT.md line 47: the displayed comparison is equality there but its right-hand side is positive. Strict decrease forces s=r; Schwarz equality forces a rotation, and equality in the real-part estimate (already its first series term) fixes w=−r. Integrating zf′/f recovers exactly the claimed normalized extremal aligned to the evaluation point. Q and A decrease, and the numerator cr increases, proving strict radial decrease and both limits. The open disk of radius Rβ has strict order >β, and a larger disk includes an extremal point below β. Independent bisection of (2 arccos(r)/π)²−2r/(π sqrt(1−r²)) confirms 0.538585996535522 rounded. The supplied finite Schwarz-jet diagnostic was inspected, not executed.

## originality

PASS

The supported distinct result is the full sharp pre-Schwarzian profile of the normalized-arcsine starlike class and the aligned equality classification. Its all-order radii are consequences of that profile. Neither the same-target image and strong-starlikeness law nor the compared radii for different targets and classes give that profile.

## value

PASS

The sharp pre-Schwarzian lower envelope is a natural quantitative invariant of this starlike class, resolving the classical transition, all other orders and the extremal geometry. It controls all Schwarz functions and remains exact well beyond the first loss of convexity, so its value is not just a numerical root or a routine inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.

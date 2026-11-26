# Independent mathematical audit

## correctness

PASS

In coordinates z=x(κ/D)^(1/4), the physical time unit is (Dκ)^(-1/2), the generator is ∂zz, and the reset hazard is z². Absorption before a reset has probability u(z), the normalized decaying solution of u''=z²u; the mean duration of a trial solves (−∂zz+z²)q=1, with the zero boundary and bounded solution. The positive Dirichlet Green kernel v(min)u(max), v=u∫₀ᶻu⁻², gives bounded q (in particular q=O(z⁻²) at infinity by the decaying and growing solution asymptotics) and so the killed-diffusion expectation by stopping. Renewal from λ gives M=q(λ)/u(λ), and the unit Wronskian gives (q/u)'=I/u². The time conversion then gives M_phys=(L²/D)m(λ)/λ². For a=−u'/u, b=I/u, one has a'=a²−z² and b'=ab−1. Integration of (u'²−z²u²)'=−2zu² gives a'>0; the positive tilted-integral representation gives a'=1−2 Var(t)<1. With H=(3a²−z²)b−3a/2, h''=2H/u. The gamma values at zero indeed give H(0)>0; at large z, a∼z and b∼1/z give H∼z/2>0. At any positive zero, substitution of b=3a/[2(3a²−z²)] into H' yields z[3a'z−6a−2z³]/[2(3a²−z²)]<0 since a>z and a'<1. A crossing back up is then impossible, proving H>0. Thus F=zh−2m has F''=zh''>0, F(0)=0 and F'(0)=−h(0)<0. Since h'/h=2a−1/b∼z, l'Hôpital gives m∼h/z and F→+∞. It has exactly one positive zero, giving the unique global minimizer via Φ'=F/z³ and the strictly increasing correspondence κ↔λ. Independent 45-digit working precision quadrature of the IVP series u''=z²u with the analytic initial values gives λ≈1.548485175665752, λ⁴≈5.749475240579111 and Φ≈0.939290010529102, agreeing at the stated precision.

## originality

PASS

The literature checked contains the model motivation, a nearby simulation estimate and oscillator/renewal methods, but not the analytic characterization with proof of a unique global optimum for the exact whole-half-line quadratic hazard. The surviving contribution is the explicit MFPT reduction and global optimization, not introduction of adaptive resetting, harmonic-oscillator methods or a finite-range theorem.

## value

PASS

This addresses a physically motivated optimization previously estimated numerically in the parabolic regime. It provides a universal dimensionless minimizer with proven uniqueness, an exact evaluation recipe for all positive curvatures, and the scaling to physical parameters. The useful advance is the analytic global result rather than extra digits or a claim about the saturating model.

The dated certificate retains the supplied scientific assessment, sources and limitations.

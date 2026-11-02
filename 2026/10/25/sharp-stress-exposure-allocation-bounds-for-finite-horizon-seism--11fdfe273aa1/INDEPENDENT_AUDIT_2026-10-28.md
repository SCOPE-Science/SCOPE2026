# Independent mathematical audit

## correctness

PASS

With constant normal stress, normalized Dieterich state Γ satisfies Γdot=(1-Γ)/a−Γ sdot, and stress jumps multiply Γ by exp(-Δs). Integrating factor gives Γ(t)=exp(-t/a−s(t))D(t), D(t)=1+(1/a)∫_0^t exp(u/a+s(u))du, hence N_s(T)=ra log D(T). Strict convexity e^z≤1+[(e^H-1)/H]z (equality iff z=0,H), followed by strictly increasing-weight bathtub rearrangement, proves unique max s=H on the last B/H units. For min, the pointwise strictly convex Lagrangian exp(x+z)−exp(C)z on [0,H] has unique minimizer clamp(C−x,0,H); its budget is continuous strictly monotone in C∈(0,H+T/a), guaranteeing unique C for 0<B<HT. Integrating three plateaus reproduces exact N_min and N_max. Independent calculation gives C=7/2−√2, N_min≈2.76976928170860,N_max≈3.27086268884977 at a=r=1,T=2,H=1.5,B=2; 100 independent budget-feasible discrete profiles lie between analytic bounds. Finite tests do not replace rearrangement proof.

## originality

PASS

Dieterich 1994 defines the underlying seismicity law; Heimisson–Segall 2018 full accessible paper derives arbitrary-stress cumulative count formula (Eq.18), fully credited. That evaluation kernel alone does not solve fixed-integral stress-exposure optimization. The primary 2018 article focuses derivation, rate evolution and assumptions, not unique extrema over all bounded histories. Ziv 2003 analyzes fixed pulses; Candela et al. 2022 and a 2026 Groningen controller optimize physically coupled injection/feedback variables and different objective. Generic convex duality and rearrangement are known methods, so the novelty is only their explicit budgeted seismicity application; possibility of generic equivalent published optimizer remains a residual risk.

## value

PASS

A model-specific sharp all-measurable-history extrema theorem gives the exact optimal stress shape, multiplicative count bounds, and uniqueness at prescribed exposure and cap. It distinguishes late concentrated forcing and early tapering in an ideal constitutive model. The modeled objective is expected nucleation count, not injection operations or risk of damage, and these restrictions are central.

The dated certificate retains the supplied scientific assessment, sources and limitations.

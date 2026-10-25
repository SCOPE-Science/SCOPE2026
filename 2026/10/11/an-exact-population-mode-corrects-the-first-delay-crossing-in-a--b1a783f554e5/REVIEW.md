# Independent mathematical audit

## correctness

PASS

Reconstructed directly from equations (5.1), not the packaged VERIFY_OK: with I=(2/25)S(P1+5P2/4)/(1+S), the four equations sum to Ndot=6/5−N/50 and the positive rational equilibrium E*=(1407/4561,544506/305587,105271160/2139109,18603955/2139109), N*=60, solves all four equations exactly. Independently differentiated current and delayed flows with SymPy: A0[1,1]=−3001/14920 and delayed transfer B[1,1]=−9/20,B[2,1]=+9/20 (zero-index). Reconstructed exact det=(50λ+1)[P(λ)+Q(λ)e^(−λτ)]/17493700000000 with P and Q coefficients identical to RESULT.md. For u=Ω² the exact modulus difference polynomial has signs +,+,+,−; derivative positive on u>0, one positive root u*=0.15333341881484640431595... giving Ω*=0.39157811329905353166..., phase τ*=5.31769616572693033590..., and d(Re λ)/dτ=0.0169758691356183881044... >0. At τ=0 cubic coefficients all positive and exact Routh–Hurwitz determinant 2548962325924970823125000>0 after unscaled normalization; factor −1/50 is stable. Zero λ cannot be a root because P(0)+Q(0)>0 independent of delay. Standard retarded-system root continuity and absence of any earlier imaginary frequency prove first loss of linear asymptotic stability. The published Ω=0.320220 does not satisfy reconstructed modulus equality. All numbers are tied to printed δ=0.02 equations, not prose δ=0.2. No nonlinear Hopf branch/first Lyapunov coefficient certified.

## originality

PASS

Best-of-knowledge source-specific originality: the direct published equation (5.1) has its own printed 5.105862/0.320220 thresholds, not the corrected first linear crossing 5.31769616572693034/0.39157811329905353. The earlier Saha--Samanta paper already states the total-population law for its NONDELAYED precursor (so this cancellation itself is not credited as new), and standard characteristic factoring and retarded-delay crossing methods are known. Nevertheless these earlier sources do not provide the exact corrected factorization and stable-delay boundary for the particular printed delayed system. The other Zhang--Yang--Xia two-delay model is structurally different. A same-record Resultary hit is not independent prior evidence. Searches are not exhaustive priority certification.

## value

PASS

The exact population identity itself is elementary and explicitly appears for the 2019 nondelayed ancestor, so it cannot alone justify value. The substantive result is a concrete correction of a published stability/Hopf benchmark: the first linear stability boundary moves from reported τ0=5.105862 to 5.3176961657..., a shift 0.2118341657 (~4.15%), with corrected imaginary frequency, an exact factorization that explains the redundant dimension, and a rigorous unique-first-crossing proof. This has direct use for reproducing the paper’s simulations, distinguishing the reported τ=5.3202 run (only 0.00250 beyond corrected crossing), and checking its bifurcation claims. It is not an arbitrary rounding improvement or a fabricated general theorem. The claim is limited to a specified printed parameter set; no new general theorem or nonlinear Hopf normal form is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.

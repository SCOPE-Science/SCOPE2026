# Independent mathematical audit

## correctness

PASS

The stated nonnegative feasible domain is invariant by the coordinate boundary derivatives and N′=r(S+E)(1−N)−μI for N=S+E+I. F stays bounded, and S(0)>0 implies S(t)>0. With u=1−S and W=E+I+(β_f/ω)F, direct differentiation at criticality gives W′=−uΛ, where Λ=β₁I+β_f F. The bound Λ≤CW gives strict finite-time W>0 for every seed. The only forward trajectories remaining in uΛ=0 have E=I=F=0: at u=0, feasibility gives E=I=0 and any F>0 immediately decreases S; at u>0, sustaining Λ=0 implies successively F=I=E=0 on a neighborhood. LaSalle on the bounded trajectory then gives W→0, and late logistic lower bounds with carrying capacities arbitrarily close to 1 give S→1. The infection block has positive left and right null vectors ℓ,v with ℓᵀv=D. Its irreducible Metzler structure, through the E,I,F cycle even at β₁=0, gives a simple zero and a stable complement. Since |(log W)′|≤Cu→0, W(s)/W(t)≤exp(ε(t−s)) at late times, and each fixed-lag ratio tends to one. The stable complement forced by O(uW)=o(W) is o(W) by convolution and exponential domination. Thus Λ/W→μ/D and (E,I,F)/W→v/D. Expanding u′ gives stable linear decay −ru, source r(E+I)+Λ, and remainder o(u+W). Comparison first gives u=O(W), then the fixed-lag ratio and dominated convergence in its stable convolution give u/W→K/D. Hence (1/W)′→μK/D², and integration yields the four limits in original time. The argument does not assume prior algebraic decay or restrict the initial seed to a neighborhood. Frozen RESULT.md lines 28–76 are the infinite proof. The uploaded script was inspected, not executed: its three positive-β₁ cases check numerical I and S amplitudes, not all four coordinates or β₁=0. An independent finite diagnostic integrated the stated ODE with DOP853, rtol=10⁻¹⁰, atol=10⁻¹² to T=200000, (r,γ,μ,ρ,ω,β_f,β₁)=(1,2,1,1,1,1,0) and seeds (.8,0,0,.1) and (.1,.3,.1,.2). Both scaled vectors were within 0.00052 in max norm of (2.5,0.5,1,1); this checks implementation at the endpoint, not the global theorem.

## originality

PASS

The distinct claim is the explicit four-coordinate critical amplitude and convergence for every feasible seeded trajectory with S(0)>0 in the exact stated model, including β₁=0. The original model and transcritical threshold are established prior work. The general t⁻¹ mechanism and projection onto a nonhyperbolic positive eigenvector are not claimed as new. Neither the same-model threshold analysis nor the available different-model profile results establish these coefficients and basin. No equivalent or stronger covering result was established in the bounded comparison.

## value

PASS

At the exact threshold the linearization predicts no strict exponential decay, while threshold and stability classifications leave the decay coefficient unknown. The explicit slow profile shows how the four components share the critical mode and separates the roles of the stable susceptible response and the infection-mode normalization. Proving it for the full seeded basin rather than only on a local center manifold gives precise information the original critical equilibrium result does not supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.

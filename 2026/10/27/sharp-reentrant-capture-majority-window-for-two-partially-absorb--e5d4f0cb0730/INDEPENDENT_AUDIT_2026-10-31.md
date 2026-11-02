# Independent mathematical audit

## correctness

PASS

For diffusion D∂xx with two delta killing hazards at −a and 2a and Poisson resetting to zero, each reset interval has 2x2 killed-resolvent occupation equations with positive determinant. Their explicitly solved local fluxes yield P_R/P_L=(B/A)e^(−t)[2t+A(1−e^(−2t))]/[2t+B(1−e^(−4t))], t=a√(r/D), A=κ_L a/D and B=κ_R a/D; renewal divides both capture fluxes by their positive sum. The continuous zero-reset limit is B(1+A)/[A(1+2B)]. Clearing positive terms gives P_R>1/2 iff A<H_B(t), with H_B(0)=B/(1+B), H_B(∞)=0, and positive derivative at 0 precisely for B>1. For B≤1 the comparison K(B,t) is affine in B, negative at endpoints B=0,1 by t<sinh(t); hence no window exists. For B>1 the positive slope creates the exact open A interval. The strict A=11/10,B=100 witness crosses at least twice. A separately formulated NumPy 2x2 matrix solve verified 175 parameter samples and the majority inequality; universal proof is the analytic affine argument, not those samples.

## originality

PASS

The older full two-defect resolvent already implies the forward two-flux ratio (not claimed new). What survives is the explicit global B>1 iff feasibility threshold and exact A-window for reentrant ultimate-capture majority under the asymmetric 1:2 geometry. The accessible sections of prior resetting papers do not give this completed threshold analysis.

## value

PASS

Ultimate capture selectivity among two imperfect targets is a natural transport observable. A sharp iff condition for a farther target winning only at intermediate reset rates provides a structurally nonmonotone phase diagram, not just a numerical crossing or re-evaluation of a known propagator.

The dated certificate retains the supplied scientific assessment, sources and limitations.

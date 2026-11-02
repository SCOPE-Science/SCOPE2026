# Independent mathematical audit

## correctness

PASS

The quadratic Hamiltonian and zero-temperature Lindblad loss yield the displayed real drift A with invariant (q_c,p_h) and (p_c,q_h) 2x2 blocks, characteristic polynomials lambda^2+(d-Omega)lambda+g^2 and lambda^2+(d+Omega)lambda+g^2. For g>0, 0<Omega<d=gamma/2 both are strictly Hurwitz, so the covariance Lyapunov ODE has a unique stable fixed point. Direct substitution proves V_inf=diag(v+,v-,v-,v+), v+=d/[2(d-Omega)], v-=d/[2(d+Omega)], whose cross block is exactly zero; the zero-mean stationary Gaussian state factorizes and has occupation Omega^2/[2(d^2-Omega^2)]>0. The exact covariance flow V(t)=V_inf+e^{At}(I/2-V_inf)e^{A^Tt} gives charger squeezes O(t), off-block correlations -g Omega t^2/2[[0,1],[1,0]]+O(t^3), and local determinants 1/4+O(t^3). Local symplectic reduction and Gaussian PPT eigenvalue expansion give nu_tilde_- =1/2-g Omega t^2/2+O(t^3), hence E_N=g Omega t^2+O(t^3). Since limiting PPT eigenvalue sqrt(v+v-)=d/[2sqrt(d^2-Omega^2)] is strictly >1/2, continuity plus exponential covariance convergence gives one finite T beyond which entanglement never returns. A NEW independent matrix-exponential computation verified the Lyapunov residual (<=5.6e-17), Hurwitz condition, four sample small-time coefficients and stationary strict PPT gaps; these finite samples corroborate, not establish, the arbitrary-parameter analytic result.

## originality

PASS

The original 2023 Downing–Ukhtary paper studies the identical quadratic charger–holder model and explicitly gives stationary energy at Delta=0, which is prior and not treated as new. The full openly available main article, including quadratic Hamiltonian Eq. (30), energy Eqs. (39),(42), and detuned figure 5, was inspected. It does not expressly give in that text the exact-resonance short-time PPT coefficient, late-time strict PPT gap and coupling-independent factorized steady covariance as this complete claim. Simon supplies the known Gaussian PPT criterion, and passive-beam-splitter or uncoupled-mode papers supply techniques, not a stronger dynamic theorem for this one-sided-damped pumped pair. Original supplementary first/second-moment derivations were TOO LARGE for accessible full-text retrieval and could imply an equivalent stationary result. Best-of-knowledge O PASS with that exact plausible source and older Gaussian-literature risks explicit; no whole-supplement negative assertion is made.

## value

PASS

A natural open two-mode bosonic battery demonstrates immediate nonzero Gaussian entanglement from a vacuum input but a uniquely attracting exactly product stationary state with nonzero stored holder energy. The coefficient g Omega in the small-time log-negativity and a strict long-time PPT gap for all positive couplings give sharp structural information about quantum correlations versus energetic usefulness and about steady measurements hiding transient correlations. This is a mathematically meaningful model classification beyond a routine parameter substitution, while not asserting a unique first death time or generic baths.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

Forward row updates give S_i^(s)=q S_(i-1)^(s)+q d_n^(s-1)+c S_i^(s-1), q=(1+a)^-1, c=a/(1+a), d=1-a sum x. The infinite profile psi_i^(s)=q^i c^(s-1) C(i+s-2,s-1) has generating function qz c^(s-1)/(1-qz)^s and sum 1/a. Uniform errors and geometric-polynomial tails are exponentially small for each fixed s, so the finite vector tends to the squared-summable profile. The coefficient residual entries are d-x_i, giving ||res||²→sum psi_i² and relative squared residual ∼gamma_s/(a n). Exact embedding Q_i=e_i+sqrt(a)e_0, r=e_0/sqrt(a) produces W=Q^TQ, Q^Tr=1 and the identity physical squared relative residual=d²+a||x||²→gamma_s. Pythagorean projection identity gives relative W-energy squared error→gamma_s; optimum physical residual fraction is 1/(1+an). Gamma_1=1/(a+2) and Gamma_2=((1+a)^2+1)/(a+2)^3. Six independent n=2048 sweeps and exact/float comparison reproduce constants. Infinite limits rely on exponential error analysis, not finite experiments.

## originality

PASS

Classical residual-vs-error conditioning warns of this qualitative risk, while the 2026 D’Ambra et al Chebyshev s-step PCG paper recommends/analyses forward GS Gram solves in practical regimes, and Thomas–D’Ambra 2025 discuss inexact GS/coarse solvers. Available abstracts and method descriptions do not give this all-fixed-sweep equicorrelation profile or exact physical Galerkin error limits. The methodological gap is narrow and potentially covered by earlier specialized rank-one GS matrix literature; preserve that explicit risk.

## value

PASS

Motivated by the interpretation of Gram-residual stopping rules for low-synchronization s-step Krylov methods, this natural equicorrelated SPD family proves that any fixed positive sweep budget can falsely pass a dimension-independent residual tolerance while leaving a fixed fraction of optimal Galerkin energy reduction unrealized. The physical embedding, equal column norms and explicit gamma_s for all fixed s give more than a generic condition-number warning; no claim is made about actual Krylov basis realizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

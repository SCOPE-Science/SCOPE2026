# Independent mathematical audit

## correctness

PASS

For a nondegenerate tail on f(x)=lambda x²/2, the exact source local smoothness quotient equals lambda, so r_k=lambda s_k satisfies r_(k+1)=min(A_k*r_k,B_k*r_k,C_k), with A_k=(t_(k+1)-m)/(t_(k+1)-1)>1, B_k=2(t_(k+1)-1)/[(1+beta)gamma t_(k+1)]>1 and C_k=(1-omega)/(2/B_k+1/[beta gamma (1-eta)A_k]). Published t recursion gives t_k=Theta(k), hence product A_k diverges and product min(A_k,B_k) diverges. C_k tends to Cinf; a positive growing recurrence capped by C_k converges to it for every r0>0. Optimize Cinf by x=beta gamma, y=(1+beta)gamma with 0<x<y<=2q, gamma=y-x<2, beta=x/(y-x)>0, where q=[2(t0-1)+m]/(2t0+m); its unattained supremum is 2q/(1+4q²) for q<=1/2 and 1/2 otherwise. If t0=1,m in (0,1), q<1/3 and uniform strict bound 6/13. The full published paper (2026 version, NOT 2025 preprint parameter set) permits t0=1. Distinct consecutive iterates is needed; cap removal on repeats excluded.

## originality

PASS

The full open 2026 Wang-Peypouquet version contains the exact three-way update and qualitative step growth/lower bound but no analyzed scalar-quadratic limiting cap and optimal transformed-parameter envelope. Its generic complexity results do not state this asymptotic recurrence solution. Related Malitsky-Mishchenko, Suh-Ma algorithms use different update recurrences. Qualified original source-specific analysis.

## value

PASS

The exact asymptotic cap and sharp source-admissible parameter ceiling quantify the tradeoff of the three published Lyapunov safeguards even when curvature is exactly measured. It is a nontrivial, natural algorithmic performance ceiling and parameter-design diagnostic; no unsupported claim about total inertial acceleration or practical wall-clock speed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

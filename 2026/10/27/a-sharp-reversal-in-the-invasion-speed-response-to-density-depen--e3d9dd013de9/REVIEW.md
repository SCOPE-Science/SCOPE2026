# Independent mathematical audit

## correctness

PASS

The normalization extracts the speed factor √(ρD₀). The crowding map from Li–Buenzli–Simpson yields d_b=1+b u(2−u), strictly positive for the stated −1<b≤1. For the decreasing front, the change of independent variable ds/dz=1/d_b(U) gives an ordinary scalar bistable equation V_ss+cV_s+d_b(V)f_a(V)=0 with the same c. The cited general theorem applies to the unbalanced smooth p=2 case, with reflection or its sign-reversed remark for negative speed; positivity of d_b and hyperbolicity give strict decrease and infinite tails. The balance case is covered by the explicit zero-speed quadrature: the partial weighted integral from u to 1 is positive inside (0,1) and vanishes quadratically at both endpoints. Independently, setting p(u)=−d_b(U)U′ yields p p′−c p+d_b f_a=0 for 0<u<1, p(0)=p(1)=0. Integrating gives c∫p=∫d_b f_a=[5+4b−(10+7b)a]/60. At b=0 use p₀=u(1−u)/√2 and c₀=(1−2a)/√2. The linearized flux equation has integrating factor proportional to I(u)=u^(2a)(1−u)^(2−2a). For partial differentiation with respect to c, the two endpoint branches satisfy (I p_c)′=I; their values at the midpoint differ by ∫₀¹I/I(1/2)>0. Smooth saddle branches and the matching implicit-function theorem thus justify differentiability and the O_a(b²) remainder. Along the matching branch (I p_b)′=I(c₁−q f_a/p₀) with q=u(2−u); the integrated endpoint terms vanish. This gives the beta moment √2 E[q(U)(U−a)] and the displayed polynomial. Its only root in (0,1) is a_*=(17−√145)/8; the sign concerns the derivative at b=0, not global speed monotonicity. The full-line existence and exact identities are analytical. Fresh finite collocation in the stretched coordinate (python3 /workspace/reproductions/frozen_checks.py 4) found the predicted signs on both sides, a symmetric slope about 9.8×10⁻⁸ at a_*, and speeds below 1.5×10⁻¹² in absolute value at the two checked balance points. These are finite truncation checks, not proof of the limiting derivative.

## originality

PASS

The general wave theory and weighted-area direction boundary are existing results or direct model substitutions; the crowding-law example itself is also prior work. The distinct supported claim is the evaluated first-order speed sensitivity for this natural crowding flux and its nontrivial sign reversal strictly within the unperturbed retreat regime. The inspected same-family primary results address finite-strip survival, while the general speed results inspected give existence, sign, or bounds, not the first-order coefficient. The exact coefficient is obtained by solving a sensitivity condition rather than just applying the weighted sign theorem. Related unavailable papers are residual risks, not evidence for or against novelty by themselves.

## value

PASS

The motility parameter is motivated by an existing crowding law. The exact sensitivity locates a distinction invisible to the direction law: as motility is strengthened locally, a retreating front retreats more slowly when 1/2<a<a_* but faster when a>a_*. The evaluated threshold is needed to identify that regime, rather than merely show that speeds can vary. This is a whole-line result about normalized front dynamics, not a claim about stochastic extinction, finite-strip survival or arbitrary b.

The dated certificate retains the supplied scientific assessment, sources and limitations.

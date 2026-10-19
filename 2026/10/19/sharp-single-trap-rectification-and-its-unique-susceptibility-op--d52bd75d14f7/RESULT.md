# Sharp single-trap rectification and its unique susceptibility optimum in a four-site exclusion channel

## Finding

For the four-site open simple-exclusion channel defined below, place a single defect of relative departure speed \(u>0\) at the second site; the other three departure speeds are one. At mean reservoir density \(1/2\), the stationary physical particle current \(J_u(d)\) under a left-to-right reservoir-density contrast \(d\) has the exact response
\[
J_u(d)=\frac{u B(u)}{Q(u)}d+\frac{u(u-1)P(u)}{(u+1)Q(u)^2}d^2+O_u(d^3),\qquad d\to0.
\]
The polynomials \(B,Q,P\) are explicitly given below and have strictly positive coefficients. Therefore its quadratic rectification coefficient has the **exact sign of \(u-1\)** and vanishes precisely at \(u=1\). Among physical slowed traps \(0<u<1\), the magnitude of this quadratic coefficient has **one and only one maximizer**:
\[
u_* =0.31891357651681155147\ldots,
\qquad -[d^2]J_{u_*}(d)=0.0032361339998734794835\ldots.
\]
Equivalently, the optimal slowdown potential depth is \(E_*/T=-\log u_*=1.1428351329127431698\ldots\), with thermal energy as the unit. For equal-speed sites \(u=1\), the exact current is \(J_1(d)=d/10\). The four-site channel is the smallest nontrivial open channel of this single-interior-defect type for which mirror asymmetry and rectification can occur: at three sites the lone interior defect is mirror-centered.

## Assumptions and scope

The system has sites \(1,2,3,4\), each occupied by at most one particle. Particles hop only into vacant nearest-neighbor sites, independently at each oriented edge, with **physical** outgoing hop rate \(w_i/2\) from occupied site \(i\), where
\[
(w_1,w_2,w_3,w_4)=(1,u,1,1),\quad u>0.
\]
The left reservoir inserts into vacant site \(1\) with rate \(\rho_L/2\) and removes from occupied site \(1\) with rate \((1-\rho_L)/2\). The right rates at site \(4\) are \(\rho_R/2\) and \((1-\rho_R)/2\). Fix
\[
\rho_L=(1+d)/2,\quad \rho_R=(1-d)/2,\quad |d|<1.
\]
The finite irreducible Markov chain has a unique stationary distribution. \(J_u(d)\) is the mean net flux from site \(2\) to \(3\), positive rightwards, per unit physical time. The Taylor coefficient \([d^2]J_u(d)\) is defined without a factorial, and rectification is the even-current part \(J_u(d)+J_u(-d)=2[d^2]J_u(d)d^2+O_u(d^4)\). A positive or negative contrast may reverse the current, but a nonzero quadratic response means its magnitude changes when the gradient is reversed. No asymptotic thermodynamic or finite-gradient optimum is asserted.

## Proof

**1. Exact finite-state generator and equilibrium.** Number configurations by \(\boldsymbol\eta\in\{0,1\}^4\). For an oriented allowed transition \(\eta\to\eta'\) across bond \(i,i+1\), the departure rate is \(w_i/2\) or \(w_{i+1}/2\), respectively. At a boundary use the insertion/removal rates in the assumptions. These 16 configurations define the entire generator \(\mathcal L(d)\). Multiply physical rates by two to work with \(M(d)=M_0+dM_1\), where the off-diagonal entries of the **column** generator are twice the rates just specified; diagonal entries are the negative exit rates. Since \(u>0\) and \(|d|<1\), this generator is irreducible. At \(d=0\) the stationary law is the product of Bernoulli laws with occupations
\[
\mathbf p=(1/2,\;1/(1+u),\;1/2,\;1/2).
\]
Detailed balance holds: for every bond the stationary hop flux factors as \(p_i(1-p_{i+1})w_i=p_{i+1}(1-p_i)w_{i+1}\), and the reservoirs satisfy the corresponding boundary identities. Thus the 16-vector \(\boldsymbol\pi_0\) obtained by multiplying Bernoulli factors satisfies \(M_0\boldsymbol\pi_0=0\) and has sum one.

**2. Exact Taylor coefficients.** Write the unique stationary law near \(d=0\) as \(\boldsymbol\pi(d)=\boldsymbol\pi_0+d\boldsymbol\pi_1+d^2\boldsymbol\pi_2+O_u(d^3)\). Equating powers and normalizing gives
\[
M_0\boldsymbol\pi_1=-M_1\boldsymbol\pi_0,\qquad
M_0\boldsymbol\pi_2=-M_1\boldsymbol\pi_1,\qquad
\mathbf1^\mathsf T\boldsymbol\pi_1=\mathbf1^\mathsf T\boldsymbol\pi_2=0.
\]
Replace one row of \(M_0\) with \(\mathbf1^\mathsf T\) to obtain a nonsingular rational matrix \(A\), and replace that row of \(M_1\) with zeros. Consequently each correction follows from one **exact rational** linear system. Define the integer-valued bond-current observable \(c(\boldsymbol\eta)=u\,\eta_2(1-\eta_3)-\eta_3(1-\eta_2)\). Restoring the factor of two in the physical time convention,
\[
[d]J_u(d)=\tfrac12\mathbf c^\mathsf T\boldsymbol\pi_1,\qquad
[d^2]J_u(d)=\tfrac12\mathbf c^\mathsf T\boldsymbol\pi_2.
\]
Symbolic rational elimination yields
\[
\begin{aligned}
B(u)&=238u^4+2642u^3+10365u^2+17100u+9975,\\
Q(u)&=2380u^5+24584u^4+90837u^3+149179u^2+108535u+27685,\\
P(u)&=232560u^8+4331572u^7+33739658u^6+142316303u^5+351379457u^4+510425170u^3+411771380u^2+155893675u+15612625.
\end{aligned}
\]
Every coefficient displayed is strictly positive and the denominator \((u+1)Q(u)^2\) is positive for \(u>0\). The two formulas in the Finding and the sign assertion follow. The attached standalone checker reconstructs \(M(d)\) directly from the 16 transitions, verifies the product equilibrium, solves both exact perturbative equations, and checks **symbolic equality** with the stated coefficients. The polynomial identities are therefore verified by exact arithmetic, not a fit to simulations.

**3. Sharp optimum.** Let \(f(u)=u(u-1)P(u)/((u+1)Q(u)^2)\), so \(f(0)=f(1)=0\) by continuous extension and \(f(u)<0\) for \(0<u<1\). Write \(f'(u)=N(u)/D(u)\), with \(D(u)>0\) for \(u>0\), using \(N\) as the numerator of the derivative without cancelling its positive denominator. Substitute \(u=x/(1+x)\); the polynomial
\[
H(x)=(1+x)^{15}N\!\left(\frac{x}{1+x}\right)
\]
has degree 15, with its coefficients **in ascending degree** of signs \((-,-,-,-,-,-,-,+,+,+,+,+,+,+,+,+)\). These exact signs are checked by integer arithmetic in the attached code. In descending degree there is precisely one sign change, so Descartes' rule permits at most one positive root, counted with multiplicity. Because \(N(0)<0\) and \(N(1)>0\), such a root exists in \(u\in(0,1)\). This root is unique, and \(f\) decreases then increases around it; hence it is the unique global minimum of \(f\) and unique global maximizer of \(|f|\) on \(0<u<1\). High-precision root isolation gives the decimal values quoted; they are approximations to a mathematically characterized algebraic root.

**4. Minimum channel size.** With symmetric end-site departure rates and only one variable interior site, the sole variable interior site for a three-site channel is the center. Spatial reflection simultaneously exchanges the reservoir densities and reverses the signed current, so \(J(d)=-J(-d)\), and the quadratic term vanishes. At four sites a lone second-site defect is not reflection-symmetric; Step 2 shows its quadratic coefficient is nonzero whenever \(u\ne1\). Thus four sites is the sharp minimum within this explicitly defined family.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The checker independently enumerates all \(16\) states and transition rates, proves the stationary product law at equilibrium, computes \(\boldsymbol\pi_1,\boldsymbol\pi_2\) using exact matrix inversion, matches the stated rational coefficients identically, checks positivity of polynomial coefficients, verifies the exact one-sign-change Descartes certificate, and computes the optimum. It additionally compares the truncated response with **six independent exact finite-contrast stationary solutions** for three defect rates and two density differences. The latter are corroboration, not a proof of the global coefficient identities, which are proved by exact algebra.

## Relationship to prior work

Sakai and Akimoto [1] introduce the boundary-driven disordered exclusion model and report sample-specific rectification-like behavior; their full-paper treatment includes numerical and approximate finite-bias response and a reflection-symmetry argument. This analysis retains their dynamics and boundary convention, but provides a symbolic theorem for the entire continuously varying **single-interior-defect family** at half-filled reservoirs: a necessary-and-sufficient sign criterion, an exact unique optimal slow-trap rate, and the smallest possible channel length for such a defect. The independent related work [2] studies a ring with an external driving field rather than two open reservoirs; it does not establish this open-system theorem. General finite Markov-chain perturbation methods are prior mathematics; the model-specific closed polynomial identities and sharp optimization are the assertion here.

## Limitations

The findings concern a finite four-site open system, one defect at site two, equal reference times, mean reservoir density exactly \(1/2\), and the *quadratic near-equilibrium* response. Neither a universal sufficiency result for all disordered exclusion chains nor a claim about optimal finite-amplitude rectification is made. The algebraic root has no elementary closed form claimed. Potential implicit coverage by more general exact disordered-exclusion formulas is an originality risk; these formulas have not been proved absent. No independent audit has been performed.

## References

[1] Sakai and Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (first public 2026-09-03); full-text Sections II, IV and discussion examined.

[2] Sakai and Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1; full-text model and response sections examined (periodic field-driven system).

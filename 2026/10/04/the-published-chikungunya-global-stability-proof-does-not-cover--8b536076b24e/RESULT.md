# The published Chikungunya global-stability proof does not cover its calibrated recruitment rates
## Finding
In the SEITR–SEI Chikungunya model of Ndonane, Ngarasta, and Ntaganda, Proposition 3.4 states that the disease-free equilibrium is globally asymptotically stable when \(\mathcal R_0<1\). The proof's final Castillo–Chavez step, however, explicitly uses the auxiliary comparisons \(\pi_h\ge\pi_m\) and \(S_m\le N_h\) to conclude \(\widehat G\ge0\). Those comparisons are not included among the proposition's hypotheses or the model's stated positivity assumptions. The numerical parameter table gives \(\pi_h=0.0684\) and \(\pi_m=0.2223\), so \(\pi_h\ge\pi_m\) fails for the calibrated parameter set. Therefore the displayed proof does not establish Proposition 3.4 for the parameter values used in the paper's numerical study.

## Assumptions and scope
The claim concerns only the logical coverage of the published global-stability proof for the deterministic model (1)–(8). Recruitment rates \(\pi_h\) and \(\pi_m\) denote the constant human and mosquito recruitment rates used by the source. The populations \(N_h\) and \(S_m\) are the source's total human and susceptible-mosquito populations. No claim is made that the disease-free equilibrium is actually unstable when \(\mathcal R_0<1\), nor that the theorem cannot be repaired by a different Lyapunov or comparison argument.

## Proof
The source states that all model parameters are positive and later states Proposition 3.4 without an additional ordering assumption on the two recruitment rates. In its proof, the system is put into the Castillo–Chavez form and the nonlinear remainder \(\widehat G\) is required to be componentwise nonnegative. For one component the source uses \(S_h\le N_h\). For the other nontrivial component the displayed argument explicitly says that, from \(\pi_h\ge\pi_m\) and \(S_m\le N_h\), the required term is nonnegative; it then concludes \(\widehat G\ge0\) and invokes the Castillo–Chavez theorem.

The numerical parameter table later gives the calibrated values
\[
\pi_h=0.0684,\qquad \pi_m=0.2223.
\]
Hence
\[
\pi_h-\pi_m=-0.1539<0,
\]
so the recruitment-order inequality used in that proof is violated by the source's own calibrated parameter set. Because the nonnegativity conclusion is the step by which the cited global-stability criterion is activated, that displayed proof does not certify the proposition for the calibrated regime. The conclusion here is deliberately narrower than a counterexample to the theorem itself.

## Verification
The source was inspected at the proposition statement, the final \(\widehat G\) argument, the stated parameter assumptions, and the numerical parameter table. The arithmetic check \(0.0684<0.2223\) is reproduced by `verify.py`. The proof-coverage conclusion requires no simulation or asymptotic approximation.

## Relationship to prior work
The source cites Castillo–Chavez, Feng, and Huang's global-stability framework and attempts to verify its nonnegative-remainder condition. The present finding is not a new epidemic threshold formula; it identifies that the source's own displayed verification uses an extra recruitment-order relation that is absent from the proposition and fails for the source's calibrated values. Searches of the indexed research ledger using the exact DOI, theorem label, recruitment-rate symbols, Castillo–Chavez terminology, and equivalent proof-gap formulations did not locate a prior item stating this source-specific incompatibility.

## Limitations
The result is a proof-applicability diagnosis, not a disproof of global stability. A different proof could establish the theorem over a larger parameter domain. The second displayed comparison \(S_m\le N_h\) is also not among the source's stated model assumptions, but the accepted claim needs only the independently decisive violation \(\pi_h<\pi_m\) in the calibrated table. Literature searches cannot prove universal absence of an unpublished or poorly indexed correction.

## References
Ndonane, B., Ngarasta, N., and Ntaganda, J. *A mathematical model of Chikungunya transmission dynamics: an application to data from Chad*. Far East Journal of Mathematical Sciences 143(10), 3353–3384 (2026). DOI: 10.17654/0972087126183. Published online 2026-08-12.

Castillo–Chavez, C., Feng, Z., and Huang. *On the computation of \(\mathcal R_0\) and its role on global stability*. In *Mathematical Approaches for Emerging and Re-emerging Infection Diseases*, IMA Volumes in Mathematics and its Applications 125, 31–65 (2002), as cited by the motivating source.

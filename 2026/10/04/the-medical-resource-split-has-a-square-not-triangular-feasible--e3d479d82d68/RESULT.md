# The medical-resource split has a square, not triangular, feasible set
## Finding
Zhuang, Zhu, Lu, Cheng and Tan parameterize four fractions of one emergency-medical-resource pool by
\[
 p_1=\\sigma\\alpha_1,\qquad p_2=\\sigma(1-\\alpha_1),\qquad p_3=(1-\\sigma)\\alpha_2,\qquad p_4=(1-\\sigma)(1-\\alpha_2),
\]
with \\(0\\le\\sigma,\\alpha_1,\\alpha_2\\le1\\). Under that parametrization the total-resource constraint is already exact: every pair \\((\\alpha_1,\\alpha_2)\\in[0,1]^2\\) gives nonnegative shares whose sum is one. The later restriction \\(\\alpha_1+\\alpha_2\\le1\\) is therefore not implied by the resource budget and excludes valid allocations.

The inconsistency is visible in the paper's own Wuhan case study. It reports the within-unvaccinated split \\(0.6242:0.3758\\) and the within-vaccine-failure split \\(0.8157:0.1843\\). Thus the two first coordinates are \\(\\alpha_1=0.6242\\) and \\(\\alpha_2=0.8157\\), for which
\[
\\alpha_1+\\alpha_2=1.4399>1.
\]
So the displayed case-study policy violates the paper's feasible set \\(U\\), even though it is admissible under the allocation fractions that define the model.

For the instantaneous objective \\(\\max\\{R_1(\\alpha_1),R_2(\\alpha_2)\\}\\), the corrected square domain also yields the exact value
\[
\\min_{(\\alpha_1,\\alpha_2)\\in[0,1]^2}\\max\\{R_1(\\alpha_1),R_2(\\alpha_2)\\}
=\\max\\left\\{\\min_{\\alpha_1\\in[0,1]}R_1(\\alpha_1),\\min_{\\alpha_2\\in[0,1]}R_2(\\alpha_2)\\right\\}.
\]
Hence the one-dimensional boundary search \\(\\alpha_2=1-\\alpha_1\\) in Eqs. (19)–(20) solves a different, artificially coupled problem.

## Assumptions and scope
The claim is about the allocation variables exactly as defined in Section 4 of the source: \\(\\sigma\\) is treated as the top-level share between the two vaccination-status strata, while \\(\\alpha_1\\) and \\(\\alpha_2\\) split those stratum shares between moderate and severe cases. The conclusion applies for fixed \\(\\sigma\\in[0,1]\\). If \\(\\sigma\\) is itself optimized, it needs its own admissible range, but that still does not generate the condition \\(\\alpha_1+\\alpha_2\\le1\\).

This finding does not rederive the epidemiological next-generation matrix, does not assess the paper's state equations outside this allocation layer, and does not claim that any particular alternative dynamic policy is globally optimal over a full state-coupled time horizon. The last displayed minimax identity concerns only the source's instantaneous objective at a fixed time.

## Proof
For arbitrary \\(\\sigma,\\alpha_1,\\alpha_2\\in[0,1]\\), each \\(p_i\\) is nonnegative. Moreover,
\[
\\begin{{aligned}}
p_1+p_2+p_3+p_4
&=\\sigma\\bigl(\\alpha_1+1-\\alpha_1\\bigr)
 +(1-\\sigma)\\bigl(\\alpha_2+1-\\alpha_2\\bigr)\\\\
&=\\sigma+(1-\\sigma)=1.
\\end{{aligned}}
\]
Thus the full square \\([0,1]^2\\) maps into the resource simplex. In particular, \\((\\alpha_1,\\alpha_2)=(1,1)\\) is valid and allocates the two stratum budgets entirely to their respective moderate classes; it is excluded by the triangular condition \\(\\alpha_1+\\alpha_2\\le1\\). Therefore that condition cannot express conservation of \\(C(t)\\) for the stated parametrization.

For the reported case-study values,
\[
0.6242+0.8157=1.4399>1,
\]
so the point is outside \\(U\\). Yet its complementary within-stratum fractions are \\(0.3758\\) and \\(0.1843\\), and for every \\(\\sigma\\in[0,1]\\) the resulting four physical shares still sum to one by the preceding identity. Hence the source's numerical policy and its declared feasible set cannot both describe the same controls.

Finally set \\(m_i=\\min_{{[0,1]}}R_i\\), which exists when \\(R_i\\) is continuous. Every point in the square obeys \\(\\max\\{R_1,R_2\\}\\ge\\max\\{m_1,m_2\\}\\). Choosing independently minimizing coordinates attains equality. This proves the square-domain minimax formula.

## Verification
The accompanying `verifier.py` uses exact rational arithmetic for the printed four-decimal case-study values. It checks that \\(0.6242+0.8157=1.4399\\), checks both complementary pairs, and substitutes both possible orientations of the reported top-level ratio \\(0.4479:0.5521\\) into the four-share map. In each orientation all shares are nonnegative and their exact sum is one. Running the file with the Python standard library prints `VERIFY_OK`.

The universal resource identity and the minimax identity are algebraic proofs above; no finite computation is used as a substitute for either argument.

## Relationship to prior work
The motivating article explicitly defines the four nested allocation fractions, then later declares \\(U=\\{{(\\alpha_1,\\alpha_2):0\\le\\alpha_i\\le1,\\ \\alpha_1+\\alpha_2\\le1\\}}\\), and reduces its instantaneous optimization to the boundary \\(\\alpha_2=1-\\alpha_1\\). Its Wuhan case study subsequently reports \\(0.6242:0.3758\\) and \\(0.8157:0.1843\\) as the two within-stratum splits. Those statements supply the direct comparison needed for this correction.

Broader epidemic-resource-allocation literature, such as Zaric and Brandeau's short-horizon framework, treats explicit resource budgets and intervention production functions, but it does not contain this paper-specific nested parametrization and therefore does not imply the square-domain correction. Searches by exact title, DOI, feasible-set language, and the distinctive numerical pair located the source itself and general allocation literature, but no published correction of this specific inconsistency was located.

## Limitations
The correction is structural, not a re-estimation of the Wuhan data. It does not determine how \\(\\sigma\\) should be chosen if that top-level share is made endogenous, nor does it validate the source's reported numerical optimum under a fully re-specified three-control problem. The source could in principle intend \\(\\alpha_1,\\alpha_2\\) in Eqs. (18)–(20) to denote different top-level resource shares, but that interpretation is incompatible with the immediately preceding formulas where the same coordinates control within-stratum moderate/severe splits and with the case-study ratios reported for those splits.

## References
1. M. Zhuang, J. Zhu, X. Lu, D. Cheng, X. Tan, “Dynamic Allocation of Emergency Medical Resources in Respiratory Infectious Disease Models Considering Vaccine Failure,” *Mathematics* 14(3), 425 (2026). DOI: 10.3390/math14030425. Published 2026-01-26.
2. G. S. Zaric, M. L. Brandeau, “Resource allocation for epidemic control over short time horizons,” *Mathematical Biosciences* 171(1), 33–58 (2001). DOI: 10.1016/S0025-5564(01)00050-5.

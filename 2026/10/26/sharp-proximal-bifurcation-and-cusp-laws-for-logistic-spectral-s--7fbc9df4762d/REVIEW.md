# Independent mathematical audit

## correctness

PASS

PASS: The logistic derivative h_a' =p+at p(1-p) is strictly positive. Its second derivative is a p(1-p)[2-at tanh(a(t-1)/2)], so the unique t0>1 is the nondegenerate global slope maximum L>1 (and H=-h_a'''(t0)>0). The stationary-input curve S_beta(t)=beta t+(1-beta)h_a(t) is strictly increasing at and below beta_c=L/(L-1), even though its derivative touches zero at beta_c. Above beta_c it has precisely two turning points. The outer global-minimum energy difference differentiates as u_l-u_r<0 and has opposite strict signs at the folds, proving exactly one Maxwell equal-depth datum for every beta>beta_c. A cubic Taylor expansion at the critical point gives the signed |s-sc|^(1/3) modulus; rescaling t-t0=√epsilon x gives the fold-width coefficient (4/3)(L-1)q, the two-minimizer jump 2√3 Lq and Maxwell-location little-o epsilon^(3/2). Independently reimplemented differentiation and numerical Maxwell root checks support the constants, but not the universal assertion. The finite input s=0 is treated by the positive objective and derivative boundary; beta=beta_c is included.

## originality

PASS

PASS (qualified): Yang–Wang–Yang prove an exact weak-convexity bound and sufficient strict inequality beta(1-1/L)<1. The asserted endpoint, unique supercritical global coexistence and exact cusp/fold coefficients require analysis beyond that sufficient condition. Lu and collaborators provide generic scalar singular-value reduction, and generic cusp theory supplies qualitative exponents, not the family-specific Maxwell location and constants. Resultary semantic search found related proximal works but no statement covering the full theorem. Original primary arXiv full text was unavailable in this execution; priority is best-of-knowledge only.

## value

PASS

PASS: A sharp global uniqueness threshold including its equality endpoint, unique supercritical datum with two global minimizers, and quantitative onset constants are directly relevant to the nonconvex logistic spectral penalty. This is not merely a restated weak-convexity sufficient condition or a stationary-root count.

The dated certificate retains the supplied scientific assessment, sources and limitations.

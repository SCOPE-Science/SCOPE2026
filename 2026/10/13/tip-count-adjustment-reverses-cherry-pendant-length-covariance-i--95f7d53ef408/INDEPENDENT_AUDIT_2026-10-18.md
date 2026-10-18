# Independent mathematical audit

## correctness

PASS

PASS: For dimensionless τ=λt, L=λP, N tip count, C cherry count, H summed ages of cherry-member leaves, J summed squared leaf ages, explicitly re-derived eleven expected-value generator ODEs including EC L: (ECL)'=ENC+ENL−3ECL−EL+EH with initial N(0)=1, C=L=H=J=0. An INDEPENDENT SymPy program verified all eleven stated closed forms satisfy exact differential equations and initial conditions with zero residual, then recomputed Cov(C,L)=F/(36r^3), Cov(C−N/3,L−N/2)=−g/(36r^3) and both residual variances. Here g=r^4−6r^2+24r log r−4r+9; g(1)=0, g'(r)=4(r^3−3r+6log r+5)>0 for r≥1. For F=6r^5−19r^4+18r^3+12r^2−24rlog r−8r−9, F(1)=F'(1)=F''(1)=0, F'''(1)=36>0 and F''''(r)=720r−456−48/r^3>0 for r≥1. Hence strict signs hold for every λt>0, not only sampled time points. Large-r leading variance and covariance yield correlation limit −sqrt(6)/12. P restored by λ−1. Initial single-lineage pendant-age convention is material; fixed-tip conditioning and extinction are explicitly not claimed.

## originality

PASS

PASS best-of-knowledge: canonical Yule tree cherry count and expected pendant-edge length were studied in separate earlier works. Their individual mean/variance formulas do not logically determine cross covariance E[CP] or the residual dependence with shared N removed. The inspected Steel–Mooers pendant expectation paper, McKenzie–Steel cherry source information, and Choi–Kaur–Wu cherries/pitchforks source address marginal branch lengths or topological counts, not the exact mixed age/cherry moment for the one-lineage model. Resultary and directed literature queries found no stronger statement yielding these formulas, but an older branching-process mixed moment under a different normalization could still exist.

## value

PASS

PASS: It quantifies the relationship between an important tree-shape statistic (number of cherries) and an important continuous branch-length statistic. The rigorous all-time sign reversal between raw covariance and canonical N-adjusted residual covariance demonstrates a real model-level Simpson-type effect and supplies exact quantitative limiting correlation. It is not a generic tautology about residuals: the nonzero mixed moment and sharp sign require a coupled generator computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

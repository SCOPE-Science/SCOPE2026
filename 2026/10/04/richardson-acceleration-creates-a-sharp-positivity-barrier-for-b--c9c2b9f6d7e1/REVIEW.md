# Independent mathematical audit

## correctness

PASS

For every integer r>=2, the frozen RESULT.md constructs B_1=(1+z)^-1, B_r=(1+z/r)^-r, and R_r=(r B_r-B_1)/(r-1). Expansion gives order two; F_r=(1+z/r)^r/(1+z) has (log F_r)'=((r-1)z)/((r+z)(1+z))>0 on z>0, F_r(0)=1<r and F_r→infinity, so precisely one sign transition. Direct rational R_2 simplification gives z_2=2+2sqrt2. Root bound log r<z_r<2 log r (large r) yields z_r=log r+log log r+o(1). Independent exact Fraction computations confirmed the R_2 algebra at 12 sample integers and bisection roots for r=2,3,4,5,8,16,32,64; finite checks are not the universal proof.

## originality

PASS

The original Constantinescu–Sandu paper constructs Aitken–Neville extrapolation from Euler substeps and studies linear stability, but its inspected Section 2, equations (2.1)–(2.6), do not give the nonnegativity threshold or log/loglog refinement asymptotics. Resultary query found the subject record and distinct BDF2/stagewise Richardson results, not an implication-equivalent positivity classification.

## value

PASS

A well-motivated and explicit obstruction to preserving positivity when accelerating a positivity-preserving stiff integrator; the complete sign interval for all r and logarithmic refinement scaling quantify a natural qualitative limitation beyond routine second-order calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

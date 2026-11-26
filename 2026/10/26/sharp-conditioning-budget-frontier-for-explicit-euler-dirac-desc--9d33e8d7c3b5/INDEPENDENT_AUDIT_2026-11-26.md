# Independent mathematical audit

## correctness

PASS

Reconstructed all formulas. B1B2=0 makes im(B1ᵀ) and im(B2) orthogonal; after similarity by P_r^{1/2}, the nonzero singular modes give two-by-two blocks with a=1−νh on the diagonal and off-diagonal magnitudes b=hσγ0√r, c=hσγ1/√r. Trace and determinant give the larger singular value (b+c)/2+sqrt(a²+(b−c)²/4). It increases with σ and dominates the kernel norm, so σ=s yields (1). Its right derivative at h=0 is C_r−ν; convexity precludes contraction when this is nonnegative. Otherwise squaring the contraction inequality yields (2), with the proposed endpoint below 1/C_r by (ν−C_r)²+D_r²>0. With Q=ν²+D_r², set x=Qh−ν; stationarity gives x=−C_rD_r/sqrt(Q−C_r²), on the correct branch, and substitution gives (3). The symmetric case D_r=0 has the unique kink minimizer 1/ν. For every h>0 the norm is strictly increasing with C_r at fixed p, so minimizing the scalar function γ0√r+γ1/√r on the exact condition-budget interval gives the unique clip rule. Solving the quadratic in K^{1/4} gives the strict root threshold before symmetrization, including equality at the Euclidean boundary. The eigenvalue endpoints 1−h(ν±p) establish Schur stability independently, and similarity yields the √K transient bound. The triangle calculations give the stated threshold 256/9 and optimum constants at budget 81.

## originality

PASS

The fully symmetrizing metric and continuous-time geometric- versus arithmetic-mean criteria are prior. The compared related condition-budget theorems concern different continuous-time operators. The distinct supported statement is the exact finite-step contraction and optimization frontier within the specified degree family, including budgets below complete symmetrization.

## value

PASS

The frontier quantifies the practically and mathematically distinct regimes of spectral stability, Euclidean one-step contraction, and contraction achieved by a limited metric distortion. It supplies an exact budget and step rule instead of merely exhibiting a fully symmetrizing metric; the triangle has a genuine nonempty gap between the budget for any contraction and that for full symmetrization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

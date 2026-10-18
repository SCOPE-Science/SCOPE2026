# Independent mathematical audit

## correctness

PASS

For the exact three-variable Beverton–Holt/Nicholson–Bailey map with r=26,a=1/10,b=3/10, a positive fixed point must satisfy φ(x)=x/(e^x−1)=a h, ψ(y)=y/(1−e^-y)=b h and r=e^x(h+e^y). Strict decrease of φ and increase of ψ parameterize a unique positive (x,y) over 10/3<h<10, reducing existence to continuous scalar F(h)=26. Rational interval sign certificates in the supplied verifier show F(4.9)>26>F(5) and F(9)<26<F(9.5); independently reconstructed roots h=4.98708531279478 and h=9.35663868823336. Direct symbolic differentiation of the ORIGINAL full map, after imposing equilibrium equations, matches the submitted full Jacobian J. Independent high-precision eigenvalues of the first J have moduli <1 (complex 0.248146±0.911481i; real 0.953657) and second J has real eigenvalue 1.01023065>1. The supplied standard-library rational interval code verifies strict Jury signs/negative det(I−J), upgrading numerical corroboration to certified inequalities. Nonzero det(I−J) at both points yields smooth continuation and persistence of the strict stability split near the parameter triple via implicit-function theorem. Claim properly says at least two, not exactly two, and no bistability.

## originality

PASS

Seno–Goyal (2026) Eq.(27)/Appendix I derives necessary conditions and qualitative native/boundary predator invasion, but does not supply two distinct strictly positive coexistence fixed points at one parameter triple or their opposing spectra. A related published SCOPE result about oscillatory invasion advantages studies transverse Lyapunov exponents, not multiplicity of this map’s positive fixed points. Statement-level comparison and Resultary searches did not expose full coverage. Seno–Goyal Lemma 6 only gives necessary ordering R_A>R_J>1, satisfied here.

## value

PASS

The existence of multiple full positive equilibria with one attracting and one unstable branch is a meaningful structural/bifurcation feature for a biologically motivated three-species discrete-time model, beyond boundary-state invasion conditions. Rigorous rational inequalities avoid unreliable phase-portrait guesses and show an open parameter region, while honestly not claiming global bistability or an exact total count.

The dated certificate retains the supplied scientific assessment, sources and limitations.

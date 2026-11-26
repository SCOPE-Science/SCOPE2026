# Independent mathematical audit

## correctness

PASS

Detailed balance is xp(x,y)=yp(y,x); multiplication by sqrt(x) conjugates to the symmetric Lebesgue kernel e^(-x-y) I_1(2 sqrt(xy)). Its series is a sum of positive rank-one terms e^(-x)x^(k+1/2) tensor itself, divided by k!(k+1)!. Their summed trace is the finite diagonal integral T_s, so the expansion converges in trace norm. A vector annihilated by the operator has all moments zero against e^(-x)sqrt(x); polynomial density on [0,s] gives injectivity. Thus zero is in the spectrum but is not an eigenvalue, and the positive eigenvalues accumulate only there. For ordered positive nodes, each generalized Vandermonde in the Cauchy–Binet expansion has positive sign: it cannot vanish by Descartes' rule (m monomials have at most m-1 positive roots), and its sign on the connected ordered chamber can be tested at nodes x_i=t^(i-1), t>1, where it is an ordinary positive Vandermonde in t^(k_j). The fixed consecutive-exponent term then bounds every sufficiently long partial-sum minor away from zero for the given nodes. The nonsymmetric p differs by positive row/column multipliers. In the Poisson(x)–Gamma(k+2,1) representation, row mass on (0,s) is at most the Gamma(2,1) mass q_s. Detailed balance yields the same bound for the adjoint row relative to the reversible measure, and the two-sided Schur inequality gives the norm estimate. The determinant product converges by trace summability; the spectral norm bound locates all zeros at or left of -1/q_s, with no zeros for any real physical bias. Spectral calculus and the geometric-series bound give the stated inverse and remainder estimates. The forcing is bounded on the compact interval with the stated boundary extension. Finally the large-x diagonal asymptotic 1/sqrt(4 pi x) with integrable error away from zero gives T_s=sqrt(s/pi)+O(1). The compression restricts the endpoints of one auxiliary transition, not a diffusion killed upon its first interior-time exit.

## originality

PASS

The SEP kernel and equation are already known, and the weighted positive trace-class realization, injectivity and qualitative pole exclusion substantially overlap a distinct same-operator record. Strict positivity of these diffusion minors fits classical one-dimensional noncollision determinant theory; it is not credited here as a general new total-positivity principle. The distinct quantitative contribution in the frozen finding is the explicit all-finite-s q_s contraction with its norm-conditioned inverse and truncation guarantees, sharpening the verified alternative elementary contraction, together with an explicit growing-trace law for this realization. Neither the stated q_s bound nor its uniform-in-bias finite-s estimates were found in the inspected strongest comparisons; no priority inference is made from catalogue dates.

## value

PASS

At a prescribed finite time the bound can be evaluated without eigenvalue computation and guarantees a concrete operator-norm error after truncating the physical negative-bias inverse series, including at omega=-1. The gain over the alternative 1-e^(-s) Schur bound changes the small-s contraction scale from s to s² and improves the explicit finite-s denominator even away from that asymptotic regime. The bound is not claimed sharp for large s. The growth of the entire trace is distinct from tracking only the nearest pole.

The dated certificate retains the supplied scientific assessment, sources and limitations.

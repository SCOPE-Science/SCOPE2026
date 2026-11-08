# Independent mathematical audit

## correctness

PASS

For each fixed nonnegative integer L the complex spherical band separates into abs(m) weighted polynomial blocks of dimension L-m+1 with (1-x^2)^m measure. Restriction to [-epsilon,epsilon] is an exact positive Gram operator. Exterior Cauchy–Binet with jet vectors gives e_{j+1}=epsilon^{(j+1)^2} det(A_j)det(U_j)(1+O_L(epsilon^2)); Taylor parity excludes order-one relative correction. Ratios of the ordered eigenvalue products give epsilon^{2j+1} times h_j D_{m,j,L}. The uniform moment quotient is the monic Legendre norm 2/(2j+1)(2^j/binom(2j,j))^2 and the jet quotient the squared endpoint Christoffel norm of y^{j-1/2}(1-y)^m Jacobi polynomials. Coefficients D are positive, and the (m,j)=(0,L) sector alone has exponent 2L+1 and coefficient (2^L/binom(2L,L))^2. Largest eigenvalue 2(max_m D_{m,0,L})epsilon gives sharp condition constant; remaining power multiplicities 2(L-j)+1. The L=0 case exactly lambda=epsilon. Direct independently written 85-digit weighted moment generalized-eigenspectrum tests at eps 0.08/0.04 for all m at L<=5 found the expected odd powers and coefficients (maximum relative finite-width discrepancy at eps=0.04 under 0.006893); an independent exact rational moment inversion checked 120 (L,m,j) for L<=7. Finite tests supplement, not replace, the arbitrary-fixed-L determinant proof.

## originality

PASS

Best-of-knowledge, explicitly qualified: literature establishes spherical concentration operators, finite equatorial-belt matrices and Slepian methods, but in materially inspected relevant texts no theorem directly states the all-fixed-degree odd-power eigenvalue hierarchy with exact Jacobi endpoint constants, uniquely weakest mode and sharp global conditioning. Gilbert–Slepian 1977 full text was inaccessible and could overlap via equivalent polynomial concentration; its abstract discusses a different large-degree regime. Negative searches are not novelty proofs.

## value

PASS

Thin latitude-strip observation is a natural spherical-harmonic partial-data and geophysical inverse problem. The complete fixed-L hierarchy identifies how many modes lose epsilon, epsilon^3,...,epsilon^(2L+1) energy, provides positive explicit Jacobi coefficients, the unique least observable direction, and the sharp noise amplification/conditioning exponent with constant. Such quantitative stability data are needed to calibrate regularization and are not a routine one-line application of the known finite-aperture matrix or a small arbitrary slice. Claim is bounded to fixed L; no significance from claimed large-L uniformity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

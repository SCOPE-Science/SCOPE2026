# Independent mathematical audit

## correctness

PASS

With u=πr², area is du dθ/(2π); the Hermite STFT phases make the disk operator diagonal and the first three integrals equal 1−5e^(−2). For the tail recurrence put A=Q_(m−1), B=Q_m; then A−A'=B and mA−(m−2)B=uB'. These make (1−d/du) of the claimed polynomial increment exactly the difference of the densities with the exponential removed. At u=2 the factors Q_j(2)=(j−1)(j−4) give P_3=P_4=P_5=17/3 and strictly larger tails thereafter, so the complementary gap is (2/3)e^(−2). The annular integral of smooth rank-one projectors admits the stated trace-norm expansion. The h1 boundary STFT is zero, the other amplitudes have angular orders two apart, and the diagonal integrations vanish by zero mean. Thus the compressed eigenvalues are 0 and ±c, where c=√2 e^(−2)|bhat(2)|. The eigenvalue lower bound uses the appropriate extremal vector in the top space; the upper bound uses the fixed gap to absorb the O(|ε|) coupling to the complement with an O(ε²) loss by completing a square. The ellipse is exactly area preserving and b=2 cos(2θ). The result concerns smooth local exact-area perturbations only; if bhat(2)=0, no linear gain is inferred. Independent replay: python /workspace/branches/independent_checks.py 3 (formal polynomial expansion in m and direct Gaussian generating-function STFT coefficients through m=6). The source checker reports finite symbolic tests, not a separate certification.

## originality

PASS

Pass for the sharp first-order fixed-h2 shape law, including local equal-area ellipse improvement. The disk triple and gap overlap exactly with Resultary a2df20aeb429 and are supporting spectral data, not a distinct contribution on their own. That distinct catalogue record is dated later; the date does not resolve priority. Its inspected disk spectrum does not give the off-diagonal boundary coupling or the sharp angular selection rule. No equivalent shape law was established by the comparisons below.

## value

PASS

The theorem pinpoints a limit of Gaussian disk optimality for a natural non-Gaussian window: an exactly area-preserving ellipse already improves the norm linearly. The selection rule gives the sharp magnitude and identifies the only boundary Fourier mode that can improve the norm to first order, information unavailable from a disk-spectrum table or a numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.

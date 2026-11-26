# Independent mathematical audit

## correctness

PASS

Right multiplication by the adjoint of the unperturbed unitary matrix leaves two modified rows over an identity block. The upper-left matrix has diagonal a and off-diagonal b, and the full two-row Gram block has diagonal 1 and off-diagonal c. Subtracting the upper-left Gram gives the two row norms squared γ_s=1+sc−(a+sb)² in the parity basis; the projected rows are orthogonal. Consequently there are N−4 unit modes and two 2×2 Gram blocks of trace 2+sc and determinant (a+sb)². In fact each γ_s is positive in the named regime: reflection interchanges retained sites j=2 and j=N−1, where the first modified cardinal row has two negative, unequal entries proportional to −1/sin((2h−δ)/2) and −1/sin((h+δ)/2), respectively. Their parity sum and difference are both nonzero. The roots are positive since a>b>0, and each parity block straddles 1. At collision c=1+O_N(η²), a+b=2d_N+O_N(η²), and the odd difference is −hD'_n(h/2)η/N+O_N(η³)=K_Nη+O_N(η³). The odd large root tends to 1, so dividing the odd determinant by it gives the square of the least singular value. The even top is separated and varies by O_N(η²), yielding the stated condition-number coefficient and remainder. The even collision roots are strictly positive with a nonzero gap, since N sin(π/(2N)) increases with N and is already √2 at N=2. The limit N→∞ of the fixed-N coefficients uses sinc at zero; this is not a uniform joint-limit claim.

## originality

PASS

Earlier inspected work supplies unperturbed circulant spectra, perturbation bounds, and the inverse-separation conditioning exponent. It does not mechanically give the full parity-resolved spectrum and the sharp largest-to-smallest singular-value coefficient for this square, symmetrically perturbed grid. The strongest local catalog hit uses the identical configuration and gives exactly the least-singular-value leading coefficient after reparametrization; it is a distinct, later-dated quadrature record, and does not supply the two quadratics, sharp condition coefficient, or the odd cubic remainder. Credit here is for the complete spectrum and sharp conditioning calculation, not for the exponent or for an exclusive claim to the least-singular-value leading term.

## value

PASS

The square complete-band Fourier grid is a natural interpolation benchmark. Its symmetric pair collision admits an exact answer beyond the known conditioning scale: the four changing modes are resolved, their positivity is explicit, and the sharp numerical blowup coefficient and fixed-size error follow. The distinction between the least singular value and the condition number matters because the top singular value has a non-unit limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.

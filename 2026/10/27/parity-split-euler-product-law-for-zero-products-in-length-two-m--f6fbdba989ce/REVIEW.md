# Independent mathematical audit

## correctness

PASS

For any fixed residue matrix of rank a, invertible residue row and column operations lift and reduce it to diag(I_a,0) modulo pi. The upper and off-diagonal blocks contribute 2na−a² freely lifted entries. The lower Schur block ranges over the full pi layer; multiplication by pi identifies this layer with F_q, including for nonsplit rings, because Ann(pi)=(pi). Counting its rank b yields the stated one-matrix factor. Each of the n columns of Y is free in a kernel of size q^(b+2c); this weights the law of X under joint uniformity on solution pairs. Substituting the rank counts gives exponent (5n²−h²−b²)/2 and factor Phi_n²/(Phi_a Phi_b Phi_c²). Extend the weights by zero off the finite feasible set; feasibility is h+b≡n mod 2 with nonnegative a=(n+h−b)/2 and c=(n−h−b)/2. Along each parity the factors converge to 1/(Phi_infinity Phi_b) and a summable Gaussian envelope bounds the weights, giving l1 convergence and then TV after normalization. The even/odd projector splits the mass into products of one Euler series and one Jacobi series, producing (P_+³±P_-³)/2. Both limiting masses are positive and differ since P_->0. The unconditional probability divides by q^(4n²); n=0 gives one empty pair. Independent checks (not uploaded code) gave 2464 for q=2,n=2 over both ring types by direct pair multiplication, 123201 for q=3,n=2 via kernels, and 0.6898119280685257 for the claimed even q=2 mass. Replay: /workspace/branches/4f8cb107-fcc5-4bcf-b791-85c8c3b28f55/independent_check.py and independent_check.txt; proof replay in frozen RESULT.md equations (1), (6)–(9).

## originality

PASS

The supported distinct content is the fixed-q parity-dependent Euler-product constants and the total-variation two-parameter Smith law for the first factor of a jointly uniform zero-product pair over a length-two ring. The individual-matrix type count is prior background, and multiplying it by the independent-column kernel factor is elementary; neither is credited as the asymptotic contribution. The closest inspected field-pair and length-two-ring results do not give the target torsion law or its cubed products. Dolžan's potentially relevant full text could not be verified; this is a residual priority risk, not evidence that it does or does not cover the theorem.

## value

PASS

The exact leading constants distinguish even and odd dimensions in a natural zero-product probability, beyond giving its exponential order. The TV law quantifies the nonvanishing torsion stratum and the jointly tight fluctuations around the balanced Smith profile. The constants and limit agree across split and nonsplit rings with the same residue field. These are structural distributional conclusions, not merely verification of the small totals or of standard individual-matrix counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.

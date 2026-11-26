# Independent mathematical audit

## correctness

PASS

Both inverse branches cover the box with Jacobian magnitude 1/2. Averaging their action on centered coordinates gives the stated row-coefficient matrix, and the diagonal stationary coordinate covariance then gives C_ij(n)=v_j(B_M^n)_ij, with v_1=1/3 and v_j=1/12 otherwise. The characteristic determinant has just the diagonal and signed cyclic permutations. A first-coordinate walk either stays at coordinate 1 or makes a full circuit of weight -2^{-(M+1)}, possibly with half-weight self-loops at intervening coordinates; this gives an independent renewal derivation of the stated resolvent and verifies the first negative lag M. The denominator's value at z=2 is 1/2, excluding cancellation, so the nonzero roots determine the limsup by the radius of convergence. Odd M can give a zero root, harmless for the radius; the positive trace supplies a nonzero root. Roots have modulus less than 1 by the characteristic equation. In the repaired theorem (/workspace/repairs/4/RESULT.md), set h=1/M and 2lambda-1=exp(hw). At h=0 the root w=-log(3)+i*pi is simple, with derivative -1; analytic continuation and conjugation give the displayed pair and hence rho_M>=1-log(3)/(2M)-O(M^-2). For a root of maximal modulus the lower bound implies |4lambda-1|>=4rho_M-1>=3-L/M. The characteristic equation gives |2lambda-1|=|4lambda-1|^(-1/(M-1)), so rho_M<=(1+(3-L/M)^(-1/(M-1)))/2=1-log(3)/(2M)+O(M^-2). This verifies the sharper repaired claim without assuming the exhibited pair are maximizers. The frozen inverse-word and finite resolvent checker was inspected; its finite checks do not prove the large-M asymptotic.

## originality

PASS

PASS applies to the repaired sharp large-M rate, not to the frozen broad presentation of the affine transfer and resolvent as distinct. Record 765a4f4ba4c8 gives exactly that transfer matrix, resolvent, characteristic polynomial, stability and noncancellation. The repair credits the overlap, drops the entrywise and first-sign formulas as distinct claims, and retains the surviving quantitative near-unit analysis, strengthened by a verified matching upper bound on the maximal modulus. This is an assessment of actual coverage, not historical priority based on path dates.

## value

PASS

The repaired theorem quantifies a nonuniformity that qualitative Bernoulli mixing cannot explain. It gives the sharp first-order scale and constant for the actual slowest first-coordinate stationary covariance rate, not just a single root, on the natural sequence of all ambient dimensions. This is a useful exact benchmark for geometric correlation in an established system.

The dated certificate retains the supplied scientific assessment, sources and limitations.

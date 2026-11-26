# Independent mathematical audit

## correctness

PASS

Split off the first spatial digit a and the lowest frequency digit d, so x=(2a+x')/b and lambda=(b/4)d+b lambda'. Multiplication in the exponent separates as phase (-1)^(ad), the diagonal spatial phase D=diag(exp(pi i x'/2)) when d=1, the shorter matrix F, and a column phase C=diag(exp(4 pi i lambda')) when a=1. Thus the unnormalized blocks are (F,DF;FC,-DFC). For even b, C=I; subtracting the top block row from the bottom makes the latter right block -2DF. For odd b, flipping the leading spatial digit shifts x' by plus or minus 2/b, giving phase (-1)^(sum of the shorter frequency digits), exactly C. If P is that flip, FC=PF, so permuting the lower block row by P and subtracting the upper yields lower-right block -(D+PDP)F. Each diagonal entry of D+PDP has modulus 2 cos(pi/(2b)). Dividing by the row normalization cancels the factors of 2. From the normalized depth-one Hadamard matrix, the recurrence multiplies the squared determinant modulus of the preceding depth by 1 or cos(pi/(2b))^(2^(n-1)), yielding the stated exponent. The determinant is nonzero, det(A* A)=|det A|^2 and the minimum Gram eigenvalue is bounded by the geometric mean. In the even case, unit column norms and equality in Hadamard's inequality imply unitarity.

## originality

PASS

The supported distinctive result is the odd-base determinant for this finite atomic grid and the specified, generally noninteger frequencies. The even-base unitary endpoint uses a familiar Hadamard mechanism; for 4|b it also overlaps an exact integer-tower catalogue theorem. The strongest actual comparisons do not cover the odd-base formula or its finite Gram-volume rate. This is a bounded best-of-knowledge distinction, not a historical-priority or infinite-frame claim.

## value

PASS

Fourier interpolation motivates the natural basis-size digit design and its volume: it is isometric at all depths for even bases but invertible with declining per-mode Gram volume for odd bases. The exact finite rate shows that no depth-uniform lower singular-value bound holds for this design and gives a benchmark against nearby frequency towers. That is a nontrivial finite quantitative conclusion, rather than a restatement of the limiting no-frame theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

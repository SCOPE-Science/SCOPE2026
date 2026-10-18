# Independent mathematical audit

## correctness

PASS

Over F8=F2[X]/(X³+X+1) reconstruct S={(x,y):Tr(xy)=0} of size 36 and binary codeword (Tr(b),(a+Tr(bx+cy))_(x,y in S)) with a∈F2,b,c∈F8. Seven explicit generators have rank 7 and reproduce source ordinary weights 1+31z16+32z17+31z20+32z21+z36. Every r-subspace of message space F2^7 has a unique RREF basis; independent exhaustive enumeration of counts 127,2667,11811,11811,2667,127,1 (total 29211) computes each support by bitwise OR of corresponding words. All detailed histograms in RESULT.md and source artifacts/certificate.json reproduced, yielding generalized Hamming weights (16,24,28,32,34,36,37) and minimizers (31,75,15,45,10,37,1). Source code and certificate inspected, independent checker executed. It is a complete finite proof, not extrapolation.

## originality

PASS

Theorem 3.9 and Example 3.11 of Liu–Liu–Yu construct the exact binary [37,7,16] code, report the ordinary weights and dual distance, but not its 2–7-dimensional subcode supports. Pan et al give complete higher-support spectra for different families, with a ternary not binary length-37 example. Neither the source ordinary enumerator nor generic formulas supply this exact 29,211-subspace census without evaluating the trace-defined generator.

## value

PASS

The code is highlighted in its primary source for best-known parameters. Exact complete support distributions extend the ordinary enumerator to all-dimensional subcodes, revealing natural generalized weight minimizers and multiplicities useful for understanding support geometry and code comparison. The 29,211-case finite classification has an intrinsic object/invariant motivation independent of a large new family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For each binary basis a,b,c, summing the expansion of the seventh power over all eight coefficient choices cancels each term missing a basis variable. The remaining 1,2,4 assignments are precisely the Moore determinant, nonzero on independent triples. If distinct U,V share a two-space with basis a,b, choose remaining basis vectors c,d. The difference of witnesses is the determinant on a,b,c+d, which is nonzero since c+d is not in the common two-space. An independent exhaustive run generated all 39060 unordered independent triples and deduplicated to 1395 spaces, the Gaussian binomial count. It found 1395 determinant identities, nine fibers of 29 at z^9=1 and 54 of 21 elsewhere, and 15 distinct colors through each of 651 two-spaces. Scalar multiplication sends the color to lambda^7 times the color, with image H of order 9. The only nontrivial stabilizer can come from binary degree 3 (the degree of an element in the stabilizer divides 3 and 6), giving one F8-multiple orbit with one witness per element of H; other orbits contribute seven per element of their coset. Hence the confirmed census also gives four free orbits on H and three per other coset. Replay: python3 /workspace/branches/3c2c98c5-d2b9-4f72-a4d2-3577ec2831e1/independent_spectrum_check.py; replay.log records the full run. The original artifacts/verify.py and VERIFICATION.md were inspected, not executed; original expert, independent-audit and Lean fields say not_performed. This is an exact finite check for F64, not a general color-spectrum theorem.

## originality

PASS

Credit the sum-free witness, Moore identity, Grassmann coloring and code correspondence to prior work. The supported distinct claim is the exact 29/21 distribution, including which colors are heavy and the equivalent scalar-orbit allocation, for this previously motivated concrete coloring. Closest inspected work does not supply that distribution or an already proved formula specializing to it.

## value

PASS

The subspace-sum coloring is already motivated by sum-freedom and constant-dimension codes. Exact fiber sizes determine the size of every code in this concrete partition and expose a norm-one subfamily with an exceptional orbit; a researcher comparing determinant constructions would need this information rather than just the number of colors. The finite output is complete and not a claim to improve the chromatic bound or maximize any code size.

The dated certificate retains the supplied scientific assessment, sources and limitations.

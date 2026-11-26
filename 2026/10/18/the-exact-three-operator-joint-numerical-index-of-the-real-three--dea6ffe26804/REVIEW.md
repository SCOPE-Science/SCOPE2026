# Independent mathematical audit

## correctness

PASS

The tuple norm is the maximum over coordinate inputs by convexity. For a norming pair every supported coordinate has the dual coefficient equal to its sign, so a convex combination of signed coordinate inputs bounds the numerical radius; maximizing over the dual cube then gives sign vectors, each of which norms the corresponding signed coordinate input. Hence the claimed coordinate formula is exact. For the matrix bound with at most two norming sign classes, D^2<=2W^2. In the three-class case the four sign representatives with coordinate product +1 sum to zero, so three may be oriented to sum to the fourth. Their images obey the same sum and have Euclidean norm at most W. Adding the vector -y/6 times this relation in the dual evaluation gives the stated bound: the three shifted vectors have norms sqrt(1+24y_j^2)/6, whose sum is at most 9/6 for unit y; the remaining norm is 1/6. This yields 5W/3 for every real matrix, including zero. An independent integer check gave Gram matrix 9I, D^2=75 and sign-image squares 27 for all eight signs. Taking only the first source column nonzero realizes equality in the operator problem.

## originality

PASS

The strongest directly matching published record proves only strict separation from the complex value and explicitly leaves the real value undetermined. No checked result covers the sharp numerical value or its equivalent 3-by-3 inequality.

## value

PASS

This is the exact value of the smallest equal-dimension odd real case left open by the prior Fourier–Walsh result, quantifying the separation that previously was only qualitative. The matching integer witness and real sign-class argument make it a useful sharp benchmark, not an arbitrary finite check or a recomputation of the complex value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

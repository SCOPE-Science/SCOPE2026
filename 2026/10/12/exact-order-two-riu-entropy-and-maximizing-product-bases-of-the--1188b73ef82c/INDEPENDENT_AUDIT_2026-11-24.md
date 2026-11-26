# Independent mathematical audit

## correctness

PASS

An independent exact Pauli calculation from the six amplitudes checked normalization plus 12, 54, 108 and 81 components at orders one through four. They agree with the frozen tensors. Walsh Parseval for the product-projector expansion gives 16C=1+(S+3T+Q^2)/9. For the Gram identity, writing H for the sum of the four triangle products and R for the sum of the three four-cycle products, det G=1-S+2H+P-2R=0, T=4-2S+2H and Q^2=P+2R, giving the stated identity. For M=sum n_i n_i^T, trace M=4, trace M^2=4+2S and det M=T. Thus S+2T<=6 reduces to 2 product(lambda)<=sum_{i<j} lambda_i lambda_j. The rank-three case is strict since sum 1/lambda_i>=9/4>2; the rank-two case is strict from the one positive pair product. Equality requires rank one. With P<=3 this gives S+3T+Q^2<=15; at rank one, the unit axes are collinear and P=3, so the bound is attained. In particular the computational basis has six outcomes each of probability 1/6. This proves the claimed natural-log entropy and all equality cases up to outcome swaps (basis-vector phases do not affect projectors). The supplied exact-checker source was inspected, not executed; the continuous optimization is analytic, not from sampling.

## originality

PASS

The order-two value was previously reported numerically for the same state, not newly predicted here. The supported distinct contribution is a continuous-basis proof and the necessary-and-sufficient common-line equality condition. No equivalent proof or optimizer classification was found in the inspected closest literature or indexed Resultary matches.

## value

PASS

This turns a previously numerical fixed-state product-measurement optimum into a sharp theorem and determines every measurement attaining it. The rigidity is useful beyond the single entropy number: it separates relative-axis alignment from a coincidence at the computational basis and gives an exact benchmark for continuous local-basis optimization. It does not resolve the larger optimization over states.

The dated certificate retains the supplied scientific assessment, sources and limitations.

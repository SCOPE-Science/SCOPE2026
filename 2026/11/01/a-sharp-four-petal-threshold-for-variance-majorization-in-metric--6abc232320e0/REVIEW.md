# Independent mathematical audit

## correctness

PASS

Conditional on selecting the same petal of length l, shortest circular distance is uniform on [0,l/2]; across different petals the junction distances add independent uniforms. Independently summed the conditional first and second moments to obtain M1=(2S2-S3)/4 and M2=S3/6+S2^2/8-5S4/24, then V=M2-M1^2. Symbolic differentiation independently reproduced the variance pair-transfer coefficient QV=-5(a^2+ab+b^2)/6+(1/2+3M1/2)(a+b)+S2/2-2M1 and the three-petal polynomial 24QV=9s^3+27s^2t-17s^2-72st+9s+44t. On m=2,3 it is positive because its affine t minimum is at t=0 or t=s^2/4 and both endpoint polynomials are positive. For raw M2 the differential coefficient is ≥s(4-3s)/8>0 for all m. At (1/2,1/2,0,0) the variance transfer coefficient is -1/8, while at equal petals it is positive, proving neither Schur-convexity nor concavity for m≥4 by continuity. Independent Fraction arithmetic verified the exact positive four-petal majorization witness and variance difference -515428427/192000000000000, with both first and second raw moments increasing.

## originality

PASS

Baptista, Kennedy and Mugnolo, Mean Distance on Metric Graphs (2024), Example 4.3 and equation (4.3), establish the flower first moment and equal-length minimization, which are acknowledged as known; the article contains no variance theorem in its indexed full-text and inspected relevant sections. Garijo, Márquez and Silveira, Continuous mean distance of a weighted graph, studies the first moment rather than a second raw moment or variance majorization. Resultary searches for the four-petal variance threshold and bouquet second moments found no covering exact table. The unavailable original Doyle–Graver 1982 extended paper is a priority caveat, not an automatic rejection.

## value

PASS

Exact contrast between raw-second-moment and centered variance response to length balancing answers a natural geometry-of-networks question. A four-loop first-failure threshold with explicit rational witness is a motivated sharp topological boundary; it does not claim a global variance optimum for m≥4.

The dated certificate retains the supplied scientific assessment, sources and limitations.

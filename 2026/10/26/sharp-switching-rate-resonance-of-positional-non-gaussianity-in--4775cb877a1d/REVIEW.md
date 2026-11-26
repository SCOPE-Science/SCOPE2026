# Independent mathematical audit

## correctness

PASS

PASS for the repaired claim, not for the frozen wording. Frozen SLOGAN.txt says the raw moments always fall for two positive stiffnesses and otherwise Q decreases strictly below the contrast threshold. The frozen Finding also states strict decrease at or below the threshold without directly restricting that clause to unequal stiffnesses, and the proof's sign sentence likewise needs the nonzero factor (a−b)². Taking a=b makes the stationary law N(0,D/a) independent of k, so Q=0, M_2=D/a and M_4=3(D/a)² are all constant. The complete corrected RESULT.md, SLOGAN.txt and updated bibliographic METADATA.json are under /workspace/repairs/1/. In the repaired proof, the chain's stationary marginal is unique and the exponential past integral is conditionally Gaussian; finiteness of all moments and same-chain contraction give existence and uniqueness and justify the generator calculation. The diffusion parts at degrees two and four are 2D times the state mass and 12D times the corresponding second moment. Solving the two linear systems gives the displayed moments and rational Q. For a≠b both raw moment derivatives have strictly negative factors, while Q' has the sign of P(k). The derivative P' is strictly negative for k≥0; P(0)=4ab[(a+b)²−8ab] and P→−∞. Thus there is exactly one strict interior global maximum precisely above contrast 3+2√2; at equality of the contrast threshold the derivative vanishes at the continuous endpoint k=0, not inside the domain. Independently reproduced exactly with Python 3/SymPy: /workspace/branches/b41d6aad-c467-480d-8b3d-e61327d08f94/ordinal1_recheck.py. The frozen checker was inspected, not executed. The final repair also correctly states that conventional excess kurtosis is 3Q and shares the same monotonicity. The new prior identity with [4, Eq. (5)] was checked by exact rational simplification.

## originality

PASS

PASS only for the repaired, expressly forward-prior-covered result: the global derivative classification in the switching rate at fixed positive stiffnesses, including the unique optimum and strictly decreasing raw moments in the unequal model. The strongest positive prior-coverage finding is that the exact full forward Q already appears, in a different label, in Biroli et al. arXiv:2508.07199v2 Eq. (5). It is not an original component. Neither that equality nor the earlier distributional theorem is a statement about global monotonicity or optimizing the rate. The derivative factorization and single-root proof, not an algebraic parameter identification, establish the additional claim. The repair credits both forward sources explicitly and limits the claim accordingly.

## value

PASS

The repaired value is the physically motivated switching-rate classification, not recovering a known formula. For modest contrast faster switching reduces both raw moments and normalized departure from Gaussianity; at strong contrast it initially increases relative non-Gaussianity while suppressing both moments, and there is an exact unique best rate. This sharp distinction for all positive stiffness pairs is useful for selecting or interpreting moment diagnostics in a standard stochastic-trap model. It does not claim new forward statistics or that the optimum was experimentally resolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.

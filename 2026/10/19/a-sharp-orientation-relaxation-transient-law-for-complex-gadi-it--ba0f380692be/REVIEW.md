# Independent mathematical audit

## correctness

PASS

This pass applies to the complete corrected RESULT.md, not an unrestricted reading of the frozen relaxation paragraph. The frozen paragraph sets theta but does not reinstate q=1/2 after discussing other orientations, whereas its proof uses lambda tending to zero and the balanced norm coefficient. The relaxation assertion as stated for arbitrary fixed q fails: set alpha=1, beta=3, v=e1 and omega=0 in the two stages. They give H=diag(0,-1/2) for every t, so the first norm divided by t tends to 0 rather than 1/4 and the radius stays 1/2 rather than tending to 0. The repair explicitly fixes the balanced overlap in the relaxation finding and proof; the exact orientation formulas remain valid for all q. Subtracting the true fixed point and eliminating the half step yields G=theta I+(1-theta)C^{-1}DB with D=d e2 e2^T. Its rank-one trace and the product of its generating vector norms give the orientation laws. Their dependence on q(1-q) proves the strict opposite extrema in q, not uniqueness of a signed vector v. At balance, H^k=lambda^(k-1)H gives the unrelaxed stiff limits, and direct substitution gives the angular-window result. The repaired relaxed proof uses the two eigenvalues and the binomial coefficient p_k(lambda), with lambda tending to zero specifically at balance. The reverse-triangle bound and the uniform k r^(k-1) tail for fixed theta<1 justify the limit of the supremum, including theta=0. The ratio theta(k+1)/k certifies the leading index and integer ties. Independently reconstructing the two stage solves confirmed the examples: at alpha=1,beta=3,q=1/2,t=1000, ||H||/t≈0.250000375 and ||H²||≈0.125000125; at theta=3/4 the leading coefficient is 27/256, tied at k=3,4, not at finite t. Direct replay inputs are the two displayed stages with these values, or alpha=1,beta=3,v=e1,omega=0 for the scope counterexample. The frozen `verify.py` was inspected, not run. The repaired file retains and proves the fixed-t transformed contraction; no claim extends to joint theta approaching one or to higher-dimensional systems.

## originality

PASS

For the corrected planar family, the verified distinct results are the opposite exact overlap extrema for Euclidean one-step norm and spectral radius, the tuned angular window and stiff power limits, and their exact balanced relaxation peak across all iteration counts. The GADI/HSS relation, convergence, and the generic k theta^(k-1) Jordan mechanism are not novel. The strongest materially related indexed finding was compared at the statement level and uses a different iteration; no implication-equivalent special case for GADI was found in the inspected passages. This is not an exhaustive priority claim.

## value

PASS

The corrected claim quantifies a meaningful conflict for a natural family of an existing solver: the overlap minimizing the spectral radius maximizes the first Euclidean step, and relaxation spreads the stiff amplification over a precisely predicted iteration horizon. The derived coefficient is useful beyond the generic Jordan explanation because it fixes the size and leading peak for these solver parameters. Balance is a mathematical condition, not a post hoc performance disclaimer; the result preserves the weighted-norm contraction and makes no unsupported numerical-stability or convergence failure claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

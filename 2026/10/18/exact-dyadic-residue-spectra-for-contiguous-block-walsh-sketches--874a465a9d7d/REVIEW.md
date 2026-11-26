# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 46–61. The product of two Walsh entries evaluated at row k*tau+u factors into the character on k of v_a XOR v_b and the character on u of w_a XOR w_b. The full u sum is tau precisely for equal residues and zero otherwise, while K*tau/N=1. Each residue block is a sum of q rank-one outer products with diagonal entries one; distinct residues therefore always give the identity, while any repeated residue fails on the sample sequence that repeats one block. Counting supports by choosing residues and then high labels gives binom(tau,m)K^m, and tau*m entries of squared size 1/N give the same leverage mass m/K in every block. For a distinct-column equal-residue pair the high-bit character is nonzero and hence balanced. Independent draws with replacement give fair independent signs; their mean controls the eigenvalues, and rank loss is precisely two unanimous sign sequences. The result holds for any fixed signature because it conjugates the Gram. Independent bounded replay: with d=3,s=1 and positive signs, enumerate all triples from {0,1,2,3}; for each pair use the exact numerator sum of (-1)^popcount((k*tau+u) & (a XOR b)) over both u and all three sampled k and divide by 6. Pair {0,2} has 48 defects of 1/3 and 16 of 1, while {0,1} has 64 defects of zero. This checks one geometry including repeated draws, not the all-dimension result. Frozen check.py and VERIFICATION.md inspected, not executed.

## originality

PASS

Credit the exact universal-isometry classification and residue-dependent law for the specified global block-SRHT model, not classical character orthogonality, a new SRHT construction, or a new general OSE bound.

## value

PASS

Contiguous equal-size blocks are a natural lawful partition of the published sketch. The exact same-mass comparison identifies which coordinate supports are isometric on every draw, and which pairs have positive and exactly quantified rank-loss probability even with perfectly flat block masses. This is a usable structural diagnostic for a specific sketch, not just a normalization check or a claim that a sufficient high-probability embedding theorem fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.

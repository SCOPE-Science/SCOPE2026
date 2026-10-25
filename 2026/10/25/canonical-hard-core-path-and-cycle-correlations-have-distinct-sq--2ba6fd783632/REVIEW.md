# Scientific review: fixed-particle hard-core correlations

## Correctness (C): PASS

The path count \(\binom{n-k+1}{k}\), the forced-site counts \(\binom{N-1}{k-1}\), \(\binom{N-2}{k-2}\), and \(\binom{N-3}{k-1}\) determine the exact path covariance. On a cycle the total count \(n\binom{n-k}{k}/(n-k)\), cyclic symmetry, and the two-site count \(\binom{n-k-2}{k-2}\) determine the second formula. Denominators are positive on the full stated domain, including maximum packings, and their numerators give precisely the claimed zeros and signs. Conditional independence after fixing the middle site vacant establishes strict positive grand-canonical covariance on a path at any finite positive activity. The square-root statement follows directly from the exact formulas. `verify.py` checked 1305 exact-rational assertions and 139038 canonical samples. Finite checks supplement, rather than replace, the proofs.

## Originality (O): PASS on compared material; residual historical uncertainty

The closest examined full text, Davies and Perkins (arXiv:2102.04984v1), treats the fixed-size independent-set measure and obtains complexity and approximate-sampling theorems for general bounded-degree graphs, not the two-site covariance sign identities. Blanca and collaborators (arXiv:1611.01115v1, published primary MSC 60C05) analyze phase coexistence on the infinite two-dimensional lattice, rather than finite fixed-cardinality path/cycle pair correlations. Joseph and Roby's path-independent-set paper considers toggle dynamics and homomesy, rather than occupation covariances. Searches of published mathematical records for hard-core path/cycle, canonical occupancies, critical particle density, independence and pair correlations returned no equivalent assertion. The exact binomial enumerators are elementary and could have been used implicitly in older one-dimensional lattice-gas work; priority is not independently certified. A generic counting identity without these cross-ensemble and boundary-sign conclusions does not by itself state the signed phase classification, although it may imply it by specialization and algebra, so this remains a residual comparison risk.

## Value (V): PASS

This is a complete exact classification of the dependence sign for the *first allowed separation* in canonical one-dimensional hard-core laws, including sharp zero-covariance families, a shared mesoscopic \(\sqrt n\) scale, and a nonzero gap between the open-chain and periodic thresholds. Fixing the occupation total can reverse the sign seen at every fugacity in the corresponding path grand-canonical ensemble. These are finite-size physical/statistical features that ordinary counts of independent sets do not directly convey and are natural for understanding canonical and grand-canonical discrepancies.

## Limitations

The theorem is not a general multivertex covariance classification. It gives no infinite-volume uniqueness result. Numerical enumeration covers a finite range only; the analytical binomial proof is essential. The possibility of older implicit exact one-dimensional correlation formulas is not eliminated by search, and an independent mathematical and priority audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.

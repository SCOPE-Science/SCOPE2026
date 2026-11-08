# Independent mathematical audit

## correctness

PASS

A permutation with exactly n-2 fixed points is one transposition: its span d=b-a removes exactly d records, hence w_n(r,n-2)=r. Exactly n-3 fixed points entails one three-cycle; counting the two orientations by their outer span gives w_n(r,n-3)=(2r-1)n-2r^2. Algebraic cancellation yields adjacent minor 2r(r+1)-n; r=1 makes 4-n<0 for all n>=5. Full TP2 for n=2,3,4 is established by complete exact joint matrices and all minors. For the covariance identity, condition record I_i on each fixed-point J_j: j<i contributes 1/(i-1), j=i contributes 1/binom(n-1,i-1), and j>i contributes 1/i, causing cancellation and giving positive (1/n)sum_{j=1}^{n-1}binom(n-1,j)^-1. Independently enumerated all n! permutations for n=2..8 and tested the covariance and near-identity cells exactly.

## originality

PASS

Bounded best-of-knowledge scientific comparison: Master-polynomial specialization could derive w_n, but no directly inspected theorem concludes all-n 2r(r+1)-n, sharp TP2 cutoff n=5, and exact positive Cov(R,F). Classical equal marginal distributions of records/cycles are insufficient for this joint comparison. The targeted Resultary query and primary works were compared on objects, hypotheses, implication and parameters, not simply titles. No decisive prior-coverage theorem identified; this is not a proof of historical priority.

## value

PASS

Record and cycle statistics have identical marginals yet different interaction with fixed points. The first TP2 failure at n=5 and sign-changing adjacent minor are meaningful dependence-structure boundaries; an all-n positive covariance alongside negative minors provides a precise, natural counterexample to conflating linear association with likelihood-ratio order.

The dated certificate retains the supplied scientific assessment, sources and limitations.

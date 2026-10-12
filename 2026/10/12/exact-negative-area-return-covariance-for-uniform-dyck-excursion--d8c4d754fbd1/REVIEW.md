# Scientific review: exact negative area–return covariance for uniform Dyck excursions

## Correctness — PASS

The sample space, area normalization and inclusion of the final return are explicit. Primitive decomposition gives \(G(z,q,u)=[1-u zq F(zq^2,q)]^{-1}\). Differentiation is coefficientwise valid at every fixed semilength; the proved identity \(P_q(z,1)=z/(1-4z)\) yields all mixed moments by algebra. Exact marginal variances and Stirling's expansion yield the correlation rate. The sign is global because \(K_1=1\) and \(K_{n+1}/K_n=1+n/[2(n+2)(n+3)]>1\). The standalone verifier independently counts every path through semilength eleven and checks coefficients through 150; the proof, not the enumeration, establishes all sizes.

## Originality — PASS with residual risk

Janson (2007) treats Brownian excursion-area marginals. Kobayashi, Sato, Hoshi and Morita (2015, Section 3) give the marginal number-of-returns law. Blanco and Petersen (2012) give a joint area/rank law, but their rank is the noncrossing-partition rank, not the count of completed primitive returns. Petersen (2019, Chapter 10) supplies area-refined prime decompositions, and marking the prime count is immediate from those known identities. Thus no novelty is claimed for the generating-function construction itself. The inspected portions do not display the exact negative covariance and sharp correlation decay, although stronger uninspected identities may imply both. Searches of scholarly literature, published research records, FindStat return counts and OEIS area tables did not identify this classification. Negative search evidence alone does not establish world priority.

## Value — PASS

Total height measures integrated excursion size, whereas completed primitive returns measure fragmentation at the absorbing boundary. A strict finite-size sign and its exact coefficient quantify their antagonistic relationship. The leading-order Brownian area fluctuations are of order \(n^{3/2}\) while return-count variance remains bounded; an \(O(n)\) mixed covariance and precise vanishing-correlation constant are not consequences of the separate marginal laws. The result is a complete answer for a natural pairing of statistics rather than a parameter-selected example.

## Scope and residual limitations

The theorem is for uniform finite Dyck excursions. The asymptotic correlation has no independence implication. The area and return marginal generating functions are well known, the extension to joint marking is elementary, and an implicit equivalent of the new sign statement could reside in previously published joint-statistic literature. In particular, Petersen's Chapter 10 provides stronger enumerative infrastructure and cannot be cited as evidence that joint marking itself is new. The review is not a priority certification.

Self-review: passed. Independent audit: not yet performed.

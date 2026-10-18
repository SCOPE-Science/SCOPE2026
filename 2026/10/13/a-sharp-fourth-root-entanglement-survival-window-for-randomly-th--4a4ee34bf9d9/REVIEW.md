# Independent mathematical audit

## correctness

PASS

Reconstructed exact F2 stabilizer constraint: lost vertex j imposes u_j=0 and u_{j−1}=u_{j+1}. Four retained consecutive sites support a=Z_i X_{i+1} Z_{i+2}, b=Z_{i+1} X_{i+2} Z_{i+3}; partial transpose of (I+a)(I+b)/16 has eigenvalue −1/8 on a=b=−1, so F⊆E. Two consecutive erasures separate surviving clusters; when neither F nor H occurs every cluster has ≤4 retained vertices with stabilizer dimension ≤1 and is fully separable in product Pauli eigenbasis, proving E⊆F∪H. At most n·2^4 five-site gap patterns, each prob r⁵. Overlapping four-run factorial moments vanish at nr⁴=O(1), giving Poisson(λ) four-run count and correct limit. For nr⁴→∞ disjoint 4-blocks give (1−r⁴)^floor(n/4)→0. Finite F2 source verifier inspected, not mistaken for asymptotic proof.

## originality

PASS

Han–Zhang–Zhang 2026 directly contains the exact 4-site NPT witness for cycles and worst-case resistance/nonresistance theorem; that witness is credited. Read the publicly available manuscript including its cycle proof, and its quantifiers are adversarial fixed-cardinality erasures, not Bernoulli random loss. The new five-gap separability upper event and fourth-root Poisson window do not follow from the prior theorem as stated. Other loss papers ask Bell robustness/coherent information with different observables. Best-of-knowledge with possible unindexed random-erasure results.

## value

PASS

For a natural scalable graph-state family and physically standard Bernoulli erasures, quantifies probability of residual entanglement with sharp n^(−1/4) critical exponent, full limiting curve and explicit finite-size error. Converts a local NPT certificate into a global probabilistic phase transition with matching separability control; not a mere restatement of the known witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.

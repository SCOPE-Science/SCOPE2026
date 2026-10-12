# Review of Exact Grassmann distance spectrum of a dihedral Toeplitz quasi-MRD family

## Correctness

PASS. Proposition 3.6 of Lee--Park gives exactly the shifted Toeplitz matrix whose rows are the coefficient vectors of \(f,xf,\ldots,x^{m-1}f\). Since \(\deg f\le n-m\), there is no wraparound or truncation. After \(f=da\), \(g=db\) with \(\gcd(a,b)=1\), the intersection equation \(fu=gv\) forces \(u=bh\) and \(v=ah\), giving dimension \(\max\{0,m-t\}\). The monic-gcd generating identity gives the exact pair counts. The bundled verifier reproduces every formula over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_9\).

Risk: the finite checks cover only small cases and are not the proof; the symbolic argument carries the stated quantifiers.

## Originality

PASS. The recent source gives the rank-metric family, full-rank property, and quasi-MRD status but does not state the direct row-space projectivization, gcd intersection law, or pair-distance spectrum. Silva--Kschischang--Koetter use an identity-block lift, not direct row spaces. Cyclic/Sidon subspace-code literature uses scalar multiplication in extension fields. Focused repository and literature searches under source-name, exact-family, row-space, Toeplitz, gcd, polynomial-module, and constant-dimension aliases found no statement implying the theorem.

Risk: an older unindexed convolutional, Toeplitz, or ordinary-polynomial subspace construction may contain an equivalent formula. Search failure is not treated as novelty proof.

## Value

PASS. The source places rank-metric codes in the network-coding/subspace-code context. For a newly published infinite constant-rank quasi-MRD family, direct row spaces are a natural finite-geometric invariant. The theorem determines every pairwise intersection dimension and the complete distance distribution in closed form, not merely parameters or a finite slice. The minimum-distance limitation \(d_S=2\) is disclosed; the value is the exact all-parameter geometry.

Self-review: passed. Independent audit: not yet performed.

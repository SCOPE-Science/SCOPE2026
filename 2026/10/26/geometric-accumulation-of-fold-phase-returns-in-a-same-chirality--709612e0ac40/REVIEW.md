# Review

## Correctness

**PASS.** The fold condition is \(h_\lambda=K h_\lambda'\). After division by \(\lambda\), the defining equation converges in \(C^1\) to \(g-Kg'\). The simple-root hypothesis yields a unique fold \(x_f=x_*+O(\lambda)\). Substituting \(h_\lambda(x_f)=\lambda g(x_*)+O(\lambda^2)\) into \(x_f-K\log h_\lambda(x_f)\) gives the claimed logarithmic phase law. Its derivative is negative for sufficiently small positive \(\lambda\), ensuring a unique phase-locked parameter for each sufficiently large winding index. Solving that equation gives the geometric ratio. The result does not rely on numerical evidence.

## Originality

**PASS under the examined sources, with residual priority risk.** The closest primary source proves qualitative infinite winding and the existence of heteroclinic tangencies for same-chirality Bykov cycles, but the inspected statements do not give the geometric ratio for phase-locked fold returns. The 2012 same-chirality symmetry-breaking analysis provides related \(n\)-pulse and horseshoe results without this rate. The 2014 different-chirality paper studies a distinct tangency mechanism. The claim is deliberately limited to fold-phase returns and does not assert a universal ratio for all tangency sequences.

## Mathematical value

**PASS.** The law converts qualitative infinite winding into a parameter-spacing invariant determined by the local logarithmic coefficient \(K\). It predicts the asymptotic ratio of successive fold-phase returns and separates that local spectral contribution from the unfolding profile \(g\). This is a useful quantitative target for continuation or numerical tracking of the return geometry, provided the stated nondegeneracy conditions are checked.

## Closest literature and limitations

The main source is Labouriau and Rodrigues, *Global bifurcations close to symmetry*, arXiv:1504.01659v1, especially the local transition map and the proof that its fold winds infinitely often. Related sources are *Global generic dynamics close to symmetry* (2012) and *Dense heteroclinic tangencies near a Bykov cycle* (arXiv:1402.5455v1). A potentially related Lin-method analysis is cited in the literature for tangencies near the cycle; its full text was not inspected here, and it remains a priority risk. The present claim concerns phase-locked fold returns in the leading map, not every tangency of the full flow.

Self-review: passed. Independent audit: not yet performed.

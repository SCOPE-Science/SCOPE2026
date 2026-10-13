# Review: Exact right-angle singular exponent and sharp local gradient-integrability threshold for a Lorentz-scalar Dirac shell

## Correctness
PASS. The source defines \(u_0^L=\phi r^{\lambda_0^L}f_0^L\), gives the angular equation, and gives \(\mathcal D(D_0^L)=\mathcal D(D^L)+\operatorname{span}\{u_0^L\}\). At \(\omega=\pi/2\), substituting \(x=\lambda_0^L+1/2\) and \(y=\sin(\pi x/2)\) reduces the angular equation exactly to \(2y^2+ty-1=0\). The local gradient test is the elementary polar integral \(\int r^{p(\lambda_0^L-1)+1}dr\). The endpoint is logarithmic, and the minimal domain contributes only an \(H^1\) term, so the cutoff is sharp for the full distinguished domain.

## Originality
PASS with residual indexing risk. The primary paper was inspected at the definition of the angular exponents, the self-adjoint extension theorem, and the regularity discussion. It states the transcendental equation and \(H^{1/2}\) selection but not the right-angle closed form or the sharp \(W^{1,p}\) cutoff. The later arXiv:2307.12772v1 was inspected at its introduction and polygon theorem/corollary; it extends self-adjointness ranges but does not provide this singular exponent or gradient-integrability law. Targeted database and web searches for right-angle, \(\lambda_0\), \(W^{1,p}\), and the endpoint \(12/7\) did not locate a covering statement.

## Value
PASS. The exponent \(\lambda_0^L\) is the distinguished corner singularity that determines the loss of elliptic regularity in the source. A right angle is the canonical polygonal corner, and converting the implicit spectral equation into a closed coupling law produces a sharp first-order local regularity threshold, including a nontrivial strong-coupling limit \(12/7\). This is a structural regularity statement rather than an arbitrary numerical evaluation.

## Closest literature and limitations
The closest source is arXiv:1902.05010v2 itself. arXiv:2307.12772v1 is the closest later extension and addresses self-adjointness for more general shell couplings and polygon geometries. The present claim is restricted to the straight-wedge/local straight-edge right-angle model; no stronger curvilinear transfer is claimed. A residual risk remains that the elementary specialization has appeared in unindexed notes or under a different regularity terminology.

Self-review: passed. Independent audit: not yet performed.

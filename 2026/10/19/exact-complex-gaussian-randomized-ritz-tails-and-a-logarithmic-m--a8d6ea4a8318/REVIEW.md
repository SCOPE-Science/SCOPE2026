# Independent mathematical audit

## correctness

PASS

For the frozen record and the narrowed theorem in /workspace/repairs/1/RESULT.md, independently solve (A-mu I)(c,eta,s)^T proportional to K, where K represents the Haar null line of Omega*. The solution is mu=bsK1/(sK1-cK3) and eta=-bscK2/((a-b)sK1-acK3). The first denominator expresses pencil nonsingularity, the second excludes collision with the exact spectator a, and the fixed-sketch branch tends to zero as K3 is nonzero a.s. The denominator of eta is independent of K2 with variance (a-b)^2 s^2+a^2 c^2=(a-beta)^2+gamma^2, proving |eta|^2=q V/U with independent unit exponentials. Normalization then yields S=s^2+c^2 qV/(U+qV). The exponential-ratio CDF gives the stated compact-interval law, and integrating its complement gives Phi with the continuous uniform case q=1. Substituting q=(b/a)^2 theta^2+O(theta^4) into -q log(q)+O(q) verifies the leading coefficient and O(theta^2) remainder. The near-zero deterministic branch is w1 and its deterministic tie at resonance is handled explicitly in the repair. Separately, subtracting beta from mu gives gamma times a quotient of independent unit complex Gaussians via the orthogonal forms cK1+sK3 and sK1-cK3; the tail and divergence are correct but already covered. The frozen simulation and quadrature checker was inspected, not needed for the analytic proof.

## originality

PASS

PASS is for the repaired finite-angle eigenvector law and expected squared-sine asymptotic only. The frozen originality claim is too broad: the unrefined eigenvalue law and infinite second moment are directly covered by earlier indexed results. The repair removes that component from the Finding as a new claim and explicitly credits it as background. The finite-angle normalized eigenvector distribution and its mean remain distinct from the strongest inspected prior coverage.

## value

PASS

The repaired model supplies an exact diagnostic for an established algorithm, separating fixed-confidence angle accuracy from expected squared-sine performance on the very same trial plane. The finite-angle normalization produces an explicit logarithmic loss versus deterministic Ritz and gives the coefficient and resonance law, quantities that neither an eigenvalue heavy-tail bound nor the limiting angle slope alone supplies.

The dated certificate retains the supplied scientific assessment, sources and limitations.

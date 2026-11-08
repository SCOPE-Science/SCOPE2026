# Independent mathematical audit

## correctness

PASS

For memoryless binary 0/pi phase kicks on one bosonic mode with finite mean photon budget E>0, an isometry correlates the environment only with the photon-number parity P: the environmental density matrix has determinant (1-r)q(1-q), so its small eigenvalue is eta_r(q)=[1-sqrt(1-4(1-r)q(1-q))]/2. Measurement of output parity followed by preparing the corresponding environment state proves degradability for this discrete law. Number pinching preserves the complement and increases output entropy; energy-constrained degradable coding then reduces quantum/private unassisted rates to maximization of coherent information over number-diagonal inputs. Conditional entropy is maximized at common geometric laws on the two parity sectors with mean (E-q)/2, giving exactly max_{0<=q<=min(E,1)}[g((E-q)/2)+h2(q)-h2(eta_r(q))]. The binary cq conditional entropy is concave, and g strictly concave, yielding unique interior q for r>0 (with appropriate endpoint derivatives). At r=0 q=0 and capacity g(E/2); at r=1 thermal q=E/(1+2E). Differentiating at q->0 uniformly at fixed E and r->0 gives -L_E/2+r log(1/q)+(1-r)log(1-r)+O_E(q|log q|), so q_r~e^-1 exp[-L_E/(2r)] and capacity gain~r*q_r/ln2. Independent mpmath optimization for E=2, r=.1,.05,.025,.01 reproduced ratios converging toward one; the analytic derivative remainder, not sampling, supports the infinite asymptotic. No photon loss, two-way assistance, general phase law or jointly varying E is covered.

## originality

PASS

Best of knowledge PASS: the relevant generalized bosonic phase-noise coding literature gives capacity reductions or unconstrained capacity, not this exact singular two-point phase-noise optimizing parity distribution and e^{-constant/r} boundary layer. The primary 2026 arXiv full text could not be retrieved this execution despite arXiv and open-access mirror attempts, and authorized institutional retrieval was blocked by VPN; its actual abstract and research source-specific comparisons were inspected, but no claim of full-text noncoverage is based solely on the abstract. No covering theorem identified; residual historical risk explicit.

## value

PASS

The exact energy-limited solution for a natural non-Gaussian binary-phase bosonic noise channel identifies the full capacity optimizing photon distribution and a physically meaningful essential-singularity boundary layer; this cannot be read off from a general capacity variational principle without doing the nontrivial constrained entropy optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

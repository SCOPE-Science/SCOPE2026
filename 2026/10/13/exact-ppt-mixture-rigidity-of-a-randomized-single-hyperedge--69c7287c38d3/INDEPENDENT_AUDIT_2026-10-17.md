# Independent mathematical audit

## correctness

PASS

For a nonspanning edge the unused tensor factor is |+> and the mixture is product across E|E^c; for p=0 or theta in 2pi Z it is globally product. For a spanning edge the two-state range S=span{|+>^n,|1>^n} contains precisely the two product rays under every bipartition, since its coefficient matrix in the two independent local vectors is diag(s,t). For cut k|(n-k), the active local 2x2 matrix H has det H=kappa*u*w, with kappa=(exp(i theta)-1)2^{-n/2}; the partial transpose of rho has active 4x4 determinant -p^3 |kappa|^4 u^4 w^4 = -16 p^3 2^{-2n} sin^4(theta/2)(1-2^{-k})^2(1-2^{-(n-k)})^2. More importantly, any positive PPT-mixture decomposition would consist of positive operators with support inside S; each cut is effectively 2x2, hence PPT implies separable, and only the two product rays may occur. But rho has a nonzero |a><v| coherence coefficient p*kappa; thus no PPT mixture at p>0 and nontrivial phase. At p=1 the pure state is entangled on every split. The proof avoids the invalid shortcut NPT on each split => non-PPT-mixture.

## originality

PASS

Chen–Đoković Lemma 12 already establishes that a convex mixture of a product projector and an entangled pure projector is NPT across a fixed cut; do not claim ordinary NPT as new. Their article makes no PPT-mixture convex-hull classification across varying cuts. Salem–Silva–Andrade define randomized hypergraph states and perform numerical PPT-mixture SDP studies up to four qubits; the inspected full paper has no arbitrary-n single spanning hyperedge exact zero-threshold theorem and no parameterized active determinant formula. The analytic all-size necessary-and-sufficient PPT mixture criterion and quantitative determinant are best-of-knowledge original; possible implicit low-rank PPT-mixture implications are residual risks.

## value

PASS

The source proposes PPT-mixture SDPs and numerical GME in few-qubit randomized hypergraphs; this theorem computes a complete infinite-size sharp decision boundary for the simplest physically interpretable randomized hyperedge, with arbitrarily small positive success probability and all phases. The support-geometry proof distinguishes strict PPT-mixture exclusion from cutwise NPT, and exact determinant quantifies the strength and asymptotic weakness of each cut certificate. It is an exact natural structural boundary, not a random tiny numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.

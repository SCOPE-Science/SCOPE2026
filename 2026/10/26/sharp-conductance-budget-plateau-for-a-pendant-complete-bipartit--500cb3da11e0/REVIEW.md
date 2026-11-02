# Independent mathematical audit

## correctness

PASS

Put m=p-1>=3, v=(1,-3/m (m times),0 (q times),2); add to vv^T the positive coefficient (m²-9)/(m(m-1)) times the A0 centering projector. This X is PSD, zero on constants, trace X=m+5=p+4, and every allowed edge has squared X-distance exactly one. Thus tr(LX)=B >= λ2 tr(X) for every nonnegative weight allocation, including nonsymmetric ones. Candidate symmetric rates leaf 2λ, a-to-D 3λ/q, A0-to-D λ/q total B yield complete spectrum from four-class equitable quotient: eigenvalue 1 from A0, (p+2)/q from D, and remaining positive roots >1, giving gap λ min(1,(p+2)/q). At equality average an arbitrary maximizer over independent A0 and D permutations; concavity preserves λ2; complementary slackness forces Lv=λv and symmetric rates uniquely as candidate. Hence q>p+2 strict unattainability. Special p3,q2 rational weights yield gap 6/41>1/7. Independently reconstructed dual distances and eigenvalue formula for 60 (p,q) examples and exact SymPy boundary six-vertex spectrum. These supplement the all-weights trace certificate.

## originality

PASS

The semidefinite embedding duality and automorphism averaging are established by fastest-mixing and algebraic-connectivity literature, but the inspected primary results do not identify the pendant biclique graph family’s sharp conductance-budget plateau nor strict size-imbalance transition and p3 boundary. The claim does not ascribe novelty to the general SDP technique.

## value

PASS

A sharp graph-dependent plateau under a total conductance budget is an interpretable optimization boundary; it tells exactly when the leaf-attached bipartite network can saturate a universal all-allocation SDP bound, including a genuinely unbalanced transition and a small-p exception. The exact certificate is reusable in spectral network design.

The dated certificate retains the supplied scientific assessment, sources and limitations.

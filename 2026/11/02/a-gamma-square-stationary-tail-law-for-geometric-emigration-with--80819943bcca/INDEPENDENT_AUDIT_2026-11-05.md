# Independent mathematical audit

## correctness

PASS

The chain Y_next=sum_{j=1}^{(Y+1-K)_+}X_j, K geometric((1-p)p^k), X offspring geometric(2^{-k-1}), has exact conditional PGF and for invariant H(s) transformed h(u)=H(1-1/u). Monotonicity at infinity forces H(p)=1-a^-2 with a=p/(1-p), ruling out a<=1. For a>1, E Delta=1-a+O(p^y), E Delta^2=2y+O(1), E|Delta|^6=O(y^3), yielding negative Foster drift for V=(1+y)^eta, 1<eta<min(a,2), hence unique stationary law. The stationary deficit recurrence g(u+1)=u^-2+((u+1)(u-a)/u^2)g(u) has exact gamma multiplier R(u)=u Gamma(u-a)/Gamma(u). Grid iteration and beta integral yield g(u)~Gamma(a)^2 Gamma(2-a) u^{1-a} for 1<a<2; monotone Tauberian inversion gives P_pi(Y>n)~Gamma(a)^2 n^{1-a}. At a=2 logarithmic generating singularity and truncated-tail sum~log n; for a>2 mean=1/(a-2). Direct independent exact PGF calculations checked 24 separate rational instances. Gamma-ratio series and beta integral analytically checked; finite tests are not an infinite-tail proof.

## originality

PASS

Carper September 2026 treats positive post-reproduction immigration; its full relevant model/limits do not imply this chain with no post-reproduction immigrant, a mechanism explicitly marked as requiring other analysis. Yanev–Yanev 2004 accessible full text studies a reproduction-then emigration–immigration transition order with other emigration laws, and does not state the same exact Gamma-square constant for this pre-reproduction emigration model. The general theory of branching with emigration/immigration is a significant residual priority risk.

## value

PASS

Removing the post-reproduction immigrant is a natural mechanistic boundary; the exact recurrence threshold a=1, heavy-tailed finite invariant phase 1<a<=2, and finite-mean transition a=2 provide a sharp phase diagram. The exact gamma-square constant is a meaningful unknown invariant for stationary critical branching processes, not simply a relabeled general Tauberian theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For fixed r>1,C>0,d,e real, define L=log n,h=(r-1)/2,A=C(4pi)^h/sqrt(r). The high-variance maximum T=max_{1..n}N(0,1) gives Y=n barPhi(T), with exactly f_Y(y)=(1-y/n)^(n-1) for 0<y<n; conditional winner probability gives exact Eq. (1). The excluded tails Y<L^-3 and Y>L^3 have mass <=L^-3+exp(-L^3)=o((log L)^2/L^2). For y in [L^-3,L^3], normal Mills inversion yields t^2=2L-2log y-log L-log(4pi)+O(log L/L), uniformly, and the ratio barPhi(sqrt(r)t)/barPhi(t)^r=(sqrt(2pi)t)^(r-1)/sqrt(r)[1+(r-r^-1)/t^2+O(t^-4)]. Multiplying by the prescribed floored m_n yields intensity Ay^r[1+((d-h/2)log L+e-h log y-(h/2)log(4pi)+(r-r^-1)/2)/L+O((log L)^2/L^2)], uniformly. The binomial exponent and exact Y-density may be replaced by exponentials at errors exponentially small in L; Taylor expansion has integrable quadratic remainder O((log L)^2/L^2), giving coefficient H and J as claimed. H is strictly positive and the independent logL/L and 1/L terms force the unique (d*,e*) within fixed real d,e. Finite n cannot establish the infinite theorem; the displayed uniform bounds do.

## originality

PASS

Best-of-knowledge priority: the exact competing two-group Gaussian winner problem at critical n^r(log n)^(-(r-1)/2) is Theorem 1 of Zhang–Miao–Mao, whose complete Sections 2–4 and proof establish the limiting Gumbel probability, not the explicit signed loglog(n)/log(n) bias or fixed-parameter (d,e) calibration. The other primary articles cover one-sample normal-extreme norming and winner/point-process limits, not this full next-order coefficient. Resultary and separate published SCOPE source searches did not show a dominating statement. A search miss is not a novelty certificate.

## value

PASS

Critical heterogeneous Gaussian maximum competition has a natural sample-size design question: the leading law chooses m_n≈Cn^r(log n)^(-(r-1)/2) to realize a nontrivial limiting win chance, but does not calibrate finite n. The derived universal signed loglog(n)/log(n) bias and exact fixed two-parameter cancellation supply an actionable mathematical refinement, involving a nonstandard integrated second-order Gaussian tail ratio rather than trivial parameter substitution. H>0 proves uniqueness, and the formula works for a whole natural continuum of variance ratios and positive C, not an arbitrary numerical slice. It provides a precise next-order asymptotic relation not contained in first-order winner theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.

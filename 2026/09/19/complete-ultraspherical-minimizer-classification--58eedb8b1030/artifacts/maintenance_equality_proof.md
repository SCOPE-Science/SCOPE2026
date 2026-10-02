# Equality cases at the Legendre endpoint

The parameter is exactly \(\lambda=1/2\), not the positive-connection argument of Proposition 6.3 in Castillo--Sadigova v2. The following checks complete the strictness argument of RESULT.md.

For the rotation range, the transfer product in Lemma 3.1 has a strictly positive path coefficient selecting the projection at the first step and the identity component thereafter: all parameters \(s>0\) have \(0<\delta_s<1\). Its first coordinate is \(\sin\theta\cos(N\theta)\). For \(\theta>0\) and \((N+1)\theta\le2\pi\), one has \(0<N\theta<2\pi\); this path is strictly below \(\sin\theta\). Every other path is at most \(\sin\theta\), hence the convex sum is strict.

For the weak energy range, the endpoint products (3.19)--(3.20) are strictly below \(1/2\) for \(N\ge K+1\): the factors \((s/(s+1))^2<s/(s+2)\) and \(\delta_K>2/(K+2)\) are strict. With \(F(0)=1\), convexity gives \(F(y)<1-y/2\) for \(0<y\le1\). Thus \(E_N<\sin^2\theta\), and its non-increasing continuation implies \(|q_n|<1\).

For \(K\ge6\), (3.27)--(3.30) give \(F_N(1/2)<320/429<3/4\). The chord on \([0,1/2]\) is therefore strictly below \(1-y/2\) whenever \(y>0\); the preceding degrees are covered by rotation. For \(5<K<6\), the remaining degree-six bound has \(F_*(7/10)<406/625<13/20\), again strictly below the required chord. The two other remaining degrees have \(1-q_4\) and \(1-q_5\) equal to positive factors times \(1-x\) in Appendix A. Its proof shows \(H_4,H_5>0\) on the precise ranges; therefore these cases are strict for \(x<1\).

For all cells \(k\ge3\), Proposition 4.1 supplies \(0<\theta<\pi/2\) and \(\theta\le2\pi/(k+1)\), so both integer parameters \(K=k,k+1\) satisfy the estimates. In the difference formula (2.8), the Jacobi signs \(Q_k<0<Q_{k-1}\) inside a cell make all later comparisons strict. At a breakpoint exactly one Jacobi factor vanishes: the adjacent degree ties, while every later positive auxiliary degree remains strict. Earlier degrees follow from interlacing and the contiguous identity.

For the first interval, Lemma 5.1 gives strictness for every degree at least seven: \(F(t_0)>0\), \(F(1)=0\), and concavity give \(F(t)>0\) for \(t_0\le t<1\). At \(d=2\), Appendix B gives positive degree-three and degree-six factors; the degree-four polynomial \(h_2=3+5t-35t^2(1-t)\) is strictly positive (the apparently non-strict lower bound at \(t=4/5\) is strict since \(t(1-t)<1/4\) there). Degree two ties only at \(t=1/3\); degree five has the single interior extra zero \(9t^2-1=0\).

For the second interval, (5.9)--(5.10) give \(G(x^2)>0\) for every degree at least seven. The factors in (B.17)--(B.19) are strict for degrees four and six. Degree three ties only at the upper breakpoint; degree one only at the lower breakpoint. For degree five, \(H<0\) for nonnegative \(x\) by (B.22); for negative \(x=-u\), (B.24)--(B.25) show \(J\) strictly increasing and (B.26) at \(d=2\) gives \(J(u)<J(1/3)=0\) unless \(u=1/3\). This establishes precisely the exceptional degrees \(1,2,5\) and no others.

All assertions are confined to the Legendre endpoint. Proposition 6.3 explicitly assumes \(\alpha>0\); its positive-connection proof does not handle this endpoint. The new argument closes that missing equality case rather than claiming the source's positive-parameter classification.

# Disconnected strict sub-Gaussian mixing for a symmetric two-radius law

## Finding

For every real \(a\ge4\), let \(X_{a,p}\) take the values \(-1,1\) with mass \((1-p)/2\) each and \(-a,a\) with mass \(p/2\) each, where \(p\in[0,1]\). Its variance is \(v_{a,p}=1+p(a^2-1)\). Write \(s_a^2(p)\) for the smallest Gaussian proxy variance of this centered law, and call it strictly sub-Gaussian if \(s_a^2(p)=v_{a,p}\).

For every such \(a\), the set of strictly sub-Gaussian weights in \((0,1)\) contains an interval adjacent to zero and another adjacent to one. It excludes the weight \(p_a=1/(2a^4)\), and at that weight
\[
\mathbb E X_{a,p_a}^4-3v_{a,p_a}^2<-\frac32.
\]
In particular the strict sub-Gaussian set is disconnected. This is a failure of the fourth-cumulant diagnostic inside a specific symmetric family that is strictly sub-Gaussian toward both ends of its mixing range.

## Scope and notation

The proxy and the test function used below are
\[
\begin{split}
M_{a,p}(t)&=(1-p)\cosh t+p\cosh(at),\\
s_a^2(p)&=\sup_{t\ne0}\frac{2\log M_{a,p}(t)}{t^2},\\
F_a(p,t)&=\log M_{a,p}(t)-v_{a,p}t^2/2.
\end{split}
\]
The proxy is always at least the variance by the limit at \(t=0\). Thus strict sub-Gaussianity is equivalent to \(F_a(p,t)\le0\) for all real \(t\). The endpoints of the strict intervals may depend on \(a\); neither the exact component endpoints nor the number of components is asserted.

## Proof

**An excluded weight with negative fourth cumulant.** At \(p_a\) the variance exceeds one, while the fourth moment is \(1+p_a(a^4-1)=3/2-1/(2a^4)\). Subtracting three times the squared variance gives the claimed bound. For \(t=a\), the mass at \(+a\) gives \(\log M_{a,p_a}(a)> a^2-\log(4a^4)\), and \(v_{a,p_a}a^2/2\le a^2/2+1/4\). Hence
\[
F_a(p_a,a)>g(a):=a^2/2-1/4-\log(4a^4).
\]
Here \(g'(a)=a-4/a>0\) on \([4,\infty)\), and \(g(4)=31/4-10\log 2>0\) since \(\log2<3/4\). Thus \(s_a^2(p_a)-v_{a,p_a}>2g(a)/a^2>0\). By continuity the test with \(t=a\) also excludes an open interval containing \(p_a\).

**Strictness near both endpoints.** Fix \(a\). At \(p=0\) and \(p=1\), \(F_a(p,t)<0\) for every \(t\ne0\), because \(\log\cosh u<u^2/2\) for \(u\ne0\) by integrating \(\tanh u<u\) for \(u>0\) and using evenness. For all weights the value and first three \(t\)-derivatives of \(F_a\) at zero vanish. At the endpoints the fourth derivatives at zero are respectively \(-2\) and \(-2a^4\). Joint continuity of this derivative and Taylor's theorem give \(\delta>0\) and endpoint neighborhoods in which \(F_a(p,t)<0\) for \(0<|t|<\delta\). The compact region \(\delta\le |t|\le 2a+1\) has strict negativity at the endpoints, so joint continuity gives uniform strict negativity there after shrinking the weight neighborhoods. Finally \(M_{a,p}(t)\le e^{a|t|}<e^{t^2/2}\le e^{v_{a,p}t^2/2}\) for \(|t|>2a\), uniformly in the weight. This proves the two endpoint intervals and hence disconnectedness.

## Sparse three-mass comparison

The divergence along \(p_a\) can be quantified by comparison with an already studied three-mass proxy problem [2]. If \(S_a\) equals \(\pm a\) with probability \(p_a/2\) each and zero otherwise, let \(M_S\) and \(s^2(S_a)\) be its MGF and optimal proxy variance. For every real \(t\),
\[
M_S(t)\le M_{a,p_a}(t)\le \cosh(t)M_S(t),\qquad
s^2(S_a)\le s_a^2(p_a)\le s^2(S_a)+1.
\]
For completeness set \(L=\log(1/p_a)=\log(2a^4)\). Testing the atom at \(+a\) at \(t=2L/a\) gives
\[
s^2(S_a)\ge \frac{a^2}{2L}\left(1-\frac{\log2}{L}\right).
\]
For \(0\le t\le L/(2a)\), \(M_S''(t)\le p_a a^2 e^{L/2}=1/\sqrt2\), giving \(2\log M_S(t)/t^2\le1/\sqrt2\) by two integrations and \(\log(1+x)\le x\). For \(t\ge L/(2a)\), \(M_S(t)\le 1+e^{at-L}\), so
\[
\frac{2\log M_S(t)}{t^2}\le \max\{0,2a/t-2L/t^2\}+\frac{8a^2\log2}{L^2}
\le \frac{a^2}{2L}+\frac{8a^2\log2}{L^2}.
\]
Evenness handles negative \(t\). The bounds and the proxy comparison give \(s_a^2(p_a)\sim a^2/(8\log a)\), while \(v_{a,p_a}\to1\) and the fourth cumulant tends to \(-3/2\). We record the proxy rate to quantify the example; it is the same leading regime as the sparse three-mass comparison, not a separate novelty claim.

## Verification and relationship to prior work

The accompanying `verify.py` checks exact moments and evaluates the nonzero MGF witness and an asymptotic lower estimate at selected amplitudes. The analytic proof, not finite sampling, establishes the result for all real \(a\ge4\).

Arbel–Marchal–Nguyen [1, Proposition 3.2] give the moment obstruction: strict sub-Gaussianity requires a **nonpositive** fourth cumulant. This obstruction is not a sufficient condition. Their three-mass example in §3.2.1 illustrates failure with positive fourth cumulant; their Proposition 3.3 gives a sufficient condition in terms of all even moments. Atouani–Marchal–Arbel [2, §3.1] characterize the symmetric three-mass law, with strict sub-Gaussianity when its total nonzero mass is at least \(1/3\); it has fourth cumulant zero at that threshold. This is not the two-radius mixing problem. The contribution here is the explicit excluded weight with negative fourth cumulant together with both strict intervals in the same two-radius family, uniformly as a statement for every fixed \(a\ge4\).

## References

1. J. Arbel, O. Marchal, H. D. Nguyen, *On strict sub-Gaussianity, optimal proxy variance and symmetry for bounded random variables*, [arXiv:1901.09188v1](https://arxiv.org/abs/1901.09188).
2. S. Atouani, O. Marchal, J. Arbel, *Optimal sub-Gaussian variance proxy for 3-mass distributions*, [arXiv:2510.06132v1](https://arxiv.org/abs/2510.06132).

# The larger part controls biharmonic heat amplification at every time on a biclique

## Finding

Let \(L\) be the unnormalized combinatorial Laplacian of \(K_{a,b}\), where \(2\le a\le b\), and write \(N=a+b\), \(T(t)=e^{-tL^2}\) for \(t\ge0\). Use counting-coordinate norms. **If \(a<b\), every larger-part row has strictly greater absolute row sum than every smaller-part row whenever \(\|T(t)\|_{\infty\to\infty}>1\).** The row types tie at other times, and at all times when \(a=b\). Consequently no comparison between two candidate contributions is needed:
\[
\|T(t)\|_{\infty\to\infty}=1+\frac{2(b-1)}{bN}\left[Ne^{-a^2t}-b-ae^{-N^2t}\right]_+,
\qquad [x]_+=\max(x,0).
\]
For every size ratio, the unique maximizing time and peak are
\[
\theta_B=\frac{\log(N/a)}{b(b+2a)},\qquad
\|T(\theta_B)\|_{\infty\to\infty}
=1+\frac{2(b-1)}N\left[\frac{b+2a}N\left(\frac aN\right)^{a^2/[b(b+2a)]}-1\right].
\]
The maximizing time and value here extend the exact peak calculation in [2] from a large-imbalance regime to all ratios. The contribution is the larger-part dominance throughout the transient, not the underlying partwise norm expression or recovery cutoffs, which already follow from [1].

## Assumptions and scope

The graph is simple and unweighted. The two vertex classes have at least two vertices each. The matrix is \(e^{-tL^2}\), not ordinary graph heat or the normalized-Laplacian analogue. The absolute row sums are the induced \(\ell^\infty\) norm on either real or complex data. No all-time row dominance is asserted for general multipartite graphs or other powers of \(L\).

## Proof

**Two row types and known recovery ordering.** Write \(A,B\) for the parts of sizes \(a,b\). The eigenspace decomposition uses the constants, vectors of sum zero supported on \(A\), vectors of sum zero supported on \(B\), and the one-dimensional part-constant contrast, with eigenvalues \(0,b,a,N\), respectively. For \(a=b\) the two supported subspaces are orthogonal and share one eigenvalue. The projections are \(P_0=J/N\), \(P_A=I_A-J_A/a\), \(P_B=I_B-J_B/b\), and \(I-P_0-P_A-P_B\), with the block matrices padded with zeros. Thus the distinct within-part entries are \(H_A(t)/(aN)\) and \(H_B(t)/(bN)\), where
\[
H_A(t)=a+b e^{-N^2t}-N e^{-b^2t},\qquad
H_B(t)=b+a e^{-N^2t}-N e^{-a^2t}.
\]
Each diagonal entry is positive, and each cross-part entry is \((1-e^{-N^2t})/N\), positive for \(t>0\). The row sums are one because \(L\) annihilates the constants. Since counting-coordinate row norms are one plus twice the mass of the negative entries, the two row norms are \(1+2[U]_+\) and \(1+2[V]_+\), where
\[
U=-\frac{a-1}{aN}H_A,\qquad V=-\frac{b-1}{bN}H_B.
\]
These expressions specialize [1]. For each part the distinct within-part entries are negative prior to its unique strictly positive cutoff and positive afterward. In fact \(H_A(0)=0\), \(H_A(t)\to a>0\), and
\[
H_A'(t)=Nb^2e^{-b^2t}\left[1-\frac Nb e^{-(N^2-b^2)t}\right]
\]
changes sign once from negative to positive; the formula for \(H_B'\) interchanges \(a,b\). In the notation of [1] the two cutoffs are \(\tau_A=N^{-2}u(b/N)\) and \(\tau_B=N^{-2}u(a/N)\), with \(u\) strictly decreasing on \((0,1)\). Hence \(\tau_A<\tau_B\) when \(a<b\). This ordering is an input to the row comparison, not a new recovery theorem.

**Strict larger-part dominance during the transient.** Assume \(a<b\), and put \(\alpha=(b-1)/b\), \(\beta=(a-1)/a\), and \(\delta=\beta b-\alpha a=(b-a)(1-N/(ab))>0\). For \(D(t)=V(t)-U(t)\), direct subtraction gives
\[
D(t)=-\frac{b-a}{N}+\alpha e^{-a^2t}-\beta e^{-b^2t}+\frac\delta N e^{-N^2t}.
\]
It begins at zero with \(D'(0)=b-a>0\) and tends to \(-(b-a)/N<0\). Let
\[
G(t)=e^{a^2t}D'(t)=-\alpha a^2+\beta b^2e^{-(b^2-a^2)t}-\delta N e^{-(N^2-a^2)t}.
\]
In \(G'\) the ratio of the positive term to the magnitude of the negative term strictly decreases, because \(N^2-a^2>b^2-a^2>0\). Therefore \(G\) either decreases throughout \(t>0\) or increases and then decreases strictly. Since \(G(0)>0\) and its limit is negative, \(D'\) changes sign exactly once from positive to negative. It follows that \(D\) has exactly one positive zero. But \(D(\tau_A)=V(\tau_A)>0\), so that zero lies strictly after \(\tau_A\). For \(0<t<\tau_A\) we have \(V>U>0\); for \(\tau_A\le t<\tau_B\) only \(V\) is positive. At \(t=0\) and at \(t\ge\tau_B\) both positive parts are zero. Thus the larger part wins strictly whenever the norm exceeds one. When \(a=b\), symmetry gives equality of the row norms and the same formula.

**Peak.** On the interval where the positive part in the norm is active, its bracket equals \(-H_B(t)\) and has exactly one maximum by the derivative test. Its stationarity equation is \(e^{-(N^2-a^2)\theta_B}=a/N\). Since \(N^2-a^2=b(b+2a)\), substitution gives both peak formulas. At the peak an extremizing \(\ell^\infty\) datum has value \(-1\) at the other vertices of a chosen larger-part row, and \(+1\) at the row vertex and every vertex of the smaller part.

## Verification

The companion standard-library `verify_bipartite.py` tests the exact rational projections and compares the two row norms with truncated Taylor matrix exponentials for 25 small bicliques, across five sampled time parameters each, with additional checks at selected peaks and cutoffs. These finite checks corroborate the formulas but do not replace the derivative and sign proof of all-time dominance. The script also includes scope beyond the present claim (asymptotic recovery and amplification diagnostics).

## Relationship to prior work

The general squared-Laplacian multipartite theorem [1] gives the two row contributions by specialization and supplies their recovery ordering through its decreasing function \(u(x)\). Its proof also gives \(u(x)\to 1.256431\ldots\) as \(x\uparrow1\) and \(xu(x)\to1\) as \(x\downarrow0\), which already imply the small- and large-part recovery scales at fixed \(a\) and growing \(b\). The biclique result [2] identifies the same sharp peak for \(b\ge32a\) and derives the large-imbalance amplification and time scales, with uniformity as \(b/a\to\infty\). The fractional multipartite result [3] gives the maximum over individual part contributions at fixed time and at their candidate peaks, including the present kernel by specialization to power two. None of those displayed comparison formulas selects the larger row at every transient time for every biclique ratio. The proof above establishes precisely that selection and extends the explicit unique peak to all ratios. The bibliographic dates of [2] and [3] are the same as that of the original finding; no within-day priority is inferred.

## References

[1] *Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph*, 2026-10-18, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-sharp-positivity-cutoff-for-squared-laplacian-heat-on-every-comp--e4f9c89a420f/RESULT.md), especially proof steps 3–5.

[2] *Two timescales of transient amplification and positivity recovery on unbalanced bipartite graphs*, 2026-10-26, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-two-timescales-of-transient-amplification-and-positivity-recover--61512629ac2e/RESULT.md).

[3] *A sharp positivity transition for fractional graph heat on complete multipartite networks*, 2026-10-26, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1/RESULT.md).

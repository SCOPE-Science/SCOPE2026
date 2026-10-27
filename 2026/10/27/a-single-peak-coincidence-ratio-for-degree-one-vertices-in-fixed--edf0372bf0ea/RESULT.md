# A single-peak coincidence ratio for degree-one vertices in fixed-edge random graphs

## Finding
For a uniformly random simple labelled graph \(G(n,m)\) with \(n\ge6\) vertices and exactly \(m\) edges, let \(I_u\) and \(I_v\) indicate that two fixed distinct vertices have degree one. Set
\[
Q_{n,m}=\frac{\Pr(I_u=I_v=1)}{\Pr(I_u=1)^2}.
\]
Let \(B=\binom{n-2}{2}\). On the complete positive-joint-probability range \(1\le m\le B+2\), the sequence \(Q_{n,m}\) is strictly log-concave, strictly increases up to \(m=\lceil n/2\rceil\), and strictly decreases thereafter. Thus its **unique maximum** is exactly at \(\lceil n/2\rceil\), regardless of the order \(n\). The set of edge counts for which \(\operatorname{Cov}(I_u,I_v)>0\) is empty or one contiguous interval of integers containing \(\lceil n/2\rceil\); outside the positive-joint-probability range, the covariance is nonpositive. In particular, when \(n=8\) its covariance is positive for exactly \(m=4\), and negative for all \(1\le m\le \binom72\) except \(m=4\) wherever the marginal is nondegenerate.

## Assumptions and scope
The graph is sampled uniformly from all \(\binom{\binom n2}{m}\) simple labelled graphs with vertex set \(\{1,\ldots,n\}\). Write \(N=\binom n2\), \(A=\binom{n-1}{2}\), \(B=\binom{n-2}{2}\), and \(K=n-2\). The ratio is defined only when \(\Pr(I_u=1)>0\), namely \(1\le m\le A+1\). Binomial coefficients with invalid lower index equal zero. Strict log-concavity is asserted on positive \(Q_{n,m}\), with interior indices \(2\le m\le B+1\). When \(m\in\{0\}\cup\{A+2,\ldots,N\}\), both degree-one indicators vanish identically and covariance is zero.

## Proof
**Exact joint counting.** For a specified vertex, choose its unique incident edge, then choose all remaining edges outside its star:
\[
p_m=\Pr(I_u=1)=\frac{(n-1)\binom A{m-1}}{\binom Nm}.
\]
For both vertices, either their common edge is the sole incident edge at each vertex (one choice), or it is absent and the two vertices each have one edge to distinct remaining incident-edge classes (\(K^2\) choices). Therefore
\[
q_m=\Pr(I_u=I_v=1)=\frac{\binom B{m-1}+K^2\binom B{m-2}}{\binom Nm}.
\]
Thus \(Q_{n,m}=q_m/p_m^2\). For \(1\le m\le B+2\), both numerator and denominator are positive.

**Adjacent quotient.** Put \(t=N-m\), \(a=K^2-1\), \(b=(K^2+K-4)/2\), and \(L_m=am-b\). Simplifying the binomial coefficients gives, for \(1\le m\le B+1\),
\[
\frac{Q_{n,m+1}}{Q_{n,m}}
=\frac{m}{m+1}\frac{t(t-2K+1)}{(t-K)^2}\frac{L_m+a}{L_m}.
\]
Writing \(x=b/a\), where \(0<x<1\), this becomes
\[
F_m:=\frac{Q_{n,m+1}}{Q_{n,m}}
=\left(1+\frac{x}{(m+1)(m-x)}\right)
\left(1-\frac{K^2-t}{(t-K)^2}\right).
\]
Here \(K\ge4\), and within the specified range \(2K\le t\le N-1<K^2\). The first parenthesis strictly decreases as \(m\) increases. In the second, \(h(t)=(K^2-t)/(t-K)^2\) has derivative
\[
h'(t)=\frac{t+K-2K^2}{(t-K)^3}<0.
\]
Since \(t=N-m\) decreases as \(m\) increases, \(h(t)\) increases and the second positive parenthesis strictly decreases. Consequently \(F_m\) strictly decreases with \(m\), proving strict log-concavity of the full positive sequence.

**Location of the peak.** It remains to locate the index where \(F_m\) crosses one. Its sign is that of
\[
P(n,m)=m t(t-2K+1)(L_m+a)-(m+1)(t-K)^2L_m.
\]
For \(n=2r\), \(r\ge3\), direct expansion gives
\[
P(2r,r-1)=2(4r^5-14r^4+16r^3-7r^2+3r-3)>0,
\]
\[
P(2r,r)=-4(r-1)^2(2r^3-7r^2+5r+1)<0.
\]
The first polynomial, under \(r=z+3\), has coefficients \(4,46,208,461,501,213\) in descending powers of \(z\), all positive. The cubic in the second line, under \(r=z+3\), is \(2z^3+11z^2+17z+7>0\).
For \(n=2r+1\), \(r\ge3\),
\[
P(2r+1,r)=(r-1)(10r^3-4r^2-3r+2)>0,
\]
\[
P(2r+1,r+1)=-2(r-1)^2(8r^3-r^2-5r+2)<0.
\]
Their cubics become \(10z^3+86z^2+243z+227\) and \(8z^3+71z^2+205z+194\), respectively, under \(r=z+3\); both are positive for \(z\ge0\). Strict decrease of \(F_m\) proves the unique maximum at \(\lceil n/2\rceil\) for every \(n\ge6\).

**Covariance sign and a sharp eight-vertex example.** Since \(p_m>0\), \(\operatorname{Cov}(I_u,I_v)=p_m^2(Q_{n,m}-1)\), and strict unimodality makes the positive set a single interval containing the maximum whenever nonempty. For \(B+3\le m\le A+1\), \(q_m=0\), hence the covariance is negative. Direct exact substitution for \(n=8\) gives
\[
\operatorname{Cov}(I_u,I_v)=\begin{cases}
-95/21294,&m=3,\\
29/342225,&m=4,\\
-113/97344,&m=5.
\end{cases}
\]
Strict unimodality and the nonpositive tail then show positivity occurs exactly at \(m=4\).

## Verification
The accompanying \(check.py\) independently enumerates all graph edge subsets for \(4\le n\le6\), checks the exact probability identities, and performs 13,618 exact integer/rational assertions including the adjacent quotient, strict log-concavity, peak index, and the eight-vertex covariance values for all \(6\le n\le32\). The infinite-order proof above is analytic; finite tests provide corroboration only. Run with `python3 check.py` (standard library only).

## Relationship to prior work
Exact degree counts, normal approximations, and degree-restricted random graphs are classical. Gutman and Paule (2002) calculate the variance of the *numerical vertex degree* in fixed-edge graphs, rather than the covariance of degree-one events. Grimmett and Janson (2007) analyze vertex-degree constraints for an independent-edge graph ensemble, and Goldstein (2010) studies normal approximation of degree counts in the independent-edge ensemble. The result here concerns a different finite-edge-budget object: the exact ratio of joint to product marginal **degree-one event** probabilities as the integer edge count varies. No claim is made that the elementary joint-counting formula itself is new.

## Limitations
The theorem is for simple labelled fixed-edge graphs only, with \(n\ge6\). It does not determine the sign of the covariance at the maximum for every \(n\); it determines the location and strict shape of the coincidence ratio, and the possible geometry of positive covariance. Broader random graph references not available in full may imply the monotonicity result implicitly; historical priority is provisional. No statement about conditional independence follows from zero covariance.

## References
1. I. Gutman and P. Paule, *The variance of the vertex degrees of randomly generated graphs*, Univ. Beograd Publ. Elektrotehn. Fak. Ser. Mat. 13 (2002), 30–35, DOI:10.2298/PETF0213030G.
2. G. Grimmett and S. Janson, *Random graphs with forbidden vertex degrees*, arXiv:0712.0270, first public 2007-12-03; subsequently Random Structures & Algorithms 37 (2010), 137–175.
3. L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, arXiv:1005.4390, first public 2010-05-24; subsequently Annals of Applied Probability 23 (2013), 617–636.

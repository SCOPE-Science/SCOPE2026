# Exact Rényi–Tsallis monotonicity threshold for two Bernoulli sums
## Finding
Let \(B_1\sim\mathrm{Bern}(p_1)\) and \(B_2\sim\mathrm{Bern}(p_2)\) be independent, with \(0\le p_1,p_2\le 1/2\), and let \(S=B_1+B_2\). For every Rényi or Tsallis order \(0\le q\le 2\), the entropy of \(S\) is coordinatewise nondecreasing when either \(p_i\) is increased toward \(1/2\). For every \(q>2\), coordinatewise monotonicity fails already for two Bernoulli summands. Consequently \(q=2\) is the exact universal order threshold for the two-summand monotonicity problem posed by Hillion and Johnson.

For \(q>0\), \(q\ne1\), write
\[
H_{R,q}=\frac{1}{1-q}\log\!\left(\sum_{k=0}^2 f_k^q\right),
\qquad
H_{T,q}=\frac{1}{q-1}\left(1-\sum_{k=0}^2 f_k^q\right),
\]
where \(f_k=\Pr\{S=k\}\). At \(q=1\) both are understood by the Shannon limit. At \(q=0\), Rényi entropy is the logarithm of support cardinality and Tsallis entropy is support cardinality minus one.

## Assumptions and scope
The result is exactly for two independent Bernoulli summands and the coordinatewise order region \(0\le p_1,p_2\le1/2\). It does not prove the Hillion–Johnson conjecture for three or more summands. It also does not assert joint concavity of Rényi or Tsallis entropy; coordinatewise monotonicity and joint concavity are distinct properties.

For the analytic argument, first take \(0<p_1,p_2\le1/2\). Set
\[
u=\frac{p_1}{1-p_1},\qquad v=\frac{p_2}{1-p_2},
\]
so \(0<u,v\le1\). Since \(v\) is strictly increasing in \(p_2\), it is enough to determine the sign of the derivative with respect to \(v\). The boundary cases with a zero success probability are then obtained by continuity for \(q>0\), and directly from support cardinality for \(q=0\).

## Proof
The mass function of \(S\), after a common normalization, is
\[
(f_0,f_1,f_2)
=
\frac{(1,u+v,uv)}{(1+u)(1+v)}.
\]
Hence the power sum is
\[
P_q(u,v)
=
\sum_{k=0}^2 f_k^q
=
\frac{1+(u+v)^q+(uv)^q}{(1+u)^q(1+v)^q}.
\]
For \(q>0\), \(q\ne1\), put \(r=q-1\). Direct differentiation gives
\[
\frac1q\,\partial_v\log P_q
=
\frac{\Phi_r(u,v)-1}
{(1+v)\,[1+(u+v)^q+(uv)^q]},
\]
where
\[
\Phi_r(u,v)=(1-u)(u+v)^r+u(uv)^r.
\]
Thus the sign problem is reduced to comparing \(\Phi_r\) with one.

For fixed \(u,v\in(0,1]\), the map \(r\mapsto\Phi_r(u,v)\) is convex because it is a positive weighted sum of exponentials in \(r\). Moreover,
\[
\Phi_0=1,
\]
and
\[
\Phi_1
=(1-u)(u+v)+u^2v
=u-u^2+v(1-u+u^2)
\le1,
\]
because \(v\le1\). The derivative at zero is
\[
\Phi'_0
=
(1-u)\log(u+v)+u\log(uv).
\]
Weighted AM–GM yields
\[
(u+v)^{1-u}(uv)^u
\le
(1-u)(u+v)+u(uv)
=
\Phi_1
\le1,
\]
so \(\Phi'_0\le0\).

If \(1\le q\le2\), then \(0\le r\le1\). Convexity between zero and one gives
\[
\Phi_r
\le
(1-r)\Phi_0+r\Phi_1
\le1.
\]
Therefore \(P_q\) is nonincreasing in \(v\). Since \(1/(1-q)<0\) and \(1/(q-1)>0\), both Rényi and Tsallis entropy are nondecreasing in \(v\).

If \(0<q<1\), then \(-1<r<0\). The tangent-line inequality for a convex function gives
\[
\Phi_r
\ge
\Phi_0+r\Phi'_0
\ge1,
\]
because both \(r\) and \(\Phi'_0\) are nonpositive. Thus \(P_q\) is nondecreasing in \(v\). Here \(1/(1-q)>0\) and \(1/(q-1)<0\), so again both entropies are nondecreasing. Symmetry exchanges \(p_1\) and \(p_2\), proving coordinatewise monotonicity.

At \(q=1\), the Shannon monotonicity theorem of Hillion and Johnson applies. At \(q=0\), increasing a Bernoulli parameter from zero can only enlarge the support of the two-summand law, while away from zero the support size is constant; hence both order-zero entropies are nondecreasing.

Sharpness for \(q>2\) is supplied by Hillion and Johnson's two-summand local calculation. For \(p_1=1/2-\varepsilon\), with the other parameter approaching \(1/2\), the relevant entropy derivative has leading term proportional to
\[
-\frac{q}{q-1}\,2^{2-2q}(2^q-2q)\varepsilon.
\]
For \(q>2\), one has \(2^q-2q>0\): equality holds at \(q=2\), while the derivative of \(2^q-2q\) is already positive at two and thereafter increases. Thus the derivative is negative for sufficiently small positive \(\varepsilon\), so coordinatewise monotonicity fails above order two.

## Verification
The analytic proof is self-contained apart from the previously established Shannon endpoint and the published sharpness counterexample for \(q>2\). The accompanying `verify.py` independently evaluates the derived power-sum derivative identity on a deterministic grid, checks the convexity-sign inequalities across representative orders on both sides of one, and stress-tests coordinatewise entropy monotonicity. These finite checks are consistency tests only; the infinite statement is proved by the convexity and tangent-line argument above.

## Relationship to prior work
Hillion and Johnson's monotonicity paper proves the Shannon case, proves the collision-entropy endpoint \(q=2\), gives a two-summand local failure for every \(q>2\), and states Conjecture 4.4 asking for monotonicity throughout \(0\le q\le2\). The result here resolves that conjecture completely for the first nontrivial dimension \(n=2\) and shows that the source's upper endpoint is exactly sharp in that dimension.

Madiman, Melbourne, and Roberto study Rényi entropy inequalities for Bernoulli sums, including sharp variance and entropy comparisons, but their stated results do not supply this coordinatewise two-parameter monotonicity classification. A 2026 paper by Wang determines the universal threshold for the different property of joint concavity: its abstract states joint concavity for \(0<q\le1\) and failure for every \(q>1\). That does not imply or contradict coordinatewise monotonicity through \(q=2\). A full-text inspection of that 2026 paper was not available through the bounded public retrieval route, so possible discussion of the monotonicity conjecture inside its body remains a residual literature risk.

## Limitations
The theorem is confined to two summands. It does not settle whether coordinatewise monotonicity holds for arbitrary \(n\) when \(0<q<2\). It does not strengthen the published \(q>2\) counterexample, and it makes no claim about joint concavity beyond distinguishing that property from monotonicity. The literature comparison cannot exclude an unindexed or inaccessible prior statement of the elementary two-summand reduction; the inaccessible full text of the 2026 concavity paper is specifically retained as a residual risk.

## References
1. E. Hillion and O. Johnson, *A proof of the Shepp-Olkin entropy monotonicity conjecture*, arXiv:1810.09791; Electronic Journal of Probability 24 (2019), paper 126, doi:10.1214/19-EJP380.
2. M. Madiman, J. Melbourne, and C. Roberto, *Bernoulli sums and Rényi entropy inequalities*, arXiv:2103.00896.
3. H. Wang, *The Sharp Rényi and Tsallis Threshold in the Shepp--Olkin Concavity Problem*, arXiv:2609.27433.

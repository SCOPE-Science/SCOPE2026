# Sharp power-moment frontier and critical risk exponent for inverse-square facility omission

## Finding
Let \(n\ge3\), and let \(C\) be the random total social cost of the Inverse-Square mechanism with \(n-1\) facilities and \(n\) distinct agent locations. Normalize by the unrestricted optimal social cost \(\delta>0\). For every real \(p>0\), the exact worst-case normalized moment is
\[
R_{n,p}:=\sup_{\mathbf x}\mathbb E[(C/\delta)^p]
=\begin{cases}
\dfrac{2-p}{2z_{n,p}^p},&0<p<2,\\[3pt]
\dfrac n2,&p=2,\\[3pt]
+\infty,&p>2,
\end{cases}
\]
where \(z_{n,p}\in(0,1)\) is the unique solution of
\[
(n-2)pz_{n,p}^{2}+4z_{n,p}^{p}=2(2-p).
\]
For \(0<p<2\), equality is attained by a line metric with nearest-neighbor-distance profile \((\delta,\delta,\delta/z_{n,p},\ldots,\delta/z_{n,p})\). For \(p=2\) the supremum is not attained by a finite distinct-location profile; for \(p>2\), every fixed finite profile has finite moment but no uniform normalized bound exists. The known \(p=1\) approximation guarantee is recovered as \(R_{n,1}=(1+\sqrt{n/2})/2\).

## Assumptions and scope
Fix a metric space \((X,d)\), integer \(n\ge3\), and pairwise distinct locations \(x_1,\ldots,x_n\). Define the nearest-neighbor distance of agent \(i\) as \(d_i:=\min_{j\ne i}d(x_i,x_j)>0\), and let \(\delta:=\min_i d_i\). The mechanism samples exactly one omitted agent with probabilities
\[
q_i=\frac{d_i^{-2}}{\sum_{j=1}^n d_j^{-2}}
\]
and opens a facility at each remaining agent location. When agent \(i\) is omitted, all other agents are served at zero cost and agent \(i\) incurs cost \(d_i\), so \(C=d_i\). Because \(n-1\) facilities can serve all but one agent, the unrestricted optimal total connection cost is \(\mathrm{OPT}=\delta\). The minimum is attained by at least two agents (the endpoints of a closest pair). The supremum ranges over all metrics and profiles satisfying these assumptions; the sharpness constructions use the real line. Identical-position reports and their zero optimal cost are outside the normalized claim.

## Proof
Write \(u_i=\delta/d_i\in(0,1]\). At least two of these values are \(1\). The normalized \(p\)-moment is exactly
\[
\mathbb E[(C/\delta)^p]
=\frac{\sum_{i=1}^n u_i^{2-p}}{\sum_{i=1}^n u_i^2}.
\tag{1}
\]
Fix \(0<p<2\) and put \(m=n-2\). Select two indices for which \(u_i=1\). For any proposed bound \(R>1\), define \(h_R(u)=u^{2-p}-Ru^2\) on \([0,1]\), with \(h_R(0)=0\). Differentiation gives \(h_R'(u)=u((2-p)u^{-p}-2R)\). Consequently \(h_R\) has the unique maximum at
\[
z_R=\left(\frac{2-p}{2R}\right)^{1/p}\in(0,1),\qquad
h_R(z_R)=\frac p2 z_R^{2-p}.
\tag{2}
\]
For arbitrary admissible \((u_i)\), the two fixed unit coordinates and the remaining \(m\) coordinates therefore satisfy
\[
\sum_{i=1}^n(u_i^{2-p}-Ru_i^2)
\le2(1-R)+m\frac p2 z_R^{2-p}.
\tag{3}
\]
The right-hand side vanishes exactly when \(R=(2-p)/(2z^p)\) and \(mpz^2+4z^p=2(2-p)\). The latter left-hand side increases strictly from zero to \(mp+4\) as \(z\) runs from zero to one, whereas the right-hand side lies strictly between zero and four. Thus there is a unique solution \(z=z_{n,p}\in(0,1)\), and \(R=(2-p)/(2z^p)>1\) because the zero equation also yields \(R-1=(mp/4)z^{2-p}>0\). Substituting this \(R\) into (3), then dividing by the positive denominator of (1), proves the universal bound. Equality in (3) forces precisely two unit coordinates and all other coordinates equal to \(z\), establishing the nearest-neighbor-distance equality profile.

Every such profile is geometrically realizable on the real line. After normalizing \(\delta=1\), place agents at \(0\), \(1\), and \(1+j/z\) for integers \(j=1,\ldots,n-2\). The first two nearest-neighbor distances equal \(1\) and the remaining \(n-2\) distances equal \(1/z\). This proves attainment for \(0<p<2\).

For \(p=2\), (1) becomes \(n/\sum_i u_i^2\). Since at least two unit coordinates exist, this is at most \(n/2\); because all \(u_i>0\) and \(n>2\), it is strictly smaller on any finite profile. The same line construction with the long consecutive gap \(L\to\infty\) gives \(u=(1,1,1/L,\ldots,1/L)\) and the sharp limiting value \(n/2\). For \(p>2\), the identical family yields
\[
\mathbb E[(C/\delta)^p]=\frac{2+(n-2)L^{p-2}}{2+(n-2)L^{-2}}\longrightarrow+\infty,
\]
proving the absence of a uniform higher-moment guarantee. Finally, solving the \(p=1\) quadratic gives \(R_{n,1}=(1+\sqrt{n/2})/2\), exactly the known mean approximation ratio.

## Verification
The standalone Python 3 script `verify.py` independently evaluates the moment formula against the sharp constants for thirteen electorate sizes and seven moment orders at 200 random metric/line/tree-like profiles per case, checks the equality constructions for all orders below two, and performs exact-rational first- and second-moment checks on further line instances. The script reports 18,718 passed checks. Its finite tests are sanity checks only: the proof above establishes the all-size, all-metric continuum of \(p\)-values. Execute with `python3 verify.py` without external dependencies.

## Relationship to prior work
Chan, Lin and Wang (2026), arXiv:2608.22484, introduced the Inverse-Square mechanism for \(n-1\) facilities, proved strategyproofness on arbitrary metrics, and established its sharp expected-social-cost ratio \((1+\sqrt{n/2})/2\). Their Section 4, especially the full proof of Theorem 3, treats the first moment \(p=1\). The present result keeps their mechanism unchanged and studies all positive moment orders: the exact interior optimizer depends on \(p\), and the qualitative critical exponent \(2\) is invisible to the first-moment result alone. Earlier work by Escoffier et al. (2011) developed inverse-distance sampling for many-facility location, a different mechanism with a different weight exponent.

## Limitations
The result concerns the moments of the aggregate total cost over a single random choice, normalized by the instance's unrestricted optimal total cost; it is not a theorem about worst-case realized cost, strategyproofness under risk-averse agents, or facilities fewer than \(n-1\). The \(p>2\) divergence is across a family of instances, not divergence within any one finite instance. The result uses the cited mechanism's existing incentive analysis without independently extending it to nonlinear agent objectives. Equivalent risk-spectrum results outside the searched literature remain possible; independent scientific validation has not been performed.

## References
1. Hau Chan, Jianan Lin and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first posted August 23, 2026, particularly Section 4 and Theorem 3. https://arxiv.org/abs/2608.22484
2. Bruno Escoffier, Laurent Gourvès, Kim Thang Nguyen, Fanny Pascual and Olivier Spanjaard, *Strategy-Proof Mechanisms for Facility Location Games with Many Facilities*, Algorithmic Decision Theory, pp. 67–81 (2011), DOI 10.1007/978-3-642-24873-3_6.

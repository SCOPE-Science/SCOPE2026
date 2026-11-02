# An exact remote-fixed-point covariance law for four Ewens triple shapes

## Finding
Let \(\Pi\) follow the Ewens distribution on \(S_n\), \(n\ge4\), with parameter \(\theta>0\). Fix consecutive positions \(i,i+1,i+2\) and another position \(j\notin\{i,i+1,i+2\}\). Set \(F_j=\mathbf1\{\Pi(j)=j\}\) and let \(U,D,P,V\) denote, respectively, the events that the three values are strictly increasing, strictly decreasing, form a peak, or form a valley. All four events partition the sample space.

Write
\[
\mathcal D=(\theta+n-4)(\theta+n-3)(\theta+n-2)(\theta+n-1)^2>0.
\]
Then, independently of the locations \(i\) and \(j\),
\[
\begin{aligned}
\operatorname{Cov}(F_j,\mathbf1_U)&=\frac{\theta^2(\theta-1)(n+2\theta-3)}{\mathcal D},\\
\operatorname{Cov}(F_j,\mathbf1_D)&=-\frac{\theta^2(\theta-1)(n-5)}{\mathcal D},\\
\operatorname{Cov}(F_j,\mathbf1_P)&=\operatorname{Cov}(F_j,\mathbf1_V)
=-\frac{\theta^2(\theta-1)(\theta+1)}{\mathcal D}.
\end{aligned}
\]
The decreasing-triple covariance vanishes identically for \(n=5\), at every \(\theta>0\), whereas the other three covariances vanish exactly when \(\theta=1\). At \(n=4\), the increasing and decreasing covariance signs agree, and for \(n\ge6\) they oppose. Peak/valley covariance always has sign opposite to \(\theta-1\).

For fixed \(\theta\ne1\) and \(n\to\infty\), increasing/decreasing covariances are of respective leading orders \(+\theta^2(\theta-1)n^{-4}\) and \(-\theta^2(\theta-1)n^{-4}\); peak and valley have leading order \(-\theta^2(\theta^2-1)n^{-5}\). Here the \(+\) and \(-\) in the first two asymptotic coefficients are algebraic signs rather than assertions of positivity for arbitrary \(\theta\).

## Assumptions and scope
Let \(S_n\) be all permutations of \([n]\). The Ewens law is \(\mathbb P_\theta(\Pi=\pi)=\theta^{c(\pi)}/\theta^{\overline n}\), where \(c(\pi)\) is the cycle count and \(\theta^{\overline n}=\prod_{r=0}^{n-1}(\theta+r)\). We assume exactly \(n\ge4\), \(\theta>0\), \(1\le i\le n-2\), and \(j\in[n]\setminus\{i,i+1,i+2\}\). Values are always distinct, so precisely one of \(U,D,P,V\) occurs. Peak means the middle value exceeds both neighbors; valley means it is smaller than both. Covariance is \(\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]\). No large-size approximation is used for the exact identities.

## Proof
**Partial-injection cycle lemma.** For any three distinct arguments \(u,v,w\) and distinct assigned images \(a,b,c\), let \(\ell\) count the directed cycles already closed by the arrows \(u\mapsto a,v\mapsto b,w\mapsto c\). Each other component of the directed partial-injection graph is a directed path, possibly a singleton. Contract each path to one vertex and remove the closed cycles. Completion to a permutation corresponds bijectively to a permutation on \(n-3\) contracted vertices, preserving the numbers of additional cycles. Since the Ewens weighted sum over \(S_m\) is \(\theta^{\overline m}\), the specified three arrows have probability
\[
\frac{\theta^{\ell}}{(\theta+n-1)(\theta+n-2)(\theta+n-3)}.
\]
This formula applies even when a specified arrow is a self-loop or when several cycles are closed.

Set \(a=\theta-1\) and \(T_3=(\theta+n-1)(\theta+n-2)(\theta+n-3)\). For the increasing and peak events respectively, sum \(\theta^{\ell}=(1+a)^{\ell}\) over all distinct ordered image triples. The following table counts \(\sum \binom{\ell}{r}\) for \(r=0,1,2,3\):

| Shape | \(r=0\) | \(r=1\) | \(r=2\) | \(r=3\) |
|---|---:|---:|---:|---:|
| Increasing | \(\binom n3\) | \(\binom n2\) | \(n\) | \(1\) |
| Peak | \(2\binom n3\) | \(n(n-2)\) | \(n-2\) | \(0\) |

Here is an explicit location-independent enumeration. Write \(u=i,v=i+1,w=i+2\). For an increasing assignment \(x<y<z\), a closed directed cycle can only be a self-loop. Counting one designated loop at \(u,v,w\) gives
\(\binom{n-u}{2}+u(n-u-1)+\binom{u+1}{2}=\binom n2\).
Counting two designated loops at \((u,v),(v,w),(u,w)\) gives \((n-u-1)+u+1=n\); all three loops occur only in the identity restriction.
For a peak assignment \(y>\max(x,z)\), the single designated cycles consist of three possible loops, two possible transpositions, and one possible three-cycle. Their counts are
\[
\sum_{b=u+1}^{n}(b-2),\quad u(u-1),\quad \sum_{b=w+1}^{n}(b-2),\quad u,\quad n-w,\quad 1,
\]
whose sum is \(n(n-2)\). Designating two disjoint cycles yields \((u-1)+(n-w)+1=n-2\): the first two terms are the loop pairs \((u,v)\) and \((u,w)\), and the final term is the loop at \(u\) jointly with the transposition \((v,w)\). No three disjoint cycles satisfy a strict peak. Thus the table holds for every \(n\) and every starting position \(i\).

It follows that the shape probabilities, independent of \(i\), are
\[
\begin{aligned}
p_U(n)&=\frac{\binom n3+a\binom n2+na^2+a^3}{T_3},\\
p_P(n)&=\frac{2\binom n3+a n(n-2)+a^2(n-2)}{T_3}.
\end{aligned}
\]
Conjugation by the reversal \(r(k)=n+1-k\) preserves cycle counts and maps peaks to valleys (at the reversed starting position), so \(p_V(n)=p_P(n)\). Partitioning the six possible relative orders gives \(p_D(n)=1-p_U(n)-2p_P(n)\).

For \(j\) outside the three specified positions, the fixed-point event has probability \(\mathbb P_\theta(F_j=1)=\theta/(\theta+n-1)\). Conditioned on \(F_j=1\), deleting \(j\) and order-relabeling the surviving indices gives an Ewens permutation of size \(n-1\). The three positions remain consecutive, so for every shape \(E\in\{U,D,P,V\}\),
\[
\operatorname{Cov}(F_j,\mathbf1_E)
=\frac{\theta}{\theta+n-1}\bigl[p_E(n-1)-p_E(n)\bigr].
\]
Substitution of the displayed rational probabilities, using \(\binom n2=n(n-1)/2\) and \(\binom n3=n(n-1)(n-2)/6\), and cancellation give exactly the four factorizations in the finding. Every factor of \(\mathcal D\) is positive in the stated domain. This proves all strict sign and zero classifications. Dividing the numerators and denominator by powers of \(n\) proves the stated asymptotic orders.

## Verification
The accompanying `verify.py` enumerates all \(46{,}224\) permutations in sizes \(4\) through \(8\) (each size once), weights them exactly at \(\theta\in\{\tfrac12,1,2,3\}\), and tests all consecutive triple starts, all remote fixed-point locations, all four shape probabilities and all four covariances using exact rational arithmetic. It passes \(1{,}720\) assertions. Separately, the cycle-table identities were checked by exact partial-injection enumeration for all \(4\le n\le10\) and every triple start; symbolic cancellation of the three independent covariance formulas was checked algebraically. The unrestricted theorem is established by the proof, not by these finite tests.

Reproduce the embedded verifier with `python3 verify.py` using the standard library. Computational cases do not establish uniqueness, infinite-size conclusions, or publication priority by themselves.

## Relationship to prior work
Galganov and Ilienko [1] study Ewens and more general cycle-weighted permutations, proving a Poisson point-process limit for cycles and results on the locations of short cycles. Their cycle probabilities motivate the conditioning step here, but their results do not give the displayed covariance with adjacent-order shapes. Fulman, Kim and Lee [2] study the global number of peaks in fixed conjugacy classes, using an exact generating function for peak counts and cycle types; this is distinct from conditioning an individual out-of-window fixed-point indicator on a specified order shape. Pinsky and Schickentanz [3] derive pairwise inversion probabilities under Ewens sampling and study inversion counts with prescribed fixed-point totals, but their pair-event formulas do not directly determine the joint three-value peak or valley probability. Their work provides a close comparison, not a source date for this result. Exact formulas for cycle/descent-set enumerators could in principle imply portions of the present calculation after additional specializations; priority remains an identified risk.

## Limitations
The theorem covers ordinary Ewens weights, consecutive windows of exactly three positions, and one fixed point outside the window. It does not claim independence for \(\theta\ne1\), nor any statement about nonconsecutive triples, position-dependent cycle weights, or joint distributions of multiple windows. The self-review is not independent validation. Existing general permutation generating functions may encode some formulas implicitly, so historical priority is provisional.

## References
[1] O. Galganov and A. Ilienko, *Short cycles of random permutations with cycle weights: point processes approach*, arXiv:2309.10721v1 (first public 2023-09-19), https://arxiv.org/html/2309.10721v1.

[2] J. Fulman, G. B. Kim and S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class of \(S_n\)*, arXiv:1902.00978v1 (2019), https://arxiv.org/html/1902.00978v1.

[3] R. G. Pinsky and D. T. Schickentanz, *Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points*, arXiv:2510.20654v2 (2025), https://arxiv.org/html/2510.20654v2.

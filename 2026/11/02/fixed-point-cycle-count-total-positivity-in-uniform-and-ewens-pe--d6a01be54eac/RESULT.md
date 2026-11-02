# Fixed-point–cycle-count total positivity in uniform and Ewens permutations

## Finding
For a permutation of \(n\ge 2\) labels let \(K\) be its number of disjoint cycles, and \(F\) its number of fixed points, that is, cycles of length one. Under the uniform distribution the joint enumeration \(w_n(k,f)\) is **totally positive of order two**:
\[
w_n(k,f)w_n(\ell,g)-w_n(k,g)w_n(\ell,f)\ge0
\quad\text{whenever }1\le k<\ell\le n,\ 0\le f<g\le n.
\]
The inequality is strict whenever its subtracted product is positive. Therefore \(F\), conditioned on \(K=k\), is nondecreasing in the monotone likelihood-ratio order as \(k\) increases. For every pair of strictly increasing functions \(h\) and \(q\) on the finite supports, \(\operatorname{Cov}(h(K),q(F))>0\). All these statements hold for the Ewens permutation law with any parameter \(\theta>0\), where a permutation receives weight proportional to \(\theta^{K}\). In fact, the conditional distribution of \(F\) given \(K\) does not depend on \(\theta\).

## Assumptions and scope
All assertions are finite-sample and hold for every integer \(n\ge2\). The Ewens parameter is any real \(\theta>0\). The likelihood-ratio order on distributions supported on integer intervals is defined by nonnegative cross-products \(p_k(f)p_\ell(g)-p_k(g)p_\ell(f)\) for \(k<\ell\) and \(f<g\), including zeros at the ends of the supports. Strict association refers to strictly increasing real functions on the attained values, not arbitrary constant transforms.

Let \(d(r,a)\) count fixed-point-free permutations of \(r\) labeled elements having \(a\) cycles. Extend by zero for impossible indices; take \(d(0,0)=1\), \(d(1,a)=0\). The known enumeration by selecting fixed points is
\[
w_n(k,f)=\binom nf\,d(n-f,k-f).
\]
For \(k<n\), positive entries have \(\max(0,2k-n)\le f\le k-1\), an integer interval; for \(k=n\), only \(f=n\) is positive. For \(k<\ell\) and \(f<g\), positivity of the crossed corners \(w_n(k,g)\) and \(w_n(\ell,f)\) forces every entry in the intervening rectangle to be positive.

## Proof
**1. Derangement cycle recurrence and strict log-concavity.** Removing the label \(r\) from a derangement either removes it from a cycle of length at least three (with \(r-1\) insertion positions in a smaller derangement), or removes its entire two-cycle (with \(r-1\) choices of partner). Thus, for \(r\ge2\),
\[
d(r,a)=(r-1)\,[d(r-1,a)+d(r-2,a-1)]. \tag{1}
\]
Put \(D_r(z)=\sum_a d(r,a)z^a\). For \(r\ge2\), write
\[
D_r(z)=(r-1)!\,zQ_{r-2}(z),
\quad Q_0(z)=Q_1(z)=1,
\quad Q_m(z)=Q_{m-1}(z)+\frac zmQ_{m-2}(z)\ (m\ge2).
\]
(The initial values correspond to \(D_2(z)=z\) and \(D_3(z)=2z\).) Define \(P_m(t)=t^mQ_m(-t^{-2})\), interpreted as a polynomial after cancellation. Its recurrence is \(P_0=1\), \(P_1=t\), and
\[
P_m(t)=tP_{m-1}(t)-\frac1mP_{m-2}(t),\qquad m\ge2.
\]
This is the characteristic-polynomial recurrence for a real symmetric \(m\)-by-\(m\) tridiagonal matrix with zero diagonal and positive adjacent entries \(1/\sqrt2,1/\sqrt3,\ldots,1/\sqrt m\). Its eigenvalues are real, simple and symmetric about zero. Hence every zero of \(Q_m\) is real and strictly negative. Consequently every \(D_r\) is real-rooted with nonnegative coefficients, implying, by Newton's inequalities, log-concavity of the sequence \(d(r,a)\). More precisely,
\[
L_{r,a}:=d(r,a)^2-d(r,a-1)d(r,a+1)\ge0,
\]
strictly whenever \(d(r,a)>0\). This includes endpoint indices because out-of-range coefficients are zero.

**2. Two coupled positivity recurrences.** Define
\[
A_{r,a}=d(r-1,a-1)d(r,a)-d(r-1,a)d(r,a-1),
\]
\[
B_{r,a}=d(r,a)d(r-1,a)-d(r,a+1)d(r-1,a-1).
\]
Applying (1), expanding both determinants, and collecting terms gives the exact identities, for \(r\ge3\),
\[
A_{r,a}=(r-1)B_{r-1,a-1},\qquad
B_{r,a}=(r-1)(L_{r-1,a}+A_{r-1,a}).\tag{2}
\]
Both arrays vanish for \(r=2\). Simultaneous induction using \(L_{r,a}\ge0\) gives \(A_{r,a},B_{r,a}\ge0\) for all indices. Moreover \(B_{r,a}>0\) whenever \(d(r-1,a)>0\), by strictness of \(L_{r-1,a}\).

**3. Adjacent and arbitrary minors.** Set \(r=n-f\), \(a=k-f\). Direct substitution into the exact joint-count formula yields
\[
\begin{aligned}
&w_n(k,f)w_n(k+1,f+1)-w_n(k,f+1)w_n(k+1,f)\\
&=\binom nf\binom n{f+1}B_{r,a}\ge0.
\end{aligned}\tag{3}
\]
Whenever all four factors are positive, the first product is strictly greater than the second by the preceding paragraph. For arbitrary \(k<\ell\) and \(f<g\), if the subtracted product vanishes, the desired nonnegative inequality is immediate. Otherwise the two opposite-corner entries \(w_n(k,g)\) and \(w_n(\ell,f)\) are positive. The interval-support formula above ensures that every entry in their rectangular span is positive. Divide (3) by its positive factors and multiply the resulting adjacent ratio inequalities along rows and columns: \(w_n(k,f)w_n(\ell,g)>w_n(k,g)w_n(\ell,f)\). This proves the full statement, including its strictness clause.

**4. Distributional consequences.** Dividing any row by its positive sum preserves all cross-product signs, so \(F\mid K=k\) increases in likelihood-ratio order. This implies increasing conditional expectations for every increasing transform of \(F\). Since the rows \(K=1\) and \(K=n\) have deterministically \(F=0\) and \(F=n\), and both occur with positive probability, the covariance of any two strictly increasing transforms is strictly positive. Under Ewens weights \(\theta^K\), each row is multiplied by \(\theta^k\); hence every minor is multiplied by \(\theta^{k+\ell}>0\), and the conditional law \(F\mid K=k\) is unchanged. No limiting argument is needed.

As a consistency check, the familiar first-moment identity is \(\operatorname{Cov}_\theta(K,F)=n\theta(n-1)/(\theta+n-1)^2\), positive for \(n\ge2\). This scalar identity and the joint enumeration are not themselves asserted to be novel.

## Verification
Run \(\texttt{python3 verify.py}\) (Python standard library only) after extracting the included file. Exact arithmetic tests 867,572 assertions: independent exhaustive generation of all permutations through \(n=8\), direct checks of every two-by-two joint-count minor through \(n=27\), recurrence and positivity identities through \(n=160\), and the uniform-law covariance identity. These finite computations are regression checks, **not** a proof for unbounded \(n\); steps 1–4 provide that proof.

## Relationship to prior work
Diaconis, Evans and Graham (Berkeley technical report 822, public August 1, 2013; later arXiv:1308.5459) analyze fixed points, succession events and Chinese-restaurant constructions under uniform permutations, not the joint fixed-point/total-cycle TP2 matrix. Ma (2010) studies roots of \(r\)-associated Stirling cycle polynomials, including the derangement-cycle case; that real-rootedness is a predecessor of step 1, not the cross-\(r\) minor inequalities (2)–(3). Mukherjee (2015) proves asymptotic Poisson laws for fixed-length cycle counts under broader permutation models, not this exact finite-\(n\) conditional total-positive ordering. Deb and Sokal (2025) study total positivity of higher-order Stirling cycle and subset triangles and their row/Hankel transforms; their matrices differ from the two-statistic joint-count matrix \(\binom nf d(n-f,k-f)\). The new assessed statement is the full joint TP2 ordering and its all-\(\theta\) conditional consequences, not classical derangement enumerations, scalar covariances or row log-concavity.

## Limitations
The result applies to uniform and Ewens cycle-weighted measures, not arbitrary distributions on permutations, and concerns total cycles and singleton cycles only. The historical-priority assessment is based on specifically inspected sources and searches; an unlocated broader total-positivity theorem could imply the statement. No external independent audit or verification has occurred.

## References
- P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822, dated 2013-08-01, https://statistics.berkeley.edu/tech-reports/822 ; manuscript https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf ; arXiv:1308.5459.
- S.-M. Ma, *Real zeros and the signless r-associated Stirling numbers of the first kind*, Ars Combinatoria 94 (2010), 229–234, https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-23.pdf .
- S. Mukherjee, *Fixed points and cycle structure of random permutations*, arXiv:1509.04552 (first posted 2015-09-15), https://arxiv.org/abs/1509.04552 .
- B. Deb and A. D. Sokal, *Higher-order Stirling cycle and subset triangles: Total positivity, continued fractions and real-rootedness*, arXiv:2507.18959 (first posted 2025-07-25), https://arxiv.org/html/2507.18959v1 .

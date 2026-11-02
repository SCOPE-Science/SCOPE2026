# Birthday-to-coverage negative regression with sharp covariance decay

## Finding

Let \(m\ge 2\) be an integer and \(X_1,X_2,\ldots\) be independent, uniformly sampled symbols from an alphabet of size \(m\). Define the **birthday time** \(B_m\) to be the first draw on which any symbol is repeated, and the **coverage time** \(C_m\) to be the first draw by which all \(m\) symbols have appeared. Draws are numbered beginning with one.

For each \(2\le t\le m\), let \(G_{j,m}\), \(1\le j\le m-t+1\), be independent geometric random variables on \(\{1,2,\ldots\}\), with \(\Pr(G_{j,m}=q)=(1-j/m)^{q-1}j/m\). Then
\[
C_m\mid\{B_m=t\}\ \overset{d}=\ t+\sum_{j=1}^{m-t+1}G_{j,m},
\qquad
C_m\mid\{B_m=m+1\}=m\ \text{a.s.}
\]
For every consecutive pair of possible birthday times, these conditional coverage-time laws are **strictly decreasing in usual stochastic order**:
\[
C_m\mid\{B_m=t+1\}\ <_{\mathrm{st}}\ C_m\mid\{B_m=t\},
\qquad 2\le t\le m,
\]
where strict means stochastic domination and a strict survival-probability inequality at at least one threshold. Consequently \((B_m,C_m)\) is negatively quadrant dependent; in particular, every pair of increasing functions with existing expectations has nonpositive covariance, and
\[
\operatorname{Cov}(B_m,C_m)<0\qquad(m\ge2).
\]

The finite-sample covariance is explicitly computable. Put
\[
p_{m,t}=\frac{t-1}{m}\prod_{j=0}^{t-2}\left(1-\frac jm\right)
\quad(2\le t\le m),\qquad
p_{m,m+1}=\frac{m!}{m^m},
\]
\[
g_m(t)=t+mH_{m-t+1}\quad(2\le t\le m),\qquad g_m(m+1)=m,
\quad H_k=\sum_{j=1}^k\frac1j.
\]
With \(\mu_m=\sum_{t=2}^{m+1}tp_{m,t}\), one has
\[
\operatorname{Cov}(B_m,C_m)
=\sum_{t=2}^{m+1}(t-\mu_m)p_{m,t}g_m(t).
\]
The dependence has the following sharp asymptotics:
\[
\boxed{\lim_{m\to\infty}\frac{\operatorname{Cov}(B_m,C_m)}{\sqrt m}
=-\sqrt{\frac\pi8}},
\qquad
\boxed{\lim_{m\to\infty}m\operatorname{Corr}(B_m,C_m)
=-\sqrt{\frac{3}{2\pi(4-\pi)}}}.
\]

## Assumptions and scope

The alphabet is finite, the sampling probabilities are exactly uniform, and successive draws are independent. Both stopping times are defined from the same infinite sequence. The statement includes the exceptional event \(B_m=m+1\): all \(m\) symbols are first collected at time \(m\) and a repeat necessarily occurs on the next draw. The result does not assert the same ordering for nonuniform sampling or for collectors using independent sequences.

## Proof

**1. Conditional representation.** On \(B_m=t\), \(2\le t\le m\), the first \(t-1\) sampled symbols are distinct and the \(t\)-th is a repeat, leaving precisely \(m-t+1\) unseen types. Future draws remain independent and uniform. If \(k\) types remain unseen, the waiting time until the next new type is geometric with success probability \(k/m\). Repeating this argument at the successive discovery times yields the independent sum in the finding. On \(B_m=m+1\), all types were collected on draw \(m\), proving the exceptional clause.

**2. Stochastic ordering.** For \(2\le t<m\), use the same geometric variables for the two laws and couple them as
\[
C^{(t)}=t+G_{m-t+1,m}+\sum_{j=1}^{m-t}G_{j,m},
\qquad
C^{(t+1)}=t+1+\sum_{j=1}^{m-t}G_{j,m}.
\]
Their difference is \(G_{m-t+1,m}-1\ge0\), and it is positive with positive probability because \((m-t+1)/m<1\). For \(t=m\), couple \(m+G_{1,m}\) with the constant \(m\). Thus all successive conditional distributions have the asserted strict stochastic order.

For every increasing bounded function \(h\), the conditional expectation \(b\mapsto\mathbb E[h(C_m)\mid B_m=b]\) is nonincreasing. For every increasing bounded \(f\), the covariance of \(f(B_m)\) with this nonincreasing function is nonpositive, by the independent-copy identity \(2\operatorname{Cov}(U,V)=\mathbb E[(U-U')(V-V')]\). Apply this to indicator functions of upper tails to obtain negative quadrant dependence. Truncation extends the assertion to increasing integrable transforms with an existing product moment. For \(f(b)=b\), \(h(c)=c\), strict ordering and positive mass at every \(b\in\{2,\ldots,m+1\}\) yield strict negative covariance.

**3. Exact means.** The birthday mass follows by requiring the first \(t-1\) draws to be distinct followed by a repeat, with the final all-distinct case handled separately. The geometric means give \(g_m(t)\) as displayed. Conditioning on \(B_m\) gives the finite-sum covariance formula. As a boundary check, the covariances at \(m=2,3,4\) are respectively \(-1/2,-8/9,-37/32\).

**4. Sharp asymptotic covariance.** The survival function is
\[
\Pr(B_m>k)=\prod_{j=0}^{k-1}\left(1-\frac jm\right),\qquad 0\le k\le m.
\]
Thus \(B_m/\sqrt m\) converges to a Rayleigh variable \(R\) with tail \(e^{-x^2/2}\). The product bound \(\Pr(B_m>k)\le\exp[-k(k-1)/(2m)]\) implies uniform boundedness of each fixed rescaled moment, so convergence extends to moments.

Define, for \(2\le b\le m+1\),
\[
D_m(b)=\sum_{j=1}^{b-2}\frac{j}{m-j},\qquad
J_m(b)=\mathbf1_{\{b=m+1\}}.
\]
Direct telescoping of the conditional means, including the endpoint correction, yields
\[
g_m(b)=mH_m+1-D_m(b)-J_m(b).
\]
For \(b\le m/2\),
\[
D_m(b)=\frac{(b-1)(b-2)}{2m}+O\left(\frac{b^3}{m^2}\right).
\]
For \(b>m/2\) the birthday-tail bound is exponentially small in \(m\), while \(D_m(b)=O(m\log m)\). The above expansion and tail control therefore give
\[
\mathbb E D_m(B_m)\to\frac12\mathbb E[R^2],
\qquad
\frac{\mathbb E[B_m D_m(B_m)]}{\sqrt m}\to\frac12\mathbb E[R^3].
\]
The contribution of \(J_m(B_m)\) to the covariance, divided by \(\sqrt m\), vanishes because \(\Pr(B_m=m+1)=m!/m^m\). Since \(\mathbb E[R]=\sqrt{\pi/2}\), \(\mathbb E[R^2]=2\), and \(\math ER^3=3\sqrt{\pi/2}\), the covariance limit is \(-\sqrt{\pi/8}\).

Finally \(\operatorname{Var}(B_m)/m\to(4-\pi)/2\) by Rayleigh moment convergence. The independent geometric discovery increments give the exact coverage-time variance
\[
\operatorname{Var}(C_m)=m^2\sum_{j=1}^m\frac1{j^2}-mH_m,
\]
so \(\operatorname{Var}(C_m)/m^2\to\pi^2/6\). Division proves the correlation limit.

## Verification

The included standalone `verify_coupon.py` uses exact rational arithmetic to check the birthday mass function, occupancy-chain first-step recursions, conditional mean monotonicity, covariance signs and several small exact values. It independently computes finite-horizon conditional coverage-time CDFs by a dynamic-programming Markov recursion and checks stochastic ordering for all consecutive birthday times at sizes \(2\le m\le8\). Three larger-size numerical diagnostics compare the normalized covariance with the proved limit. The script passed 3,493 assertions. These finite calculations are not substituted for the preceding infinite-parameter proof.

## Relationship to prior work

Flajolet and Sedgewick's *Analytic Combinatorics* (2009, Chapter II, Examples II.10--II.11) treats the first birthday collision and coupon completion in the same iid-word framework and gives the classical birthday Rayleigh law and coverage-time methods. Myers and Wilf (2003) treat coupon-collector waiting times, two independent collectors, repeated collections and final singleton counts. Those published descriptions and inspected primary-text sections do not state the present conditional stochastic ordering between the two stopping times from **one** sampling stream or the displayed sharp mixed covariance rate. The individual stopping-time marginal distributions and geometric phase decomposition are classical and are not presented as new.

## Limitations

Only uniform iid draws are covered. Negative quadrant dependence does not imply full negative association of arbitrary multivariate events. The proof is analytic; numerical calculations provide finite sanity checks. Literature searches and available original passages do not establish absolute historical priority: an unlocated classical joint birthday--coverage theorem or an equivalent result implicit in a broader occupancy-process treatment remains possible. The full text of the large 2009 textbook was not exhaustively reviewed. No independent audit has been performed.

## References

1. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1 (public preprint 2003-04-16), https://arxiv.org/abs/math/0304229 .
2. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapter II, Examples II.10--II.11, ISBN 9780521898065, https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html .

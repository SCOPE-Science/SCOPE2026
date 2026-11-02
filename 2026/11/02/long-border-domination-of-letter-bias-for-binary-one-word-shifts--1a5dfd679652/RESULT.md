# Long-border domination of letter bias for binary one-word shifts

## Finding

Let \(w\) be a binary word beginning and ending with \(11\). For each nonempty border \(b\) of \(w\), including \(w\) itself, write \(\delta(b)=2|b|_1-|b|\). Assume that \(\delta(b)\le0\) for every border of length at least three, and that at least one such border has \(\delta(b)<0\). If \(\rho(w)\) denotes the limiting mean proportion of ones among all finite binary words avoiding \(w\), then

\[\boxed{\rho(w)>\tfrac12.}\]

In particular, this conclusion permits **arbitrarily many** zero-heavy borders competing with the two short one-heavy borders. For \(u=1100000011\), every \(w=u^r\) with integer \(r\ge1\) satisfies the hypotheses and has exactly \(r\) negative-imbalance borders.

## Assumptions and scope

A border of \(w\) is a nonempty prefix that is also a suffix; \(w\) is included. The hypothesis implies \(|w|\ge9\), since a negative-imbalance border starting and ending in \(11\) must have at least nine symbols. Define \(\Omega_n(w)\) to be the set of words of length \(n\) over \(\{0,1\}\) that have no occurrence of \(w\) as a contiguous factor, and set

\[\rho(w)=\lim_{n\to\infty}\frac{\sum_{v\in\Omega_n(w)}|v|_1}{n|\Omega_n(w)|}.\]

Existence of the limit follows from the primitive finite-state presentation proved below. The statement does not concern Bernoulli stopping-time letter frequencies, forbidding multiple words, or generalizations without the boundary condition \(11\).

## Proof

**1. Primitivity and an entropy floor.** Put \(k=|w|\) and construct the de Bruijn graph on all binary \((k-1)\)-blocks, deleting the unique edge labeled by the forbidden \(k\)-block \(w\). To reach any target vertex \(v\) from any vertex, first append \(k-1\) zeros and then append the symbols of \(v\). During the first stage each new \(k\)-block ends in zero, whereas \(w\) ends in one; during the second, each new \(k\)-block begins in zero, whereas \(w\) begins in one. This is an admissible path. The all-zero state has a loop, hence the graph is primitive.

Its Perron eigenvalue \(\lambda\) is the entropy growth rate of the avoiding language. Since any word avoiding \(11\) automatically avoids \(w\), \(\lambda\ge\varphi=(1+\sqrt5)/2\). On the other hand, splitting a word into disjoint blocks of length \(k\) gives \(\lambda\le(2^k-1)^{1/k}<2\). Thus \(\varphi\le\lambda<2\), and the dominant pole of the avoidance generating function is simple and positive.

**2. An exact border identity for the bias.** Let \(\mathcal B(w)\) be the nonempty borders and set

\[B(X,Y)=\sum_{b\in\mathcal B(w)}X^{|b|}Y^{|b|_1},\qquad F(x,y)=1-x(1+y)+B(x^{-1},y^{-1})^{-1}.\]

The standard weighted border generating-function identity gives \(\sum_{n,v\in\Omega_n(w)}x^ny^{|v|_1}=1/F(x,y)\). Put \(x_0=\lambda^{-1}\). Analytic differentiation of the simple dominant pole shows

\[\rho(w)=\frac{F_y(x_0,1)}{x_0F_x(x_0,1)}.\]

Write \(Q=\sum_{b}\lambda^{|b|}\), \(S=\sum_b |b|\lambda^{|b|}\), and \(T=\sum_b|b|_1\lambda^{|b|}\). Then

\[F_y(x_0,1)=-x_0+\frac{T}{Q^2},\qquad x_0F_x(x_0,1)=-2x_0+\frac{S}{Q^2}.\]

The denominator \(x_0F_x(x_0,1)\) is strictly negative: \(1/F(x,1)\) has positive coefficients and a simple positive pole at \(x_0\). Consequently, with \(E=\sum_{b\in\mathcal B(w)}\delta(b)\lambda^{|b|}\),

\[\rho(w)-\tfrac12=\frac{E}{2Q^2x_0F_x(x_0,1)}.\]

Thus the sign of \(\rho(w)-1/2\) is **opposite** to the sign of \(E\).

**3. A uniform long-border dominance estimate.** Because \(w\) begins and ends in \(11\), its borders of length one and two are exactly \(1\) and \(11\), with imbalances \(+1\) and \(+2\). Every longer border has nonpositive imbalance by hypothesis. Any negatively imbalanced border \(b\) begins and ends in \(11\); hence it has at least four ones, so \(\delta(b)<0\) forces \(|b|\ge9\). Since at least one such border exists and all negative imbalances are negative integers,

\[E\le\lambda+2\lambda^2-\lambda^9.\]

For \(\lambda\ge\varphi\), the identity \(\varphi^3=1+2\varphi\), monotonicity of \(t^3-2t-1\) on \([\varphi,\infty)\), and \(\lambda>1\) imply \(\lambda^4>1+2\lambda\). Hence \(\lambda^9\ge\lambda^5>\lambda+2\lambda^2\). Therefore \(E<0\), and the border identity proves \(\rho(w)>1/2\).

**4. Arbitrarily many conflicting borders.** For \(u=11\,0^6\,11\), the word \(u^r\) has precisely the border lengths \(1,2,10,20,\ldots,10r\). Indeed, a shared prefix-suffix of length at least three must begin with \(110\). Such an occurrence in \(u^r\) starts only at the beginning of one of its \(r\) ten-symbol blocks, giving a border length divisible by ten. The imbalance is \(+1\) at length one, \(+2\) at length two, and \(-2j\) at length \(10j\). The hypotheses hold for every \(r\ge1\), with an unbounded number of negative borders. This proves the final assertion.

## Verification

The bundled standard-library program `verify_long_border.py` independently constructs self-border lists, enumerates all candidate words of length at most sixteen with the prescribed prefix and suffix, and tests the exact border-sign criterion at the golden-ratio bound. It found 629 eligible words, all satisfying the strict sign inequality. It also checks the predicted border lists for \(u^r\) at \(1\le r\le8\) and, using 100-digit decimal bisection on the exact border-polynomial equation, confirms \(\rho(u^r)>1/2\) in those eight cases. Its output is in `verify_long_border.log`. These finite checks only corroborate the proof; they are not an infinite certificate.

## Relationship to prior work

Bóna, Maga and Richey [1], first public June 4, 2026, establish the weighted border generating function, prove balanced borders imply \(\rho=1/2\), and obtain strict sign conclusions when all border imbalances have one sign. They explicitly formulate the mixed-sign cancellation question as Conjecture 6.1. The present theorem treats a mixed-sign region with arbitrarily many negative-imbalance borders using the entropy floor inherited from the golden-mean subshift. The two-sign injection theorem from [1] does not apply, because the borders \(1\) and \(11\) are positive while longer borders are negative. Chandgotia, Marcus, Richey and Wu [2] study one-forbidden-word shifts, border autocorrelations and conjugacy rather than this signed letter-frequency criterion.

## Limitations

This proves a sufficient sign condition, not the full converse of the balanced-border conjecture. It does not claim the same result for positive imbalanced borders of length three or greater, for arbitrary negative and positive interlacing, or for the stopping-time frequency statistic. Priority remains subject to earlier work not found in the searched sources.

## References

[1] M. Bóna, B. Maga and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655v2 (initial release June 4, 2026), Sections 2, 3 and 6. https://arxiv.org/html/2606.06655v2

[2] N. Chandgotia, B. Marcus, J. Richey and C. Wu, *Shifts of Finite Type Obtained by Forbidding a Single Pattern*, arXiv:2409.09024v1, Sections 2–4 and 6. https://arxiv.org/html/2409.09024v1

# Monotone inversion profiles and a square-root fugacity crossover for random involutions

## Finding
For every integer \(n\ge 2\), write \(\mathcal I_{n,m}\) for the involutions of \(\{1,\ldots,n\}\) having exactly \(m\) transpositions, where \(0\le m\le\lfloor n/2\rfloor\). Write \(J(\pi)\) for the usual inversion count and \(F(\pi)\) for the number of fixed points.

**Theorem (monotone coupling and density crossover).** One can place uniformly distributed \(\Pi_{n,m}\in\mathcal I_{n,m}\), for every admissible \(m\), on one probability space so that
\[
J(\Pi_{n,0})<J(\Pi_{n,1})<\cdots<J(\Pi_{n,\lfloor n/2\rfloor})
\quad\text{almost surely}.
\]
In particular, if \(\Pi_{n,\theta}\) has probability proportional to \(\theta^{F(\pi)}\) for \(\theta>0\), then \(J(\Pi_{n,\theta})\) is decreasing in \(\theta\) in usual stochastic order, strictly in expectation. For every \(n\ge2\),
\[
\operatorname{Cov}_{\theta}(F,J)<0.
\]

Let \(\theta_n>0\) and \(\theta_n/\sqrt n\to a\) in the extended range \([0,\infty]\). Define \(s(0)=0\), \(s(\infty)=1\), and, for \(0<a<\infty\), let \(s(a)\) be the unique number in \((0,1)\) with \(s(a)^2=a^2(1-s(a))\). Then
\[
\frac{F(\Pi_{n,\theta_n})}{n}\xrightarrow{\mathbb P}s(a),
\qquad
\frac{J(\Pi_{n,\theta_n})}{n^2}\xrightarrow{\mathbb P}
\frac{(1-s(a))(3+s(a))}{12}.
\]
The last limit is strictly decreasing and continuous in \(a\), from \(1/4\) to \(0\). Hence \(\theta_n\asymp\sqrt n\) is precisely the scale with a nonconstant limiting inversion density.

## Assumptions and scope
An involution is a permutation \(\pi\) satisfying \(\pi^2=\mathrm{id}\). Its disjoint cycles are singletons and unordered pairs. The inversion count is \(J(\pi)=\#\{(i,j):1\le i<j\le n,\ \pi(i)>\pi(j)\}\). The law at fixed \(m\) is uniform over all partial matchings with \(m\) pairs. At fugacity \(\theta>0\), every involution receives weight \(\theta^{F(\pi)}\); this is *not* the Ewens distribution on all permutations. Both endpoints \(a=0\) and \(a=\infty\) concern limits of positive fugacities and are included. No uniqueness of any finite-dimensional distributional representation is asserted.

## Proof
**1. A strictly increasing insertion coupling.** Begin with the identity permutation. Given a partial matching with \(m\) pairs, choose uniformly one unordered pair \(a<b\) from its \(n-2m\) unpaired vertices and join them. For an involution \(\pi\) fixing \(a,b\), let \(\pi'\) be the result of joining them. For every index outside the interval \((a,b)\), the changes in pairs of inversion indicators cancel. Within that interval, precisely those indices \(c\) satisfying \(a<\pi(c)<b\) contribute two new inversions; the new pair \((a,b)\) contributes one. Thus the exact identity is
\[
J(\pi')-J(\pi)=1+2\#\{c:a<c<b,\ a<\pi(c)<b\}\ge1.
\]
A partial matching with \(m\) pairs has \(\binom{n-2m}{2}\) possible extensions, and every partial matching with \(m+1\) pairs has exactly \(m+1\) predecessors obtained by removing one pair. Hence uniformity propagates at each step. This proves simultaneous uniform marginals and strict pathwise increase. At fugacity \(\theta\), the mixture weight for \(m\) is proportional to \(\theta^{n-2m}\#\mathcal I_{n,m}\). These weights form a monotone likelihood-ratio family decreasing in \(m\) as \(\theta\) increases. Coupling the indices by common quantiles, then using the insertion chain, proves the stochastic order. Strict expected decrease follows because all admissible classes have positive weight and adjacent means differ strictly.

**2. Conditional inversion mean.** Fix \(m\) pairs and \(f=n-2m\) fixed vertices. Each transposition contributes one internal inversion. An unordered pair of transpositions contributes an average of two additional inversions: among the three equiprobable pairings of four ordered endpoints, the additional counts are \(0,2,4\). A transposition and a fixed point contribute two inversions exactly when the fixed point lies between the endpoints, an event of probability \(1/3\). Therefore
\[
\mathbb E[J\mid F=f]=m+2\binom m2+\frac{2mf}{3}
=m^2+\frac{2mf}{3}
=\frac{(n-f)(3n+f)}{12}.
\]
This is a consequence of earlier full inversion enumerators and is **not separately claimed to be new**. Because this expression is strictly decreasing in \(f\), and the weighted law of \(F\) has at least two support points for \(n\ge2\), the law of total covariance yields \(\operatorname{Cov}(F,J)=\operatorname{Cov}(F,\mathbb E[J\mid F])<0\).

**3. Fixed-point concentration at variable fugacity.** For admissible \(f\equiv n\pmod 2\), the total weight of involutions with \(f\) fixed points is
\[
w_n(f)=\frac{n!\,\theta_n^f}{f!\,2^{(n-f)/2}((n-f)/2)!},
\quad
\frac{w_n(f+2)}{w_n(f)}=
\frac{\theta_n^2(n-f)}{(f+1)(f+2)}.
\]
The ratio decreases strictly in \(f\). If \(0<a<\infty\), its limiting value along \(f/n\to t\in(0,1)\) is \(a^2(1-t)/t^2\), which crosses one exactly at \(t=s(a)\). For any fixed \(\varepsilon>0\), the successive ratios are uniformly bounded away from one on both sides of the interval \((s(a)-\varepsilon,s(a)+\varepsilon)\), away from endpoints. Comparing the at-least-linearly-many factors between either tail and the mode gives exponentially small normalized tail weights, proving \(F/n\to s(a)\) in probability. If \(a=0\), the ratios are eventually less than a fixed number below one for every \(f\ge\varepsilon n\); if \(a=\infty\), they are eventually greater than a fixed number above one whenever \(f\le(1-\varepsilon)n\). The same geometric ratio argument proves convergence to the respective endpoints.

**4. Uniform conditional concentration of inversions.** Generate a uniform \(m\)-pair matching by taking a uniformly random ordering of all \(n\) labels, pairing positions \((1,2),(3,4),\ldots,(2m-1,2m)\), and leaving the remaining labels fixed. Swapping any two entries of that ordering changes the resulting involution at no more than four arguments. Since changing one argument can alter at most \(n-1\) inversion comparisons, this operation changes \(J\) by at most \(4(n-1)\). Reveal the random ordering successively; swapping the alternative next entries gives a coupling of conditional completions. The Doob martingale-difference bound implies, uniformly in \(m\),
\[
\operatorname{Var}(J\mid m)\le16n^3.
\]
Consequently, \(\mathbb P(|J-\mathbb E[J\mid F]|>\varepsilon n^2)\le16/(\varepsilon^2 n)\) for every \(\varepsilon>0\). Combining this with the conditional mean formula and convergence of \(F/n\) proves the stated limit of \(J/n^2\). The unique positive solution of the quadratic is \(s(a)=(\sqrt{a^4+4a^2}-a^2)/2\); implicit differentiation shows it increases strictly. The density \((1-s)(3+s)/12\) decreases strictly in \(s\), completing the proof.

## Verification
The standalone standard-library script `verify.py` exhaustively generates the \(13{,}230\) involutions at orders \(2\) through \(10\). It checks the insertion identity for \(45{,}612\) admissible transitions, conditional inversion means as exact rational numbers, all distributional tail inequalities over adjacent pair counts, and \(36\) exact negative-covariance cases at positive rational fugacities. It also numerically checks the two endpoint regimes and four interior crossover parameters using exactly computed finite-weight expectations at order \(5{,}000\). Running `python3 verify.py` returns `VERIFY_OK`. These finite checks are not the proof of the infinite assertions.

## Relationship to prior work
Désarménien's 1982 \(q\)-Hermite recurrence already enumerates involutions jointly by fixed points and inversions; it is explicitly stated and discussed in Dukes (2004), section 2.3. Hart and Rowley (2014), Theorem 1.1, give the exact inversion-length generating polynomial separately for every conjugacy class of involutions. Those enumerators **already encode the complete finite distributions**, and this finding does not claim a new counting formula or distribution table. What is established here is a pathwise strict coupling across *all* transposition classes, the resulting stochastic monotonicity under arbitrary positive fixed-point bias, and a probabilistic law of large numbers with an explicit square-root fugacity crossover. These conclusions are not stated in the inspected source sections. Lugo (2009), section 6, treats partial matchings with prescribed fixed points in a different composition/cycle setting; it supplies contextual probability models, not inversion ordering.

## Limitations
The law-of-large-numbers statement specifies only the inversion density, not a central or local limit theorem, fluctuation variance, or uniform rates in a moving crossover parameter. In particular the conditional-variance estimate has only an order bound. Earlier full inversion enumerators may permit a different derivation of the same structural inequalities and crossover, so independent historical-priority review remains necessary. The claim does not assert that those earlier complete enumerators are weaker as counting statements. The finite verification is not an infinite proof; all infinite assertions are justified by the preceding coupling and concentration arguments.

## References
1. W. M. B. Dukes, *Permutation statistics on involutions*, arXiv:math/0412222, first submitted 2004-12-11; especially sections 2.1 and 2.3. https://arxiv.org/abs/math/0412222
2. S. B. Hart and P. J. Rowley, *Involution Statistics in Finite Coxeter Groups*, arXiv:1403.7506, first submitted 2014-03-28; especially Theorem 1.1 and its discussion of earlier bivariate inversion enumeration. https://arxiv.org/abs/1403.7506
3. M. Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604, first submitted 2009-11-18; especially section 6. https://arxiv.org/abs/0911.3604
4. J. Désarménien, *Les q-analogues des polynômes d'Hermite*, Séminaire Lotharingien de Combinatoire 6 (1982), Art. B06b; cited and summarized by Dukes. An exact day of original publication was not verified.

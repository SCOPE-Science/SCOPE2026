# Sixteen exact bands and prime-pattern densities for squarefree reciprocal-cube divisor sums

## Finding

Let \(\mathcal S\) denote the squarefree positive integers, and define the ordinary generalized divisor function
\[
F(n)=\sigma_{-3}(n)=\sum_{d\mid n}d^{-3}=\prod_{p\mid n}(1+p^{-3})\quad (n\in\mathcal S).
\]
Write \(B=\{2,3,5,7\}\), and, for every subset \(S\subseteq B\), let
\[
c_S=\prod_{p\in S}(1+p^{-3}),\qquad
T=\prod_{p\ge11}(1+p^{-3})
=\frac{\zeta(3)}{\zeta(6)\prod_{p\in B}(1+p^{-3})}.
\]
An empty product is \(1\). The exact topological closure is
\[
\boxed{\overline{F(\mathcal S)}=\bigsqcup_{S\subseteq\{2,3,5,7\}}[c_S,c_ST].}
\]
All sixteen displayed closed intervals are nonempty and pairwise disjoint, and hence they are exactly the sixteen connected components; fifteen gaps separate them. This also determines every endpoint as an exact rational multiple of \(T\). In particular, the bottom and top bands are \([1,T]\) and \([c_B,c_BT]\), and \(c_BT=\zeta(3)/\zeta(6)\).

The set of squarefree positive integers mapped into the band indexed by \(S\) has absolute natural density
\[
\boxed{\quad d_S=\frac{6}{\pi^2}\prod_{p\in S}\frac1{p+1}\prod_{p\in B\setminus S}\frac p{p+1}.\quad}
\]
The conditional relative density *among squarefree integers* is therefore the rational factor multiplying \(6/\pi^2\). The sixteen conditional densities add to \(1\); all are positive.

## Assumptions and scope

Every prime \(p\) is a positive rational prime; \(n\in\mathcal S\) includes \(n=1\). Only the domain of squarefree positive integers is used. Closure and connected components are in the usual real topology. The density assertions concern natural density of integers and conditional density among squarefree positive integers. No unproved hypothesis about primes is used; the only external prime-gap input is the classical theorem of Nagura, stated below.

## Proof

**1. A summable-weight interval lemma.** Let \(w_j>0\) be summable and satisfy \(w_j\le\sum_{i>j}w_i\) for every \(j\). Then the closure of its finite subsums is exactly \([0,\sum_{j\ge1}w_j]\). Indeed, given a target \(x\) in that interval and remaining tail \(R_j=\sum_{i\ge j}w_i\), choose digit \(\varepsilon_j=1\) whenever the current remainder exceeds \(R_{j+1}\), and choose \(0\) otherwise. In the first case, \(R_{j+1}\ge w_j\) ensures subtraction leaves a remainder in \([0,R_{j+1}]\); otherwise this already holds. The remainders tend to zero, so the corresponding infinite subsum equals \(x\). Its finite partial subsums converge to \(x\). The opposite inclusion follows from positivity and the total sum.

**2. Every prime from \(11\) onward has a covered weight.** Put \(w_p=\log(1+p^{-3})\). For primes \(p\in\{11,13,17,19,23\}\), exact rational multiplication establishes respectively
\[
\begin{aligned}
1+11^{-3}&<(1+13^{-3})(1+17^{-3})(1+19^{-3}),\\
1+13^{-3}&<(1+17^{-3})(1+19^{-3})(1+23^{-3})(1+29^{-3}),\\
1+17^{-3}&<(1+19^{-3})(1+23^{-3}),\\
1+19^{-3}&<(1+23^{-3})(1+29^{-3})(1+31^{-3}),\\
1+23^{-3}&<(1+29^{-3})(1+31^{-3})(1+37^{-3}).
\end{aligned}
\]
Every right-hand-side prime is strictly greater than the prime on its left. These are verifiable fraction inequalities, not numerical approximations.

For every prime \(p\ge29\), Nagura's unconditional 1952 theorem gives a prime in each open interval \((x,6x/5)\) for real \(x\ge25\). Consequently, for every integer \(i\ge1\) there are distinct primes
\[
(6/5)^{i-1}p<q_i<(6/5)^ip.
\]
Set \(y=p^{-3}\) and \(a=(5/6)^3=125/216\). Since \(0<q_i^{-3}<y\), the elementary inequality \(\log(1+t)\ge t/(1+t)\) gives
\[
\sum_{q>p}w_q\ \ge\ \sum_{i\ge1}\log(1+q_i^{-3})
>\frac y{1+y}\sum_{i\ge1}a^i
=\frac{125}{91}\frac y{1+y}>y\ge w_p.
\]
The penultimate inequality holds because \(p\ge29\) and \(125>91(1+29^{-3})\). Thus \(w_p\le\sum_{q>p}w_q\) for every \(p\ge11\). By Step 1, the closure of finite products of \(1+p^{-3}\) over primes \(p\ge11\) is the entire interval \([1,T]\). Continuity of exponentiation, and strict monotonicity of logarithm, transfer the additive interval to the multiplicative one.

**3. The four smaller prime weights are strictly dominant.** The sum of inverse cubes of primes from \(11\) onward admits the rational upper bound
\[
\sum_{q\ge11}q^{-3}\le\sum_{m\ge0}(11+2m)^{-3}
\le\frac1{1331}+\int_0^\infty(11+2t)^{-3}\,dt
=U:=\frac1{1331}+\frac1{484}.
\]
For every prime \(p\), \(\log(1+p^{-3})>1/(p^3+1)\), while \(\log(1+q^{-3})<q^{-3}\). Four exact rational inequalities are
\[
\begin{aligned}
\frac1{344}&>U,\\
\frac1{126}&>\frac1{343}+U,\\
\frac1{28}&>\frac1{125}+\frac1{343}+U,\\
\frac19&>\frac1{27}+\frac1{125}+\frac1{343}+U.
\end{aligned}
\]
Therefore \(w_p>\sum_{q>p}w_q\) for \(p=7,5,3,2\), respectively. For any two distinct subsets of \(B\), the first (smallest) prime on which their inclusion patterns differ has weight strictly larger than the sum of all remaining prime weights. Hence the full log-product intervals
\[
\left[\sum_{p\in S}w_p,\ \sum_{p\in S}w_p+\sum_{q\ge11}w_q\right]
\]
for different \(S\subseteq B\) are strictly separated. By Step 2, each is filled in the closure by restricting the prime factors from \(B\) exactly to \(S\). Exponentiating proves the stated disjoint union and exactly sixteen components.

**4. Exact component densities.** Because the intervals are disjoint, an integer \(n\in\mathcal S\) lies in \([c_S,c_ST]\) if and only if its set of prime divisors from \(B\) is exactly \(S\). For a fixed prime \(p\), among squarefree integers the limiting fraction having \(v_p(n)=1\) is \((1/p-1/p^2)/(1-1/p^2)=1/(p+1)\); the fraction with \(v_p(n)=0\) is \(p/(p+1)\). For finitely many fixed primes these events are asymptotically independent: use the Chinese remainder theorem to impose each valuation modulo \(p^2\), and then the convergent squarefree sieve for the remaining primes (the contribution from squared primes exceeding \(Y\) is at most \(X\sum_{p>Y}p^{-2}+O(\sqrt X)\)). The density of squarefree integers is \(1/\zeta(2)=6/\pi^2\). Multiplying the corresponding local factors gives the formula for \(d_S\). Summing them over the sixteen subsets multiplies \(\prod_{p\in B}[(1+p)/(p+1)]=1\). This completes the proof.

## Verification

The standalone Python 3 standard-library program `check.py` verifies with exact rational arithmetic all five finite-prime tail product inequalities, all four separating inequalities, the universal Nagura-geometric bound at \(p=29\), and the exact sum of the sixteen conditional density weights. It also calculates the sixteen rational left endpoints \(c_S\) and checks their distinctness. The proof of the infinite-prime tail relies on the displayed analytic argument and Nagura's theorem, not on finite enumeration; a successful program run alone is not claimed to certify that theorem. Execute `python3 check.py` from the extracted package directory; expected output is `VERIFY_OK: 16 intervals, 16 conditional masses, finite inequalities exact`.

## Relationship to prior work

Defant's 2015 article on generalized divisor functions with restricted domains (arXiv:1507.02663v1) defines \(\sigma_{t,k}\), with \(k=1\) corresponding to the squarefree case, proves criteria for full-range density, and explicitly asks for the number of gaps in the restricted ranges at various parameters. The present result answers that exact gap-count question for the natural case \((k,r)=(1,3)\), and additionally supplies exact endpoints and component-density formulas. Defant does not present these sixteen bands or their densities.

Sanna's 2015 theorem on closure and rational band densities (arXiv:1507.08091v1) treats the generalized divisor function on *all* positive integers; restricting to the squarefree subset changes its range and cannot be inferred from the unrestricted component count. Earlier exact squarefree reciprocal-square calculations and unrestricted reciprocal-cube calculations likewise do not imply this restricted cubic classification. The prime-gap result invoked here is Nagura (1952). This claim does not assert a novelty proof from absence of search results.

## Limitations

The theorem is for exponent exactly \(3\) and the squarefree domain, not arbitrary real exponents or all integers. It does not classify the internal frequency distribution of individual values inside a component. Possible earlier unindexed calculations of this exact restricted cubic case remain an originality risk. The cited prime-gap theorem is used as an established published input rather than reproved here. This is a mathematically self-contained deduction conditional only on that unconditional established theorem and routine squarefree-density facts, with a reproducible rational certificate for the finite comparisons.

## References

1. C. Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663v1, first posted 2015-07-09. https://arxiv.org/abs/1507.02663
2. C. Sanna, *On the closure of the image of the generalized divisor function*, arXiv:1507.08091v1, first posted 2015-07-29. https://arxiv.org/abs/1507.08091
3. J. Nagura, *On the interval containing at least one prime number*, Proceedings of the Japan Academy **28** (1952), 177–181, DOI:10.3792/pja/1195570997.

# Determinant-controlled joint derangements of primitive words in commuting permutations

## Finding
Fix linearly independent primitive vectors \(v=(a,b)\), \(w=(c,d)\) in \(\mathbb Z^2\), and put \(\Delta=|ad-bc|\ge1\). For every \(n\ge1\), choose uniformly an ordered commuting pair \((\sigma,\tau)\in S_n^2\). Write \(T_v=\sigma^a\tau^b\), \(T_w=\sigma^c\tau^d\) (negative powers denote inverses). Let \(E_v\) and \(E_w\) mean respectively that \(T_v\) and \(T_w\) have **no fixed point**. These are first-order sentences in the two-bijection language for each fixed pair of vectors.

Write \(p(n)\) for the ordinary integer partition number, \(p(-1)=0\), and \(P(z)=\sum_{n\ge0}p(n)z^n=\prod_{m\ge1}(1-z^m)^{-1}\). With \(F_\Delta(z)=\sum_{d\mid\Delta}z^d/d\), the exact probability identities are
\[
 \Pr_n(E_v)=\frac{p(n)-p(n-1)}{p(n)},\qquad
 \Pr_n(E_v\cap E_w)=\frac{[z^n]P(z)(1-z)^2\exp(F_\Delta(z))}{p(n)}.
\]
For every **fixed** independent primitive pair, as \(n\to\infty\),
\[
 \Pr_n(E_v)\sim \frac{\pi}{\sqrt{6n}},\qquad
 \Pr_n(E_v\cap E_w)\sim \frac{\pi^2}{6n}\exp\left(\sum_{d\mid\Delta}\frac1d\right),
\]
so the limiting multiplicative dependence is
\[
 \boxed{\displaystyle\lim_{n\to\infty}\frac{\Pr_n(E_v\cap E_w)}{\Pr_n(E_v)\Pr_n(E_w)}=\exp\left(\sum_{d\mid\Delta}\frac1d\right).}
\]
More generally, if \(K_v\), \(K_w\) count joint \(\langle\sigma,\tau\rangle\)-orbits pointwise fixed by their respective words, then their exact bivariate probability generating function is
\[
 \mathbb E_n[x^{K_v}y^{K_w}]
 =\frac{[z^n]P(z)(1-z)^{2-x-y}\exp((x-1)(y-1)F_\Delta(z))}{p(n)}.
\]
The probability results above are specializations \(x=y=0\). The theorem concerns commuting-pair-uniform probability, not independent-uniform sampling of the two permutations.

## Assumptions and scope
The two vectors are individually primitive (each coordinate gcd equals one), nonparallel, and fixed as \(n\) increases. Both permutations are chosen jointly uniformly from **all** ordered commuting pairs on \([n]\). A permutation word fixes one point of a transitive \(\mathbb Z^2\)-orbit if and only if it fixes every point of that orbit: all translations commute. The two events are therefore elementary first-order fixed-point-exclusion sentences, although \(K_v\) itself is an orbit count.

## Proof
**1. Finite transitive orbit census.** An ordered commuting pair is a finite \(\mathbb Z^2\)-action. Each transitive component is a quotient \(\mathbb Z^2/H\) by a unique finite-index subgroup \(H\le\mathbb Z^2\) (the point stabilizer, independent of the point). If \(m=[\mathbb Z^2:H]\), then this transitive action has \(m\) automorphisms and thus contributes exactly \(m!/m\) structures on a given labelled \(m\)-element set. The labelled exponential contribution of that component type is \(z^m/m\). The number of index-\(m\) subgroups is \(\sum_{d\mid m}d\), by the triangular-lattice normal form. The exponential formula consequently gives
\[
 \exp\left(\sum_{m\ge1}\frac{\sigma_1(m)}m z^m\right)=\prod_{j\ge1}(1-z^j)^{-1}=P(z),
\]
where \(\sigma_1(m)=\sum_{d\mid m}d\). Hence exactly \(n!p(n)\) ordered commuting pairs exist.

**2. Primitive stabilizer arithmetic.** Since \(v\) is primitive, it extends to an integer basis of \(\mathbb Z^2\). For every \(m\ge1\), there is exactly **one** index-\(m\) subgroup containing \(v\): in the basis \((v,u)\) it is \(\mathbb Zv+m\mathbb Zu\). Thus the exponential generating function for all component types fixed by \(T_v\) is \(\exp(\sum_{m\ge1}z^m/m)=(1-z)^{-1}\). For the intersection of the two fixed-component families, \(H\) must contain \(L=\mathbb Zv+\mathbb Zw\). The quotient \(\mathbb Z^2/L\) is cyclic of order \(\Delta\) because \(v\) is primitive. Therefore its subgroups give exactly one containing subgroup \(H\) of each index \(d\mid\Delta\). Their aggregate connected exponential contribution is \(F_\Delta(z)\).

**3. Exact marked counting.** Mark each component fixed by \(T_v\) with a factor \(x\), and likewise those fixed by \(T_w\) with \(y\). A component fixed by both receives \(xy\), not \(x+y\). Relative to the unmarked generating function, this introduces the exponential correction
\[
 (x-1)\sum_{m\ge1}\frac{z^m}{m}+(y-1)\sum_{m\ge1}\frac{z^m}{m}+(x-1)(y-1)F_\Delta(z).
\]
Exponentiating and extracting degree \(n\), then dividing by \(p(n)\), gives the bivariate formula. Setting \(x=0,y=1\) gives \(P(z)(1-z)\); setting \(x=y=0\) gives \(P(z)(1-z)^2e^{F_\Delta(z)}\).

**4. Sharp rare-event constants.** Put \(A=\pi\sqrt{2/3}\) and \(h(t)=e^{A\sqrt{t-1/24}}/(4\sqrt3(t-1/24))\). The leading Rademacher summand for \(p(n)\) has the form \(h(n)(1+O(n^{-1/2}))\) with its smooth correction terms and an exponentially smaller remainder; differentiating that explicit smooth summand twice shows
\[
 \frac{p(n)-p(n-1)}{p(n)}\sim\frac{A}{2\sqrt n}=\frac{\pi}{\sqrt{6n}},
\quad
 \frac{p(n)-2p(n-1)+p(n-2)}{p(n)}\sim\frac{A^2}{4n}=\frac{\pi^2}{6n}.
\]
For clarity, the mere leading-order Hardy--Ramanujan relative error is **not** by itself enough to justify second finite differences; using the smoothly differentiable first Rademacher term with exponentially smaller remaining terms is essential. Write \(e^{F_\Delta(z)}=\sum_{j\ge0}b_jz^j\), where \(b_j\ge0\), \(\sum_jb_j=e^{F_\Delta(1)}\), and for each fixed \(\Delta\) its tail decays faster than any power. The joint numerator equals \(\sum_{j=0}^n b_j\,[p(n-j)-2p(n-j-1)+p(n-j-2)]\), with \(p(t)=0\) for negative \(t\). For \(j\le C\log n\), smooth Rademacher asymptotics make the summand's second-difference ratio to that at \(n\) tend uniformly to one. For \(j>C\log n\), choose \(C\) so the entire-function coefficient tail is \(o(1/n)\), and use the elementary bound \(|\Delta^2p(k)|\le4p(n)\) for \(0\le k\le n\). The convolution is therefore asymptotic to \(e^{F_\Delta(1)}\Delta^2p(n)\), proving the claimed joint constant. Divide by the product of single-event asymptotics for the final factor.

## Verification
Run the standalone file `commuting_pair_checker.py` with Python 3 (standard library only). The program independently exhausts the \(\sum_{n=1}^6n!p(n)=8903\) commuting pairs across sizes \(1\) to \(6\), comparing the exact one-event counts and five two-event counts for independent primitive directions \((1,0)\) and \((1,d)\), \(d=1,\ldots,5\), with rational generating-function coefficients. The computed signal is `COMMUTING_PRIMITIVE_EXCLUSION_OK 8903 30`. These checks validate small finite instances; the theorem for every \(n\) and the asymptotic statement rest on the preceding argument.

## Relationship to prior work
Abdesselam and Starr (arXiv:2505.11469; published 2026) prove central-limit asymptotics for the **total number of joint orbits** of commuting tuples and describe the known partition-function representation. Abdesselam, Brunialti, Doan and Velie (2024) enumerate commuting tuples by total orbit count and provide a bijection. The result here instead weights **fixed points of specified primitive words**, provides a complete exact two-word generating function, and shows that its sharp rare-event dependence is governed by the sum of reciprocal divisors of the determinant. The partition-function and transitive-component machinery are classical; neither those ingredients nor the one-variable partition asymptotic are claimed as new. The 2026 work of Marström and Räty studies logical limit laws for small permutation classes in the two-order encoding and does not directly address these commuting bijection actions.

## Limitations
All probability statements require primitive independent vectors fixed as \(n\to\infty\). The formulas do not extend unchanged to nonprimitive or parallel vectors, independently sampled permutations, or unrestricted pairs. The finite checker is not a proof of the infinite theorem. Historical priority remains subject to stronger unlocated specializations of random group-homomorphism enumeration; no independent mathematical validation has been performed.

## References
1. A. Abdesselam and S. Starr, *A central limit theorem for a generalization of the Ewens measure to random tuples of commuting permutations*, arXiv:2505.11469v1 (2025-05-16), *Journal of Theoretical Probability* 39 (2026), article 32; doi:10.1007/s10959-026-01489-2.
2. A. Abdesselam, P. Brunialti, T. Doan and P. Velie, *A bijection for tuples of commuting permutations and a log-concavity conjecture*, *Research in Number Theory* 10 (2024), article 45; doi:10.1007/s40993-024-00531-8.
3. K. Marström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1 (2026-10-15).
4. H. Rademacher, *On the partition function \(p(n)\)*, *Proceedings of the London Mathematical Society* (1937), for the convergent series and its exponentially accurate first-term approximation.

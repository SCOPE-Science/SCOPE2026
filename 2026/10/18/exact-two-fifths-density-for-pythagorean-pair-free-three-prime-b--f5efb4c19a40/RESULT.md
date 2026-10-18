# Exact two-fifths density for Pythagorean-pair-free three-prime boxes

## Finding
For positive integers \(A,B,C\), let
\[
\mathcal B_{A,B,C}=\{2^a3^b5^c:0\leq a<A,\ 0\leq b<B,\ 0\leq c<C\},
\]
and let \(F(A,B,C)\) denote the maximum cardinality of a subset \(S\subseteq\mathcal B_{A,B,C}\) with no two distinct members \(x,y\) for which \(x^2+y^2=z^2\) for some positive integer \(z\). The hypotenuse \(z\) is unrestricted. For all positive \(A,B,C\),
\[
BC\left(2\left\lfloor\frac A5\right\rfloor+\min(A\bmod5,2)\right)\leq F(A,B,C).
\]
For every \(A\geq2\) and every positive \(B,C\),
\[
F(A,B,C)\leq\left\lfloor\frac25(A+3)(B+2)(C+1)\right\rfloor.
\]
Consequently,
\[
\lim_{\min(A,B,C)\to\infty}\frac{F(A,B,C)}{ABC}=\frac25,
\]
in particular \(\lim_{N\to\infty}F(N,N,N)/N^3=2/5\). The result also gives an exact classification of the primitive Pythagorean leg pairs supported on \(\{2,3,5\}\): they are \((3,4),(5,12),(8,15),(9,40)\), up to swapping the legs.

## Assumptions and scope
All exponent bounds are positive integers, the legs are distinct positive integers, and the third side need only be an integer. The density limit concerns exponent-box cardinality \(ABC\), not natural density among all positive integers. The theorem gives sharp limiting density but does **not** claim exact finite values of \(F(A,B,C)\), classification of all maximizers, or a result when the number of allowed prime factors grows with the box side.

## Proof
**Lemma (all primitive supported legs).** Suppose \(x,y>0\), \(\gcd(x,y)=1\), every prime divisor of \(xy\) lies in \(\{2,3,5\}\), and \(x^2+y^2\) is a square. Then \(\{x,y\}\) is one of \(\{3,4\},\{5,12\},\{8,15\},\{9,40\}\).

*Proof of lemma.* Exactly one primitive leg \(X\) is odd. Euclid's parametrization for primitive Pythagorean triples gives coprime odd integers \(u>v\geq1\) such that \(X=uv\) and the even leg is \(Y=(u^2-v^2)/2\). (Indeed, if the usual parameters are \(m>n\), coprime of opposite parity, take \(u=m+n\) and \(v=m-n\).) The odd leg is \(3\)-\(5\)-smooth. Since \(\gcd(X,Y)=1\), the even leg has no odd prime factors that divide \(X\).

If \(X=1\), the equation \(1+Y^2=z^2\) has no positive solution. If \(X=3^r\) with \(r\geq1\), coprimality forces \(u=3^r,v=1\), and \(Y=(3^{2r}-1)/2\) has prime factors only \(2,5\). If \(r\) is odd, \(v_2(3^r-1)=1\) and \(v_2(3^r+1)=2\). Both odd parts must be powers of \(5\), but \(\gcd(3^r-1,3^r+1)=2\), so at most one can be divisible by \(5\). When \(r>1\), both factors exceed their respective pure powers of \(2\); this is impossible. Hence \(r=1\) and \((X,Y)=(3,4)\). If \(r\) is even, \(v_2(3^r+1)=1\). Because \(3^r+1>2\) and only primes \(2,5\) can divide either factor, the odd part of \(3^r+1\) is a **positive** power of \(5\). Since the two factors have gcd \(2\), the odd part of \(3^r-1\) is not divisible by \(5\) and hence \(3^r-1\) is a power of \(2\). The factors \(3^{r/2}-1\) and \(3^{r/2}+1\) are consecutive even powers of \(2\), so they are \(2\) and \(4\). Hence \(r=2\) and \((X,Y)=(9,40)\).

If \(X=5^s\) with \(s\geq1\), similarly \(u=5^s,v=1\) and \(Y=(5^{2s}-1)/2\) has prime factors only \(2,3\). For odd \(s\), the two factors \(5^s-1\) and \(5^s+1\) have \(2\)-adic valuations \(2\) and \(1\), respectively, and their odd parts must be powers of \(3\). For \(s>1\), both would be divisible by \(3\), contradicting their gcd of \(2\). Thus \(s=1\), yielding \((5,12)\). For even \(s\), the factor \(5^s+1\) is congruent to \(2\) modulo \(8\) and \(2\) modulo \(3\), so its only permitted prime divisor is \(2\), occurring exactly once; the impossible equality \(5^s+1=2\) results.

Finally suppose \(X=3^r5^s\) with \(r,s\geq1\). The coprime factors \(u,v\) either equal \(X,1\), or are \(3^r,5^s\) in some order. In either case \(Y\) must be a power of \(2\). In the first case, \((X-1)(X+1)=2Y\) is a power of \(2\); two consecutive even powers of \(2\) are necessarily \(2,4\), giving \(X=3\), a contradiction. In the second case, both \(u+v\) and \(|u-v|\) are powers of \(2\) with gcd \(2\). Thus \(|u-v|=2\) and \(\{3^r,5^s\}=\{2^t-1,2^t+1\}\) for some \(t\geq2\). If \(3^r=2^t-1\), then \(t\) must be even (by reducing modulo \(3\)); factoring \(2^t-1=(2^{t/2}-1)(2^{t/2}+1)\) into coprime odd factors that are powers of \(3\) forces \(t=2\), giving \(3,5\). If \(3^r=2^t+1\), then \(t\) is odd. For \(t\geq3\), reduction modulo \(8\) forces \(r\) even, and the factorization \((3^{r/2}-1)(3^{r/2}+1)=2^t\) forces \(r=2,t=3\), where \(2^t-1=7\) is not a power of \(5\). The case \(t=1\) gives the other factor \(1\), also excluded. We are left with \((X,Y)=(15,8)\). Direct substitution checks all four primitive pairs. This proves the lemma.

**Exponent graph.** Every Pythagorean pair among supported integers has a common positive integer factor \(d=2^i3^j5^k\), and after division by \(d\) its legs form one of the four pairs above. Hence, in exponent coordinates \((a,b,c)\), all and only the forbidden edges have difference \(\pm d_j\), for
\[
d_1=(2,-1,0),\quad d_2=(2,1,-1),\quad d_3=(3,-1,-1),\quad d_4=(3,-2,1).
\]
Here the displayed \(d_j\) are signed integer displacement vectors, not multiplicative factors.

**Lower bound.** Take all exponent vectors for which \(a\bmod5\in\{0,1\}\). Every forbidden displacement changes \(a\) by \(\pm2\) or \(\pm3\), so neither end of any forbidden edge can lie in this selection simultaneously. There are \(2\lfloor A/5\rfloor+\min(A\bmod5,2)\) allowed \(a\)-coordinates and \(BC\) choices of the other coordinates. This proves the stated lower bound.

**Upper bound.** The five numbers
\[
405,\ 540,\ 720,\ 1350,\ 1800
\]
form a five-cycle of forbidden pairs, in the displayed cyclic order (the consecutive hypotenuses are \(675,900,1530,2250,1845\)). Their exponent vectors are respectively
\[
(0,4,1),\quad(2,3,1),\quad(4,2,1),\quad(1,3,2),\quad(3,2,2).
\]
Their successive edge displacements (including the final edge to the first vertex) belong to \(\{\pm d_1,\ldots,\pm d_4\}\).

Fix \(A\geq2\). Work on the discrete three-torus
\[
T=\mathbb Z/(A+3)\mathbb Z\times\mathbb Z/(B+2)\mathbb Z\times\mathbb Z/(C+1)\mathbb Z
\]
with the same four edge displacements modulo its periods. Embed any admissible exponent-box subset \(S\) as a subset of \(T\), with all points outside the original box unoccupied. The embedded subset remains independent: for each coordinate \(j\), the maximal absolute difference of two occupied coordinates is one smaller than the original side length; by contrast, a wrapped congruence to a displacement of absolute size at most \((3,2,1)_j\) would require a difference of absolute size at least the corresponding original side length. Thus no forbidden edge can arise across a torus seam.

The five template exponent vectors are distinct modulo \(T\) because their first coordinates are \(0,1,2,3,4\) in some order and \(A+3\geq5\). Translating this five-cycle by each point of \(T\) gives a (possibly chorded) five-cycle, so each translate meets \(S\) in at most two vertices. Every occupied torus vertex lies in exactly five translated cycle vertex-sets, counted with multiplicity across translations. Double-counting yields
\[
5|S|\leq2|T|=2(A+3)(B+2)(C+1),
\]
and hence the upper bound after taking the integer floor.

Finally divide the bounds by \(ABC\) and let \(\min(A,B,C)\to\infty\). Both lower and upper bounds converge to \(2/5\), completing the proof.

## Verification
The standalone program `verify.py` independently constructs Pythagorean edges by integer-square testing and compares them with the four-vector exponent graph on 120 small rectangular boxes. It checks the explicit five-cycle, its hypotenuses, the periodic construction's arithmetic preconditions, and the lower independent set. Run `python3 verify.py` using Python 3 standard library only. Expected result: `VERIFY_OK rectangular_boxes=120 five_cycle_edges=5 classification_agrees=YES`. These finite checks are supplementary; the infinite theorem follows from the proof above.

## Relationship to prior work
R. Xiao, *Pythagorean pairs in boxes of prime powers* (arXiv:2610.11965, first posted 8 October 2026), considers exponent boxes whose prime support grows with the side length and proves an upper bound with vanishing relative density. The present theorem keeps exactly three primes and lets all exponent sides grow; neither theorem implies the other. R. Xiao, *Quantitative lower bound for Pythagorean pairs in boxes of prime powers* (arXiv:2610.20311, 14 October 2026), gives a lower bound in the growing-support regime, likewise not a fixed-three-prime density classification. The general partition-regularity and multiplicative-density theorem of N. Frantzikinakis, O. Klurman, and J. Moreira, *Partition regularity of Pythagorean pairs* (arXiv:2309.10636, 2023), does not determine this positive density inside the multiplicative subsemigroup supported on just three primes.

## Limitations
No exact formula for finite \(F(A,B,C)\) or all extremizing sets is established. The primitive leg classification assumes both legs are supported on precisely the allowed *set of possible prime factors* \(\{2,3,5\}\), with no requirement that each prime occur. The result does not establish results for four or more supported primes, where additional Pythagorean ratios can occur. The first-public source date belongs to the motivating paper and not to a claim of publication or independent validation of this theorem.

## References
1. R. Xiao, *Pythagorean pairs in boxes of prime powers*, arXiv:2610.11965, initially released 8 October 2026, https://arxiv.org/abs/2610.11965.
2. R. Xiao, *Quantitative lower bound for Pythagorean pairs in boxes of prime powers*, arXiv:2610.20311, first released 14 October 2026, https://arxiv.org/abs/2610.20311.
3. N. Frantzikinakis, O. Klurman, and J. Moreira, *Partition regularity of Pythagorean pairs*, arXiv:2309.10636, first released 19 September 2023, https://arxiv.org/abs/2309.10636.

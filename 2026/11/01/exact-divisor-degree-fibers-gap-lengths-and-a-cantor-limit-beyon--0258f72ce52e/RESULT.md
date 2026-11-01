# Exact divisor-degree fibers, gap lengths and a Cantor limit beyond the two-prime \(\varphi\)-practical threshold

## Finding
For integers \(a,b\ge1\), an odd prime \(p>2^a+1\), and \(n=2^a p^b\), let \(N_n(d)\) be the number of monic integral-polynomial divisors of \(X^n-1\) of degree \(d\). Put \(A=2^a\), and let \(\mathcal D_n=\{d:N_n(d)>0\}\). All the possible degrees, their multiplicities, and every missing-degree interval are determined as follows.

Each vector \((u_0,\ldots,u_b)\in\{0,\ldots,A\}^{b+1}\) defines a **distinct** attained degree
\[
d=u_0+(p-1)\sum_{j=1}^b p^{j-1}u_j,
\]
with precisely
\[
N_n(d)=2^{\#\{j:0<u_j<A\}}
\]
monic divisors of that degree; all other degrees have multiplicity zero. In particular, for \(0\le r\le b+1\),
\[
\#\{d:N_n(d)=2^r\}=\binom{b+1}{r}(A-1)^r2^{b+1-r}.
\]
Thus exactly \((A+1)^{b+1}\) of the \(Ap^b+1\) degrees occur, and precisely \(2^{b+1}-2\) **interior** degrees occur uniquely.

For each \(0\le k<b\), the consecutive omitted-degree intervals of length
\[
L_k=(p-1-A)p^k-1
\]
occur exactly \(A(A+1)^{b-1-k}\) times. These are all the omissions, and all \(L_k\) are positive and pairwise distinct.

For fixed \(a,p\), the normalized degree sets \(\{d/(Ap^b):d\in\mathcal D_{Ap^b}\}\) converge in Hausdorff distance at most \(p^{-b}\) to the self-similar set
\[
K_{A,p}=\left\{\frac{p-1}{A}\sum_{h\ge1}v_hp^{-h}:v_h\in\{0,\ldots,A\}\right\},
\qquad \dim_H K_{A,p}=\frac{\log(A+1)}{\log p}.
\]
A uniformly chosen monic divisor of \(X^{Ap^b}-1\) produces a probability distribution on normalized degrees
\[
\mu_b=2^{-(a+1)(b+1)}\sum_{d=0}^{Ap^b}N_{Ap^b}(d)\,\delta_{d/(Ap^b)}.
\]
These distributions converge weakly to the self-similar probability measure \(\mu_{A,p}\) on \(K_{A,p}\) whose independent digits \(v_h\) have probabilities
\[
\mathbb P(v_h=0)=\mathbb P(v_h=A)=\frac1{2A},\qquad
\mathbb P(v_h=u)=\frac1A\quad(1\le u<A).
\]
The limiting measure is exact dimensional, with
\[
\boxed{\dim_H\mu_{A,p}=\frac{\log A+(\log2)/A}{\log p}}.
\]

## Assumptions and scope
All monic divisors are in \(\mathbb Z[X]\), not modulo a prime or in a finite field. The index is exactly \(n=2^a p^b\), with \(a,b\ge1\) and odd prime \(p>2^a+1\). Set \(A=2^a\). For integral \(d\in[0,n]\), \(N_n(d)\) counts distinct monic divisor polynomials (not factorizations or subsets with repetition). The empty and complete products are included. The complementary threshold \(p\le A+1\) is the known \(\varphi\)-practical range, and is not part of this theorem.

## Proof
**1. Factor-degree generating polynomial.** The cyclotomic factorization \(X^n-1=\prod_{m\mid n}\Phi_m(X)\) is squarefree over \(\mathbb Q[X]\), and each cyclotomic factor is monic and irreducible. Hence every monic integral divisor is uniquely a subset product, of degree the sum of its cyclotomic-factor degrees \(\varphi(m)\). On the power-of-two layer, the multiset of degrees is \(1,1,2,4,\ldots,2^{a-1}\). Its generating polynomial is
\[
H_A(z)=(1+z)^2\prod_{i=1}^{a-1}(1+z^{2^i})
       =(1+z)(1+z+\cdots+z^{A-1})
       =1+2\sum_{u=1}^{A-1}z^u+z^A.
\]
For \(j\ge1\), the corresponding layer with exact \(p\)-exponent \(j\) has all factor-degrees multiplied by \(c_j=(p-1)p^{j-1}\). Therefore
\[
\sum_{d=0}^n N_n(d)z^d=H_A(z)\prod_{j=1}^bH_A(z^{c_j}).\tag{1}
\]
This identity also shows the maximal possible degree is \(A+(p-1)A(1+\cdots+p^{b-1})=Ap^b=n\).

**2. No distinct digit vectors collide.** In any representation \(d=u_0+(p-1)t\), where \(t=\sum_{j=1}^b u_jp^{j-1}\), the residue modulo \(p-1\) determines \(u_0\) uniquely, because \(0\le u_0\le A<p-1\). The resulting nonnegative integer \(t\) has unique base-\(p\) digits \(u_1,\ldots,u_b\), since each lies in \([0,A]\subset[0,p-1]\). Hence the map of the finding is injective. Coefficients in (1) therefore do not combine across different digit vectors, and are the product of \(1\) for endpoint digits and \(2\) for interior digits. Choosing the \(r\) interior positions, their \(A-1\) values, and the two endpoint values at other positions proves the exact multiplicity histogram. Its \(r=0\) count is \(2^{b+1}\); removing degrees \(0,n\) gives the uniquely represented interior degrees.

**3. Every missing interval.** The allowed values of \(t\) are exactly the integers with at most \(b\) base-\(p\) digits from \(\{0,1,\ldots,A\}\), including leading zeros. For each such \(t\), varying \(u_0\) fills the entire integer block \([(p-1)t,(p-1)t+A]\). Order these blocks by increasing \(t\). Two successive allowed base-\(p\) words differ by increasing one digit and resetting exactly \(k\) trailing digits from \(A\) to zero, for a unique \(0\le k<b\). Their corresponding values differ by
\[
\Delta_k=p^k-A\sum_{i=0}^{k-1}p^i.
\]
The intervening missing integer degrees therefore number \((p-1)\Delta_k-A-1=(p-1-A)p^k-1=L_k\). For a transition with **exactly** \(k\) trailing maximum digits, the incremented digit must be at position \(k\), with \(A\) choices for its old value and \((A+1)^{b-1-k}\) choices for the more significant digits. Thus the count is \(A(A+1)^{b-1-k}\). The threshold \(p>A+1\) ensures \(L_k\ge1\), and their strict growth follows from \(p>1\). Every pair of adjacent blocks is counted exactly once. Consequently these are all the missing intervals, and their lengths sum to \(Ap^b+1-(A+1)^{b+1}\).

**4. Limit set.** Upon dividing a represented degree by \(Ap^b\) and reversing the order of the digits of \(t\), one obtains the first \(b\) digits of a series defining \(K_{A,p}\), plus an endpoint term \(u_0/(Ap^b)\). A full series tail after its first \(b\) digits is at most \(p^{-b}\), and the endpoint term is at most \(p^{-b}\). Matching each represented point with the same-prefix infinite series, and each infinite series with the truncated represented point having \(u_0=0\), gives Hausdorff distance at most \(p^{-b}\). The maps \(f_u(x)=((p-1)u/A+x)/p\), \(0\le u\le A\), generate \(K_{A,p}\). Their first-level closed images lie in disjoint subintervals because \(p-1>A\). The standard disjoint self-similar-set dimension formula therefore gives \((A+1)p^{-s}=1\) and \(s=\log(A+1)/\log p\).

**5. Natural divisor-degree measure.** Each monic divisor is a subset product of exactly \((a+1)(b+1)\) distinct cyclotomic irreducibles. Choosing it uniformly makes the digit contributions at different \(p\)-layers independent. By the layer polynomial \(H_A\), a digit \(u\) has probability \(h_A(u)/H_A(1)=h_A(u)/(2A)\), with endpoint and interior values stated above. Upon scaling degrees by \(Ap^b\), the reversed first \(b\) digits agree with those of the infinite random series for \(\mu_{A,p}\). Both the discarded series tail and the last normalized digit \(u_0/(Ap^b)\) lie in \([0,p^{-b}]\); a coupling therefore has displacement at most \(p^{-b}\). In particular, \(\mu_b\) converges weakly to the Bernoulli self-similar measure.

Because the first-level images are disjoint by a positive gap, each level-\(b\) cylinder has diameter at most \(p^{-b}\) and distinct level-\(b\) cylinders are separated by a fixed positive multiple of \(p^{-b}\). For an infinite digit word, the associated cylinder has mass \(\prod_{h=1}^b w_{v_h}\), where \(w_0=w_A=1/(2A)\) and \(w_u=1/A\) otherwise. By the strong law of large numbers, the logarithmic mass of the cylinder divided by \(-b\) converges for almost every word to its Shannon entropy
\[
-\sum_{u=0}^A w_u\log w_u=\log A+\frac{\log2}{A}.
\]
Balls with radii comparable to \(p^{-b}\) sandwich the same cylinder mass by the separation and diameter bounds. Hence the local dimension exists and equals the entropy divided by \(\log p\) almost surely, proving the stated exact dimension of \(\mu_{A,p}\).

## Verification
The standalone Python 3 file `verify.py` independently constructs every coefficient of \(\sum N_n(d)z^d\) by multiplying separate factors \(1+z^{\varphi(m)}\), rather than generating its coefficients by the theorem's digit formula. It then checks the full per-degree coefficient dictionary, the multiplicity histogram, all consecutive gap lengths and counts, endpoints, and the number of distinct monic divisors. The tested grid includes \(96\) distinct triples, with \(510728\) represented-degree coefficients and \(34336\) gaps. The exact output terminates in `VERIFY_OK cases=96 represented_degree_coefficients=510728 complement_gaps=34336`. Finite replay is corroboration; all quantified claims follow from the preceding proof. No external mathematical certification has been performed.

For illustration, at \(a=1,p=5,b=2\), the index is \(n=50\). Exactly \(27\) degrees occur, with multiplicity histogram \(8,12,6,1\) for multiplicities \(1,2,4,8\) respectively; there are six gaps of length \(1\) and two gaps of length \(9\), omitting exactly \(24\) degrees.

## Relationship to prior work
Thompson's \(\varphi\)-practical-number criterion establishes that the family \(2^a p^b\) has a monic divisor of every degree if and only if \(p\le2^a+1\); it does not determine the non-practical multiplicity or gap spectrum. Pollack and Thompson study the degree sets of divisors of \(T^n-1\) and their frequency, including uniqueness questions for other families; their general framework does not supply this explicit distribution. Pomerance, Thompson and Weingartner analyze the asymptotic prevalence of the all-degrees property, rather than non-practical degree gaps.

Two later publicly available, particularly close results were also compared by their mathematical claims and proofs. *Interior divisor degrees are never unique for two-prime \(\varphi\)-practical numbers* proves multiplicity at least two for all interior degrees **when \(p\le A+1\)** and explicitly excludes the present \(p>A+1\) regime; its use of the layer polynomial \(H_A\) is an acknowledged methodological overlap. *Complete-or-injective divisor subset sums on \(2^a p^b\)* instead studies sums of **positive integer divisors** and has the distinct boundary \(p>2^{a+1}\), not cyclotomic polynomial-factor degree sums. Neither statement implies the exact non-practical cyclotomic-degree fibers, gap multiset or Cantor limit described here. The current deduction from the shared digital method is elementary but treats a naturally complementary arithmetic regime and computes previously unreported exact invariants.

## Limitations
The theorem treats indices with exactly the indicated two-prime shape and \(a,b\ge1\); it makes no assertion about three-prime-support indices or divisor degrees modulo a coefficient ring. The self-similar limit fixes \(a,p\) and lets only \(b\) vary, and describes both the support of degrees and the limiting probability distribution of a uniformly chosen monic divisor; it does not classify arbitrary nonuniform choices or the multifractal spectrum. The gap classification follows from a simple digit argument and should not be confused with a general algorithmic breakthrough. Although the inspected primary texts and accessible published records do not establish this exact statement, unknown sources or reformulations may affect historical priority. Independent validation has not been performed.

## References
1. L. Thompson, “Polynomials with divisors of every degree,” arXiv:1111.5401v1, initially public 23 November 2011; *Journal of Number Theory* 132 (2012), 1038–1053.
2. P. Pollack and L. Thompson, “On the degrees of divisors of \(T^n-1\),” arXiv:1206.2084v1, initially public 11 June 2012.
3. C. Pomerance, L. Thompson and A. Weingartner, “On integers \(n\) for which \(X^n-1\) has a divisor of every degree,” arXiv:1511.03357v1, initially public 11 November 2015.
4. “Interior divisor degrees are never unique for two-prime \(\varphi\)-practical numbers,” public research record at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-interior-divisor-degrees-are-never-unique-for-two-prime-practica--02336813184a .
5. “Complete-or-injective divisor subset sums on \(2^a p^b\),” public research record at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-complete-or-injective-divisor-subset-sums-on-2-a-p-b--20554cd8e689 .

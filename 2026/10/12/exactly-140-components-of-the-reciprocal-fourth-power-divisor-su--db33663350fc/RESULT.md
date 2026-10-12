# Exactly 140 components of the reciprocal-fourth-power divisor-sum range

## Finding
For every positive integer \(n\), define \(\sigma_{-4}(n)=\sum_{d\mid n}d^{-4}\). Put
\[
T=\frac{\pi^4}{90}\prod_{p\in\{2,3,5,7,11,13\}}(1-p^{-4}).
\]
The closure of its image on the positive integers has **exactly 140 connected components** and exactly 139 bounded complementary gaps. More precisely,
\[
\overline{\{\sigma_{-4}(n):n\ge1\}}=\bigcup_{j=1}^{140}[a_j,Tb_j],
\]
where every \(a_j,b_j\) is rational and the 140 ordered pairs are specified without rounding in the accompanying `COMPONENTS.tsv`. Each interval is nondegenerate, the intervals are ordered strictly from left to right and pairwise disjoint, the first begins at \(1\), and the last ends at \(\zeta(4)=\pi^4/90\). Thus the component count and *all* endpoints are exact, not merely numerical estimates.

## Assumptions and scope
The divisor sum uses all positive divisors with the ordinary multiplicative structure; the topology is the usual real-line topology. No hypothesis about primes is made beyond the classical unconditional prime-interval theorem cited below. Every endpoint, including the limits associated with arbitrarily large prime powers and products of distinct primes, is asserted for the **closure**, not necessarily as the value of a finite argument. No natural-density classification is claimed.

Write \(f_p(a)=\sum_{k=0}^{a}p^{-4k}\) for a nonnegative integer \(a\), and \(f_p(\infty)=(1-p^{-4})^{-1}\). Let
\[
\mathcal P=(2,3,5,7,11,13),\qquad (A_2,A_3,A_5,A_7,A_{11},A_{13})=(3,2,1,1,1,1).
\]
For each \(p\in\mathcal P\), introduce a finite set of endpoint pairs
\[
\mathcal Q_p=\{(f_p(a),f_p(a)):0\le a<A_p\}
\cup\{(f_p(A_p),f_p(\infty))\}.
\]
The final theorem is equivalently the explicit finite-union formula
\[
\overline{\sigma_{-4}(\mathbb N_{>0})}
=\bigcup_{(\ell_p,u_p)\in\prod_{p\in\mathcal P}\mathcal Q_p}
\left[\prod_{p\in\mathcal P}\ell_p,\ T\prod_{p\in\mathcal P}u_p\right].
\]
There are exactly \(4\cdot3\cdot2^4=192\) intervals before merging, and the union has exactly 140 components.

## Proof
**1. The unrestricted prime tail is one interval.** Multiplicativity gives
\[
T=\prod_{p\ge17}(1-p^{-4})^{-1}.
\]
For every prime \(p\ge17\), it is enough to establish
\[
1+p^{-4}<\prod_{q>p}(1-q^{-4})^{-1}.
\tag{1}
\]
For every prime \(17\le p<396738\), a complete sieve through \(430000\), together with exact rational arithmetic, checks that the sum of the inverse fourth powers of the next at most ten primes strictly exceeds \(p^{-4}\). There are exactly 33602 tested primes; ten successors are needed in the worst case. Hence (1) follows, since the product on its right strictly exceeds one plus that prime sum.

For \(p\ge396738\), Dusart's explicit prime-interval theorem supplies a prime in \((x,x+x/(25\log^2x)]\) for every \(x\ge396738\). As \(\log x>7\), two successive primes \(q_1,q_2>p\) obey
\[
q_2/p<(1001/1000)^2<101/100,
\qquad (p/q_1)^4+(p/q_2)^4>2(100/101)^4>1.
\]
This proves (1) for all larger primes. By Sanna's interval-filling lemma for generalized divisor functions (Lemma 2.3 of the cited paper), (1) for all primes in this tail implies the exact closure identity
\[
\overline{\{\sigma_{-4}(m):\text{every prime divisor of }m\text{ is at least }17\}}=[1,T].
\tag{2}
\]

**2. The six small primes reduce to 192 rationally parameterized blocks.** For each \(p\in\mathcal P\), direct exact inequalities give
\[
\frac{f_p(A_p)}{f_p(A_p-1)}>T,
\qquad
\frac{f_p(A_p+1)}{f_p(A_p)}<T.
\tag{3}
\]
The quotient \(f_p(a+1)/f_p(a)\) strictly decreases with \(a\), so every adjacent pair of prime-power factors with exponent at least \(A_p\) has ratio less than \(T\). For any fixed values of the other five prime exponents, their associated scaled copies of \([1,T]\) overlap. The integer exponent grid for all primes assigned the high-tier condition is connected by single-coordinate moves; consequently the union of all scaled tail intervals in any of the 192 fixed-tier/high-tier classes is a *single interval*. The minimum and supremum of that class are respectively \(\prod\ell_p\) and \(T\prod u_p\). This justifies the stated 192-block formula using only one factor of \(T\), despite allowing several high-tier primes.

**3. The block endpoints give precisely 140 components.** The identity \(\zeta(4)=\pi^4/90\), the rational products above and Machin's arctangent identity give certified rational bounds on \(T\). Specifically, twenty alternating terms for each arctangent certify
\[
\frac{3141592653589793}{10^{15}}<\pi<
\frac{3141592653589794}{10^{15}}.
\]
The accompanying exact-arithmetic program builds all 192 blocks, orders them by rational lower endpoint, and evaluates every overlap and strict gap against certified enclosing rational values for \(T\). All comparisons are decisive. Exactly 52 blocks merge into preceding components, leaving 140 connected components and 139 strict gaps. An independently implemented backward interval recurrence, applying each prime in reverse order and choosing cutoffs separately for each input interval, reproduces the intermediate component counts \(2,4,8,16,48,140\) and the same 140 pairs. A third union-find graph comparison gives the same component count. The exact endpoint table completes the proof.

## Verification
Place `verify.py` and `COMPONENTS.tsv` together and run `python3 verify.py` (Python 3 standard library only). The certificate recomputes the 33602 finite prime checks with exact rational arithmetic and a deterministic sieve, checks the infinite-range bounding inequality used with Dusart's theorem, proves the small-prime threshold inequalities using arctangent interval arithmetic, constructs all 192 blocks, establishes all 139 strict gaps, checks the 140 component endpoints against `COMPONENTS.tsv`, and cross-checks via independent backward recursion and a graph connectivity calculation. The expected final line begins `EXACT_CERTIFICATE_OK` and gives `components=140`, `gaps=139` and `finite_primes=33602`. All numerical comparisons are exact; the general infinite-prime step explicitly uses the published Dusart theorem and Sanna's proved interval-filling lemma, not finite extrapolation.

To interpret the table, row \(j\) gives \(a_j=\texttt{lower\_num}/\texttt{lower\_den}\) and \(b_j=\texttt{upper\_coefficient\_num}/\texttt{upper\_coefficient\_den}\). The actual upper endpoint is \(Tb_j\). The table is data, not a secondary conjecture.

## Relationship to prior work
Sanna's 2015 preprint proves that for any real \(r>1\) the range closure of \(\sigma_{-r}\) is a finite union of closed intervals, develops a recursive algorithm to compute them, and evaluates the case \(r=2\), which has three components. The present result explicitly evaluates the next natural unreported even reciprocal exponent \(r=4\), determining its 140 components and their exact endpoints. It uses, rather than claims to originate, Sanna's interval-filling lemma and recursive framework. Defant's 2015 density-transition theorem identifies the broader motivation. Zubrilina's later work provides general bounds on the component count as the exponent varies, but does not state this exact exponent-four classification. Dusart supplies the explicit prime-interval input needed to make the infinite-tail reduction completely effective. The numerical value 140 and the 140 endpoint pairs are the particular new content; the general finiteness theorem is prior art.

## Limitations
The theorem concerns only the reciprocal-fourth-power sum and does not calculate the asymptotic densities of the 140 components, establish an exponent-uniform formula, or resolve arbitrary real exponents. Exact arithmetic and the written proof substantiate the mathematical claim, but no independent mathematical audit has been conducted. Published and indexed literature searches cannot rule out an unindexed earlier computation of the same component count. Reproduction of a finite computation alone would not certify a general theorem without the cited infinite-prime and interval-filling arguments.

## References
1. Carlo Sanna, *On the closure of the image of the generalized divisor function*, arXiv:1507.08091v1, first posted 29 July 2015, particularly Lemmas 2.3–2.5 and Sections 4–5. https://arxiv.org/html/1507.08091v1
2. Pierre Dusart, *Estimates of Some Functions Over Primes without R.H.*, arXiv:1002.0442 (2010), explicit prime interval theorem. https://ar5iv.labs.arxiv.org/html/1002.0442
3. Colin Defant, *On the Density of Ranges of Generalized Divisor Functions*, arXiv:1506.05432 (2015). https://arxiv.org/abs/1506.05432
4. Nina Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871 (2017), general component-count bounds and structural arguments. https://arxiv.org/html/1711.02871v2

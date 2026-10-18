# Fourteen connected components of the reciprocal-cube unitary divisor range

## Finding
For a positive integer \(n\), put
\[
\sigma_{-3}^*(n)=\sum_{d\mid n,\,\gcd(d,n/d)=1}d^{-3}
=\prod_{p^a\parallel n}(1+p^{-3a}).
\]
Let \(\mathcal R\) denote the topological closure in \(\mathbb R\) of \(\{\sigma_{-3}^*(n):n\ge1\}\). Set
\[
Z=\frac{\zeta(3)}{\zeta(6)},\qquad
P=\prod_{p\in\{2,3,5,7,11,13,17,19,23,29\}}(1+p^{-3}),\qquad
T=Z/P.
\]
**Theorem.** The set \(\mathcal R\) has exactly **14 connected components**. More precisely,
\[
\mathcal R=\bigcup_{j=1}^{14}[L_j,TU_j],
\]
where every rational pair \((L_j,U_j)\) is given exactly in the table below. The intervals are ordered, nonempty, pairwise disjoint, and each adjacent gap is strictly positive. In particular \(L_1=1\) and \(TU_{14}=Z\).

| Component | \(L_j\) | \(U_j\) | Approximate interval |
| ---: | ---: | ---: | --- |
| 1 | \(1\) | \(339979683167171034624/332738560088645051275\) | \([1.000000000,1.021896204]\) |
| 2 | \(819/800\) | \(13707103570671813120/13309542403545802051\) | \([1.023750000,1.030005453]\) |
| 3 | \(28/27\) | \(457038019810872968832/437813894853480330625\) | \([1.037037037,1.044046262]\) |
| 4 | \(392/375\) | \(3685318731356072832/3502511158827842645\) | \([1.045333333,1.052331283]\) |
| 5 | \(455/432\) | \(70213603875189495552/66547712017729010255\) | \([1.053240741,1.055225045]\) |
| 6 | \(2795/2646\) | \(1760442742975214398464/1663692800443225256375\) | \([1.056311413,1.058292507]\) |
| 7 | \(637/600\) | \(14154156675210988800/13309542403545802051\) | \([1.061666667,1.063598775]\) |
| 8 | \(559/525\) | \(14195301780038206464/13309542403545802051\) | \([1.064761905,1.066690579]\) |
| 9 | \(9/8\) | \(1882964399079716499456/1663692800443225256375\) | \([1.125000000,1.131946564]\) |
| 10 | \(567/500\) | \(15183253185974931456/13309542403545802051\) | \([1.134000000,1.140929117]\) |
| 11 | \(7/6\) | \(388875344539511052288/332738560088645051275\) | \([1.166666667,1.168864665]\) |
| 12 | \(172/147\) | \(9750144422631956668416/8318464002216126281875\) | \([1.170068027,1.172262469]\) |
| 13 | \(147/125\) | \(15678450471002941440/13309542403545802051\) | \([1.176000000,1.178140181]\) |
| 14 | \(1032/875\) | \(78620132935596220416/66547712017729010255\) | \([1.179428571,1.181564949]\) |

## Assumptions and scope
All integers \(n\ge1\) are allowed, with no squarefree restriction. The exponent in the unitary divisor sum is exactly \(-3\); the theorem does not claim a formula for general real exponents. The closure includes limits of sequences of integer values. \(\zeta\) is the Riemann zeta function. There is no hypothesis about unproved prime-gap conjectures.

## Proof
**1. The tail is a full interval.** Write \(p_i\) for the increasing primes, and for \(i\ge11\) put
\[
M_i=\prod_{j\ge i}(1+p_j^{-3}),\qquad
B_i=\{0\}\cup\{\log(1+p_i^{-3a}):a\ge1\}.
\]
Every consecutive gap in the compact ordered digit set \(B_i\) has size at most
\[
g_i=\log\frac{1+p_i^{-3}}{1+p_i^{-6}}.
\]
Indeed the positive digits decrease to zero and successive ratios shrink with the exponent. It suffices to show
\[
\frac{1+p_i^{-3}}{1+p_i^{-6}}<M_{i+1}\qquad(i\ge10).\tag{1}
\]
To prove (1), define
\[
F_i=\frac{1+p_i^{-3}}{1+p_i^{-6}}\prod_{j\le i}(1+p_j^{-3}).
\]
Put \(a=p_i^3\) and \(b=p_{i+1}^3\). Nagura's unconditional prime-gap theorem gives \(p_{i+1}<6p_i/5\) for \(p_i\ge29\); hence \(a<b<2a\). Consequently,
\[
\frac{F_{i+1}}{F_i}
=\frac{(b+1)^2}{b^2+1}\frac{a^2+1}{a^2+a}
>\frac{(2a+1)^2}{4a^2+1}\frac{a^2+1}{a^2+a}>1.
\]
The first strict inequality uses that \(x\mapsto(x+1)^2/(x^2+1)\) decreases for \(x>1\). The second follows on subtracting \(1\) from each factor and clearing positive denominators:
\[
4a(a^2+1)-(a-1)(4a^2+1)=4a^2+3a+1>0.
\]
Since \(F_i\uparrow Z\) as \(i\to\infty\), we have \(F_i<Z\) for all \(i\ge10\), which is (1). Thus, at every prime \(p_i\ge31\), the largest gap between choices in \(B_i\) is strictly below the total possible logarithmic contribution of later primes. The intervals of allowable later sums starting at each digit overlap and cover the full interval from zero to the total remaining logarithmic mass. Iterating this choice leaves a residual bounded by \(\sum_{j>k}\log(1+p_j^{-3})\to0\). It follows that the closure of all products from primes \(p\ge31\) equals \([1,T]\).

**2. The ten small primes reduce to a finite union of intervals.** For \(p\in\{2,3,5,7,11,13,17,19,23,29\}\), let \(A_p\) be the least positive exponent satisfying \(1+p^{-3A_p}\le T\). The exact values, in increasing prime order, are
\[
(A_2,A_3,A_5,A_7,A_{11},A_{13},A_{17},A_{19},A_{23},A_{29})
=(5,3,2,2,2,2,2,2,1,1).
\]
Suppose a previously processed set of products is a union of intervals \([L,TU]\) with \(U\ge L>0\). The omitted prime and all exponents \(a\ge A_p\) together yield exactly the single interval
\[
[L,(1+p^{-3A_p})TU].\tag{2}
\]
For each \(1\le a<A_p\), they also yield the interval
\[
[(1+p^{-3a})L,(1+p^{-3a})TU].\tag{3}
\]
The equality in (2) follows because \(1+p^{-3A_p}\le T\), so every such scaled interval overlaps the preceding one and the unscaled interval. Starting from \([1,T]\), apply (2)–(3) successively to the ten primes, then coalesce overlapping intervals. This is an *exact identity of closed sets*: it retains all exponent choices, not merely a finite search over integers.

**3. Exact rational separation and the endpoints.** The rational certificate in `verify_components.py` computes every interim endpoint and checks all overlaps and separations with strict rational inequalities. Specifically, from \(N=20000\), \(Q=10^{30}\), and integer sums \(S_s=\sum_{k=1}^{N}\lfloor Q/k^s\rfloor\), it uses
\[
\frac{S_s}{Q}+\frac{1}{(s-1)(N+1)^{s-1}}
\le\zeta(s)\le
\frac{S_s+N}{Q}+\frac{1}{(s-1)N^{s-1}},\qquad s\in\{3,6\}.
\]
The enclosure follows from monotonicity and the integral test; the interval for \(T\) is obtained by division by the positive exact rational \(P\). For two candidate intervals \([L,TU]\) and \([L',TU']\), the program merges them only after proving \(T_{\rm lo}U\ge L'\), and otherwise proves \(T_{\rm hi}U<L'\). There are no undecided comparisons. It obtains the 14 pairs in the theorem table. Processing primes in the reverse order reproduces the same rational pairs, giving a second order-of-composition check. The last upper endpoint equals \(Z\) exactly. Thus precisely 14 intervals remain, and every pair of neighbors has a genuine gap.

## Verification
Run `python3 verify_components.py` with Python 3; the standalone program requires only the standard library. It prints `COMPONENTS 14`, both merge traces, all exact pairs \((L_j,U_j)\), certified tail enclosures, and finally `VERIFY_OK`. The computation is finite exact rational arithmetic; the infinite part is established in Step 1 rather than inferred from enumeration. The mathematical input from analytic number theory is Nagura's prime-gap theorem, used only for primes at least \(29\).

## Relationship to prior work
Colin Defant introduced the topological-closure problem for unitary divisor sums and proved a critical exponent \(\eta^*\approx1.974255\): the closure is connected for \(0<r\le\eta^*\) and disconnected beyond. He also proposed studying the component-count function \(\mathcal N^*(-r)\). This work evaluates that function exactly at \(r=3\), and gives the full 14-interval closure, information not implied by the connected/disconnected criterion. A separately reported exact result at \(r=2\) obtains two components; it does not determine the value at \(r=3\). The literature on ordinary (nonunitary) divisor-function closures addresses a different Euler-factor family.

## Limitations
No assertion is made about \(\mathcal N^*(-r)\) at noninteger parameters, global monotonicity, or the conjectured spectrum of attainable component counts. The finite certificate relies on standard exact rational operations and on the proved tail-interval reduction; the numerical endpoint approximations are illustrative only. Prior unindexed enumerations of this specific exponent remain a possible originality risk. There has been no independent scientific audit.

## References
1. C. Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654 (first submitted 9 July 2015; full exposition v3, 2018), https://arxiv.org/html/1507.02654v3 ; https://arxiv.org/abs/1507.02654 .
2. J. Nagura, *On the interval containing at least one prime number*, Proc. Japan Acad. 28 (1952), 177–181 (prime-gap theorem, as cited and used in Defant's paper).
3. N. Achenjang and A. Berger, *On Gaps in the Closures of Images of Divisor Functions*, arXiv:1808.07550 (2018), https://arxiv.org/abs/1808.07550 (ordinary divisor functions, not unitary).

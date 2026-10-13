# Fourteen connected components of the reciprocal-cube unitary-divisor range

## Finding
For positive integers \(n\), let \(\sigma_{-3}^{*}(n)\) be the sum of the reciprocal cubes of the unitary divisors of \(n\), with \(\sigma_{-3}^{*}(1)=1\). The closure
\[\mathcal R=\overline{\{\sigma_{-3}^{*}(n):n\in\mathbb N\}}\]
has **exactly fourteen connected components**. The following finite specification gives each component, including its exact endpoints.

Put
\[P=\prod_{p\text{ prime},\ p\ge11}(1+p^{-3})=\frac{\zeta(3)}{\zeta(6)\prod_{p\in\{2,3,5,7\}}(1+p^{-3})}.\]
Use four-position codes in the prime order \((2,3,5,7)\). The permitted symbols are \(H,1,2,3\) at the first position and \(H,1\) at the other positions. Set \(A_2=4\) and \(A_3=A_5=A_7=2\). For a code \(c\), let
\[L(c)=\prod_{p:c_p\ne H}(1+p^{-3c_p}),\qquad U(c)=L(c)\prod_{p:c_p=H}(1+p^{-3A_p}).\]
Here numerical symbols in codes stand for integers, while \(H\) denotes the bucket consisting of absence of that prime or an exponent at least \(A_p\). The complete list of connected components, in increasing order, is \([L(s),P U(t)]\) for the following pairs:

| Component | Start code \(s\) | End code \(t\) |
|---:|:---:|:---:|
| 1 | HHHH | 2HH1 |
| 2 | 2H1H | 2H11 |
| 3 | H1HH | 31H1 |
| 4 | H11H | 3111 |
| 5 | 21HH | 21HH |
| 6 | 21H1 | 21H1 |
| 7 | 211H | 211H |
| 8 | 2111 | 2111 |
| 9 | 1HHH | 1HH1 |
| 10 | 1H1H | 1H11 |
| 11 | 11HH | 11HH |
| 12 | 11H1 | 11H1 |
| 13 | 111H | 111H |
| 14 | 1111 | 1111 |

## Assumptions and scope
The unitary divisors \(d\) of \(n\) satisfy \(d\mid n\) and \(\gcd(d,n/d)=1\). Thus
\[\sigma_{-3}^{*}\!\left(\prod_p p^{e_p}\right)=\prod_{p:e_p\ge1}(1+p^{-3e_p}).\]
The result is for the closure of the unrestricted range on all positive integers, not the range itself. No hypotheses about the unknown distribution of special primes are required. The Euler product \(P\) converges absolutely.

## Proof
**1. The tail is an interval.** Define \(w_p=\log(1+p^{-3})\) for primes \(p\ge11\). These are positive and summable. For \(p\in\{11,13,17,19,23\}\), use the successor sets
\[\begin{aligned}
11&:\{13,17,19\},&13&:\{17,19,23,29\},\\
17&:\{19,23\},&19&:\{23,29,31\},\\
23&:\{29,31,37\}.
\end{aligned}\]
The elementary bounds \(z/(1+z)\le\log(1+z)\le z\), valid for \(z\ge0\), and five exact rational inequalities
\[\sum_{q\text{ in the listed successor set}}\frac1{q^3+1}>\frac1{p^3}\]
give \(w_p<\sum_{q>p}w_q\) in these five cases. For every prime \(p\ge29\), Nagura's prime-interval theorem gives \(p_{\mathrm{next}}<6p/5\). Repeating, the \(j\)-th following prime is less than \((6/5)^j p\). Consequently
\[\sum_{q>p}w_q\ge\frac{p^{-3}}{1+p^{-3}}\sum_{j\ge1}(5/6)^{3j}=\frac{125}{91}\frac{p^{-3}}{1+p^{-3}}>p^{-3}\ge w_p.\]
The strict inequality uses \(p\ge29\). Hence every weight is at most the sum of its successors. The elementary complete-subsums lemma now applies: for a summable positive sequence with this property, every number between zero and the total sum is an infinite subsum. Indeed, at each stage choose the current weight if the desired remainder exceeds the sum of all subsequent weights, and otherwise omit it; the remainder always remains between zero and the new available total and tends to zero. Exponentiating finite partial subsums yields
\[\overline{\left\{\prod_{p\ge11:\varepsilon_p=1}(1+p^{-3}):\varepsilon_p\in\{0,1\}\text{ with finite support}\right\}}=[1,P],\]
where \(\varepsilon_p=0\) means that the factor is omitted. Every higher prime-power factor lies between \(1\) and \(1+p^{-3}\), so allowing arbitrary exponents for primes \(p\ge11\) changes neither endpoint nor the interval.

**2. Exactly thirty-two candidate intervals.** A factor corresponding to an absent prime or an exponent \(a\ge A_p\) ranges over \(1\) and \(1+p^{-3a}\). For each \(p\in\{2,3,5,7\}\), the quantity \(1+p^{-3A_p}\) is strictly less than \(P\). One elementary proof uses
\[P\ge(1+11^{-3})(1+13^{-3})(1+17^{-3})>1+3^{-6},\]
and \(1+3^{-6}\) exceeds the other three cutoff factors. For any interval \([1,T]\) with \(T\ge P\), all the scaled intervals \([(1+p^{-3a}),(1+p^{-3a})T]\), \(a\ge A_p\), intersect \([1,T]\). Their union is exactly \([1,(1+p^{-3A_p})T]\). This argument iterates over all prime positions labeled \(H\). Fixing the other positions to the explicitly listed lower exponents proves
\[\mathcal R=\bigcup_{c\in\{H,1,2,3\}\times\{H,1\}^3}[L(c),P U(c)].\]
This union contains exactly thirty-two closed candidate intervals.

**3. Exact component count and endpoints.** Sort these thirty-two intervals by their rational lower endpoints. To decide every overlap or gap rigorously, bound the tail product using a finite product \(P_B\) over primes between \(11\) and \(B=1000\):
\[P_B\le P\le\frac{P_B}{1-1/(2B^2)},\qquad P_B=\prod_{11\le p\le B}(1+p^{-3}).\]
The upper bound follows from \(\sum_{m>B}m^{-3}\le1/(2B^2)\) and \(\prod_i(1+x_i)\le(1-\sum_i x_i)^{-1}\) for nonnegative \(x_i\) of total less than one. Thus any proposed overlap \(L(c)\le P_B U(d)\) is rigorous, and any proposed separation \(L(c)>[P_B/(1-1/(2B^2))]U(d)\) is rigorous. Tracking the maximal rational \(U\) in each merged component, exact fraction comparisons certify all thirty-one successive overlap-or-gap decisions, with fourteen merged components and the start/end codes in the table. The standalone standard-library script `verify_components.py` carries out these comparisons with rational arithmetic and fails if any enclosure is insufficient. This is exhaustive for the thirty-two intervals, not a bounded search over integers \(n\). The fourteen components are separated by strict gaps, proving the claimed exact count. \(\square\)

## Verification
Run `python3 verify_components.py` using Python 3. It checks the five finite prime-tail inequalities, the numerical implication of Nagura's ratio bound, the cutoff inequalities, all thirty-two exact candidate intervals, the fourteen component merges, and every strict gap using rational Euler-product bounds. Expected header:

`EXACT_CERTIFICATE_OK: finite_kakeya_cases=5, prime_gap_ratio=6/5, prime_cutoffs={2: 4, 3: 2, 5: 2, 7: 2}, candidate_intervals=32, connected_components=14`

The script checks the finite arithmetic; it does not prove Nagura's theorem or the infinite complete-subsums lemma. Those are used explicitly in the mathematical proof above.

## Relationship to prior work
Colin Defant's *Ranges of Unitary Divisor Functions* (first posted July 9, 2015, arXiv:1507.02654) shows that the closure \(\overline{\sigma_{-r}^{*}(\mathbb N)}\) is connected precisely up to the critical value \(r\approx1.974255\). That theorem establishes disconnection at \(r=3\), but does not specify its number of components or their boundaries. Section 3 of the full paper explicitly motivates studying these component counts. The present result determines the exact topology and boundaries at the next integer exponent after \(2\), at which the number of components rises sharply. Nagura's 1952 prime-interval theorem supplies the uniform prime-tail estimate. Nina Zubrilina's 2017 component-count bounds concern the ordinary divisor function rather than the unitary divisor function, so they do not determine the present components.

## Limitations
Only the exponent \(-3\) is classified. The result does not establish the monotonicity in \(r\) of the number of components, does not classify other exponents, and does not assert that all points inside the displayed intervals are themselves finite unitary-divisor sums. The Euler-product endpoints are limits. The finite checker relies on the independently published prime-gap bound for its infinite-tail premise.

## References
1. Colin Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654, version 1 posted 2015-07-09; expanded version 3 posted 2018-06-18. https://arxiv.org/abs/1507.02654 ; https://arxiv.org/html/1507.02654v3 .
2. Jitsuro Nagura, *On the Interval Containing At Least One Prime Number*, Proceedings of the Japan Academy **28** (1952), 177–181. DOI:10.3792/pja/1195570997 .
3. Nina Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871 (2017), dealing with the ordinary divisor function.

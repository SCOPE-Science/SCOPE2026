# Four exact closure components for reciprocal divisor sums on squarefree integers

## Finding
Let \(\mathcal S\) be the set of positive squarefree integers and let
\[
F(n)=\sum_{d\mid n}\frac{1}{d^2}=\prod_{p\mid n}\left(1+\frac{1}{p^2}\right),\qquad n\in\mathcal S.
\]
Put \(R=54/(5\pi^2)\). Then the closure in the real line of the range of \(F\) on \(\mathcal S\) is exactly
\[
\boxed{\overline{F(\mathcal S)}=[1,R]\;\cup\;[10/9,10R/9]\;\cup\;[5/4,5R/4]\;\cup\;[25/18,25R/18].}
\]
All four closed intervals are nonempty and pairwise disjoint. In particular, the closure has exactly four connected components and three bounded complementary gaps between them.

## Assumptions and scope
Here a positive integer is squarefree if no square of a prime divides it; \(1\) is squarefree. Only the reciprocal-square divisor sum and the squarefree domain are considered. Products over primes are over distinct primes. The number \(R\) is the total Euler product with the primes \(2\) and \(3\) omitted. The theorem describes a topological closure, not the existence of an integer producing every point of the intervals.

## Proof
**1. The prime tail is a full interval.** List the primes starting at \(5\) as \(q_1<q_2<\cdots\) and set \(w_j=\log(1+q_j^{-2})\). The weights are strictly positive, strictly decreasing, and summable. We prove
\[
 w_j<\sum_{i>j}w_i \quad\text{for every }j\ge1. \tag{1}
\]
For \(p\in\{5,7,11,13,17,19,23\}\), respectively choose a cutoff \(B_p\) equal to \(19,23,17,19,23,29,31\). An exact rational multiplication establishes
\[
 \prod_{p<q\le B_p\atop q\text{ prime}}(1+q^{-2})>1+p^{-2}. \tag{2}
\]
The respective positive differences, left side minus right side, are
\[
\frac{213216438}{153732003425},\quad
\frac{6767013150}{3252969192473},\quad
\frac{394}{347633},\quad
\frac{5690}{17631601},\quad
\frac{66530}{55190041},\quad
\frac{50042}{160604929},\quad
\frac{145586}{427538329}.
\]
Thus (1) holds for these seven primes, after taking logarithms.

For \(p\ge29\), let \(q_i\) be the \(i\)-th prime strictly greater than \(p\). Nagura's prime-in-a-short-interval theorem states that every real \(x\ge25\) has a prime strictly between \(x\) and \(6x/5\). Applying it successively gives \(q_i<(6/5)^i p\). For \(u>0\), \(\log(1+u)\ge u/(1+u)\), hence
\[
\begin{aligned}
\sum_{q>p}\log(1+q^{-2})
&\ge\sum_{i\ge1}\frac1{q_i^2+1}
>\frac1{p^2+1}\sum_{i\ge1}\left(\frac56\right)^{2i}\\
&=\frac{25}{11(p^2+1)}
>\frac1{p^2}
>\log(1+p^{-2}).
\end{aligned}
\]
The penultimate strict inequality holds because \(14p^2>11\). This proves (1) for every remaining prime. The strict inequalities are stronger than necessary.

**2. A no-gap lemma.** Let \((v_j)_{j\ge1}\) be positive summable real weights with \(v_j\le\sum_{i>j}v_i\) for every \(j\), and write \(V_j=\sum_{i\ge j}v_i\). Then the set of all infinite binary subsums \(\sum_{j\ge1}\epsilon_jv_j\), \(\epsilon_j\in\{0,1\}\), is exactly \([0,V_1]\). Indeed, for each residual \(x\in[0,V_j]\), the intervals \([0,V_{j+1}]\) and \([v_j,v_j+V_{j+1}]\) cover \([0,V_j]\). Choose \(\epsilon_j\) to leave the next residual in \([0,V_{j+1}]\); the residual tends to zero. Conversely, every subsum belongs to the displayed interval. Truncating any binary subsum shows that the finite subsums are dense in it.

Apply the lemma to \(v_j=w_j\). Exponentiation is continuous, so the closure of the finite products \(\prod_{p\mid n,\,p\ge5}(1+p^{-2})\) is the interval \([1,R]\), with
\[
R=\prod_{p\ge5}(1+p^{-2})
=\frac{\zeta(2)/\zeta(4)}{(1+2^{-2})(1+3^{-2})}
=\frac{54}{5\pi^2}. \tag{3}
\]
Here the standard Euler products and \(\zeta(2)/\zeta(4)=15/\pi^2\) give (3).

**3. The first two primes give four components.** A squarefree integer either contains or omits each of \(2\) and \(3\). Their two independent factors are \(5/4\) and \(10/9\); their product is \(25/18\). Thus the closure is the union of the four claimed rescalings of \([1,R]\).

It remains to prove there are no accidental mergers. Archimedes' bounds \(223/71<\pi<22/7\) imply
\[
 1<R<10/9<9/8.
\]
Indeed, \((22/7)^2<54/5\) proves \(R>1\), and \((223/71)^2>243/25\) proves \(R<10/9\). The successive left endpoints are \(1,10/9,5/4,25/18\); their consecutive ratios are \(10/9,9/8,10/9\). Because \(R<10/9\), each interval ends strictly below the next one's left endpoint. Therefore the four intervals are pairwise disjoint and exhaust the closure. \(\square\)

## Verification
The accompanying `checker.py` runs using Python 3 standard-library exact fractions, without external packages. Its seven finite-prime checks reproduce the rational differences in (2); it checks the rational bounds on \(\pi\), the separation comparisons, and confirms that 18,242 squarefree sample inputs up to 30,000 produce values in the four predicted intervals. The checker prints `ALL_CHECKS_PASSED` on success. The infinite tail argument depends on Nagura's published theorem and the explicit no-gap proof, not on a finite computation. To reproduce, run `python3 checker.py` in the directory containing this document.

## Relationship to prior work
Defant's 2015 study of generalized divisor functions on restricted domains introduces \(\sigma_{-r,k}\) and determines the threshold for dense image in the full permissible interval; it explicitly poses the problem of classifying parameter choices by their finite number of gaps. In the case \(k=1\), the permissible divisors correspond to squarefree prime exponents, and the present theorem determines that number exactly at \(r=2\), with all gap endpoints. A separate study of the unitary divisor function at the same exponent permits arbitrary positive prime exponents, unlike the strictly squarefree domain here; even when its prime tail fills an interval, its global component count does not determine the squarefree component count. Results about unrestricted ordinary divisor functions likewise do not supply this four-interval identity.

## Limitations
The theorem is only for squarefree integers and the exponent \(2\). It does not determine the component counts at other exponents or for the unrestricted ordinary or unitary divisor-sum ranges. The infinite proof assumes the classical prime-in-short-interval theorem of Nagura. An equivalent statement could exist in unindexed or incompletely accessible literature; the literature review does not constitute a uniqueness certificate. No independent audit of this result has been performed.

## References
1. C. Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663 (first public version July 9, 2015); *Uniform Distribution Theory* 10 (2015), no. 1, 19–33. https://arxiv.org/abs/1507.02663
2. J. Nagura, *On the Interval Containing at Least One Prime Number*, *Proceedings of the Japan Academy* 28 (1952), 177–181. https://doi.org/10.3792/pja/1195570997
3. C. Defant, *On the Density of Ranges of Generalized Unitary Divisor Functions*, arXiv:1507.02654 (2015). https://arxiv.org/abs/1507.02654
4. C. Sanna, *On the Closure of the Image of the Generalized Divisor Function*, *Uniform Distribution Theory* 12 (2017), 77–90. https://doi.org/10.1515/udt-2017-0016

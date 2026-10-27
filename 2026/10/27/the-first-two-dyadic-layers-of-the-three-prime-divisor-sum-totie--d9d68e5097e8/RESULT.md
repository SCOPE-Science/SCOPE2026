# The first two dyadic layers of the three-prime divisor-sum/totient equation

## Finding
Let \(\sigma(n)\) denote the ordinary sum of positive divisors and \(\varphi(n)\) Euler's totient. For all integers \(a\in\{1,2\}\), all odd primes \(3\le p<q\), and every pair of positive integers \(b,c\), the identity
\[
\sigma(2^a p^bq^c)=4\varphi(2^a p^bq^c)
\]
holds if and only if \(b=c=1\) and
\[
(a,p,q)\in\{(1,11,19),(2,17,127),(2,19,71),(2,23,43),(2,29,31)\}.
\]
Equivalently, the complete list is \(418,3596,3956,5396,8636\). These five individual values were recorded previously; the assertion is the **exclusion of all repeated odd-prime factors** at the two lowest positive exponents of \(2\).

## Assumptions and scope
The three primes \(2,p,q\) are distinct, \(p<q\); the two odd-prime exponents \(b,c\) are unrestricted positive integers, while \(a\) is precisely \(1\) or \(2\). The theorem says nothing about larger \(a\), or integers supported on other numbers of distinct primes.

## Proof
For any prime \(r\) and integer \(t\ge1\) put
\[
H_r(t)=\frac{\sigma(r^t)}{\varphi(r^t)}
=\frac{r^2}{(r-1)^2}\left(1-r^{-t-1}\right),\quad
L_r=H_r(1)=\frac{r+1}{r-1},\quad U_r=\frac{r^2}{(r-1)^2}.
\]
For fixed \(r\), the function \(H_r(t)\) is strictly increasing and \(L_r\le H_r(t)<U_r\). It decreases with \(r\) at every fixed exponent, as do its endpoints. Since \(H_2(1)=3\) and \(H_2(2)=7/2\), the proposed equality requires, respectively,
\[
H_p(b)H_q(c)=W_1:=\frac43,\qquad
H_p(b)H_q(c)=W_2:=\frac87.
\]
In particular, a necessary pair sieve is \(L_pL_q\le W_a<U_pU_q\).

**First layer \(a=1\).** The inequality \(L_7=4/3\), together with \(H_q(c)>1\), eliminates \(p\le7\). Moreover \(U_{13}U_{17}<4/3\) eliminates \(p\ge13\), because \(q\ge17\). Thus \(p=11\). The bound \(U_{11}U_{23}<4/3\) eliminates \(q\ge23\). The remaining primes are \(q=13,17,19\); the first two have \(L_{11}L_q>4/3\), and \(L_{11}L_{19}=4/3\). Strict exponent monotonicity forces \(b=c=1\), giving \(n=418\).

**Second layer \(a=2\): prime support.** As \(L_{13}=7/6>8/7\), necessarily \(p\ge17\). As \(U_{31}U_{37}<8/7\), necessarily \(p<31\); hence \(p\in\{17,19,23,29\}\). For these four primes, respectively, the inequalities
\[
U_{17}U_{167}<\frac87,\quad
U_{19}U_{83}<\frac87,\quad
U_{23}U_{47}<\frac87,\quad
U_{29}U_{37}<\frac87
\]
give upper limits on \(q\). The lower limits follow from \(L_pL_q\le8/7\). Enumerating primes in these explicit bounded intervals leaves exactly the following thirteen pairs:
\[
\begin{array}{ll}
p=17:&q\in\{127,131,137,139,149,151,157,163\},\\
p=19:&q\in\{71,73,79\},\\
p=23:&q=43,\\
p=29:&q=31.
\end{array}
\]
The four pairs \((17,127),(19,71),(23,43),(29,31)\) have \(L_pL_q=8/7\). Thus they solve the equation with \(b=c=1\), and monotonicity forbids larger exponents.

**Second layer: eliminating the other nine pairs.** For \((17,q)\) with \(q\in\{131,137,139,149,151,157\}\) and for \((p,q)=(19,73)\), the exact rational inequalities
\[
L_pU_q<\frac87<H_p(2)L_q
\]
hold. If \(b=1\), the product is strictly less than \(8/7\), regardless of \(c\); if \(b\ge2\), it is greater, regardless of \(c\). Hence these seven pairs are impossible.

There remain \((p,q)=(17,163)\) and \((19,79)\). Direct rational inequalities give \(H_p(2)U_q<8/7\), so any solution has \(b\ge3\). Multiplicativity and the equality \(\sigma(4p^bq^c)=4\varphi(4p^bq^c)\) imply \(p\mid\sigma(4p^bq^c)\), because \(p\mid\varphi(p^b)\). But \(\sigma(4)=7\) and \(\sigma(p^b)\equiv1\pmod p\), while \(p\ne7\); therefore \(p\mid\sigma(q^c)\). Since \(q\not\equiv1\pmod p\), the geometric-sum identity implies
\[
q^{c+1}\equiv1\pmod p.
\]
The multiplicative orders are \(\operatorname{ord}_{17}(163)=16\) and \(\operatorname{ord}_{19}(79)=18\), so \(c\ge15\) or \(c\ge17\), respectively. The exact rational inequalities
\[
H_{17}(3)H_{163}(15)>\frac87,\qquad
H_{19}(3)H_{79}(17)>\frac87
\]
contradict the equation. The list is exhausted.

Finally, the identities \(\sigma(2^a pq)=(2^{a+1}-1)(p+1)(q+1)\) and \(\varphi(2^a pq)=2^{a-1}(p-1)(q-1)\) verify each of the five listed cases. This proves necessity and sufficiency.

## Verification
All displayed sieve inequalities are between explicitly written rational numbers; `verify.py` recomputes them exactly with rational arithmetic. The same program independently enumerates the original divisor-sum and totient identities over both allowed \(a\), all distinct odd primes below \(167\), and odd-prime exponents from \(1\) through \(8\). The finite enumeration is a check, not a substitute for the unbounded-exponent proof. It also verifies both multiplicative-order exclusions and all five solutions.

## Relationship to prior work
Broughan and Zhou (2014) identify the even quotient-four, three-distinct-prime case as an outstanding exception to their wider classification and explicitly list these five solutions, all with odd-prime exponents one. OEIS A292422 records the **restricted** family \(2^a pq\), whereas OEIS A068390 records the unrestricted quotient-four equation. Neither cited record asserts that for \(a=1\) and \(a=2\), every solution of the larger family \(2^a p^bq^c\) must have \(b=c=1\). The present theorem establishes this additional rigidity in two complete dyadic layers.

## Limitations
No claim of new numerical examples is made. The proof does not classify \(a\ge3\), arbitrary even elements of the quotient-four family, or any number supported on a different prime count. Publication-priority checks are necessarily bounded; an unindexed equivalent prior proof cannot be ruled out merely by search.

## References
- K. A. Broughan and Q. Zhou, *On the Ratio of the Sum of Divisors and Euler's Totient Function II*, Journal of Integer Sequences 17 (2014), Article 14.9.2. https://www.kevinbroughan.nz/papers/sopFour.pdf
- OEIS A068390, *Numbers satisfying \(\sigma(n)=4\varphi(n)\)*, first recorded 2002-03-03. https://oeis.org/A068390
- OEIS A292422, *Numbers of the form \(n=2^k pq\) with two odd prime factors and \(\sigma(n)/\varphi(n)=4\)*. https://oeis.org/A292422

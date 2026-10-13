# Prime-factor support and split-prime cancellation in a modulo-three partition function

## Finding
Let \(f(n)\) count partitions of \(n\geq0\) into parts congruent to \(0\), \(1\), or \(4\) modulo \(5\), each allowed at most twice. Define
\[
\Theta(q)=\sum_{j\in\mathbb Z}(-1)^j q^{j(5j-3)/2},\qquad
 g(n)=[q^n]\Theta(q)^2,\qquad N=20n+9.
\]
For each prime \(p\), let \(e_p=\nu_p(N)\). The following formula evaluates the absolute value of the **integer** theta coefficient:
\[
|g(n)|=
\begin{cases}
\displaystyle\prod_{p\equiv 1,9\pmod{20}}(e_p+1),&
\text{if all }e_p\text{ are even for }p\equiv3\pmod4\text{ and for }p\equiv13,17\pmod{20},\\[2pt]
0,&\text{otherwise.}
\end{cases}
\]
The product is over prime divisors of \(N\) in the indicated classes and an empty product means \(1\). Since \(f(n)\equiv g(n)\pmod3\), this yields a **necessary and sufficient** condition:
\[
\boxed{f(n)\not\equiv0\pmod3
\iff\begin{cases}
e_p\text{ is even for every }p\equiv3\pmod4,\\
e_p\text{ is even for every }p\equiv13,17\pmod{20},\\
e_p\not\equiv2\pmod3\text{ for every }p\equiv1,9\pmod{20}.
\end{cases}}
\]
In particular, \(N=629=17\cdot37\) is a sum of two squares yet \(g(31)=0\) and \(f(31)\equiv0\pmod3\), illustrating cancellation not detected by the classical representation obstruction.

## Assumptions and scope
All statements apply for **every integer** \(n\ge0\), without asymptotic qualifications. The integer \(N=20n+9\) is positive, odd, congruent to \(4\) modulo \(5\), and is coprime to \(10\). Thus primes \(2\) and \(5\) never occur. The result evaluates the absolute value of \(g(n)\), not the exact unrestricted partition number \(f(n)\), and the partition conclusion is only modulo \(3\). The sign of a nonzero \(g(n)\) is not asserted by the product.

## Proof
**1. Theta reduction.** In the formal power-series ring over \(\mathbb Z/3\mathbb Z\), each permitted positive part \(k\) contributes
\[
1+q^k+q^{2k}=\frac{1-q^{3k}}{1-q^k}\equiv(1-q^k)^2\pmod3.
\]
The Jacobi triple product converts the product over permitted residues into \(\Theta(q)\); hence \(f(n)\equiv g(n)\pmod3\). This is the reduction established in Proposition 3.3 of Li's cited paper. The following coefficient and prime-factor analysis is independent of the partition product.

**2. A signed Gaussian norm sum.** An ordered pair \((a,b)\in\mathbb Z^2\) in the coefficient of \(\Theta^2\) has exponent \(n\) exactly when
\[
X=5(a+b)-3,\qquad Y=5(a-b),\qquad X^2+Y^2=20n+9.
\]
Conversely, every solution \((X,Y)\in\mathbb Z^2\) of this norm equation with \(X\equiv2\pmod5\), \(Y\equiv0\pmod5\) has the unique inverse \(a=(X+Y+3)/10\), \(b=(X-Y+3)/10\): divisibility by \(5\) follows from the congruences, and divisibility by \(2\) from the odd norm, which forces \(X,Y\) to have opposite parities. The theta sign is \((-1)^{a+b}=(-1)^{(X+3)/5}=(-1)^Y\). Therefore
\[
g(n)=\sum_{\substack{X^2+Y^2=N\\X\equiv2\ (\mathrm{mod}\ 5)\\Y\equiv0\ (\mathrm{mod}\ 5)}}(-1)^Y.
\]
Since \(N\equiv4\pmod5\), the only square pairs modulo \(5\) have one coordinate zero and the other equal to \(\pm2\). Every orbit of the four Gaussian units \(\{1,-1,i,-i\}\) on Gaussian integers of norm \(N\) thus contains **exactly one** representative \(X+iY\) with \(X\equiv2\pmod5\), \(Y\equiv0\pmod5\). This representative is called *canonical*. The coefficient is the sum of signs \((-1)^Y\) over unit orbits.

**3. Factorization and local sign changes.** Unique factorization in \(\mathbb Z[i]\) shows that representations exist only if every rational prime \(p\equiv3\pmod4\) divides \(N\) to even order. Under this condition every Gaussian unit orbit of norm \(N\) corresponds uniquely to an exponent choice \(j_p\in\{0,1,\ldots,e_p\}\) for each split prime \(p\equiv1\pmod4\), by distributing the factors between \(\pi_p\) and \(\overline\pi_p\), where \(p=\pi_p\overline\pi_p\); inert factors contribute a fixed real factor. Neither ramified prime occurs.

Compare two orbits differing by replacing one factor \(\overline\pi_p\) with \(\pi_p\). In the rings modulo \(2\) and \(5\), the quotient \(\pi_p/\overline\pi_p\) is defined because \(p\) is coprime to \(10\). It is congruent to \(1\) modulo \(2\), since \(\pi_p-\overline\pi_p\) is divisible by \(2\). Modulo \(5\), write \(\pi_p=A+iB\) and use
\[
\frac{\pi_p}{\overline\pi_p}=\frac{A^2-B^2+2ABi}{p}.
\]
If \(p\equiv\pm1\pmod5\), one of \(A,B\) is zero modulo \(5\), and the quotient is \(\pm1\). If \(p\equiv\pm2\pmod5\), the squares \(A^2,B^2\) are equal and nonzero modulo \(5\), so the quotient is \(\pm i\). These are respectively the split-prime classes \(p\equiv1,9\pmod{20}\) and \(p\equiv13,17\pmod{20}\).

The parity classes of the two coordinates do not change before canonical reorientation because the quotient is \(1\) modulo \(2\). A quotient \(\pm1\) modulo \(5\) requires only multiplication by a real unit to restore the canonical orientation and therefore preserves the imaginary-coordinate parity. A quotient \(\pm i\) requires a quarter-turn, exchanging the coordinate parities. Since \(N\) is odd, exactly one coordinate is odd, so this **reverses** the sign \((-1)^Y\). Thus varying \(j_p\) by one preserves the sign for a split prime in classes \(1,9\) and reverses it for one in classes \(13,17\), always modulo \(20\).

**4. Independent local sums.** Fix a reference factorization and sum its signs over all independent exponent choices. Up to one global sign, each prime in classes \(1,9\) contributes \(e_p+1\), whereas each prime in classes \(13,17\) contributes the alternating sum
\[
\sum_{j=0}^{e_p}(-1)^j=\begin{cases}1,&e_p\text{ even},\\0,&e_p\text{ odd}.
\end{cases}
\]
An odd inert exponent supplies no norm representations. Consequently the displayed exact formula for \(|g(n)|\) follows. The coefficient is zero exactly in the stated zero cases, and otherwise has absolute value the product. Reduction modulo \(3\) gives the prime-factor criterion because \(e_p+1\equiv0\pmod3\) exactly when \(e_p\equiv2\pmod3\). This completes the proof.

## Verification
The standalone Python program `verify.py`, requiring only the Python standard library, independently computes restricted partitions modulo \(3\) for all \(0\le n\le1200\), evaluates the signed Gaussian norm sum, and compares absolute coefficients with the prime-factor formula for all \(0\le n<10000\). It also tests the two-squares cancellation example \(N=629\). Run `python verify.py`; the expected output is preserved as `verification_output.txt`. This finite check is corroborative only; the infinite proof rests on the theta identity and Gaussian unique factorization.

## Relationship to prior work
Li, *A quadratic-residue dichotomy for two partition functions modulo 3* (arXiv:2609.22340v1, first public posting 2026-09-16), defines the same restricted partition function and proves the theta-squared reduction in Section 3. Its Sections 4–7 derive congruences and self-similarity for primes \(p\equiv3\pmod4\), without the present all-index prime-exponent classification. Section 8.2 explains why the same **progression self-similarity** mechanism does not extend to primes \(p\equiv1\pmod4\). That limitation is compatible with, rather than equivalent to, the present Gaussian unit-orbit cancellation calculation, which explicitly handles those split primes. Jacobi's triple-product theorem and unique factorization in the Gaussian integers are classical inputs, not claimed discoveries.

## Limitations
The result does not recover the unrestricted integers \(f(n)\) or determine the sign of \(g(n)\) when nonzero. It does not establish density estimates for the nonvanishing indices or extend to different residue restrictions and multiplicities. It has only self-review; no independent audit has been performed. An equivalent unindexed or otherwise inaccessible prime-factor formulation could exist.

## References
1. Jiyuan Li, *A quadratic-residue dichotomy for two partition functions modulo 3*, arXiv:2609.22340v1 (first posted 2026-09-16), §§2–8, https://arxiv.org/abs/2609.22340.
2. G. E. Andrews, *The Theory of Partitions*, Addison-Wesley (1976), reissued Cambridge University Press (1998), classical Jacobi triple-product background.
3. The classical Gaussian-integer unique-factorization and sum-of-two-squares theorems.

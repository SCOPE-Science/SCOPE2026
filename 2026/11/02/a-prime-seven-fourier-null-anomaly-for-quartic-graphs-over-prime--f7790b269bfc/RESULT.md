# A prime-seven Fourier-null anomaly for quartic graphs over prime-square rings

## Finding
For any prime \(p\ge5\), put \(R=\mathbb Z/p^2\mathbb Z\), and let \(C_p=\{(x,x^4):x\in R\}\subset R^2\). For \(a,b\in R\), define its unnormalized Fourier coefficient
\[
F_p(a,b)=\sum_{x\in R}\exp\!\left(2\pi i(ax+bx^4)/p^2\right).
\]
Write \(\bar a,\bar b\in\mathbb F_p\) for reductions, and \(d=\gcd(3,p-1)\). **All coefficients are zero or nonzero as follows.**

* **Primitive frequencies** \((\bar a,\bar b)\ne(0,0)\): \(F_p(a,b)\ne0\) precisely when \(\bar b\ne0\) and the equation \(\bar a+4\bar b z^3=0\) has a solution \(z\in\mathbb F_p\). Thus for each nonzero \(\bar b\), exactly \(1+(p-1)/d\) reduced \(\bar a\) values survive.
* **Imprimitive frequencies** \(a=pA,b=pB\): the coefficient vanishes precisely when \(B=0,A\ne0\), **or** when \(p=7\), \(B\ne0\) and \(A/B\in\{3,4\}\subset\mathbb F_7\). All other imprimitive frequencies survive.

Let \(T_p\) be additive convolution by \(\mathbf1_{C_p}\) on \(\ell^2(R^2)\). Its exact complex rank is
\[
\boxed{\operatorname{rank}T_p=p^2(p-1)\left(1+\frac{p-1}{d}\right)+p^2-(p-1)\left(1+2\mathbf1_{\{p=7\}}\right).}
\]
For example, the ranks for \(p=5,7,11\) are \(521,913,13421\), in dimensions \(625,2401,14641\) respectively. As \(p\to\infty\) through primes congruent to \(2\pmod3\), the rank proportion tends to \(1\); through primes congruent to \(1\pmod3\), it tends to \(1/3\). The prime \(7\) produces an additional imprimitive nullspace of dimension \(12\), absent from every other prime.

## Assumptions and scope
The statement includes every additive frequency of \(R^2\), every prime \(p\ge5\), and the exact monomial graph \(x\mapsto x^4\). Complex Fourier transforms and convolution are unnormalized; nonzero scaling of the operator does not affect rank. It does not address other polynomials, higher prime-power moduli, or primes two and three.

## Proof
**1. Cyclotomic noncancellation.** For a nonnegative-coefficient polynomial \(P(X)=\sum_{j=0}^{p^2-1}c_jX^j\), \(P(\zeta_{p^2})=0\) if and only if \(c_{r}=c_{r+p}=\cdots=c_{r+(p-1)p}\) for every \(0\le r<p\). This is the minimal-polynomial identity \(\Phi_{p^2}(X)=1+X^p+\cdots+X^{(p-1)p}\). In particular a sum of between one and four \(p^2\)-th roots cannot vanish for \(p\ge5\).

**2. Primitive stationary phases.** Write \(x=x_0+pz\) with \(x_0,z\in\{0,\dots,p-1\}\). Exact Taylor expansion modulo \(p^2\) gives
\[
F_p(a,b)=p\sum_{\substack{x_0\in\mathbb F_p\\\bar a+4\bar b x_0^3=0}}
\exp\!\left(\frac{2\pi i}{p^2}(a x_0+b x_0^4)\right).
\]
For a primitive frequency the derivative equation has zero, one or three distinct solutions. By step 1 no sum with one or three \(p^2\)-th roots can cancel. If \(\bar b=0\) then \(\bar a\ne0\) and there is no root. If \(\bar b\ne0\), the number of possible right-hand sides of the cube map, including zero, is \(1+(p-1)/d\). This proves the primitive condition and counts its surviving frequencies.

**3. Imprimitive cyclotomic criterion.** When \(a=pA,b=pB\), every input value modulo \(p\) occurs in \(p\) lifts, hence
\[
F_p(pA,pB)=p\sum_{z\in\mathbb F_p}\exp\!\left(\frac{2\pi i}{p}(Az+Bz^4)\right).
\]
Since this is a sum of exactly \(p\) \(p\)-th roots, it vanishes if and only if the function \(z\mapsto Az+Bz^4\) permutes \(\mathbb F_p\). This follows because the only integer polynomial of degree at most \(p-1\) vanishing at \(\zeta_p\), up to scaling, is \(\Phi_p=1+X+\cdots+X^{p-1}\).

The cases \(B=0,A\ne0\) give linear permutations. With \(A=0,B\ne0\), the fourth-power map is not a permutation because \(p-1\) is even. If both are nonzero, rescale to \(z^4+cz\), \(c=A/B\). The Masuda–Zieve theorem [1, Thm. 1.3] requires \(\gcd(3,p-1)>\sqrt p-1\) whenever this binomial permutes a prime field. Thus \(p<16\). For \(p=5,7,11,13\), direct exact enumeration of \(z^4+cz\) for every \(c\in\mathbb F_p^\times\) shows that only \(p=7\), \(c=3\) or \(c=4\) work. This is a finite exhaustive calculation with a fully specified field and bounds; the theorem excludes all larger primes. The imprimitive criterion follows.

**4. Rank and asymptotics.** The \((p-1)(1+(p-1)/d)\) primitive reduced frequency classes each have \(p^2\) lifts. Among the \(p^2\) imprimitive frequencies, \(p-1\) linear and an extra \(12\) at \(p=7\) vanish. Summing the surviving frequencies gives the displayed rank. Character diagonalization of finite abelian convolution identifies this count with complex operator rank. Dividing by \(p^4\) and taking the two congruence classes yields the stated limits.

## Verification
The standalone `checks/verify.py` directly computes each character sum as an integer-coefficient polynomial modulo \(\Phi_{p^2}\), exhaustively for **every frequency** of \(R^2\) for \(p=5,7,11\). Its decisions are exact, not floating-point. All checks match the theorem and it separately enumerates all nonzero quartic-linear binomial coefficients at primes \(13,17,19\). Run `python3 checks/verify.py`; the final marker is `QUARTIC_PRIME_SQUARE_CYCLOTOMIC_OK`. The infinite proof depends on the published Masuda–Zieve bound and the finite exhaustive enumeration only for the four remaining primes; not on an extrapolation from tests.

## Relationship to prior work
Masuda–Zieve [1] prove a strong nonexistence theorem for permutation binomials over prime fields; its reduction to four small primes is a substantive step in the present complete low-conductor Fourier-zero classification. Cochrane–Zheng [2] develop general stationary-phase methods for prime-power polynomial exponential sums; the primitive-character step follows this classical principle. The previously published result *All exponential spectra of the cubic graph over prime-square cyclic rings* [3] treats the different degree-three graph and derives its own Fourier-zero characterization. That cubic result is not claimed here. Existing finite-field quartic-curve fourth-moment work [4] concerns a different Fourier operator. No inspected source states the quartic graph's all-frequency rank law or the special extra \(p=7\) null directions; mathematical equivalence from other specialized work remains possible.

## Limitations
The operator's nonzero eigenvalue magnitudes are not classified. The Masuda–Zieve nonexistence theorem is used as an established input. All finite exceptions are exhaustively enumerated; the published theorem excludes further primes. This self-review is not independent validation. The comparison with specialized quartic exponential-sum literature is bounded.

## References
1. A. M. Masuda and M. E. Zieve, *Permutation binomials over finite fields*, arXiv:0707.1108v1, first posted 2007-07-07, Theorem 1.3.
2. T. Cochrane and Z. Zheng, *Pure and mixed exponential sums*, Acta Arithmetica 91 (1999), 249–278, DOI 10.4064/aa-91-3-249-278.
3. *All exponential spectra of the cubic graph over prime-square cyclic rings*, public repository identifier 2026/10/11/SCOPE-all-exponential-spectra-of-the-cubic-graph-over-prime-square-cyc--a783058468ac, RESULT.md, Step 1.
4. *Exact additive energy of the finite-field quartic graph*, public record 2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f.

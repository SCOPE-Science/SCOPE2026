# A two-term counting law for derivative–totient coincidences with a fixed prime factor

## Finding

Let \(D\) be the arithmetic derivative, with \(D(r)=1\) for primes \(r\) and the Leibniz rule, and let \(\varphi\) be Euler's totient. Fix an odd prime \(p\). Define
\[
N_p(X)=\#\{n\le X:n=p^a q^b,\ q>p\text{ prime},\ a,b\ge1,\ D(n)=\varphi(n)\}.
\]
Set \(L=\log X\), \(\ell=\log L\), \(m=\log\ell\), and
\[
H_p=\sum_{t=1}^{p-2}\frac1t,\qquad J_p=\sum_{t=1}^{p-2}\frac{\log(p/t)}t.
\]
As \(X\to\infty\), with \(p\) fixed,
\[
\boxed{N_p(X)=\frac{pL}{(p-1)\ell^2}\left[H_p+\frac{(2m+1)H_p-2J_p}{\ell}+O_p\!\left(\frac{m^2}{\ell^2}\right)\right].}
\]
In particular, \(N_p(X)\sim pH_p\log X/((p-1)(\log\log X)^2)\), and the exact analogous count for \(p=2\) is zero.

## Assumptions and scope

All logarithms are natural. The asymptotic concerns integers with exactly two **distinct** prime factors and prescribed smaller factor \(p\), not the unrestricted coincidence set. The constants implied by \(O_p\) may depend on the fixed prime \(p\). The theorem makes no uniform claim as \(p\) grows with \(X\). The harmonic symbol \(H_p\) is defined above and is not the conventional sum through \(p\).

## Proof

**1. Exact prime parametrization.** For \(n=p^a q^b\), the defining formulas yield
\[
D(n)=a p^{a-1}q^b+b p^a q^{b-1},\quad
\varphi(n)=(p-1)p^{a-1}(q-1)q^{b-1}.
\]
Canceling the positive common factor gives
\[
aq+bp=(p-1)(q-1).
\]
Since \(a,b\ge1\), necessarily \(1\le a\le p-2\). Put \(t=p-1-a\). Exactly one exponent pair exists for a given prime \(q>p\) if and only if
\[
1\le t\le p-2,\qquad tq\equiv-1\pmod p,
\]
and then
\[
a=p-1-t,\quad b=\frac{tq-(p-1)}p>0.
\]
For each \(t\), the allowed primes lie in exactly one reduced residue class modulo \(p\); distinct \(t\)'s give disjoint classes. There is no allowable \(t\) for \(p=2\). This parametrization is consistent with the earlier OEIS A166374 existence comment; **existence or parametrization alone is not the claimed new result**.

**2. Converting the size restriction to prime cutoffs.** On the class associated with \(t\),
\[
\log n=\frac tp q\log q-\frac{p-1}{p}\log q+(p-1-t)\log p.
\]
Let \(c_t=p/t\) and define \(Q_t=c_t L/W(c_t L)\), where \(W\) is the positive Lambert function, so \(Q_t\log Q_t=c_tL\). For large \(L\), the left side is strictly increasing in \(q\). Its difference from \((t/p)q\log q\) is \(O_p(\log q)\), whereas the latter has derivative \((t/p)(1+\log q)\); therefore the actual cutoff differs from \(Q_t\) by \(O_p(1)\). The number of admitted primes is consequently \(\pi(Q_t;p,r_t)+O_p(1)\), with \(r_t\equiv-t^{-1}\pmod p\). The possible endpoint error remains bounded because the cutoff changes by a bounded amount.

**3. Prime distribution in fixed progressions.** The prime number theorem in arithmetic progressions, with a fixed modulus and a power-saving error stronger than any fixed inverse logarithm, gives
\[
N_p(X)=\frac1{p-1}\sum_{t=1}^{p-2}\operatorname{Li}(Q_t)
+O_{p,A}\!\left(\frac{L}{\ell^A}\right)
\]
for every prescribed constant \(A>0\). Here \(\operatorname{Li}\) denotes the logarithmic integral; for large \(L\), each \(Q_t\asymp_p L/\ell\), so the standard fixed-modulus prime-counting error is negligible to every term displayed.

**4. Uniform finite-sum expansion.** Write \(c=\log(p/t)\). Since there are only \(p-2\) possible values of \(t\), every following error is uniform over the sum:
\[
W(e^cL)=\ell+c-m+O_p(m/\ell),\quad
Q_t=\frac{pL}{t\ell}\left(1+\frac{m-c}{\ell}+O_p(m^2/\ell^2)\right).
\]
The classical expansion \(\operatorname{Li}(y)=y/\log y+y/(\log y)^2+O(y/(\log y)^3)\) and \(\log Q_t=\ell+c-m+O_p(m/\ell)\) imply
\[
\operatorname{Li}(Q_t)=\frac{pL}{t\ell^2}\left(1+\frac{2m-2\log(p/t)+1}{\ell}+O_p(m^2/\ell^2)\right).
\]
Summing first \(1/t\) and then \(\log(p/t)/t\) proves the displayed two-term law, including the asserted remainder. The asymptotic also proves infinitely many distinct integers in each fixed odd-prime layer. \(\square\)

## Verification

The included `verify.py` uses only the Python standard library and independently enumerates short Diophantine solutions for prime pairs, compares the full derivative/totient on complete small domains, and compares two separate exact counting procedures at high integer cutoffs. The checked output is `VERIFY_OK: 220 independent two-prime Diophantine enumerations; 3 direct semiprime-support equality cases through 180000; 15 exact high-cutoff counting comparisons.` These checks do not verify the infinite asymptotic; that follows from the proof and the cited prime number theorem in progressions.

## Relationship to prior work

Ufnarovski and Åhlander (2003), Theorem 1, supply the standard arithmetic-derivative formula. OEIS A166374 explicitly documents the equality \(D(n)=\varphi(n)\); its August 21, 2014 comment already establishes existence of two-prime examples by solving a linear Diophantine equation. Neither that existence assertion nor any single example is claimed to be novel here. Kovič (2012) develops arithmetic antiderivatives and related methods. The contribution assessed here is the **explicit fixed-prime two-term counting asymptotic and harmonic secondary constant** for those previously recognized solutions. The analytic component invokes the classical prime number theorem in fixed arithmetic progressions, not a new prime-distribution theorem.

## Limitations

No claim is made about unrestricted coincidences, bounded total prime-support count across varying \(p\), or uniform asymptotics for growing \(p\). A complete originality guarantee is unavailable: an equivalent fixed-prime asymptotic may exist in specialized or unindexed literature. Independent validation has not occurred. Finite computational checks alone cannot establish the asymptotic.

## References

1. V. Ufnarovski and B. Åhlander, *How to Differentiate a Number*, Journal of Integer Sequences **6** (2003), Article 03.3.4, published September 17, 2003. https://cs.uwaterloo.ca/journals/JIS/VOL6/Ufnarovski/ufnarovski.pdf
2. OEIS A166374, *Numbers whose arithmetic derivative is equal to Euler totient function*, first recorded October 13, 2009; Robert Israel's two-prime existence comment, August 21, 2014. https://oeis.org/A166374
3. M. Kovič, *The Arithmetic Derivative and Antiderivative*, Journal of Integer Sequences **15** (2012), Article 12.3.8. https://cs.uwaterloo.ca/journals/JIS/VOL15/Kovic/kovic4.pdf
4. Classical prime number theorem for fixed arithmetic progressions, e.g. the Siegel–Walfisz theorem and its fixed-modulus consequence. https://en.wikipedia.org/wiki/Siegel%E2%80%93Walfisz_theorem

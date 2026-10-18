# Exact characteristic-two truncated Möbius autocorrelation and its quartic cutoff law

## Finding

For every nonzero polynomial \(a\in\mathbb F_2[t]\) and integer \(M\ge1\), let
\[
\mu_M(f)=\mu(f)^2(-1)^{\omega_M(f)},\qquad
\omega_M(f)=\#\{P:\ P\text{ monic irreducible},\ P\mid f,\ \deg P\le M\}.
\]
The limit
\[
L_a(M)=\lim_{n\to\infty}2^{-n}\!\sum_{\substack{f\ \mathrm{monic}\\\deg f=n}}\mu_M(f)\mu_M(f+a)
\]
exists, is nonzero, and has the following explicit Euler product. Write \(Q_P=2^{\deg P}\), \(v_P(a)\) for multiplicity, and
\[
 c_{P,a}=\begin{cases}1-2/Q_P^2,&v_P(a)=1,\\1-1/Q_P^2,&v_P(a)\ge2.\end{cases}
\]
Then
\[
 L_a(M)=\prod_{P\mid a}c_{P,a}
 \prod_{\substack{P\nmid a\\\deg P\le M}}\left(1-\frac4{Q_P}+\frac2{Q_P^2}\right)
 \prod_{\substack{P\nmid a\\\deg P>M}}\left(1-\frac2{Q_P^2}\right).
\]
All products range over monic irreducibles. If \(r(a)=\#\{z\in\mathbb F_2:a(z)=0\}\), then
\[
 \operatorname{sgn}(L_a(M))=(-1)^{r(a)}\quad(M\ge1).
\]
Moreover, with Euler's constant \(\gamma\),
\[
\lim_{M\to\infty}M^4L_a(M)=C_a\ne0,
\]
where the absolutely convergent, nonzero normalized product is
\[
 C_a=e^{-4\gamma}
 \prod_{P\mid a}\frac{c_{P,a}}{(1-Q_P^{-1})^4}
 \prod_{P\nmid a}\frac{1-4Q_P^{-1}+2Q_P^{-2}}{(1-Q_P^{-1})^4}.
\]
In particular \(\operatorname{sgn}(C_a)=(-1)^{r(a)}\). The fourth-power decay and the sign criterion hold in the characteristic-two case excluded from the motivating sieve theorem.

## Assumptions and scope

The coefficient field is exactly \(\mathbb F_2\). The shift \(a\) is fixed and nonzero, not necessarily monic; \(n\to\infty\) is taken first at each fixed cutoff \(M\ge1\). For \(n>\deg a\), both \(f\) and \(f+a\) are monic of degree \(n\). The Möbius function on monic polynomials is zero on polynomials divisible by a square of a nonconstant irreducible, and otherwise is the sign of the number of distinct irreducible factors. Every sum is over exactly \(2^n\) monic polynomials. The result does not assert a uniform estimate when \(M\) grows simultaneously with \(n\).

## Proof

**1. Exact local factors.** Fix monic irreducible \(P\), and let \(Q=2^{\deg P}\). The product \(\mu_M(f)\mu_M(f+a)\) is a product of local weights, with local weight zero when \(P^2\mid f(f+a)\); otherwise each of \(P\mid f\) and \(P\mid(f+a)\) contributes a minus sign when \(\deg P\le M\). All local conditions depend only on \(f\bmod P^2\).

If \(P\nmid a\), the two square-divisibility forbidden classes, \(0\) and \(-a\) modulo \(P^2\), are distinct. There are \(Q-1\) permitted classes in each of the disjoint residue families \(f\equiv0\pmod P\) and \(f\equiv-a\pmod P\). Hence \(2(Q-1)\) classes carry sign minus when \(\deg P\le M\), while two classes carry weight zero. The average over \(Q^2\) classes is \(1-4/Q+2/Q^2\). For \(\deg P>M\), every squarefree local class has weight plus, giving \(1-2/Q^2\).

If \(P\mid a\), the two polynomial values are divisible by \(P\) simultaneously, so their sign contributions cancel regardless of \(M\). If \(v_P(a)=1\), the two forbidden square-residue classes are distinct, giving \(1-2/Q^2\). If \(v_P(a)\ge2\), these classes coincide and the factor is \(1-1/Q^2\). These are \(c_{P,a}\).

**2. Passage from finite conditions to the infinite product.** For any finite collection \(\mathcal P\) of prime polynomials, the Chinese remainder theorem and exact equidistribution of monic degree-\(n\) polynomials modulo \(\prod_{P\in\mathcal P}P^2\) imply that the average of the finite product of local weights equals the product of their local averages once \(n\ge2\sum_{P\in\mathcal P}\deg P\). Fix \(K\ge M\). The difference between the true correlation and this finite product over \(\deg P\le K\) can occur only if \(P^2\mid f\) or \(P^2\mid(f+a)\) for some \(\deg P>K\). For \(n>\deg a\), primes with \(2\deg P>n\) cannot cause either event, while each remaining square-divisibility event has exact probability \(2^{-2\deg P}\). The union bound gives
\[
 \left|2^{-n}\!\sum_{\deg f=n}\mu_M(f)\mu_M(f+a)
 -\prod_{\deg P\le K}c_P(a,M)\right|
 \le2\sum_{d>K}\pi_2(d)2^{-2d}
 \le2\sum_{d>K}\frac{2^{-d}}d,
\]
where \(\pi_2(d)\le2^d/d\) counts degree-\(d\) monic irreducibles. This tends to zero independently of \(n\), establishing existence, equality with the product and absolute convergence of its high-degree tail.

**3. Nonvanishing and sign.** Every factor attached to \(P\mid a\) is strictly positive, as is every high-degree factor. A small-prime factor \(1-4/Q+2/Q^2\) is negative only when \(Q=2\) and is then exactly \(-1/2\); for \(Q\ge4\) it is strictly positive. The only two degree-one primes are \(t\) and \(t+1\). They divide \(a\) exactly when the corresponding elements of \(\mathbb F_2\) are roots of \(a\). Thus there are \(2-r(a)\) negative factors for every \(M\ge1\). Their parity equals that of \(r(a)\), proving the sign criterion. Absolute convergence of the positive tail and absence of zero factors give \(L_a(M)\ne0\).

**4. Sharp cutoff asymptotic.** Put \(F_M=\prod_{\deg P\le M}(1-Q_P^{-1})\). The irreducible-counting identity \(\sum_{d\mid m}d\pi_2(d)=2^m\) yields
\[
 -\log F_M=H_M+R_M,\qquad
 R_M=\sum_{d\le M}\pi_2(d)\sum_{\substack{k\ge2\\kd>M}}\frac{2^{-kd}}k.
\]
Here \(R_M\to0\) by dominated convergence, since \(\sum_{d\ge1}\pi_2(d)\sum_{k\ge2}2^{-kd}/k<\infty\). Since \(H_M=\log M+\gamma+o(1)\), we obtain \(F_M\sim e^{-\gamma}/M\).

For each \(P\nmid a\), the quotient \((1-4/Q_P+2/Q_P^2)/(1-1/Q_P)^4=1+O(Q_P^{-2})\); the product of these quotients therefore converges absolutely and is nonzero (possibly with negative sign). The finitely many primes dividing \(a\) contribute their indicated quotients. The product over \(\deg P>M\) of \(1-2/Q_P^2\) tends to one. Consequently \(L_a(M)/F_M^4\) converges to the nonzero product displayed for \(e^{4\gamma}C_a\), and \(M^4L_a(M)\to C_a\). This completes the proof.

## Verification

`VERIFY.py` is a standalone Python standard-library checker. It independently enumerates every polynomial residue class modulo \(P^2\) for each monic irreducible of degree at most three over \(\mathbb F_2\), five different shifts, and four cutoffs; all 100 exact rational local-factor tests pass. It also enumerates monic polynomials in several degrees up to eleven and computes both truncated Möbius weights by explicit divisibility and square-divisibility. Those finite computations test the local arithmetic but are not substitutes for the infinite-product and asymptotic arguments above. The recorded output is in `VERIFY_OUTPUT.txt`.

## Relationship to prior work

Chatterjee, *Chowla Conjecture for the truncated Möbius function over* \(\mathbb F_q[t]\) (arXiv:2610.06471v1, first posted 5 October 2026), defines exactly the same truncation and proves a two-point estimate for \(q\ne2\), using a bivariate probabilistic sieve. Its Section 4 identifies a sieve degeneracy at norm two; characteristic two is explicitly excluded. The present result treats precisely \(q=2\) by an elementary finite-residue product, and identifies the nonzero fixed-cutoff limit, its sign and sharp fourth-power cutoff rate. It does not strengthen the source's simultaneous degree/cutoff range.

Mangerel's bivariate Erdős–Kac paper (arXiv:1612.09544) treats the analogous truncated Möbius correlation over the integers, not the fixed polynomial field \(\mathbb F_2[t]\). Carmon's characteristic-two autocorrelation paper (arXiv:1409.3694) studies the ordinary, untruncated Möbius function with field size tending to infinity at fixed degree, not the present order of limits or local signed product. The local two-polynomial squarefree sieve principle is classical; neither that principle nor general CRT equidistribution is claimed as new.

## Limitations

Only the iterated limit, first polynomial degree and then the cutoff, is covered. A sharp estimate uniform in a jointly growing cutoff would require additional arguments. Only two-point correlations and shifts by a fixed nonzero polynomial are considered. This finding is self-reviewed and has not undergone independent audit; unindexed equivalent earlier literature remains a risk.

## References

1. A. Chatterjee, *Chowla Conjecture for the truncated Möbius function over* \(\mathbb F_q[t]\), arXiv:2610.06471v1 (5 October 2026), https://arxiv.org/html/2610.06471v1 .
2. A. P. Mangerel, *On the Bivariate Erdős–Kac Theorem and Correlations of the Möbius Function*, arXiv:1612.09544 (2016), https://ar5iv.labs.arxiv.org/html/1612.09544 .
3. D. Carmon, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field in characteristic 2*, arXiv:1409.3694 (2014); *Philosophical Transactions A* 373 (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4375379/ .

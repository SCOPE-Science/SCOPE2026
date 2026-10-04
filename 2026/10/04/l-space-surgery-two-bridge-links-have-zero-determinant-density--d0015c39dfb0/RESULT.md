# L-space-surgery two-bridge links have zero determinant density
## Finding
For every even integer \(p\ge4\), let \(c_p\) denote the number, up to mirror, of unoriented two-bridge link types with Schubert numerator \(p\) that admit a non-trivial L-space surgery. Then
\[
c_p=
\frac{
\tau(p-1)+\tau(p+1)-2
+\mathbf 1_{p-1\ {\rm square}}
+\mathbf 1_{p+1\ {\rm square}}
}{2}.
\]
The exceptional initial case is the Hopf link, for which \(c_2=1\).

Let
\[
L(X)=\sum_{\substack{2\le p\le X\\2\mid p}}c_p.
\]
Then
\[
L(X)\sim\frac14X\log X.
\]

Let \(B(X)\) be the number, up to mirror, of all unoriented two-bridge link types with even Schubert numerator at most \(X\). Then
\[
B(X)\sim\frac{X^2}{4\pi^2},
\]
and consequently
\[
\frac{L(X)}{B(X)}
\sim
\frac{\pi^2\log X}{X}
\longrightarrow0.
\]

For a two-bridge link the Schubert numerator is the order of the first homology of the double branched cover, so it is also the usual determinant cutoff. Thus links admitting non-trivial L-space surgeries form a zero-density subfamily of two-component two-bridge links under this natural complexity ordering.

## Assumptions and scope
The two-bridge link \(b(p,q)\) is taken in the convention used by Santoro--Zhou and Lyu--Nie: \(p>0\), \(p\) is even for a two-component link, \(q\) is odd, \(\gcd(p,q)=1\), and one may choose \(0<|q|\le p/2\). Passing to mirror identifies the signs of \(q\), so a positive representative \(1\le q\le p/2\) is used.

Schubert's classification identifies unoriented two-bridge links with the same numerator through inversion of the denominator modulo \(p\). After also quotienting by mirror, the positive representative is acted on by
\[
q\longmapsto \min(q^{-1}\bmod p,\ p-(q^{-1}\bmod p)).
\]

The recent L-space-surgery classification gives the criterion
\[
b(p,q)\text{ admits a non-trivial L-space surgery}
\quad\Longleftrightarrow\quad
p\equiv\pm1\pmod{|q|}.
\]

No assertion is made about how many surgery slopes on an admissible link are L-space slopes; only the existence of at least one non-trivial L-space surgery is counted.

## Proof
Fix an even integer \(p\ge4\). For a positive canonical denominator \(q\), the L-space criterion is equivalent to
\[
q\mid p-1
\quad\text{or}\quad
q\mid p+1.
\]
Since \(p-1\) and \(p+1\) are odd, every such \(q\) is automatically odd and coprime to \(p\).

Every proper divisor \(q>1\) of either \(p-1\) or \(p+1\) satisfies
\[
q\le\frac{p+1}{3}\le\frac p2
\]
except that the displayed middle inequality is strict on the \(p-1\) side and the endpoint issue on the \(p+1\) side is harmless for \(p\ge4\). Thus the positive canonical admissible denominators are \(q=1\) together with all nontrivial proper divisors of \(p-1\) and of \(p+1\).

Now impose Schubert equivalence up to mirror. If \(q>1\) divides \(p-1\), then
\[
q\cdot\frac{p-1}{q}\equiv-1\pmod p,
\]
so inversion up to sign pairs \(q\) with \((p-1)/q\). If \(q>1\) divides \(p+1\), then
\[
q\cdot\frac{p+1}{q}\equiv1\pmod p,
\]
so inversion pairs \(q\) with \((p+1)/q\). The two divisor families intersect only at \(q=1\), because
\[
\gcd(p-1,p+1)=1
\]
for even \(p\).

For an odd integer \(N>1\), the nontrivial proper divisors of \(N\), modulo complementary pairing \(d\leftrightarrow N/d\), therefore contribute
\[
\frac{\tau(N)-2+\mathbf 1_{N\ {\rm square}}}{2}
\]
orbits. Adding the shared \(q=1\) orbit gives the asserted formula for \(c_p\).

For the summatory estimate, write
\[
D_{\rm odd}(X)=\sum_{\substack{n\le X\\n\ {\rm odd}}}\tau(n).
\]
Counting odd factor pairs gives
\[
D_{\rm odd}(X)
=
\sum_{\substack{a\le X\\a\ {\rm odd}}}
\left(\frac{X}{2a}+O(1)\right)
=
\frac14X\log X+O(X),
\]
because
\[
\sum_{\substack{a\le X\\a\ {\rm odd}}}\frac1a
=
\frac12\log X+O(1).
\]
The exact formula for \(c_p\) then shows that the two shifted divisor sums from \(p-1\) and \(p+1\) contribute
\[
\frac14X\log X+O(X)
\]
after the orbit factor \(1/2\). The square-indicator contribution is \(O(\sqrt X)\), so
\[
L(X)\sim\frac14X\log X.
\]

It remains to count all two-bridge link types up to mirror. For fixed even \(p\), there are \(\varphi(p)/2\) positive canonical denominators. Quotienting by inversion up to sign gives
\[
\frac{\varphi(p)}4+O(f(p))
\]
orbits, where \(f(p)\) is the number of fixed positive representatives. A fixed representative satisfies
\[
q^2\equiv1\pmod p
\quad\text{or}\quad
q^2\equiv-1\pmod p.
\]
The number of such solutions is bounded by a constant multiple of \(2^{\omega(p)}\), and
\[
\sum_{n\le X}2^{\omega(n)}=O(X\log X).
\]

Finally,
\[
\sum_{\substack{p\le X\\2\mid p}}\varphi(p)
\sim\frac{X^2}{\pi^2}.
\]
For completeness, this follows by subtracting the odd totient sum from the classical total. Using
\[
\varphi(n)=\sum_{d\mid n}\mu(d)\frac nd
\]
gives
\[
\sum_{\substack{n\le X\\n\ {\rm odd}}}\varphi(n)
=
\frac{2}{\pi^2}X^2+O(X\log X),
\]
while
\[
\sum_{n\le X}\varphi(n)
=
\frac{3}{\pi^2}X^2+O(X\log X).
\]
Hence
\[
B(X)\sim\frac14\cdot\frac{X^2}{\pi^2}
=
\frac{X^2}{4\pi^2},
\]
and dividing the two asymptotics proves the zero-density statement.

## Verification
The source criterion was checked directly in Lyu--Nie, Corollary 4.3, including its hypotheses \(p\) even, \(q\) odd, \(0<|q|\le p/2\), and \(\gcd(p,q)=1\). Santoro--Zhou Section 2 was checked for the Schubert equivalence used to quotient denominators.

The bundled verifier independently enumerates all positive canonical denominators, applies the congruence criterion, quotients by modular inversion up to sign, and compares the resulting orbit count against the divisor formula for every even \(p\le1000\). It also reports finite scaled-density values as a regression check. Its output is:

`VERIFY_OK exact_even_p_through=1000 scaled_density=100:110/313:7.63137269,1000:1629/26156:9.01597735,5000:10107/638096:9.29843265 target_pi2=9.86960440`

The finite enumeration is not the proof of either asymptotic. The infinite argument is the divisor-pairing proof together with the displayed summatory divisor and totient estimates.

## Relationship to prior work
Santoro--Zhou classify exactly which two-bridge links admit non-trivial L-space surgeries and describe the full surgery sets of their surviving families. Lyu--Nie recover the existence classification in the arithmetic form
\[
p\equiv\pm1\pmod{|q|}.
\]
Neither inspected source states the resulting divisor-orbit count at fixed Schubert numerator, nor a determinant-ordered asymptotic or density theorem.

Schubert's classical classification supplies the denominator inversion relation needed to convert parameter counts into link-type counts. The present result combines that equivalence with the new L-space criterion and then performs the divisor and totient asymptotics.

Targeted literature searches for two-bridge L-space surgery counts, divisor-function formulations, determinant asymptotics, and density statements located the two recent classification papers and earlier work on L-space links, but no equivalent counting theorem.

## Limitations
The count is taken up to mirror. Counting mirror-distinct types requires an additional amphichirality correction and is not claimed here.

The asymptotic orders links by Schubert numerator, equivalently determinant, rather than by crossing number or hyperbolic volume. No statement about those alternative orderings follows automatically.

The theorem counts link types that admit at least one non-trivial L-space surgery. It does not count the surgery slopes themselves or weight links by the size or geometry of their L-space surgery regions.

## References
1. D. Santoro and H. Zhou, *On L-space surgeries on two-bridge links*, arXiv:2606.27145v1, first posted 2026-06-25.
2. Q. Lyu and Z. Nie, *L-space surgeries on (1,1)-knots in \(S^1\times S^2\)*, arXiv:2608.30925v1, first posted 2026-08-31.
3. H. Schubert, *Knoten mit zwei Brücken*, Mathematische Zeitschrift 65 (1956), 133--170.

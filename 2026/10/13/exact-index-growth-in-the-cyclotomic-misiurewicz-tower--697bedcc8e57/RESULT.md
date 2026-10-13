# Exact index growth in the cyclotomic Misiurewicz tower
## Finding
Let \(p\) be an odd prime, \(j\ge1\), and
\[
h_j(x)=x^2-4jx+(4j^2+2j).
\]
Assume the integer \(\Phi_p(2j)\) is squarefree, where \(\Phi_p\) is the \(p\)-th cyclotomic polynomial. For every \(k\ge1\), define
\[
F_k(x)=\Phi_p(h_j^{\circ k}(x)).
\]
If \(\theta_k\) is a root, \(s=\nu_2(j)\), and \(t=\min\{s,k\}\), then \(F_k\) is irreducible and
\[
[\mathcal O_{\mathbb Q(\theta_k)}:\mathbb Z[\theta_k]]
=2^{(p-1)(2^k-2^{k-t})}.
\]
Thus every level is monogenic exactly when \(j\) is odd. If \(j\) is even, already
\[
[\mathcal O_{\mathbb Q(\theta_1)}:\mathbb Z[\theta_1]]=2^{p-1}.
\]
More generally, the entire index profile depends on \(j\) only through \(\nu_2(j)\).

## Assumptions and scope
The hypotheses are: \(p\) is an odd prime, \(j\) is a positive integer, \(k\ge1\), and \(\Phi_p(2j)\) is squarefree. The squarefree hypothesis is exactly the arithmetic hypothesis appearing in the recent Misiurewicz-tower construction. Since \(2j\) is even and \(p\) is odd, \(\Phi_p(2j)\) is odd.

The index is the absolute order index in the full ring of integers. No finite computation is used to establish the universal formula.

## Proof
Translate by the fixed critical point. Writing \(x=y+2j\) gives
\[
h_j(y+2j)=y^2+2j,
\qquad
h_j^{\circ k}(y+2j)=y^{2^k}+2j.
\]
An integral translation does not change the polynomial index, so set \(n=2^k\) and study
\[
G_k(y)=\Phi_p(y^n+2j).
\]
Let \(\zeta\) be a primitive \(p\)-th root of unity, \(K=\mathbb Q(\zeta)\), and \(a=\zeta-2j\). Then
\[
N_{K/\mathbb Q}(a)=\Phi_p(2j).
\]
Because this norm is squarefree, the principal ideal \((a)\subset\mathcal O_K\) is squarefree. Choose a prime ideal \(\mathfrak q\mid(a)\). Then \(v_{\mathfrak q}(a)=1\), so \(X^n-a\) is Eisenstein at \(\mathfrak q\) and hence irreducible over \(K\). If \(\beta^n=a\), then \(\zeta=\beta^n+2j\in\mathbb Q(\beta)\). Consequently
\[
[\mathbb Q(\beta):\mathbb Q]=n(p-1),
\]
which is the degree of \(G_k\); hence \(G_k\), and therefore \(F_k\), is irreducible.

Moreover \(\mathbb Z[\beta]=\mathcal O_K[\beta]\), because \(\mathcal O_K=\mathbb Z[\zeta]\) and \(\zeta=\beta^n+2j\). At every odd prime ideal dividing \((a)\), the Eisenstein extension is totally ramified of degree \(n\), which is prime to the odd residue characteristic, so it is tame and \(\mathcal O_K[\beta]\) is locally maximal. Primes not dividing \(2a\) do not divide the discriminant of \(X^n-a\). Thus the relative index can be supported only at primes of \(K\) above \(2\).

Fix \(\mathfrak P\mid2\). The cyclotomic field \(K\) is unramified at \(2\), so normalize \(v_{\mathfrak P}(2)=1\). Choose an integer \(r\) with \(rn\equiv1\pmod p\), and put \(u=\zeta^r\), so \(u^n=\zeta\). After the local shift \(X=Y+u\),
\[
P(Y)=(Y+u)^n-u^n+2j.
\]
Its constant coefficient has valuation \(s+1\), while for \(1\le m<n\),
\[
v_{\mathfrak P}\!\left(\binom{n}{m}u^{n-m}\right)
=\nu_2\!\left(\binom{2^k}{m}\right)
=k-\nu_2(m).
\]
The last identity follows from
\[
\binom{2^k}{m}=\frac{2^k}{m}\binom{2^k-1}{m-1},
\]
because the second factor is odd.

Let \(t=\min\{s,k\}\). The lower Newton polygon determined by these points has, at each integer abscissa \(1\le m<n\), floor ordinate
\[
e_m=\min\{t,\,k-\lceil\log_2 m\rceil\}.
\]
This follows by grouping the coefficient points into the dyadic blocks
\(2^{a-1}<m\le2^a\): their minimal valuation is \(k-a\), and the successive lower supporting segments join exactly those dyadic minima. The initial segment is regular as well. If \(s=0\), or if \(s>k\), its residual polynomial has degree one. If \(1\le s\le k\), its residual polynomial has degree two; the midpoint \(m=2^{k-s}\) lies on that segment and has exact normalized coefficient valuation \(s\). Hence its residual quadratic has nonzero linear term in characteristic \(2\), so it is separable. Every later segment has residual degree one. Therefore Ore's index theorem applies with equality.

The \(\mathfrak P\)-adic relative index exponent is consequently
\[
I_{k,s}=\sum_{m=1}^{2^k-1}e_m.
\]
For each \(1\le q\le t\), exactly \(2^{k-q}\) indices satisfy \(e_m\ge q\). Thus
\[
I_{k,s}=\sum_{q=1}^{t}2^{k-q}=2^k-2^{k-t}.
\]
This exponent is the same for every \(\mathfrak P\mid2\). Since \(2\) is unramified in \(K\), the residue degrees of the primes above \(2\) sum to \([K:\mathbb Q]=p-1\). Taking the norm of the relative index ideal gives
\[
[\mathcal O_{\mathbb Q(\beta)}:\mathbb Z[\beta]]
=2^{(p-1)I_{k,s}}
=2^{(p-1)(2^k-2^{k-t})}.
\]
Finally, the integral translation \(x=y+2j\) transfers this index unchanged to \(F_k\).

## Verification
The accompanying `verify.py` independently checks the dyadic coefficient-valuation identity, reconstructs the lower Newton polygon exactly using rational slopes, verifies the floor-ordinate formula and its sum, and checks the midpoint valuation needed for separability. It covers \(1\le k\le10\) and \(0\le\nu_2(j)\le k+4\), printing
`VERIFY_OK newton_cases=105 k_max=10 index_formula=OK residual_midpoints=OK`.

This finite replay is corroborative only. Irreducibility, support of the index, Newton-polygon regularity, and the all-\(k\) index formula are proved above.

## Relationship to prior work
Jakhar, Kalwaniya, Laishram, and Yadav introduce this cyclotomic Misiurewicz tower and prove that, under squarefreeness of \(\Phi_p(2j)\), odd \(j\) gives monogeneity at every level. Their proof isolates the prime \(2\) as the exceptional local case and verifies the needed Dedekind condition when \(j\) is odd. The inspected source does not state an exact index when \(j\) is even, nor an all-level index-growth formula.

The present calculation resolves that same local obstruction quantitatively: it recovers index one for odd \(j\), and for even \(j\) gives the exact power of \(2\) at every level. General work on integral bases of pure radical fields is methodologically related, but the inspected literature does not supply this relative cyclotomic tower formula.

## Limitations
The theorem assumes \(\Phi_p(2j)\) is squarefree. It does not describe additional index contributions when that critical value has repeated prime factors. It treats the specific Misiurewicz quadratic from the cited construction, not arbitrary postcritically finite polynomials. Bibliographic searches cannot exclude an equivalent result hidden in unindexed or differently phrased literature.

## References
1. A. Jakhar, R. Kalwaniya, S. Laishram, P. Yadav, *On The Index of Polynomial Compositions over Valued Fields*, arXiv:2610.02111v1, first posted 2026-10-01; especially Theorem 1.2 and Proposition 6.3.
2. A. Jakhar, R. Kalwaniya, P. Yadav, *A study of monogeneity of trinomial compositions: Qualitative and quantitative aspects*, Journal of Pure and Applied Algebra (2026), DOI: 10.1016/j.jpaa.2026.108231.
3. A. Jakhar, S. K. Khanduja, N. Sangwan, *On integral basis of pure number fields*, Mathematika 67 (2021), DOI: 10.1112/mtk.12067.

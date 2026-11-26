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
Thus at each level \(F_k\) is monogenic **as a polynomial** (its specified root generates the full ring of integers) exactly when \(j\) is odd. If \(j\) is even, already
\[
[\mathcal O_{\mathbb Q(\theta_1)}:\mathbb Z[\theta_1]]=2^{p-1}.
\]
For fixed \(p\), the entire index profile depends on \(j\) only through \(\nu_2(j)\). Nonmaximality for the specified generator does not assert nonmonogeneity of the field: a different generator may give a full power basis.

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

Moreover \(\mathbb Z[\beta]=\mathcal O_K[\beta]\), because \(\mathcal O_K=\mathbb Z[\zeta]\) and \(\zeta=\beta^n+2j\). At every odd prime ideal dividing \((a)\), the Eisenstein extension is totally ramified of degree \(n\) and \(\beta\) is a local uniformizer. In the local basis \(1,\beta,\ldots,\beta^{n-1}\), nonzero terms with coefficients in the base field have valuations in distinct classes modulo \(n\) under the extension's integer normalization. Thus an integral element has all coefficients integral, proving local maximality. Primes not dividing \(2a\) do not divide the discriminant of \(X^n-a\). Thus the relative index can be supported only at primes of \(K\) above \(2\).

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
To see this, the dyadic points are \(D_a=(2^a,k-a)\) for \(0\le a\le k\), including the leading coefficient at \(D_k\). Between consecutive dyadic points the other coefficient valuations are at least the higher endpoint valuation, and the consecutive dyadic slopes \(-1/2^{a-1}\) (from \(D_{a-1}\) to \(D_a\)) are strictly increasing. If \(s=0\), the polygon consists of the segment from \((0,1)\) to \(D_k\). If \(s>k\), its first segment joins \((0,s+1)\) to \(D_0\), followed by the dyadic segments. If \(1\le s\le k\), put \(M=2^{k-s}\). The first segment joins \((0,s+1)\) to \((2M,s-1)=D_{k-s+1}\), with midpoint \((M,s)\). All intermediate coefficients other than the midpoint have valuation at least \(s+1\). The polygon then follows the dyadic segments, whose slopes are strictly greater than \(-1/M\), the initial slope. Thus on the first segment of the middle case the floor is \(s\) for \(1\le m\le M\) and \(s-1\) for \(M<m\le2M\); on each subsequent dyadic block \(2^{a-1}<m\le2^a\) it is \(k-a\). The other two cases give the same displayed formula.

The reduction of \(X^n-a\) at \(\mathfrak P\) is \((X-\bar u)^n\), so the shift computes the Newton polygon for its only residual factor. Each face has residual degree one except for the first face when \(1\le s\le k\), whose horizontal length \(2M\) and vertical drop two give residual degree two. Its midpoint coefficient has valuation exactly \(s\); it gives a nonzero linear coefficient in the residual quadratic. In characteristic \(2\) this proves separability. Therefore all faces are regular and Ore's index theorem applies with equality.

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

For example, the first level for \(p=3,j=2\) is a monogenic field even though the specified generator has index four. Here \(\Phi_3(4)=21\), and with \(u=\zeta^2\) the element \(\eta=(\beta-u)/2\) satisfies \(\eta^2+u\eta+1=0\). It is a root of \(X^4-X^3+3X^2-X+1\), obtained by multiplying the quadratic by its cyclotomic conjugate. The constant term one gives \(\eta^{-1}\in\mathbb Z[\eta]\), so \(u=-\eta-\eta^{-1}\in\mathbb Z[\eta]\). In particular \(\mathbb Z[\eta]=\mathcal O_K[\eta]\) and contains \(\beta=2\eta+u\). Comparing the relative bases \(1,\beta\) and \(1,\eta\) gives index four over \(\mathbb Z\), so the formula identifies \(\mathbb Z[\eta]\) with the full ring of integers.

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

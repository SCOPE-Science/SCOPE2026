# Exact 2-adic valuation of Mersenne-index reciprocal binomial sums

## Finding

For every integer \(e\ge4\), set \(n=2^e-1\) and \(f(n)=\sum_{k=0}^{n}\binom{n}{k}^{-1}\in\mathbb Q\). Then
\[
\boxed{\nu_2(f(2^e-1))=3e-2.}
\]
This proves the specific valuation equality conjectured by Donald M. Davis in Proposition 4.7 of his 2012 paper. In fact, in \(\mathbb Q_2\), let \(L_3=\sum_{h\ge1}2^h/h^3=\operatorname{Li}_3(2)\). Then \(\nu_2(L_3)=-2\) and
\[
f(2^e-1)=-2^{3e}L_3+E_e,\qquad \nu_2(E_e)\ge4e-4.
\]
Consequently \(2^{-3e}f(2^e-1)\to-L_3\) in \(\mathbb Q_2\); the leading constant is nonzero.

## Assumptions and scope

All sums of rational binomial reciprocals use \(0\le k\le n\), and \(\nu_2(2)=1\). The 2-adic polylogarithm \(\operatorname{Li}_s(2)=\sum_{h\ge1}2^h/h^s\) converges for positive integral \(s\), since \(h-s\nu_2(h)\to+\infty\). The main valuation assertion is for all integers \(e\ge4\), not just the tested finite range. The small values are \(\nu_2(f(1))=1\), \(\nu_2(f(3))=3\), and \(\nu_2(f(7))=8\); the displayed general formula does not assert their inclusion.

## Proof

**1. Reciprocal-binomial recurrence and a harmonic transform.** The elementary recurrence
\[
f(n)=1+\frac{n+1}{2n}f(n-1)\quad(n\ge1),\qquad f(0)=1,
\]
iterates to
\[
f(N-1)=\frac{N}{2^N}\sum_{j=1}^{N}\frac{2^j}{j}\qquad(N\ge1).
\]
For example, the recurrence follows by adding adjacent reciprocal binomial identities, and the second identity follows by telescoping after multiplication by \(2^{n+1}/(n+1)\). Every expression is a rational identity, so it holds when embedded in \(\mathbb Q_2\).

**2. The first two 2-adic polylogarithms vanish.** The convergent logarithmic series gives
\[
L_1=\sum_{h\ge1}\frac{2^h}{h}=-\log(1-2)=-\log(-1)=0.
\]
Here \(\log(-1)=0\), because the 2-adic logarithm is a group homomorphism on \(1+2\mathbb Z_2\) and \((-1)^2=1\). For the second series, consider the identity of rational formal power series
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac{z}{z-1}\right)
=-\frac12\log^2(1-z).
\]
It follows by differentiating both sides and checking their zero constant terms. All three expressions converge 2-adically at \(z=2\), where \(z/(z-1)=2\) and \(\log(1-z)=\log(-1)=0\). Therefore \(2L_2=0\), hence \(L_2=0\).

**3. The third polylogarithm has exact valuation \(-2\).** In \(L_3\), the summand with \(h=4\) has \(\nu_2(2^4/4^3)=-2\). Every other positive integer \(h\) satisfies \(h-3\nu_2(h)\ge-1\): writing \(h=2^t u\) with \(u\) odd, check \(t=0,1,2,3\) directly and use \(h\ge2^t\) for \(t\ge4\). Thus the valuation \(-2\) term is unique, with no possible cancellation, and \(\nu_2(L_3)=-2\).

**4. Uniformly control the tail at powers of two.** Since \(L_1=0\), writing \(j=N+h\) in the omitted tail of the harmonic transform yields the exact convergent identity
\[
f(N-1)=-N\sum_{h\ge1}\frac{2^h}{N+h}.
\]
Use the exact rational decomposition
\[
\frac1{N+h}=\frac1h-\frac{N}{h^2}+\frac{N^2}{h^3}-\frac{N^3}{h^3(N+h)}.
\]
Since \(L_1=L_2=0\), this becomes
\[
f(N-1)=-N^3L_3+N^4R_N,\quad
R_N=\sum_{h\ge1}\frac{2^h}{h^3(h+N)}.
\]
Set \(N=2^e\), \(e\ge4\). For \(1\le h<N\), put \(t=\nu_2(h)<e\); then \(\nu_2(h+N)=t\) and
\[
\nu_2\left(\frac{2^h}{h^3(h+N)}\right)=h-4t\ge-4.
\]
Indeed \(h\ge2^t\) and \(2^t-4t\ge-4\) for all integers \(t\ge0\) (equality at \(t=2,3\)). For \(h\ge N\), choose \(s\ge4\) with \(2^s\le h<2^{s+1}\). Then \(\nu_2(h)\le s\), and since \(0<h+N<2^{s+2}\), \(\nu_2(h+N)\le s+1\). Therefore
\[
\nu_2\left(\frac{2^h}{h^3(h+N)}\right)\ge h-4s-1\ge2^s-4s-1\ge-1.
\]
Termwise nonarchimedean bounds and convergence imply \(\nu_2(R_N)\ge-4\). Consequently \(\nu_2(N^4R_N)\ge4e-4\), while \(\nu_2(-N^3L_3)=3e-2\). As \(4e-4>3e-2\) for every \(e\ge3\), the two terms have distinct valuations, proving the exact assertion for \(e\ge4\). The normalized convergence and error bound are immediate. \(\square\)

## Verification

The included standalone `verify.py` computes \(f(2^e-1)\) directly as a rational sum of inverse binomial coefficients, evaluates the independent harmonic-transform expression, and compares 2-adic valuations for \(1\le e\le9\). It also checks the leading-constant valuation through a convergent finite prefix whose omitted terms all have sufficiently high valuation. Execute with `python3 verify.py` in a standard Python 3 environment; no external packages or downloaded data are required. Finite tests corroborate but do not replace the complete proof.

## Relationship to prior work

Davis, *For which p-adic integers x can sum of inverse binomial coefficients be defined?*, arXiv:1208.0250v1 (first submitted 2012-08-01), Proposition 4.7, proves the weaker estimate \(\nu_2(f(2^e-1))\ge2e\) for \(e\ge3\) and explicitly proposes the equality \(3e-2\) for \(e\ge4\). The present theorem addresses exactly that conjecture with a polylogarithmic leading coefficient and a uniform error bound. Davis's 2013 follow-up arXiv:1301.2532 addresses a distinct odd-argument difference conjecture. Searches for equivalent formulations and stronger theorems did not identify earlier exact coverage; this remains a literature-limited priority assessment, not a certification of uniqueness.

## Limitations

The exact formula here concerns \(2^e-1\), not general odd indices, other prime bases, or analogous sums over other coefficient families. The 2-adic polylogarithm provides the leading coefficient; no elementary rational closed form for that 2-adic constant is claimed. Historical priority may be affected by unindexed or inaccessible sources. Independent mathematical audit has not been performed.

## References

1. D. M. Davis, *For which p-adic integers x can sum of inverse binomial coefficients be defined?*, arXiv:1208.0250v1, 2012-08-01, Proposition 4.7 and recurrence (2.4). https://arxiv.org/abs/1208.0250
2. D. M. Davis, *For which 2-adic integers x can sum of inverse binomial coefficients be defined?*, arXiv:1301.2532, 2013-01-11. https://arxiv.org/abs/1301.2532

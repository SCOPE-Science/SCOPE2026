# An exact residue-gap shift law for two-generator numerical semigroups

## Finding

Let \(\langle a,b\rangle=\{ia+jb:i,j\in\mathbb Z_{\ge0}\}\) and let a *gap* be a positive integer not in this semigroup. For integers \(a\ge2\), \(k\ge1\), and \(m\ge2\) satisfying \(\gcd(a,k)=\gcd(a+m,k)=1\), let \(G_{a,k,m}(t)\) count the gaps of \(\langle a,a+k\rangle\) that are congruent to \(t\pmod m\), for \(0\le t<m\).

Put \(d=\gcd(a,m)\) and \(e=\gcd(a+k,m)\). These are coprime and each is coprime to \(k\). For \(q\in\{d,e\}\), define \(u_q(t)\) to be the representative in \(\{0,\ldots,q-1\}\) of \(t k^{-1}\pmod q\), and set \(u_1(t)=0\).

**Exact residuewise transition theorem.** For every \(0\le t<m\),
\[
\boxed{G_{a+m,k,m}(t)-G_{a,k,m}(t)
=a+\frac{k+m-d+e}{2}+u_d(t)-u_e(t)-e\mathbf1_{e\mid t}.}
\]
The right side is always an integer. As \(t\) runs over its \(m\) possible classes, its multiset is exactly the multiset of \(B+U-V\), in which \(B=a+(k+m-d+e)/2\), \(U\) is uniform on \(\{0,\ldots,d-1\}\), \(V\) is uniform on \(\{1,\ldots,e\}\), and each ordered pair is repeated \(m/(de)\) times. Consequently the transition profile is constant exactly when \(\gcd(m,a(a+k))=1\); its exact largest-minus-smallest spread and its population variance are
\[
\boxed{d+e-2\quad\text{and}\quad\frac{d^2+e^2-2}{12}.}
\]

A quotient-semigroup consequence follows by taking \(t=0\): writing \(\gamma(S)\) for the genus (number of gaps) of a numerical semigroup,
\[
\boxed{\gamma(\langle a+m,a+m+k\rangle/m)-\gamma(\langle a,a+k\rangle/m)
=a+\frac{k+m-d-e}{2}.}
\]
Here \(S/m:=\{j\in\mathbb Z_{\ge0}:mj\in S\}\); no coprimality between \(m\) and the individual generators is assumed.

For example \((a,k,m)=(2,1,6)\) gives the six increments \((3,6,4,4,5,5)\), with sharp spread \(3\).

## Assumptions and scope

The generators and their translated counterparts must each be relatively prime. Thus \(a\), \(a+k\), \(a+m\), and \(a+m+k\) are positive, with \(\gcd(a,a+k)=\gcd(a+m,a+m+k)=1\). The modulus \(m\ge2\) is arbitrary, including common divisors with either generator. All gap counts are finite by coprimality. The characteristic functions \(\mathbf1_{e\mid t}\) equal one when \(e\) divides \(t\) and zero otherwise; if \(e=1\), the indicator is identically one. Inverses modulo one are not needed because of the convention \(u_1=0\).

## Proof

**1. Rational gap polynomial and its translated values.** Write \(b=a+k\). For two coprime positive generators the formal Hilbert series and gap polynomial are
\[
H_{a,b}(z)=\frac{1-z^{ab}}{(1-z^a)(1-z^b)},\qquad
P_{a,b}(z)=\frac{1}{1-z}-H_{a,b}(z)
=\sum_{h\notin\langle a,b\rangle}z^h.
\]
The finite sum ranges over positive gaps. The geometric-series identity for the Hilbert series follows from uniqueness of a representative \(i\in\{0,\ldots,b-1\}\) in \(ia+jb\), with \(j\ge0\); equivalently one can interchange the two generators. In particular Sylvester's formula gives \(P_{a,b}(1)=(a-1)(b-1)/2\).

Put \(a'=a+m\), \(b'=b+m\), and \(\Delta P=P_{a',b'}-P_{a,b}\). Let \(\zeta\ne1\) be an \(m\)-th root of unity. If neither \(\zeta^a\) nor \(\zeta^b\) equals one, the rational Hilbert-series values for the primed and unprimed parameters agree, because the exponents of all numerator and denominator monomials agree modulo \(m\). Hence \(\Delta P(\zeta)=0\).

If \(\zeta^a=1\), then \(\zeta^b=\zeta^k\ne1\) since \(\gcd(a,k)=1\). The removable singularity gives \(H_{a,b}(\zeta)=b/(1-\zeta^k)\) and \(H_{a',b'}(\zeta)=(b+m)/(1-\zeta^k)\). Thus
\[
\Delta P(\zeta)=-\frac{m}{1-\zeta^k}.
\]
Likewise, if \(\zeta^b=1\), then \(\zeta^a=\zeta^{-k}\ne1\), so
\[
\Delta P(\zeta)=-\frac{m}{1-\zeta^{-k}}.
\]
The two cases are disjoint: a root satisfying both would have order dividing \(\gcd(a,b)=1\). At \(z=1\), Sylvester's genus identity yields
\[
\Delta P(1)=\frac{m(2a+k+m-2)}2.
\]

**2. Exact roots-of-unity filtering.** Since \(P\) is a finite polynomial, orthogonality of the \(m\)-th roots gives the desired transition as
\[
\Delta G(t)=\frac1m\sum_{\zeta^m=1}\zeta^{-t}\Delta P(\zeta).
\]
The roots in the first singular class are precisely the nonidentity \(d\)-th roots, and those in the second class are precisely the nonidentity \(e\)-th roots. Here \(d\) and \(e\) are coprime because any common prime would divide both \(a\) and \(a+k\), hence \(k\), contradicting \(\gcd(a,k)=1\). Each of \(d,e\) is likewise coprime to \(k\).

For \(q\ge1\) coprime to \(k\), the following elementary finite Fourier sums hold, with \(u=u_q(t)\):
\[
\sum_{\substack{\zeta^q=1\\\zeta\ne1}}
\frac{\zeta^{-t}}{1-\zeta^k}=\frac{q-1}{2}-u,
\qquad
\sum_{\substack{\zeta^q=1\\\zeta\ne1}}
\frac{\zeta^{-t}}{1-\zeta^{-k}}=
 u-\frac{q+1}{2}+q\mathbf1_{q\mid t}.
\]
To see the first, change variables \(\eta=\zeta^k\). At \(u=0\), pairing each \(\eta\) with its inverse gives \((q-1)/2\). On replacing \(u\) by \(u+1\), for \(0\le u<q-1\), the sum decreases by \(\sum_{\eta\ne1}\eta^{-(u+1)}=-1\). The second identity follows by replacing \(k\) with \(-k\) and distinguishing \(u=0\). Both equations are valid for \(q=1\), where the left sides are empty sums and the right sides vanish.

Substituting these sums and the value at one into the Fourier filter gives
\[
\Delta G(t)=\frac{2a+k+m-2}{2}
-\left(\frac{d-1}{2}-u_d(t)\right)
-\left(u_e(t)-\frac{e+1}{2}+e\mathbf1_{e\mid t}\right),
\]
which simplifies to the theorem.

**3. Sharp spectrum and variance.** Since \(d\) and \(e\) are coprime, CRT gives a surjection with exactly \(m/(de)\) preimages per pair from \(\mathbb Z/m\mathbb Z\) onto \(\mathbb Z/d\mathbb Z\times\mathbb Z/e\mathbb Z\). Multiplication by the inverse of \(k\) permutes each factor. Therefore \(u_d(t)\) is uniform on \(\{0,\ldots,d-1\}\), while \(u_e(t)+e\mathbf1_{e\mid t}\) is uniform on \(\{1,\ldots,e\}\), and these are independent. The extremal difference is \((d-1)-1- (0-e)=d+e-2\). The variance is the sum of the variances of independent discrete uniforms: \((d^2-1)/12+(e^2-1)/12\). The spread vanishes exactly when \(d=e=1\), equivalently \(\gcd(m,a(a+k))=1\).

**4. Quotient genus.** A positive integer \(j\) is a gap of \(\langle a,b\rangle/m\) precisely when \(mj\) is a gap of \(\langle a,b\rangle\). Hence the genus of the quotient equals \(G_{a,k,m}(0)\). In the transition formula, \(u_d(0)=u_e(0)=0\) and \(\mathbf1_{e\mid0}=1\), proving the displayed quotient-genus difference. This completes the proof.

## Verification

The standalone exact-arithmetic program `verify.py` independently creates the semigroup membership array through Sylvester's conductor, extracts gap histograms, and compares them with the derived transition for \(5005\) admissible triples with \(2\le m\le21\), \(1\le k\le18\), and \(2\le a\le33\). This covers \(57323\) individual residue comparisons. It also checks the CRT multiplicities, sharp range, balance criterion, quotient-genus increment, and population variance using exact rational arithmetic. It reports `VERIFY_OK parameters=5005 residue_instances=57323 independent_dp=yes CRT_and_variance=yes exact_rationals=yes`.

These tests support, but do not replace, the universal Fourier/CRT proof.

## Relationship to prior work

Feihu Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076 (first publicly posted 2026-07-25), studies Frobenius numbers of quotient semigroups and proves quasipolynomial behavior for a consecutive-generator family. The quantity studied there is the largest gap in a quotient, not the entire vector of residue-specific gap-count **changes** under simultaneous generator translation.

Adeniran and coauthors, *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360, give a general root-of-unity filter for quotient genus and a quasipolynomial theorem for two-generator quotients. Their general formula provides a closely related method and covers part of the setting at a more abstract level. The present statement evaluates the singular root contributions explicitly for **all residue classes at once**, including shared factors of the modulus with generators, and deduces a sharp finite CRT spectrum and variance. It should not be presented as an independent discovery of root-of-unity filtering or of quasipolynomiality.

Caleb Shor, *Equidistribution of numerical semigroup gaps modulo m*, arXiv:2101.01760, gives a static criterion for the gap multiset of \(\langle a,b\rangle\) to be equidistributed modulo \(m\). The present criterion concerns **uniformity of the vector of differences** of gap counts after translating both generators by \(m\); the two predicates are distinct. An older explicit transition theorem, if located, would alter the priority assessment.

Emmanuel Cabanillas, *Quotients of numerical semigroups generated by two numbers*, arXiv:1904.08240, gives continued-fraction methods for quotient-genus problems. Its inspected classifications do not state the full residuewise translation law.

## Limitations

The exact theorem requires both generator pairs to be coprime; it does not make a claim for nonnumerical semigroups with infinite gap complements. The law gives a transition in gap histograms rather than an absolute closed formula for every histogram without an initial value. It addresses genus of quotients, not their Frobenius numbers. The proof is self-contained given standard Hilbert-series and Sylvester identities, but its underlying Fourier technique is classical. Publication priority is not independently established: a more general published identity could subsume the transition after specialization. Independent mathematical review has not been performed.

## References

1. F. Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076 (2026), https://arxiv.org/abs/2607.23076.
2. A. Adeniran, S. Butler, C. Defant, Y. Gao, P. E. Harris, C. Hettle, Q. Liang, H. Nam, and A. Volk, *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360 (2018), https://arxiv.org/abs/1809.09360.
3. C. M. Shor, *Equidistribution of numerical semigroup gaps modulo m*, arXiv:2101.01760 (2021), https://arxiv.org/abs/2101.01760.
4. E. Cabanillas, *Quotients of numerical semigroups generated by two numbers*, arXiv:1904.08240 (2019), https://arxiv.org/abs/1904.08240.

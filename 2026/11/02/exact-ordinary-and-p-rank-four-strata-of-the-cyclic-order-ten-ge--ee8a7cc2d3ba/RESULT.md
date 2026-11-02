# Exact ordinary and \(p\)-rank-four strata of the cyclic order-ten genus-six quintics

## Finding
Let \(p=10n+1>13\) be prime, \(n\ge1\), and let \(k\) be an algebraically closed field of characteristic \(p\). For \(\lambda\in k\setminus\{0,1\}\), let \(C_\lambda\) be the smooth projective model of
\[
 y^5=x(x^2-1)(x^2-\lambda).
\]
Define the polynomial
\[
 Q_n(\lambda)=\sum_{j=0}^{3n}\binom{4n}{j}\binom{4n}{3n-j}\lambda^j\in\mathbb F_p[\lambda].
\]
Then \(Q_n\) has exactly \(3n\) distinct roots in \(k\), none at \(0\) or \(1\), and
\[
 \bigl(f_p(C_\lambda),a(C_\lambda)\bigr)=
 \begin{cases}(6,0),&Q_n(\lambda)\ne0,\\(4,2),&Q_n(\lambda)=0.
 \end{cases}
\]
Here \(f_p\) is the geometric \(p\)-rank of the Jacobian and \(a\) is its \(a\)-number. Thus there are precisely \(3n\) geometric parameters with nonordinary Jacobian, with a uniform drop in \(p\)-rank by two. Among curves in this family whose full geometric automorphism group is cyclic of order ten, precisely \(\lfloor 3n/2\rfloor\) geometric isomorphism classes are nonordinary.

## Assumptions and scope
The characteristic satisfies \(p\equiv1\pmod{10}\), and necessarily \(p\ge31\) under the stated bound. All geometry and isomorphism classes are over an algebraic closure. The five branch points of the degree-five Kummer map are distinct when \(\lambda\ne0,1\). Riemann–Hurwitz gives genus \(6\). The parameter \(\lambda\) is not a coordinate on the coarse moduli curve without identification: the equivalence \(\lambda\sim1/\lambda\) is accounted for in the class count. A curve with automorphism group of order twenty is omitted from the cyclic-order-ten class count.

## Proof
**Differentials and Cartier blocks.** Put \(f(x)=x(x^2-1)(x^2-\lambda)\). For \(i=2,3,4\) and \(1\le h<i\),
\[
 \omega_{i,h}=x^{h-1}\,dx/y^i
\]
is a holomorphic differential; these \(1+2+3=6\) forms constitute a basis. For example, at a finite branch point, \(dx/y^i\) has valuation \(4-i\ge0\), and at each of the five points above infinity, \(x^{h-1}dx/y^i\) has valuation \(i-h-1\ge0\). Distinct-character components under the fifth-root deck action have dimensions \(d_1=0,d_2=1,d_3=2,d_4=3\). Since \(p\equiv1\pmod5\), Cartier preserves each component.

Set \(a_i=i(p-1)/5=2in\). The identity \(y^{ip}=y^i f^{a_i}\), together with the extraction rule \(\mathcal C(x^{mp+p-1}dx)=x^m dx\), shows that the \(i\)-th Cartier block, up to entrywise \(p\)-th roots, is
\[
 B_i=(b_{i,hk}),\qquad b_{i,hk}=[x^{hp-k}]f(x)^{a_i},\quad 1\le h,k<i.
\]
The coefficients are polynomials in \(\lambda\) over \(\mathbb F_p\). Since \(a_i\) is even, the entry vanishes when \(hp-k-a_i\) is odd. In particular, \(B_3\) is diagonal.

**The one-dimensional block.** Expanding \(f^{4n}=x^{4n}(x^2-1)^{4n}(x^2-\lambda)^{4n}\) gives
\[
 B_2=\bigl((-1)^{5n}\lambda^n Q_n(\lambda)\bigr).
\]
Thus \(B_2\) loses rank exactly at roots of \(Q_n\).

**The two-dimensional block.** For \(i=3\) let \(P(z)=(z-1)^{6n}(z-\lambda)^{6n}\). Its diagonal entries are \([z^{2n}]P\) and \([z^{7n}]P\). The first is a nonzero scalar multiple of \(\lambda^{4n}(1-\lambda)^{2n}\): in the binomial coefficient sequence, the ratio of the next coefficient to the current one reduces modulo \(p=10n+1\) to the ratio for \((1-\lambda)^{2n}\).

For the second, disregard the overall sign and write its coefficient polynomial as
\[
 R(\lambda)=\sum_{j=0}^{5n}\binom{6n}{j}\binom{6n}{n+j}\lambda^j.
\]
Its coefficients satisfy
\[
 \frac{[\lambda^{j+1}]R}{[\lambda^j]R}
 =\frac{(6n-j)(5n-j)}{(j+1)(n+j+1)}\quad(0\le j<5n).
\]
Hence \(R\) satisfies the Gauss differential equation with parameters \((-6n,-5n;n+1)\). Similarly \(Q_n\) satisfies that with \((-4n,-3n;n+1)\). The Euler gauge substitution \(R\propto(1-\lambda)^{2n}Q_n\) carries the second equation into the first: in characteristic \(p\), the exponent \(n+1+6n+5n=12n+1\) equals \(2n\), and the transformed upper parameters \(7n+1,6n+1\) equal \(-3n,-4n\). Both polynomials have degree at most \(5n\) and a nonzero constant term. Their coefficient recurrences determine them uniquely up to scalar through degree \(5n\), because all denominators \((j+1)(n+j+1)\) in this range are nonzero modulo \(p\). Therefore
\[
 B_3=\operatorname{diag}\bigl(u\lambda^{4n}(1-\lambda)^{2n},\ v(1-\lambda)^{2n}Q_n(\lambda)\bigr),
\]
for nonzero constants \(u,v\in\mathbb F_p^\times\). At a root of \(Q_n\) exactly its second diagonal entry vanishes.

**The three-dimensional block is always invertible.** The deck transformation \(y\mapsto\zeta y\), \(\zeta^5=1\), satisfies \(1+\delta+\cdots+\delta^4=0\) on the Jacobian because the quotient has genus zero. Since \(p\equiv1\pmod5\), the cyclotomic algebra splits over \(\mathbb Z_p\), decomposing the Jacobian's \(p\)-divisible group into four character components. The character component with three holomorphic differential dimensions has height \(d_i+d_{5-i}=3\) (the other three dimensions come from Serre-dual cohomology) and dimension \(3\). A \(p\)-divisible group over an algebraically closed field whose height equals its dimension is multiplicative; Verschiebung is therefore bijective on its invariant differentials. Cartier identifies with that Verschiebung on the Jacobian's differentials. Accordingly \(B_4\) is invertible for every smooth \(C_\lambda\).

The three blocks now give Cartier rank \(6\) if \(Q_n(\lambda)\ne0\), and rank \(0+1+3=4\) otherwise. The nonzero diagonal entries and invertible \(B_4\) remain nonzero under every semilinear iterate, so the stable Cartier rank (the geometric \(p\)-rank) equals the one-step rank. The \(a\)-number is \(6\) minus the Cartier rank. This proves the stratification.

**Distinctness and counting.** For \(q_j=[\lambda^j]Q_n\),
\[
 \frac{q_{j+1}}{q_j}=\frac{(4n-j)(3n-j)}{(j+1)(n+j+1)}\quad(0\le j<3n).
\]
Therefore \(Q_n\) satisfies
\[
 \lambda(1-\lambda)Q_n''+
 \bigl[n+1-(1-7n)\lambda\bigr]Q_n'-12n^2Q_n=0.
\]
The leading coefficient is nonzero; \(Q_n(0)=\binom{4n}{3n}\ne0\), and by Vandermonde \(Q_n(1)=\binom{8n}{3n}\ne0\). A repeated root away from \(0,1\) would, by the differential equation and successive differentiation, make all derivatives vanish there. This is impossible because \(\deg Q_n=3n<p\). Thus the polynomial has exactly \(3n\) distinct admissible roots.

Its coefficients are palindromic: \(\lambda^{3n}Q_n(1/\lambda)=Q_n(\lambda)\). Also
\[
 Q_n(-1)=[z^{3n}](1-z^2)^{4n},
\]
so \(-1\) is a root exactly when \(n\) is odd. By Ohashi's classification, the only extra-automorphism parameters are \(\lambda=-1\) (cyclic order twenty) and the two Fermat-quintic parameters. The latter are ordinary for \(p\equiv1\pmod5\): on a Fermat model \(y^5=x^5+1\), the Cartier matrix in the same monomial basis is diagonal with nonzero entries \(\binom{2in}{2nh}\) for \(1\le h<i\), since all upper indices are less than \(p\). Thus they are not roots of \(Q_n\). The remaining roots come in two-element isomorphism orbits \(\{\lambda,\lambda^{-1}\}\); when \(n\) is odd the one fixed root \(-1\) is first removed. The number with full automorphism group cyclic ten is therefore \(\lfloor3n/2\rfloor\).

## Verification
Run \(\texttt{python3 verify.py}\) using the Python 3 standard library. The program constructs the exact Cartier coefficient blocks in characteristics \(31,41,61,71,101\), checks their two factor identities, verifies that the third block determinant is nonzero for admissible \(\lambda\) by a fully computed polynomial factorization in these characteristics, checks square-freeness, reciprocity, and the special parameter. It finishes with \(\texttt{VERIFY_OK}\). These finite checks test the symbolic derivation; the proof of the theorem for all eligible primes is mathematical and does not rely on finite testing.

## Relationship to prior work
Ohashi (2026), Section 3.2 and Proposition 3.5, introduced the same Kummer family and characterized **superspeciality**, showing in particular that no member is superspecial when \(p\equiv1\pmod5\). The result here instead gives every ordinary and nonordinary \(p\)-rank stratum, proves square-freeness of its nonordinary divisor, and counts the geometric cyclic-order-ten isomorphism classes. Ohashi's Lemma 3.3 supplies the isomorphism identification used here. Elkin (2007) develops general character-space and Cartier-rank bounds for cyclic covers but does not establish this exact parameter polynomial or root count. Bouw (2001) studies generic \(p\)-rank of cyclic covers, whereas the present statement treats every member of one specific positive-dimensional family. These differences distinguish the logical implications; they are not a claim of exhaustive historical priority.

## Limitations
This result is confined to \(p\equiv1\pmod{10}\), \(p>13\), and \(\lambda\ne0,1\). It does not determine the Newton polygon, integral endomorphism ring, or complete Ekedahl–Oort type at nonordinary parameters. The count concerns geometric isomorphism classes with full automorphism group cyclic ten; it does not count rational forms over fixed finite fields. Historical priority may be affected by results under transformed models, unpublished sources, or broader theorems not located in the searches. Independent mathematical validation has not been performed.

## References
1. R. Ohashi, *Superspecial plane quintics with large automorphism groups*, arXiv:2605.29624 (initial public version 2026-05-28), especially Section 3.2, Lemma 3.3, and Proposition 3.5. https://arxiv.org/abs/2605.29624
2. A. Elkin, *The rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431, especially Theorem 1.1 and Sections 2–4. https://arxiv.org/abs/0708.0431
3. I. I. Bouw, *The p-rank of ramified covers of curves*, Compositio Mathematica **126** (2001), 295–322, DOI:10.1023/A:1017513122376. (Generic-cover context; only the accessible abstract was inspected.)

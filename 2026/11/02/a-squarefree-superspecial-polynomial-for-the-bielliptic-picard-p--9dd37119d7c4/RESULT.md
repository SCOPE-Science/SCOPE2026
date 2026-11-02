# A squarefree superspecial polynomial for the bielliptic Picard pencil in every prime characteristic above three

## Finding

Let \(k=\overline{\mathbb F}_p\), where \(p>3\) is prime. The smooth projective genus-three curves
\[
C_a:\quad y^3=x^4+a x^2+1,\qquad a\in k,\quad a^2\ne4,
\]
form the bielliptic Picard pencil. Their superspecial locus has the following complete description.

For \(p\equiv1\pmod3\), no smooth member is superspecial. For \(p\equiv2\pmod3\), write \(p=6m+5\) and define
\[
Q_p(a)=[u^{3m+2}](u^2+au+1)^{2m+1}
=\sum_{r=0}^{\lfloor m/2\rfloor}
\frac{(2m+1)!}{r!(m-2r)!(m+1+r)!}\,a^{m-2r}\in\mathbb F_p[a].
\]
These factorials are ordinary integers reduced modulo \(p\); every displayed factorial argument is less than \(p\). The curve \(C_a\) is superspecial **if and only if** \(Q_p(a)=0\). The polynomial \(Q_p\) has degree \(m\), is separable, and has no root at either excluded parameter \(a=2\) or \(a=-2\). Thus exactly \(m=(p-5)/6\) distinct *marked parameter values* are superspecial over \(k\). Up to geometric isomorphism of unmarked curves, these give \(\lceil m/2\rceil\) distinct classes.

For \(p\equiv2\pmod3\), the entire smooth pencil has just two Ekedahl–Oort and Newton possibilities: at roots of \(Q_p\), the Cartier operator is zero, the \(a\)-number is \(3\), the \(p\)-rank is \(0\), and the Newton slopes are six copies of \(1/2\); elsewhere the Cartier rank is \(2\), the \(a\)-number is \(1\), the \(p\)-rank is \(2\), and the Newton slopes are \(0,0,1/2,1/2,1,1\). The claim does not classify the ordinary and nonordinary subloci when \(p\equiv1\pmod3\).

Examples: \(Q_5=1\); \(Q_{11}=3a\); \(Q_{17}=10a^2+5\) has precisely the roots \(a=5,12\) in \(\mathbb F_{17}\), representing one geometric class; \(Q_{23}=12a^3+19a\). In particular characteristic \(17\) has the first nonzero superspecial parameters in this pencil, whereas the characteristic-\(11\) Fermat member is the first superspecial member.

## Assumptions and scope

The base field is algebraically closed, and \(p\) always denotes a prime greater than three. The discriminant of \(f_a(x)=x^4+a x^2+1\) is nonzero precisely when \(a^2\ne4\), so the indicated smooth completion has genus three. A curve is superspecial when its Jacobian over \(k\) is isomorphic to a product of supersingular elliptic curves; equivalently, its Cartier operator on global regular differentials is zero. We distinguish \(p\)-rank from rank of the single Cartier matrix; the former is the stable rank of its iterates. “Marked parameters” means coefficients in this displayed normalized pencil. The geometric isomorphism count uses the complete bielliptic Picard invariant described below.

## Proof

**1. Cartier operator.** A basis of global regular one-forms on \(C_a\) is
\[
\omega_1=dx/y^2,\qquad \omega_2=x\,dx/y^2,\qquad \omega_3=dx/y.
\]
Assume \(p=6m+5\). Write \(f=f_a\). Using \(y^3=f\), the \(p^{-1}\)-linearity of Cartier, and \(\mathcal C(x^{pr+p-1}dx)=x^r dx\), one obtains
\[
\mathcal C(\omega_1)=Q_p(a)^{1/p}\omega_3,
\quad\mathcal C(\omega_2)=0,
\quad\mathcal C(\omega_3)=P_p(a)^{1/p}\omega_1,
\]
where
\[
P_p(a)=[u^{3m+2}](u^2+au+1)^{4m+3}.
\]
Indeed, \(1/y^2=f^{(p-2)/3}/y^p\) and \(1/y=f^{(2p-1)/3}/y^{2p}\). Parity of \(f\) forces all the other possible coefficients to vanish; the largest exponents required for the next Cartier basis element exceed the relevant polynomial degrees. Hence the Cartier operator has rank two if both \(P_p\) and \(Q_p\) are nonzero, and rank zero if they both vanish.

**2. An exact coefficient identity in every characteristic.** For integers \(0\le d\le n<p\), write
\[
B_{n,d}(a)=[u^d](u^2+au+1)^n
=\sum_{r=0}^{\lfloor d/2\rfloor}
\frac{n!}{r!(d-2r)!(n-d+r)!}\,a^{d-2r}.
\]
(The coefficient at exponent \(2n-d\) is the same, by reciprocity.) Direct substitution of consecutive coefficients proves the differential equation
\[
(a^2-4)B_{n,d}''-(2n-1)aB_{n,d}'+d(2n-d)B_{n,d}=0.
\tag{1}
\]
Its coefficient recurrence is nonsingular in \(\mathbb F_p\) for the two instances used below: all \(r\) and \(n-d+r\) occurring are strictly between zero and \(p\), and the leading coefficient \(\binom nd\) is nonzero. Thus the solution polynomial of prescribed degree \(d\) and parity, if it exists, is unique up to a scalar.

Set \(D=a^2-4\), \(h=m+1\), \(Q=B_{2m+1,m}\), and \(P=B_{4m+3,3m+2}\). Multiplying equation (1) for \(Q\) by \(D^h\), then differentiating the product, yields the following *integral differential-operator identity*, where \(L_{n,d}\) denotes the left-hand operator in (1):
\[
L_{4m+3,\,3m+2}(D^hQ)
=D^hL_{2m+1,\,m}(Q)-8hp\,D^{h-1}Q.
\tag{2}
\]
Since \(p=6m+5\), both \(P\) and \(D^h Q\) solve the same equation (1) modulo \(p\), and both have degree \(3m+2\), the same parity, and nonzero leading coefficients. By the recurrence uniqueness,
\[
\boxed{P_p(a)=c_p(a^2-4)^{m+1}Q_p(a)},
\quad c_p=\frac{\binom{4m+3}{3m+2}}{\binom{2m+1}{m}}\in\mathbb F_p^{\times}.
\tag{3}
\]
This is an identity of polynomials, not an inference from a finite search.

**3. Distinctness and smoothness.** Equation (1) for \(Q\) reads
\[
(a^2-4)Q''-(4m+1)aQ'+m(3m+2)Q=0.
\tag{4}
\]
The leading coefficient of \(Q\) is \(\binom{2m+1}{m}\), which is nonzero in \(\mathbb F_p\), so its degree is exactly \(m\). At the exceptional parameters,
\[
Q(2)=\binom{4m+2}{3m+2},\qquad
Q(-2)=(-1)^{3m+2}\binom{4m+2}{3m+2},
\]
which are nonzero modulo \(p\) because \(4m+2<p\). Suppose \(a_0\ne\pm2\) were a multiple root of multiplicity \(r\ge2\). Taking the lowest-degree nonzero Taylor term in (4) gives \((a_0^2-4)r(r-1)=0\). But \(r\le m<p\), a contradiction. Thus all \(m\) geometric roots are simple and give smooth curves. Equation (3) shows that the Cartier matrix vanishes exactly at those roots, proving superspeciality and the parameter count.

**4. Complementary \(p\)-rank and Newton strata.** If \(Q(a)\ne0\) and \(a^2\ne4\), equation (3) implies \(P(a)\ne0\). Cartier interchanges \(\omega_1\) and \(\omega_3\) by nonzero semilinear scalars and kills \(\omega_2\). Its iterated stable rank is therefore two, so the Jacobian has \(p\)-rank two and \(a\)-number one. A dimension-three principally polarized abelian variety of \(p\)-rank two has remaining symmetric Newton slopes \(1/2,1/2\); hence its slopes are \(0,0,1/2,1/2,1,1\). If \(Q(a)=0\), Cartier is zero, the Jacobian is superspecial, and all slopes are \(1/2\).

**5. The other residue class.** For \(p\equiv1\pmod3\), the involution \((x,y)\mapsto(-x,y)\) has elliptic quotient \(y^3=u^2+au+1\). Completing the square, \((2u+a)^2=4y^3+(a^2-4)\), shows that it has \(j=0\). In these characteristics that elliptic curve is ordinary. A superspecial curve cannot admit an ordinary elliptic quotient (the quotient of a superspecial abelian variety has \(p\)-rank zero). Thus no smooth member can be superspecial.

**6. Geometric isomorphism classes.** For normalized bielliptic Picard curves, Laga–Shnidman's complete geometric invariant is
\(j(C_a)=(4-a^2)/4\). In characteristic greater than three, two smooth members are geometrically isomorphic exactly when their \(a\)-parameters have the same square. The displayed polynomial has parity \(m\), hence its nonzero roots come in \(\{a,-a\}\) pairs; zero occurs precisely when \(m\) is odd, and is simple. Its \(m\) roots therefore give exactly \(\lceil m/2\rceil\) distinct geometric isomorphism classes.

## Verification

The companion `verify.py` uses only Python 3's standard library. It computes the two coefficient polynomials from the exact multinomial formula, checks identity (3) and equation (1) for every prime \(p<200\) with \(p\equiv5\pmod6\), verifies squarefreeness and absence of forbidden roots in those cases, and evaluates the exceptional characteristic-\(17\) and characteristic-\(23\) polynomials. The saved output is `verify_output.txt`, ending in `VERIFY_OK`. These finite checks corroborate, but do not establish, the all-prime theorem; that relies on equations (1)–(4) and the geometric argument above.

## Relationship to prior work

Malmskog–Rasmussen (2014) provide early background on Picard quartic models, not a superspecial count over varying positive characteristics. Kazemifard–Tafazolian (2015), §3, determine the Newton polygon of special Fermat-covered Picard curves, including the \(a=0\) member, but do not give the varying-\(a\) squarefree superspecial polynomial. Estrada-Sarlabous (1991) obtains general Hasse–Witt criteria for Picard Jacobians; its full article was not accessible for a direct comparison of every implication. Nourozi–Rahmati (2023), §3, give general coefficient expressions for Cartier matrices and state a constant \(a\)-number for all quartics with nonzero constant term when \(p\equiv2\pmod3\). That broad assertion is in tension with both the classical superspecial Fermat examples and the explicit specialization \(p=17,a=5\); the polynomial identity and direct Cartier computation here independently establish the distinction. Laga–Shnidman (arXiv 2023; journal 2025), §2.3, identify the same bielliptic pencil and its complete geometric isomorphism invariant, without the all-prime superspecial root count. Later genus-three superspecial enumerations for bounded characteristics do not by themselves imply the uniform all-prime result.

The new contribution claimed here is specifically the uniform identity (3), separability, superspecial root count and moduli count, and two-stratum Newton classification for \(p\equiv2\pmod3\), not the general Cartier coefficient method or the pre-existing Fermat special cases.

## Limitations

This is a pencil-specific geometric classification over algebraic closures, not a complete classification of all genus-three Picard curves. It does not determine individual Frobenius orbit lengths or fields of definition of the roots for arbitrary \(p\). It does not classify all Newton strata for \(p\equiv1\pmod3\). The closest older 1991 article was available by abstract only, and additional unindexed pre-existing computations may affect historical priority; independent expert review is still needed. Numerical tests for primes below 200 are supporting checks only.

## References

1. B. Malmskog and C. Rasmussen, *Picard curves over Q with good reduction away from 3*, arXiv:1407.7892 (first submitted 2014-07-29), https://arxiv.org/abs/1407.7892.
2. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields Appl. 34 (2015), 107–122, DOI:10.1016/j.ffa.2014.12.002.
3. J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic p > 0*, Math. Nachr. 152 (1991), 329–340, DOI:10.1002/mana.19911520125.
4. V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823 (2023), https://arxiv.org/abs/2306.07823.
5. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (first submitted 2023-08-29), J. London Math. Soc. 112 (2025), e70347, https://arxiv.org/abs/2308.15297.
6. M. Ohashi et al., *Listing superspecial curves of genus three using Richelot isogeny graphs*, arXiv:2401.10500 (2024), https://arxiv.org/abs/2401.10500.

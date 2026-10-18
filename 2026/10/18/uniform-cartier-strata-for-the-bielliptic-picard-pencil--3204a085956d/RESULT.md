# Uniform Cartier strata for the bielliptic Picard pencil

## Finding
Let \(p\ge5\) be a prime, let \(k=\overline{\mathbf F}_p\), and take \(t\in k\setminus\{1,-1\}\). Consider the smooth genus-three curve
\[
C_t:\quad y^3=x^4+2tx^2+1.
\]
Write \(p=6m+1\) or \(p=6m+5\) and put
\[
H_p(t)=[z^m](z^2+2tz+1)^e,
\quad e=\begin{cases}2m,&p=6m+1,\\2m+1,&p=6m+5.\end{cases}
\]
Equivalently,
\[
H_p(t)=\sum_{j=0}^{\lfloor m/2\rfloor}\binom ej\binom{e-j}{m-2j}(2t)^{m-2j}\pmod p.
\]
The exact \(p\)-rank and \(a\)-number of \(\operatorname{Jac}(C_t)\) are
\[
\begin{array}{c|cc|cc}
 &\multicolumn{2}{c|}{H_p(t)\ne0}&\multicolumn{2}{c}{H_p(t)=0}\\
 &p\text{-rank}&a\text{-number}&p\text{-rank}&a\text{-number}\\\hline
p\equiv1\pmod6&3&0&1&2\\
p\equiv5\pmod6&2&1&0&3
\end{array}.
\]
The polynomial \(H_p\) has degree exactly \(m\), is squarefree over \(k\), and does not vanish at \(t=\pm1\). Hence precisely \(m\) distinct smooth **parameters** form the exceptional stratum. For \(p=5\), \(m=0\) and the exceptional stratum is empty. In the \(p\equiv5\pmod6\) case the exceptional Jacobians are superspecial; this term is used in the standard sense \(a=g\).

## Assumptions and scope
All curves and invariants are geometric, over \(\overline{\mathbf F}_p\), not merely evaluated at rational parameters. The affine equation has four distinct roots if and only if \(t^2\ne1\); because \(3\) and \(4\) are coprime, its smooth projective completion is a plane quartic of genus \(3\). The theorem concerns exact pointwise Cartier rank, stabilized Frobenius rank (\(p\)-rank), and the \(a\)-number. It does not claim distinct exceptional parameters necessarily represent distinct geometric isomorphism classes.

## Proof
**Cartier calculation.** Set \(Q(z)=z^2+2tz+1\). A basis of regular differentials is
\[
\omega_0=dx/y^2,\qquad\omega_1=x\,dx/y^2,\qquad\omega_2=dx/y.
\]
In characteristic \(p\), use the standard identity \(\mathcal C(g^p\eta)=g\,\mathcal C(\eta)\), and \(\mathcal C(x^{pn+p-1}dx)=x^n dx\). Coefficients below are written *before* applying the inverse-Frobenius \(p\)-th root, which does not affect zero patterns or rank.

For \(p=6m+1\), the Cartier matrix is diagonal, with coefficients
\[
A=[z^{3m}]Q^{4m},\quad B=[z^{2m}]Q^{4m},\quad H=[z^m]Q^{2m}.
\]
Here reciprocity of \(Q\) identifies the \(\omega_1\)-coefficient originally indexed by \(6m\) with \(B\), and likewise the \(\omega_2\)-coefficient originally indexed by \(3m\) with \(H\). The coefficient identities are
\[
A=(t^2-1)^mH,\qquad
B=(-1)^m\binom{4m}{m}(t^2-1)^m.\tag{1}
\]
The second scalar is nonzero because \(4m<p\).

For \(p=6m+5\), \(\mathcal C(\omega_1)=0\), and the two other basis vectors are interchanged:
\[
\mathcal C(\omega_0)=A^{1/p}\omega_2,\quad
\mathcal C(\omega_2)=H^{1/p}\omega_0,
\]
where
\[
A=[z^{3m+2}]Q^{4m+3}=2(t^2-1)^{m+1}H,\quad
H=[z^m]Q^{2m+1}.\tag{2}
\]
In each case the \(p\)-th roots are interpreted in the algebraic closure and the basis formula is semilinear. Thus, away from \(t=\pm1\), the diagonal case has ranks \(3\) and \(1\), and the exchanging case has ranks \(2\) and \(0\), according to whether \(H\ne0\) or \(H=0\). Every nonzero diagonal entry, and each nonzero two-cycle, remains nonzero under all semilinear Cartier iterates. Therefore stable Cartier rank equals the displayed rank and equals the geometric \(p\)-rank; the \(a\)-number is genus minus Cartier rank.

**Uniform coefficient identities.** Write \(P_{e,n}(t)=[z^n]Q(z)^e\). Direct differentiation of the binomial expansion yields the differential equation
\[
(1-t^2)P_{e,n}''+(2e-1)tP_{e,n}'+n(n-2e)P_{e,n}=0.\tag{3}
\]
Its coefficient recurrence is
\[
a_{j+2}=\frac{(j-n)(j+n-2e)}{(j+1)(j+2)}a_j.\tag{4}
\]
For each of the pairs \((e,n)=(4m,3m),(4m,2m),(4m+3,3m+2)\), all denominators and both downward-recurrence numerator factors are nonzero for indices less than \(n\) in characteristic \(p\). Consequently, a polynomial solution of (3) of degree at most \(n\) is unique up to a scalar.

The conjugation formula for \(R=(t^2-1)^rS\), where \(S\) solves (3) with indices \((e-2r,n-2r)\), shows that its differential operator differs from (3) only by multiplication by \(2r(2e-2r+1)/(t^2-1)\), provided \(n(n-2e)+4r(e-r)=(n-2r)(n-2r-2(e-2r))\). For \((e,n,r)=(4m,3m,m)\), that discrepancy is \(2m(6m+1)/(t^2-1)=0\) modulo \(p\); for \((4m+3,3m+2,m+1)\), it is \(2(m+1)(6m+5)/(t^2-1)=0\). The factor \((t^2-1)^m\) itself solves the \((4m,2m)\) equation, giving the second identity of (1).

To determine the constants, differentiate at \(t=1\) using
\[
P_{e,n}^{(j)}(1)=(e)_j2^j\binom{2e-2j}{n-j}.
\]
For (1), taking the \(m\)-th derivative gives the same nonzero value \(2^m(4m)!/(3m)!\) for \(P_{4m,3m}\) and \((t^2-1)^mP_{2m,m}\). For (2), taking the \((m+1)\)-st derivative gives the coefficient ratio \(2\), using \(- (4m+3)\equiv2(m+1)\pmod p\). Finally, evaluation at \(t=0\) yields the scalar \((-1)^m\binom{4m}{m}\) in (1).

**Exact exceptional count.** The leading coefficient of \(H=P_{e,m}\) is \(2^m\binom e m\ne0\pmod p\). At \(t=\pm1\),
\[
H(\pm1)=(\pm1)^m\binom{2e}{m}\ne0\pmod p,
\]
because \(2e<p\). If \(H\) had a multiple root outside \(\pm1\), equation (3) would force all successive derivatives to vanish there; since \(m<p\), this forces \(H=0\), a contradiction. Thus \(H\) has exactly \(m\) distinct roots over \(k\), all allowed smooth parameters.

## Verification
The accompanying pure-Python file `verify.py` reproduces the coefficient polynomials directly from binomial coefficients for 18 primes between \(5\) and \(71\). For each, it checks identities (1) or (2), the degree of \(H\), the values at \(\pm1\), and \(\gcd(H,H')=1\). The infinite-characteristic proof is algebraic as above, and does not rest on the finite computation.

## Relationship to prior work
Laga and Shnidman introduce and study the bielliptic Picard curves \(y^3=x^4+ax^2+b\), their Pryms, and quaternionic multiplication; this normalized smooth pencil specializes their family [1]. Their inspected text does not give the pointwise characteristic-dependent \(p\)-rank/\(a\)-number strata or the polynomial \(H_p\). Nourozi and Rahmati investigate Cartier rank for Picard curves, including general coefficient methods [2]. A broad nonvanishing assertion appearing in the inspected preprint does not cover the exceptional coefficients here: for example at \(p=11,t=0\), direct substitution in (2) makes all three Cartier entries zero while the curve is smooth. The general computational treatment of Cartier–Manin matrices and \(L\)-polynomials by Asif, Fité, and Pentland [3] concerns a different generic arithmetic question and does not state this complete stratification. The result is a complete rank stratification rather than a new general Cartier formula.

## Limitations
The assertion is restricted to prime characteristic \(p\ge5\) over algebraically closed fields and smooth parameters \(t^2\ne1\). It gives \(p\)-rank and \(a\)-number, not the full Newton polygon or Ekedahl–Oort type. The polynomial roots are counted as parameters, not moduli points. A mathematically equivalent unindexed specialization of general Picard or hypergeometric literature cannot be entirely ruled out; no independent external validation has been performed.

## References
[1] J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297v1 (first posted 2023-08-29), https://arxiv.org/abs/2308.15297.

[2] V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823v1 (first posted 2023-06-13), https://arxiv.org/abs/2306.07823.

[3] S. Asif, F. Fité and D. Pentland, *Computing L-Polynomials of Picard curves from Cartier-Manin matrices*, arXiv:2010.07247v1 (first posted 2020-10-14), https://arxiv.org/abs/2010.07247.

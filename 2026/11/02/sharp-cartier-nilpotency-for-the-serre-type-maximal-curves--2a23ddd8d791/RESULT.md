# Sharp Cartier nilpotency for the Serre-type maximal curves

## Finding

For every prime \(p\), integer \(t\ge1\), \(q=p^t\), and odd integer \(n\ge3\), let \(X=X(q,n)\) be the smooth projective model of
\[
y^{q^2}-y=x^m,\qquad m=\frac{q^n+1}{q+1}.
\]
Let \(\mathcal C\) be the Cartier operator on \(H^0(X,\Omega_X^1)\). Its exact nilpotency index is
\[
\boxed{\mathcal C^{tn}=0\quad\text{and}\quad \mathcal C^{tn-1}\ne0.}
\]
More precisely, writing \(b=(q^{n-1}-1)/(q+1)\), the regular differential
\[
\omega=x^{p^{t-1}b-1}y^{p^{t-1}}dx
\]
satisfies \(\mathcal C^{tn-1}(\omega)=-dx\ne0\). In characteristic two the displayed minus sign equals plus.

## Assumptions and scope

All curves, divisors, and differential spaces are considered over an algebraically closed field of characteristic \(p\). Since \(n\) is odd, \(m\) and \(b\) are integers and \(m\) is prime to \(p\). Set \(Q=q^2\) and \(g=(Q-1)(m-1)/2=(q-1)(q^n-q)/2\). The affine equation gives a separable extension of degree \(Q\) of \(k(x)\), ramified only at its unique point \(P_\infty\) at infinity, and its smooth completion has genus \(g\). The canonical divisor is \((2g-2)P_\infty\) for the differential \(dx\), and
\[
-v_{P_\infty}(x)=Q,\quad -v_{P_\infty}(y)=m,\quad v_{P_\infty}(dx)=2g-2.
\]
Consequently the \(g\) monomials \(x^iy^jdx\) with \(i\ge0\), \(0\le j<Q\), and \(Qi+mj\le2g-2\) form a basis of \(H^0(X,\Omega_X^1)\).

## Proof

**Step 1: Cartier's monomial rule.** Write \(i=pi_1+i_0\) and \(j=pj_1+j_0\), with \(0\le i_0,j_0<p\). Since \(m\equiv1\pmod p\), expanding \(y^{j_0}=(y^Q-x^m)^{j_0}\) and applying the standard rules for Cartier shows that \(\mathcal C(x^iy^jdx)=0\) when \(i_0+j_0<p-1\). Otherwise put
\[
\nu=i_0+j_0-(p-1),\qquad S=\frac{i+m(j_0-\nu)-(p-1)}p,\qquad E=j_1+\frac Qp\nu.
\]
Then
\[
\mathcal C(x^iy^jdx)=(-1)^{j_0-\nu}\binom{j_0}{\nu}\,x^S y^E dx.
\]
Here \(0\le\nu\le j_0<p\), so the binomial coefficient is nonzero modulo \(p\). The result is again regular because Cartier acts on regular differentials. This rule also follows directly from \(\mathcal C(f^p x^{p-1}dx)=f\,dx\) and \(\mathcal C(f^p x^a dx)=0\) for \(0\le a<p-1\).

**Step 2: The explicit witness is holomorphic.** The identity
\[
q^2b+m=q^n-q+1
\]
gives the pole weight of \(\omega\) as
\[
W=q^2(p^{t-1}b-1)+mp^{t-1}=p^{t-1}(q^n-q+1)-q^2.
\]
Because \(p^{t-1}\le q-1\) and \(q\ge2\),
\[
W\le(q-1)(q^n-q+1)-q^2\le(q-1)(q^n-q)-2=2g-2.
\]
Both exponents of \(x\) and \(y\) in \(\omega\) are nonnegative and the \(y\)-exponent is strictly less than \(Q\). Thus \(\omega\) belongs to the stated holomorphic basis. Similarly \(dx\) is a nonzero holomorphic differential.

**Step 3: The full nonzero chain.** For \(1\le s\le t\), put
\[
\omega_s=x^{p^{s-1}b-1}y^{p^{s-1}}dx.
\]
For \(s\ge2\), the residues are \(i_0=p-1\), \(j_0=0\), so the rule in Step 1 gives \(\mathcal C(\omega_s)=\omega_{s-1}\). For \(s=1\), we have \(b\equiv-1\pmod p\), hence \(i_0=p-2\), \(j_0=1\), \(\nu=0\), and, using \(b+m=q^{n-1}\),
\[
\mathcal C(\omega_1)=-x^{p^{t(n-1)-1}-1}dx.
\]
Set \(K=t(n-1)-1\ge1\). Repeatedly applying \(\mathcal C(x^{p^a-1}dx)=x^{p^{a-1}-1}dx\) for \(a\ge1\) yields
\[
\mathcal C^{t+K}(\omega_t)=-dx\ne0.
\]
Since \(t+K=tn-1\), this proves \(\mathcal C^{tn-1}\ne0\).

**Step 4: The universal upper bound.** The curves \(X(q,n)\) are maximal over \(\mathbb F_{q^{2n}}\) (Abdón--Bezerra--Quoos). Garcia--Tafazolian, Theorem 3.3, proves that maximality over \(\mathbb F_{p^{2N}}\) forces \(\mathcal C^N=0\) on regular differentials. Here \(q^n=p^{tn}\), so \(N=tn\) and \(\mathcal C^{tn}=0\). The same identity persists after extension to the algebraic closure. Together with Step 3 this proves the asserted exact index.

## Verification

The standalone exact-integer checker `verify.py` regenerates the holomorphic monomial basis, independently implements the Cartier monomial rule, verifies that every computed image stays in the basis, and determines all finite chains for the listed sample parameters. It also reconstructs the proposed witness and checks that its \((tn-1)\)-st image is \(-dx\). Run with `python3 verify.py`. All listed tests produced `VERIFY_OK` when packaged. These finite checks corroborate the formula; the unrestricted theorem is proved in the four steps above.

## Relationship to prior work

Shafighi (2026), arXiv:2610.15266v1, computes the \(a\)-number of these specific curves using their holomorphic monomial basis and Cartier action. The present assertion concerns the **last nonzero Cartier iterate**, a different invariant that is not implied by an \(a\)-number. Garcia--Tafazolian (2008), Theorem 3.3, establishes the **upper** nilpotence bound for arbitrary maximal curves; it does not assert that the bound is attained. Almeida Filho--Tafazolian--Vieira (2026), arXiv:2610.17476v1, calculate higher Cartier ranks and nilpotency on a different additive-polynomial family of degree-\(p\) Artin--Schreier covers; their explicit formulas do not contain this family. Groen (2022), arXiv:2208.06504, treats powers of Cartier on degree-\(p\) Artin--Schreier covers and provides broader methods, but does not state the exact index for the present degree-\(q^2\) equation. A literature search cannot establish absolute priority; the proposed contribution is the explicit sharpness proof for every \(p,t,n\) in the displayed Serre-type family.

## Limitations

Only the exact index, not all intermediate Cartier ranks, the full Ekedahl--Oort type, or a numerical count of witnesses to maximality is determined. The claim assumes odd \(n\ge3\) and the exact monomial equation, not arbitrary Artin--Schreier or additive curves. Independence from every unpublished or differently parameterized equivalent result has not been established. Scientific checking described here is not an independent mathematical audit.

## References

1. M. Shafighi, *The a-number of the Serre-type maximal curves of Abdón-Bezerra-Quoos*, arXiv:2610.15266v1 (2026-10-11), https://arxiv.org/abs/2610.15266.
2. M. Abdón, M. Bezerra, D. Quoos, *Further examples of maximal curves*, Journal of Pure and Applied Algebra (2009), https://doi.org/10.1016/j.jpaa.2008.11.037.
3. A. Garcia and S. Tafazolian, *Certain maximal curves and Cartier operators*, Acta Arithmetica 135 (2008), 199--218, Theorem 3.3, https://www.impan.pl/shop/publication/transaction/download/product/81908.
4. G. B. Almeida Filho, S. Tafazolian, S. C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer-van der Vlugt curves*, arXiv:2610.17476v1 (2026), https://arxiv.org/abs/2610.17476.
5. S. R. Groen, *Powers of the Cartier operator on Artin-Schreier covers*, arXiv:2208.06504 (2022), https://arxiv.org/abs/2208.06504.

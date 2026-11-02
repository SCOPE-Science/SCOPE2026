# Irreducible residual factor and dual root geometry of prime-power Ramanujan-sum polynomials

## Finding

For every prime \(p\) and integer \(a\ge1\), put \(P=p^{a-1}\), define the Ramanujan sums \(c_n(k)=\sum_{1\le j\le n,\,(j,n)=1}e^{2\pi i jk/n}\), and form \(R_n(X)=\sum_{k=0}^{n-1}c_n(k)X^k\). Set
\[
E_{p,a}(X)=\sum_{j=0}^{p-2}(p-1-j)X^{jP}.
\]
Then the exact primitive integral factorization is
\[
R_{p^a}(X)=p^{a-1}(1-X^P)E_{p,a}(X).
\]
For \(p=2\), \(E_{2,a}=1\). For every **odd prime** \(p\), the polynomial \(E_{p,a}\) is monic, irreducible over \(\mathbb Q\) and over \(\mathbb Q_p\), with degree \(d=(p-2)P\). More precisely, \(E_{p,a}(X+1)\) is \(p\)-Eisenstein. If \(\alpha\) is any root, then
\[
\nu_p(\alpha-1)=\frac{1}{(p-2)P},
\qquad
\left(\frac{p-1}{p-2}\right)^{1/P}\le |\alpha|\le 2^{1/P}.
\]
Here the normalized extension valuation satisfies \(\nu_p(p)=1\). Thus adjoining any residual root gives a totally ramified degree-\(d\) extension of \(\mathbb Q_p\), while all its complex conjugates lie strictly outside the closed complex unit disk. The residual polynomial has exactly one real root, which is negative. Its discriminant is explicitly
\[
\operatorname{Disc}(E_{p,a})
=(-1)^{(d-1)/2}\frac{2^P P^d p^{P(p-3)}(p-1)^{P(p-3)}}{p-1}.
\]
This is an integer for every odd prime \(p\), including \(p=3\).

Consequently, the *full* factorization of \(R_{p^a}\) into irreducibles over \(\mathbb Q\) consists of the scalar \(p^{a-1}\), the cyclotomic factors \(\prod_{m\mid P}\Phi_m(X)\), and (for odd \(p\)) exactly one additional irreducible factor \(E_{p,a}\). Each cyclotomic zero is simple, and there are no other zeros on or inside the complex unit circle.

## Assumptions and scope

The exponent \(a\) is any positive integer and \(p\) is any rational prime. Irreducibility is asserted for odd \(p\); the \(p=2\) case is the explicit binomial above. All polynomials and factorizations are over \(\mathbb Z[X]\) or \(\mathbb Q[X]\) as indicated. For a chosen embedding into an algebraic closure of \(\mathbb Q_p\), the valuation is normalized by \(\nu_p(p)=1\). Complex absolute values refer to all archimedean embeddings of the residual root.

## Proof

**1. Known coefficient formula and the residual factor.** The prime-power Ramanujan sum is \((p-1)P\) for \(pP\mid k\), is \(-P\) for \(P\mid k\) but \(pP\nmid k\), and vanishes otherwise. Therefore, with \(Y=X^P\),
\[
R_{p^a}(X)=P\left[(p-1)-\sum_{j=1}^{p-1}Y^j\right].
\]
The identity
\[
(p-1)-\sum_{j=1}^{p-1}Y^j
=(1-Y)\sum_{j=0}^{p-2}(p-1-j)Y^j
\]
follows by comparing coefficients. This is the prime-power specialization explicitly derived by Tóth [1, formula (19)]; the expression itself is prior work.

**2. Eisenstein irreducibility.** For odd prime \(p\), write \(Q_p(Y)=\sum_{j=0}^{p-2}(p-1-j)Y^j\). In \(\mathbb F_p[Y]\),
\[
Q_p(Y)\equiv (Y-1)^{p-2}\pmod p.
\]
Indeed, the difference of the two sides is the zero polynomial by the characteristic-\(p\) identity \(Q_p(Y)(Y-1)^2=Y^p-pY+(p-1)\), which reduces to \((Y-1)^p\) modulo \(p\); cancellation in the integral domain \(\mathbb F_p[Y]\) gives the stated congruence. By Frobenius,
\[
E_{p,a}(X)=Q_p(X^P)\equiv(X-1)^{(p-2)P}\pmod p.
\]
Consequently \(E_{p,a}(X+1)\equiv X^d\pmod p\), so all its non-leading coefficients are multiples of \(p\). Its leading coefficient is \(1\), while its constant term is
\[
E_{p,a}(1)=\sum_{r=1}^{p-1}r=\frac{p(p-1)}2,
\]
which is divisible by \(p\), not by \(p^2\) because \(p\) is odd. Eisenstein's criterion over both \(\mathbb Q\) and \(\mathbb Q_p\) proves irreducibility. It also gives total ramification, and the single-edge Newton polygon of \(E_{p,a}(1+Z)\) has endpoints \((0,1)\) and \((d,0)\). Thus every root \(\alpha\) satisfies \(\nu_p(\alpha-1)=1/d\).

**3. Explicit complex annulus.** For a real positive-coefficient polynomial \(A(Y)=\sum_{j=0}^m a_jY^j\), all its nonzero roots \(\beta\) satisfy
\[
\min_{j<m}\frac{a_j}{a_{j+1}}\le|\beta|\le\max_{j<m}\frac{a_j}{a_{j+1}}.
\]
For completeness, if \(0<a_0\le\cdots\le a_m\), then \((1-Y)A(Y)=a_0+\sum_{j=1}^m(a_j-a_{j-1})Y^j-a_mY^{m+1}\). A root with \(|Y|>1\) would force \(a_m|Y|^{m+1}\le a_m|Y|^m\), an impossibility. This bounds roots in the unit disk for increasing coefficients. Applying it to the reciprocal polynomial bounds decreasing-coefficient roots outside the unit disk, and rescaling the variable yields the displayed two-sided ratio bound.

For \(Q_p\), the consecutive coefficient ratios are \((p-1)/(p-2),(p-2)/(p-3),\ldots,2\). Hence every root \(\beta\) of \(Q_p\) satisfies \((p-1)/(p-2)\le|\beta|\le2\). Since \(\alpha^P=\beta\), take \(P\)-th roots to obtain the asserted bound. In particular, \(|\alpha|>1\).

**4. Unique real residual root.** The polynomial identity from step 2 gives
\[
(Y-1)^2Q_p(Y)=G_p(Y):=Y^p-pY+(p-1).
\]
Since \(p\) is odd, \(G_p'(Y)=p(Y^{p-1}-1)\). On \(( -\infty,-1)\), \(G_p\) is strictly increasing from \(-\infty\) to \(G_p(-1)=2(p-1)>0\). On \([-1,1]\), its minimum occurs at \(1\), where \(G_p(1)=0\) with a double zero; and \(G_p(Y)>0\) for \(Y>1\). Therefore \(Q_p\) has exactly one real zero, negative and smaller than \(-1\). Because \(P\) is odd, each real equation \(X^P=\beta\) has exactly one real solution. This proves the residual real-zero assertion.

**5. Exact residual discriminant.** Let \(m=p-2\), the degree of \(Q_p\). If \(\beta\) is a root of \(Q_p\), the identity \(G_p=(Y-1)^2Q_p\) and \(G_p(\beta)=0\) give
\[
Q_p'(\beta)=\frac{p(p-1)}{\beta(\beta-1)}.
\]
Because \(m\) is odd, the products over all \(m\) roots are \(\prod\beta=-(p-1)\) and \(\prod(\beta-1)=-Q_p(1)=-p(p-1)/2\). Taking the product of the displayed derivative identity and the standard monic-polynomial resultant formula yields
\[
|\operatorname{Disc}(Q_p)|=2p^{p-3}(p-1)^{p-4}.
\]
(The exponent \(p-4\) is \(-1\) when \(p=3\), and the right side is then exactly \(1\).) For \(E(X)=Q_p(X^P)\), the chain rule \(E'(X)=PX^{P-1}Q_p'(X^P)\) and the product of its values over all \(d=mP\) roots yield
\[
|\operatorname{Disc}(E)|=P^d(p-1)^{P-1}|\operatorname{Disc}(Q_p)|^P
=\frac{2^P P^d p^{P(p-3)}(p-1)^{P(p-3)}}{p-1}.
\]
The prior step showed there is exactly one real root; the other \(d-1\) roots form \((d-1)/2\) nonreal conjugate pairs. The sign of the discriminant is therefore \((-1)^{(d-1)/2}\), completing the formula.

**6. Exhaustiveness and multiplicities.** The factor \(1-X^P\) is the product of the distinct \(\Phi_m(X)\) for \(m\mid P\). The residual factor is irreducible, hence separable in characteristic zero, and by step 3 none of its roots lies on the unit circle. The two factors are coprime; no further rational irreducible factors exist.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It independently computes Ramanujan sums by their prime-power arithmetic formula, compares every coefficient with the proposed product, and checks translated Eisenstein congruences exactly for 14 prime-power cases, and independently evaluates six discriminants by exact Sylvester resultants. The supplied verifier returned: `VERIFY_OK: 14 exact prime-power cases; 417 independently computed Ramanujan coefficients; 265 shifted-Eisenstein coefficient divisibility checks; 6 independent resultant-discriminant checks.` These are finite consistency tests; universal assertions follow from the symbolic proof above.

## Relationship to prior work

Tóth [1] defined these polynomials, gave the coefficient formula, and proved the visible cyclotomic divisor \(1-X^P\) for every prime power. Those claims are explicitly credited and not new. The additional assertion proved here is that for every odd prime power the remaining integral factor is **irreducible even over the local field**, admits an exact normalized root valuation, has a closed discriminant formula, and has all complex roots confined to an explicit annulus outside the unit circle, together with a unique real root. A later treatment of logarithmic derivatives of cyclotomic polynomials [2, Section 6] concerns evaluations at roots of unity, not this residual irreducibility/geometry classification. As the original formula immediately implies the polynomial under study, unlocated equivalent irreducibility treatments of derivatives of prime-power cyclotomic polynomials remain a legitimate prior-art risk.

## Limitations

No claim is made for arbitrary moduli with multiple distinct prime factors. The complex annulus is an explicit universal enclosure, not an assertion that each boundary circle contains a root. The exact discriminant does not determine Galois groups or splitting fields beyond the local ramification statement. The factorization formula itself was already known; the proved contribution is the complete residual irreducibility and local/complex root classification.

## References

[1] László Tóth, *Some remarks on Ramanujan sums and cyclotomic polynomials*, arXiv:1002.3221v1 (17 February 2010), Section 3, particularly Theorems 5 and 7 and equation (19).

[2] B. Bzdęga, A. Herrera-Poyatos and P. Moree, *Cyclotomic polynomials at roots of unity*, arXiv:1611.06783v2 (2016), Section 6.

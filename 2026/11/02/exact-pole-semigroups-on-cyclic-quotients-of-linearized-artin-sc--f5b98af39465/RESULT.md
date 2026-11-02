# Exact pole semigroups on cyclic quotients of linearized Artin–Schreier curves

## Finding
Let \(p\ge5\) be an odd prime, \(N\ge2\), and \(k\) an algebraically closed field of characteristic \(p\). For every linearized polynomial \(R(X)=\sum_{j=0}^{N}B_jX^{p^j}\) with \(B_0B_N\ne0\), let \(W_R\) be the smooth projective normalization of \(Y^p-Y=XR(X)\), and let \(Z_R\) be its quotient by \((X,Y)\mapsto(\zeta X,\zeta^2Y)\), \(\zeta\in\mathbb F_p^\times\). Write \(P_\infty\) for the unique point of \(Z_R\) above infinity, and put
\[
L=\frac{p-1}{2},\qquad d=\frac{p^N-1}{p-1}-2.
\]
Then \(g(Z_R)=(p^N-1)/2\), and the complete Weierstrass semigroup at \(P_\infty\), *with its minimal generators*, is
\[
\boxed{H(P_\infty)=\langle p,\ p+d,\ p+2d,\ldots,\ p+Ld\rangle.}
\]
The Apéry set relative to \(p\) has the representatives
\[
a_0=0,\quad a_j=p+jd\ (1\le j\le L),\quad a_j=2p+jd\ (L<j\le p-1).
\]
It follows that the conductor is \(p^N-p+2\), the semigroup type is \(L\), and the dimension of every one-point Riemann–Roch space is
\[
\ell(mP_\infty)=\sum_{j=0}^{p-1}\max\left\{0,\left\lfloor\frac{m-a_j}{p}\right\rfloor+1\right\}\quad (m\ge0).
\]
In particular these invariants are independent of all the coefficients \(B_j\) subject to the stated endpoint condition.

## Assumptions and scope
All points, ramification indices, genera, and semigroups are geometric over \(k\). The subgroup of order \(p-1\) acts faithfully. The symbol \(H(P_\infty)\) means the set of nonnegative pole orders of functions regular away from that point. The type is the number of pseudo-Frobenius gaps. No assertion is made about rational point counts or the full automorphism group. If the coefficients lie in a finite field containing \(\mathbb F_p\), the distinguished infinity point and the displayed functions are defined over that field.

## Proof
**1. Quotient and genus.** Put \(u=X^{p-1}\), \(v=Y/X^2\), and \(e=(p^N-1)/(p-1)\). These invariants generate the quotient function field, since adjoining \(X\) gives an extension of degree at most \(p-1\), and the stated scalar group already has that order. Dividing the original equation by \(X^2\) gives
\[
u^2v^p-v=\Psi(u),\qquad \Psi(u)=\sum_{j=0}^N B_j u^{(p^j-1)/(p-1)}.
\]
The last polynomial has degree \(e\), with \(e>2\). The original Artin–Schreier curve has one pole of order \(p^N+1\), prime to \(p\), so its genus is \((p-1)p^N/2\). The scalar action fixes its sole point at infinity and the affine point \((0,0)\), both with stabilizer order \(p-1\). The \(p-1\) points \((0,b)\), \(b\in\mathbb F_p^\times\), have stabilizer order \(2\), while no other affine point has nontrivial stabilizer. Tame Riemann–Hurwitz therefore gives
\[
(p-1)p^N-2=(p-1)(2g(Z_R)-2)+2(p-2)+(p-1),
\]
whence \(g(Z_R)=(p^N-1)/2\).

**2. Places and explicit pole functions.** At any point \(Q\) above \(u=\infty\), write \(\operatorname{ord}_Q(u)=-r<0\). The quotient equation forces a pole of \(v\), say \(\operatorname{ord}_Q(v)=-a\); comparing the unique leading terms yields \(2r+pa=er\), or \(pa=(e-2)r=dr\). Because \(d\equiv-1\pmod p\), \(p\mid r\). As the map \(u:Z_R\to\mathbb P^1\) has degree \(p\), this proves that there is exactly one place \(P_\infty\) above infinity and
\[
\operatorname{ord}_{P_\infty}(u)=-p,\qquad \operatorname{ord}_{P_\infty}(v)=-d.
\]
At finite places with \(u\ne0\), \(v\) is integral because its defining polynomial has unit leading coefficient. To analyze \(u=0\), set \(w=1/v\), so \(u^2-w^{p-1}=\Psi(u)w^p\). With \(L=(p-1)/2\), write \(u=w^Lz\) and divide by \(w^{p-1}\). The equation becomes \(z^2-1=w\Psi(w^Lz)\). Since \(p\) is odd, there are two distinct smooth branches at \(w=0\), both with \(\operatorname{ord}(u)=L\) and \(\operatorname{ord}(v)=-1\). The remaining point over \(u=0\) is the smooth finite point \((u,v)=(0,-B_0)\). The ramification-degree sum \(2L+1=p\) confirms no other branches.

For every \(1\le j\le p-1\), the function
\[
f_j=u^{\lceil j/L\rceil}v^j
\]
is regular at both poles of \(v\) above zero, and everywhere else away from infinity. It has pole order \(a_j=p\lceil j/L\rceil+jd\), while \(u\) has pole order \(p\). In particular \(p,p+d,\dots,p+Ld\) belong to \(H(P_\infty)\); when \(L<j\le p-1\), \(a_j=(p+Ld)+(p+(j-L)d)\).

**3. Exactness by Apéry and genus.** Let \(S=\langle p,p+d,\ldots,p+Ld\rangle\). Because \(d\equiv-1\pmod p\), the residues of \(a_0,\dots,a_{p-1}\) modulo \(p\) are distinct. A sum of \(\ell\) non-\(p\) generators, with subscripts totaling \(s\), has value \(\ell p+sd\), with \(\ell\ge\lceil s/L\rceil\). In the residue class of \(jd\) modulo \(p\), every possible nonnegative subscript sum satisfies \(s\equiv j\pmod p\), so \(s\ge j\) when \(1\le j<p\); since \(d>0\), the least value is exactly \(a_j=p\lceil j/L\rceil+jd\). This proves that the displayed list is the full Apéry set of \(S\).

The standard Apéry genus formula gives
\[
\#(\mathbb Z_{\ge0}\setminus S)=\frac1p\sum_{j=0}^{p-1}a_j-\frac{p-1}{2}=\frac{(p-1)(d+2)}2=\frac{p^N-1}{2}=g(Z_R).
\]
Since \(S\subseteq H(P_\infty)\), and the Weierstrass gap theorem gives exactly \(g(Z_R)\) gaps for \(H(P_\infty)\), equality follows.

**4. Further invariants.** The \(L+1\) displayed generators are minimal: for \(1\le j\le L\), any sum of two or more positive generators in the same residue as \(p+jd\) has strictly larger value. The largest Apéry element is \(a_{p-1}=2p+(p-1)d\), giving conductor \(a_{p-1}-p+1=p^N-p+2\). In the semigroup partial order on the Apéry set, the maximal elements are precisely \(a_j\) for \(L<j\le p-1\): every earlier \(a_j\) is below \(a_{j+L}\), and no two of the latter can be comparable because their positive difference is smaller than the least element of its residue class. Thus the pseudo-Frobenius numbers are \(a_j-p=p+jd\) for \(L<j\le p-1\), and the type is \(L\). Finally every nongap has a unique expression \(a_j+tp\), \(t\ge0\), establishing the stated dimension formula.

## Verification
The accompanying `semigroup_checker.py` is a self-contained Python 3 program using no external packages. Run `python semigroup_checker.py`; successful execution concludes with `VERIFY_OK`. It independently computes minimal residue representatives by a shortest-path algorithm, checks the numerical genus, conductor, gaps, type, and Riemann–Roch dimension identity for several prime/exponent pairs. In particular \((p,N)=(5,2)\) yields \(H=\langle5,9,13\rangle\), Apéry set \(\{0,9,13,22,26\}\), genus \(12\), and conductor \(22\). These numerical tests are not a proof of the universally quantified geometric assertions; the preceding valuation and genus argument is the proof.

## Relationship to prior work
Mendoza's 2026 study of generalized Weierstrass semigroups in linearized function fields treats extensions of the form \(L(y)=h(x)\) with a constant-coefficient linearized polynomial \(L\), and presents absolute and relative maximal elements for totally ramified points (Theorem 4.2). The present quotient equation has variable leading coefficient \(u^2\) in its additive equation and the distinguished point is on the scalar-quotient curve; applying the cited linearized-field formula directly would therefore be unjustified. Navarro's 2024 work studies Riemann–Roch bases on linearized function fields, while the present explicit pole generators concern a tame invariant subfield. Prior Kummer semigroup formulas refer to different extension towers. The exact statement may have equivalent presentations elsewhere; exhaustive historical priority is not claimed.

## Limitations
This is a geometric one-point semigroup theorem. It does not calculate multipoint semigroups, rational point counts, code minimum distances, or isomorphism classes. It does not claim that all quotient curves have distinct moduli. Full historical coverage of equivalent tame-invariant constructions is not guaranteed; no independent mathematical audit has been performed.

## References
1. E. Mendoza, *On generalized Weierstrass semigroups in linearized function fields*, arXiv:2606.01369v1 (publicly submitted May 31, 2026), especially Theorem 4.2 and Examples 4.4–4.5.
2. H. Navarro, *Bases for Riemann–Roch spaces of linearized function fields with applications to generalized algebraic geometry codes*, Designs, Codes and Cryptography **92** (2024), 3033–3048.
3. A. S. Castellanos, E. A. R. Mendoza, G. Tizziotti, *On generalized Weierstrass Semigroups in arbitrary Kummer extensions of* \(\mathbb F_q(x)\), arXiv:2504.12453 (2025).
4. H. Stichtenoth, *Algebraic Function Fields and Codes*, second edition, Springer (2009), for the Artin–Schreier genus formula, Riemann–Hurwitz, and Weierstrass gap theorem.

# Modular idempotent resonance in prime dihedral quandle algebras

## Finding

Let \(p\) be an odd prime, let \(K\) be **any** field of characteristic \(p\), and let \(R_p\) be the dihedral quandle on \(\mathbb Z/p\mathbb Z\) with operation \(i\triangleright j=2j-i\). Write \(K[R_p]\) for its bilinear (generally nonassociative) quandle algebra, with basis \(e_i\) and product \(e_i e_j=e_{2j-i}\). Let \(d=\operatorname{ord}_{p}(2)\), \(L=\operatorname{lcm}(2,d)\), and \(\kappa=1+\lfloor(p-2)/L\rfloor\). Put \(\mathscr D_p=\{1,1+L,\ldots,1+(\kappa-1)L\}\).

In the **ordinary associative** group algebra \(K[T]/(T^p-1)\), define
\[
X=\log T=\sum_{j=1}^{p-1}\frac{(-1)^{j+1}(T-1)^j}{j},
\qquad
\exp H=\sum_{j=0}^{p-1}\frac{H^j}{j!}
\]
for \(H\) in the ideal \((T-1)\); these are finite polynomials because \((T-1)^p=0\). Identify \(e_i\) with \(T^i\) as **vectors**. This is not an identification of the quandle product with ordinary multiplication.

**Classification theorem.** The entire idempotent set of \(K[R_p]\) is the zero element and exactly the distinct elements
\[
F_{\mathbf a}=\exp\!\left(\sum_{m\in\mathscr D_p}a_m X^m\right),
\qquad \mathbf a=(a_m)_{m\in\mathscr D_p}\in K^{\kappa}.
\]
Its nonzero part is closed under the quandle-algebra product, with
\[
F_{\mathbf a}F_{\mathbf b}=F_{-\mathbf a+2\mathbf b}.
\]
Consequently it is a Takasaki (dihedral/Alexander) quandle on the additive group \(K^\kappa\). In particular, for \(K=\mathbb F_q\) with \(q\) a power of \(p\), there are exactly
\[
\boxed{1+q^{\kappa}\quad\text{idempotents}.}
\]
For the prime field \(K=\mathbb F_p\), the only nonzero idempotents are the basis idempotents exactly when \(\kappa=1\). For larger coefficient fields, the size of \(K\) matters even when \(\kappa=1\): over \(\mathbb F_9[R_3]\), there are ten idempotents, including six nontrivial idempotents supported on all three basis elements. The **first** odd prime with \(\kappa>1\) is \(p=17\): its quandle algebra has \(17^2+1=290\) idempotents, of which \(272\) are neither zero nor basis elements. For \(p=31\), \(\kappa=3\), giving \(31^3+1=29792\) idempotents.

## Assumptions and scope

The algebra is the vector space with bilinear product induced by \(R_p\), not its associative group algebra. All operations in the finite exponential and logarithm occur in the latter, used only as a coordinate device. The characteristic is **equal to** the odd prime indexing the quandle, rather than merely odd or prime to the quandle order. No algebraic closure, finite-field hypothesis, or restriction on the extension degree of \(K\) is required for the classification. The cardinality statement applies when \(K\) is finite.

## Proof

**Step 1: a group-algebra coordinate identity.** Let \(A=K[T]/(T^p-1)\) and identify the underlying vector spaces of \(K[R_p]\) and \(A\) by \(e_i\mapsto T^i\). If \(f,g\in A\) correspond to two quandle-algebra elements, their quandle product corresponds to
\[
 f\star g=f(T^{-1})g(T^2),
\]
where multiplication on the right is ordinary commutative multiplication in \(A\). Indeed, the formula sends \(T^i,T^j\) to \(T^{-i+2j}\), and bilinearity gives the claim. The augmentation \(\varepsilon(f)=f(1)\) satisfies \(\varepsilon(f\star g)=\varepsilon(f)\varepsilon(g)\).

**Step 2: exclude nonzero augmentation-zero idempotents.** Because \(\operatorname{char}K=p\), one has \(A=K[u]/(u^p)\) with \(u=T-1\). If \(f\ne0\) has augmentation zero, write \(f=u^r v\) with \(1\le r<p\) and \(v\) a unit. The substitutions \(T\mapsto T^{-1}\) and \(T\mapsto T^2\) send \(u\) respectively to \(-u/(1+u)\) and \(2u+u^2\). Since \(p\) is odd, both preserve the \(u\)-adic order \(r\). Therefore \(f\star f\) either has order \(2r>r\), or is zero when \(2r\ge p\), and cannot equal \(f\). An idempotent has augmentation \(0\) or \(1\); hence the only augmentation-zero idempotent is zero.

**Step 3: additive logarithmic coordinates.** In the nilpotent ideal \(J=(u)\), the finite series \(\exp:J\to1+J\) and \(\log:1+J\to J\) are mutually inverse group isomorphisms between addition and ordinary multiplication. To see this, reduce the usual formal identities \(\exp(A+B)=\exp(A)\exp(B)\) and \(\log(UV)=\log U+\log V\) modulo total degree \(p\); all denominators in degrees less than \(p\) are invertible in characteristic \(p\). The element \(X=\log T\) has leading term \(u\), so \(1,X,\ldots,X^{p-1}\) form a \(K\)-basis of \(A\), and every augmentation-one element is uniquely \(\exp H(X)\) with \(H\in XK[X]/(X^p)\).

Logarithm commutes with the two substitutions. Therefore \(\log(T^{-1})=-X\) and \(\log(T^2)=2X\). Using Step 1 and the group-homomorphism property,
\[
\exp H(X)\star\exp G(X)=\exp\bigl(H(-X)+G(2X)\bigr).
\]
In particular, idempotence is equivalent to the **linear** equation \(H(X)=H(-X)+H(2X)\).

**Step 4: solve every coefficient equation.** Write \(H=\sum_{m=1}^{p-1}a_mX^m\). Its coefficient equation is
\[
\bigl((-1)^m+2^m-1\bigr)a_m=0.
\]
For even \(m\), the coefficient is \(2^m\ne0\). For odd \(m\), it is \(2(2^{m-1}-1)\), so \(a_m\) is arbitrary exactly when \(d\mid(m-1)\). The latter exponent must also be even, giving \(m=1+jL\), with \(j\ge0\) and \(m\le p-1\). There are precisely \(\kappa=1+\lfloor(p-2)/L\rfloor\) such exponents. Uniqueness of logarithmic coordinates gives both the complete classification and the count.

**Step 5: identify the nonzero idempotent quandle.** All exponents in \(\mathscr D_p\) are odd and satisfy \(2^m=2\) in \(K\). Hence for solutions \(H_{\mathbf a}\), \(H_{\mathbf b}\) we have \(H_{\mathbf a}(-X)+H_{\mathbf b}(2X)=-H_{\mathbf a}(X)+2H_{\mathbf b}(X)\). The product formula of Step 3 yields \(F_{\mathbf a}F_{\mathbf b}=F_{-\mathbf a+2\mathbf b}\). The latter operation is the Takasaki quandle operation on the additive group \(K^\kappa\); multiplication by \(2\) is invertible since \(p\) is odd. The basis idempotent \(e_i=T^i=\exp(iX)\) is the parameter vector with first coordinate \(i\in\mathbb F_p\) and all other coordinates zero. Thus over \(\mathbb F_p\) the basis idempotents exhaust the nonzero idempotents precisely when \(\kappa=1\).

Finally, for odd primes \(p<17\), the values \(d=2,4,3,10,12\) at \(p=3,5,7,11,13\) imply \(\kappa=1\). At \(p=17\), \(d=8\) yields \(\mathscr D_p=\{1,9\}\), and at \(p=31\), \(d=5\) yields \(\{1,11,21\}\). This proves the stated first characteristic-dependent jump and examples.

## Verification

The standalone `check_idempotents.py` uses ordinary truncated-polynomial arithmetic to construct \(X\), the proposed exponential elements, and then tests their squares using **direct quandle basis multiplication**, not the logarithmic coefficient criterion alone. It exhaustively enumerates all \(3^3\) and \(5^5\) coefficient vectors for \(\mathbb F_3[R_3]\) and \(\mathbb F_5[R_5]\), and all \(9^3\) vectors for \(\mathbb F_9[R_3]\). It checks the explicit multiplication law on independently sampled parameters at primes \(3,5,7,11,13,17,19,23,31,41\), including the nontrivial \(p=17\) witness \(\exp(X^9)\). Each reported arithmetic test passed. A concrete length-three example in \(\mathbb F_9[R_3]\) uses \(\alpha^2=-1\) in \(\mathbb F_9=\mathbb F_3(\alpha)\): \[h=2e_0+(1+\alpha)e_1+(1+2\alpha)e_2.\] Direct multiplication gives \(h^2=h\), and all three coefficients are nonzero. In this quandle, for a coefficient triple \((a,b,c)\), the square has coefficients \((a^2+2bc,b^2+2ac,c^2+2ab)\); substitution verifies the witness without relying on logarithmic identities. This explicitly violates the universal length-three assertion of Sangare and Ta (2026, Theorem 3.6) *under its printed characteristic hypotheses*. The proof above, not finite enumeration, establishes the universal statement.

## Relationship to prior work

Bardakov, Passi, and Singh (2020, arXiv:2001.06843), Sections 4–5, calculate idempotents and maximal quandles for selected small quandles, especially integral \(R_3\), but do not present the modular arbitrary-prime classification. Elhamdadi, Nunez, and Singh (2022, arXiv:2207.09257), Sections 3 and 6, investigate finite quandle-ring idempotents and give small-order tables; these motivate an exact uniform answer in modular characteristic. The known characteristic-three line for \(R_3\) is precisely the \(p=3\), \(\kappa=1\) specialization, **not** a novelty claim here.

Sangare and Ta (2026, arXiv:2608.01550), Section 3, give a general length-two/three obstruction in Theorem 3.6 under the assumption of an integral domain of characteristic different from two. The explicit \(\mathbb F_9[R_3]\) length-three idempotent above is a counterexample to that assertion as written: \(R_3\) is commutative and \(\mathbb F_9\) is an integral domain of characteristic three. Their proof cites Bardakov–Passi–Singh Proposition 4.3 in the \(R_3\) case, although that proposition concerns integral coefficients, not arbitrary characteristic-three fields. The accessible paper does not establish the present modular arbitrary-prime classification. This discrepancy is an independent concrete boundary of earlier arguments, not a claim about the authors’ intentions. The related 2026 studies by Elhamdadi, Ta, and Virgin (arXiv:2609.03799), and Zhang (arXiv:2610.08204), chiefly advertise Fourier and integral-coefficient results. Only abstracts of those two later papers could be inspected; they remain potential overlap risks, **not** certified exclusions. The theorem's particular claims are the full finite-field count, the arithmetic resonance exponents, and the Takasaki quandle structure in defining characteristic.

## Limitations

The statement is restricted to **prime** odd quandle order and **matching** coefficient characteristic. It does not classify idempotents for composite dihedral quandle orders or nonmatching characteristics, nor does it assert integral-coefficient results, knot-invariant consequences, or uniqueness in the literature. Full text of two relevant 2026 preprints could not be inspected; novelty therefore remains subject to those comparisons and further independent scholarly review. The computational checks are finite corroboration and are not independent mathematical certification.

## References

1. V. G. Bardakov, I. B. S. Passi, and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (first public version January 19, 2020), Osaka J. Math. 59 (2022), 611–637.
2. M. Elhamdadi, B. Nunez, and M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257 (first public version July 19, 2022), J. Pure Appl. Algebra 227 (2023), 107400.
3. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (first public version August 3, 2026).
4. M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (first public version September 3, 2026).
5. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first public version October 6, 2026).

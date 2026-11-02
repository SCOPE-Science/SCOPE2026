# Modular prime-dihedral idempotents form an explicit vector-space quandle

## Finding
Fix an odd prime \(p\ge5\), a field \(K\) of characteristic \(p\), and the dihedral quandle \(R_p=\mathbb Z/p\mathbb Z\) with \(i\star j=2j-i\). Its quandle algebra \(A=K[R_p]\) has basis \(e_i\), with \(e_i\star e_j=e_{2j-i}\). An idempotent means an element \(a\) with \(a\star a=a\), including zero.

Put \(h=\operatorname{ord}_p(2)\) and \(d=(p-1)/\operatorname{lcm}(2,h)\). The nonzero idempotents are **exactly** a connected, Latin subquandle isomorphic to the core quandle of the additive vector space \(K^d\), whose operation is
\[
 u\star v=-u+2v.
\]
More precisely, in the associative group algebra \(B=K[t]/(t^p-1)\), define \(\iota f=f(t^{-1})\), \(\sigma f=f(t^2)\), \(J=(t-1)B\), and
\[
 W=\{u\in J:\iota u=-u,\quad \sigma u=2u\}.
\]
Under the basis identification \(e_i\leftrightarrow t^i\), every nonzero idempotent is uniquely \(\operatorname{Exp}(u)\) for \(u\in W\), where
\[
 \operatorname{Exp}(u)=\sum_{j=0}^{p-1}\frac{u^j}{j!}.
\]
Thus the complete idempotent set is \(\{0\}\sqcup\operatorname{Exp}(W)\), with zero absorbing and
\[
 \operatorname{Exp}(u)\star\operatorname{Exp}(v)
 =\operatorname{Exp}(-u+2v).
\]
The \(K\)-dimension of \(W\) is exactly \(d\). Over \(K=\mathbb F_q\), where \(q=p^e\), the number of idempotents, including zero, is \(q^d+1\); the number outside the original basis and zero is \(q^d-p\). Such genuinely new nonzero idempotents exist if and only if \(ed>1\). In particular, \(\mathbb F_{17}[R_{17}]\) has \(290\) idempotents, of which \(272\) are nonzero and not basis elements, whereas \(\mathbb F_{31}[R_{31}]\) has \(31^3+1=29792\) idempotents.

## Assumptions and scope
The modulus is an **odd prime** \(p\ge5\), the coefficient field has characteristic exactly \(p\), and products of quandle-algebra elements are interpreted with the displayed bilinear multiplication (which is not associative). No algebraic closure, perfection, or finiteness hypothesis on \(K\) is used for the classification. Cardinality formulas require \(K=\mathbb F_q\). The truncated exponential uses the ordinary associative multiplication of the auxiliary group algebra \(B\), **not** iterated nonassociative quandle products.

## Proof
**1. Associative encoding.** For monomials, the bilinear quandle multiplication becomes
\[
 t^i\star t^j=t^{2j-i} =\iota(t^i)\,\sigma(t^j).
\]
Consequently, for all \(f,g\in B\),
\[
 f\star g=\iota(f)\,\sigma(g),
\]
where the product on the right is taken in the ordinary commutative associative algebra \(B\). Because \(t^p-1=(t-1)^p\) in characteristic \(p\), the ideal \(J=(t-1)B\) satisfies \(J^p=0\), and \(B/J=K\). Both \(\iota\) and \(\sigma\) are commuting algebra automorphisms of \(B\) preserving \(J\), because \(-1\) and \(2\) are invertible modulo \(p\).

**2. Augmentation obstruction.** The quotient map \(\varepsilon:B\to B/J=K\) takes \(f\star f=f\) to \(\varepsilon(f)^2=\varepsilon(f)\), so the augmentation is \(0\) or \(1\). If it is zero, then \(f\in J\) and the idempotency equation gives \(f\in J^2\). Inductively \(f\in J^{2^r}\) for every positive integer \(r\); since \(J^p=0\), necessarily \(f=0\). Hence every nonzero idempotent lies in \(1+J\).

**3. Logarithmic linearization.** Since \(J^p=0\) and all integers \(1,\ldots,p-1\) are invertible in \(K\), the truncated polynomials
\[
 \operatorname{Exp}(u)=\sum_{j=0}^{p-1}\frac{u^j}{j!},\qquad
 \operatorname{Log}(1+v)=\sum_{j=1}^{p-1}\frac{(-1)^{j+1}v^j}{j}
\]
are inverse bijections between \((J,+)\) and \((1+J,\cdot)\). They are group homomorphisms: the formal rational identities \(\exp(U+V)=\exp(U)\exp(V)\) and \(\log((1+U)(1+V))=\log(1+U)+\log(1+V)\) are valid through total degree \(p-1\), where their denominators are prime to \(p\); all higher terms vanish upon substitution from \(J\). They commute with algebra automorphisms of \(B\).

Writing \(f=\operatorname{Exp}(u)\), the idempotency equation is therefore equivalent to
\[
 u=\iota(u)+\sigma(u).
\]
As \(p\) is odd, decompose \(u=u_++u_-\) into \(\iota\)-eigenspaces of eigenvalues \(+1\) and \(-1\). The map \(\sigma\) commutes with \(\iota\), so the two component equations are \(\sigma(u_+)=0\) and \(\sigma(u_-)=2u_-\). Since \(\sigma\) is invertible, \(u_+=0\). Thus the solutions are precisely \(W\), proving the complete idempotent classification.

**4. Dimension.** Represent \(u=\sum_{i=0}^{p-1}a_i t^i\). The condition \(\iota u=-u\) implies \(a_0=0\), and the doubling permutation \(i\mapsto2i\) has exactly \((p-1)/h\) cycles of length \(h\) on the nonzero residues. On each such cycle, the \(\sigma\)-eigenspace of eigenvalue \(2\) is one-dimensional: consecutive coefficients must differ by multiplication by \(2^{-1}\), which is consistent because \(2^h=1\pmod p\). If \(h\) is even, \(2^{h/2}=-1\pmod p\), hence \(\iota=\sigma^{h/2}\) and the \(\sigma\)-eigenvalue-\(2\) vectors already satisfy \(\iota u=-u\). Therefore \(\dim_K W=(p-1)/h\). If \(h\) is odd, inversion pairs distinct doubling cycles, and imposing \(\iota=-1\) leaves one eigenvector for each pair; hence \(\dim_K W=(p-1)/(2h)\). Both cases give \((p-1)/\operatorname{lcm}(2,h)\).

**5. Multiplication and the basis subquandle.** For \(u,v\in W\),
\[
 \operatorname{Exp}(u)\star\operatorname{Exp}(v)
 =\operatorname{Exp}(\iota u+\sigma v)
 =\operatorname{Exp}(-u+2v).
\]
The operation \((u,v)\mapsto-u+2v\) is the core-quandle operation of the additive abelian group \((W,+)\). It is connected because \(2\) is invertible on \(W\), and Latin because both \(-1\) and \(2\) are invertible. The original basis elements \(t^i\) lie in \(\operatorname{Exp}(W)\): \(\operatorname{Log}(t^i)=i\operatorname{Log}(t)\), and \(\operatorname{Log}(t)\neq0\). Their logarithms are exactly the \(p\) points of one \(\mathbb F_p\)-line. Consequently, when \(K=\mathbb F_q\), there are \(q^d\) nonzero idempotents, exactly \(p\) original basis idempotents, and \(q^d-p\) others. This establishes every assertion.

## Verification
The accompanying `verify.py` independently evaluates the **defining coefficient equation** \(a\star a=a\), rather than assuming the exponential classification, on all \(3^3=27\), \(5^5=3125\), and \(7^7=823543\) elements of the corresponding prime-field quandle algebras. It finds respectively \(4\), \(6\), and \(8\) idempotents including zero; each set agrees exactly with the exponential construction, and all nonzero idempotents are closed under the quandle multiplication with bijective right translations. A separate direct calculation of the \(729\) coefficient vectors in \(\mathbb F_9[R_3]\) finds \(10\) idempotents, agreeing with the previously recorded small-modulus case. Further finite checks compute doubling orbits for nine other primes, including \(17\), \(31\), and \(1093\); these numerical checks do not constitute a proof for arbitrary primes or infinite fields. Run with `python3 verify.py` (Python 3 and NumPy required). The unrestricted proof is above.

## Relationship to prior work
Bardakov, Passi and Singh initiated explicit quandle-ring idempotent calculations and treated the **integral** ring of \(R_3\) (arXiv:2001.06843, Proposition 4.3); Narayanan and Panja treated the **integral** ring of \(R_5\) (arXiv:2206.10386, Theorem 3.1). Neither integral classification controls the defining-characteristic field case. Elhamdadi, Nunez, Singh and Swain developed the use of idempotent subquandles in link-coloring enhancements and studied integral and characteristic-two examples (arXiv:2204.11288 and arXiv:2207.09257). Their quandle-covering classification assumes a nontrivial covering and does not supply the present prime-modulus modular idempotent set.

For \(p=3\), a characteristic-three affine line of idempotents has already been recorded and is **excluded from the new claim**; our small-field tests use it solely as a check. The signed-doubling eigenspace \(W\) is also natural in modular derivation problems for the same family, so its isolated dimension count is **not** presented as the primary novelty. The contribution is the *complete exponential classification of all idempotents*, the fact that all nonzero ones form a connected Latin core quandle, and the exact arithmetic criterion for additional idempotents over finite fields. Sangare and Ta (arXiv:2608.01550) discuss idempotents of commutative quandles and automorphisms of dihedral quandle algebras; their commutative-quandle idempotent hypotheses do not apply to \(R_p\) for \(p\ge5\), which is noncommutative. Two additional closely related papers were compared directly: Bardakov and Elhamdadi (arXiv:2601.07057) investigate the augmentation ideals of **integral** dihedral quandle rings, while Kaur and Singh (arXiv:2609.09183) prove an integral-ring idempotent theorem and construct integral affine-quandle families. Neither gives a defining-characteristic finite-field idempotent count or core law. We have not established absolute publication priority.

## Limitations
The prime-modulus and matching-characteristic hypotheses are essential to the logarithmic proof. In modulus \(p^a\) with \(a>1\), \((t-1)^p\) need not vanish and the truncated logarithm argument does not apply unchanged; no such extension is asserted. Fields of characteristic different from \(p\), characteristic two, and composite quandle moduli are excluded. No inference about the entire set of idempotents of unrelated quandle algebras is made. Exhaustive checks are confined to specified finite cases and do not establish the general theorem. An equivalent construction hidden in general modular-quandle, Alexander-quandle or truncated-group-algebra literature remains possible.

## References
1. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843, first posted 2020-01-19; Osaka J. Math. **59** (2022), 611–637, Proposition 4.3.
2. P. Narayanan and S. Panja, *Idempotents in integral ring of dihedral quandle*, arXiv:2206.10386, first posted 2022-06-17, Theorem 3.1.
3. M. Elhamdadi, B. Nunez, M. Singh and D. Swain, *Idempotents, free products and quandle coverings*, arXiv:2204.11288, first posted 2022-04-24, Theorem 4.5.
4. M. Elhamdadi, B. Nunez and M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257, first posted 2022-07-19, Theorem 5.1 and Section 6.
5. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, first posted 2026-08-03, Sections 3–4.
6. V. Bardakov and M. Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057, first posted 2026-01-11, Section 4.
7. D. Kaur and P. Singh, *A note on idempotents in quandle rings*, arXiv:2609.09183, first posted 2026-08-29, Theorem 2.5 and Section 4.

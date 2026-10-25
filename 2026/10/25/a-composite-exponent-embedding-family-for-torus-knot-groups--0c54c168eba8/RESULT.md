# A composite-exponent embedding family for torus knot groups

## Finding

For coprime integers \(p,q>1\) and an integer \(s>1\) satisfying \(\gcd(s,pq)=1\), define
\[
G_{p,q}=\langle a,b\mid a^p=b^q\rangle,\qquad
G_{pq,s}=\langle x,y\mid x^{pq}=y^s\rangle.
\]
There is an injective homomorphism
\[
\phi:G_{p,q}\longrightarrow G_{pq,s},\qquad
\phi(a)=x^q,\quad \phi(b)=yx^p y^{-1}.
\]
Moreover, these two groups are not isomorphic: their quotients by their centers are \(C_p*C_q\) and \(C_{pq}*C_s\), and the latter contains an element of order \(pq\) while the former does not.

## Assumptions and scope

The parameters are integers with \(p,q,s>1\), \(\gcd(p,q)=1\), and \(\gcd(s,pq)=1\). These are precisely the coprimality assumptions needed for both presentations to be torus-knot groups of the stated types. The result gives a sufficient family of embeddings; it is not a classification of all embeddings between torus-knot groups.

## Proof

Write \(h=a^p=b^q\) in the source and \(k=x^{pq}=y^s\) in the target. In each group this common power is central, because it commutes with both displayed generators. The assignments are compatible with the defining relation:
\[
\phi(a)^p=x^{pq}=k=yx^{pq}y^{-1}=\phi(b)^q.
\]
Thus they define a homomorphism.

Quotienting by the central powers gives
\[
G_{p,q}/\langle h\rangle\cong C_p*C_q,
\qquad
G_{pq,s}/\langle k\rangle\cong C_{pq}*C_s.
\]
The induced quotient map sends the generator of \(C_p\) to \(\bar x^q\), and the generator of \(C_q\) to \(\bar y\bar x^p\bar y^{-1}\). More precisely, \(\bar x^q\) has order \(p\) and \(\bar x^p\) has order \(q\). Every nonempty reduced word in \(C_p*C_q\) alternates nontrivial powers of these two generators. After substitution, its syllables alternate between nonidentity powers in \(C_{pq}\) and nonidentity powers of \(\bar y\) in \(C_s\); hence it remains reduced in \(C_{pq}*C_s\). The quotient map is therefore injective.

If \(g\in\ker\phi\), its image in \(C_p*C_q\) is trivial by injectivity of the quotient map, so \(g\in\langle h\rangle\), since the kernel of the quotient is the normal closure of \(h\) and \(h\) is central. Finally, the homomorphism \(G_{pq,s}\to\mathbb Z\) given by \(x\mapsto s\), \(y\mapsto pq\) is well-defined and sends \(k\) to \(pqs\ne0\). Thus \(k\) has infinite order. Since \(\phi(h)=k\), no nontrivial power of \(h\) lies in \(\ker\phi\). Therefore \(\ker\phi=1\).

For the nonisomorphism claim, the centers are exactly \(\langle h\rangle\) and \(\langle k\rangle\): each is central, and the corresponding quotient free product has trivial center. An isomorphism would induce an isomorphism of the quotients. But every finite-order element of \(C_p*C_q\) is conjugate into one factor, so none has order \(pq\), whereas \(C_{pq}*C_s\) contains an element of that order. The quotient groups, and hence the original groups, are not isomorphic.

## Verification

The relation check is exact. Injectivity is proved by the reduced-word normal form in the free product quotient and by the infinite order of the target central element. No finite computation or experimental enumeration is used. For the concrete instance \(p=2,q=3,s=5\), this gives an explicit embedding \(G_{2,3}\hookrightarrow G_{6,5}\) between nonisomorphic groups.

## Relationship to prior work

Myers's paper on wild arcs states a torus-knot-group embedding lemma for the restricted case where all four parameters are prime; the lemma uses the quotient by the center, which is a free product of finite cyclic groups. The construction above addresses a different parameter regime: both source exponents are placed in distinct conjugate subgroups of the same composite cyclic factor \(C_{pq}\). It supplies an explicit counterexample to simply dropping the prime-parameter restriction, without asserting a full subgroup classification.

## Limitations

This result is a sufficient embedding family only. It does not decide when \(G_{r,s}\) embeds in \(G_{p,q}\) for arbitrary coprime pairs, classify all embeddings, or identify these groups with one another. The novelty assessment is limited to the explicit family and its comparison with the prime-parameter lemma; a complete survey of all subgroup-classification literature was not established.

## References

R. Myers, “Uncountably many arcs in \(S^3\) whose complements have non-isomorphic, indecomposable fundamental groups,” arXiv:math/9901106 (first public version dated 1999-01-25); published in *Journal of Knot Theory and Its Ramifications* 9(4) (2000), 505–521. Section 4, Lemma 4.1.

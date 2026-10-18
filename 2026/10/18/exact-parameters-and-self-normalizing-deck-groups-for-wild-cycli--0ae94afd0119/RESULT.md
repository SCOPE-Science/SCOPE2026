# Exact parameters and self-normalizing deck groups for wild cyclic genus-six covers

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For each \(\lambda\in k\), let \(X_\lambda\) be the smooth projective normalization of the compositum, over \(k(z)\), of the Kummer extension \(x^3=z\) and the length-two Artin–Schreier–Witt extension
\[
\wp_2(y_0,y_1)=(z^{-1},\lambda z^{-1}).
\]
Let \(G_\lambda=\operatorname{Gal}(k(X_\lambda)/k(z))\cong C_{12}\) be its distinguished cyclic subgroup of automorphisms. Then, for all \(\lambda,\mu\in k\), there is an isomorphism of **unlabelled-subgroup pairs** \((X_\lambda,G_\lambda)\cong(X_\mu,G_\mu)\) if and only if \(\mu-\lambda\in\mathbb F_2\). Equivalently, \(\lambda^2+\lambda\) is a complete invariant of these pairs and takes every value of \(k\). Furthermore, for every \(\lambda\),
\[
N_{\operatorname{Aut}_k(X_\lambda)}(G_\lambda)=G_\lambda.
\]
Here an isomorphism of pairs conjugates the cyclic subgroups but does not fix an individual generator of either subgroup.

## Assumptions and scope
Throughout, \(k\) is algebraically closed of characteristic \(2\); \(\wp_2=F-1\) acts on length-two \(2\)-typical Witt vectors and \(t=z^{-1}\). Theorem 5.8 of Kazemifard–Tafazolian establishes that these smooth curves have genus \(6\), their displayed extension is connected and Galois with group \(C_{12}\), and **every** genus-six pair with a cyclic subgroup of order \(12\) has one of these normal forms. The branch locus of the quotient map \(X_\lambda\to\mathbb P^1_z\) consists of a full, wildly ramified point of inertia \(12\) at \(z=0\) and a tamely ramified point of inertia \(3\) at \(z=\infty\). These source results are premises, not new assertions here.

## Proof
The two branch points have different inertia orders, so an isomorphism of pairs must send each to the point of the same type. Its descended projective automorphism has the form \(z\mapsto az\) with \(a\in k^\times\). The unique degree-two quotient of the cyclic degree-twelve extension is the Artin–Schreier cover corresponding to the first Witt component, namely the class of \(t=1/z\) in \(k(z)/\{h^2+h:h\in k(z)\}\). A base scaling carries this class to that of \(a^{-1}t\). Equality implies
\[
(a^{-1}+1)t=h^2+h
\]
for some \(h\in k(z)\). If \(a\ne1\), the left side has a pole of odd order \(1\) at \(z=0\), whereas every nonzero rational-function Artin–Schreier coboundary with a pole has even pole order at that point. Therefore \(a=1\).

Consequently, pair isomorphism is equivalent to isomorphism over \(k(z)\) of the associated cyclic extensions. Their unique cyclic cubic subextensions are the same \(x^3=z\); it remains to compare the cyclic quartic subextensions. By Artin–Schreier–Witt theory, cyclic quartic extensions over \(k(z)\), with no distinguished generator of the Galois group, correspond to order-four Witt cohomology classes up to the unit action of \((\mathbb Z/4\mathbb Z)^\times=\{1,-1\}\). Let \(a_\lambda=(t,\lambda t)\). The Witt addition and negation laws in characteristic \(2\) are
\[
(u_0,u_1)+(v_0,v_1)=(u_0+v_0,u_1+v_1+u_0v_0),
\qquad -(u_0,u_1)=(u_0,u_1+u_0^2).
\]
In the positive-unit case, \([a_\mu]=[a_\lambda]\) is equivalent to \((0,(\mu+\lambda)t)\in\wp_2 W_2(k(z))\). In the negative-unit case, \([a_\mu]=-[a_\lambda]\) is equivalent to \((0,(\mu+\lambda)t+t^2)\in\wp_2 W_2(k(z))\).

If \(\wp_2(r,s)\) has zero first coordinate, then \(r^2+r=0\), so \(r\in\{0,1\}\); in either case its second coordinate is \(s^2+s\). Thus the positive-unit condition is precisely
\[
(\mu+\lambda)t=s^2+s.
\]
The odd-pole-order argument forces \(\mu+\lambda=0\). The negative-unit condition is
\[
t^2+(\mu+\lambda)t=s^2+s.
\]
Any such \(s\) can have poles only at \(z=0\); there it has pole order at most one, so \(s=ct+d\) for constants \(c,d\in k\). Comparing the \(t^2\) coefficient gives \(c^2=1\), hence \(c=1\); comparing the \(t\) coefficient then gives \(\mu+\lambda=1\). Conversely, \(s=t\) realizes this coboundary, so both allowed parameter relations genuinely yield isomorphic covers. We conclude that the two pairs are isomorphic exactly when \(\mu=\lambda\) or \(\mu=\lambda+1\).

Since \(k\) is algebraically closed, the polynomial map \(\lambda\mapsto\lambda^2+\lambda\) is surjective and each fibre has exactly the two values \(\{\lambda,\lambda+1\}\). This proves the complete-invariant assertion.

Finally, take an automorphism \(\phi\in\operatorname{Aut}_k(X_\lambda)\) normalizing \(G_\lambda\). It descends to an automorphism of \(\mathbb P^1_z\) preserving the two distinctly ramified branch points. The preceding quadratic-quotient argument forces this descended automorphism to be the identity. Hence \(\phi\) lies in the Galois group \(\operatorname{Aut}_{k(z)}(k(X_\lambda))=G_\lambda\). The reverse inclusion follows because \(G_\lambda\) normalizes itself, completing the proof.

## Verification
The accompanying dependency-free `CHECK.py` symbolically computes the Witt addition, inverse, and coboundary identity
\[
-a_\lambda+\wp_2(0,t)=a_{\lambda+1}
\]
over \(\mathbb F_2[\lambda,t]\), and exhaustively verifies the two-element fibres of \(\lambda\mapsto\lambda^2+\lambda\) over \(\mathbb F_{16}\). Run `python3 CHECK.py` beside this file. The checks corroborate algebraic identities only. The pole-order arguments, classification of quartic extensions, and normalizer statement have the infinite-field proofs above; finite testing is not a substitute for them.

## Relationship to prior work
Kazemifard–Tafazolian, Theorem 5.8, provides the entire normal-form family and expressly does not claim uniqueness of its parameter. Their Theorem 6.1 classifies the numerical boundary cases. The present result determines the exact redundancy of that one-parameter genus-six normal form as pairs and the full normalizer of each distinguished cyclic group; it does not claim the normal form, genus, or ramification signature as new. Earlier results on larger-order cyclic groups in characteristic two exclude the order-twelve boundary with a quartic wild factor, and classifications of genus-two curves do not themselves settle the genus-six pair classification. The parameter equivalence is a comparison of Witt cohomology classes, not just a comparison of displayed equations.

## Limitations
The classification is of curves **together with a designated but unlabelled cyclic order-twelve subgroup**. It does not assert that underlying unmarked curves are nonisomorphic whenever their invariants differ, nor does it determine their full automorphism groups. A self-normalizing subgroup may still be proper in the full automorphism group. The parameter invariant is geometric over an algebraically closed field and is not a classification of descent forms over arbitrary ground fields. Previously unindexed treatments of the same marked moduli problem may exist.

## References
1. A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702v1, posted 2026-10-03; especially §§5.3–5.4, Theorems 5.8 and 6.1. https://arxiv.org/html/2610.04702v1
2. Standard Artin–Schreier–Witt classification of cyclic degree-four extensions; for the explicit group law and the normal form used here, see reference 1, §5.3.
3. S. Timpanella, *Large cyclic automorphism groups and cyclic subgroups of index two in characteristic two*, arXiv:2609.34709; relevant higher-order range, not the boundary case. https://arxiv.org/abs/2609.34709

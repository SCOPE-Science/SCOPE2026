# Exact repair of a four-dimensional Hom–Jacobi–Jordan twisting example

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2.
\]
Consider the commutative algebra \(B\) with basis
\[
\{e_1,e_2,e_3,e_4\}
\]
and sole nonzero products
\[
e_1e_1=e_2,
\qquad
e_1e_4=e_4e_1=e_4.
\]
This is the multiplication printed in Example 3.4(ii) of Attan's Hom–Jacobi–Jordan paper.

The printed claim that \(B\) is a Jacobi–Jordan algebra is false in characteristic different from \(2\). Its ordinary Jacobiator satisfies
\[
\boxed{J(e_1,e_1,e_4)=2e_4\ne0.}
\]

The four-parameter linear map displayed in the same example is also never a self-morphism of this printed multiplication. The source has
\[
\alpha(e_1)=-e_1-e_3,
\]
so
\[
\alpha(e_1)^2=e_2,
\]
whereas it prints
\[
\alpha(e_2)=a_{12}e_1+e_2+2e_4.
\]
Thus
\[
\boxed{\alpha(e_1)^2-\alpha(e_2)=-a_{12}e_1-2e_4\ne0}
\]
for every parameter choice.

There is, however, a complete positive repair. Every algebra endomorphism \(\alpha:B\to B\) is exactly one of the following two types.

**Type I.**
\[
\begin{aligned}
\alpha(e_1)&=u e_2+v e_3+w e_4,\\
\alpha(e_2)&=0,\\
\alpha(e_3)&=p e_2+s e_3+r e_4,\\
\alpha(e_4)&=0,
\end{aligned}
\]
with
\[
u,v,w,p,s,r\in K.
\]

**Type II.** For
\[
\lambda\in K^\times,
\]
\[
\begin{aligned}
\alpha(e_1)&=\lambda e_1+u e_2+v e_3,\\
\alpha(e_2)&=\lambda^2e_2,\\
\alpha(e_3)&=p e_2+s e_3,\\
\alpha(e_4)&=t e_4,
\end{aligned}
\]
with
\[
(1-\lambda)t=0.
\]

For any such endomorphism define
\[
x\ast_\alpha y=\alpha(xy).
\]
Then \((B,\ast_\alpha,\alpha)\) is multiplicative automatically. Its Hom-Jacobian is
\[
J_\alpha(x,y,z)=\alpha^2(J(x,y,z)).
\]
The ordinary Jacobiator of \(B\) spans \(Ke_4\). Therefore
\[
\boxed{(B,\ast_\alpha,\alpha)\text{ is Hom–Jacobi–Jordan}\iff \alpha^2(e_4)=0.}
\]

Type I always satisfies this criterion. In Type II,
\[
\alpha^2(e_4)=t^2e_4,
\]
so the criterion is simply
\[
\boxed{t=0.}
\]
Consequently every valid Type II twist has
\[
\alpha(e_4)=0.
\]
In particular,
\[
\boxed{\text{no algebra automorphism of }B\text{ produces a valid Hom–Jacobi–Jordan twist}.}
\]

Over every odd finite field \(\mathbf F_q\), the valid-twist set has
\[
\boxed{q^6+(q-1)q^4=q^6+q^5-q^4}
\]
points. The full algebra-endomorphism set has
\[
\boxed{q^4(q^2+2q-2)}
\]
points, so exactly
\[
\boxed{q^4(q-1)}
\]
endomorphisms fail the Hom-Jacobi condition. The automorphism group has
\[
\boxed{q^3(q-1)^2}
\]
elements, all lying in the failing stratum.

For every extension field \(\mathbf F_{q^m}\), the valid-twist count is
\[
q^{6m}+q^{5m}-q^{4m}.
\]
Hence the Hasse–Weil zeta function of the reduced valid-twist locus is
\[
\boxed{
Z(T)=\frac{1-q^4T}{(1-q^6T)(1-q^5T)}.
}
\]

## Assumptions and scope

Attan's preprint first appeared on 30 May 2021 and lists \(16W10\) first among its Mathematics Subject Classification codes. The 2025 journal version available through public indexing reproduces the same Example 3.4(ii), including the same multiplication and the same displayed self-morphism.

The theorem above concerns the example exactly as printed. It does not assert what multiplication or map the author may originally have intended.

The source works in characteristic \(0\). The correction and salvage classification are valid over every field of characteristic different from \(2\). Characteristic \(2\) is excluded because both the ordinary Jacobi obstruction and the endomorphism equations change.

## Proof

For vectors
\[
x=x_1e_1+x_2e_2+x_3e_3+x_4e_4,
\qquad
y=y_1e_1+y_2e_2+y_3e_3+y_4e_4,
\]
the printed multiplication is
\[
xy=x_1y_1e_2+(x_1y_4+x_4y_1)e_4.
\]
A direct cyclic calculation gives
\[
J(e_1,e_1,e_4)=2e_4,
\]
so the printed algebra is not Jacobi–Jordan.

Now let
\[
\alpha(e_1)=\lambda e_1+u e_2+v e_3+w e_4.
\]
Because \(e_2=e_1^2\), multiplicativity forces
\[
\alpha(e_2)=\alpha(e_1)^2=\lambda^2e_2+2\lambda w e_4.
\]
The relation \(e_1e_2=0\) then gives
\[
2\lambda^2w=0.
\]
Thus either \(\lambda=0\), or \(w=0\).

Write a general image of \(e_3\). The relation \(e_3^2=0\) forces its \(e_1\)-coordinate to vanish. If \(\lambda\ne0\), the relation \(e_1e_3=0\) then also kills its \(e_4\)-coordinate. This gives precisely the two displayed forms for \(\alpha(e_3)\).

Finally, since \(e_4=e_1e_4\), the equation
\[
\alpha(e_4)=\alpha(e_1)\alpha(e_4)
\]
forces \(\alpha(e_4)=0\) when \(\lambda=0\). When \(\lambda\ne0\), it forces
\[
\alpha(e_4)=t e_4,
\qquad
(1-\lambda)t=0.
\]
All remaining zero products are then automatically preserved. This proves the complete endomorphism classification.

For an algebra endomorphism \(\alpha\), the twisted product is
\[
\mu_\alpha=\alpha\circ\mu.
\]
Using multiplicativity twice,
\[
\mu_\alpha(\mu_\alpha(x,y),\alpha z)
=
\alpha^2(\mu(\mu(x,y),z)).
\]
Cyclic summation gives
\[
J_\alpha(x,y,z)=\alpha^2(J(x,y,z)).
\]
The explicit multiplication shows that every ordinary Jacobiator lies in \(Ke_4\), and \(J(e_1,e_1,e_4)=2e_4\) spans that line. Hence the Hom-Jacobi identity is equivalent to
\[
\alpha^2(e_4)=0.
\]
The Type I branch has \(\alpha(e_4)=0\). In Type II, \(\alpha(e_4)=t e_4\), so the criterion is \(t=0\).

An endomorphism is invertible only in the \(\lambda=1\) branch. There its matrix has determinant equal to the product of the \(e_3\)-diagonal coefficient and \(t\). Thus every automorphism has \(t\ne0\), and therefore no automorphism yields a valid Hom–Jacobi–Jordan twist.

For finite fields, Type I contributes \(q^6\) valid twists. Valid Type II contributes \((q-1)q^4\). The endomorphism count additionally includes the \(\lambda=1\), arbitrary-\(t\) branch, yielding \(q^4(q^2+2q-2)\). The automorphism formula follows from the two nonzero determinant factors. Replacing \(q\) by \(q^m\) gives the zeta function.

## Verification

The bundled checker `artifacts/verify.py` reconstructs the printed multiplication and verifies
\[
J(e_1,e_1,e_4)=2e_4.
\]
It substitutes the exact four-parameter map printed in Example 3.4(ii) and verifies
\[
\alpha(e_1)^2-\alpha(e_2)=-a_{12}e_1-2e_4.
\]

It symbolically checks both endomorphism branches, the twisted Hom-Jacobi identity on all ordered basis triples, and the exact obstruction \(2t^2e_4\) on the \(\lambda=1\) branch.

Over \(\mathbf F_3\), it exhaustively reconstructs every algebra endomorphism from its basis images and obtains
\[
1053
\]
endomorphisms, of which
\[
891
\]
are valid twists and
\[
108
\]
are automorphisms. All automorphisms fail the Hom-Jacobi identity. Closed-form counts are also cross-checked for \(q=5,7,11\).

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is the symbolic proof above.

## Relationship to prior work

The primary preprint and its 2025 journal version both print Example 3.4(ii) with the same multiplication and self-morphism. The error is therefore not merely a discrepancy between an early and later displayed version.

Burde and Fialowski prove that every Jacobi–Jordan algebra of dimension at most four over an algebraically closed field of characteristic different from \(2\) and \(3\) is associative with vanishing third power. Their six-class four-dimensional list does not contain the printed algebra. This independently agrees with the explicit Jacobiator obstruction above.

The source's twisting proposition is a valid general construction when its hypotheses hold. The failure is local to the printed example: its claimed base Jacobi–Jordan algebra and its claimed self-morphism do not satisfy those hypotheses. The positive part of the present result does not use that proposition; it solves all algebra endomorphisms of the printed multiplication and directly checks which twisted products satisfy the Hom-Jacobi identity.

Targeted semantic-database and web searches for the exact printed multiplication, the self-morphism failure, the endomorphism-twist classification, and the finite-field polynomial did not locate a prior correction or complete salvage theorem.

## Limitations

The theorem corrects the example exactly as printed; it does not reconstruct the author's intended example.

The direct 2025 journal PDF is protected by an anti-bot interstitial in ordinary browsing, although public search indexing exposes the exact Example 3.4 text and shows it unchanged. A non-indexed erratum could therefore remain undiscovered.

Characteristic \(2\) is outside scope.

Failed searches do not prove absolute historical novelty.

## References

1. S. Attan, “Representations and O-operators of Hom-(pre)-Jacobi-Jordan algebras,” arXiv:2105.14650v1, first public 30 May 2021, DOI `10.48550/arXiv.2105.14650`; later published in the *Moroccan Journal of Algebra*.
2. D. Burde and A. Fialowski, “Jacobi-Jordan algebras,” *Linear Algebra and its Applications* 459 (2014), 586–594, arXiv:1404.5435.

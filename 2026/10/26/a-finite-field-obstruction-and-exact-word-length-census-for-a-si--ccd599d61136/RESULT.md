# A finite-field obstruction and exact word-length census for a simple spin factor over \(\mathbb F_3\)

## Finding

Let \(S=\mathbb F_3\mathbf1\oplus V\), where \(V=\mathbb F_3^3\), with quadratic form \(q(x,y,z)=x^2+y^2+z^2\), bilinear form \(B(u,v)=u\cdot v\), and product
\[
(a\mathbf1+u)\circ(b\mathbf1+v)=(ab+B(u,v))\mathbf1+av+bu.
\]
Exactly 72 of the 81 elements of \(S\) are finite left-nested products of idempotents. The nine nonrepresentable elements are \(2\mathbf1\) and the eight pure vectors \(x\) with scalar coefficient zero and all three vector coordinates in \(\{1,2\}\). Among the 72 representable elements, the minimum word-length counts for lengths \(1\) through \(6\) are, respectively,
\[
8,\ 12,\ 14,\ 18,\ 12,\ 8.
\]

## Assumptions and scope

All calculations are in \(\mathbb F_3\), so \(2=-1\) and \(1/2=2\). A word is left-nested: \(e_1\circ e_2\circ\cdots\circ e_m\), with each \(e_i\) idempotent and the product evaluated from left to right. Zero and the unit count as length-one words. The form \(B\) is nondegenerate, and this four-dimensional spin factor is simple. The claim concerns only this field and this quadratic form; it is not a classification over arbitrary fields.

## Proof

Write elements as pairs \((a,u)\), with \(a\in\mathbb F_3\) and \(u\in\mathbb F_3^3\). Squaring gives
\[
(a,u)^2=(a^2+q(u),2au).
\]
If \(u=0\), idempotence forces \(a\in\{0,1\}\). If \(u\ne0\), the vector equation \(2au=u\) forces \(a=2\), and the scalar equation then forces \(q(u)=1\). Since each nonzero coordinate in \(\mathbb F_3\) has square 1, the equation \(x^2+y^2+z^2=1\) holds exactly when one coordinate is nonzero. Thus the idempotents are 0, 1, and the six elements \((2,\sigma e_i)\), where \(\sigma\in\{1,2\}\) and \(e_i\) is a coordinate vector.

For a nontrivial idempotent \(e=(2,\sigma e_i)\),
\[
(a,v)\circ e=(2a+\sigma v_i,\ a\sigma e_i-v).
\]
If the new scalar coefficient is zero, then \(2a+\sigma v_i=0\), hence \(\sigma v_i=a\); the new \(i\)-th vector coordinate is therefore \(a\sigma-v_i=0\). Consequently, any left-nested word with scalar coefficient zero and a nontrivial final idempotent has at least one zero vector coordinate. Appending the unit changes nothing, and appending zero gives zero. Hence none of the eight pure vectors \((0,x,y,z)\) with \(x,y,z\in\{1,2\}\) is representable.

The scalar \(2\mathbf1\) is also not representable. Indeed, if \((a,v)\circ(2,u)\) is scalar with \(q(u)=1\), its vector part gives \(v=au\); its scalar part is then \(2a+v\cdot u=2a+a q(u)=0\). Thus a product ending in a nontrivial idempotent cannot be a nonzero scalar. Removing trailing unit factors shows that the only representable scalar elements are 0 and 1.

For the positive classification and exact minimum lengths, the included standard-library program `verify_spin_factor_f3.py` enumerates all 81 elements and all eight idempotents. Breadth-first closure under right multiplication by every idempotent is exhaustive because each left-nested word is a shorter word followed by one idempotent. The program stores and replays a word witnessing the first (hence minimum) discovery of every reachable element, checks that the missing set is exactly the nine elements described above, and asserts the length counts. Its run prints `VERIFY_OK`.

## Verification

The verifier has no third-party dependencies. It enumerates all 81 algebra elements, derives the idempotent set from the defining equation, replays a minimal word for each of the 72 reachable elements, and asserts both the exact complement and the six length counts. The symbolic invariant above independently explains why the eight pure isotropic vectors cannot be reached; the scalar obstruction is checked directly. The finite enumeration makes no claim about other fields or dimensions.

## Relationship to prior work

Gogić and Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581v1 (first posted 20 September 2026), study finite left-nested idempotent words in simple Jordan algebras. Their spin-factor length theorem assumes a quadratically closed field, while their arbitrary-field exact classification in Proposition 4.1 is for the matrix Jordan algebra \(M_2(\mathbb F)^+\). Those statements do not give this finite-field census for the spin factor with \(q(x,y,z)=x^2+y^2+z^2\) over \(\mathbb F_3\). The paper also notes that representability can fail over some nonclosed fields; the present result supplies a concrete finite-field instance and its full 81-element classification.

## Limitations

This is a finite, form-specific classification over \(\mathbb F_3\). It does not classify other three-dimensional quadratic forms, spin factors over larger finite fields, or arbitrary parenthesizations of products. The exact minimum-length counts are established by exhaustive finite enumeration together with the explicit nonrepresentability invariant, not by a general formula in the field size.

## References

1. I. Gogić and M. Tomašević, “Idempotent words in finite-dimensional simple Jordan algebras,” arXiv:2609.23581v1, submitted 20 September 2026. https://arxiv.org/abs/2609.23581
2. `verify_spin_factor_f3.py`, the standalone exact enumerator embedded with this result.

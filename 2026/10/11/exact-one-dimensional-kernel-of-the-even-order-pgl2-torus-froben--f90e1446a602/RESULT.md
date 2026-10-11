# Exact one-dimensional kernel of the even-order PGL2 torus Frobenius map
## Finding
Under the hypotheses and notation of Higgins--Silva--Somers--Stephens--Sundar--Wokhlu for the torus, suppose \(q^2\) has even order \(n\). Then the PGL2 skein Frobenius homomorphism
\[
\mathrm{{Fr}}^Y:S_t^Y(T^2)\longrightarrow S_q^Y(T^2)
\]
has exact kernel
\[
\ker(\mathrm{{Fr}}^Y)=\mathbb C\,w.
\]
In particular, the source's noninjectivity is minimal as a vector-space defect: it kills precisely the one-dimensional web direction spanned by \(w\), and it kills no nonzero linear combination of the unit and the loop-basis elements \((k,l)_Y\).

## Assumptions and scope
The notation is that of *PGL2 webs at roots of unity*. The source assumes \(q+q^{{-1}}\ne0\), takes \(q^2\) to be a root of unity of order \(n\), and defines a torus Frobenius homomorphism between the corresponding PGL2 skein algebras.

The source recalls the torus basis
\[
\{(k,l)_Y:(k,l)\in\mathbb Z^2\setminus\{(0,0)\}\}\cup\{w,\varnothing\}.
\]
The claim concerns the even-order case only. It is a statement about the linear kernel of the algebra homomorphism; no claim is made here about kernels for other surfaces or about additional structure of the quotient.

## Proof
Theorem 5.6 of the source defines the Frobenius homomorphism on the displayed basis by
\[
\mathrm{{Fr}}^Y((k,l)_Y)=(nk,nl)_Y,
\qquad
\mathrm{{Fr}}^Y(w)=\alpha_n w,
\qquad
\mathrm{{Fr}}^Y(\varnothing)=\varnothing,
\]
where \(\alpha_n=0\) when \(n\) is even.

Let a finite linear combination lie in the kernel:
\[
c_0\varnothing+c_w w+\sum_{{(k,l)\in F}}c_{{k,l}}(k,l)_Y.
\]
Its image is
\[
c_0\varnothing+\sum_{{(k,l)\in F}}c_{{k,l}}(nk,nl)_Y,
\]
because the \(w\)-term vanishes. Multiplication by the positive integer \(n\) is injective on \(\mathbb Z^2\setminus\{(0,0)\}\). Hence the vectors \((nk,nl)\) occurring above are pairwise distinct. By the same torus basis theorem in the target skein algebra, the elements \(\varnothing\) and \((nk,nl)_Y\) are linearly independent. Therefore \(c_0=0\) and every \(c_{{k,l}}=0\). The only unrestricted coefficient is \(c_w\), proving
\[
\ker(\mathrm{{Fr}}^Y)=\mathbb C\,w.
\]

## Verification
The argument was reconstructed directly from the torus basis statement and the basis-level Frobenius formula in Theorem 5.6. The source's Corollaries 1.4 and 5.7 state only the parity dichotomy: noninjective for even \(n\), injective for odd \(n\). A full-text search of the inspected manuscript found no statement identifying the even-order kernel.

No finite experiment is used. The proof is purely linear-algebraic once the published basis and Frobenius formula are accepted. The critical boundary point is that distinct nonzero lattice indices remain distinct after multiplication by \(n\); this is what rules out every additional kernel vector.

## Relationship to prior work
The 2026 source constructs the PGL2 Frobenius homomorphism on the torus and proves that it is noninjective when \(n\) is even, contrasting this with the injective Kauffman-bracket surface Frobenius map. Its basis formula already shows that \(w\) is killed in even order, but the paper states only noninjectivity rather than the complete kernel.

The present statement extracts the exact defect from that formula: all other basis vectors have distinct basis images. Targeted searches for an exact torus PGL2 Frobenius kernel, a one-dimensional kernel, and the formulation \(\ker(\mathrm{{Fr}}^Y)=\mathbb C w\) located no covering result.

## Limitations
The claim is restricted to the torus and to even \(n=\operatorname{{ord}}(q^2)\) under the source's standing assumptions. It does not determine the image as an algebra, a presentation of the quotient, or the behavior for other surfaces. The result is a sharpening of the new torus Frobenius computation, not an independent construction of the homomorphism.

## References
1. S. Higgins, M. Silva, J. Somers, J. Stephens, S. Sundar and V. Wokhlu, *PGL2 webs at roots of unity*, arXiv:2610.01881v1, 2026. See the torus basis discussion, Theorem 5.6, and Corollaries 1.4 and 5.7.

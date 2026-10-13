# The top coherent Frobenius divisor is an \(n\)-fold thickening
## Finding
Let \(k\) be a perfect field of characteristic \(p>0\), and let
\[
f:\mathcal X\longrightarrow S
\]
be smooth and proper with geometrically connected fibres of dimension \(2n\ge4\), with
\[
\omega_{\mathcal X/S}\simeq\mathcal O_{\mathcal X},
\]
and assume every geometric fibre is Hodge-good in the sense of Zou. Put
\[
E_i=R^{2i}f_*\mathcal O_{\mathcal X}\qquad(1\le i\le n).
\]
For each \(i\), relative Frobenius induces an \(\mathcal O_S\)-linear map
\[
h_i:F_S^*E_i\longrightarrow E_i.
\]
Cup product identifies \(E_i\) with \(E_1^{\otimes i}\), and under this identification
\[
\boxed{h_i=h_1^{\otimes i}.}
\]

Equivalently, if \(s_i\) denotes the corresponding section of
\[
\mathcal H_i=E_i\otimes(F_S^*E_i)^{-1},
\]
then \(\mathcal H_i\simeq\mathcal H_1^{\otimes i}\) and
\[
s_i=s_1^{\otimes i}.
\]
Hence, if \(S\) is integral and the Frobenius-split locus is nonempty, the zero schemes define effective Cartier divisors satisfying
\[
\boxed{D_i=iD_1\qquad(1\le i\le n).}
\]
In particular the top coherent Frobenius divisor is the \(n\)-fold Cartier thickening of the degree-two divisor:
\[
D_n=nD_1.
\]
Their common support is the non-Frobenius-split locus. On the Hodge-good locus, Zou's Theorem 6.7 identifies this support also with the locus of infinite quasi-F-split height.

## Assumptions and scope
The hypothesis that every geometric fibre is Hodge-good means that for each fibre \(X_s\), cup product gives
\[
H^\bullet(X_s,\mathcal O_{X_s})\simeq \kappa(\overline s)[\eta]/(\eta^{n+1}),
\qquad \deg\eta=2.
\]
Zou's Lemma 6.1 then makes each \(E_i\) an invertible sheaf, with formation commuting with arbitrary base change. The divisor statement additionally assumes that \(S\) is integral and that at least one fibre is Frobenius split; this ensures that the relevant Frobenius sections are not identically zero.

The assertion is about coherent structure-sheaf cohomology. It does not identify the complete Ekedahl--Oort or Newton stratification, and it does not claim reducedness of \(D_1\).

## Proof
For \(1\le i\le n\), cup product gives a morphism
\[
c_i:E_1^{\otimes i}\longrightarrow E_i.
\]
Both sides are line bundles. On every geometric fibre, Hodge-goodness says that a nonzero generator \(\eta\in H^2(\mathcal O)\) has nonzero power \(\eta^i\), and that this power generates \(H^{2i}(\mathcal O)\). Thus every fibre of \(c_i\) is nonzero. A morphism between line bundles that is nonzero at every point is an isomorphism, so
\[
c_i:E_1^{\otimes i}\xrightarrow{\sim}E_i.
\]

Let \(F_{\mathcal X/S}:\mathcal X\to\mathcal X^{(p)}\) be relative Frobenius. Since each \(E_i\) is locally free and satisfies base change, the induced map on coherent cohomology is
\[
h_i:F_S^*E_i\longrightarrow E_i.
\]
The Frobenius homomorphism on structure sheaves is multiplicative. Therefore the cup-product square commutes:
\[
\begin{array}{ccc}
F_S^*(E_1^{\otimes i}) & \xrightarrow{F_S^*c_i} & F_S^*E_i\\
\downarrow h_1^{\otimes i} && \downarrow h_i\\
E_1^{\otimes i} & \xrightarrow{c_i} & E_i.
\end{array}
\]
Conjugating by the cup-product isomorphisms proves
\[
h_i=c_i\circ h_1^{\otimes i}\circ(F_S^*c_i)^{-1}.
\]
This is precisely the asserted identity after identifying \(E_i\) with \(E_1^{\otimes i}\).

Under the induced identification
\[
\mathcal H_i=E_i\otimes(F_S^*E_i)^{-1}\simeq
\bigl(E_1\otimes(F_S^*E_1)^{-1}\bigr)^{\otimes i},
\]
the section \(s_i\) is \(s_1^{\otimes i}\). Locally trivializing \(\mathcal H_1\), write \(s_1=a\). Then \(s_i=a^i\). On an integral base with \(a\) not identically zero, \(a\) is a non-zero-divisor, so
\[
\operatorname{div}(s_i)=i\operatorname{div}(s_1).
\]
This gives \(D_i=iD_1\).

For \(i=n\), Zou's Lemma 6.2 says that nonvanishing of \(h_n\) on a fibre is equivalent to Frobenius splitting. Since \(h_n=h_1^{\otimes n}\), all \(h_i\) have the same set-theoretic nonvanishing locus. Zou's Theorem 6.7 then identifies that locus, on Hodge-good fibres of dimension at least four, with the quasi-F-split and finite-height loci.

## Verification
The initiating source was checked in full text at Definition 4.10, Proposition 4.14, Lemmas 6.1 and 6.2, and Theorem 6.7. Lemma 6.1 supplies invertibility and base change for all even coherent cohomology sheaves on the Hodge-good locus and explicitly uses the top cup-power map. Lemma 6.2 constructs the top relative Frobenius section and identifies its nonvanishing with Frobenius splitting. Theorem 6.7 identifies Frobenius splitting, quasi-F-splitting, and finite top Artin--Mazur height on the Hodge-good locus.

The new step is a functoriality calculation: the same relative Frobenius construction applies to every invertible \(E_i\), and multiplicativity of Frobenius forces the entire family of coherent Frobenius sections to be tensor powers of the degree-two section. This calculation is formal but scheme-theoretic: it records multiplicity, not merely equality of supports.

As a boundary check, if the Frobenius-split locus is empty then every \(h_i\) is identically zero and the Cartier-divisor statement is not made. If the base is not integral, the tensor-power identity still holds, but an identically vanishing or zero-divisor section need not define an effective Cartier divisor.

## Relationship to prior work
Zou proves the Hodge-good cup-product algebra and the Frobenius-splitting dichotomy in families, but the paper uses the top coherent Frobenius map to detect the open Frobenius-split locus and does not state the tensor-power relation among the degree-\(2i\) coherent Frobenius sections or the resulting divisor multiplicities.

Goldring--Reppen study vanishing orders of Hasse invariants for Calabi--Yau-type \(F\)-zips and apply their Ogus principle to K3 moduli. Their framework demonstrates that scheme-theoretic vanishing order is significant information beyond the support of a Hasse divisor. The inspected K3 result concerns the Hasse invariant of \(H^2_{\mathrm{dR}}\) for K3 surfaces; it does not compare coherent Frobenius sections in degrees \(2,4,\ldots,2n\) for higher-dimensional primitive-symplectic families and does not imply \(D_i=iD_1\).

Targeted searches for the tensor-power formulation, the exact divisor identity, and equivalent Hasse-Witt wording found no covering statement.

## Limitations
The divisor equality is conditional on an integral base and a nonempty Frobenius-split locus. The theorem does not determine whether \(D_1\) is reduced, smooth, irreducible, or nonempty. It does not compute local vanishing orders of \(D_1\); it only proves that every higher even-degree coherent Frobenius section has exactly the corresponding multiple of those local orders.

The statement concerns the Hodge-good locus. It gives no assertion across fibres where Hodge-goodness fails, because there the line-bundle and cup-power identifications used in the proof can break down.

## References
H. Zou, “Quasi-\(F\)-split primitive symplectic varieties in positive characteristic,” arXiv:2609.35467, first submitted 2026-09-28; especially Definition 4.10, Proposition 4.14, Lemmas 6.1--6.2, and Theorem 6.7.

W. Goldring and S. Reppen, “An Ogus Principle for Zip period maps: The Hasse invariant's vanishing order via `Frobenius and the Hodge filtration',” arXiv:2404.05707v1, 2024; especially Sections 1.2.2--1.2.3, 1.4, and 4.7.

# The top coherent Frobenius divisor is an \(n\)-fold thickening

## Finding
Let \(k\) be a perfect field of characteristic \(p>0\). Let \(f:\mathcal X\to S\) be a smooth proper morphism of \(k\)-schemes with geometrically connected fibres of dimension \(2n\ge4\), with \(\omega_{\mathcal X/S}\simeq\mathcal O_{\mathcal X}\). Assume every geometric fibre is Hodge-good: its coherent cohomology algebra is \(\kappa(\bar s)[\eta]/(\eta^{n+1})\) with \(\deg\eta=2\). The base need not be reduced or noetherian.

For \(1\le i\le n\), put \(E_i=R^{2i}f_*\mathcal O_{\mathcal X}\). These are line bundles with formation commuting with arbitrary base change. Cup power identifies \(E_1^{\otimes i}\simeq E_i\), and relative Frobenius induces an \(\mathcal O_S\)-linear map \(h_i:F_S^*E_i\to E_i\). Under the cup-power identifications,
\[
h_i=h_1^{\otimes i}.
\]
Equivalently, for the associated sections \(s_i\) of \(\mathcal H_i=E_i\otimes(F_S^*E_i)^{-1}\), one has \(\mathcal H_i\simeq\mathcal H_1^{\otimes i}\) and \(s_i=s_1^{\otimes i}\). If \(S\) is integral and at least one geometric fibre is Frobenius split, their zero schemes are effective Cartier divisors with
\[
D_i=iD_1,\qquad D_n=nD_1.
\]
Their common support is the locus of geometric fibres that are not Frobenius split, equivalently the locus of infinite quasi-\(F\)-split height.

## Proof
**Cohomology and base change.** Properness and smoothness imply that \(K=Rf_*\mathcal O_{\mathcal X}\) is perfect and commutes with arbitrary derived base change: apply Stacks Project Lemma 36.30.1 with the perfect object and the flat, finitely presented sheaf both equal to \(\mathcal O_{\mathcal X}\). The derived fibre of \(K\) at any point has a one-dimensional cohomology group in each degree \(0,2,\ldots,2n\) and zero cohomology otherwise, as can be checked after the faithfully flat extension to a geometric point.

Fix a point of \(S\) and work locally with a bounded finite free complex representing \(K\). Over the local ring at the point, whenever an entry of a differential is a unit, elementary changes of bases split off a contractible two-term subcomplex with differential \(1\). The complex identities make the neighboring maps zero on the split pair. Repeat until every remaining differential has entries in the maximal ideal. This finite procedure is valid on an open neighborhood after inverting the finitely many required unit entries. Over the residue field the remaining differentials are zero, so the ranks of its terms are the dimensions of the fibre cohomology. In particular only even terms remain and all differentials are therefore zero on the neighborhood itself. It follows that the even cohomology sheaves are line bundles and their formation commutes with arbitrary base change. This uses the absence of odd terms, not just constancy of ranks on the reduction of \(S\).

**Cup powers and Frobenius.** The map \(c_i:E_1^{\otimes i}\to E_i\) given by cup power is an isomorphism since, on every geometric fibre, a generator \(\eta\) of degree two has \(\eta^i\) generating degree \(2i\). For \(\mathcal X^{(p)}=\mathcal X\times_{S,F_S}S\), base change identifies the coherent cohomology of \(\mathcal X^{(p)}\) over \(S\) with the corresponding \(F_S^*E_i\). The pullback by \(F_{\mathcal X/S}:\mathcal X\to\mathcal X^{(p)}\) preserves cup products because the morphism on structure sheaves is multiplicative. As a result,
\[
h_i\circ F_S^*c_i=c_i\circ h_1^{\otimes i}.
\]
This is an equality of morphisms over \(S\), not a comparison only at geometric points. It gives the stated identity of sections upon tensoring with the corresponding dual lines.

**Divisors and support.** In a local trivialization of \(\mathcal H_1\) with \(s_1=a\), the zero ideals of the higher sections are \((a^i)\). Over a geometric fibre, the top coherent map is the linearization of Frobenius on \(H^{2n}(\mathcal O)\). By the fibre criterion used in Zou's Lemma 6.2, it is nonzero if and only if that fibre is Frobenius split. This is equivalently nonvanishing of any of the \(s_i\) at that point. If \(S\) is integral and this locus is nonempty, \(s_1\) is nonzero at the generic point and each \(a\) in a nonempty trivializing open is a non-zero-divisor. Thus \((a^i)=(a)^i\) gives \(D_i=iD_1\) as effective Cartier divisors. For each geometric fibre, Zou's Corollary 4.16 (applied to the Hodge-good fibre of dimension at least four with trivial canonical bundle) identifies Frobenius splitting with quasi-\(F\)-split height one, and gives infinite height otherwise. This is the fibrewise dichotomy used in Zou's Theorem 6.7.

## Verification
The argument needs no finite computation. The parity of the nonzero degrees in the perfect complex proves local freeness and base change on the given base, including at nilpotent thickenings. The cup-product commutative square is defined over the base, giving the local ideal-power statement before any Cartier hypothesis is imposed. Testing geometric fibres is used for the cup-power isomorphisms and for the set-theoretic criterion, not for the equality of the sections.

## Relationship to prior work
Zou's Definition 4.10 supplies the fibre cohomology algebra. Lemma 6.1 constructs the Hodge-good open locus and uses the top cup power over a reduced base in its proof; Lemma 6.2 uses the top coherent Frobenius section to detect splitting. Corollary 4.16 and Theorem 6.7 give the height dichotomy. Those support and height statements do not make an equality of the vanishing ideals across degrees. The cup-product comparison above relates those ideals exactly. Goldring–Reppen's Hasse-vanishing-order results for Calabi–Yau-type \(F\)-zips, including the K3 application, concern the vanishing order of an invariant in a given zip representation, not this comparison between different coherent cohomological degrees.

## Limitations
The tensor-power identity and the equality of zero ideals with the corresponding ideal powers do not require an integral base. The Cartier conclusion requires the local equation to be a non-zero-divisor, guaranteed here by integrality and a nonempty Frobenius-split locus. If that locus is empty, every section vanishes at every geometric point; this implies zero sections on a reduced base, but on a nonreduced base only nilpotence of their local coefficients follows from pointwise vanishing. The theorem neither asserts that \(D_1\) is reduced or nonempty nor describes the full Ekedahl–Oort or Newton stratification. It does not apply across fibres where Hodge-goodness fails.

## References
1. H. Zou, *Quasi-\(F\)-split primitive symplectic varieties in positive characteristic*, [arXiv:2609.35467v1](https://arxiv.org/abs/2609.35467v1), Definition 4.10, Corollary 4.16, Lemmas 6.1–6.2 and Theorem 6.7.
2. The Stacks Project, Lemma 36.30.1 and Remark 36.30.2, [Cohomology and base change, VI](https://stacks.math.columbia.edu/tag/0A1G).
3. W. Goldring and S. Reppen, *An Ogus Principle for Zip period maps: The Hasse invariant's vanishing order via Frobenius and the Hodge filtration*, [arXiv:2404.05707](https://arxiv.org/abs/2404.05707), especially the Ogus principle and K3 application.

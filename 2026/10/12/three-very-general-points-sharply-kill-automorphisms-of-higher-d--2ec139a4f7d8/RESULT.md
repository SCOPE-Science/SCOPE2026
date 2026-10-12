# Three very general points sharply kill automorphisms of higher-dimensional abelian blow-ups
## Finding
Let \(A\) be a complex abelian variety of dimension \(d\ge 3\). For a very general ordered triple \((p_1,p_2,p_3)\in A^3\),
\[
\operatorname{Aut}\!\left(\operatorname{Bl}_{p_1,p_2,p_3}A\right)=\{1\}.
\]
Moreover, the number of points is sharp: every one-point blow-up and every two-distinct-point blow-up retains a nontrivial involution. Thus the exact very-general threshold is \(3\).

## Assumptions and scope
The base field is \(\mathbf C\), \(A\) is an abelian variety of dimension \(d\ge3\), and the triple is very general in the standard sense: it lies outside a countable union of proper closed subsets of \(A^3\). No assertion is made for merely general triples, special triples, or positive characteristic. The claim concerns ordinary algebraic automorphisms.

## Proof
Write \(\pi:\widetilde A=\operatorname{Bl}_{p_1,p_2,p_3}A\to A\). First, every automorphism of \(\widetilde A\) descends to an automorphism of \(A\) preserving the unordered center. Sarkar's proof of Theorem A in dimension at least \(3\) contracts all \((-1)\)-hypersurfaces and shows that every automorphism descends to the resulting variety. An abelian variety contains no rational curves: if \(f:\mathbf P^1\to A\) were nonconstant, every translation-invariant holomorphic one-form on \(A\) would pull back to zero, but these forms span every cotangent space, forcing \(df=0\) and hence \(f\) constant. Therefore \(A\) contains no divisor isomorphic to \(\mathbf P^{d-1}\), hence no \((-1)\)-hypersurface. Sarkar's contraction in this case is exactly \(\pi\), so an automorphism of \(\widetilde A\) descends and permutes \(\{p_1,p_2,p_3\}\). Conversely, any automorphism of \(A\) preserving this finite center lifts uniquely to its blow-up. It therefore suffices to show that a very general triple has trivial setwise stabilizer in \(\operatorname{Aut}(A)\).

Every automorphism \(f\) of \(A\) has a unique affine form
\[
f(x)=g(x)+a,
\]
with \(a=f(0)\in A\) and \(g\in\operatorname{Aut}_{\mathrm{gp}}(A)\). Indeed, translating \(f\) by \(-f(0)\) gives an automorphism fixing the origin, hence a group homomorphism by the rigidity lemma. Milne's finiteness theorem gives that \(\operatorname{End}(A)\) is a free abelian group of finite rank, so \(\operatorname{Aut}_{\mathrm{gp}}(A)\subset\operatorname{End}(A)\) is countable.

Fix \(g\in\operatorname{Aut}_{\mathrm{gp}}(A)\) and \(\sigma\in S_3\). The triples stabilized through the permutation \(\sigma\) are those for which some \(a\in A\) satisfies \(g(p_i)+a=p_{\sigma(i)}\) for all \(i\). Eliminating \(a\) gives
\[
g(p_2-p_1)=p_{\sigma(2)}-p_{\sigma(1)},\qquad
g(p_3-p_1)=p_{\sigma(3)}-p_{\sigma(1)}.
\]
Hence this locus \(L_{g,\sigma}\subset A^3\) is closed, indeed the kernel of a homomorphism \(A^3\to A^2\). It equals all of \(A^3\) only for \((g,\sigma)=(1,1)\): if the first identity held identically, its right-hand side could not involve \(p_3\), so \(\sigma\) must preserve \(\{1,2\}\); similarly the second identity forces \(\sigma\) to preserve \(\{1,3\}\). Thus \(\sigma=1\), after which the identities force \(g=1\). Consequently every \(L_{g,\sigma}\) with \((g,\sigma)\ne(1,1)\) is a proper closed subset. There are only countably many such pairs. A very general triple avoids their union and the diagonals, so its setwise stabilizer is trivial. The descended automorphism of \(A\), and therefore the original automorphism of \(\widetilde A\), is the identity.

Sharpness is explicit. For one point \(p\), the involution \(x\mapsto2p-x\) fixes \(p\) and lifts to \(\operatorname{Bl}_pA\). For two distinct points \(p,q\), the involution \(x\mapsto p+q-x\) swaps \(p\) and \(q\) and lifts to \(\operatorname{Bl}_{p,q}A\). Neither involution is the identity. Thus \(3\) is minimal.

## Verification
The proof reduces the blow-up automorphism problem to a setwise-stabilizer problem using the dimension-at-least-three contraction argument in Sarkar's proof of Theorem A. The stabilizer argument is exact: it uses the affine decomposition of automorphisms of an abelian variety, countability of the group-automorphism part, and two homomorphism equations whose common kernel is proper for every nonidentity pair \((g,\sigma)\). No finite experiment or unproved exhaustion is used. The one- and two-point lower bounds are verified by explicit involutions.

## Relationship to prior work
Sarkar proves that for every projective variety of dimension at least \(2\) that is not a rational surface, sufficiently many very general point blow-ups have no nontrivial automorphism. His Theorem 3.1 gives the general bound \(r_0=\dim\operatorname{Aut}^0(X)+1\); for an abelian variety of dimension \(d\), this is \(d+1\). For every \(d\ge3\), the present argument replaces that dimension-dependent bound by the sharp constant \(3\). Sarkar's Remark 5.1 also shows why “very general” cannot simply be weakened to “general” in the abelian setting when an infinite-order automorphism is present, using torsion points. The exact three-point threshold and its matching one-/two-point obstruction were not found in the checked source or targeted literature searches.

## Limitations
The result is stated over \(\mathbf C\) and for dimension at least \(3\). It does not classify the stabilizers of special triples, does not assert an analogous statement for merely general triples, and does not address positive characteristic. The originality search cannot exclude an unindexed prior note stating the same sharp stabilizer threshold under different terminology.

## References
1. Supravat Sarkar, *Automorphisms of very general blow up*, arXiv:2608.07983v1, especially Theorem 3.1, Lemma 2.2, the dimension-at-least-three case in the proof of Theorem A, and Remark 5.1.
2. J. S. Milne, *Abelian Varieties*, Theorem 9.14 and Corollary 15.2, for finite-rank homomorphism groups and the rigidity statement that a morphism of abelian varieties carrying zero to zero is a homomorphism.

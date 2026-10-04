# Exact finite-parameter 1-type growth in the universal homogeneous meet-tree
## Finding
Let \(T=\mathsf{DMT}\) be the theory of the Fraïssé limit of finite meet-trees, in the language consisting of the tree order and meet. For every nonempty finite parameter set \(P\), let
\[
A=\operatorname{dcl}(P)=\langle P\rangle_\wedge,
\qquad m=|A|.
\]
Then
\[
\boxed{|S_1(P)|=4m}.
\]
Thus a finite meet-closed parameter tree with \(m\) points has exactly \(m\) algebraic and \(3m\) nonalgebraic complete 1-types.

More explicitly, the nonalgebraic types form three families of size \(m\):

1. a new point lying on the tree skeleton in one of the \(m\) linear gaps determined by \(A\);
2. a new point whose maximal meet with \(A\) is an existing vertex \(v\in A\), lying in a cone above \(v\) not occupied there by \(A\);
3. a new point whose maximal meet with \(A\) is a new point lying in one of those \(m\) linear gaps, and which then branches into a fresh cone above that new meet-point.

If \(|P|=n\ge1\), then
\[
\boxed{4n\le |S_1(P)|\le 8n-4},
\]
and both bounds are sharp. Hence
\[
\boxed{\max_{|P|=n}|S_1(P)|=8n-4}.
\]
For the empty parameter set, \(|S_1(\varnothing)|=1\).

## Assumptions and scope
A meet-tree is a lower semilinear order in which every pair has a greatest lower bound. The theory \(\mathsf{DMT}\) is the complete theory of the countable universal homogeneous meet-tree, equivalently the Fraïssé limit of all finite meet-trees. It eliminates quantifiers. For a finite set \(P\), definable closure is its meet-closure, so types over \(P\) and over \(A=\operatorname{dcl}(P)\) are naturally in bijection.

The statement concerns complete 1-types over finite parameter sets. It does not claim a formula for higher-arity type spaces or for expansions of \(\mathsf{DMT}\) by additional cone structure.

## Proof
Fix a nonempty finite meet-closed substructure \(A\), with \(|A|=m\). Its Hasse diagram is a finite rooted tree. There are exactly \(m\) linear gaps relevant to inserting one new point without branching: one gap strictly below the root, and one open interval corresponding to each of the \(m-1\) cover edges. Density of \(\mathsf{DMT}\) realizes every such gap.

For a realization \(b\) of a nonalgebraic 1-type over \(A\), set
\[
c=\max\{a\wedge b:a\in A\}.
\]
The standard one-point generation analysis for meet-trees says that \(\langle A b\rangle\) contains at most the two new points \(b\) and \(c\). Quantifier elimination therefore reduces the complete type of \(b\) over \(A\) to the position of \(c\), whether \(b=c\), and, when \(c<b\), which cone above \(c\) contains \(b\).

There are three disjoint cases.

First, \(b=c\). Then \(b\) lies on the existing tree skeleton, and its cut in \(A\) is exactly one of the \(m\) gaps above. This gives \(m\) types.

Second, \(c\in A\) and \(c<b\). For each \(c\in A\), the point \(b\) must lie in a cone above \(c\) not already represented by an element of \(A\) strictly above \(c\); otherwise the maximal meet with \(A\) would be greater than \(c\). The dense generic meet-tree has infinitely many open cones above every point, so such a fresh cone exists, and homogeneity makes all choices of fresh cone have the same type over \(A\). This gives exactly \(m\) types.

Third, \(c\notin A\) and \(c<b\). The new meet-point \(c\) lies in exactly one of the same \(m\) linear gaps. Once that gap is fixed, \(b\) must occupy a fresh cone above \(c\), distinct from the cone leading toward the relevant old points of \(A\). Again density and infinite ramification give existence, and homogeneity gives uniqueness over \(A\). This gives another \(m\) types.

These cases are exhaustive by the one-point generation lemma and pairwise distinct by their quantifier-free meet/order diagrams. Hence there are \(3m\) nonalgebraic types. Adding the \(m\) algebraic types \(x=a\), \(a\in A\), yields \(|S_1(A)|=4m\), and therefore \(|S_1(P)|=4|\operatorname{dcl}(P)|\).

It remains to bound the size of the meet-closure of an \(n\)-element set. Starting with one generator gives one point. Adjoining one new generator to a finite meet-tree adds at most the generator and one new maximal meet-point, so induction gives
\[
|\operatorname{dcl}(P)|\le 1+2(n-1)=2n-1.
\]
The obvious lower bound is \(|\operatorname{dcl}(P)|\ge n\). A chain of \(n\) parameters attains the lower bound. A finite full binary meet-tree with \(n\) chosen leaves has exactly \(n-1\) internal meet-points, so its leaf set has meet-closure of size \(2n-1\); universality embeds such a finite meet-tree into the generic structure. Multiplying by four gives the sharp type-count bounds.

## Verification
The bundled `verify.py` performs two finite checks independent of the symbolic count. First, it exhaustively enumerates rooted labeled trees and one-point generated extensions for every meet-closed old structure with at most four old vertices. It canonically records the full meet table of the generated extension over the fixed old labels and confirms that every old structure has exactly \(3m\) distinct nonalgebraic extension signatures for \(m=1,2,3,4\).

Second, it exhaustively enumerates rooted tree shapes with topological labels through seven vertices, computes meet-closures of all nonempty subsets, and checks the bound \(|\langle P\rangle_\wedge|\le 2|P|-1\). It also finds examples meeting the lower and upper bounds in the tested range. The checker returns `VERIFY_OK`.

## Relationship to prior work
Kaplan, Rzepecki, and Siniora establish the Fraïssé description, quantifier elimination, and the fact that a finitely generated substructure is the meet-closure of its generators. Estevan and Kaplan record the sharper local structural ingredient that adjoining one point to a finite tree adds at most that point and one additional maximal meet-point, and use a polynomial bound on finite 1-type counts in an NIP argument. Mennuni gives a detailed classification of global invariant 1-types of dense meet-trees and records the standard definable-closure description.

The exact finite-parameter formula \(|S_1(P)|=4|\operatorname{dcl}(P)|\), the sharpened closure envelope \(2n-1\), and the resulting exact maximal type count \(8n-4\) were not located in those sources or in targeted searches for equivalent finite-type-count formulations. The result therefore refines the qualitative polynomial type-counting argument into an exact local complexity profile. Because the deduction is short once the one-point extension geometry is isolated, some residual folklore risk remains.

## Limitations
The proof uses the pure meet-tree language. Additional predicates or relations on cones can increase the number of 1-types. The finite checker is a consistency check only; the infinite theorem rests on quantifier elimination, the one-point generation lemma, density, infinite ramification, and universality. No independent audit has been performed.

## References
- Itay Kaplan, Tomasz Rzepecki, and Daoud Siniora, *On the automorphism group of the universal homogeneous meet-tree*, arXiv:1904.05144; first public version 2019-04-10.
- Pedro Andrés Estevan and Itay Kaplan, *Non-forking and preservation of NIP and dp-rank*, arXiv:1909.04626. In particular, Remark 4.6 gives the one-point generation bound and Corollary 4.14 uses polynomial finite-type counting.
- Rosario Mennuni, *Weakly binary expansions of dense meet-trees*, Mathematical Logic Quarterly 68 (2022), DOI 10.1002/malq.202000045.

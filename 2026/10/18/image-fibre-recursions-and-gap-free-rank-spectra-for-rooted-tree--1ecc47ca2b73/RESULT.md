# Image-fibre recursions and gap-free rank spectra for rooted-tree retractions

## Finding
For integers \(b\ge2\) and \(h\ge1\), let \(T_{b,h}\) be the complete rooted word tree through depth \(h\) on an alphabet with \(b\) letters. An endomorphism here fixes the empty-word root and maps children to children of the image of their parent. A retraction is an endomorphism \(F\) with \(F\circ F=F\).

**Theorem.** The images of the retractions are exactly the prefix closures of the nonempty subsets of the depth-\(h\) leaves. Thus there are \(2^{b^h}-1\) different images. Moreover, the number \(R(Y)\) of retractions onto each specified image \(Y\) and the complete generating polynomial
\[
P_{b,h}(z)=\sum_{F\circ F=F}z^{|\operatorname{im}F|}
\]
are determined exactly by the child-subtree recursions below. Their rank support has no gaps:
\[
\operatorname{supp}P_{b,h}=\{h+1,h+2,\dots,N\},\qquad
N=1+b+\cdots+b^h=\frac{b^{h+1}-1}{b-1}.
\]
The four extreme coefficients are
\[
[z^{h+1}]P_{b,h}=b^h,\qquad
[z^{h+2}]P_{b,h}=b^{h-1}\binom{b}{2}2^{b^h-2},
\]
\[
[z^{N-1}]P_{b,h}=b^h(b-1),\qquad [z^N]P_{b,h}=1.
\]
Overlapping boundary exponents in the smallest cases express the same consistent coefficient.

## Assumptions and scope
Vertices are finite words \(w\) of length \(|w|\le h\); the root is the empty word and the children of \(w\) are \(wa\), one per alphabet letter. All maps preserve the root and directed parent-child arcs. Every image has vertices on every level \(0,\ldots,h\). Image rank means the total number of image vertices, rather than the number of image leaves or retained first-level children. This is an endomorphism monoid under composition, not the monoid of unrestricted graph homomorphisms allowing level reversals.

For a nonempty prefix-closed full-height rooted subtree \(Y\) of a complete height-\(d\) tree, let \(A_d(Y)\) denote the number of root-preserving, arc-preserving maps from the complete height-\(d\) tree into \(Y\). Let \(R_d(Y)\) denote the number of retractions of the full height-\(d\) tree whose image is exactly \(Y\). If the root of \(Y\) has \(k\) retained children, with descendant subtrees \(Y_1,\ldots,Y_k\) of height \(d-1\), then \(1\le k\le b\). A one-vertex subtree has \(A_0=R_0=1\).

## Proof
**Image characterization.** The image of an idempotent map is precisely its fixed-point set. If a vertex \(v\) of depth below \(h\) is fixed, every source child of \(v\) maps to a child \(w\) of \(v\). Idempotence makes this image child fixed: \(F(w)=F(F(c))=F(c)=w\). Thus every fixed internal vertex has at least one fixed child, and fixed vertices are prefix-closed because the parent of \(F(v)=v\) equals \(F(\operatorname{parent}v)\). Hence every image is the prefix closure of a nonempty set of leaves of depth \(h\). Conversely any such subtree admits a retraction: fix its vertices and recursively send every omitted child subtree to a chosen retained child subtree using any rooted-tree morphism. The leaf subset determines the subtree uniquely, proving the image count.

**Exact image-fibre multiplicity.** A root-preserving map from the complete height-\(d\) source into \(Y\) assigns each of its \(b\) child subtrees independently to one of the \(k\) retained child subtrees and then chooses an arbitrary rooted map to the selected target. This proves
\[
A_d(Y)=\left(\sum_{j=1}^{k}A_{d-1}(Y_j)\right)^b.
\]
For a retraction onto \(Y\), each retained source child must map into itself by a retraction onto its prescribed image \(Y_j\); each of the other \(b-k\) source child subtrees chooses any morphism into one of the retained target subtrees. Therefore
\[
R_d(Y)=\left(\prod_{j=1}^k R_{d-1}(Y_j)\right)
\left(\sum_{j=1}^kA_{d-1}(Y_j)\right)^{b-k}.
\]
These equations count distinct maps without symmetry division because source and target alphabet child positions are labeled.

**Complete finite rank polynomial.** Start with a *multiset* \(\mathcal S_0=\{(1,1,1)\}\). Given \(\mathcal S_{d-1}\), take each ordered \(b\)-tuple of choices from \(\{\bot\}\sqcup\mathcal S_{d-1}\), except the all-\(\bot\) tuple. For the \(k\) non-\(\bot\) entries \((s_j,a_j,r_j)\), insert into \(\mathcal S_d\) the triple
\[
\left(1+\sum_j s_j,\ \left(\sum_j a_j\right)^b,\
\left(\prod_jr_j\right)\left(\sum_j a_j\right)^{b-k}\right).
\]
Keep repetitions: different labeled subtrees may have identical triples. Then
\[
P_{b,h}(z)=\sum_{(s,a,r)\in\mathcal S_h}r z^s.
\]
This is an exact terminating prescription for every coefficient, and its triple states additionally retain the complete image-specific retraction multiplicities.

**No gaps.** Induct on \(h\). At height zero only rank one occurs. For height \(h\ge1\), if the root retains exactly \(k\) children, induction shows that the possible ranks of its \(k\) retained subtrees fill every integer from \(kh\) through \(kN_{h-1}\), where \(N_{h-1}=1+\cdots+b^{h-1}\). The full image ranks at fixed \(k\) therefore fill \([1+kh,1+kN_{h-1}]\cap\mathbb Z\). The intervals for consecutive \(k\) overlap or touch: for \(k\ge1\),
\[
1+kN_{h-1}+1\ge 1+(k+1)h
\]
because \(N_{h-1}\ge2h-1\) for \(b\ge2\). The first rank is \(1+h\) and the last is \(1+bN_{h-1}=N\). Each image admits at least one retraction, so all these coefficients are positive.

**Boundary coefficients.** Rank \(h+1\) forces a single rooted path ending in one leaf. There are \(b^h\) such paths and exactly one map onto each (all source leaves map to that leaf). Rank \(h+2\) forces the image to be one path to depth \(h-1\), split only at its last step into two retained leaves. Such images number \(b^{h-1}\binom b2\). Every nonretained source leaf may map independently to either retained leaf, since those two images have a common prefix through depth \(h-1\); hence each such image supports \(2^{b^h-2}\) retractions. For rank \(N-1\), the unique deleted vertex must be a leaf, of which there are \(b^h\); that omitted leaf can map to any of the \(b-1\) other children of its parent, with all other vertices fixed. Full rank forces the identity. These are exact counts, including \(h=1\).

## Verification
The standalone `verify.py` computes every labeled image-tree triple using the stated recurrence. Separately, it constructs **every** root-preserving parent-preserving endomorphism directly from all local child maps, squares each resulting vertex map by composition, and tallies its actual image size if idempotent. Five exhaustive cases \((b,h)=(2,1),(2,2),(2,3),(3,1),(3,2)\) cover \(547{,}920\) total endomorphisms. The direct histograms agree coefficientwise with the recursion and with all four boundary formulas. Further recurrence-only consistency checks cover \((2,4),(4,1)\). Reproduce with `python3 verify.py` from the same directory; it reports `ALL_EXACT_CHECKS_PASSED`. The finite experiments check implementations and small cases; the arbitrary-parameter conclusions rest on the preceding proof.

For example,
\[
P_{2,2}(z)=4z^3+8z^4+4z^5+4z^6+z^7,
\]
and the total numbers at \((b,h)=(2,3)\) and \((3,2)\) are respectively \(1065\) and \(9028\).

## Relationship to prior work
Ahmed and Savchuk study the rooted-tree endomorphisms **induced by integer polynomials** on adic residue systems; their 2017 paper establishes section formulas and level-transitive automorphism criteria. The present endomorphisms are unrestricted parent-preserving finite-tree maps, and its claim concerns their composition-idempotent images and every total-vertex image rank, not polynomial-induced tree dynamics.

Al-Aadhami's 2017 thesis, Section 4.3.2, Theorem 4.3.4, **already counts all idempotents of arbitrary monoid wreath products**. Since the full rooted-tree endomorphism monoid is an iterated full-transformation wreath product, the *unweighted total* \(P_{b,h}(1)\) is covered in principle by that existing theorem and is not proposed as a separate new enumeration. The additional statements here refine this to exactly which labeled leaf-prefix subsets are retract images, their individual retraction fibres, the full rank polynomial weighted by the image size at **every level**, its gap-free support, and sharp near-extremal coefficients. The thesis's use of the term 'rank' in this section is the rank of the outer transformation on the \(b\) first-level children, not the full image-vertex cardinality studied here.

Gu and Hou's 2020 study of regular graph endomorphisms of trees concerns a different ambient category and regularity. Its full text was not inspected, and no claim about its entire contents is made.

## Limitations
The theorem is for complete finite rooted trees with labeled child positions and strictly level-preserving arc morphisms; it does not classify arbitrary unrooted graph endomorphisms, infinite-tree retractions, or automorphisms. The polynomial is specified by an exact finite multiset recursion, not a closed elementary expression for arbitrary height. Known wreath-product formulas imply its unweighted specialization; equivalent rank-weighted results in older semigroup or adic-Lipschitz literature cannot be excluded solely from search coverage. No independent audit of this theorem has been performed.

## References
1. E. Ahmed and D. Savchuk, *Endomorphisms of regular rooted trees induced by the action of polynomials on the ring of d-adic integers*, arXiv:1711.06735v1 (17 November 2017), https://arxiv.org/html/1711.06735v1.
2. A. D. H. Al-Aadhami, *Combinatorial Questions for \(S\wr \mathcal T_n\) for a semigroup*, University of York thesis (2017), Section 4.3.2, Theorem 4.3.4, https://etheses.whiterose.ac.uk/id/eprint/19494/1/asawer-thesis-v2.pdf.
3. J. Gu and Y. Hou, *Trees whose regular endomorphisms form a monoid*, Discrete Mathematics (2020), doi:10.1016/j.disc.2019.111655. Bibliographic/abstract-level comparison only.

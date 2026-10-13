# Modal rigidity and depth collapse in nested S5 hierarchies

## Finding
Let \(H\geq1\) and let \(W\) be a nonempty finite set with a chain of equivalence relations \(E_1\subseteq\cdots\subseteq E_H=W^2\). The ordinary multimodal Boolean algebra on \(\mathcal P(W)\) has one diamond for each \(E_i\). Given an ordered tuple of propositional generators, color each world by its joint Boolean truth-value word.

For \(i=0\), define the signature of a singleton leaf to be its color. For \(1\leq i\leq H\), define the signature \(s_i(B)\) of an \(E_i\)-class \(B\) as the **set** (without multiplicity) of signatures of the \(E_{i-1}\)-classes contained in \(B\); for \(i=1\), these are the singleton colors. For a world \(x\), let \(B_i(x)\) be its \(E_i\)-class and let \(B_0(x)=\{x\}\). Put
\[
\tau(x)=(s_0(B_0(x)),s_1(B_1(x)),\ldots,s_{H-1}(B_{H-1}(x))).
\]
Then **two worlds satisfy exactly the same ordinary modal formulas if and only if their \(\tau\)-vectors agree**. This is already decided by formulas of modal depth at most \(H-1\). If \(K\) is the number of distinct vectors, the generated algebra has exactly \(2^K\) elements.

In particular, the generators yield the entire powerset algebra **if and only if the coloring has no nonidentity automorphism preserving every \(E_i\)**. Thus, for these nested epistemic frames, modal generation is equivalent to rigidity of the colored partition tree, despite the failure of equivalence between bisimulation and automorphism orbits for arbitrary colorings.

For a homogeneous hierarchy, let \(b_i\geq1\) be the number of children of each node at height \(i\), counted upwards from world-leaves, and let \(n=\prod_{i=1}^{H}b_i\). If \(r\geq0\) propositions give \(q=2^r\) available colors, set
\[
A_0=q,\qquad A_i=\binom{A_{i-1}}{b_i}\quad(1\leq i\leq H),
\]
interpreting a binomial coefficient as zero if its lower argument exceeds its upper argument. The exact number of **ordered generating \(r\)-tuples** is
\[
\boxed{N_H(q)=A_H\prod_{i=1}^{H}(b_i!)^{\prod_{j=i+1}^{H}b_j}}.
\]
Consequently, the minimum generator rank is the least \(r\geq0\) for which \(A_H(2^r)>0\). For complete binary hierarchies of height \(H\geq2\), this rank is **exactly two**, even as the number of worlds \(2^H\) grows without bound. For every \(H\geq2\), there is a generating two-proposition coloring for which depth \(H-2\) does not distinguish all worlds, so the depth bound \(H-1\) is sharp.

## Assumptions and scope
The relations are named and nested, all finite, and the largest relation is universal. Modal formulas use Boolean connectives and ordinary existential diamonds, without counting modalities, nominals, or fixpoints. A coloring by \(q\) colors is any assignment of the \(q\) available words; unused colors are permitted. The irregular-tree classification applies without uniform block sizes. The displayed enumeration applies only to complete level-regular hierarchies, and counts ordered tuples on the fixed, individually labeled world-set. Binary-tree sharpness assumes at least two propositions but uses only three of their four truth-value words.

## Proof
**Signature formulas.** Let \(\chi_{0,a}\) be the propositional conjunction characterizing the color \(a\). Inductively, for every realizable signature \(S\) of a level-\(i\) block, let
\[
\chi_{i,S}=\left(\bigwedge_{t\in S}\Diamond_i\chi_{i-1,t}\right)\wedge\Box_i\left(\bigvee_{t\in S}\chi_{i-1,t}\right).
\]
Every \(E_i\)-class is nonempty, and this formula holds at precisely the worlds whose level-\(i\) class has signature \(S\). Its modal depth is \(i\). Hence different \(\tau\)-vectors are separated at depth at most \(H-1\).

**Bisimulation converse.** Relate worlds whose complete signature vectors agree. If \(x\) is related to \(x'\) and \(yE_i x\), equality of the level-\(i\) signatures provides an \(E_{i-1}\)-child block of \(B_i(x')\) with the same signature as the child containing \(y\). Descend recursively through the equality of the *sets* of child signatures, choosing a corresponding child until obtaining a leaf \(y'\). Then the signatures of \(y,y'\) agree at levels at most \(i\), and their signatures at levels above \(i\) agree because those ancestors are inherited from \(x,x'\). Thus \(yE_i x\) has a related successor, and symmetrically the back condition holds. Color agreement supplies the atomic condition. The relation is a bisimulation, so no modal formula separates equal vectors. Boolean closure then has one atom per vector and size \(2^K\).

**Rigidity criterion.** A nonidentity color-preserving automorphism leaves every modal formula invariant, so full generation implies rigidity. For the converse, realize the hierarchy as the rooted tree of equivalence classes, with labeled leaves and level-preserving isomorphisms. A colored tree is rigid exactly when each child subtree is rigid and siblings of the same uncolored shape have different colored isomorphism types (the standard rooted-tree symmetry argument). Induction on level shows that for rigid colored subtrees, equality of their *set-valued* signatures implies a color-preserving, level-preserving isomorphism: at the leaf level this is immediate, and at the next level rigidity makes all child signatures distinct, so equal signature sets give a bijection of corresponding rigid children. Consequently, at any parent, distinct children in a rigid colored tree have distinct signatures. Two different leaves either have distinct colors or diverge at some internal parent; at their least common ancestor, their respective children have distinct signatures. Their \(\tau\)-vectors therefore differ. This proves full modal generation.

**Homogeneous counting.** The signature of a rigid height-zero tree is a color, giving \(A_0=q\) possibilities. A rigid height-\(i\) subtree is described up to rooted color-preserving isomorphism by an unordered collection of \(b_i\) distinct rigid height-\(i-1\) types, giving \(A_i=\binom{A_{i-1}}{b_i}\). For a fixed hierarchy on labeled leaves, each such unordered choice can be assigned to its labeled child positions in \(b_i!\) ways, independently at each of the \(\prod_{j=i+1}^H b_j\) nodes at height \(i\). Multiplying gives the formula. This is the familiar distinguishing-rooted-tree binomial recursion, applied here only after proving its modal interpretation; the bare combinatorial recursion is not claimed as new.

**Binary rank and sharp depth.** For \(b_i=2\), \(q=2\) gives \(A_1=1\), \(A_2=0\), ruling out one proposition when \(H\ge2\). For \(q=4\), \(A_1=6\), \(A_2=15\) and all subsequent terms are at least \(15\), proving sufficiency of two propositions. To see depth sharpness, construct three rigid, pairwise nonisomorphic colored binary subtrees \(T_i^0,T_i^1,T_i^2\) at every height \(i\): start with singleton leaves of three different colors and define \(T_i^a\) to have as children the two \(T_{i-1}\)-types other than \(a\). Every such tree is rigid. Every height-\(i\) subtree for \(i\ge2\) contains all three height-\((i-2)\) subtree signatures, because any two distinct two-element subsets of a three-element set have full union. By induction on modal depth, in this family the depth-\(t\) type of a leaf, for \(t\le H-2\), is determined by its level-zero through level-\(t\) signatures: modalities into levels at most \(t\) see only the corresponding child-signature hierarchy, while every larger equivalence block contains all three height-\((t-1)\) signatures and therefore offers the same lower-depth successor types. The two height-\((H-1)\) children of \(T_H^0\) have different signatures but share one height-\((H-2)\) child type. Choose corresponding leaves in those shared-type children. They agree through level \(H-2\), hence are depth-\((H-2)\) equivalent, but depth \(H-1\) distinguishes them by the characteristic formula for their different height-\((H-1)\) block types.

## Verification
The standalone `verify.py` requires only the Python standard library. Execute `python3 verify.py`. It compares generated modal partitions to color-preserving rooted-tree rigidity on 15,137 exhaustive colorings of eight regular models and 6,102 exhaustive colorings of six nonuniform models, checks the exact enumeration in every regular test, directly computes 330 modal Boolean closures, and tests the binary sharp-depth construction through height seven. Finite tests support the proof and are not substitutes for it.

## Relationship to prior work
Wißmann, Milius and Schröder (first publicly available May 3, 2021) develop general modal characteristic formulas and behavioral partition refinement, but the inspected introduction, main construction, and appendices do not give the nested-equivalence signature-vector theorem or the sharp \(H-1\) stabilization. Cheng (2006), Theorems 3.1 and 3.2, already proves the rooted-tree distinguishing-coloring criterion and its recursive count. The present regular-hierarchy binomial formula is a specialization of that established enumeration **conditional on** the modal-to-rigidity equivalence, not a newly discovered enumeration principle. The central proposed addition is the exact ordinary-modal description of nested equivalence frames and its depth cutoff, including the sharp family.

## Limitations
No claim is made for arbitrary nonnested multimodal S5 frames, graded modalities, infinite frames, or counting versions of the logic. Equality of arbitrary modal equivalence classes with automorphism orbits is **not** asserted: a singleton colored red and a two-leaf block colored red-red have different automorphism orbits but may be ordinarily modally bisimilar. The originality of the modal specialization, rather than the classical tree recurrence, requires independent historical review.

## References
1. T. Wißmann, S. Milius, L. Schröder, *Explaining Behavioural Inequivalence Generically in Quasilinear Time*, arXiv:2105.00669 (public May 3, 2021), and expanded *Quasilinear-time Computation of Generic Modal Witnesses for Behavioural Inequivalence*, Logical Methods in Computer Science 18(4), 2022, DOI:10.46298/lmcs-18(4:6)2022. The published work is indexed under primary MSC2020 03B45.
2. C. T. Cheng, *On Computing the Distinguishing Numbers of Trees and Forests*, Electronic Journal of Combinatorics 13 (2006), R11, DOI:10.37236/1037, especially Theorems 3.1–3.2.
3. V. Arvind, C. Cheng, N. Devanur, *On Computing the Distinguishing Numbers of Planar Graphs and Beyond: A Counting Approach*, SIAM Journal on Discrete Mathematics 22 (2008), 1297–1324, DOI:10.1137/07068686X.

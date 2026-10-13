# A sharp arity threshold for graded-versus-ordinary bisimulation compression of regular trees

## Finding

**Theorem (maximal quotient separation).** Let \(q\ge2\) be fixed. Let \(T_{q,h}\) be the complete rooted \(q\)-ary tree of height \(h\), with edges oriented away from the root, and let every vertex receive one of two colors. Write \(B(T)\) for the number of classes of greatest color-preserving **ordinary bisimulation**, and \(G(T)\) for the number of classes of greatest color-preserving **graded (counting) bisimulation**. Put
\[
N_h=\frac{q^{h+1}-1}{q-1}.
\]
The following sharp dichotomy holds.

1. If \(q=2\), then \(G(T)=B(T)\) for **every** two-coloring and every \(h\).
2. If \(q\ge3\), then, as \(h\to\infty\),
\[
\max_{\text{two-colorings of }T_{q,h}}\frac{G(T)}{B(T)}
=\Theta_q\!\left(\frac{N_h}{(\log N_h)^2}\right).
\]
The lower bound is realized by two-colorings satisfying the *smallest possible ordinary footprint compatible with any counting separation*, namely
\[
B(T)=h+2,\qquad G(T)=\Theta_q\!\left(\frac{N_h}{\log N_h}\right).
\]
Moreover, if any coloring has \(B(T)=h+1\), then necessarily \(G(T)=h+1\). Thus the threshold at arity three is exact, and one additional ordinary type beyond the mandatory height classes suffices for asymptotically maximum graded-state complexity.

## Assumptions and scope

A vertex of residual height \(k\) is one with longest directed path to a leaf of length \(k\); the root has residual height \(h\). The binary color is a single propositional atom \(p\). Ordinary modal formulas use Boolean connectives and the existence modality \(\Diamond\). Graded formulas may additionally use \(\Diamond_{\ge m}\) for each positive integer \(m\): this modality holds at a vertex if at least \(m\) **distinct** successors satisfy its argument. On these finite trees, the infinity diamond adds no distinction. Ordinary bisimulation counts successor *types appearing*, whereas graded bisimulation counts successor *multiplicities by type*; the finite-depth characterizations follow from structural induction.

All asymptotic constants depend on fixed \(q\), never on \(h\). The maximum is over all vertex two-colorings, including those using just one color. These are equivalence-class cardinalities, not claims that the resulting quotient of a multigraph has exactly \(q\) outgoing edges per state. No ordered-child labels or parent modality are present.

## Proof

### 1. Rooted normal forms and the binary threshold

On a finite outward-directed tree, define rooted **plain types** bottom-up as \((\text{color},\text{set of child plain types})\). Define rooted **counting types** as \((\text{color},\text{multiset of child counting types})\). Induction on residual height, using the forth/back conditions (respectively the graded counting conditions), shows that equality of these codes is exactly greatest ordinary (respectively graded) bisimulation equivalence. A counting type always determines a plain type. Different residual heights cannot share even an ordinary type, since one satisfies a sufficiently long iteration of \(\Diamond\top\) and the other does not.

For \(q=2\), if a pair of child plain types has support of size one, the multiset consists of two copies of that type; if the support has size two, it consists of one copy of each. Thus the support uniquely determines the multiset. Assuming by induction that counting and plain types agree at height \(k\), they also agree at height \(k+1\). The leaf base case is immediate. Hence \(B(T)=G(T)\) in every binary regular tree, independent of coloring.

### 2. Universal counting quotient bound

Let \(t_k\) be the number of rooted counting types realizable on the complete \(q\)-ary subtree of height \(k\) with two colors. Child-position order is invisible to counting modalities, but child multiplicities are visible. Disjoint child subtrees can be chosen independently, hence
\[
t_0=2,\qquad t_{k+1}=2\binom{t_k+q-1}{q}.
\]
For fixed \(q\), there is \(C_q>0\) for which \(t_k\le\exp(C_q q^k)\) for every \(k\): indeed
\[
\log t_{k+1}\le q\log t_k+q\log(q+1)+\log2,
\]
so one may take \(C_q=\log2+(q\log(q+1)+\log2)/(q-1)\). There are exactly \(q^{h-k}\) vertices of residual height \(k\). Consequently
\[
G(T)\le\sum_{k=0}^{h}\min\{q^{h-k},t_k\}.
\]
Set \(K=\lfloor\log_q(h\log q/(4C_q))\rfloor\) when the argument is at least one. For \(k\le K\), the summands total at most \((h+1)q^{h/4}\); for \(k>K\), their total is at most a geometric tail \(O_q(q^{h-K})=O_q(q^h/h)\). The first part is \(o(q^h/h)\). Since \(N_h=\Theta_q(q^h)\) and \(h=\Theta_q(\log N_h)\), this proves
\[
G(T)=O_q(N_h/\log N_h).
\]
Every coloring also has \(B(T)\ge h+1\), because the \(h+1\) residual heights are pairwise modally distinguishable. Therefore, for fixed \(q\ge2\),
\[
\frac{G(T)}{B(T)}=O_q(N_h/(\log N_h)^2).
\]

### 3. A restricted family with very few plain types and many counting types

Fix \(q\ge3\). Color every nonleaf vertex zero and require *every* vertex of residual height one to have at least one zero-colored and at least one one-colored leaf child. These requirements are compatible because the corresponding groups of leaves are disjoint.

Every leaf has one of precisely two plain types. Every height-one vertex has the unique plain type \((0,\{0,1\})\). Inductively, every vertex of each positive residual height has exactly one plain type, since all its children have the same lower-height plain type. Therefore **every** coloring in this restricted family satisfies
\[
B(T)=h+2\quad(h\ge1).
\]

Let \(g_k\) be the number of counting types obtainable as the root of a restricted colored \(q\)-ary subtree of residual height \(k\). A height-one root is determined by the positive number of one-colored children, which can be any number from one through \(q-1\). At higher heights, the \(q\) child counting types may be chosen independently and repetitions are allowed, so
\[
g_1=q-1,\qquad g_{k+1}=\binom{g_k+q-1}{q}\quad(k\ge1).
\]
In particular \(g_2=\binom{2q-2}{q}\ge(q-1)^2\ge q+1\) for \(q\ge3\). The recurrence and \(\binom{u+q-1}{q}\ge u^q/q!\) give, with \(b_q=\log(q!)/(q-1)\) and \(\delta_q=\log g_2-b_q>0\),
\[
\log g_k\ge b_q+\delta_q q^{k-2}\quad(k\ge2).
\]
The strict positivity follows from \((q+1)^{q-1}>q!\). Thus \(g_k\ge\exp(c_q q^k)\) for \(k\ge2\), with \(c_q=\delta_q/q^2>0\).

For sufficiently large \(h\), choose
\[
k=\left\lceil\log_q\!\left(\frac{2h\log q}{c_q}\right)\right\rceil.
\]
Then \(k\le h\), \(q^k=\Theta_q(h)\), and \(g_k\ge q^{2h}\ge q^{h-k}\). There are \(q^{h-k}\) pairwise disjoint rooted subtrees of residual height \(k\). Assign a **different** restricted counting type to every one, using the \(g_k\) available types. Color all remaining internal vertices zero. Every height-one parent still sees both leaf colors, so the ordinary quotient stays exactly \(h+2\). At residual height \(k\) alone, the graded quotient has at least \(q^{h-k}=\Omega_q(q^h/h)=\Omega_q(N_h/\log N_h)\) classes. Combined with Section 2, its graded size is \(\Theta_q(N_h/\log N_h)\).

The ratio is therefore \(\Omega_q(N_h/(\log N_h)^2)\), matching the universal upper bound.

### 4. Sharpness of the extra ordinary type

Suppose \(B(T)=h+1\). Since distinct heights cannot be ordinarily bisimilar, there is exactly one plain type at each height. In particular all leaves have the same color, so they have one counting type. By induction, if all nodes at height \(k\) have the same counting type, each node at height \(k+1\) has \(q\) copies of that child type, and all have the same root color because they share the same plain type. Thus all vertices of each height also have one counting type. Hence \(G(T)=h+1\). Any genuine counting separation must have at least \(h+2\) ordinary classes, which the construction attains.

## Verification

Run `python3 verify.py` in a directory containing the included standalone script; it has no third-party dependencies. The verifier exhaustively enumerates all two-colorings of binary regular trees of heights zero through three and ternary regular trees of heights zero through two. For each coloring it compares bottom-up ordinary/graded types, checks graded refinement, and periodically cross-checks both partitions using an independent global fixed-point refinement. It constructs 14 further restricted-family witnesses for arities three, four and five, checks the predicted ordinary footprint and distinct graded types at the chosen level, and checks the starting strict-growth inequality for arities three through eleven.

The completed replay reports `VERIFY_OK exhaustive_colorings 41116 parameter_cases 7 independent_partition_comparisons 648 structured_witnesses 14 growth_threshold_checks 9`. For ternary height two, 2,808 of the 8,192 colorings exhibit a genuine partition difference, and the minimum ordinary quotient among them has four classes. For the constructed ternary height-nine witness, \(N_h=29524\), \(B(T)=11\), and \(G(T)=383\). These are **finite checks**, not proofs of the asymptotic theorem; the proof is the argument above.

## Relationship to prior work

Bellas Acosta and Venema develop graded modal logic, its infinity extension, and structural counting bisimulations, not the present extremal two-quotient tradeoff on uniformly branching finite trees. Otto characterizes graded modal logic using counting bisimulation and rooted-tree locality, without the arity threshold or sharp quotient-separation rate. Jacobs and Wißmann analyze generic efficient coalgebraic bisimilarity minimization; an algorithm for computing quotients does not imply this sharp family-specific ratio. Established tree-compression bounds, and an earlier direct ordinary-bisimulation bound for complete colored trees, concern single quotients rather than the simultaneous maximum **relative** size of counting and noncounting quotients under the same coloring. Those background notions, counting signatures, and finite-tree rooted-type recurrences are not claimed as inventions.

The proposed new claim is the sharp \(q=2\)/\(q\ge3\) phase boundary and \(\Theta_q(N_h/(\log N_h)^2)\) extremal ratio, attained with the smallest nontrivial ordinary quotient. Targeted literature and mathematical-result searches did not identify this particular statement. This negative evidence is not a guarantee of priority; an equivalent antecedent under coalgebraic set-versus-multiset language or unordered-tree compression terminology remains possible.

## Limitations

The theorem is for finite complete **uniformly branching**, outward-directed trees; it does not cover irregular outdegrees, ordered/labeled child positions, converse modalities, infinite models, bounded counting ranks below \(q\), or variable arity growing with height. The bound gives order of magnitude with \(q\)-dependent constants, not a limiting leading constant or an exact finite-height maximizer. Independent mathematical audit has not yet been performed.

## References

- Ignacio Bellas Acosta and Yde Venema, *Counting to Infinity: Graded Modal Logic with an Infinity Diamond*, *Review of Symbolic Logic* 17 (2024), 1–35; published online July 8, 2022. DOI: 10.1017/S1755020322000247. Full text: https://pure.uva.nl/ws/files/178706957/counting-to-infinity-graded-modal-logic-with-an-infinity-diamond.pdf
- Martin Otto, *Graded modal logic and counting bisimulation*, arXiv:1910.00039, first submitted September 30, 2019. https://arxiv.org/abs/1910.00039
- Jules Jacobs and Thorsten Wißmann, *Fast Coalgebraic Bisimilarity Minimization*, arXiv:2204.12368, first submitted April 26, 2022. https://arxiv.org/abs/2204.12368

# Sharp description-depth spectra in role-free local and global definite-description logics

## Finding

Fix an integer \(k\ge 0\) and a nonempty finite structure whose only nonlogical symbols are \(k\) unary predicates. Allow all Boolean concept operations and, separately, either the local definite-description constructor \(L(C)\) or the global constructor \(G(C,D)\), with the semantics defined below. Write \(T=2^k\). The following statements concern **pointed** finite structures, not sentence theories or arbitrary role-bearing interpretations.

**Local descriptions.** The numbers of distinct pointed theories at description depths \(0\), \(1\), and \(d\ge2\) are respectively
\[
\boxed{N^{L}_{k,0}=T,\qquad N^{L}_{k,1}=T(1+2^{T-1}),\qquad N^{L}_{k,d}=T(1+3^{T-1})\ (d\ge2).}
\]
Thus all local descriptions can be eliminated down to depth two. Both depth increases are strict when \(k\ge1\); when \(k=0\), depth one already suffices.

**Global descriptions.** The numbers of distinct pointed theories at depths \(0\) and \(d\ge1\) are
\[
\boxed{N^{G}_{k,0}=T,\qquad N^{G}_{k,d}=T(1+2\cdot3^{T-1}-2^{T-1})\ (d\ge1).}
\]
Thus all global descriptions can be eliminated down to depth one, and this depth is necessary for every \(k\ge0\).

At each indicated depth, the number of Boolean-equivalence classes of concepts is exactly \(2^{N^{L}_{k,d}}\), respectively \(2^{N^{G}_{k,d}}\). Every pointed theory in either language has a realizing finite model with at most \(\max\{2,2T-1\}\) elements. This bound is optimal simultaneously for the two languages.

## Assumptions and scope

Let \(\Delta\) be a nonempty finite domain. Each of the \(k\) unary predicates is interpreted as a subset of \(\Delta\); there are no relation symbols of positive arity beyond unary predicates, no individual names, nominals, universal role, counting operators, or background ontology. Boolean constructors act as set complement, intersection, and union. Every element has a unique atomic color \(\sigma\in\{0,1\}^{k}\), describing exactly which atomic predicates hold there. The formula \(\chi_\sigma\) denotes the Boolean conjunction defining that color; for \(k=0\), the sole color formula is \(\top\).

The local definite description denotes
\[
L(C)^{\mathcal I}=\begin{cases}C^{\mathcal I},&|C^{\mathcal I}|=1,\\ \varnothing,&\text{otherwise.}\end{cases}
\]
The global definite description denotes
\[
G(C,D)^{\mathcal I}=\begin{cases}\Delta,&C^{\mathcal I}=\{u\}\ \text{and}\ u\in D^{\mathcal I},\\ \varnothing,&\text{otherwise.}\end{cases}
\]
These coincide with the local \(\{\iota C\}\) and global \(\iota C.D\) operators used in the cited work. The **description depth** counts the maximum number of description operators on any root-to-leaf syntactic path, taking depth one plus the maximum argument depth at each description operator. Two pointed models are depth-\(d\) equivalent when they agree on all Boolean concepts of description depth at most \(d\).

Write \(c_\sigma=\min\{2,|\chi_\sigma^{\mathcal I}|\}\in\{0,1,2\}\) and let \(\tau\) be the color of the distinguished point. By \(\operatorname{supp}(c)\) we mean the colors with \(c_\sigma>0\).

## Proof

**1. Color homogeneity and truncation.** Every permutation of the domain preserving colors is an automorphism of the Boolean structure and of both description constructors. By structural induction, each concept therefore denotes a union of entire color classes. If a concept selects the color set \(S\), its extension is a singleton exactly when exactly one selected color has \(c_\sigma=1\) and all other selected colors have \(c_\rho=0\). Consequently, the complete vector \(c\) together with the pointed color \(\tau\) determines the truth of every formula under either semantics, with arbitrary description nesting. Explicitly, Boolean cases update the selected set \(S\); \(L(C)\) updates it to the unique selected singleton color or to the empty set; \(G(C,D)\) updates it to all colors or to none, according to the same singleton test and the truth of \(D\) at that color. These recursion rules never inspect a count beyond two.

**2. Local depth zero and the collapse at nonsingleton points.** At depth zero, concepts are exactly Boolean combinations of color predicates; the pointed color \(\tau\) is the full invariant. If \(c_\tau=2\), then \(L(C)\) is false at the point for every \(C\), irrespective of nesting: a singleton concept extension cannot contain any element of a color class having at least two members. By structural induction, replacing every local-description subformula by \(\bot\) gives its value at such a point. Thus all nonsingleton points of color \(\tau\) share one full local theory, regardless of what other colors occur.

**3. Local depth one.** At a singleton point of color \(\tau\), a depth-one description \(L(C)\) has a depth-zero Boolean argument, hence a union of colors. Its truth depends only on which *other* colors are absent; multiplicities one and two are not distinguished. The formulas \(L(\chi_\tau\vee\chi_\sigma)\) for \(\sigma\ne\tau\) test the absence of \(\sigma\), while \(L(\chi_\tau)\) identifies singletonhood of the distinguished color. These formulas, with the atomic-color formulas, separate exactly \(2^{T-1}\) singleton-point profiles for each \(\tau\), plus one nonsingleton-point profile. Hence \(N^L_{k,1}=T(1+2^{T-1})\).

**4. Local depth two.** Suppose \(c_\tau=1\) and \(\sigma\ne\tau\). The depth-one test \(L(\chi_\tau\vee\chi_\sigma)\) detects \(c_\sigma=0\). The depth-two test
\[
L\bigl(\chi_\tau\vee(\chi_\sigma\wedge\neg L(\chi_\sigma))\bigr)
\]
is true at the \(\tau\)-point precisely when \(c_\sigma\in\{0,1\}\), and false when \(c_\sigma=2\). Together these tests distinguish all three values of every other coordinate of \(c\). This yields \(3^{T-1}\) singleton-point signatures for each \(\tau\) and the one nonsingleton signature from step 2. Step 1 proves that no deeper formula refines the partition. Hence \(N^L_{k,d}=T(1+3^{T-1})\) for \(d\ge2\).

**5. Global description collapse without an anchor.** If no color class is a singleton, every Boolean concept selects a union of classes of sizes zero or at least two. An induction on nested concepts shows that no concept has a singleton extension. Every \(G(C,D)\) consequently denotes \(\varnothing\). At a distinguished color \(\tau\), all such models therefore have the same global theory, independently of any other occupied colors.

**6. One global description detects the complete profile when an anchor exists.** Suppose \(c_\rho=1\) for at least one color \(\rho\). Depth-one concepts \(G(\chi_\sigma,\top)\) detect exactly which colors have size one. In particular, they identify a singleton anchor \(\rho\). For \(\sigma\ne\rho\), the depth-one concept \(G(\chi_\rho\vee\chi_\sigma,\top)\) holds exactly when \(c_\sigma=0\); any remaining color has size at least two. The pointed color \(\tau\) is observed by its atomic formula. Thus depth one detects the full vector \(c\) whenever at least one singleton exists, and step 1 shows deeper operators cannot improve this distinction. For each fixed pointed \(\tau\), either (a) \(c_\tau=1\), allowing \(3^{T-1}\) choices of the other coordinates, or (b) \(c_\tau=2\) and at least one other coordinate equals one, allowing \(3^{T-1}-2^{T-1}\) choices, or (c) there is no singleton, giving one collapsed class. Summing yields \(N^G_{k,d}=T(1+2\cdot3^{T-1}-2^{T-1})\) for \(d\ge1\).

**7. Sharpness, formula-class counts, and smallest representatives.** All profile choices used above are realized by a finite model having respectively zero, one, or two elements of each color; take the point in color \(\tau\). The distinguishing tests in steps 3, 4, and 6, together with Boolean operations, construct a characteristic concept for *each* pointed signature: conjoin appropriate tests or their negations, and the pointed-color formula. Therefore every subset of signatures is definable by a disjunction, and different subsets are inequivalent. This proves the powers-of-two formula-class counts. When \(T\ge2\), the depth-one local signatures distinguish absence from presence of any other color and depth two distinguishes singleton from multiple presence, so the two inclusions in the local depth hierarchy are strict; global depth zero cannot distinguish the two nonempty one-color multiplicities, but depth one can, proving sharpness for every \(k\ge0\).

For the representative bound, nonsingleton-point local theories and anchor-free global theories have a two-point representative consisting solely of two points of the distinguished color. Any remaining (local-singleton or anchored global) theory is represented by realizing its vector \(c\) with precisely \(0,1,2\) elements of each color. As some color is a singleton, the total size is at most \(1+2(T-1)=2T-1\). For \(T=1\), two worlds are needed for the nonsingleton theory. For \(T\ge2\), choose a singleton distinguished color \(\tau\) and two elements in each other color. Every coordinate of this vector is detectable by local depth-two and global depth-one concepts, so no equivalent finite representative for either language can have fewer than \(2T-1\) elements. This proves sharpness.

## Verification

The accompanying executable `rolefree_dd_checker.py` evaluates the *original set semantics* of the local and global constructs, not the closed-form theory counts as a substitute for semantics. It exhaustively enumerates all truncated color-count vectors \(c\in\{0,1,2\}^{T}\), all possible pointed colors, and explicit separating concepts for \(k=0,1,2\). It compares their observed truth vectors with the predicted signatures at all relevant depths. An additional deterministic seeded experiment evaluates arbitrarily nested randomly generated concepts after increasing non-singleton multiplicities while preserving truncated counts, in \(48{,}000\) comparisons. It reports no counterexamples. These are finite checks only; the unrestricted proof is in the preceding steps.

Representative pointed-theory counts from these tests are: for \(k=0\), local \(1,2,2\), global \(1,2\); for \(k=1\), local \(2,6,8\), global \(2,10\); and for \(k=2\), local \(4,36,112\), global \(4,188\).

Run the standalone script with Python 3 using `python3 rolefree_dd_checker.py`; it requires only the standard library. Its final success line is `ROLEFREE_DD_CHECKS_OK pointed_comparisons= 1725`.

## Relationship to prior work

Sochański, Wałęga, and Zawidzki introduced the local/global description constructs and established general bisimulation conditions and expressive-power relations for description logics with roles (Theorems 6 and 7), as well as a finite-model upper bound depending on the concept size (Theorem 17). The present theorem treats a sharply specified role-free fragment and yields exact finite pointed-theory spectra, the optimal depth at which nesting becomes redundant, finite Boolean-algebra cardinalities of definable concepts, and an optimal uniform model bound depending only on the number of predicates. These quantitative conclusions are not statements of the inspected theorems; the general bisimulation results provide relevant conceptual context but do not by themselves state the closed forms.

Artale, Mazzullo, Ozaki, and Wolter investigated local definite descriptions with additional nominals and the universal role. Their expressiveness analysis shows the importance of distinguishing singleton and nonsingleton color classes; those extra symbols change what is globally observable. Accordingly, no conclusion here is asserted for their richer language, for arbitrary roles, or for ontological background axioms. Earlier generic results about monadic Boolean algebras or finite-variable logics may admit an equivalent specialization; that historical-priority possibility remains open.

## Limitations

This is a classification of concept semantics over finite nonempty role-free structures only; it says nothing about universal-role, relational, nominal, or ontology-constrained extensions. The formulas count equivalence classes over the indicated class of finite models, not syntax trees, theorem-proof counts, or the number of finite structures. The depth bounds are semantic existence results and do not promise polynomial-size translations. The exhaustive experiments cover \(k\le2\), with additional randomized larger-\(k\) checks; those experiments do not exhaust all formulas of arbitrary depth. The self-review has not been independently audited. An equivalent older specialization of general bisimulation/counting theory cannot be excluded by search alone.

## References

1. M. Sochański, P. A. Wałęga, M. Zawidzki, *Description Logics with Two Types of Definite Descriptions: Complexity, Expressiveness, and Automated Deduction*, arXiv:2512.06604 (first posted 2025-12-07); AAAI 2026, DOI 10.1609/aaai.v40i23.39014. https://arxiv.org/abs/2512.06604
2. A. Artale, A. Mazzullo, A. Ozaki, F. Wolter, *On Free Description Logics with Definite Descriptions*, arXiv:2106.15513 (2021). https://arxiv.org/html/2106.15513v1

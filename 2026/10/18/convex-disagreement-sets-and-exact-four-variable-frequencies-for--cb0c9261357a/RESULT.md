# Convex disagreement sets and exact four-variable frequencies for positive formulas

## Finding

Let \(k\geq1\). In classical two-valued propositional logic consider nonempty formulas built only from the positive variables \(p_1,\ldots,p_k\), conjunction, and disjunction, with **no nullary constants**. For formulas \(\varphi,\psi\), define their disagreement set \(D(\varphi,\psi)=\{a\in\{0,1\}^k:\varphi(a)\ne\psi(a)\}\).

**Exact disagreement-set theorem.** A subset \(D\subseteq\{0,1\}^k\) occurs as \(D(\varphi,\psi)\) if and only if it omits the all-zero and all-one assignments and is order-convex for coordinatewise order: whenever \(a\leq b\leq c\) and \(a,c\in D\), then \(b\in D\). Thus the possible equality sets are exactly complements of those convex subsets.

The first genuinely restrictive arity is \(k=4\). For \(k\leq3\), every subset of nonextreme assignments is a possible disagreement set. At \(k=4\), only \(3605\) of the \(2^{14}=16384\) subsets of the fourteen nonextreme assignments are possible. More generally, if \(C_k\) counts order-convex subsets of the Boolean lattice and \(M_k\) is the Dedekind number (the number of upsets), then the number of distinct disagreement sets equals \(C_k-2M_k+3\).

For fixed \(k\geq2\), the agreement probabilities of all formula pairs are exactly \(j/2^k\) for each integer \(2\leq j\leq2^k\). Across all positive arities the entire equational probability spectrum of this two-operation propositional fragment is the set of strictly positive dyadic rationals no larger than one, with zero as an unattained infimum.

**Complete four-variable frequency refinement.** There are exactly \(166\) distinct four-variable term functions. For ordered formula-function pairs, the number at each disagreement distance \(d=|D|\) is:

| \(d\) | Ordered function pairs |
|---:|---:|
| 0 | 166 |
| 1 | 904 |
| 2 | 2560 |
| 3 | 4616 |
| 4 | 5824 |
| 5 | 5312 |
| 6 | 3736 |
| 7 | 2176 |
| 8 | 1188 |
| 9 | 568 |
| 10 | 296 |
| 11 | 136 |
| 12 | 56 |
| 13 | 16 |
| 14 | 2 |
| **Total** | **27556** |

This is an ordered-pair census of *term functions*, not a syntactic count of infinitely many formulas. The two pairs at distance fourteen are the two orientations of full conjunction versus full disjunction. For \(k\geq3\), those remain the only ordered pairs that disagree on every nonextreme assignment.

## Assumptions and scope

All valuations are classical \(\{0,1\}\)-valued, assignments are equipped with coordinatewise inclusion order, and the signature contains binary \(\wedge\), binary \(\vee\), and variables only. Variables may be semantically inessential, so the arity is the ambient list of allowable variables; any inessential variable can also be introduced syntactically by absorption without changing the function. We count *functionally distinct* pairs, not presentation-dependent formula pairs.

Write \(\bot=(0,\ldots,0)\) and \(\top=(1,\ldots,1)\), and call \(U\) an upset when \(a\in U\) and \(a\leq b\) imply \(b\in U\). The symbol \(\uparrow D\) means the upward closure of \(D\) in the assignment poset. An order-convex set is not convex in the Euclidean-linear sense; this distinction matters.

## Proof

**Term-function characterization.** Every positive formula is isotone, takes value zero at \(\bot\), and takes value one at \(\top\), by induction. Conversely, any isotone Boolean function satisfying these endpoint values has a nonempty family \(\mathcal M\) of minimal true assignments, all of which are nonempty subsets of variables. Its monotone disjunctive normal form \(\bigvee_{S\in\mathcal M}\bigwedge_{i\in S}p_i\) is an allowed formula. Hence the term functions are exactly the characteristic functions of upsets \(U\) with \(\bot\notin U\) and \(\top\in U\).

**Necessity.** Suppose \(a\leq b\leq c\) and both endpoints belong to \(D(\varphi,\psi)\). At \(a\) the truth-value pair must be either \((1,0)\) or \((0,1)\). In the first case monotonicity forces \(\varphi(b)=\varphi(c)=1\). Since \(c\) is also a disagreement, \(\psi(c)=0\), and therefore \(\psi(b)=0\). Hence \(b\in D\). The second case is symmetric. Both formulas agree at \(\bot\) and \(\top\), so those points cannot be in \(D\).

**Sufficiency.** Let \(D\) be nonempty, order-convex, and avoid \(\bot,\top\). Put \(U=\uparrow D\), \(V=U\setminus D\). Both are upsets: if \(x\in V\) and \(x\leq y\in D\), the definition of \(U\) supplies \(d\in D\) with \(d\leq x\leq y\); convexity would force \(x\in D\), contradiction. Both \(U,V\) contain \(\top\) and omit \(\bot\); the former follows since \(D\) is nonempty and does not include \(\top\). Their symmetric difference is exactly \(D\), so characteristic formulas for \(U,V\) realize it. If \(D=\varnothing\), take the same nonconstant positive formula twice.

**First obstruction and counts.** Removing both extremes from the \(k\)-cube leaves no chain of length three when \(k\leq3\), so every subset is convex. In dimension four the two assignments with true-variable sets \(\{1\}\) and \(\{1,2,3\}\) cannot be the *only* disagreements, since the intermediate assignment \(\{1,2\}\) would have to disagree as well. The same example persists in all higher dimensions. A convex set containing \(\bot\) is exactly a nonempty order ideal, and one containing \(\top\) is exactly a nonempty upset; there are \(M_k-1\) of each. Their intersection among convex sets is just the whole cube. Inclusion-exclusion yields \(C_k-2M_k+3\). At \(k=4\), previously enumerated totals \(C_4=3938\) and \(M_4=168\) give \(3605\). The independent exhaustive checker below also derives this directly.

**Sharp probability spectrum.** Both extremes satisfy every equation, hence agreement counts are at least two. Let \(\varphi=\bigwedge_{i=1}^k p_i\), so its true upset is exactly \(\{\top\}\). For any integer \(m\in\{1,\ldots,2^k-1\}\), choose an upset of size \(m\) containing \(\top\) and avoiding \(\bot\): order the cube in nonincreasing Hamming weight, breaking ties arbitrarily, and take the first \(m\) assignments. A positive formula \(\psi\) represents its indicator. The equality set of \(\varphi,\psi\) then has \(2^k-m+1\) assignments, yielding all counts from two through \(2^k\). For \(k=1\) only the identity function exists and agreement is always one. For any positive dyadic rational \(r=t/2^s\leq1\), doubling numerator and denominator sufficiently produces \(2\leq2^j t\leq2^{s+j}\), so it occurs at a larger arity; zero never does.

**Unique maximum disagreement for \(k\geq3\).** When \(D\) is the entire nonextreme part of the cube, the orientation \((\varphi(a),\psi(a))\in\{(1,0),(0,1)\}\) must be constant on every pair of comparable interior assignments, by monotonicity. The comparability graph of the nonextreme assignments is connected for \(k\geq3\): every interior non-singleton lies above a singleton, and any two singletons have a two-element superset strictly below \(\top\). Thus all orientations agree, giving precisely conjunction versus disjunction and its reversal. For \(k=2\), the interior points are incomparable, and there are four maximally distant ordered pairs.

**Exact finite four-variable distance counts.** Each allowed function is represented by a sixteen-bit word, with bit \(a\) its value at assignment \(a\). The checker loops through all \(2^{16}=65536\) such words and retains those with false bottom, true top, and monotonicity on every covering edge. This is a necessary-and-sufficient test for every word, yielding exactly 166 functions. It computes \(\operatorname{popcount}(f\oplus g)\) on all \(166^2=27556\) ordered pairs, producing the displayed fifteen-cell histogram. An independently organized recursive enumeration by monotone lower/upper Boolean slices reproduces the same 166 words and all counts. Independently testing all \(2^{14}\) subsets of the nonextreme four-cube for order convexity yields 3605 and matches exactly the distinct disagreement masks of the pairs. These are exhaustive finite calculations, not an extrapolation to larger arities.

## Verification

Run `python3 verify_positive_equations.py` with Python 3.8 or later, using only the standard library. It independently constructs four-variable monotone functions by (i) scanning all Boolean truth tables and checking covering edges, and (ii) recursively composing monotone lower and upper slices. It checks equality of these function families, computes the complete ordered-pair Hamming-distance histogram, and independently matches realizable disagreement masks to all order-convex subsets through arity four. Expected final line: `POSITIVE_EQUATIONAL_CONVEXITY_VERIFY_OK`. The general-arities claims are proved above and are not inferred solely from this finite computation.

## Relationship to prior work

Dvorkin's 2026 investigation of monotonicity and positive formulas explicitly recalls that every monotone Boolean function is expressible by conjunction, disjunction, and constants (Introduction, §1), and studies the Lyndon positivity property in modal logic. The present result asks a **different and finer classical propositional question**: for the naturally constant-free positive signature, on which assignments may *two* such formulas disagree, and with what exact multiplicities? Dvorkin's results about positivity and modal interpolation do not establish the order-convex pairwise disagreement realization, the exact dyadic agreement spectrum, or the four-variable distance enumerator. Omitting constants is essential to the endpoint conditions: allowing constants changes the classification. The primary mathematics here is the semantics of classical positive propositional formulas, not a claim about modal logic.

Cardó's 2026 investigation of equation probabilities establishes a general framework and gives the density of the spectrum for the two-element \(\{\wedge,\vee\}\)-algebra (Example 6.4), but does not provide the exact equality-set characterization, its sharp first obstruction at four variables, or the four-variable pair-frequency refinement. The monotone term-function characterization here is established directly, without assuming any broader functional-completeness property.

The classical Dedekind numbers and the enumeration of interval-closed sets of Boolean lattices are prior mathematics; in particular, the values 168 and 3938 used as count cross-checks are not new. Elder, Lafrenière, McNicholas, Striker, and Welch study interval-closed sets and rowmotion; this finding's semantic equivalence with positive-formula disagreements and its weighted ordered-pair frequencies are different assertions. Fihman, Van Hirtum, and Plessl analyze Hamming distances of monotone Boolean functions as a sampling diagnostic at much higher dimensions, but do not give this exact sixteen-assignment distance distribution. The available sources do not establish absolute historical priority for the combined claim.

## Limitations

This theorem concerns the classical no-constants positive fragment with both conjunction and disjunction; it is not a classification for negation, implication, constants, or alternative semantics. The spectrum statement concerns **existence** of formula pairs, whereas the finite histogram counts distinct term-function pairs. The four-variable histogram is specific to four variables; the general convexity characterization does not supply closed-form distance enumerators for all arities. Earlier equivalent statements under different order-theoretic terminology may exist, so independent novelty verification remains appropriate.

## References

1. Lev Dvorkin, *Monotonicity versus positivity in modal logics*, arXiv:2602.02837 (first public version 2026-02-02), Introduction §1 and §3 on positive formulas.
2. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446 (first public version 2026-04-09), especially Example 6.4 and §5.
3. Alex Fihman, Lennart Van Hirtum, and Christian Plessl, *Statistical Estimation of higher Dedekind Numbers*, arXiv:2607.08446 (first public version 2026-07-09), especially §3.4 and Appendix A.
4. Jennifer Elder, Nadia Lafrenière, Erin McNicholas, Jessica Striker, and Amanda Welch, *Toggling, rowmotion, and homomesy on interval-closed sets*, arXiv:2307.08520; *Journal of Combinatorics* 15 (2024), 479–528.
5. OEIS A369313, *Number of interval-closed sets in the boolean lattice of dimension n*; OEIS A000372, *Dedekind numbers*.

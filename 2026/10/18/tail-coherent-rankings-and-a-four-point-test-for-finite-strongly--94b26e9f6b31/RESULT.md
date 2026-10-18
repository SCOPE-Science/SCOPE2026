# Tail-coherent rankings and a four-point test for finite strongly dense selection frames

## Finding

Let \(W\) be a finite nonempty set. Consider a total, centered, functional selection frame: for each \(w\in W\) and nonempty \(A\subseteq W\) there is exactly one selected point \(f_w(A)\in A\), and \(f_w(A)=w\) whenever \(w\in A\). The frame is **strongly dense** when, for every \(w\in W\) and nonempty \(C\subseteq A\subseteq W\),
\[
 f_w(C)=f_{f_w(A)}(C). \tag{SD}
\]

**Classification theorem.** Strong density holds if and only if there is a unique family \((\prec_w)_{w\in W}\) of strict total orders, each with \(w\) as its first element, such that \(f_w(A)\) is the \(\prec_w\)-least member of \(A\) and the family obeys the following **four-point condition** for pairwise distinct \(w,u,v,z\):
\[
 u\prec_w v\prec_w z\quad\Longrightarrow\quad v\prec_u z. \tag{FP}
\]
Equivalently, for every \(w,u\), the order \(\prec_u\) restricted to the suffix \(\{x:u\preceq_w x\}\) coincides with the restriction of \(\prec_w\) to that suffix. Thus a strong-density test on a general family of subset selections becomes an \(O(|W|^4)\) comparison test once its ranking representation has been established.

The numbers of such frames on a fixed labelled set and the numbers of isomorphism classes, respectively, for \(|W|=1,2,3,4,5\), are
\[
 (1,1),\ (1,1),\ (8,2),\ (138,7),\ (3984,34).
\]
In particular, the first nontrivial four-point restrictions occur at four worlds. The isomorphism action relabels the worlds simultaneously in their indices and in every ranking.

## Assumptions and scope

A selection family is *total* when a choice is made for every nonempty antecedent at every world; *functional* when there is exactly one choice; *successful* when the chosen world lies in its antecedent; and *centered* when the base world, if in the antecedent, is always selected. The empty antecedent has no selected successor. No linear or tree ordering on the underlying worlds is assumed. The strong-density condition is the finite functional specialization of relational strong density \(wR_Cv\Rightarrow \exists u\,(wR_Au\land uR_Cv)\) whenever \(C\subseteq A\), where \(wR_Au\) means \(f_w(A)=u\).

The result classifies **all finite sizes**; the displayed exact counts are exhaustively certified only for sizes one through five. No unstated formula for their entire counting sequence is asserted. Conditional-algebra interpretation uses the additional totality assumption and the standard powerset operation \(A\mathbin{\Rightarrow}B=\{w:f_w(A)\in B\}\) for nonempty \(A\), with \(\varnothing\mathbin{\Rightarrow}B=W\).

## Proof

**1. Strong density forces contraction consistency.** Suppose \(u=f_w(A)\in C\subseteq A\). Equation (SD) and centering at \(u\) give \(f_w(C)=f_u(C)=u\). Call this property (CC). It holds for every nonempty \(C\subseteq A\) containing the winner \(u\).

**2. Every finite (CC) choice function is uniquely induced by a ranking.** Fix \(w\). On any two distinct elements define \(v\prec_w z\) precisely when \(f_w(\{v,z\})=v\). This produces a tournament. If three vertices formed a cyclic triangle, the chosen element of the three-element set, together with (CC), would beat the other two, contradicting the triangle. Therefore the tournament has no directed triangle. A tournament with no directed triangle is transitive: if \(a\prec_w b\) and \(b\prec_w c\), the contrary \(c\prec_w a\) would make a directed triangle. The resulting total order is unique. For any nonempty \(A\), (CC) says its selected element precedes every other element in \(A\); hence it is the unique least element. Since centering chooses \(w\) whenever \(w\in A\), \(w\) comes first.

**3. Strong density implies (FP).** Assume \(u\prec_w v\prec_w z\) with four pairwise distinct elements. Let \(A\) be the \(\prec_w\)-suffix beginning at \(u\), so \(f_w(A)=u\). Take \(C=\{v,z\}\subseteq A\). Since \(v\prec_w z\), (SD) gives \(f_u(C)=f_w(C)=v\), i.e. \(v\prec_u z\).

**4. (FP) implies strong density.** Fix \(w\), nonempty \(C\subseteq A\), and put \(u=f_w(A)\). If \(u\in C\), then \(f_w(C)=u=f_u(C)\) because \(u\) is first in \(\prec_u\). Otherwise, if \(u=w\), equation (SD) is tautological. In the remaining case \(u\ne w\), centering forces \(w\notin A\), so all four points below are distinct. Every element of \(C\) is strictly later than \(u\) in \(\prec_w\). For any distinct \(v,z\in C\), (FP) (with its four pairwise distinct elements) says that whichever precedes the other under \(\prec_w\) also precedes the other under \(\prec_u\). Consequently these orders agree on \(C\), and their minima coincide. This proves (SD).

**5. Suffix formulation and algorithm.** Step 3 applies to every pair of distinct points strictly after \(u\) in \(\prec_w\); the fact that \(u\) is first in \(\prec_u\) handles comparisons with \(u\). Thus (FP) is precisely equality of the two orders on the suffix from \(u\). Conversely such equality immediately implies (FP). Four nested point choices, with constant-time inverse-rank comparisons, test all instances in polynomial time.

**6. Exact finite enumeration.** Each \(\prec_w\) can be encoded by a permutation starting with \(w\), so there are \(((n-1)!)^n\) initially possible labelled ranking profiles. The standalone `verify.py` enumerates these profiles up to label symmetry, applies (FP), and computes their permutation orbits. For the equivalence of (FP) with the literal (SD) subset condition it independently checks *all* ranking profiles through four worlds. At four worlds, the independent `verify_direct.c` enumerates every possible centered total functional selection table without assuming ranking representability: each base world has \(2^3\cdot3=24\) possibilities, so the whole space contains \(24^4=331776\) tables. Exactly \(138\) satisfy (SD). This independently agrees with the order-profile census.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. Its last line is `VERIFY_OK`. It reports labelled/isomorphism counts for one through five worlds and checks literal density against (FP) on all ranking profiles through four worlds. Independently compile `verify_direct.c` using `cc -O3 -std=c11 verify_direct.c -o verify_direct`, then execute `./verify_direct`; the expected final line is `raw=331776 dense=138`. The C program does not use the ranking theorem in its enumeration.

These finite computations reproduce the displayed coefficients but do not substitute for the proof for arbitrary finite \(W\).

## Relationship to prior work

Holliday's *Preconditionals* (first publicly available February 2024) defines strong-density selection frames and proves soundness (Proposition 15) and a finite-Boolean representation theorem (Proposition 16) for preconditionals satisfying modus ponens, identity, normality, and **Boolean-complement** negation import. Those are the source axioms and representation results, not new claims here. The extra assumption that every nonempty antecedent is selected at every world corresponds to the nonvacuity law \(A\ne\varnothing\Rightarrow A\mathbin{\Rightarrow}\varnothing=\varnothing\). Thus the theorem offers a concrete ranking-based and finite forbidden-pattern parametrization of this nonvacuous, functional, centered subclass. In particular, the argument gives a finite selection-frame description rather than a representation theorem for all Boolean preconditionals.

Related enumerations of preconditional expansions of finite **chains** do not establish a classification for Boolean powerset algebras, whose selection-frame carriers have incomparable atoms and choice restrictions across all nonempty subsets. The present count is not derived from those chain formulas.

## Limitations

The class is deliberately restricted to finite, total, functional, centered, successful selection frames. This does not enumerate all strongly dense (possibly nonfunctional or partial) selection frames or all finite Boolean preconditionals. The five-world numbers are finite exhaustive outputs, not a closed-form enumeration for all sizes. Strong density of arbitrary selection tables must first imply ranking representability; (FP) alone is not meaningful before this step. Earlier equivalent descriptions may exist in literature using rationalizable choice, conditional belief, or Lewis/Stalnaker sphere terminology. No independent mathematical audit has been performed.

## References

1. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296 (first posted 3 February 2024), https://arxiv.org/abs/2402.02296 ; full HTML https://arxiv.org/html/2402.02296v2 , especially Definition 13 and Propositions 15–16.
2. E. Boylan and M. Mandelkern, *Logic and information sensitivity*, ESSLLI lecture notes (2022), https://mandelkern.hosting.nyu.edu/ESSLLI2022Day3.pdf (not obtained for full-text comparison).

# Quadratic average one-point type growth over random finite weak orders

## Finding

Let \(\mathbb U\) be the countable universal homogeneous strict partial order. Choose uniformly at random a weak order \(P_n\) on the labelled set \(\{1,\ldots,n\}\), meaning an ordered sequence of nonempty antichains, and regard it as an induced parameter subposet of \(\mathbb U\). Write \(T(P_n)\) for the number of complete nonalgebraic one-types over its named parameters in \(\operatorname{Th}(\mathbb U)\), and \(O(P_n)\) for their number of orbits under the induced action of \(\operatorname{Aut}(P_n)\). Then, with \(\rho=\log 2\),

\[
\mathbb E T(P_n)=\frac{n^2}{2\rho^2}+O(n),\qquad
\mathbb E O(P_n)=\frac{n^2}{2}+O(n),\qquad
\lim_{n\to\infty}\frac{\mathbb E T(P_n)}{\mathbb E O(P_n)}=\frac1{(\log 2)^2}.
\]

These are ratios of two expectations, not an asserted almost-sure ratio. The two exact exponential generating functions below also compute all finite expectations.

## Assumptions and scope

All posets are strict, finite parameter sets carry their given labels, and the random weak order ranges uniformly over all ordered partitions of the labelled \(n\)-element set. The empty weak order is included only in generating-function normalization. The ambient countable poset has the one-point extension property and eliminates quantifiers; thus each consistent one-point comparison pattern corresponds to a distinct complete nonalgebraic one-type. Orbit counts are taken under automorphisms of the finite parameter subposet (equivalently, automorphisms of \(\mathbb U\) acting setwise on that parameter set), not pointwise stabilizers.

For an individual weak order \(P=A_1\oplus\cdots\oplus A_h\) with \(n_i=|A_i|\ge1\), put \(a_i=2^{n_i}-1\). The exact type and symmetry-orbit counts are

\[
T(P)=1+2\sum_i a_i+\sum_{i<j}a_i a_j,
\qquad O(P)=1+2\sum_i n_i+\sum_{i<j}n_i n_j.
\]

Define \(B(z)=e^z-1\), \(A(z)=e^{2z}-e^z\), \(C(z)=ze^z\), and \(W(z)=1/(1-B(z))=1/(2-e^z)\). The exponential generating functions enumerating the **totals** of \(T(P)\) and \(O(P)\) over all labelled weak orders, including the empty order, are respectively

\[
F_T(z)=W(z)+2A(z)W(z)^2+A(z)^2W(z)^3,
\qquad F_O(z)=W(z)+2C(z)W(z)^2+C(z)^2W(z)^3.
\]

Thus \(\mathbb E T(P_n)=[z^n]F_T(z)/[z^n]W(z)\) and likewise for \(O\), for all \(n\ge1\).

## Proof

**Types and finite block counts.** For a new world \(x\), let \(L=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). Transitivity forces \(L\) to be a downset, \(U\) an upset, and every member of \(L\) strictly below every member of \(U\). Conversely, these conditions make a one-point partial-order extension, and the extension property realizes it in \(\mathbb U\). Ultrahomogeneity and quantifier elimination make the ternary comparisons complete and mutually distinguishing as types. In a weak order, a nonempty \(L\) is all levels below its highest occupied level together with a nonempty subset there; a nonempty \(U\) is dually a nonempty subset in its lowest occupied level together with all higher levels. If both occur, the chosen levels must be strictly ordered, yielding exactly the four cases: neither boundary; only a lower boundary; only an upper boundary; or an ordered pair of lower and upper boundary levels. Each boundary subset in level \(i\) has \(a_i\) choices. This proves the formula for \(T(P)\). Since \(\operatorname{Aut}(P)=\prod_i S_{n_i}\), a nonempty subset of level \(i\) has exactly \(n_i\) orbits, classified by cardinality. This proves the formula for \(O(P)\).

**Labelled generating functions.** A weak order is an ordered sequence of nonempty labelled blocks, with block EGF \(B(z)\), so its EGF is \(W(z)\). A block together with a nonempty distinguished subset is counted by \(A(z)\): a block of size \(k\) contributes \(2^k-1\) choices. For the orbit statistic, a distinguished cardinality from \(1\) to \(k\) gives \(k\) choices, hence block EGF \(C(z)\). For each statistic, an empty boundary set contributes \(W\); exactly one of the two possible boundary kinds contributes \(2AW^2\) (respectively \(2CW^2\)); and an ordered pair of opposite boundaries contributes \(A^2W^3\) (respectively \(C^2W^3\)). The labelled product and sequence rules give the two stated EGFs without overlap.

**Dominant singularity.** The poles of \(W(z)\) occur at \(z=\rho+2\pi i k\), \(k\in\mathbb Z\); the unique nearest pole is the positive real \(\rho=\log2\). Around it, with \(u=\rho-z\),

\[
W(z)=\frac1{2u}+O(1),\qquad A(z)=2+O(u),\qquad C(z)=2\rho+O(u).
\]

Consequently \(F_T(z)=1/(2u^3)+O(u^{-2})\) and \(F_O(z)=\rho^2/(2u^3)+O(u^{-2})\). The isolated-pole coefficient formula yields

\[
[z^n]W(z)=\frac12\rho^{-n-1}(1+o(1)),
\quad [z^n]F_T(z)=\frac12\binom{n+2}{2}\rho^{-n-3}+O(n\rho^{-n-3}),
\]

and \([z^n]F_O(z)=\frac{\rho^2}{2}\binom{n+2}{2}\rho^{-n-3}+O(n\rho^{-n-3})\). The farther complex poles make exponentially smaller contributions than the displayed leading singularity. Division proves both mean laws with \(O(n)\) errors and their limiting ratio.

## Verification

The standalone `verify.py` independently enumerates ternary comparison assignments for every ordered positive block-size composition with up to eight points and at most five levels, deduplicates them by within-level permutation signatures, and checks the two individual-poset formulas. It then compares the EGFs' exact coefficients against direct labelled ordered-partition enumeration through ten points. The checked output includes `VERIFY_OK` and `EGF_VERIFY_OK`. These finite computations support the normal forms; they do not replace the infinite singularity proof.

## Relationship to prior work

The countable homogeneous poset and its one-point-extension property are classical. A published classification of finite-parameter one-types for arbitrary finite posets already describes them by downset/upset pairs. That generic description is used as input, not claimed as novel. Elder, Lafrenière, McNicholas, Striker and Welch explicitly count interval-closed subsets of ordinal sums of antichains in Theorem 3.3 (arXiv:2307.08520); their count \(1+\sum_i a_i+\sum_{i<j}a_i a_j\) is closely related and implies the unaveraged type count after accounting for one-sided boundaries. Simon's 2022 work provides broader finite-parameter model-theoretic type-profile context, but its NIP hypothesis does not apply to the generic poset. The Fubini/ordered Bell EGF \(W\) is classical (OEIS A000670).

The claimed contribution is specifically the paired **random weak-order average laws**, the orbit-normalized EGF, and the sharp constant \(1/(\log2)^2\), not the unrestricted ideal/filter normal form, the interval-closed-set count, or the ordered Bell denominator.

## Limitations

The expectations use the uniform distribution on labelled weak orders, not on all finite posets or on unlabelled weak orders. No concentration, variance, limiting distribution, or almost-sure convergence is claimed. Source searches do not prove universal novelty; a hidden equivalent weighted species identity is possible. The self-review is not an independent external verification.

## References

1. P. Simon, *NIP ω-categorical structures: The rank 1 case*, arXiv:1807.07102 (first posted 2018-07-18); Proceedings of the London Mathematical Society 125 (2022), 1253–1331, DOI: 10.1112/plms.12482. Used for finite-type-profile context only.
2. J. Elder, N. Lafrenière, E. McNicholas, J. Striker, and A. Welch, *Toggling, rowmotion, and homomesy on interval-closed sets*, arXiv:2307.08520 (first posted 2023-07-17), especially Theorem 3.3.
3. OEIS A000670, *Fubini numbers / ordered Bell numbers*, for the classical labelled weak-order enumeration.
4. *Finite-parameter 1-type counting in the random poset is #P-complete*, publicly indexed research record, 2026, for the already-established general ideal/filter description. No distinct authorship is inferred here.

# Complete image-incidence fibers and faithful counts for null transformation actions

## Finding

Fix integers \(m\ge 1\), \(n\ge0\). Let \(X\) be a labeled set of \(n+1\) elements with distinguished point \(0\), and let \(c_0:X\to X\) be the constant map with value \(0\). Consider ordered \(m\)-tuples of total transformations \((f_1,\ldots,f_m)\) with
\[
f_i\circ f_j=c_0\qquad(1\le i,j\le m).
\]
These are precisely homomorphisms from the labeled null semigroup on \(m\) generators and a zero into the full transformation monoid, subject to the zero mapping to \(c_0\). They need not be injective.

For each nonempty \(S\subseteq[m]\), define the exact image-incidence cell
\[
C_S=\{x\in X\setminus\{0\}:x\in\operatorname{im}(f_i)\text{ exactly for }i\in S\}.
\]
Prescribe nonnegative integers \(t_S=|C_S|\) for all such \(S\). Write
\[
u=\sum_{\varnothing\ne S\subseteq[m]}t_S,\qquad
r=n-u,\qquad a_i=\sum_{S\ni i}t_S.
\]
If \(u>n\), there are no tuples of this profile. Otherwise their **exact number** is
\[
\boxed{\displaystyle
N_{n,m}(\mathbf t)=
\frac{n!}{r!\prod_{\varnothing\ne S\subseteq[m]}t_S!}
\prod_{i=1}^{m}a_i!\left\{\begin{matrix}r+1\\a_i+1\end{matrix}\right\},
}
\]
where \(\left\{\begin{smallmatrix}h\\k\end{smallmatrix}\right\}\) denotes a Stirling number of the second kind; it is zero when \(k>h\). Thus the prescribed profile occurs **if and only if**
\[
\boxed{\quad u+\max_{1\le i\le m}a_i\le n.\quad}
\]
Equivalently, its smallest possible carrier size is \(1+u+\max_i a_i\). This includes the all-zero profile, which is realized by the unique tuple \((c_0,\ldots,c_0)\).

Let \(F_m(n)=\sum_{\mathbf t}N_{n,m}(\mathbf t)\) be the number of such ordered tuples, and set \(F_0(n)=1\). Let \(E_m(n)\) count **faithful** (injective) homomorphisms of the same labeled null semigroup into the transformation monoid with its zero mapped to \(c_0\). Then
\[
\boxed{\quad E_m(n)=\sum_{k=1}^{m+1}s(m+1,k)F_{k-1}(n),\quad}
\]
where \(s(h,k)\) is the signed Stirling number of the first kind, defined by \(z(z-1)\cdots(z-h+1)=\sum_{k=0}^{h}s(h,k)z^k\).

For example, the totals for \(n=2,3,4,5\) and \(m=2\) are respectively \(7,52,553,7896\); the faithful counts are \(0,24,432,7310\). These are on carriers of sizes \(3,4,5,6\), respectively.

## Assumptions and scope

The carrier is a **labeled** finite set, the transformations are **total** functions, and the distinguished zero of the source null semigroup is required to act as the **constant map** \(c_0\). Generator labels are ordered and no quotient by relabeling or conjugation is taken. All equations and counts are set-theoretic, not linear-algebraic. Every integer \(m\ge1\), every \(n\ge0\), and every incidence vector of nonnegative integers \((t_S)\) are covered. There is no field or characteristic parameter.

In the formula, \(\operatorname{im}(f_i)\) always contains \(0\), and \(a_i\) is exactly its number of *nonzero* image points. By definition \(u\) is the size of the nonzero union of all images, and \(r\) counts the remaining nonzero points. The factorial quotient is a multinomial coefficient and hence integral.

## Proof

**Step 1 (zero is fixed).** From \(f_i^2=c_0\) and associativity, \(f_i^3=f_i\circ c_0\) is the constant map with value \(f_i(0)\), whereas \(f_i^3=c_0\circ f_i=c_0\). Therefore \(f_i(0)=0\) for every \(i\).

**Step 2 (universal annihilated image).** Put \(A_i=\operatorname{im}(f_i)\setminus\{0\}\) and \(U=\bigcup_i A_i\). For each \(x\in A_j\), choose \(y\in X\) with \(f_j(y)=x\). Then \(f_i(x)=f_i(f_j(y))=0\) for every \(i\). Hence **all** maps vanish on \(U\cup\{0\}\). Conversely, if every \(f_i\) vanishes on \(U\cup\{0\}\), has image contained in \(A_i\cup\{0\}\), and actually takes every value in \(A_i\), then every composite is \(c_0\). Thus this description is necessary and sufficient.

**Step 3 (fixed-cell enumeration).** Exact incidence cells \(C_S\) are disjoint and partition \(U\). Choose them among the \(n\) nonzero labeled points, leaving \(r=n-u\) points outside \(U\). The choice count is
\[
\frac{n!}{r!\prod_{S\ne\varnothing}t_S!}.
\]
For a fixed choice, the values of \(f_i\) are forced to \(0\) on \(U\cup\{0\}\); on the \(r\) remaining points they are arbitrary values in \(A_i\cup\{0\}\), subject only to hitting every member of \(A_i\). Adjoin a dummy input \(*\) forced to map to \(0\). Kernel partitions of the \(r+1\) inputs into \(a_i+1\) nonempty blocks are counted by \(\left\{\begin{smallmatrix}r+1\\a_i+1\end{smallmatrix}\right\}\); the block containing \(*\) is the zero block, and the other \(a_i\) blocks may be bijectively labeled by the elements of \(A_i\) in \(a_i!\) ways. Choices for different \(i\) are independent because all products vanish automatically once every map kills \(U\). Multiplication gives the stated exact formula.

**Step 4 (sharp support).** The partition-and-surjection count is positive exactly when \(r+1\ge a_i+1\) for all \(i\), or \(r\ge\max_i a_i\). The preceding construction realizes every profile satisfying this inequality, including cases with empty individual images. Rewriting it as \(u+\max_i a_i\le n\) proves the sharp carrier-size boundary.

**Step 5 (injective representations).** On the \(m+1\) labeled elements of the source null semigroup, every set partition defines a congruence, because all products are the zero element. A homomorphism constant on each block of a partition with \(k\) blocks is equivalent to a homomorphism of a \((k-1)\)-generator null semigroup, whose distinguished zero acts as \(c_0\): there are exactly \(F_{k-1}(n)\) such homomorphisms. The injective ones are obtained by Möbius inversion in the set-partition lattice. The sum of its Möbius coefficients over partitions into \(k\) blocks is the signed Stirling number \(s(m+1,k)\), which follows for example by the cycle expansion of the falling factorial. This yields the faithful formula. No assumption that the generators have distinct images was made in Steps 1–4; distinctness is imposed precisely by this inversion.

## Verification

The accompanying standard-library program `verify.py` independently enumerates every pointed total transformation and directly checks **all** \(m^2\) compositions for zero. It then classifies every valid tuple by the full Boolean image-incidence profile and compares each individual profile count with the Stirling formula. It also tests actual injectivity against the signed-Stirling inversion. Cases checked are \((n,m)=(0,1),(1,1),(2,1),(3,1),(4,1),(2,2),(3,2),(4,2),(2,3),(3,3)\). The program prints `VERIFY_OK_NULL_TRANSFORMATION_IMAGE_INCIDENCE` on success.

The exact exhaustive totals for \((n,m)=(4,2)\) are \(553\) homomorphisms, \(432\) injective homomorphisms, and \(10\) nonempty incidence cells in the parameter space (distinct nonzero profile vectors). For \((n,m)=(3,3)\), the corresponding numbers are \(226\), \(18\), and \(14\). For larger parameters, symbolic proof, not finite enumeration, establishes the result.

## Relationship to prior work

Cameron, Gadouleau, Mitchell and Péresse's 2015 study of chains of subsemigroups uses null subsemigroups of transformation principal factors and classical Stirling rank enumerators, but its focus is extremal chains, not the joint incidence patterns of labeled null generators. Cameron, East, FitzGerald, Mitchell, Pebody and Quinn-Gregson (2021 preprint, later published) give a general structural classification of null subsemigroups \(S\subseteq T_X\) via annihilating image sets and calculate their maximum sizes, degrees, and numbers of **maximal** null subsemigroups. This supplies an important broader structural setting, but neither their size formula for a fixed maximal ambient null subsemigroup nor their extremal degree theorem directly computes the complete Boolean-profile counts of labeled tuples or the number of faithful embeddings. The present proof enumerates exact image-surjection fibers and then performs an independent partition-lattice inversion. Cain, Malheiro and Paulista (2023 preprint) treat largest commutative nilpotent subsemigroups, not these image-incidence fibers. The underlying annihilated-image characterization is **not** presented as novel.

The theorem's total counts and complete \(2^m-1\)-parameter image-incidence distribution should not be confused with counts of maximal null subsemigroups, which are different objects. The result refines the representation count for a fixed rank-one zero; it neither subsumes nor contradicts the referenced maximal-size theorems.

## Limitations

The result concerns only a source null semigroup with all products zero, and a constant rank-one zero transformation in a **full** transformation monoid. It does not address higher-rank idempotent zero actions, non-null nilpotent semigroups, injectivity subject to *each prescribed incidence cell* (only the unrefined faithful total is given), or conjugacy classes of embeddings. It gives exact finite formulas, not asymptotic estimates. Historical-priority assessment is limited to the cited primary texts and targeted published-record/literature searches: an equivalent multivariate occupancy formula might occur in unexamined enumeration literature. Finite verification is not an independent mathematical audit.

## References

1. P. J. Cameron, M. Gadouleau, J. D. Mitchell, Y. Péresse, *Chains of subsemigroups*, arXiv:1501.06394v1, publicly submitted 26 January 2015, especially Sections 4 and 9. https://arxiv.org/abs/1501.06394
2. P. J. Cameron, J. East, D. FitzGerald, J. D. Mitchell, L. Pebody, T. Quinn-Gregson, *Minimum degrees of finite rectangular bands, null semigroups, and variants of full transformation semigroups*, arXiv:2110.09701v1, publicly submitted 19 October 2021, especially Sections 4.1–4.2. https://arxiv.org/html/2110.09701v2
3. A. J. Cain, A. Malheiro, T. Paulista, *Commutative nilpotent transformation semigroups*, arXiv:2310.08481v1, publicly submitted 12 October 2023, especially Sections 2–3. https://arxiv.org/abs/2310.08481

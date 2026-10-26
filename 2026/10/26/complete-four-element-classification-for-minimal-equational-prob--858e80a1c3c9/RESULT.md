# Complete four-element classification for minimal equational probability spectrum

## Finding
For an algebra \((Q,*)\) with a single binary operation and \(|Q|=4\), give each assignment to the variables of a binary-term equation equal weight, and let \(\operatorname{PSpec}(Q)\) be the set of all resulting satisfaction probabilities. There are **exactly ten isomorphism classes** with
\[
\operatorname{PSpec}(Q)=\{1/4,1\}.
\]
On a fixed labeled four-point universe, there are **exactly 52** such binary operation tables.

Five isomorphism classes are nonquasigroups: the constant operation; the two projections; and the two orientations of \(x*y=f(x)\) or \(x*y=f(y)\), where \(f\) has one fixed point and a three-cycle. The **five quasigroup classes** have representatives over \(\mathbb F_4=\mathbb F_2[\omega]\), \(\omega^2=\omega+1\), of the form
\[
x*y=ax+by,\qquad
(a,b)\in\{(1,1),(\omega,1),(1,\omega),(\omega,\omega),(\omega,\omega^2)\}.
\]
The quasigroup representatives have, respectively, \(4,8,8,8,2\) labeled tables in their isomorphism orbits. Thus the quasigroups account for 30 labeled tables and the nonquasigroups for 22.

## Assumptions and scope
A groupoid means a **nonempty set with one binary operation**, not necessarily associative, unital, idempotent, or commutative. An equation is an equality of binary terms in finitely many variables, without named constants or inverse operations. A variable may occur more than once or only on one side. Its probability is the number of satisfying assignments divided by the number of all assignments to the variables appearing in the equation. Isomorphisms are bijections simultaneously relabeling the rows, columns, and outputs. A quasigroup means that every row and every column of the operation table is a permutation.

## Proof
**Step 1: eliminate all other nonquasigroup forms.** For every groupoid \((Q,*)\), the equation \(x*y=x*z\) has at least \(4^2=16\) of the \(4^3=64\) possible solutions, namely those with \(y=z\). If the spectrum is minimal, its number of solutions is either 16 or 64. It equals 16 exactly when each row is injective, since all 16 forced assignments already exhaust the solutions. It equals 64 exactly when each row is constant. Applying the same argument to \(y*x=z*x\) shows that each column is injective or every column is constant. Crossing the two dichotomies gives a Latin square, a constant table, or a table depending on just one input, \(x*y=f(x)\) or \(x*y=f(y)\), with \(f\) necessarily a permutation. For a permutation of four points, the one-variable equation \(f(x)=x\) has either one or four solutions under minimal spectrum. Thus \(f\) is the identity or has exactly one fixed point, in which case it has a single three-cycle. Conversely, a term in any such unary-permutation groupoid is an iterate of \(f\) applied to one of its variables. A comparison of two such terms is therefore either always true, holds for exactly one of four values of a repeated variable, or equates two independent uniform permutation images with probability \(1/4\). These five nonquasigroup isomorphism types all qualify. Their labeled multiplicities are \(4,1,1,8,8\).

**Step 2: four necessary equations exhaust the Latin case.** A Latin table on \(\{0,1,2,3\}\) is a choice of four row permutations with entries pairwise distinct in every column. The executable enumerator `verify.py` constructs **all** such tables, 576 in total, by recursive traversal of the 24 row permutations, rejecting a row if it repeats any earlier entry in any column. It canonicalizes a table under all 24 simultaneous permutations of inputs and outputs using
\[
t^p(i,j)=p\bigl(t(p^{-1}(i),p^{-1}(j))\bigr).
\]
This gives 35 ordinary quasigroup isomorphism classes, a useful independent census check.

Every minimally spectral table must give probabilities only \(1/4\) or \(1\) for the four equations
\[
xy\approx yx,\qquad xx\approx yy,\qquad xx\approx x,\qquad x(xx)\approx x.
\]
The first two use two variables and so require 4 or 16 solutions; the latter two use one and require 1 or 4. The exhaustive verifier filters all 576 Latin tables by these four exact integer counts, leaving **30 labeled tables in five simultaneous-isomorphism classes**, of orbit sizes \(4,8,8,8,2\). This is an exhaustive finite step: the code enumerates every Latin table, not just a sample, and its complete source is embedded alongside this proof.

**Step 3: identify each surviving class.** Encode \(\mathbb F_4\) as \(\{0,1,\omega,\omega+1\}\), with addition by binary XOR and multiplication determined by \(\omega^2=\omega+1\). The verifier constructs the five displayed affine tables from explicit field arithmetic, computes their five distinct canonical forms, and checks that the **set** of these forms equals the set of five forms surviving Step 2. Consequently the list is complete and free of isomorphic repetitions.

**Step 4: prove sufficiency for every equation, without a term-length cutoff.** For any displayed coefficient pair, the operation \(x*y=ax+by\) is a quasigroup because both coefficients are nonzero. By induction on term formation, every term in arbitrarily many variables is a homogeneous \(\mathbb F_4\)-linear form. Therefore the difference of two terms is either the zero functional, giving probability \(1\), or a nonzero linear functional on a finite-dimensional \(\mathbb F_4\)-vector space, whose kernel has exactly one quarter of the assignments. The equation \(x\approx y\) gives probability \(1/4\), and \(x\approx x\) gives probability \(1\), so the spectrum is *exactly* \(\{1/4,1\}\). This establishes sufficiency for the infinitely many equations. The five verified nonquasigroup cases and their labeled multiplicities, combined with the 30 Latin tables, give ten classes and 52 labeled tables.

## Verification
Execute `python3 verify.py` with standard Python 3; it needs no external modules or internet access. The program printed:

```
VERIFY_OK latin=576 latin_isotypes=35 qualifying_latin=30 qualifying_quasigroup_isotypes=5 non_latin_isotypes=5 all_isotypes=10 labeled_minimal_groupoids=52
affine_coefficients= ((1, 1), (2, 1), (1, 2), (2, 2), (2, 3))
quasigroup_isomorphism_orbits= [2, 4, 8, 8, 8]
```

Here the code numbers \(2\) and \(3\) represent \(\omega\) and \(\omega^2\). Its exhaustive loops cover all possible Latin tables and all simultaneous relabelings, and it verifies exact equality with the affine-representative canonical set. The infinite-equation sufficiency in Step 4 is proved algebraically and does not rest on finite-length testing.

## Relationship to prior work
Cardó, *Minimal probabilistic spectrum grupoids* (arXiv:2603.19487v1, first public 2026-03-19), established the groupoid-to-quasigroup/isocyclic reduction in Theorem 3.8. Section 6 lists six previously available four-element isomorphism types (the five nonquasigroup types and the elementary-abelian group) and leaves the order-four quasigroup completion unresolved. The present result supplies the four additional affine quasigroup types and proves the ten-class exhaustive classification with exact labeled counts. The general reduction and the fact that vector-space linear forms yield minimal equational probabilities are not asserted to be new in isolation; novelty lies in the complete enumeration and exact structural classification at order four.

## Limitations
Only the four-element, one-binary-operation signature is classified. Neither quasigroups of higher orders nor signatures with designated constants or divisions are covered. The finite census is reproducible and logically exhaustive if the short enumerator and the stated canonicalization are correct; it is not independent formal-machine certification. No independent mathematical audit has been performed. An equivalent earlier result in unindexed literature remains possible.

## References
1. Carles Cardó, *Minimal probabilistic spectrum grupoids*, arXiv:2603.19487v1 (2026-03-19), especially Theorem 3.8 and Section 6. https://arxiv.org/abs/2603.19487
2. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (2026-04-09), complementary context. https://arxiv.org/abs/2604.08446
3. Denis S. Krotov and Vladimir N. Potapov, *n-Ary Quasigroups of Order 4*, SIAM Journal on Discrete Mathematics (2008), classical structural background on low-order quasigroups. https://doi.org/10.1137/070697331

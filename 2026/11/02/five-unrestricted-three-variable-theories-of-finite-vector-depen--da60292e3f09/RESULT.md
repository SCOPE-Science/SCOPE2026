# Five unrestricted three-variable theories of finite vector dependence geometries

## Finding
Let \(F\) be any finite field of order \(q\), and let \(d\ge1\). Define \(\mathcal D(F,d)\) with universe \(F^d\), equality, and one ternary predicate \(D\), interpreted by
\[
D(u,v,w)\quad\Longleftrightarrow\quad\dim_F\langle u,v,w\rangle\le2.
\]
This is the *pure three-vector linear-dependence reduct*: addition, multiplication, zero, scalar constants, and coordinate predicates are not in its language.

**Theorem.** Exactly five equivalence classes occur for the unrestricted noncounting three-variable first-order theories of \(\mathcal D(F,d)\). Their complete parameter descriptions and smallest representatives within this family are:

| Class | Parameters | Smallest structure |
| --- | --- | --- |
| A | \(d=1,q=2\) | \(\mathcal D(\mathbb F_2,1)\), 2 elements |
| B | \(d\le2\), except class A | \(\mathcal D(\mathbb F_3,1)\), 3 elements |
| C | \(d\ge3,q=2\) | \(\mathcal D(\mathbb F_2,3)\), 8 elements |
| D | \(d\ge3,q=3\) | \(\mathcal D(\mathbb F_3,3)\), 27 elements |
| E | \(d\ge3,q\ge4\) | \(\mathcal D(\mathbb F_4,3)\), 64 elements |

For example, \(\mathcal D(\mathbb F_4,3)\equiv_{\mathrm{FO}^3}\mathcal D(\mathbb F_5,10)\), despite the different characteristics, dimensions and cardinalities. Thus \(64\) is the sharp uniform smallest-representative bound. Two members are equivalent in all first-order sentences using only three variable names (without any quantifier-depth bound) exactly when they belong to the same class.

## Assumptions and scope
The universe consists of **all** vectors, including zero and all nonzero scalar multiples; vectors are not projectivized. Fields are finite, \(q\) is a prime power, and \(d\) is a positive integer. A tuple with repetitions is dependent by the displayed definition. Only equality and \(D\) are permitted. The relation is interpreted as dependence of a *triple of vectors*, not affine collinearity of three points.

The ordinary three-pebble game characterizes equivalence for first-order logic using three variables at unrestricted quantifier depth. A game position preserves every atomic equality and the truth of \(D\) on every triple of currently pebbled elements, including repeated positions.

## Proof
**1. The low-dimensional branch.** For \(d\le2\), every triple is dependent, so \(D\) is universally true and the reduct is a pure equality structure on \(q^d\) elements. Ordinary three-variable logic distinguishes cardinality two from cardinality at least three, but cannot distinguish any two pure nonempty equality sets of cardinality at least three. In the stated domain \(d\ge1\), the sole two-element case is \((q,d)=(2,1)\). Classes A and B follow.

**2. A stronger matching invariant for \(d\ge3\).** For each occupied pebble, record whether its vector is zero. For each ordered pair, retain its equality status and whether the vectors are linearly dependent. There are six possible ordered-pair states: \(ZZ\) (both zero), \(ZX\) (first zero), \(XZ\) (second zero), \(XX\) (same nonzero vector), \(PP\) (distinct nonzero parallel vectors), and \(II\) (independent vectors). Also preserve the value of \(D\) on the occupied triple.

Suppose Spoiler moves a pebble, leaving at most two stationary pebbles. We show that each desired extension state can be matched in the other structure if the field sizes are both two, both three, or both at least four, and both dimensions are at least three. Let \(N=q^d\). If the two stationary vectors are independent, the seven disjoint possibilities for the new vector \(z\), together with their exact numbers, are: zero (1); equal to the first (1); equal to the second (1); nonzero parallel to the first but distinct (\(q-2\)); nonzero parallel to the second but distinct (\(q-2\)); in their span but independent of either separately (\((q-1)^2\)); outside their span (\(N-q^2\)). In the first six cases the triple is dependent; in the last it is independent. The count \((q-1)^2\) is obtained by using two nonzero coefficients of the fixed independent pair.

If both stationary vectors are zero, the two possibilities have counts \(1\) (zero) and \(N-1\) (nonzero). If exactly one is zero, or they are equal and nonzero, the four possibilities have counts \(1,1,q-2,N-q\): zero, the named nonzero vector, a distinct nonzero parallel vector, and a vector independent of it. For two distinct parallel nonzero vectors, the five possibilities have counts \(1,1,1,q-3,N-q\): zero, each of the two named vectors, another distinct parallel nonzero vector, and an independent vector. In all these nonindependent-anchor cases, the triple is always dependent.

Because \(d\ge3\), \(N-q>0\) and \(N-q^2>0\). All listed counts are positive except precisely the \(q-2\) and \(q-3\) terms, whose positivity is determined by whether \(q=2\), \(q=3\), or \(q\ge4\). In particular, the extension-support pattern depends on no other parameter. Choosing an extension of the same support type maintains all zero flags, equality and pair-dependence states, and the atomic ternary-dependence relation. Induction through arbitrarily many pebble moves proves equivalence within each of C, D, and E.

**3. Separation.** For \(d\ge3\), the formula \(\exists x\exists y\exists z\,\neg D(x,y,z)\) is true and distinguishes classes C–E from A–B. In these dimensions, \(Z(x):=\forall y\forall z\,D(x,y,z)\) defines the zero vector, while \(P(x,y):=\forall z\,D(x,y,z)\) defines pairwise linear dependence. All three formulas use at most three variable names. The formula asserting that two distinct nonzero vectors satisfy \(P\) holds exactly when \(q\ge3\). The formula asserting three pairwise distinct nonzero vectors satisfying \(P(x,y)\) and \(P(x,z)\) holds exactly when \(q\ge4\). These formulas use only \(x,y,z\): when the displayed definitions are expanded, each inner quantifier can shadow a third variable because the parallelism and zero tests have at most two or one free variables respectively. Pure equality separates A from B by a sentence asserting three distinct elements. This proves all five classes are pairwise distinguishable.

**4. Sharpness.** Every class contains its displayed representative. In class E every permissible field has at least four elements and every dimension at least three; hence every member has at least \(4^3=64\) vectors. The displayed class-E representative realizes the bound.

## Verification
The standalone program `support_check.py` explicitly enumerates full vector spaces for \((q,d)\) equal to \((2,3),(2,4),(3,3),(3,4),(4,3),(5,3),(7,3)\). It checks **every** ordered anchor pair and every possible third vector, finds the full support profile, verifies homogeneity within each pair class, and compares full profiles across models in the same field-size class. Field order four is implemented with \(\mathbb F_2[a]/(a^2+a+1)\).

The independent program `count_check.py` computes exact extension frequencies for canonical anchored pairs (including all nontrivial scalar ratios in the parallel case), and compares them with the algebraic table above over the same seven finite configurations. Both scripts use only Python's standard library. Reproduce with `python support_check.py` and `python count_check.py`; expected output is embedded as `support_output.txt` and `count_output.txt`. Their finite checks corroborate, but do not replace, the general counting proof.

## Relationship to prior work
Pierce (2009) studies vector spaces over unspecified fields and languages with dependence predicates; his model-companion results concern an appropriately richer theory and do not, in the accessible abstract, state these five pure ternary-reduct, finite-field, unrestricted three-variable classes. The full article was not accessible for a decisive comparison. Grohe and Otto (2012) develop pebble-game methods and general finite-variable equivalence; the inspected introduction and game section establish the background methodology but no exact classification of full vector-dependence structures. Kardoš, Král', Liebenau, and Mach (2015) study first-order convergence and limit modelings of matroids representable over fixed finite fields; their full online text concerns a different question and does not imply the stated cross-field finite-variable equivalences. Earlier results on subspace-inclusion posets and affine collinearity structures use different universes, languages, and logical resources and do not imply this claim.

## Limitations
The result concerns only pure ternary dependence and equality. It does not apply to signatures naming addition, scalar multiplication, vector zero, all arity dependence relations, counting quantifiers, or four or more variable names. It does not classify arbitrary representable matroids or infinite-dimensional vector spaces. Historical priority may be affected by general results on matroid pebble games or by parts of Pierce's inaccessible full paper. Independent mathematical examination has not been performed.

## References
1. David Pierce, *Model-theory of vector-spaces over unspecified fields*, Archive for Mathematical Logic 48 (2009), 421–436, DOI 10.1007/s00153-009-0130-x. First publisher-publication date 2009-04-16: https://link.springer.com/article/10.1007/s00153-009-0130-x ; public repository: https://open.metu.edu.tr/handle/11511/63860 . (Abstract and metadata inspected; full article unavailable.)
2. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, CSL 2012, pp. 289–304, DOI 10.4230/LIPIcs.CSL.2012.289. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2012.289 . (Open-access PDF introduction and game section inspected.)
3. František Kardoš, Daniel Král', Anita Liebenau, and Lukáš Mach, *First order convergence of matroids*, preprint first submitted 2015-01-26, arXiv:1501.06518. https://arxiv.org/abs/1501.06518 . (Full online HTML introduction, definitions, and main theorems inspected.)

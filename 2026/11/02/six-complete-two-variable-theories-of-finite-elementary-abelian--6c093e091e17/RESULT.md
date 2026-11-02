# Six complete two-variable theories of finite elementary abelian prime groups

## Finding

For a prime \(p\) and positive integer \(d\), let \(V(p,d)\) be the additive group \(\mathbb F_p^d\) in the relational language consisting of equality, a named zero, and the ternary relation \(R(x,y,z)\) meaning \(x+y=z\). Let \(\equiv_{\mathrm{FO}^2}\) mean agreement on **every** first-order sentence using at most the two variable names \(x,y\), with no restriction on quantifier rank or quantifier alternation.

**Theorem.** Exactly six \(\mathrm{FO}^2\) theories occur among these structures. The six classes are:

1. \(p=2,d=1\).
2. \(p=2,d\ge2\).
3. \(p=3,d=1\).
4. \(p=3,d\ge2\).
5. \(p=5,d=1\).
6. \(p=5,d\ge2\), **together with every \(p\ge7,d\ge1\)**.

Distinct numbered classes satisfy different \(\mathrm{FO}^2\) sentences of quantifier rank **two**. Within a class, the structures agree on every \(\mathrm{FO}^2\) sentence, however deeply quantified. In particular,
\[
V(5,2)\equiv_{\mathrm{FO}^2}V(7,1)\equiv_{\mathrm{FO}^2}V(101,100).
\]
Every class has a representative with at most **nine elements**; nine is sharp within this family (the fourth class requires \(V(3,2)\)).

## Assumptions and scope

The underlying set is a nontrivial elementary abelian prime group, with prime \(p\) and dimension \(d\ge1\). The first-order language has a **relational**, not functional, addition symbol, and a named constant \(0\). Formulas can reuse either variable arbitrarily many times, including under nested quantifiers, but no third variable name is allowed. This is ordinary two-variable first-order logic \(\mathrm{FO}^2\) without counting quantifiers. The theorem is not a classification of unrestricted first-order logic.

## Proof

**Pair atomic diagrams.** In the given vocabulary any quantifier-free formula with only the variable names \(x,y\) is a Boolean combination of equality atoms and instances of \(R(u,v,w)\), where \(u,v,w\in\{0,x,y\}\). All such atoms are included in `verify_two_variable.py`. For \(x\ne0\) and \(y=ax\) with \(a\in\mathbb F_p\), in every odd characteristic at least five, their complete truth pattern depends only on whether
\[
a\in S=\{0,1,-1,2,1/2\}
\]
and, if so, which member of this set is chosen. These five slopes are distinct for every \(p\ge5\). They correspond respectively to \(y=0\), \(y=x\), \(x+y=0\), \(y=2x\), and \(x=2y\); all other nonzero two-variable atomic equations reduce to these or to trivial identities. If \(x,y\) are linearly independent, none of the five special relations holds, and the quantifier-free diagram is precisely the generic scalar-slope diagram. The remaining case \(x=0\) has only the alternatives \(y=0\) and \(y\ne0\), whose diagrams are characteristic-stable in the indicated regimes.

For \(p=2\), the only scalar slopes are \(0,1\); for \(p=3\), they are \(0,1,-1\) and the relations \(2=-1=1/2\) coincide. In dimensions at least two, an independent choice supplies an extra generic diagram. At \(p=5,d=1\), the five special slopes exhaust the field and no generic diagram exists. At \(p=5,d\ge2\) and at every \(p\ge7,d\ge1\), all five special diagrams and the generic diagram exist. These observations produce exactly the six pair-diagram spectra stated in the theorem. Each spectrum is different from every other, as verified by direct enumeration of all atomic triples and equalities. Since every pair diagram can be described by a complete conjunction of positive and negated atomic formulas, the sentence \(\exists x\exists y\,\theta(x,y)\) isolates the presence of any such diagram. Thus the six classes are pairwise inequivalent already at quantifier rank two.

**Uniform two-pebble back-and-forth, independent of quantifier depth.** Suppose two structures have the same pair-diagram spectrum from the above six-way partition. Match any current pair \((x,y)\) with another pair having the same complete atomic diagram. The diagram records whether either coordinate is zero. If the next quantifier reassigns \(x\) while retaining \(y=0\), the available new pair diagrams are precisely the zero/zero and nonzero/zero cases, independent of the structure. If \(y\ne0\), the possible new diagrams are the special scalar ratios listed above, together with the generic diagram exactly when that class admits one. By the spectrum calculation, these possibilities match perfectly in the two structures. The same reasoning holds when a move reassigns \(y\) while retaining \(x\). In either direction one can match **every** selected new value with one realizing the same new diagram. This establishes a two-pebble back-and-forth relation closed under both variable reassignments for arbitrarily many rounds.

An induction on the formation of two-variable formulas now proves that a pair and its matching partner satisfy the same formulas of **every** quantifier rank. Starting from empty assignments, the first variable can also be matched (zero to zero or nonzero to nonzero), so the structures satisfy the same \(\mathrm{FO}^2\) sentences. This proves the upper implication without any finite-rank cutoff or extrapolation from sampled characteristics.

**Sharp representatives.** The smallest orders in the six classes are respectively \(2,4,3,9,5,7\). In particular, the fourth class requires dimension at least two over \(\mathbb F_3\), so its least member has nine elements. This establishes the sharp nine-element representative bound.

## Verification

`verify_two_variable.py` is a standalone Python 3 standard-library checker. It directly enumerates every quantifier-free equality and ternary-addition atom on \(0,x,y\), every ordered pair of elements of tested groups, and the replacement-diagram spectra when either variable is changed while the other is held at zero or nonzero. It asserts that the six predicted spectra are distinct and that tested parameters fall into the exact classes. Execute with `python3 verify_two_variable.py`. The program's actual output is included as `verification_output.txt`.

The program is an exact finite check, **not** a proof of the assertion for all primes, all dimensions, or all quantifier ranks. Those parts follow from the five-slope calculation and the two-pebble back-and-forth argument above.

## Relationship to prior work

Walid Gomaa's 2007 dissertation *Model Theory and Complexity Theory* examines Ehrenfeucht–Fraïssé games and quantifier/variable resources for finite abelian groups, providing general distinguishing-rank and variable-count bounds. The previously established thirteen-class **ordinary quantifier-rank-three** classification for elementary abelian prime groups does not imply agreement of unbounded-depth \(\mathrm{FO}^2\) sentences. Conversely, the present six classes are strictly coarser: two-variable logic loses several characteristic and dimension distinctions visible to unrestricted rank-three logic. Kim Scott's treatment of vector spaces uses a richer scalar language and does not imply this relational two-variable theorem.

## Limitations

This is specifically a theorem about \(\mathrm{FO}^2\) without counting, for named-zero relational addition structures on elementary abelian prime groups. No assertion is made for arbitrary abelian groups, for ternary multiplication in nonabelian groups, for functional addition, or for logic using three or more variables. Historical-priority verification is incomplete; independent mathematical audit has not been performed.

## References

- Walid Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland (public repository date 2007-07-06), https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 (finite-abelian-group Ehrenfeucht–Fraïssé and variable-resource sections).
- Walid Gomaa, *Descriptive Complexity of Finite Abelian Groups*, *International Journal of Algebra and Computation* 20 (2010), 1087–1116, https://doi.org/10.1142/S0218196710006047 (published abstract and complexity bounds; full publisher text not inspected).
- Kim Scott, *A Partial Characterization of Ehrenfeucht–Fraïssé Games on Fields and Vector Spaces*, https://web.mit.edu/rsi/www/pdfs/papers/2005/2005-kscott.pdf (the scalar-enriched language definition was inspected).

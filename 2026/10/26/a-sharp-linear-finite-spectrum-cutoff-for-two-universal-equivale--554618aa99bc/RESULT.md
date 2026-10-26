# A sharp linear finite-spectrum cutoff for two-universal equivalence theories

## Finding

For every integer \(k\ge0\), let \(\Phi\) be a first-order sentence of the form
\[
\Phi=\exists x_1\cdots\exists x_k\;\forall y\;\forall z\;\psi(\bar x,y,z),
\]
where \(\psi\) is quantifier-free in the language with equality and one binary relation \(E\). Interpret \(E\) as an equivalence relation, and take finite structures to be nonempty.

**Sharp cutoff theorem.** If \(\Phi\) has a model of size at least \(2k+2\), then it has a model of every cardinality \(n\ge k+2\). Thus a finite nonempty spectrum has maximum at most \(2k+1\). The bound is sharp for each \(k\ge0\): when \(k\ge1\), some sentence has exactly the spectrum
\[
\{k,k+1,\ldots,2k+1\};
\]
for \(k=0\), the spectrum \(\{1\}\) attains the same endpoint \(2k+1\).

In particular, to determine whether such a sentence has an unbounded finite spectrum, it suffices in principle to test satisfiability on a single domain size \(2k+2\). This is a mathematical finite search criterion, not a claim of a fast algorithm in formula length.

## Assumptions and scope

The only nonlogical symbol is a binary predicate \(E\), interpreted **externally** as an equivalence relation; reflexivity, symmetry, and transitivity are semantic assumptions on the model class, not necessarily part of the \(\forall^2\) sentence. Repetitions among the existential witnesses are allowed. A spectrum is the set of positive integers \(n\) for which the sentence has an \(n\)-element equivalence-relation model. The quantifier-free matrix may contain arbitrary Boolean combinations of equality and \(E\) between witnesses and the two universal variables.

## Proof

**1. Finding two interchangeable elements.** Suppose \(M\models\Phi\), fix witnesses \(a_1,\ldots,a_k\), and let \(U\) be their set of distinct values. Write \(u=|U|\le k\), and let \(t\le u\) denote the number of \(E\)-equivalence classes intersecting \(U\).

For any \(b\notin U\), its complete incidence profile with \(U\) is one of \(t+1\) possibilities: \(b\) belongs to one of the \(t\) marked classes, or \(b\) is unrelated to all of \(U\). If \(|M|\ge 2k+2\), then
\[
|M\setminus U|\ge 2k+2-u>t+1.
\]
Thus there are distinct \(b,c\in M\setminus U\) having the same incidence profile with \(U\).

**2. Reduction to an induced core.** Let \(H\) be the induced equivalence substructure on \(U\cup\{b,c\}\). Every quantifier-free formula has the same truth value in \(H\) as in \(M\) on assignments in \(H\). Since the matrix is universally quantified over exactly \(y,z\), \(H\models\Phi\) with the original witness tuple. The transposition exchanging \(b,c\) and fixing \(U\) is an automorphism of \(H\): their incidences with \(U\) agree, and \(E\) is reflexive and symmetric.

**3. Arbitrary-size expansion.** Fix an integer \(s\ge2\). Replace \(b,c\) in \(H\) with a new set \(C\) of size \(s\); keep \(E\) unchanged on \(U\), assign every element of \(C\) the incidence profile of \(b\) to \(U\), and put
\[
E(p,q)\quad\Longleftrightarrow\quad E_H(b,c)
\qquad(p,q\in C,\ p\ne q).
\]
Set \(E(p,p)\) true for every \(p\in C\). This is again an equivalence relation. Indeed, if the common profile meets a marked class, equivalence of \(E\) forces \(E_H(b,c)\), and all members of \(C\) join that same class. If the common profile is unmarked, \(C\) either forms one separate equivalence class (when \(E_H(b,c)\) is true), or consists of pairwise distinct singleton classes (when it is false).

Every assignment to \((y,z)\) in the new structure has the same full atomic type over the fixed witness tuple as an assignment in \(H\). If both variables lie in \(U\), retain the assignment. If just one lies in \(C\), represent it by \(b\); all witness incidences match. If the two variables are the same member of \(C\), use \((b,b)\). If they are distinct members of \(C\), use \((b,c)\). The transposition of \(b,c\) ensures the appropriate orientations for mixed assignments. Hence the quantifier-free matrix \(\psi\) remains true everywhere, and the new structure satisfies \(\Phi\).

Given \(n\ge k+2\), take \(s=n-u\ge2\). The resulting model has exactly \(n\) elements, proving the cofinite tail and the finite-spectrum upper bound.

**4. Sharpness for every \(k\).** For \(k\ge1\), take \(k\) existential witnesses in pairwise distinct \(E\)-classes. Require, by a quantifier-free matrix universally quantified over \(y,z\), that (i) for each \(i\), any two members of the \(E\)-class of \(x_i\) other than \(x_i\) are equal; and (ii) any two members of classes meeting no witness are equal. An explicit matrix is
\[
\begin{aligned}
\theta_k(\bar x,y,z)={}&\bigwedge_{1\le i<j\le k}\neg E(x_i,x_j)\\
&{}\land\bigwedge_{i=1}^k
\bigl[(E(y,x_i)\land y\ne x_i\land E(z,x_i)\land z\ne x_i)\to y=z\bigr]\\
&{}\land\bigl[(\bigwedge_{i=1}^k\neg E(y,x_i))\land(\bigwedge_{i=1}^k\neg E(z,x_i))\to y=z\bigr].
\end{aligned}
\]
Each marked class contains the witness and at most one other point, and there is at most one point outside all marked classes. Thus any model has at most \(2k+1\) elements and at least \(k\). Conversely, independent choices to add zero or one further member to each marked class, and zero or one unmarked singleton, realize every order from \(k\) to \(2k+1\). For \(k=0\), \(\forall y\forall z\,(y=z)\) has only a one-element model. This proves sharpness.

## Verification

The inequalities have been checked at both boundaries: \(u\le k\) and \(t\le u\), so \(2k+2-u\ge k+2>t+1\) (with the final inequality holding also when \(u=k\) and \(t=k\)). Both cases for the relation among the chosen outside elements were analyzed; cloning preserves transitivity in the marked and unmarked cases. A comparison of all atomic types in one and two outside variables proves the conclusion for every quantifier-free Boolean matrix, not only for positive formulas. The sharpness theory is a concrete finite equivalence-class construction for arbitrary \(k\). No finite experiment is used to infer an infinite result.

## Relationship to prior work

The finite/cofinite spectrum theorem for Bernays–Schönfinkel graph sentences is classical, as surveyed by Pikhurko and Verbitsky. A related exact result for the \(\exists^k\forall^2\) fragment on **arbitrary simple graphs** gives the different sharp bound \(k+2^k\). Here equivalence classes collapse the \(2^k\) general adjacency profiles into at most \(t+1\le k+1\) profiles, yielding a strictly smaller optimal **linear** bound for \(k\ge2\). This is not implied by the numerical general-graph cutoff: its extremal graph constructions need not be disjoint unions of cliques.

Sankaran and Chakraborty study semantic extensions of the Bernays–Schönfinkel class with finite/cofinite spectra, but not this precise sharp equivalence-structure cutoff. Fiuk studies finite-model bounds for guarded logic; its objects and quantifier regime are different and provide contemporary motivation for explicit spectrum thresholds rather than an implication of the result proved here.

## Limitations

The theorem applies to one equivalence symbol, no other nonlogical predicates or functions, and exactly two universally quantified variables. Extra unary predicates may split each marked/unmarked class into additional profiles; a third universal variable can inspect triples of outside elements, so the same bound is not asserted there. Although the result supplies an exact finite-spectrum endpoint, it does not determine a general complexity class for input formulas. The sharpening may have appeared in earlier unindexed equivalence-relation model-theory literature; a targeted literature and database search cannot certify absolute priority.

## References

1. Oskar Fiuk, *Random Models and Guarded Logic*, arXiv:2601.05247v1, first publicly posted 8 January 2026, https://arxiv.org/abs/2601.05247.
2. Abhisekh Sankaran and Supratik Chakraborty, *On Semantic Generalizations of the Bernays-Schönfinkel-Ramsey Class with Finite or Co-finite Spectra*, arXiv:1002.4334v2, https://arxiv.org/abs/1002.4334.
3. Oleg Pikhurko and Oleg Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865v4, Section 7.3, https://arxiv.org/abs/1003.4865.
4. *Sharp finite-spectrum cutoff for \(\exists^k\forall^2\) graph sentences*, published-finding corpus public mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-finite-spectrum-cutoff-for-exists-k-forall-2-graph-sentenc--86f3d437f099.

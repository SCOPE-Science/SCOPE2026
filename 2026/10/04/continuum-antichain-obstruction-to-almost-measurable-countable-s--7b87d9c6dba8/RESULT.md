# Continuum antichain obstruction to almost-measurable countable-sentential models
## Finding

Consider the infinitary classical sentential language used in Cosyns's 2026 modal-sentential framework. It has at least countably many distinct propositional variables and admits countable conjunctions. Let \(\mathfrak A\) be its Lindenbaum--Tarski Boolean algebra modulo classical logical equivalence.

Then \(\mathfrak A\) contains a pairwise disjoint family of cardinality
\[
2^{\aleph_0}.
\]
Consequently \(\mathfrak A\) does not satisfy the countable chain condition.

The paper defines an **almost measurable** Lindenbaum--Tarski algebra to be one satisfying the countable chain condition together with weak countable distributivity. Therefore, under the paper's stated language assumptions, there are no almost measurable Lindenbaum--Tarski algebras at all. In particular, the model classes subsequently defined by taking such an algebra as their first component have no instances.

## Assumptions and scope

The language has a family of variables containing distinct
\[
p_0,p_1,p_2,\ldots
\]
and admits conjunctions indexed by \(\omega\). Logical equivalence is the ordinary classical equivalence used to form the Lindenbaum--Tarski algebra. Equivalently, one may use the paper's stated freeness property: every assignment of the propositional generators into the two-element Boolean algebra extends to a homomorphism.

The conclusion concerns the framework exactly as stated with \(\kappa\ge\omega\). It does not say that related constructions are impossible after changing the language, quotient, or notion of admissible algebra. For example, a finite-variable language without enough independent countable choices would require a separate analysis.

## Proof

Choose pairwise distinct variables \(p_n\) for \(n\in\omega\). For every binary sequence \(x\in2^\omega\), define the literal
\[
\ell_n^x=
\begin{cases}
p_n,&x(n)=1,\\
\neg p_n,&x(n)=0,
\end{cases}
\]
and the formula
\[
F_x=\bigwedge_{n\in\omega}\ell_n^x.
\]
This is a well-formed formula because countable conjunctions are allowed.

First, \([F_x]\ne0\). Indeed, assign the selected variables by \(p_n\mapsto x(n)\) in the two-element Boolean algebra and assign arbitrary values to the remaining variables. Under the ordinary classical evaluation, every literal \(\ell_n^x\) receives value \(1\), so the countable conjunction \(F_x\) receives value \(1\). Equivalently, using the freeness property stated for the Lindenbaum--Tarski algebra, this assignment extends to a Boolean homomorphism sending \([F_x]\) to \(1\); hence \([F_x]\) cannot be zero.

Second, if \(x\ne y\), choose \(n\) with \(x(n)\ne y(n)\). One of \(F_x,F_y\) contains \(p_n\) and the other contains \(\neg p_n\). Therefore
\[
[F_x]\wedge[F_y]=0.
\]
Thus
\[
\mathcal A=\{[F_x]:x\in2^\omega\}
\]
is a family of nonzero pairwise disjoint elements. Distinct sequences yield distinct elements because equal nonzero elements cannot have zero meet. Hence
\[
|\mathcal A|=2^{\aleph_0}.
\]

The countable chain condition requires every pairwise disjoint family of nonzero elements to be countable. The family \(\mathcal A\) violates this requirement, so the Lindenbaum--Tarski algebra is not c.c.c.

Cosyns defines an almost measurable Lindenbaum--Tarski algebra by imposing the c.c.c. condition (together with weak countable distributivity) on this same infinitary Lindenbaum--Tarski algebra. Since the c.c.c. already fails, no such almost measurable algebra exists. Definitions of the subsequent classical and modal models require an almost measurable Lindenbaum--Tarski algebra as their first component, so those model classes are empty under the stated assumptions.

## Verification

The proof uses only the language formation rule for countable conjunctions, the existence of countably many distinct variables, and ordinary Boolean evaluation. No set-theoretic hypothesis beyond the usual existence of the Cantor set \(2^\omega\) is needed.

The bundled checker verifies the finite skeleton of the argument: for each \(1\le d\le12\), the \(2^d\) complete conjunctions of \(d\) literals are all satisfiable and pairwise incompatible. This computation is not used as a proof of the continuum statement; it only checks the finite pattern from which the general construction is defined.

## Relationship to prior work

The 2026 paper explicitly fixes \(\kappa\ge\omega\), permits countable conjunctions and disjunctions, forms the associated \(\sigma\)-complete Lindenbaum--Tarski Boolean algebra, and defines the countable chain condition by requiring every disjoint family to be at most countable. It then defines “almost measurable” Lindenbaum--Tarski algebras by adding that c.c.c. requirement and uses such algebras as the first component of its classical and modal models.

The author's earlier thesis contains the same setup and also notes, for the countably generated case, an atomicity/cardinality description closely related to the obstruction. However, neither the thesis nor the 2026 paper states the uniform \(2^{\aleph_0}\)-sized antichain construction for every allowed \(\kappa\ge\omega\), nor draws the resulting conclusion that the almost-measurable and derived model classes are empty.

Classical work of Rieger on free \(\aleph_\xi\)-complete Boolean algebras provides background on the infinitary Boolean algebras involved. The present point is the direct implication of the new framework's own language assumptions for its c.c.c.-based model class.

## Limitations

The result is an obstruction to the framework as presently parameterized, not a nonexistence theorem for all probability-inspired modal semantics. It can be avoided only by changing at least one ingredient responsible for the antichain, such as the supply of independent variables, the availability of countable conjunctions, the equivalence/quotient being used, or the c.c.c. requirement.

The proof does not assess which modification is mathematically preferable, nor whether all later intended conclusions can be recovered after such a modification.

## References

[1] Loïc Cosyns, “On the foundations of logic and probability, I. Modal sentential calculi,” arXiv:2609.28104, 2026.

[2] Loïc Cosyns, *The Modal Logic of the Calculus of Probability*, doctoral thesis, Durham University, 2025.

[3] Ladislav Rieger, “On Free \(\aleph_\xi\)-complete Boolean Algebras (with an application to logic),” *Fundamenta Mathematicae* 38 (1951), 35--52.

# A computable template with a \(\Pi^0_2\)-complete first-obstruction index set

## Finding

There is a computable countably infinite relational template \(\mathbf B=(B;E,H)\), with one binary relation \(E\) and one unary relation \(H\), for which the first failed finite-prefix homomorphism problem is uniformly computably equivalent on indices to the least-missing-number problem for computably enumerable sets. The index set of total computable structures whose every finite initial segment maps to \(\mathbf B\) is \(\Pi^0_2\)-complete.

## Assumptions and scope

Fix an effective enumeration \((M_e)_{e\in\mathbb N}\) of machines and a computable sequence of pairwise distinct primes \((p_e)_{e\in\mathbb N}\). For each pair \((e,t)\), make a component with vertices \((e,t,i)\) for \(0\le i<p_e\), and put directed edges from \((e,t,i)\) to \((e,t,i+1\bmod p_e)\). Put \((e,t,0)\) in \(H\) exactly when \(M_e\) first halts at step \(t\). There are no other edges or unary facts. This gives a computable countably infinite template \(\mathbf B\).

For a computable structure \(\mathbf G\) on domain \(\mathbb N\), write \(\mathbf G\!\upharpoonright n\) for the induced substructure on \(\{0,\ldots,n-1\}\). Define \(\mathsf{FirstBad}_{\mathbf B}\) to return the least \(n\ge1\) such that \(\mathbf G\!\upharpoonright n\not\to\mathbf B\), or \(\infty\) if every finite prefix maps. Define \(\mathsf{MinMissing}(e)=\min(\mathbb N\setminus W_e)\) when this complement is nonempty, and \(\infty\) when \(W_e=\mathbb N\), where \((W_e)\) is a standard enumeration of the c.e. sets. The index-set completeness claim is made on the promise that the input index describes a total computable structure.

## Proof

**Step 1: the finite gadget codes halting.** Let \(A_e\) be a directed cycle of length \(p_e\), with its vertex \(0\) marked by \(H\). A homomorphism from a directed cycle of length \(p_e\) to a directed cycle of length \(p_d\) exists only if \(p_d\mid p_e\): following the image around the source cycle advances one step modulo \(p_d\), and closure requires divisibility. Since both numbers are prime and the primes are pairwise distinct, the target component must have index \(d=e\). The unary mark then requires a component \((e,t)\) whose vertex \(0\) belongs to \(H\). Such a component exists exactly when \(M_e\) halts. Hence

\[
A_e\to\mathbf B\quad\Longleftrightarrow\quad M_e\text{ halts}.
\]

It follows that \(\operatorname{CSP}(\mathbf B)\) is c.e.-complete: membership is c.e. by enumerating all finite tuples of target vertices and checking the homomorphism constraints, and the map \(e\mapsto A_e\) reduces the halting set to it.

**Step 2: reduce first bad prefix to least missing c.e. number.** For a total computable \(\mathbf G\), let
\[
W_{\mathbf G}=\{n\in\mathbb N:\mathbf G\!\upharpoonright n\to\mathbf B\},
\]
including \(n=0\), whose empty structure maps vacuously. This set is c.e., because a homomorphism is a finite tuple witness and \(\mathbf B\) is computable. It is downward closed: a homomorphism on a prefix restricts to every shorter prefix. Therefore \(\mathsf{MinMissing}(W_{\mathbf G})\) is exactly \(\mathsf{FirstBad}_{\mathbf B}(\mathbf G)\), including the all-prefixes-map case. This transformation is uniform in an index for \(\mathbf G\).

**Step 3: reduce least missing number to first bad prefix.** Given an index \(e\) for a c.e. set \(W_e\), uniformly obtain, for each \(i\), a machine index \(q(e,i)\) that halts exactly when \(i\in W_e\). Build a computable structure \(\mathbf G_e\) as the disjoint union, in successive finite intervals, of the gadgets \(A_{q(e,0)},A_{q(e,1)},\ldots\). The interval lengths \(p_{q(e,i)}\) and their cumulative endpoints are computable from \(e,i\). A component maps to \(\mathbf B\) exactly when its index \(i\) belongs to \(W_e\). Every prefix of a map-able component also maps by restriction. Thus all prefixes of \(\mathbf G_e\) map if and only if \(W_e=\mathbb N\). If \(k=\min(\mathbb N\setminus W_e)\), the first bad prefix lies strictly after the start of component \(k\) and no later than its endpoint. Its output length therefore identifies \(k\) by the computable interval boundaries. This gives the reverse uniform reduction.

**Step 4: the index-set complexity.** For any total computable \(\mathbf G\), the statement that every prefix maps has the form “for every \(n\), there exists a finite homomorphism witness,” so it is \(\Pi^0_2\). The construction \(e\mapsto\mathbf G_e\) reduces the \(\Pi^0_2\)-complete set \(\{e:W_e=\mathbb N\}\) to this promised index set. Hence it is \(\Pi^0_2\)-complete.

## Verification

The proof uses only the divisibility condition for homomorphisms between directed cycles, the decidability of bounded halting, and uniform enumeration of finite homomorphism witnesses. The all-prefix statement is proved by a uniform reduction, not by finite experimentation. The least-missing-number equivalence is an index-level computable reduction in both directions; no Weihrauch-degree claim is made.

## Relationship to prior work

Research on countable-template constraint satisfaction establishes that infinite templates can have substantially richer complexity than finite templates. The present statement is more specific: it identifies the exact least-missing-number index problem for the first failed finite prefix of one explicit computable template. The construction is deliberately non-homogeneous and does not fall under classifications whose hypotheses require countable homogeneity or \(\omega\)-categoricity. The cited recent work provides context for infinite-template complexity but does not state this exact first-prefix equivalence in its inspected abstract.

## Limitations

The result concerns one explicit countably infinite template with one binary and one unary relation. It does not classify first-obstruction problems for all infinite templates, and it does not claim an exact Weihrauch degree. The index-set statement is a promise result for total computable presentations; no claim is made about indices of partial programs.

## References

1. M. Bodirsky, D. Bradley-Williams, E. Hrushovski, and C. Spiess, “A Non-Dichotomy for CSPs of Stable \(\omega\)-Categorical Structures,” arXiv:2610.19940 (2026).
2. M. Bodirsky and J. Nešetřil, “Constraint Satisfaction with Countable Homogeneous Templates,” *Journal of Logic and Computation* 16(3) (2006), 359–373. DOI: 10.1093/logcom/exi083.

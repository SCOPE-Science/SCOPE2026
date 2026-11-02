# Eight-element Boolean preconditionals: exact census and first unavoidable multivalued selection

## Finding

On the labelled Boolean algebra \(\mathcal P(\Omega)\), with \(\Omega=\{0,1,2\}\), there are exactly **1,235** binary operations satisfying the five preconditional axioms, conditional identity, modus ponens, and finite-meet preservation in the consequent. These operations form exactly **227** isomorphism classes under relabelling the three atoms. Exactly **283** admit a functional (possibly partial) selection representation on the same atomic carrier, while **952** necessarily have a multivalued selection fiber. No such multivalued fiber is possible on any smaller nontrivial finite Boolean algebra. Thus the eight-element Boolean algebra is the smallest Boolean algebra exhibiting this distinction in the stated variety of conditional operations.

## Assumptions and scope

For any nonempty finite set \(\Omega\), write \(1=\Omega\), \(0=\varnothing\), \(A\wedge B=A\cap B\), and \(A\le B\) for inclusion. A binary operation \(\Rightarrow:\mathcal P(\Omega)^2\to\mathcal P(\Omega)\) is required to satisfy, for all \(A,B,C\subseteq\Omega\), the five preconditional axioms

\[
\begin{aligned}
\text{(P1)}\quad&1\Rightarrow B\subseteq B,\\
\text{(P2)}\quad&A\cap B\subseteq A\Rightarrow B,\\
\text{(P3)}\quad&A\Rightarrow B\subseteq A\Rightarrow(A\cap B),\\
\text{(P4)}\quad&A\Rightarrow(B\cap C)\subseteq A\Rightarrow B,\\
\text{(P5)}\quad&A\Rightarrow((A\cap B)\Rightarrow C)\subseteq(A\cap B)\Rightarrow C,
\end{aligned}
\]

and the additional laws

\[
\begin{aligned}
\text{(Id)}\quad&A\Rightarrow A=1,\\
\text{(MP)}\quad&A\cap(A\Rightarrow B)\subseteq B,\\
\text{(N)}\quad&A\Rightarrow(B\cap C)=(A\Rightarrow B)\cap(A\Rightarrow C).
\end{aligned}
\]

Here (N) is consequent-meet normality. A selection representation is a family of sets \(R_A(x)\subseteq\Omega\), indexed by \(A\subseteq\Omega\) and \(x\in\Omega\), with

\[
x\in A\Rightarrow B\quad\Longleftrightarrow\quad R_A(x)\subseteq B.
\]

It is *functional* if \(|R_A(x)|\le1\) for every pair \((A,x)\). Empty fibers are permitted; requiring total selection would define a different class. All counts concern operations on a **fixed labelled carrier** except the count of isomorphism classes.

## Proof

**1. Uniquely determined selection fibers.** From (P3) and (P4), \(A\Rightarrow B=A\Rightarrow(A\cap B)\). Axioms (P2), (Id), and (N) give \(A\Rightarrow1=1\), while (N) says each coordinate map \(B\mapsto\mathbf1_{\{x\in A\Rightarrow B\}}\) preserves finite intersections. Its inverse image of true is therefore a principal filter of the finite Boolean lattice, with a unique least member \(R_A(x)\). Equality with the \(A\)-relative consequent forces \(R_A(x)\subseteq A\). Moreover (P2) and (MP) imply

\[
R_A(x)=\{x\}\quad\text{if }x\in A;
\qquad R_\varnothing(x)=\varnothing.
\]

In particular \(R_1(x)=\{x\}\), which gives (P1). Conversely, every fiber family with these fixed values and the condition below defines an operation satisfying all stated axioms.

**2. Exact nonstandard constraint.** Put \(D=A\cap B\). For all \(C\), the left side of (P5) contains \(x\) exactly when \(\bigcup_{y\in R_A(x)}R_D(y)\subseteq C\). Thus (P5) for all consequents is *equivalent* to

\[
\boxed{R_D(x)\subseteq\bigcup_{y\in R_A(x)}R_D(y)
\quad\text{for every }D\subseteq A\subseteq\Omega,\ x\in\Omega.}
\tag{1}
\]

This is the finite relational strong-density constraint (not claimed as a new general representation theorem).

**3. Reduction to six bits and three four-way choices.** On \(\Omega=\{0,1,2\}\), the only free fibers are six singleton-antecedent fibers and three two-element-antecedent fibers. For distinct \(u,v\) let \(t_{u,v}\in\{0,1\}\) satisfy

\[
R_{\{u\}}(v)=
\begin{cases}\{u\},&t_{u,v}=1,\\\varnothing,&t_{u,v}=0.\end{cases}
\]

For each \(w\), let \(\{u,v\}=\Omega\setminus\{w\}\) and \(S_w=R_{\{u,v\}}(w)\in\{\varnothing,\{u\},\{v\},\{u,v\}\}\). All instances of (1) are automatic except those where \(A\) has two elements, \(D\) is one of its singleton subsets, and \(x\) is the missing atom. Their complete requirements are

\[
\begin{aligned}
t_{u,w}=1&\ \Longrightarrow\ (u\in S_w)\ \lor\ ((v\in S_w)\land t_{u,v}=1),\\
t_{v,w}=1&\ \Longrightarrow\ (v\in S_w)\ \lor\ ((u\in S_w)\land t_{v,u}=1).
\end{aligned}
\tag{2}
\]

Define \(c_w(t)\) as the number of four candidate subsets \(S_w\) satisfying the two implications (2). The choices for distinct missing atoms are independent once the six bits are fixed, so the complete labelled census is

\[
\boxed{N_3=\sum_{t\in\{0,1\}^{6}}\prod_{w\in\Omega}c_w(t)=1235.}
\tag{3}
\]

The product distribution over all 64 assignments has, respectively, the value/frequency pairs
\[
(8,8),(9,3),(12,6),(16,15),(18,12),(24,6),
(27,4),(32,6),(36,3),(64,1).
\]
These frequencies sum to 64, and their frequency-weighted sum is 1,235.

**4. Isomorphism, functional count, and minimality.** Every algebra automorphism of \(\mathcal P(\Omega)\) is an atom permutation. Directly imposing invariance on the six bits and three subsets gives **1,235** operations fixed by the identity, **35** by each transposition, and **11** by each three-cycle. Burnside's lemma yields
\[
\boxed{N_3^{\mathrm{iso}}=(1235+3\cdot35+2\cdot11)/6=227.}
\]
Restricting each admissible \(S_w\) to size at most one, and applying the identical exact enumeration, yields **283** functional operations; subtraction gives \(1235-283=952\) operations with an unavoidable multivalued fiber. The uniqueness of the principal-filter generators \(R_A(x)\) rules out an alternative functional selection on the same atomic carrier. For \(|\Omega|\le2\), every nontrivial proper antecedent is a singleton, and each free \(R_A(x)\subseteq A\) automatically has size at most one. The complete operation counts for one and two atoms are respectively \(1\) and \(4\). These observations prove the sharp eight-element carrier threshold.

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. It enumerates the \(4,096\) possible free-fiber assignments on three atoms and all \(5\) assignments for smaller carriers. It checks the strong-density criterion and *separately* evaluates the original five preconditional axioms and three added laws for every candidate. It independently evaluates the 64-term formula (3), the functional restriction, all six permutation-fixed counts, and Burnside's formula. Running `python3 checker.py` gives

`ALL_CHECKS_OK ranks=(1,2,3) candidates=4101 accepted=1235 functional=283 nonfunctional=952 orbits=227`

The finite enumeration is exhaustive because the principal-filter representation proves that every operation in the target class occurs uniquely among these candidates; it is not an extrapolation from sampled operations.

## Relationship to prior work

Holliday's *Preconditionals* introduced the relevant algebraic laws and explained strongly dense relational selection frames. Chen's *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations* develops preconditional algebra semantics and demonstrates why additional conditional identities must be specified. Those general results are explicitly used; the finite relational representation and its strong-density condition are not asserted to be new.

The claims here are the complete **three-atom labelled and isomorphism census**, the functional/nonfunctional split, and the **first-cardinality threshold** for nonfunctional selectors under the stated additional MP and normality laws. Finite-chain enumeration concerns a different lattice family; permutation-equivariant subclasses do not determine this unrestricted census. A matching older enumeration under unsearched terminology cannot be excluded.

## Limitations

This is a complete result for Boolean algebras with at most three atoms, not an enumeration for four or more atoms. The characterization by (1) is valid for arbitrary *finite* Boolean carriers, but the closed numerical census is not extended beyond three atoms. The threshold depends on allowing partial functional selection and on requiring (Id), (MP), and (N); it does not assert a threshold for arbitrary preconditionals or for different non-Boolean lattices. The comparisons do not prove historical uniqueness. No independent external validation has been performed.

## References

1. W. H. Holliday, *Preconditionals*, arXiv:2402.02296 (2024), especially the algebraic axioms and relational selection semantics. https://arxiv.org/abs/2402.02296
2. Z. Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221, first posted 22 July 2026, especially the finite preconditional algebra axioms. https://arxiv.org/abs/2607.20221

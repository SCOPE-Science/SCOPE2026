# Catalan census and relational collapse of finite-chain constructive neighbourhood modalities

## Finding

Fix an integer \(n\geq1\) and the labelled intuitionistic chain \(C_n=\{0<1<\cdots<n-1\}\). A **proper inhabited constructive neighbourhood frame** assigns to each world \(i\) a nonempty family \(N(i)\) of nonempty subsets of \(C_n\). Modal formulas use the persistent constructive-neighbourhood semantics specified below.

Two frames are **observationally equivalent** when they induce exactly the same pair of unary operations \(\Box,\Diamond\) on the full Heyting algebra of upsets of \(C_n\). Equivalently, every modal formula has the same truth set in the two frames under every shared persistent valuation.

**Theorem.** Define, for each world,
\[
\alpha_i=\max_{U\in N(i)}\min U,\quad
\gamma_i=\min_{U\in N(i)}\max U,\quad
b_i=\min_{j\ge i}\alpha_j,\quad
d_i=\min_{j\ge i}\gamma_j.
\]
The pair of sequences \((b,d)\) is a complete and unique observational invariant. Every ordered pair of weakly increasing sequences of length \(n\) with entries in \(\{0,\ldots,n-1\}\) occurs. Consequently the number of observational equivalence classes is exactly
\[
\boxed{Q_n=\binom{2n-1}{n}^{\!2}.}
\]
The frame validates the modal axiom \(\mathsf D:\ \Box p\to\Diamond p\), for all persistent valuations, **if and only if**
\[
\boxed{b_i\le d_i\quad\text{for every }i.}
\]
Every class satisfying \(\mathsf D\) has a canonical representative whose neighbourhood family at world \(i\) consists of the single interval \(\{b_i,b_i+1,\ldots,d_i\}\). Its two modal operators therefore agree on every upset with those of one ordinary serial accessibility relation, interpreted by the same persistent modal clauses.

The exact number of \(\mathsf D\)-valid observational classes is
\[
\boxed{Q_n^{\mathsf D}=\frac{1}{2(n+1)}\binom{2n}{n}^{\!2}
=\frac{2}{n+1}Q_n.}
\]
Thus the proportion is exactly \(2/(n+1)\), and \(Q_n^{\mathsf D}\sim16^n/(2\pi n^2)\). For \(n=1,2,3,4\), the unrestricted counts are \(1,9,100,1225\), and the \(\mathsf D\)-valid counts are \(1,6,50,490\).

The local pairwise-intersection condition on raw neighbourhood families is not necessary for \(\mathsf D\): on \(C_3\), assigning \(N(i)=\{\{0,2\},\{1\}\}\) at each world yields disjoint neighbourhoods but validates \(\mathsf D\), with invariant \(b=d=(1,1,1)\).

## Assumptions and scope

An upset is one of \(X_t=\{t,t+1,\ldots,n-1\}\) for \(0\le t\le n\), where \(X_n=\varnothing\). A valuation sends each propositional atom to an upset. Intuitionistic conjunction and disjunction use intersection and union, and implication uses the ordinary Kripke clause for \(\le\). For arbitrary formula truth set \(X\) the constructive modal clauses are
\[
\begin{split}
i\in\Box X&\iff (\forall j\ge i)(\exists U\in N(j))\;U\subseteq X,\\
i\in\Diamond X&\iff (\forall j\ge i)(\forall U\in N(j))\;U\cap X\ne\varnothing.
\end{split}
\]
These clauses preserve persistence, so every formula has an upset truth set. By assumption, all neighbourhood families are nonempty and contain no empty neighbourhood. In the cited 2026 semantics these raw conditions suffice for the usual \(\mathsf N\) and \(\mathsf P\) frame axioms; on a nonempty finite chain their global validity is also necessary. The count is for **labelled observational equivalence classes**, not the number of raw neighbourhood functions, relations or formula equivalence classes. No reflexivity or confluence restriction is imposed on the neighbourhood choices.

## Proof

### 1. Computing the modal observables

For nonempty \(U\subseteq C_n\), inclusion \(U\subseteq X_t\) holds precisely when \(\min U\ge t\). The family \(N(j)\) contains such a set precisely when \(\alpha_j\ge t\). Taking the universal condition over all \(j\ge i\) gives
\[
\boxed{i\in\Box X_t\iff t\le b_i.}
\]
Similarly, \(U\cap X_t\ne\varnothing\) precisely when \(\max U\ge t\). Every set in \(N(j)\) meets the upset precisely when \(\gamma_j\ge t\). Therefore
\[
\boxed{i\in\Diamond X_t\iff t\le d_i.}
\]
Because the sets of indices \(\{j:j\ge i\}\) shrink with increasing \(i\), each of the sequences \(b\) and \(d\) is weakly increasing. The two displayed equivalences show that they determine both operators on every upset. Conversely, testing the finitely many inputs \(X_t\) uniquely recovers \(b_i\) as the greatest threshold with \(i\in\Box X_t\), and similarly recovers \(d_i\). Equivalence of the one-step operations implies equivalence of the interpretation of *every* formula by structural induction, since the propositional operations and valuations are fixed.

### 2. Realizability of every monotone pair

Take arbitrary nondecreasing sequences \(b,d\) valued in \(\{0,\ldots,n-1\}\). If \(b_i\le d_i\), assign the sole neighbourhood \(\{b_i,\ldots,d_i\}\) at world \(i\); otherwise assign the two singleton neighbourhoods \(\{b_i\}\) and \(\{d_i\}\). In either case direct calculation gives \(\alpha_i=b_i\) and \(\gamma_i=d_i\). Weak monotonicity implies \(\min_{j\ge i}b_j=b_i\) and \(\min_{j\ge i}d_j=d_i\). The resulting observable invariant is therefore exactly the prescribed \((b,d)\). Each sequence is a multiset of size \(n\) from an \(n\)-symbol alphabet, giving \(\binom{2n-1}{n}\) choices independently for each modality and proving \(Q_n\).

### 3. The exact \(\mathsf D\) boundary and canonical representative

For any valuation, the truth set of \(p\) is an upset \(X_t\). The formula \(\Box p\to\Diamond p\) is valid at every world precisely when \(\Box X_t\subseteq\Diamond X_t\) for each \(t\). By the threshold formulas, this holds exactly when \(b_i\le d_i\) for all \(i\): if an inequality fails, \(X_{d_i+1}\) gives \(i\in\Box X_{d_i+1}\) but \(i\notin\Diamond X_{d_i+1}\). If all inequalities hold, no such counterexample exists. When \(b_i\le d_i\), the singleton interval construction of Step 2 is a representative in the same observational class. Its \(N(i)\) is the single interval \(R(i)=[b_i,d_i]\), which is nonempty, hence yields a serial relational representative. Equality of the modal operators proves equality of all formula truth sets; it does not identify the original raw frames.

For the disjoint-family example, \(\max\{\min\{0,2\},\min\{1\}\}=1\) and \(\min\{\max\{0,2\},\max\{1\}\}=1\). These values are constant in \(i\), so \(b_i=d_i=1\), although the two raw neighbourhoods have empty intersection. Hence the familiar pairwise-intersection condition is sufficient but not necessary for this particular finite-chain \(\mathsf D\) validity.

### 4. Exact enumeration

The count is the number of pairs of weakly increasing sequences \((b_i),(d_i)\) on \(\{0,\ldots,n-1\}\) satisfying \(b_i\le d_i\) coordinatewise. Put \(A_i=b_i+1\) and \(B_i=d_i+2\). These form the top and bottom rows of a semistandard Young tableau of rectangular shape \((n,n)\) with entries in \(\{1,\ldots,n+1\}\): both rows are weakly increasing, and each column is strictly increasing because \(A_i<B_i\iff b_i\le d_i\). Conversely, any such tableau gives the unique admissible pair: row strictness enforces that top entries are at most \(n\) and bottom entries at least \(2\). By the standard two-row specialization of the Jacobi--Trudi identity, with \(h_k(1^{n+1})=\binom{n+k}{k}\), the number is
\[
\begin{aligned}
s_{(n,n)}(1^{n+1})
&=\det\begin{pmatrix}h_n&h_{n+1}\\h_{n-1}&h_n\end{pmatrix}\\
&=\binom{2n}{n}^{2}-\binom{2n+1}{n+1}\binom{2n-1}{n-1}\\
&=\frac{1}{2(n+1)}\binom{2n}{n}^{2}.
\end{aligned}
\]
Finally \(\binom{2n-1}{n}=\tfrac12\binom{2n}{n}\), proving the proportion. The central-binomial asymptotic \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) yields the stated asymptotic.

## Verification

Run the standalone Python 3 script `checker.py`; it requires only the standard library. The checker independently enumerates all inhabited proper single-world neighbourhood families for \(n=1,2,3,4\), exhaustively evaluates all raw frames for \(n\le2\), and checks fixed-seed samples of \(30{,}000\) frames at \(n=3\) and \(8{,}000\) at \(n=4\). For every tested frame it interprets both modalities directly on every upset, independently computes the endpoint invariant, tests the normal representative, and checks validity of \(\mathsf D\) against the coordinate inequality. It also enumerates *all* possible monotone sequence pairs through \(n=4\), confirming the exact census and constructive realizability; the disjoint-neighbourhood example is tested separately. The program prints `ALL_CHECKS_OK`.

The full arbitrary-\(n\) theorem is supplied by the preceding symbolic proof; random frame tests are not exhaustive above \(n=2\) and the finite sequence census is not an infinite proof.

## Relationship to prior work

Dalmonte and de Groot (2026, arXiv:2606.31870) give the constructive neighbourhood semantics and sufficient local conditions for modal principles, including \(\mathsf N,\mathsf P,\mathsf D\); their Lemma 2.4 gives the familiar pairwise-intersection sufficient condition for \(\mathsf D\). Dalmonte (2022, arXiv:2210.09937) develops the earlier Wijesekera-style neighbourhood framework. De Groot (2025, arXiv:2507.13746) provides a distinct intuitionistic monotone modal perspective. These papers establish the modal setting, not the finite-chain observational quotient, its exact Catalan-type census, or the shown insufficiency of pairwise intersection as a necessary condition on a chain.

Related finite-chain relational normal forms for confluence-based \(\mathbf{KI}\) frames and for intuitionistic birelational frames classify *relations subject to specific interaction conditions*, rather than observational equivalence classes of all proper inhabited neighbourhood families under the two quantifier-alternating constructive modalities. Their row/column extrema do not determine the modal quotient here, and their raw relation counts do not imply the \(\mathsf D\)-valid class count.

The tableau enumeration relies on the classical Jacobi--Trudi identity; no novelty is claimed for that combinatorial identity or for the underlying semantic clauses.

## Limitations

The theorem fixes a finite **total order** and persistent upsets. On a branching preorder, neighborhoods can distinguish different upward-closed truth sets, so a single min/max threshold need not suffice. The frame conditions N and P exclude empty neighbourhood families and empty members; dropping these conditions changes the endpoint invariants and counts. Canonical single-interval representatives are asserted only for \(\mathsf D\)-valid observational classes and do not identify original raw neighbourhood sets. The result does not assert a general relational completeness theorem for intuitionistic monotone logic, an optimal modal formula-size bound, or any equivalence for arbitrary truth subsets not upward closed. An earlier equivalent classification in algebraic terminology remains a possible originality risk; historical priority has not been independently certified.

## References

[1] T. Dalmonte and J. de Groot, “Intuitionistic Monotone Modal Logic: Proof Theory and Semantics,” arXiv:2606.31870, first publicly posted 30 June 2026, especially Section 2.2 and Lemma 2.4. https://arxiv.org/abs/2606.31870

[2] T. Dalmonte, “Wijesekera-style constructive modal logics,” arXiv:2210.09937, first publicly posted 18 October 2022, especially Section 4 and the neighbourhood interpretations. https://arxiv.org/abs/2210.09937

[3] J. de Groot, “Intuitionistic monotone modal logic via translation,” arXiv:2507.13746, first publicly posted 18 July 2025. https://arxiv.org/abs/2507.13746

[4] I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Clarendon Press, 1995; standard Jacobi--Trudi identity and complete homogeneous symmetric functions.

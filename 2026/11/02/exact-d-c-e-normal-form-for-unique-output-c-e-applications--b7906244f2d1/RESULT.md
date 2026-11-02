# Exact d.c.e. normal form for unique-output c.e. applications

## Finding
Let \(R\subseteq\mathbb N\times\mathbb N\) be computably enumerable (c.e.), and define the partial function \(U_R:\mathbb N\rightharpoonup\mathbb N\) by \(U_R(x)=y\) exactly if \(\{z:(x,z)\in R\}=\{y\}\). Let \(\mathcal U\) consist of all such partial functions as \(R\) varies over c.e. relations. The following is an exact, uniform classification.

**Normal-form theorem.** A partial function \(f\) lies in \(\mathcal U\) if and only if there are a partial computable function \(g\) and a c.e. set \(B\subseteq\operatorname{dom}(g)\) such that
\[
f=g\upharpoonright(\operatorname{dom}(g)\setminus B).
\]
The transformations between an enumeration index for \(R\) and suitable indices for \(g,B\), and in the converse direction, are computable.

**Domain and composition theorem.** The collection of possible domains of functions in \(\mathcal U\) is exactly the class of d.c.e. sets \(A\setminus B\) with \(A,B\) c.e. Moreover, \(\mathcal U\) is closed under extensional composition, with an effective index construction in the above normal form.

**Boundary theorem.** Every total member of \(\mathcal U\) is computable. There exist functions in \(\mathcal U\) whose domains are neither c.e. nor co-c.e., whereas the graph of a total noncomputable characteristic function may be d.c.e. without that function belonging to \(\mathcal U\). Thus the condition “d.c.e. graph” is not an alternative function-level characterization.

## Assumptions and scope
Here \(\mathbb N=\{0,1,2,\ldots\}\), computability is ordinary unrelativized Turing computability, and pairs are coded by a fixed computable bijection. A c.e. relation is an effectively enumerable set of pairs; repeated enumeration of the same pair is immaterial. The set \(\operatorname{dom}(g)\) is c.e. for any partial computable \(g\). A d.c.e. set is, by definition, the difference of two c.e. sets. All claims include empty and finite relations and allow arbitrarily long or nonterminating enumerations. “Uniform” means effective conversion of indices, not a bound on the time before any output is observed.

When a universal c.e. formula enumerates all binary c.e. relations, the theorem applies to its unique-output application scheme at the level of partial functions extentionally represented by indices. It does not assert new intensional combinatory identities.

## Proof
**1. Extraction into a computable selector plus c.e. erasures.** Given an enumeration of \(R\), define \(g(x)\) to be the value of the first pair \((x,y)\) to appear. This procedure is partial computable and its domain is
\[
A=\{x:\exists y\ (x,y)\in R\}.
\]
Let
\[
B=\{x:\exists y\ne z\ ((x,y)\in R\ \wedge\ (x,z)\in R)\}.
\]
The set \(B\) is c.e. by dovetailing the enumeration and watching for two distinct values, and \(B\subseteq A\). For \(x\in A\setminus B\), every output ever enumerated is the first output, so \(U_R(x)=g(x)\). On \(B\), there is more than one possible output, while outside \(A\) there is none. Hence \(U_R=g\upharpoonright(A\setminus B)\). The enumeration of \(R\) computes indices for both \(g\) and \(B\).

**2. Converse construction.** Given partial computable \(g\) and c.e. \(B\subseteq\operatorname{dom}(g)\), enumerate the graph of \(g\). For each \(x\) enumerated into \(B\), wait until \(g(x)\) halts and additionally enumerate \((x,g(x)+1)\). The two outputs are distinct. If \(x\in\operatorname{dom}(g)\setminus B\), precisely one distinct value appears; on \(B\) at least two appear; outside \(\operatorname{dom}(g)\) none appear. The unique-output function of the constructed c.e. relation is exactly \(g\upharpoonright(\operatorname{dom}(g)\setminus B)\). This is uniform in indices. The hypothesis \(B\subseteq\operatorname{dom}(g)\) guarantees that the auxiliary computation terminates on each enumerated erasure input, but the construction would still enumerate a c.e. relation without needing to decide this hypothesis.

**3. Exact domain class.** Step 1 gives every domain as \(A\setminus B\) for c.e. \(A,B\). Conversely, given any c.e. \(A,C\), set \(B=A\cap C\), which is c.e. and contained in \(A\). Let \(g(x)=0\) when \(x\in A\), undefined otherwise. Then \(g\) is partial computable and the normal form has domain \(A\setminus C\). The converse construction realizes it. Thus every and only d.c.e. set occurs.

**4. Composition.** Suppose \(f=g\upharpoonright(A\setminus B)\), with \(A=\operatorname{dom}(g)\), and \(h=k\upharpoonright(C\setminus D)\), with \(C=\operatorname{dom}(k)\), where \(B\subseteq A\) and \(D\subseteq C\) are c.e. Define the partial computable function \(\ell=k\circ g\), with \(L=\operatorname{dom}(\ell)\). Define the c.e. erasure set
\[
E=(B\cap L)\ \cup\ \{x\in L:g(x)\in D\}.
\]
The first piece is an intersection of c.e. sets. To enumerate the second, dovetail computations of \(g(x)\), \(k(g(x))\), and the enumeration of \(D\), printing \(x\) when all relevant positive witnesses have appeared. Thus \(E\) is c.e. and \(E\subseteq L\). For every \(x\), the composition \(h(f(x))\) is defined exactly when \(x\in L\), \(x\notin B\), and \(g(x)\notin D\), and then equals \(\ell(x)\). Therefore
\[
h\circ f=\ell\upharpoonright(L\setminus E)\in\mathcal U.
\]
All operations on indices are effective. Repeated application gives closure under arbitrary finite compositions.

**5. Strict boundaries.** If \(f\in\mathcal U\) is total, its selector \(g\) from Step 1 is total and computes \(f\); conversely every total computable function is represented by its c.e. graph. Let \(K\subseteq\mathbb N\) be a fixed c.e. noncomputable set. For example, the constant-zero function on \(\mathbb N\setminus K\) is in \(\mathcal U\), by taking \(g(x)=0\) everywhere and \(B=K\). Its domain is not c.e. More sharply, let
\[
D=\{2n:n\in K\}\cup\{2n+1:n\notin K\}.
\]
This is d.c.e.: write \(D=A\setminus B\), where \(A=\{2n:n\in K\}\cup\{2n+1:n\in\mathbb N\}\) and \(B=\{2n+1:n\in K\}\). If \(D\) were co-c.e., the even slice of its complement would enumerate \(\mathbb N\setminus K\); if \(D\) were c.e., its odd slice would also enumerate \(\mathbb N\setminus K\). Either alternative contradicts the noncomputability of the c.e. set \(K\). Thus the domain of a suitable constant-zero member of \(\mathcal U\) is neither c.e. nor co-c.e.

Finally, the graph of the total characteristic function \(\chi_K\) is d.c.e., since it equals
\[
(\mathbb N\times\{0\}\ \cup\ K\times\{1\})\setminus(K\times\{0\}).
\]
But \(\chi_K\) is not computable and so cannot belong to \(\mathcal U\), by totality. This separates the function classification from the weaker graph-complexity statement.

## Verification
The proof in Steps 1–5 is independent of finite tests. The accompanying `checker.py` enumerates all \(2^9=512\) binary relations on a three-element carrier, constructs their first-output and erasure normal forms, verifies reconstruction, and tests the displayed composition identity for all \(512^2=262144\) ordered pairs of relations. Executing it with Python 3 prints `ALL_CHECKS_OK relations=512 composition_pairs=262144`. This is a finite consistency check, not a proof of the infinite c.e. normal form or the existence of a noncomputable c.e. set.

## Relationship to prior work
Shuwei Wang, *A technical note on universal formula pcas* (arXiv:2610.23365, first public October 16, 2026), investigates alternative ways to extract application values from universal \(\Sigma^0_1\) relations. Its unique-output construction includes ordinary partial recursive functions and can have non-c.e. convergence domains. That establishes the motivation and an inclusion/example, but the inspected discussion does not give the full selector-minus-erasure classification, the exact d.c.e. domain class, the uniform extensional composition construction, or the total-function obstruction. The latter statements are the present claim, not the underlying definition of the application or the standard notion of d.c.e. sets.

The basic facts that c.e. sets are halting domains, that finite intersections of c.e. sets remain c.e., and that a noncomputable c.e. set has non-c.e. complement are standard recursion theory. They are used without novelty claims. Earlier treatments under terminology such as “unique-value part of an enumeration” could contain equivalent theorems and remain a historical-priority risk.

## Limitations
The classification is extensional and depends on allowing arbitrary c.e. binary relations and ordinary natural-number outputs. It does not establish which individual elements or terms exist in any fixed presentation of a partial combinatory algebra beyond the universality assumption. It does not identify an optimal program index or decide membership in the class from arbitrary input code. The finite checker cannot certify infinite claims or historical uniqueness. The work has not undergone independent mathematical review.

## References
1. Shuwei Wang, *A technical note on universal formula pcas*, arXiv:2610.23365v1, October 16, 2026. https://arxiv.org/abs/2610.23365
2. Robert I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987 (standard terminology of c.e. sets and their differences).

# Order-convex disagreement sets for three-valued dependence-like formulas

## Finding
Let \(K=\{0,u,1\}\), with truth order \(0<u<1\), negation \(\neg0=1\), \(\neg u=u\), \(\neg1=0\), and conjunction and disjunction given by minimum and maximum in the truth order. For every integer \(k\geq1\), give \(K^k\) the **information order**: \(u\preceq0\) and \(u\preceq1\), with \(0\) and \(1\) incomparable, coordinatewise. Write \(\mathbf u=(u,\ldots,u)\). For two constant-free formulas \(\varphi,\psi\) built from \(p_1,\ldots,p_k\) with \(\wedge,\vee,\neg\), define their exact-value disagreement set by
\[
D(\varphi,\psi)=\{a\in K^k:\llbracket\varphi\rrbracket(a)\ne\llbracket\psi\rrbracket(a)\}.
\]
**Theorem.** A subset \(D\subseteq K^k\) is such a disagreement set if and only if it is order-convex under \(\preceq\) and \(\mathbf u\notin D\). Here order-convex means that \(a,c\in D\) and \(a\preceq b\preceq c\) imply \(b\in D\). The same characterization holds if the infectious conditional of the propositional languages \(K_3^d\) and \(LP^d\) is allowed.

In particular, for uniformly distributed independent values in \(K\), the exact probability that two formulas agree has the **complete fixed-arity spectrum**
\[
\left\{\frac{j}{3^k}:1\leq j\leq 3^k\right\}.
\]
Across positive finite arities the complete spectrum consists of all strictly positive triadic rationals in \([0,1]\); zero is not attainable. For one and two variables every subset of the noncentral valuations is a possible disagreement set (respectively \(4\) and \(256\) sets). Non-convex obstructions first arise with three variables. The exact number of realizable disagreement sets for three labeled variables is \(3{,}886{,}222\), established by an exhaustive independent order-convexity count, with the characterization giving realizability.

## Assumptions and scope
There are at least one and finitely many propositional variables; constants are not part of the signature. The equality relation compares the *entire* three-valued output, not just designatedness in a consequence relation. The designation choice distinguishes \(K_3^d\) and \(LP^d\) for validity, but it does not change this exact-value theorem. The additional conditional has the term definition, under the stated truth operations,
\[
a\to b=(\neg a\vee b)\wedge(a\vee\neg a)\wedge(b\vee\neg b).
\]
It agrees with classical material implication on crisp inputs and returns \(u\) whenever an input is \(u\); thus it adds no term functions. This is the definability fact in Petrukhin's 2026 semantics, and it also follows by direct inspection of the nine input pairs.

## Proof
**Necessity.** Each primitive operation preserves the information order: \(\neg\) fixes \(u\) and exchanges the two maximal points, while \(\wedge\) and \(\vee\) preserve the refinement of each input from \(u\) to a crisp value. Consequently every term function \(f:K^k\to K\) is information-monotone. Each term maps \(\mathbf u\) to \(u\) by induction, so no disagreement contains \(\mathbf u\).

Let \(f,g\) be two term functions and suppose \(a\preceq b\preceq c\), with \(f(a)\ne g(a)\) and \(f(c)\ne g(c)\). If \(f(b)=g(b)=u\), information-monotonicity forces \(f(a)=g(a)=u\), contradiction, because \(u\) is the least output value in the information order. If \(f(b)=g(b)\) is crisp, the crisp output is maximal, so monotonicity forces \(f(c)=g(c)\), contradiction. Hence \(f(b)\ne g(b)\), proving convexity.

**Sufficiency.** Fix an arbitrary order-convex set \(D\subseteq K^k\) not containing \(\mathbf u\). If \(D=\varnothing\), take two copies of \(p_1\). Otherwise put \(U=\uparrow D\), the upward closure in the information order, and \(V=U\setminus D\). Both \(U\) and \(V\) are upsets, \(V\subseteq U\), and \(\mathbf u\notin U\). Indeed, if \(x\in V\), \(y\succeq x\), and \(y\in D\), choose \(d\in D\) with \(d\preceq x\); then \(d\preceq x\preceq y\) contradicts convexity.

For each noncentral \(a\in K^k\), let \(\alpha_a\) be the conjunction of those literals \(p_i\) for which \(a_i=1\), and \(\neg p_i\) for which \(a_i=0\); at least one literal occurs. Its output is \(1\) exactly on \(\uparrow a\). Define \(A=\bigvee_{a\in U}\alpha_a\). The set where \(A\) takes value \(1\) is exactly \(U\). If \(V\ne\varnothing\), define \(B=\bigvee_{v\in V}\alpha_v\). Otherwise define \(B=A\wedge\neg A\). In either case \(B\leq A\) in the truth order, and the set where \(B\) takes value \(1\) is exactly \(V\). Now choose
\[
\varphi=A\vee\neg A,\qquad \psi=B\vee\neg A.
\]
At points of \(U\setminus V=D\), the output of \(\varphi\) is \(1\) but that of \(\psi\) is less than \(1\). On \(V\) both outputs are \(1\). Outside \(U\), if \(A=0\) both are \(1\), while if \(A=u\) both are \(u\) because \(B\leq A\). Hence the disagreement set is exactly \(D\). This is an explicit finite formula construction and completes the characterization.

**Probability spectrum and arity boundary.** The value \(\mathbf u\) is always an agreement assignment, yielding probability at least \(1/3^k\). Every upset of \(K^k\setminus\{\mathbf u\}\) is convex and thus realizable; choosing initial segments of a reverse linear extension gives upsets of every cardinality from \(0\) to \(3^k-1\). Their complements therefore realize every agreement count from \(1\) through \(3^k\). For \(k=1\) and \(k=2\), the punctured information poset has no chain with three points; every subset avoiding the least point is convex. For \(k=3\), the two-point set \(\{(0,u,u),(0,0,0)\}\) is not convex because it omits \((0,0,u)\) between its elements.

## Verification
The proof holds for arbitrary positive finite arity and does not infer infinite or universal statements from enumeration. Standalone `verify.py` exhausts all two-variable term functions, their pairwise disagreement sets, and the constructive converse for all \(256\) possible sets. It finds \(82\) distinct constant-free two-variable term functions and exactly \(256\) disagreement sets. Standalone `verify_convex3.cpp` enumerates all \(2^{26}\) subsets of the three-variable valuation cube avoiding its least point and tests every possible missing interval point. It counts exactly \(3{,}886{,}222\) convex sets. Compile and run the latter using `g++ -O3 -std=c++17 verify_convex3.cpp -o verify_convex3 && ./verify_convex3`; run the former using `python3 verify.py`.

## Relationship to prior work
Petrukhin's 2026 paper introduces the three-valued dependence-like logics and the relevant definability of their conditional; it does not assert the classification of exact equality/disagreement loci. Cardó's 2026 paper defines probabilistic equational spectra for finite algebras and proves general results under hypotheses such as primality, but does not compute this three-valued Kleene algebra's exact spectrum. Berman and Mukaidono's 1984 work enumerates free Kleene-algebra term functions; known two- and three-generator term-function counts are not the same object as the counts of pairwise equality loci. Unlike the previously established constant-free positive classical Boolean result, the present theorem uses the three-valued information order, permits negation, and addresses both three-valued consequence-matrix expansions. The Boolean result does not imply these new equality loci or triadic probabilities. The present construction is self-contained and does not require a preexisting normal-form classification.

## Limitations
The theorem concerns exact-valued pointwise equations without truth constants. It does not classify semantic consequence based only on designated values, languages with additional independent connectives, or weighted/nonuniform assignments. The three-variable number is a reproducible finite enumeration, not a closed formula for counts at arbitrary arity. Potential priority overlap with the older fuzzy-switching literature cannot be fully excluded because the Berman--Mukaidono full article was not accessible in the present literature check; accessible metadata and secondary count records were considered, but no whole-document noncoverage inference was made.

## References
1. Yaroslav Petrukhin, *On Three-Valued Dependence-Like Logics*, arXiv:2610.08293, initially submitted 2026-10-06. https://arxiv.org/abs/2610.08293.
2. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446, initially submitted 2026-04-09. https://arxiv.org/abs/2604.08446.
3. Joel Berman and Masao Mukaidono, *Enumerating fuzzy switching functions and free Kleene algebras*, *Computers & Mathematics with Applications* **10** (1984), 25–35, DOI:10.1016/0898-1221(84)90083-X.
4. OEIS A268534, *Size of free Kleene algebra on n generators*, https://oeis.org/A268534 (secondary confirmation of previously known term counts, not a source for the theorem).

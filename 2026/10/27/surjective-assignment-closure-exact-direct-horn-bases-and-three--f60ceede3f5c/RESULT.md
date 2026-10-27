# Surjective-assignment closure: exact direct Horn bases and three-colour lattice counts

## Finding

**Theorem.** Let \(n>q\ge3\) be integers. Write \(E=[n]\times[q]\), and regard each surjection \(f:[n]\to[q]\) as the \(n\)-element subset \(M_f=\{(i,f(i)):i\in[n]\}\) of \(E\). Set
\[
\operatorname{cl}(S)=\bigcap_{M_f\supseteq S}M_f,
\]
with an empty intersection interpreted as all of \(E\). An implication \(P\to B\) is valid when \(B\subseteq\operatorname{cl}(P)\), and a basis is **simultaneously direct** when
\[
\operatorname{cl}(S)=S\cup\bigcup_{P\to B:\,P\subseteq S}B
\quad\text{for every }S\subseteq E.
\]
Multi-attribute conclusions are allowed, and the cost is the number of implications (not the number of concluded atoms).

**(a) Closed sets.** Besides \(E\), the closed subsets are exactly the graphs of surjection-extendible partial functions \(p:D\to[q]\) **except** those with one unassigned input and precisely one colour absent from the image. An extendible partial function with \(r=n-|D|\) empty positions and \(s=q-|p(D)|\) missing colours exists precisely when \(s\le r\). The excluded near-complete partial functions each close by forcing the unique missing colour at the unique empty position.

**(b) Exactly three families of irreducible direct premises.** Every inclusion-minimal premise that entails some atom not already in the premise belongs to exactly one of these families:

1. A **same-position conflict**, consisting of two different values at one input.
2. A feasible partial function assigning \(n-1\) positions and using exactly \(q-1\) colours; it forces the omitted colour at the last position.
3. A **minimal surjectivity shortage**: a partial function with \(r\) empty positions, exactly \(r+1\) missing colours, and each colour that is used appearing at least twice.

The first and third families have closure \(E\); the second forces exactly one new atom. Taking one implication with its full required conclusion for each such premise gives a simultaneously direct basis of **minimum cardinality among all simultaneously direct bases**. No assertion is made that it minimizes the cardinality among bases permitted to iterate implications.

Let \(\left\{\!\!\begin{smallmatrix} k\\t\end{smallmatrix}\!\!\right\}_{\ge2}\) denote the number of partitions of a labelled \(k\)-set into \(t\) nonempty blocks, each of size at least two, and let \(\left\{\!\!\begin{smallmatrix} k\\t\end{smallmatrix}\!\!\right\}\) be an ordinary Stirling number of the second kind. The exact optimum is
\[
\boxed{\displaystyle
b_{n,q}=
 n\binom q2+nq(q-1)!\left\{\!\!\begin{matrix}n-1\\q-1\end{matrix}\!\!\right\}
+\sum_{r=0}^{q-2}\binom nr\binom q{q-r-1}(q-r-1)!
\left\{\!\!\begin{matrix}n-r\\q-r-1\end{matrix}\!\!\right\}_{\ge2}.}
\]
The associated Stirling numbers obey
\[
T(k,t)=tT(k-1,t)+(k-1)T(k-2,t-1),\qquad T(0,0)=1,
\]
with impossible indices interpreted as zero.

**(c) Three-colour specialization.** For every \(n\ge4\), the exact direct-basis size and the number of closed subsets are
\[
\boxed{b_{n,3}=3(n+2)2^{n-1}-6(n+1),}
\]
\[
\boxed{|\mathcal L_{n,3}|=4^n-3\cdot 2^n-3n2^{n-1}+3n+4.}
\]
In particular \((b_{4,3},|\mathcal L_{4,3}|)=(114,128)\) and \((b_{5,3},|\mathcal L_{5,3}|)=(300,707)\).

## Assumptions and scope

The domain and codomain are labelled finite sets, with \(n>q\ge3\). All positive attribute assertions are of the form \((i,a)\), meaning that the function takes value \(a\) at \(i\). **No negative literals** or auxiliary attributes are permitted in a basis. Closure after one round evaluates every premise against the **original** set \(S\), without using conclusions added during that round. No upper bound is imposed on the size of an implication's conclusion. The inconsistency convention is standard for intersections of an empty family.

A partial function is represented by its graph, and a full surjective function is already closed. The bijective boundary \(n=q\) is outside the new parameter scope; its different combinatorics must not be counted as a separate contribution here. The two-colour boundary requires different minimal-inconsistency bookkeeping and is also excluded.

## Proof

**1. Feasibility and forced values.** Suppose a set of positive assertions is a partial function \(p:D\to[q]\). Write \(r=n-|D|\) and \(s=q-|p(D)|\). A surjective completion exists if and only if \(s\le r\): every absent colour needs a distinct empty input, and assigning those colours to distinct empty inputs leaves all remaining inputs arbitrary. A set that assigns two different colours at one input is inconsistent. All inconsistent sets therefore close to \(E\).

For a feasible partial function with \(r\ge2\), no specific value at any unassigned input is forced. If \(s=r\ge2\), permute the missing colours among empty inputs. If \(s<r\), there are at least two admissible choices at each empty input: either use two available colours, or move the responsibility for a missing colour to another empty input. More explicitly, when \(s>0\) and at least one colour is already used, one can put a missing colour or an already-used colour at the chosen input and then cover the other missing colours with remaining inputs; when no colour is yet used, at least two missing colours can be placed at the chosen input. If \(s=0\), the chosen input may take any of the \(q\ge3\) values. If \(r=1\), a value is forced exactly when \(s=1\), and is then the single missing colour. This proves the closure characterization in (a).

**2. Minimal impossible premises.** A partial function is infeasible precisely when its shortage \(\delta=s-r\) is positive. If a used colour occurs only once, deleting its unique assertion increases \(s\) and \(r\) by one, leaving \(\delta\) unchanged; thus such an infeasible premise cannot be inclusion-minimal. If no used colour is a singleton and \(\delta\ge2\), deleting any assertion increases \(r\) without changing \(s\), leaving an infeasible proper subset. Conversely, if \(\delta=1\) and every used colour has multiplicity at least two, deletion of any assertion changes the shortage to zero. Hence every proper subset is feasible. The minimal infeasible graph-shaped premises are exactly family 3. Independently, assigning two colours at the same position gives a minimal inconsistent two-element premise, family 1.

**3. Exhaustion of direct premises.** Let \(P\) be inclusion-minimal with some \(e\in\operatorname{cl}(P)\setminus P\) not entailed by any strict subset of \(P\). If \(P\) is feasible, paragraph 1 implies that \(P\) belongs to family 2. If \(P\) is infeasible, it contains a minimal inconsistent subset of type 1 or type 3. Since that subset already entails every atom, minimality forces equality. There are no other premises. Conversely every family-2 premise minimally forces its last atom, and every family-1 or family-3 premise with at least one missing conclusion has a genuinely minimal root. For type 3 with no empty positions, every strict subset can only force values of the one omitted colour; since \(q\ge3\), some other value absent from \(P\) cannot be forced by any strict subset. For type 3 with an empty position, every strict subset has at least two empty positions and forces no atom. For type 1, strict subsets are singletons and force no atom because \(n>q\ge3\). Therefore the listed premises are precisely the stems of this closure operator.

**4. One-round directness and optimality.** Use each type-1 or type-3 premise to conclude \(E\), and each type-2 premise to conclude its single forced atom. Given \(S\), if it is consistent but infeasible, it contains a minimal type-3 premise and so closes to \(E\) in one round. If it contains two assignments at one position, a type-1 rule likewise fires. If feasible, its only nontrivial consequences, by paragraph 1, arise from a type-2 premise, and the one-round rules give exactly \(\operatorname{cl}(S)\). Every implication is valid, so no spurious conclusion occurs.

For a lower bound, choose for each stem \(P\) an atom \(e_P\in\operatorname{cl}(P)\setminus P\) that is **not** in the closure of any proper subset of \(P\), as shown in paragraph 3. In any simultaneously direct valid basis, producing \(e_P\) from input \(P\) requires a rule whose premise is exactly \(P\): a rule with a strictly smaller premise cannot validly produce \(e_P\), and a rule with an incomparable or larger premise does not fire. The listed stems are distinct. Thus every simultaneously direct basis has at least as many rules as the displayed family, regardless of how many atoms may occur on the right side. This proves optimality. It is also the general stem principle for direct bases, specialized here with an explicit classification.

**5. Exact enumeration.** There are \(n\binom q2\) type-1 premises. For type 2, choose an empty input (\(n\) choices), a missing colour (\(q\) choices), and a surjection of the remaining \(n-1\) labelled inputs onto the other \(q-1\) colours, giving \(nq(q-1)!\left\{\!\!\begin{smallmatrix}n-1\\q-1\end{smallmatrix}\!\!\right\}\). For type 3, let \(r\) be the number of empty inputs. The number \(t\) of used colours must equal \(q-r-1\), with \(1\le t\le q-1\). Choose the \(r\) empty inputs, choose the \(t\) used colours, and partition the remaining \(n-r\) positions into \(t\) labelled colour classes each of size at least two. This produces the summand \(\binom nr\binom qt t!T(n-r,t)\) and proves the general formula.

For \(q=3\), the type-3 sum has only \(r=0,1\). Its terms are \(3(2^n-2n-2)\) and \(3n\), respectively. Type 2 contributes \(3n(2^{n-1}-2)\), and type 1 contributes \(3n\); simplification gives the formula for \(b_{n,3}\). To count closed sets, start with the \(4^n\) partial assignments (each input blank or assigned one of three colours). The infeasible ones are: \(3n\) assignments with exactly one blank position and all other values identical; and \(3\cdot2^n-3\) complete functions missing at least one colour. Thus the number of feasible partial assignments is \(4^n-3n-3\cdot2^n+3\). Subtract the \(3n(2^{n-1}-2)\) feasible but nonclosed type-2 assignments and add the separate top \(E\). This yields the stated lattice cardinality.

## Verification

The standalone `verify.py` reconstructs all onto-function incidence rows as bitmasks and computes exact closure by intersecting the rows containing a given premise. It separately enumerates the three proposed rule families, compares their counts against ordinary and associated Stirling recurrences, and checks simultaneous one-round closure. It also checks necessity by deleting each displayed rule and testing the one-round output at its premise. Exhaustive tests cover \((n,q)=(3,3),(4,3),(5,3),(4,4)\), and deterministic larger samples cover \((6,3),(5,4),(5,5)\). The total is 149,720 distinct tested input sets across these parameter sets (some sample counts include required rule premises). Exhaustion of finite parameters is not the proof for unrestricted \(n,q\); paragraphs 1–5 supply the proof.

Run from the directory containing `verify.py` with `python verify.py`; it uses only the Python standard library. Expected final line begins `VERIFY_OK candidate_subsets 149720`.

## Relationship to prior work

The canonical direct-basis/stem principle, as well as the distinction between minimum-cardinality and direct bases, are established general theory; see Wild's survey, particularly Section 3.3 and Theorem 2. Adaricheva, Nourine and Vilmin investigate algorithms and hardness results for the \(D\)-base of arbitrary finite closure systems. Baixeries and Napoli compare computation using minimal and direct bases, without furnishing the above exact onto-assignment formulas. The present claim is the explicit classification of all stems and closed sets for **surjections with a nontrivial unused-input margin**, together with the associated-Stirling optimum and three-colour counts. It is not a claim to have introduced the general direct-basis theorem. The bijection case \(n=q\) has a different prior context and does not by itself imply the shortage-multiplicity classification for \(n>q\).

## Limitations

The lower bound is for **simultaneously direct** bases with positive antecedents and multi-atom conclusions, not for unrestricted iterative Horn minimization, unit-head clause count, or general propositional encodings with negative literals. The case \(q=2\) and the bijective boundary \(n=q\) are outside the theorem. No claim of a complete historical priority search is made; an equivalent formulation in constraint satisfaction, database theory, or Horn-envelope language remains a possibility. The verification is finite, while the arbitrary-parameter theorem is deductive.

## References

1. K. Adaricheva, L. Nourine, and S. Vilmin, *Computing the D-base and D-relation in finite closure systems*, first posted 2024-04-10, arXiv:2404.07037, https://arxiv.org/abs/2404.07037.
2. J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, first posted 2024-04-18, arXiv:2404.12229, https://arxiv.org/abs/2404.12229.
3. M. Wild, *The joy of implications, aka pure Horn formulas: mainly a survey*, arXiv:1411.6432, https://arxiv.org/html/1411.6432v4. In particular Section 3.3 and Theorem 2 are explicitly credited as prior general results.

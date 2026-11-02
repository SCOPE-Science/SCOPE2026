# Sharp finite-size prevalence of weak excluded middle in Heyting algebras

## Finding

Let \(H\) be a finite Heyting algebra, and write
\[
 w(H)=\frac{|\{a\in H:\neg a\vee\neg\neg a=\top\}|}{|H|}.
\]
If \(H\) has \(n\ge3\) join-irreducible elements and does **not** satisfy weak excluded middle identically, then
\[
 \boxed{w(H)\le\frac{2^{n-2}+1}{2^{n-2}+3}.}
\]
Equality holds if and only if \(H\) is isomorphic to the downset Heyting algebra of \(A_2\oplus A_{n-2}\), the ordinal sum of a two-point antichain and an \((n-2)\)-point antichain. In particular, the minimum possible proportion of failing elements at fixed join-irreducible count \(n\) is exactly \(2/(2^{n-2}+3)\).

There is also an exact counting formula. Write \(H\cong J(P)\), where \(P\) is the finite poset of its join-irreducibles, and let \(C_1,\ldots,C_k\) be the connected components of the *undirected comparability graph* of \(P\). If \(\operatorname{Min}(C_i)\) denotes the minimal points of \(C_i\), then
\[
 \boxed{|\{a\in H:\neg a\vee\neg\neg a=\top\}|=
 \prod_{i=1}^k\bigl(1+|J(C_i\setminus\operatorname{Min}(C_i))|\bigr).}
\]
Here \(J(Q)\) denotes all order ideals of the induced finite poset \(Q\), including the empty ideal. In particular \(w(H)=1\) if and only if each \(C_i\) has exactly one minimal point.

## Assumptions and scope

The language is that of Heyting algebras with the usual pseudocomplement \(\neg a=a\to\bot\); the probability uses the uniform distribution on the **elements** of \(H\), not on the join-irreducibles. The exact product formula holds for every finite Heyting algebra, with the empty product interpreted as one for the trivial algebra. The sharp bound applies only when \(n\ge3\) and \(w(H)<1\). An isomorphism of Heyting algebras is equivalent here to a bounded distributive lattice isomorphism.

A connected component is formed using undirected edges between distinct comparable elements; this convention fixes the direction of the finite Birkhoff representation. \(A_j\) denotes an antichain of \(j\) points, and the ordinal sum places every element of the first antichain below every element of the second.

## Proof

**1. Pointwise semantics.** By finite Birkhoff representation, take \(H=J(P)\). For an ideal \(I\subseteq P\) and a point \(p\in P\), the relative pseudocomplement satisfies
\[
 p\in\neg I\iff \downarrow p\cap I=\varnothing.
\]
Writing \(M(p)=\operatorname{Min}(P)\cap\downarrow p\) and \(S=I\cap\operatorname{Min}(P)\), every nonempty ideal of \(\downarrow p\) contains a minimal point of \(P\), so
\[
 p\in\neg I\iff M(p)\cap S=\varnothing,
 \qquad
 p\in\neg\neg I\iff M(p)\subseteq S.
\]
For the second equivalence, a missing minimum \(m\in M(p)\setminus S\) belongs to \(\neg I\) and witnesses \(p\notin\neg\neg I\); conversely every \(q\le p\) has a minimum \(m\le q\), and if all such minima lie in \(S\), then \(q\notin\neg I\).

Thus \(\neg I\cup\neg\neg I=P\) exactly when each nonempty \(M(p)\) is either wholly contained in \(S\) or disjoint from \(S\).

**2. Connected components.** In one comparability component \(C\), construct a graph on its minimal points, joining two when they have a common upper bound in \(C\). This graph is connected: every \(M(p)\) is a clique, and for comparable \(p\le q\) the nonempty set \(M(p)\) is contained in \(M(q)\), so comparability paths glue these cliques together. The pointwise condition from step 1 therefore means precisely that \(S\cap C\) is either empty or all of \(\operatorname{Min}(C)\).

An ideal with no minimum of \(C\) is empty on \(C\). Ideals containing every minimum of \(C\) correspond bijectively, by deleting those minima, to \(J(C\setminus\operatorname{Min}(C))\). Therefore the number of satisfying ideals of \(C\) is \(1+|J(C\setminus\operatorname{Min}(C))|\). Choices over distinct components are independent, proving the product formula. All ideals satisfy the equation if and only if every connected component has one minimum: when there are at least two minima, an ideal containing exactly one gives a counterexample.

**3. Sharp bound for a connected component.** Let \(C\) have \(s\) points and \(m\ge2\) minimal points. Connectedness implies \(s\ge m+1\). Put \(t=|J(C\setminus\operatorname{Min}(C))|\le 2^{s-m}\). There are exactly \(1+t\) satisfying ideals. Every nonempty proper subset of the \(m\) minima is itself an ideal and fails weak excluded middle, giving at least \(2^m-2\) failing ideals. Hence
\[
 1-w(J(C))\ge\frac{2^m-2}{1+t+2^m-2}
 \ge\frac{2}{2^{s-2}+3}.
\]
The last inequality follows because \(2^m-2\ge2\), \(t\le2^{s-m}\le2^{s-2}\), and \(B/(1+t+B)\) increases in \(B>0\) and decreases in \(t\ge0\).

For equality, necessarily \(m=2\), \(t=2^{s-2}\), and the only failing ideals must be the two singleton minima. The second condition says the remaining \(s-2\) points are an antichain. As \(C\) is connected, every remaining point lies above at least one minimum. If such a point lay above exactly one, its principal downset would be a third failing ideal. Thus every remaining point lies above **both** minima, and \(C\cong A_2\oplus A_{s-2}\). Conversely that poset has \(2^{s-2}+3\) ideals and exactly \(2^{s-2}+1\) satisfying ideals, so equality holds.

**4. Arbitrary finite posets.** If \(w(J(P))<1\), at least one component \(C\) has two or more minima. Writing \(s=|C|\le n\), multiplicativity gives
\[
 w(J(P))=\prod_i w(J(C_i))\le w(J(C))
 \le\frac{2^{s-2}+1}{2^{s-2}+3}
 \le\frac{2^{n-2}+1}{2^{n-2}+3}.
\]
The right-hand fraction is strictly increasing in \(s\), so equality requires \(s=n\) (there is only one component), and step 3 gives the unique equality type. This completes the proof.

## Verification

The standalone standard-library script `verify_wem.py` independently evaluates \(\neg I\) and \(\neg\neg I\) as bitsets over all ideals. It enumerates all naturally labeled posets through six points: exactly \(1,2,7,40,357,4824\) orders in sizes one to six. Every poset passes the exact component-product formula and the sharp inequality. At sizes three through six, it finds exactly one naturally labeled equality structure, the asserted two-level poset. It also directly counts the equality constructions through sixteen points. These finite tests corroborate but are not used to prove the universal statements.

Run the check with `python3 verify_wem.py`. It requires only Python 3 and its standard library.

## Relationship to prior work

Bumpus and Kocsis (2021 preprint, later journal publication) introduced satisfiability-degree questions for Heyting algebras and classified which one-variable equations have a uniform finite satisfiability gap. Their results imply in particular that the weak excluded-middle equation has **no universal gap**. They do not give the stated sharp bound at each prescribed number of join-irreducibles, its equality characterization, or the componentwise enumeration formula.

Lávička, Moraschini and Raftery (2021 preprint) develop the algebraic characterization of weak excluded-middle laws, including the logical connection with \(\mathbf{KC}\). That is a global validity characterization rather than a quantitative fixed-size prevalence statement. The result here gives a sharp, exponentially vanishing *conditional defect* bound for non-\(\mathbf{KC}\) finite algebras, consistent with the absence of a uniform gap.

## Limitations

The size parameter is the number of join-irreducibles, not the total number of elements of the Heyting algebra. The result gives the maximum satisfaction proportion among non-\(\mathbf{KC}\) algebras at that parameter, not the entire set of attainable proportions or an extremal lower bound. It is restricted to finite algebras. Terminological variants involving Stone or De Morgan algebras leave some historical-priority uncertainty.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, initially public 2021-10-21. See Sections 1–2 and Theorem 2.19 of the 2024 revised preprint. https://arxiv.org/abs/2110.11515
2. T. Lávička, T. Moraschini and J. G. Raftery, *The Algebraic Significance of Weak Excluded Middle Laws*, arXiv:2108.09168, initially public 2021-08-20; *Mathematical Logic Quarterly* 68 (2022), 79–94. https://arxiv.org/abs/2108.09168

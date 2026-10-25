# A single support-closure gate for acyclic collective-attack argumentation

## Finding

**Theorem (acyclic-attack closure criterion).** Let \(\mathcal F=(A,R,S)\) be a finite bipolar set-based argumentation framework (BSAF), with nonempty attack tails and arbitrary collective support tails, including empty tails and cyclic supports. Form the *attack-dependency digraph* with an arc \(u\to v\) for every \((T,v)\in R\) and every \(u\in T\). Suppose that digraph is acyclic. In any topological ordering, define \(K\subseteq A\) by accepting each \(v\) precisely when no attack \((T,v)\in R\) has \(T\subseteq K\) among the previously examined arguments.

Then exactly one of the following occurs:

1. If \(K\) is closed under \(S\), the complete, stable, and grounded extension families all equal \(\{K\}\).
2. If \(K\) is not closed under \(S\), all three extension families are empty.

The criterion, its unique extension when present, and a witness support rule when absent can all be computed in time \(O(|A|+\sum_{(T,v)\in R}(|T|+1)+\sum_{(U,h)\in S}(|U|+1))\) for explicitly listed finite rules. Neither the supports' dependency digraph nor the full positive-and-negative dependency digraph needs to be acyclic.

## Assumptions and scope

Let \(A\) be a finite set; \(R,S\subseteq\mathcal P(A)\times A\). Every attack tail \(T\) is required to be nonempty. Every support tail \(U\) may be empty, and support cycles are permitted. A set \(E\subseteq A\) *attacks* an argument \(v\) if some \((T,v)\in R\) has \(T\subseteq E\); it attacks a set \(Y\) if it attacks an argument of \(Y\). The set is *conflict-free* if it does not attack itself. It is *support-closed* if for every \((U,h)\in S\), \(U\subseteq E\) implies \(h\in E\). Write \(\operatorname{cl}_S(Y)\) for the least support-closed superset of \(Y\), obtained by repeated rule firing.

A set \(E\) *defends* \(v\) if it attacks every support-closed set \(Y\) that attacks \(v\). It is *admissible* if it is support-closed, conflict-free, and defends all its members. It is *complete* if in addition it contains every argument it defends. It is *stable* if it is admissible and attacks every argument outside itself. A *grounded* extension is an inclusion-minimal complete extension. These are the classical BSAF semantics, not the modified support-aware semantics introduced elsewhere. All three symbols \(\operatorname{com}(\mathcal F)\), \(\operatorname{stb}(\mathcal F)\), and \(\operatorname{grd}(\mathcal F)\) denote families of extensions, possibly empty.

The attack-dependency graph uses only the attack rules. Its acyclicity ensures all members of an attack tail occur strictly before its head in a topological ordering. Thus the recursive definition of \(K\) is unambiguous; the proof below also proves that \(K\) is independent of which topological order was selected.

## Proof

**Step 1: attack-only recursion.** In topological order, a head \(v\) enters \(K\) exactly when there is no \((T,v)\in R\) with \(T\subseteq K\). Since \(T\) contains only predecessors, this decision is definitive. Consequently \(K\) is conflict-free: if \(T\subseteq K\) and \(v\in K\) for some attack, the decision at \(v\) would have rejected it. Also, each \(v\notin K\) has a fired attack \((T,v)\) with \(T\subseteq K\). Thus \(K\) attacks every outsider, without using support properties.

**Step 2: every complete extension equals \(K\).** Let \(E\) be any complete extension. We induct along the same topological order that \(v\in E\) exactly when \(v\in K\); the strengthened induction also asserts that \(E\) attacks each rejected predecessor. Assume this for all predecessors of \(v\). If an attack \((T,v)\) fires from \(K\), all elements of \(T\) are predecessors in \(E\); conflict-freeness of \(E\) excludes \(v\). This attack from \(E\) establishes the strengthened assertion for rejected \(v\).

Otherwise no attack on \(v\) fires from \(K\). Consider any support-closed attacker \(Y\) of \(v\). There is an attack \((T,v)\) with \(T\subseteq Y\). Since \(T\not\subseteq K\), choose \(u\in T\setminus K\). This \(u\) is a predecessor, and by the strengthened induction \(E\) attacks \(u\); hence \(E\) attacks \(Y\). As this works for every closed attacker, \(E\) defends \(v\). Completeness gives \(v\in E\). This completes the induction, including sources (for which the attacking families are empty). Therefore \(E=K\), regardless of support rules. Since \(E\) is closed, a complete extension is impossible unless \(K\) is support-closed.

**Step 3: every stable extension equals \(K\).** Let \(E\) be stable and induct along the topological order. If an attack at \(v\) fires from accepted predecessors, conflict-freeness forces \(v\notin E\); otherwise stability would be violated if \(v\notin E\), because no attack on \(v\) could fire from \(E\). Thus the membership recursion for \(E\) agrees exactly with that for \(K\). Hence \(E=K\), and support-closure of \(K\) is necessary for any stable extension.

**Step 4: support-closed \(K\) is admissible, complete and stable.** Assume \(K\) is support-closed. For any \(v\in K\) and any closed attacking set \(Y\) of \(v\), choose an attack \((T,v)\) with \(T\subseteq Y\). Conflict-freeness of \(K\) ensures \(T\not\subseteq K\); choose \(u\in T\setminus K\). By Step 1, \(K\) attacks \(u\) and thus \(Y\). Therefore \(K\) defends each of its members and is admissible. Step 1 also says that it attacks every outsider, so it is stable.

For completeness, let \(v\notin K\). Step 1 supplies an attack \((T,v)\) with \(T\subseteq K\). Its support closure \(Y=\operatorname{cl}_S(T)\) is a closed attacker of \(v\); since \(K\) is closed, \(Y\subseteq K\). Conflict-freeness of \(K\) implies that \(K\) does not attack any member of \(Y\); hence \(K\) fails to defend \(v\). So the defended arguments are exactly \(K\), making it complete. The uniqueness established in Steps 2 and 3 shows that \(K\) is the only complete and stable extension, and therefore the unique grounded extension.

**Step 5: algorithm and boundary examples.** Construct the attack-dependency digraph and topologically sort it. Process the attack tails indexed by head to decide membership in \(K\); test every support implication \(U\to h\) once. Summing the incidence-list lengths gives the stated linear bound. If the test fails, the violated support rule certifies nonexistence of complete, grounded and stable extensions under the theorem's hypothesis.

The criterion can fail already for \(A=\{a,b\}\), attack \(a\to b\), and support \(a\to b\): here \(K=\{a\}\) is not support-closed. Moreover preferred extensions do not collapse with complete extensions, even when \(K\) is closed. For \(A=\{a,b,c\}\), attacks \(a\to b\), \(b\to c\), and support \(a\to c\), the only complete, stable, and grounded extension is \(\{a,c\}\), but the preferred extensions are \(\{b\}\) and \(\{a,c\}\). These two examples distinguish the theorem from an assertion about all semantics.

## Verification

The accompanying `checker.py` evaluates the BSAF definitions directly by enumerating support-closed sets, closed attackers, admissibility, completeness, and stability, and separately implements the proposed recursion and closure criterion. It exhausts all attack-rule subsets respecting the labelled topological order for up to three arguments, with all singleton-support relations including cycles; it also samples collective attack and support rules, including empty support tails, for two through six arguments and checks both boundary examples. It reports `ALL_CHECKS_OK 34455` in Python 3. These are finite diagnostic comparisons, not a substitute for the all-size induction and closure proof above.

## Relationship to prior work

The BSAF semantics and the closed-attacker defense criterion are established by Berthold, Rapberger, and Ulbricht (2024), particularly their Definitions 3.1–3.3 and Lemma 3.12. Their examples show that complete extensions may fail to exist, but do not identify the present attack-acyclic support-closure criterion. Berthold, Blümel, Buraglio, and Rapberger (2026) give general splitting theorems, including limitations for grounded and preferred extensions, but do not classify acyclic attack dependency or derive the linear-time existence test here. Berthold, Blümel, and colleagues' 2025 analysis of strong and weak admissibility concerns different semantics. Classical uniqueness for acyclic Dung/collective-attack frameworks is the support-free boundary; it does not by itself classify possible nonexistence when arbitrary supports remain. The distinguishing content is that **one attack-only topological candidate governs all three BSAF semantics despite unrestricted positive dependencies**, with a single exact support-closure gate for existence.

## Limitations

The attack-dependency digraph must be acyclic; cycles of attack rules fall outside the theorem, even when support rules are simple. Empty attack tails are excluded. The complexity bound assumes explicitly represented finite hyperrules, not exponentially succinct rule specifications. The result does not classify admissible or preferred extensions; these need not be unique. The relationship to older formulations of non-flat assumption-based argumentation, especially under different acyclicity notions, remains a possible priority risk. No independent validation is claimed.

## References

1. M. Berthold, A. Rapberger, and M. Ulbricht, *Capturing Non-flat Assumption-based Argumentation with Bipolar SETAFs*, KR 2024, pp. 127–132, doi:10.24963/kr.2024/12. https://proceedings.kr.org/2024/12/kr2024-0012-berthold-et-al.pdf
2. M. Berthold, L. Blümel, G. Buraglio, and A. Rapberger, *Splitting Argumentation Frameworks with Collective Attacks and Supports*, arXiv:2604.28112v1 (first public 2026-04-30); KR 2026, pp. 167–178, doi:10.24963/kr.2026/16. https://arxiv.org/abs/2604.28112
3. M. Berthold et al., *On Strong and Weak Admissibility in Non-Flat Assumption-Based Argumentation*, KR 2025, doi:10.24963/kr.2025/14. https://proceedings.kr.org/2025/14/kr2025-0014-berthold-et-al.pdf
4. G. Buraglio, W. Dvořák, and S. Woltran, *Splitting Assumption-Based Argumentation Frameworks*, arXiv:2604.27964v1 (2026-04-30). https://arxiv.org/abs/2604.27964

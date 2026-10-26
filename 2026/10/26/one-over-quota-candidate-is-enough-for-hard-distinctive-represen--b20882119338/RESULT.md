# One over-quota candidate is enough for hard distinctive-representation elections

## Finding

The restriction that each elected candidate have exactly the voter quota may turn a simple representation guarantee into an NP-complete feasibility problem. The following establishes a sharp structural boundary for the *distinctive representation* (DR) criterion of Chingoma, Grossi, Lindeboom and Maly (2026).

**Theorem.** For every approval election with \(n\) voters, \(m\ge k\ge1\) candidates and quota \(q=\lceil n/k\rceil\):

1. If every candidate has at most \(q\) supporters and at least \(k\) candidates have exactly \(q\) supporters, a DR committee exists and can be constructed in polynomial time.
2. The DR-existence decision problem is NP-complete even when \(q=4\), all but one candidates have exactly four supporters, all those four-supported candidates share a common supporter, and the sole exceptional candidate is approved by *every voter except that common supporter*.

Thus one candidate whose support exceeds the quota is sufficient for NP-completeness, while zero such candidates permit a universal constructive guarantee whenever the necessary \(k\) quota-sized candidates exist. The construction fixes the support quota at
\[
q=\left\lceil\frac{12t+1}{4t}\right\rceil=4.
\]

## Assumptions and scope

Let \(N\) be a finite nonempty voter set, \(C\) a finite candidate set, and \(A_i\subseteq C\) the candidates approved by voter \(i\). Write \(N_c=\{i\in N:c\in A_i\}\), \(n=|N|\), \(m=|C|\), and fix integer \(1\le k\le m\). The relevant quota is the integer \(q=\lceil n/k\rceil\). A voter is *represented* by \(W\subseteq C\) if their approval ballot intersects \(W\).

A committee \(W\) of exactly \(k\) distinct candidates satisfies *justified representation* (JR) if no candidate has at least \(q\) supporters who are all unrepresented by \(W\). This is equivalent to the usual condition on cohesive voter groups because \(q\) is the least integer at least \(n/k\). A committee satisfies *distinctive representation* (DR) when it has JR and \(|N_c|=q\) for **every** \(c\in W\). The notions refer to raw supporter counts, not to the number of voters a particular elected candidate uniquely represents.

The positive assertion assumes that there are enough quota-sized candidates to fill the committee. For the hardness assertion, the source X3C problem has a set \(U\) with \(|U|=3t\), a family \(\mathcal F\) of three-element subsets of \(U\), and asks whether some \(t\) members partition \(U\). We may restrict to \(t\ge2\) and \(|\mathcal F|\ge t\); cases violating either condition are polynomial-time decidable and can be sent to a fixed no-instance satisfying the restriction, so this does not weaken NP-hardness.

## Proof

**Part I: existence when no candidate exceeds the quota.** Form the hypergraph whose edges are the \(q\)-supporter sets \(N_c\) for the candidates \(c\) with \(|N_c|=q\). Repeated edges arising from distinct candidates are permitted. Start with no selected candidate. Repeatedly select any quota-sized candidate whose entire supporter set is disjoint from every previously selected support set; stop when no such candidate remains. Let \(B\) denote this inclusion-maximal disjoint-support family. Since each member contributes \(q\) different voters, \(|B|q\le n\), whence \(|B|\le\lfloor n/q\rfloor\le k\). Since at least \(k\) quota-sized candidates exist, pad \(B\) to exactly \(k\) *distinct* quota-sized candidates to obtain \(W\).

Every quota-sized candidate outside \(B\) intersects a selected supporter set, by maximality; the voters in this intersection are represented. The same is obvious for candidates in \(B\). A candidate with fewer than \(q\) supporters cannot witness a JR violation. Because every candidate has at most \(q\) supporters, no candidate can have \(q\) unrepresented supporters. Hence \(W\) satisfies JR and all elected candidates have \(q\) supporters: it is DR. Support-set intersection and padding take polynomial time.

**Part II: membership in NP.** Given a size-\(k\) committee \(W\), compute the set \(R\) of represented voters, verify \(|N_c|=q\) for each \(c\in W\), then verify \(|N_c\setminus R|<q\) for each candidate \(c\in C\). This is polynomial in the explicit approval matrix. The tests are exactly the DR requirements.

**Part III: hardness with a single over-quota candidate.** Take an X3C instance \((U,\mathcal F)\) with \(|U|=3t\), \(t\ge2\) and \(|\mathcal F|\ge t\). Create four disjoint copies \(U_1,U_2,U_3,U_4\) of \(U\), one further voter \(d\), and a committee budget \(k=4t\). There are \(n=12t+1\) voters, giving \(q=\lceil(12t+1)/(4t)\rceil=4\). For each \(T\in\mathcal F\) and each \(j\in\{1,2,3,4\}\), create a different candidate \(c_{j,T}\) whose supporters are \(T_j\cup\{d\}\), where \(T_j\) is the corresponding triple in copy \(j\). Finally create one exceptional candidate \(e\) whose supporters are all \(12t\) element voters and do not include \(d\). All the other candidates have exactly four supporters, all approveable by \(d\), while \(|N_e|=12t>4\). The election has \(4|\mathcal F|+1\ge k+1\) candidates and is constructed in polynomial time.

Every DR committee must omit \(e\), since it has too many supporters. Every eligible committee of size \(k\) contains some \(c_{j,T}\), and hence represents \(d\). Thus each ordinary four-supported candidate has a represented supporter and cannot violate JR. The *only* potentially JR-blocking candidate is \(e\), which blocks precisely when at least four element voters are still unrepresented. Consequently, an eligible size-\(k\) committee is DR **if and only if** its selected triples leave at most three of the \(12t\) element voters uncovered.

If the X3C instance admits \(t\) disjoint triples covering \(U\), choose those \(t\) candidates in each of the four copies. This produces \(4t\) elected quota-supported candidates and covers every element voter, so it is DR.

Conversely, suppose X3C is a no-instance and select *any* \(4t\) ordinary candidates. Let \(s_j\) be the number chosen from copy \(j\), so \(\sum_{j=1}^4s_j=4t\). If \(s_j=t\), the selected triples cannot cover all \(3t\) voters in copy \(j\), since a collection of \(t\) triples covering \(3t\) distinct elements would necessarily be an exact cover. At least one voter remains uncovered there. If \(s_j<t\), at least \(3(t-s_j)\) voters are uncovered there by the elementary cardinality bound \(|\bigcup T|\le3s_j\).

Let \(B=\sum_{j:s_j<t}(t-s_j)\) denote the total number of missing triple slots in underallocated copies. If \(B=0\), every \(s_j\ge t\), and the sum constraint forces all four to equal \(t\); at least four voters remain uncovered. If \(B\ge2\), the underallocated copies alone leave at least \(3B\ge6\) voters uncovered. If \(B=1\), exactly one copy has \(t-1\) chosen candidates and hence at least three uncovered voters; by the sum constraint exactly one copy has \(t+1\) chosen candidates and the other two have exactly \(t\) chosen candidates, each leaving at least one uncovered voter. At least five remain uncovered. Every possible allocation therefore leaves at least four element voters uncovered, making \(e\) a JR-blocking candidate. No DR committee exists.

We have a polynomial reduction with exact YES/NO equivalence and the advertised support restrictions. Together with NP membership this proves NP-completeness. Combining Parts I and III yields the one-overquota-candidate boundary.

## Verification

The accompanying standalone `verify.py` implements the definition of JR *directly* from voter approvals and support sets; it never assumes the proposed correspondence when performing the finite checks. It enumerates all eligible size-\(k\) committees in a small X3C demonstration with \(t=2\) (four independent copies of a six-element universe), checking one YES family and one NO family: the latter has 12,870 candidate subsets. An additional small hypergraph sweep checks the greedy construction against the direct JR predicate for many quota-support families. These finite tests supplement, and do not replace, the symbolic X3C reduction and maximal-matching proof.

To reproduce with standard Python 3, run `python verify.py` in the directory containing this document and the program. All membership, quota, and uncovered-voter tests are integer and exact; no external packages are required.

## Relationship to prior work

Chingoma, Grossi, Lindeboom and Maly (2026) introduce DR in their Definition 22 and prove unrestricted DR decision hardness in their Theorem 26 (including the appendix proof), while also giving a polynomial local-search procedure for a weaker local condition. Their unrestricted hardness assertion does not imply hardness after restricting *every but one* candidate to have exactly the quota-sized support, nor does it give this positive no-overquota boundary. The present result is a restriction-specific complexity dichotomy, not a new definition of DR, a general NP-hardness theorem, or a claim about the authors' published construction.

Aziz and collaborators (2015) establish universal JR existence and a greedy construction without the added restriction on elected candidates' support size; this does not settle when *all elected supports equal the quota*. Elkind and collaborators (2021) study small justifying groups and optimization, but the cited material does not state the single-overquota-candidate complexity threshold. The reduction uses classical X3C and a four-copy gap mechanism; familiar tools are acknowledged rather than claimed as inventions. A search of related mathematical-result records and primary publications did not reveal an implication-equivalent published boundary, but this is not a proof of priority.

## Limitations

The positive algorithm needs at least \(k\) candidates with support exactly \(q\); without them DR is impossible for the obvious cardinality reason. The hardness instances have a very specific one-exception structure with quota four, one universally shared voter among the ordinary candidates, and one almost universally supported exceptional candidate. The theorem does not prove hardness for smaller quotas, bounded ballot lengths, interval-support domains, or fixed committee size. It proves decision complexity, not optimal approximability. Finite program checks are illustrative, not exhaustive for all election sizes. Independent historical-priority verification and independent scientific audit have not been performed.

## References

- Julian Chingoma, Davide Grossi, Feline Lindeboom, Jan Maly, *Diverse Representation in Approval-Based Committee Voting*, arXiv:2609.29332, first publicly posted 2026-09-24. Definition 22, Theorem 26, and Appendix D. https://arxiv.org/abs/2609.29332
- Haris Aziz et al., *Justified Representation in Approval-Based Committee Voting*, arXiv:1407.8269, first publicly posted 2014-07-31. Theorem 1. https://arxiv.org/abs/1407.8269
- Edith Elkind et al., *Justifying Groups in Multiwinner Approval Voting*, arXiv:2108.12949, first publicly posted 2021-08-30. Sections 1 and 3–4. https://arxiv.org/abs/2108.12949
- Michael R. Garey and David S. Johnson, *Computers and Intractability*, W. H. Freeman, 1979, problem SP2 (Exact Cover by 3-Sets).

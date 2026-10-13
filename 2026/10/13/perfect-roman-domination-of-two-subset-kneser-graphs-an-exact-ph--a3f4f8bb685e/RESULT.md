# Perfect Roman domination of two-subset Kneser graphs: an exact phase transition

## Finding
Let \(KG(n,2)\) have as vertices the two-element subsets of \([n]\), with two vertices adjacent precisely when they are disjoint. For every integer \(n\ge7\), the perfect Roman domination number is
\[
\gamma_{pR}(KG(n,2))=\begin{cases}11,&n=7,\\14,&n=8,\\2n-2,&n\ge9.\end{cases}
\]
Moreover the numbers of minimum-weight perfect Roman dominating functions are, respectively, \(105\), \(238\), and \(\binom n2\). Every optimal function labels \(2\) exactly on the edges of a matching of size two for \(n=7\), either on a single edge or on a two-edge matching for \(n=8\), and on a single edge for \(n\ge9\). Given these \(2\)-labels, all other labels are uniquely determined.

## Assumptions and scope
A perfect Roman dominating function on a finite graph is a map \(f:V\to\{0,1,2\}\) such that every vertex with label \(0\) has **exactly one** neighbor with label \(2\). Its weight is \(\sum_v f(v)\), and \(\gamma_{pR}\) is the minimum weight. The domain here consists of simple two-subset Kneser graphs and integers \(n\ge7\); small orders are not claimed.

Write \(N=\binom n2\). A support \(F\subseteq\binom{[n]}2\) is the family of underlying two-subsets given label \(2\), and write \(r=|F|\). For an underlying pair \(e\notin F\), let \(d_F(e)\) be the number of members of \(F\) disjoint from \(e\), and set \(U(F)=|\{e\notin F:d_F(e)=1\}|\).

## Proof
**Step 1: exact support reduction.** For prescribed \(F\), the defining condition permits a label \(0\) on \(e\notin F\) exactly when \(d_F(e)=1\); otherwise that pair must carry label \(1\). Labeling every permitted pair by \(0\) is the unique minimum-weight extension of \(F\), of weight
\[
W(F)=N+r-U(F).
\]
Other extensions of the same support have strictly larger weight. An empty support has weight \(N\). For a one-pair support, the pairs disjoint from that pair are exactly \(\binom{n-2}{2}\), so
\[
W(F)=N+1-\binom{n-2}{2}=2n-2.
\]

**Step 2: universal unique-neighbor bound for \(r\ge2\).** We prove \(U(F)\le4(n-4)\) for all \(n\ge7\).

Suppose first that \(F\) contains disjoint pairs \(a,b\). Let \(X=a\cup b\), with four vertices, and \(Y=[n]\setminus X\). If a pair is disjoint from exactly one of \(a,b\), it has one vertex in \(X\) and one in \(Y\), except that the pairs \(a,b\) themselves each meet one and are disjoint from the other, but are excluded because they belong to \(F\). Thus there are exactly \(4(n-4)\) available pairs that are disjoint from exactly one of \(a,b\). A pair with \(d_F(e)=1\) either belongs to this collection or is one of the four cross pairs joining \(a\) to \(b\). If \(F=\{a,b\}\), then exactly the former \(4(n-4)\) pairs are uniquely dominated, establishing equality.

If some third pair \(c\in F\setminus\{a,b\}\) is present, at least four of those \(4(n-4)\) former candidates are disjoint from \(c\), so they cannot be uniquely dominated. Indeed, if \(c\) contains respectively two, one, or zero points of \(X\), at least \(2(n-4)\), \(3(n-5)\), or \(4(n-6)\) former candidates are disjoint from \(c\). Each bound is at least four when \(n\ge7\). At most four exceptional cross pairs can be newly eligible. Consequently \(U(F)\le4(n-4)\) in every case.

Suppose instead no two pairs in \(F\) are disjoint. Such a family of two-subsets is contained in a star, or is the three edges of a triangle. Directly, when \(r=2\), the two intersecting pairs have \(U(F)=2(n-3)\); when \(r=3\) forms a triangle, \(U(F)=3(n-3)\); when \(r=3\) forms a star, \(U(F)=3\); and when \(r\ge4\), the family is a star and \(U(F)=0\). Each value is at most \(4(n-4)\) for \(n\ge7\).

**Step 3: optimization and rigidity.** By Step 2, every support of size \(r\ge2\) satisfies
\[
W(F)\ge N+r-4(n-4).
\]
Since \(r\ge2\), this is at least \(N+2-4(n-4)\), with equality possible only when \(r=2\) and \(F\) is a pair of disjoint underlying edges. (For two intersecting members, the bound on \(U\) is strict.) In contrast, the best one-pair support has weight \(2n-2\), and their difference is
\[
N+2-4(n-4)-(2n-2)=\frac{(n-5)(n-8)}2.
\]
For \(n=7\), the two-edge matching wins by one, giving \(11\). For \(n=8\) the two choices tie at \(14\); for every \(n\ge9\), the one-edge support wins strictly, yielding \(2n-2\). The empty support has weight \(N\), strictly larger than all three optima. The strictness statements also establish the asserted **complete** classification of minimizers: a chosen support cannot be extended with any extra \(1\) in place of a permitted \(0\) without increasing weight.

**Step 4: enumeration.** There are \(\binom n2\) single-pair supports and \(3\binom n4\) unordered two-edge matchings on \([n]\) (choose the four endpoints and one of three pairings). Each support gives exactly one minimum extension. Thus \(n=7\) has \(3\binom74=105\) optima; \(n=8\) has \(\binom82+3\binom84=238\); and \(n\ge9\) has \(\binom n2\).

## Verification
The standalone Python program `verifier.py` enumerates all \(2\)-supports with \(2r\) at most the claimed optimum for \(n=7,8,9\), which is exhaustive for all potentially optimal functions: a support with \(2r\) larger than the optimum cannot achieve it. The tests cover \(27{,}896\), \(1{,}683{,}218\), and \(40{,}999{,}516\) supports respectively and recover the claimed optima, exact multiplicities, and support sizes. A separate direct neighborhood-count implementation cross-checks the support-weight identity on supports of sizes one through three at orders seven through eleven. Run `python3 verifier.py`; `verification_output.txt` records the expected deterministic output. The proof above, rather than the finite experiments, establishes the theorem for all \(n\ge7\).

## Relationship to prior work
Henning and Klostermeyer introduced general regular-graph perfect Roman domination bounds, including a theorem for regular graphs of degree at least four; these inequalities do not identify the exact minimum or minimizers of \(KG(n,2)\). Zec and Grbić proved Roman and total Roman domination results for Kneser graphs, but not the perfect Roman variant (exactly one \(2\)-neighbor). Fernau and Mann studied perfect Roman domination and unique-response variants from algorithmic and complexity viewpoints, without the present exact Kneser classification. Here the exact unique-neighbor constraint is decisive: it produces a two-edge versus one-edge support phase transition and multiplicity formula. The complete inspected primary texts are listed below.

## Limitations
This theorem does not cover \(n<7\), Kneser graphs \(KG(n,k)\) for \(k>2\), or other Roman domination variants. Exhaustive checks at finite orders are reproducibility checks only. A differently worded historical result on perfect Roman domination of two-subset Kneser graphs cannot be categorically excluded, so priority should be evaluated independently before public dissemination. The review is not independent validation.

## References
1. M. A. Henning and W. F. Klostermeyer, *Perfect Roman Domination in Regular Graphs*, Applicable Analysis and Discrete Mathematics **12** (2018), 143–152. DOI 10.2298/AADM1801143H; full text: https://doiserbia.nb.rs/img/doi/1452-8630/2018/1452-86301801143H.pdf.
2. T. Zec and M. Grbić, *Several Roman domination graph invariants on Kneser graphs*, Discrete Mathematics & Theoretical Computer Science **25** (2023), DOI 10.46298/dmtcs.10506; arXiv:2204.05664; full text: https://dmtcs.episciences.org/11340/pdf.
3. H. Fernau and K. Mann, *Perfect Roman Domination and Unique Response Roman Domination*, arXiv:2309.07018 (2023); full text: https://arxiv.org/pdf/2309.07018.

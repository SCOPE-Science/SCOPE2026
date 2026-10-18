# Exact independent-Roman weight enumerators for clique coronas and minimum sunlet configurations

## Finding
For every finite simple graph \(H\) of order \(n\ge1\), and every integer \(m\ge1\), the complete independent-Roman weight enumerator of the corona \(H\circ K_m\) has the following sharp dichotomy:
\[
F_{H,m}(z)=
\begin{cases}
\displaystyle z^{2n}\sum_{S\subseteq V(H)\,\text{independent}}m^{n-|S|}, & m\ge2,\\[5pt]
\displaystyle\sum_{S\subseteq V(H)\,\text{independent}} z^{2n-|N_H(S)|}(1+z)^{|N_H(S)|}, &m=1.
\end{cases}
\]
The first expression is \(m^nI_H(1/m)z^{2n}\), where \(I_H\) is the usual independence polynomial. In particular, when \(m\ge2\), every independent-Roman dominating function has weight \(2n\), and there are exactly \(m^nI_H(1/m)\) of them. When \(m=1\), the minimum weight is \(n+i(H)\), where \(i(H)\) is the independent domination number. The scalar domination values are not the priority claim; the complete weight distributions and exact multiplicities are.

For the labeled sunlet \(C_n\circ K_1\), \(n\ge3\), put
\[
T(z)=\begin{pmatrix}
z^2&z+z^2&0\\
0&0&z^2\\
z+z^2&z+z^2&0
\end{pmatrix}.
\]
Its full independent-Roman polynomial is
\[F_{C_n,1}(z)=\operatorname{tr}(T(z)^n).\]
In particular, the exact number \(a_n\) of minimum-weight independent-Roman functions is
\[
a_n=\begin{cases}
3,&n\equiv0\pmod3,\\
n(n+5)/6,&n\equiv1\pmod3,\\
n,&n\equiv2\pmod3.
\end{cases}
\]
The minimum weight is \(\lceil4n/3\rceil\), and all vertices and labels are distinguished.

## Assumptions and scope
The base \(H=(V,E)\) is a finite, labeled, loopless simple graph, not necessarily connected, with \(n=|V|\ge1\). The corona \(H\circ K_m\) contains a copy of \(H\), together with one fresh private \(m\)-clique \(Q_v\) for every \(v\in V\); all vertices of \(Q_v\) are adjacent to \(v\), and there are no other new edges. A function \(f:V(H\circ K_m)\to\{0,1,2\}\) is independent Roman dominating if (i) every zero-labeled vertex has a two-labeled neighbor and (ii) the positive-labeled vertices are independent. Its weight is \(w(f)=\sum_x f(x)\). Define \(F_{H,m}(z)=\sum_fz^{w(f)}\) over all such functions. The open neighborhood of a vertex set \(S\) in \(H\) is \(N_H(S)=\bigcup_{v\in S}N_H(v)\). Let \(I_H(t)=\sum_{S\,\text{independent}}t^{|S|}\). The least size of an independent dominating set of \(H\) is \(i(H)\). The minimum independent Roman weight of a graph \(G\) is denoted \(i_R(G)\).

## Proof
**Local dichotomy for private clique order at least two.** Fix \(v\in V(H)\). In any independent Roman dominating function, at most one vertex of the complete subgraph on \(\{v\}\cup Q_v\) can be positive. At least one must be positive: otherwise the private clique's zero vertices have no two-labeled neighbor. That unique positive vertex must have label two, for if it had label one then at least one other vertex of this complete subgraph (there is one because \(m\ge2\)) would be zero and have no two-labeled neighbor: its neighbors lie inside that complete subgraph, except that \(v\) also has base neighbors, but when the positive vertex is a private vertex a zero private vertex has no outside neighbors; and when the positive vertex is \(v\) each zero private vertex has no outside neighbors. Thus every \(\{v\}\cup Q_v\) has exactly one label two and all other labels zero. If a core vertex \(v\) carries two, its neighbors in \(H\) cannot carry two. Conversely, an independent set \(S\) of core vertices carrying two, together with a choice of one private vertex carrying two in each \(Q_v\) for \(v\notin S\), is an independent Roman dominating function. It has total weight \(2n\) and exactly \(m^{n-|S|}\) realizations. Summing over \(S\) gives the first formula, without missing or double-counting a function.

**One-leaf case.** Let \(m=1\). A core vertex cannot carry label one: its sole leaf would then have label zero by independence, but no neighbor with label two. Thus the set \(S\) of core vertices labeled two is independent; their own leaves are necessarily zero. At any core vertex \(v\notin S\), the core label is zero, so its leaf is positive, and it may be one or two. If \(v\notin N_H(S)\), the core vertex has no two-labeled core neighbor and therefore its leaf must carry label two. If \(v\in N_H(S)\), its core is already defended by an adjacent core two, and its leaf may carry either label one or label two. This construction is reversible. There are \(|N_H(S)|\) independent leaf choices with weights one or two; every other block contributes weight two. Their generating polynomial is \(z^{2n-|N_H(S)|}(1+z)^{|N_H(S)|}\). Summation over independent \(S\) establishes the second formula.

**Minimum weight.** For fixed independent \(S\), the least exponent is \(2n-|N_H(S)|\), attained uniquely by giving one to every leaf of \(N_H(S)\). Extend \(S\) to a maximal independent set \(D\). Then \(D\) dominates \(H\), so \(|N_H(D)|=n-|D|\le n-i(H)\) and \(N_H(S)\subseteq N_H(D)\). A minimum independent dominating set realizes equality, showing the minimum possible weight \(n+i(H)\). This scalar identity follows from the structure and is not asserted as a new invariant formula.

**Transfer polynomial for the sunlet.** Encode each cycle's core-two vertices by a binary cyclic word \(b_0\ldots b_{n-1}\) with no adjacent ones. For each \(b_i=1\), its leaf has label zero and the block weight is two. For \(b_i=0\), the leaf has label one or two if either adjacent bit is one, or is forced to label two if both adjacent bits are zero. The allowed ordered consecutive-bit states are \((0,0),(0,1),(1,0)\). A transition \((a,b)\to(b,c)\) is permitted only when \(bc\ne11\). It contributes weight \(z^2\) when \(b=1\) or \(a=c=0\), and \(z+z^2\) otherwise. In the displayed state order this is precisely \(T(z)\). Closed walks of length \(n\) in the state graph correspond bijectively to the indexed cyclic binary words and multiply the correct block contributions. Therefore \(F_{C_n,1}(z)=\operatorname{tr}(T(z)^n)\), for every \(n\ge3\). Cayley–Hamilton gives the optional recurrence
\[
F_{C_n,1}(z)=z^2F_{C_{n-1},1}(z)+(z^3+z^4)F_{C_{n-2},1}(z)+(z^4+z^5)F_{C_{n-3},1}(z),\quad n\ge6,
\]
with initial polynomials \(F_{C_3,1}(z)=3z^4+6z^5+4z^6\), \(F_{C_4,1}(z)=6z^6+12z^7+7z^8\), and \(F_{C_5,1}(z)=5z^7+20z^8+25z^9+11z^{10}\). The characteristic polynomial is \(\lambda^3-z^2\lambda^2-(z^3+z^4)\lambda-(z^4+z^5)\).

**Exact minimum multiplicities.** On \(C_n\), an independent nonempty set \(S\) of \(q\) chosen core positions has \(q\) cyclic gaps of zero positions of positive lengths \(g_1,\ldots,g_q\), with sum \(n-q\). The distinct vertices in \(N_{C_n}(S)\) are precisely the first and last zero vertices in each gap, so \(|N_{C_n}(S)|=\sum_{j=1}^q\min(2,g_j)\le\min(2q,n-q)\). The maximum is \(\lfloor2n/3\rfloor\); the constructions below attain it. Each maximizing \(S\) gives exactly one minimum-weight labeling (each optional leaf must be one). Write \(n=3r,3r+1,3r+2\). For \(3r\), only \(q=r\) works, with all gaps two; there are three core subsets. For \(3r+1\), either \(q=r\) with one gap three and all others two (\(n\) subsets), or \(q=r+1\) with exactly two gaps one and all other gaps two (\(\frac{n}{r+1}\binom{r+1}{2}=nr/2\) subsets). Their sum is \(n(r+2)/2=n(n+5)/6\). For \(3r+2\), only \(q=r+1\) works, with one gap one and all others two, giving \(n\) subsets. The gap counts divide rooted cyclic descriptions by \(q\), since each actual independent set has exactly \(q\) possible distinguished starting selected vertices. The empty \(S\) never attains the maximum for \(n\ge3\). The optimum weight is \(2n-\lfloor2n/3\rfloor=\lceil4n/3\rceil\). This completes the classification and counts.

## Verification
The accompanying `verify.py` constructs coronas directly, enumerates all labelings in \(\{0,1,2\}\) on thirteen small instances, and tests the two defining conditions without using the structural classification. Across those instances it examines 1,713,969 raw label assignments; each resulting complete weight distribution matches the formula. A separate polynomial-matrix implementation checks the sunlet identity against the subset formula through cycle order 12 and checks all optimum counts and weight exponents through order 25. Execute `python3 verify.py` in an environment with standard Python 3; no extra packages are required. These finite checks detect implementation and boundary errors but do not prove the infinite formulas: the preceding bijections and cyclic-run argument do.

## Relationship to prior work
Siva Parvathi and Maheswari (2017), *Independent Roman Domination of Corona Graph*, specifically analyze \(C_n\circ K_m\), provide examples of minimal independent Roman functions and give a scalar \(2n\) independent-Roman domination statement. The present result identifies the distinct \(m=1\) boundary with a full polynomial, and counts every feasible labeling rather than particular minimal functions. Cabrera-Martínez and Rueda-Vázquez (online 2023) give closed formulas for independent Roman domination **numbers** on general rooted products; our scalar minimum is not claimed as new relative to that broader theory. Their publisher preview and abstract do not provide a complete enumerator; their full text was not accessible in this examination, leaving a specific priority risk. Paul, Sharma and Pandey (first public arXiv 2024-07-04) study optimization algorithms for independent Roman domination on distance-hereditary, split and \(P_4\)-sparse graphs; their inspected preprint does not give the corona weight-polynomial or labeled optimum-multiplicity classification. Prior counts for pointwise-minimal ordinary Roman functions on sunlets concern a different admissibility criterion and do not imply counts for independent Roman functions.

## Limitations
The exact base-graph summations may require exponentially many independent-set terms; no polynomial-time general counting algorithm is asserted. The closed three-state transfer matrix and residue-class minimum counts apply to cycle bases with a single private leaf. The private-clique dichotomy is specific to complete attached graphs and the standard independence condition on positive labels. Labels and vertices are distinguished; quotienting by automorphisms yields different counts. The bibliographic review is not exhaustive; the inaccessible full text of the 2023 rooted-product paper and other unindexed sources are residual novelty risks. No independent scientific audit has been performed.

## References
1. M. Siva Parvathi and B. Maheswari, *Independent Roman Domination of Corona Graph*, International Journal of Advanced Research in Computer Science 8(6), 136–142 (2017). https://www.ijarcs.info/index.php/Ijarcs/article/viewFile/4489/3963
2. A. Cabrera-Martínez and J. M. Rueda-Vázquez, *Closed Formulas for the Independent (Roman) Domination Number of Rooted Product Graphs*, Mediterranean Journal of Mathematics 21, 24 (online 27 December 2023). https://doi.org/10.1007/s00009-023-02565-1
3. K. Paul, A. Sharma and A. Pandey, *Exploring Algorithmic Solutions for the Independent Roman Domination Problem in Graphs*, arXiv:2407.03831 (first public 4 July 2024). https://arxiv.org/abs/2407.03831

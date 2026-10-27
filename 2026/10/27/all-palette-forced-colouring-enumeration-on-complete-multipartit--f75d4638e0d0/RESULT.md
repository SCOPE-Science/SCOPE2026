# All-palette forced-colouring enumeration on complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\ge2\), positive integer part sizes, and \(N=\sum_i n_i\). Let \(\lambda\ge r+1\) be the number of *named* available colours. A partial assignment **forces** a proper total colouring if repeated local steps suffice to colour all vertices, where an uncoloured vertex is assigned the unique remaining colour when its already-coloured neighbours exhibit precisely \(\lambda-1\) distinct colours. Let \(F_{G,\lambda}(z)=\sum_{k=0}^N f_kz^k\) count successful partial assignments with exactly \(k\) initially coloured vertices.

**Structural classification.** Every proper complete colouring already assigned to all vertices succeeds. Every successful *incomplete* assignment has a unique resulting proper colouring \(c\), and the following conditions are necessary and sufficient:

1. All \(\lambda\) colours occur in \(c\), and initially assigned colours agree with \(c\).
2. Every part on which \(c\) uses at least two distinct colours is **fully** initially coloured.
3. Among the monochromatic parts of \(c\), all but at most one contain at least one initially coloured vertex. (Other vertices of seeded monochromatic parts may remain uncoloured.)

Whenever these conditions hold, synchronous forcing finishes in at most two rounds. In particular, all successful incomplete assignments are classified, not merely counted.

For a vector \(\mathbf t=(t_1,\ldots,t_r)\) of integers, put \(\mathcal M(\mathbf t)=\{i:t_i=1\}\), \(b(\mathbf t)=\sum_{i:t_i>1}n_i\), and \(A_i(z)=(1+z)^{n_i}-1\). Let \(S(n,t)\) be a Stirling number of the second kind, with \(S(n,t)=0\) outside \(1\le t\le n\). The chromatic polynomial evaluation needed below is explicitly
\[
P_G(\lambda)=\sum_{\substack{1\le t_i\le n_i\\ \sum_i t_i\le\lambda}} (\lambda)_{\sum_i t_i}\prod_{i=1}^r S(n_i,t_i),
\]
where \((\lambda)_u=\lambda!/(\lambda-u)!\). Define
\[
\begin{aligned}
\mathcal E_{\mathbf t}(z)={}&\prod_{i\in\mathcal M(\mathbf t)} A_i(z)
-z^{\sum_{i\in\mathcal M(\mathbf t)}n_i}\\
&+\sum_{j\in\mathcal M(\mathbf t)}\prod_{i\in\mathcal M(\mathbf t)\setminus\{j\}}A_i(z).
\end{aligned}
\]
Empty products equal \(1\), so \(\mathcal E_{\mathbf t}(z)=0\) if \(\mathcal M(\mathbf t)=\varnothing\). Then the **exact all-palette forcing-domain polynomial** is
\[
\boxed{F_{G,\lambda}(z)=P_G(\lambda)z^N+\lambda!\!\sum_{\substack{1\le t_i\le n_i\\\sum_i t_i=\lambda}}\!\left(\prod_{i=1}^rS(n_i,t_i)\right)z^{b(\mathbf t)}\mathcal E_{\mathbf t}(z).}
\]
This is a finite coefficient formula with no enumerations over individual vertex assignments. Farr's forced-colouring probability polynomial consequently satisfies, for \(0\le p\le 1/\lambda\),
\[
\boxed{\operatorname{FC}_{\lambda}(G;p)=\sum_{k=0}^N[z^k]F_{G,\lambda}(z)\,p^k(1-\lambda p)^{N-k}.}
\]

There is also an exact minimum-seed formula. Set \(e=\lambda-r\), \(c_i=n_i-1\), and define
\[
\mathcal S_j=\left\{S\subseteq\{i\ne j:n_i\ge2\}:1\le |S|\le e\le\sum_{i\in S}c_i\right\}.
\]
The minimum possible size of a successful forcing domain is
\[
\boxed{s_{G,\lambda}=\min\!\left\{N,\ r-1+\min_{1\le j\le r}\ \min_{S\in\mathcal S_j}\sum_{i\in S}c_i\right\},}
\]
where a minimum over an empty family is \(+\infty\). Incomplete successful forcing occurs if and only if \(\lambda\le N-\min_i n_i+1\). For example,
\[
F_{K_{2,2,2},4}(z)=288z^3+432z^4+288z^5+96z^6,
\]
so three seeds suffice and all coefficient counts are explicit.

## Assumptions and scope
All graphs here are finite and simple. All parts are labelled vertex sets, and the \(\lambda\) colours are distinguished; assignments are counted without identifying colour permutations or graph automorphisms. The principal new regime is \(\lambda>r=\chi(G)\). If \(\lambda> N-\min_i n_i+1\), no vertex has enough neighbours to be forced, and the formula correctly reduces to \(P_G(\lambda)z^N\). The formula for \(\lambda=r\) is already known and is used only as a consistency boundary, not claimed as novel. No assertion is made about arbitrary nonmultipartite graphs.

## Proof
**Step 1: proper extensions and palette saturation.** Every successful assignment is the restriction of a proper complete colouring \(c\): forced steps never change a seeded colour. In a complete multipartite graph, the sets \(C_i\) of colours used by \(c\) in distinct parts are disjoint, because all vertices in distinct parts are adjacent. If an incomplete assignment succeeds, there is a first forcing step. At that step the neighbours of the forced vertex already display \(\lambda-1\) different colours. The forced vertex supplies the remaining colour, so the resulting colouring and hence \(c\) use all \(\lambda\) colours. This proves condition 1.

**Step 2: rigidity of multicoloured parts.** Suppose part \(i\) has at least two colours in \(c\) and contains an initially uncoloured vertex. Consider the first vertex of that part ever forced. Its neighbours lie in other parts and display \(\lambda-1\) different colours. Properness ensures that every colour of \(C_i\) is absent from those neighbours, but the complement of their \(\lambda-1\) colours has size one. Thus \(|C_i|\le1\), a contradiction. Therefore such a part must be initially completely coloured, proving condition 2.

**Step 3: the empty-part obstruction.** If at least two monochromatic parts have no seeded vertex, then by Step 2 every colour absent from the initial palette corresponds to such an empty part. These two different colours are absent initially, so the entire initial assignment displays at most \(\lambda-2\) colours. No first forcing step can exist. This proves the necessity of condition 3.

**Step 4: sufficiency and round bound.** Suppose conditions 1–3 hold. Every colour used in a multicoloured part is seeded by condition 2. If no monochromatic part is wholly unseeded, every colour in \(c\) is represented initially. For any uncoloured vertex in a monochromatic part \(i\), all \(\lambda-1\) colours different from its own are therefore present among its neighbours; it is forced in the first parallel round. If exactly one monochromatic part \(j\) is unseeded, all \(\lambda-1\) colours outside that part are represented. Thus all vertices in \(j\) are forced in the first round, after which the preceding argument forces any remaining vertices in a second round. Necessity and sufficiency, uniqueness of the completed colouring, and the two-round assertion follow.

**Step 5: enumeration.** A proper full colouring with \(t_i\) colours in part \(i\) contributes \((\lambda)_{\sum t_i}\prod_i S(n_i,t_i)\): choose disjoint named colour sets of respective sizes \(t_i\), and surject onto each. This gives \(P_G(\lambda)\) and counts all fully seeded assignments once, in \(P_G(\lambda)z^N\). By Steps 1–4 only proper full colourings using all \(\lambda\) colours have incomplete successful restrictions. For \(\sum_i t_i=\lambda\), the number of full colourings with this colour-usage vector is \(\lambda!\prod_iS(n_i,t_i)\). The multicoloured parts are fully seeded, contributing \(z^{b(\mathbf t)}\). Every seeded monochromatic part contributes its nonempty-subset polynomial \(A_i(z)\). Either all monochromatic parts are seeded, or exactly one is unseeded. The corresponding contribution is the first and third term in \(\mathcal E_{\mathbf t}(z)\); subtracting the all-fully-seeded monomial prevents double-counting the full colouring already included in \(P_G(\lambda)z^N\). Since a successful restriction uniquely determines its completed colouring, there is no further overcount. Summing proves the boxed enumerator. Independent random partial assignments assign probability \(p\) to each specific colour and \(1-\lambda p\) to being uncoloured, yielding the probability formula.

**Step 6: minimum seeds and palette cutoff.** An incomplete successful restriction with every monochromatic part seeded can be improved by unseeding an entire monochromatic part: all colours outside it were already seeded by Steps 2–4, so the smaller restriction still succeeds. Consequently some minimum incomplete domain has exactly one completely unseeded monochromatic part \(j\). Let \(S\) be the other parts using at least two colours. Each such part must have all \(n_i\) vertices seeded; each remaining part except \(j\) needs only one seeded vertex. This costs \(r-1+\sum_{i\in S}(n_i-1)\). Starting from the \(r\) nonempty colour palettes, the \(\lambda-r=e\) extra colours must be distributed across the parts of \(S\), each of capacity \(c_i=n_i-1\) and using at least one extra. The distribution is possible exactly when \(1\le|S|\le e\le\sum_{i\in S}c_i\). Thus the displayed finite minimization is exact, with the always-valid fully seeded option of size \(N\). Finally, some incomplete assignment exists precisely when a target part \(j\) has at least \(\lambda-1\) other vertices, so its neighbours can initially display \(\lambda-1\) colours. Such a part exists exactly when \(\lambda\le N-\min_i n_i+1\); choosing distinct colours on \(\lambda-1\) outside vertices and assigning the remaining outside vertices colours appropriately gives a proper \(\lambda\)-colouring with a monochromatic unseeded target. This establishes the cutoff.

## Verification
The standalone `verify.py` uses two different enumeration routes for small graphs. One directly enumerates all \((\lambda+1)^N\) partial assignments and executes the local forcing rule until no further step is possible. The other constructs the stated Stirling-number formula by integer polynomial arithmetic. The 17 independent comparisons cover bipartite and tripartite examples, palettes from two through five colours, and graph orders up to six. Every comparison of each seeded-domain count passed, as did the independent minimum-seed tests. Four further exhaustive comparisons reconstruct the set of all successful partial assignments from the structural criterion and compare it assignment-by-assignment with direct forcing, including the nonchromatic-palette cases. The printed terminal line is `ALL_EXHAUSTIVE_CASES_PASS`. Notably, \(K_{2,2,2}\) with four colours has coefficients \((288,432,288,96)\) at degrees three through six; direct enumeration examines all \(5^6=15625\) assignments.

These finite tests support the implementation and boundary cases but do not establish the infinite theorem. Steps 1–6 provide the general proof. The checker uses Python's standard library only and can be run as `python3 verify.py`.

## Relationship to prior work
Farr and Morgan introduced the random partial-colouring model and its local forcing definition. Farr's 2026 paper develops the forced-colouring function, including a general complexity result, but a complete comparison with that 29-page preprint remains limited by full-text access. Published exact results already treat the \(\lambda=r\) chromatic-palette case for complete multipartite graphs, the \(\lambda=3\) complete-bipartite case, and maximum-degree-two graphs at three colours. The present theorem treats the previously excluded \(\lambda>r\) regime **for every complete multipartite part profile**, including all domain-size coefficients, a forcing-round classification, and a minimum-seed formula. It specializes consistently to the earlier formulas when evaluated at their parameters, but those specializations are not claimed as new.

For example, in the prior chromatic-palette classification no part can be multicoloured; at larger palettes, multicoloured parts must be fully initially seeded. That distinct rigidity condition is the reason the old product formula does not imply the new all-palette coefficient formula. The existing complete-bipartite three-colour formula covers only \((r,\lambda)=(2,3)\); it does not cover \(\lambda\ge4\) or \(r\ge3\). Results on zero forcing and unique-extension colouring concern different forcing rules and do not imply the statement.

## Limitations
The result gives an explicit finite sum rather than a uniformly bounded-degree expression for every variable number of parts. It does not evaluate arbitrary graphs or prove any complexity-class collapse. Historical originality cannot be established by searching alone: the complete 2026 initiating preprint was unavailable during source inspection, so exact priority remains a material risk pending access and independent review. The mathematical proof and enumerator assume the iterative local rule stated above, not global unique extendability.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first public 2026-09-15, https://arxiv.org/abs/2609.17108.
2. G. E. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746 (2024), public full text at https://www.researchgate.net/publication/381666584_Graph_polynomials_some_questions_on_the_edge.
3. *Forced colourings of complete multipartite graphs at the chromatic palette size*, published published-finding corpus record 2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655.
4. *Forced three-colouring polynomial of complete bipartite graphs*, published published-finding corpus record 2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69.
5. *Exact forced 3-colouring polynomials at maximum degree two*, published published-finding corpus record 2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd, https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd.

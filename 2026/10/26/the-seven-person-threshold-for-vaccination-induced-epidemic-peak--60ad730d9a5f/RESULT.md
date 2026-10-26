# The seven-person threshold for vaccination-induced epidemic peak amplification

## Finding

In a static one-generation-infective network SIR model, vaccinating one person cannot increase the peak number of simultaneously infectious people when the population has at most six people. This holds for **every** directed contact network and **every** coupled realization of successful contacts, and thus for arbitrary time-homogeneous transmission probabilities. The population cutoff is sharp: a seven-person directed network has peak \\(2\\) without vaccination and peak \\(3\\) after vaccinating one person, while its total number ever infected falls from seven to six.

For this minimal witness, if each of its seven potential directed contacts succeeds independently with probability \\(p\\in(0,1]\\), the expected vaccinated-minus-unvaccinated peak is exactly

\\[
\\Delta(p)=p^2(p^5-2p^4+3p^3-1).
\\]

The polynomial \\(f(p)=p^5-2p^4+3p^3-1\\) has a unique zero \\(p_*\\) in \\((0,1)\\), with \\(p_*\\approx0.787833660305238\\). Therefore the **expected** peak increases precisely when \\(p>p_*\\), decreases when \\(0<p<p_*\\), and ties at \\(p=p_*\\). This is an exact property of the specified finite model, not an empirical statement about vaccination campaigns.

## Assumptions and scope

A finite loop-free directed graph \\(G=(V,E)\\) describes potential infectious contacts. A single designated vertex \\(s\\) is initially infected at generation zero. Each infected individual is infectious for exactly one generation, attempts transmission once across each outward contact, and thereafter is permanently removed. Contacts' time-homogeneous successes may be preassigned before the epidemic; for the stochastic seven-person calculation they are independent Bernoulli variables with common probability \\(p\\). A perfectly vaccinated vertex \\(v\\ne s\\) is never infected and cannot transmit, so its deletion (with its incident arcs) represents vaccination under the same contact realization.

Write \\(d_G(u)\\) for the length of a shortest directed path from \\(s\\) to \\(u\\), with value infinity if no such path exists. Define the infectious generation set

\\[
L_j(G)=\\{u\\in V:d_G(u)=j\\},\\qquad j=0,1,2,\\ldots,
\\]

and the **peak simultaneous infectious count**

\\[
M(G)=\\max_{j\\ge0}|L_j(G)|.
\\]

Generation zero (the seed) counts towards the maximum. In the coupled stochastic model, \\(G\\) denotes the random subgraph of successful directed contacts. The result concerns a vertex vaccinated **before** the initial infection and a *fixed*, nonadaptive contact network. It is not a statement about arbitrary infectious periods, calendar-time-varying contacts, or vaccination administered during an outbreak.

## Proof

**1. Infectious generations are directed shortest-path layers.** Generation zero contains exactly \\(s\\). If a person at distance \\(j\\) is infected at generation \\(j\\), they can transmit during the next step; no person can be infected earlier than the length of a directed path from \\(s\\). Induction on path length gives precisely the nonempty distance layers \\(L_j(G)\\). Vaccination replaces \\(G\\) by \\(G-v\\), with all successful edges elsewhere unchanged.

**2. No peak increase with at most six people.** First suppose \\(M(G)=1\\). Each nonempty original distance layer then contains one vertex. If \\(v\\) is unreachable from \\(s\\), deleting it leaves all other infection times unchanged. Otherwise suppose \\(d_G(v)=h\\ge1\\). Any directed path from \\(s\\) to a vertex of original distance greater than \\(h\\) must meet an original-distance-\\(h\\) vertex: along each edge, finite source-distance can increase by at most one, so the first time a path reaches distance at least \\(h\\) it has distance exactly \\(h\\). That vertex is uniquely \\(v\\). Consequently deleting \\(v\\) makes every originally later vertex unreachable. Vertices at original distances less than \\(h\\) retain their original shortest paths; \\(v\\) was the sole vertex of its layer. Thus \\(M(G-v)\\le1=M(G)\\).

Now suppose \\(M(G)\\ge2\\) and, for contradiction, \\(M(G-v)>M(G)\\). Some vaccinated distance layer \\(L'_t=L_t(G-v)\\) has at least three vertices. It cannot be generation zero, which always contains only the seed. It cannot be generation one, since every direct contact from the seed to a nonvaccinated person remains and \\(L'_1\\subseteq L_1(G)\\). Nor can it be generation two: if \\(d_{G-v}(u)=2\\), then \\(d_G(u)\\le2\\); if \\(d_G(u)=1\\), its direct arc from the seed would survive deletion, giving \\(d_{G-v}(u)=1\\), a contradiction. Thus \\(L'_2\\subseteq L_2(G)\\). Hence \\(t\\ge3\\). A vaccinated graph with at least three vertices in a layer of distance at least three must contain the seed, at least one intermediate vertex in each of the first two layers, and at least three vertices in that later layer: at least six *surviving* vertices. Including \\(v\\) forces \\(n\\ge7\\), contradicting \\(n\\le6\\). This proves the deterministic inequality for all directed graphs. Applying it to every successful-edge realization yields the expectation inequality without independence assumptions.

**3. A seven-person sharpness witness.** Take vertices \\(0,1,2,3,4,5,6\\), seed \\(s=0\\), vaccinated vertex \\(v=2\\), and exactly seven directed potential contacts

\\[
0\\to1,\\quad0\\to2,\\quad1\\to3,\\quad2\\to4,\\quad3\\to4,\\quad3\\to5,\\quad3\\to6.
\\]

If every contact succeeds, the unvaccinated infectious layers are \\(\\{0\\},\\{1,2\\},\\{3,4\\},\\{5,6\\}\\), so the peak is \\(2\\). After deleting vertex \\(2\\), the layers are \\(\\{0\\},\\{1\\},\\{3\\},\\{4,5,6\\}\\), so the peak is \\(3\\). The number ever infected decreases by one, since vertex \\(2\\) is never infected in the vaccinated outbreak.

**4. Exact common-transmissibility law.** For each subset of successful contacts among the seven, let \\(k\\) be the number of successful edges and let \\(\\delta=M(G-v)-M(G)\\). Exhausting all \\(2^7=128\\) subsets gives this full count table:

| Successful edges \\(k\\) | Count with \\(\\delta=-1\\) | Count with \\(\\delta=0\\) | Count with \\(\\delta=1\\) |
|:--:|--:|--:|--:|
| 0 | 0 | 1 | 0 |
| 1 | 0 | 7 | 0 |
| 2 | 1 | 20 | 0 |
| 3 | 5 | 30 | 0 |
| 4 | 10 | 25 | 0 |
| 5 | 7 | 14 | 0 |
| 6 | 1 | 6 | 0 |
| 7 | 0 | 0 | 1 |

Each row totals \\(\\binom{7}{k}\\). Its signed binomial weighting gives

\\[
\\begin{aligned}
\\mathbb E[M(G-v)-M(G)]={}&p^7-p^2(1-p)^5-5p^3(1-p)^4\\\\
&-10p^4(1-p)^3-7p^5(1-p)^2-p^6(1-p)\\\\
={}&p^2(p^5-2p^4+3p^3-1).
\\end{aligned}
\\]

The exhaustive table is independently reproducible from the self-contained \`verify.py\` program; it is an **exhaustive finite computation** only for this explicit seven-edge witness, not a replacement for the universal argument in step 2.

Finally \\(f(0)=-1\\), \\(f(1)=1\\), and

\\[
f'(p)=p^2(5p^2-8p+9)>0\\qquad(p>0),
\\]

because the quadratic has negative discriminant and positive leading coefficient. Hence there is exactly one crossing in \\((0,1)\\), whose numerical value and signs follow. This completes the proof.

## Verification

Run \`python3 verify.py\` using Python's standard library. The checker reconstructs every infectious-distance layer for all 128 successful-contact subsets, validates the complete integer count table, obtains the exact polynomial coefficients \\((0,0,-1,0,0,3,-2,1)\\), and numerically brackets the unique root. It also checks 20,000 seeded random directed networks of orders two through six. These random tests are supplementary; the bound for all graphs of order at most six is proved in step 2, not inferred from the sample.

## Relationship to prior work

Floyd, Kay and Shapiro studied vaccination monotonicity in network SIR models, proving under time-homogeneous transmission that one person's vaccination cannot increase another person's infection probability. That statement concerns **ever infected**, not the maximum simultaneous infectious count. Its published abstract was accessible; its complete text was not inspected, so further undiscovered coverage remains possible.

Kenah and Miller's 2011 open-access study derives epidemic-percolation-network constructions, identifies infection times with weighted shortest paths (Section 3) and represents perfect vaccination by deleting a vertex's incident edges (Section 4). Those general principles motivate the present distance-layer reduction. Their treatment focuses on epidemic probability, final size and large-network vaccine targeting; the specific seven-person peak-width boundary and exact common-probability polynomial were not identified in the inspected text. Sherborne, Blyuss and Kiss (2015) analyze peak prevalence when infectious-period staging changes, a distinct modification from deleting one vertex while preserving one-generation infectiousness.

The derived peak-width result is **not** an assertion of historical priority over all graph theory or epidemic literature. Particularly, a broader theorem about maximum breadth-first-search layer width under vertex deletion could imply the result without using vaccination terminology.

## Limitations

The model presumes one fixed initially infected seed, exactly one infectious generation, a static directed contact graph, one perfect vaccination administered before infection, and the stated convention that the initial seed counts toward peak prevalence. The seven-person polynomial further assumes identical independent contact probabilities on its seven present arcs. It does not cover variable infectious periods, dynamic vaccination, imperfect efficacy, adaptive contacts, noisy observations, or real-world clinical decisions. The Floyd–Kay–Shapiro full text and some possible graph-theoretic equivalents were not fully accessible; independent validation of novelty and proof has not been performed.

## References

1. W. Floyd, L. Kay, M. Shapiro, *Some Elementary Properties of SIR Networks or, Can I Get Sick because You Got Vaccinated?* Bulletin of Mathematical Biology **70** (2008), 713–727; first online 30 November 2007. DOI: 10.1007/s11538-007-9275-0.
2. E. Kenah, J. C. Miller, *Epidemic Percolation Networks, Epidemic Outcomes, and Interventions*. Interdisciplinary Perspectives on Infectious Diseases (2011), 543520. DOI: 10.1155/2011/543520. Open full text: https://onlinelibrary.wiley.com/doi/full/10.1155/2011/543520.
3. N. Sherborne, K. B. Blyuss, I. Z. Kiss, *Dynamics of Multi-stage Infections on Networks*. Bulletin of Mathematical Biology **77** (2015), 1909–1933. DOI: 10.1007/s11538-015-0109-1. Open full text: https://link.springer.com/article/10.1007/s11538-015-0109-1.

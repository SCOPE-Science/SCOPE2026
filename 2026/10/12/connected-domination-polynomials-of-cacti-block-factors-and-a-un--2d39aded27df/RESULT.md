# Connected-domination polynomials of cacti: block factors and a unique root exception

## Finding

For every finite connected simple cactus graph \(G\), the complete connected-domination polynomial factors over the cycle blocks. Apart from the triangle \(K_3\), this polynomial has only real, nonpositive zeros. Thus its entire coefficient sequence is log-concave and unimodal. This statement includes arbitrary trees, arbitrary cycle lengths, several cycles meeting at articulations, and trees attached to any cycle vertices.

More precisely, suppose \(|V(G)|\ge3\). Write \(A\) for the cut vertices and \(a=|A|\); let \(\ell\) count the degree-one vertices. For each cycle block \(C\), put
\[
F_C=V(C)\setminus A,\qquad q_C=|F_C|,\qquad t_C=|\{uv\in E(C):u,v\in F_C\}|.
\]
Then, with each zero-coefficient term omitted,
\[
\boxed{D_c(G;x)=x^a(1+x)^\ell\prod_{C\text{ a cycle block}}
       \left(x^{q_C}+q_Cx^{q_C-1}+t_Cx^{q_C-2}\right).}
\]
In particular, define the factor without negative exponents by
\[
Q_C(x)=\begin{cases}1,&q_C=0,\\1+x,&q_C=1,\\x^{q_C-2}(x^2+q_Cx+t_C),&q_C\ge2.\end{cases}
\]
For the two smaller connected cacti, \(D_c(K_1;x)=x\) and \(D_c(K_2;x)=2x+x^2\). All zeros of the displayed factorization are real and nonpositive unless \(G\cong K_3\), in which case
\[D_c(K_3;x)=x(x^2+3x+3)\]
and the two nonzero roots are nonreal. The factorization also determines the connected-domination number, every coefficient, and their multiplicities from the block-cut structure. For example, two 4-cycles meeting at one vertex have \(D_c(G;x)=x^3(x+1)^2(x+2)^2\), a case not reducible to the polynomial of one cycle.

## Assumptions and scope

A *connected cactus* is a finite simple connected undirected graph in which each edge belongs to at most one simple cycle. Equivalently, each maximal 2-connected block is an edge or a chordless cycle. The connected domination polynomial is
\[
D_c(G;x)=\sum_{\substack{S\subseteq V(G),\ S\ne\varnothing\\G[S]\ \mathrm{connected},\ N_G[S]=V(G)}}x^{|S|}.
\]
A singleton induces a connected graph. An empty product is \(1\); cycle blocks with no free vertices contribute \(1\). The theorem concerns *connected* dominating sets, not ordinary dominating sets, total dominating sets, or doubly connected dominating sets. The connectivity requirement is essential. All statements about roots count multiplicities and include the zero roots.

## Proof

**Lemma 1 (forced cut vertices).** If \(G\) is connected with at least two vertices, every connected dominating set \(S\) contains every cut vertex \(v\). Indeed, if \(v\notin S\), the connected set \(S\) lies inside one component of \(G-v\). Any vertex in another component has no neighbor in \(S\), contradicting domination. Conversely, no assertion is made that the cut vertices alone dominate arbitrary connected graphs.

**Lemma 2 (independent vertex roles).** For a connected cactus \(G\) of order at least three, every non-cut vertex is either a degree-one leaf or belongs to exactly one cycle block. Moreover, vertices in distinct categories here are distinct. To see this, use the block-cut tree. A vertex occurring in more than one block is a cut vertex. A non-cut vertex in a single edge block is a leaf, except in \(K_2\), which is excluded. A non-cut vertex in a cycle block has degree two, with no edges outside that block.

**Lemma 3 (cycle omission criterion).** Let \(C\) be any cycle block, and require all of its cut vertices to be in a connected dominating set \(S\). Then the omitted vertices \(V(C)\setminus S\), all lying in \(F_C\), are either empty, a singleton, or the two endpoints of one edge of \(C[F_C]\).

First, if three consecutive cycle vertices are omitted and its middle vertex is free, that vertex has no selected neighbor and is undominated. Because only free vertices can be omitted, a contiguous omission run therefore contains at most two vertices. Second, there cannot be two disjoint nonempty omission runs: the selected vertices of the cycle would then be split into separate nonempty segments. They cannot be reconnected outside \(C\): the block-cut incidence graph of a cactus is a tree, so a path outside \(C\) between two distinct cut vertices of \(C\) would create a cycle in that incidence graph; a segment without cut vertices has no external neighbor. When \(G=C\) itself, disconnected selected segments likewise violate connectedness. Thus a single contiguous omission run of length at most two is necessary.

Conversely, for each cycle block, omitting zero, one, or two consecutive free vertices leaves a nonempty connected segment of selected cycle vertices (a connected path, or the whole cycle) containing every cut vertex of that block, and every omitted cycle vertex has a selected cycle neighbor. This applies also to a sole triangle: one vertex may remain selected. If any cut vertices occur in \(G\), the selected segments connect through all cut vertices along the block-cut tree. Every selected leaf is attached to its selected cut-vertex neighbor, and every omitted leaf is dominated by that neighbor. Consequently all such choices, made independently across cycle blocks and leaves, yield connected dominating sets. If no cut vertices occur and \(|V(G)|\ge3\), the connected cactus is one cycle, already addressed by the same rule.

**Factor count.** Lemma 1 forces the \(a\) cut vertices, contributing \(x^a\). Each leaf is independently present or absent, contributing \(1+x\). In cycle \(C\), there is one zero-omission choice (weight \(x^{q_C}\)), exactly \(q_C\) one-omission choices (weight \(x^{q_C-1}\)), and exactly \(t_C\) adjacent two-omission choices (weight \(x^{q_C-2}\)). Lemmas 2 and 3 prove a nonovercounting bijection, hence the stated product. The separate \(K_1\) and \(K_2\) formulas follow by inspecting their connected dominating subsets.

**Real-rootedness.** If \(q_C=0\) or \(q_C=1\), its factor has no nonreal zero. For \(q_C\ge2\), the only potentially nonreal roots come from
\[x^2+q_Cx+t_C,\qquad \Delta_C=q_C^2-4t_C.\]
If \(q_C=2\), then \(t_C\le1\), so \(\Delta_C\ge0\). If \(q_C=3\) and \(C\) has at least one cut vertex, then the free vertices form a proper subset of the cycle and induce at most two edges, so \(t_C\le2\) and \(\Delta_C\ge1\). If \(q_C\ge4\), then \(t_C\le q_C\), giving \(\Delta_C\ge q_C(q_C-4)\ge0\). The remaining possibility \(q_C=3,t_C=3\) means all vertices of \(C\) are free and \(C\) is a triangle. Such a cycle has no cut vertex and hence constitutes the entire connected cactus \(G=K_3\). In this one case \(\Delta_C=-3\). Everywhere else \(\Delta_C\ge0\), and since each nonconstant quadratic has nonnegative coefficients and positive middle coefficient, its real roots are nonpositive. Products with \(x^a\) and \((1+x)^\ell\) preserve this. Finally a polynomial with nonnegative coefficients and only real nonpositive zeros has a log-concave coefficient sequence (Newton inequalities) and therefore is unimodal.

## Verification

The standalone file `verify_cactus.py` implements two independent computations: direct enumeration of all vertex subsets, with separate induced-connectivity and closed-neighborhood checks, and calculation of the block-factor coefficients from articulation vertices, cycle blocks, and leaves. Running `python verify_cactus.py` with NetworkX 3.x produced `VERIFY_OK`: 103 nonisomorphic cactus graphs from the NetworkX atlas, 720 randomized cacti with 8–15 vertices, and 6,280,063 tested nonempty subsets in total. An additional 7,105 random cycle blocks were checked for the quadratic discriminant, and the exceptional triangle and square were tested explicitly. The captured output is in `verification_output.txt`.

These computations check only the finite indicated inputs and are not used as a substitute for Lemmas 1–3 or the infinite discriminant argument. They do not establish originality.

## Relationship to prior work

Mojdeh and Emadi [1] establish general coefficients near the top degree, and full connected-domination polynomials for paths, cycles and corona graphs; in particular the one-cycle factor with no articulations is already covered. Ibrahim and Salih [2] count connected dominating sets for particular coalescences of complete and wheel graphs, motivating the need for a structural treatment of graph gluing. Yoosuf and Kuttipulackal [3] give a full friendship-graph enumerator, an exact special case of the present product. Vijayan and Felix Nes Mabel [4] study further small constructed families including tadpole graphs. None of these special-family identities is claimed as new. The claimed contribution is the simultaneous arbitrary-cactus block factorization and its sharp root-location dichotomy.

Shao and Zhao [5] investigate the root closure of connected-domination polynomials using other constructions and cycles. Their full text could not be material-inspected here; overlap from an equivalent formulation elsewhere therefore remains a stated limitation. Work on *doubly* connected domination [6] imposes the additional requirement that the complement be connected and so addresses a different polynomial.

## Limitations

The theorem assumes finite simple connected cacti. It is false as stated for arbitrary graphs containing shared-cycle edges or for disconnected graphs under the usual connected-domination convention. The triangle is a genuine nonreal-root exception. The factorization and qualitative root results do not assert novelty for the individual cycle, friendship, path, star, corona, or tadpole cases. Prior-work searches do not prove uniqueness, and one recent relevant paper was accessible only through its abstract. No independent validation of this result has been performed.

## References

[1] D. A. Mojdeh and A. S. Emadi, “Connected Domination Polynomial of Graphs,” *Fasciculi Mathematici* 60 (2018), 103–121, DOI 10.1515/fascmath-2018-0007; full text: https://fasciculi-mathematici.put.poznan.pl/artykuly/60/FM60%282018%29-MojdehDA-EmadiAS.pdf.

[2] N. B. Ibrahim and H. F. M. Salih, “Vertex Connected Domination Polynomial of some Coalescence of Complete and Wheel Graphs,” *International Journal of Mathematical Sciences and Computing* 6(6) (2020), 1–8; first verified public date 2020-12-08, DOI 10.5815/ijmsc.2020.06.01; https://www.mecs-press.org/ijmsc/ijmsc-v6-n6/v6n6-1.html.

[3] S. M. Yoosuf and A. Kuttipulackal, “The connected domination polynomial of some graph constructions,” *Journal of Physics: Conference Series* 1850 (2021), 012043, DOI 10.1088/1742-6596/1850/1/012043.

[4] A. Vijayan and M. Felix Nes Mabel, “Connected Domination Polynomial of Some Graphs,” *IOSR Journal of Mathematics* 12(4) (2016), 13–16, DOI 10.9790/5728-1204031316.

[5] P. Shao and C. Zhao, “On the Roots of Connected Domination Polynomials,” arXiv:2609.06569 (2026), https://arxiv.org/abs/2609.06569.

[6] M. H. Akhbari, F. Movahedi, and M. Arslanov, “On the doubly connected domination polynomial of a graph,” *Asian-European Journal of Mathematics* 12(3) (2019), 1950036, DOI 10.1142/S1793557119500360.

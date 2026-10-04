# Chromatic compression of proper relational covers
## Finding
Let \(N=(W,(R_i)_{{i\in A}},v)\) be a finite relational model with \(|W|=m\) and \(|A|\ge 2\). Define the **joint-accessibility conflict graph** \(G_N\) on vertex set \(W\) by putting an undirected edge \(\{{x,y}}\) between distinct worlds exactly when either \(xR_i y\) for every \(i\in A\), or \(yR_i x\) for every \(i\in A\). Write \(q=\chi(G_N)\).

There is a proper relational model \(\widetilde N\) with exactly \(mq\) worlds and a surjective bounded morphism \(\pi:\widetilde N\to N\). For each agent separately, if \(R_i\) is reflexive, symmetric, transitive, serial, or Euclidean, then the corresponding lifted relation has the same property.

This quantitatively sharpens the finite construction of Bjorndahl and Sink, which uses \(W\times W\) and hence \(m^2\) worlds. Their construction is recovered by the trivial injective \(m\)-coloring. The compression can be strict whenever \(\chi(G_N)<m\).

The quadratic bound remains a genuine worst case: for the two-agent \(m\)-world S5 model in which both accessibility relations are universal, every proper bounded-morphic cover whose two lifted relations are equivalence relations has at least \(m^2\) worlds.

There is also a boundary at one agent. A one-agent model admits a proper surjective bounded-morphic cover if and only if its accessibility relation has no off-diagonal pair; equivalently, the target is already proper.

## Assumptions and scope
The finite compression theorem assumes at least two agents. The conflict graph is undirected even when the accessibility relations are directed: an edge is inserted when joint accessibility occurs in either orientation. A bounded morphism means a surjective valuation-preserving map satisfying the usual forth and back conditions for every agent.

The lower bound concerns two-agent S5 targets and covers whose lifted relations remain equivalence relations. It does not claim that \(m\chi(G_N)\) is the globally smallest proper cover for every model.

## Proof
Choose a proper coloring \(c:W\to\mathbb Z_q\). Set
\[
\widetilde W=W\times\mathbb Z_q,
\]
and let \(\pi(x,t)=x\). Lift valuations through \(\pi\). Distinguish one agent, called agent \(1\). For every other agent \(i\ne 1\), define
\[
(x,t)\,\widetilde R_i\,(y,s)\quad\Longleftrightarrow\quad t=s\text{ and }xR_i y.
\]
For agent \(1\), define
\[
(x,t)\,\widetilde R_1\,(y,s)\quad\Longleftrightarrow\quad t-c(x)=s-c(y)\pmod q\text{ and }xR_1y.
\]

**Properness.** Suppose two lifted worlds are related by every lifted relation. Because there is an agent \(i\ne1\), its relation forces \(t=s\). Agent \(1\) then forces \(c(x)=c(y)\). The projected worlds satisfy \(xR_i y\) for every agent. If \(x\ne y\), then \(\{{x,y}}\) is an edge of \(G_N\), contradicting properness of the coloring. Hence \(x=y\), and with \(t=s\) the two lifted worlds coincide.

**Bounded morphism.** Forth is immediate from the definitions. For back, if \(xR_i y\) with \(i\ne1\), then \((x,t)\widetilde R_i(y,t)\). If \(xR_1y\), take
\[
s=t-c(x)+c(y)\pmod q.
\]
Then \((x,t)\widetilde R_1(y,s)\) and \(\pi(y,s)=y\). Surjectivity and valuation preservation are immediate.

**Preserved frame properties.** For \(i\ne1\), the lifted relation is a disjoint union of \(q\) copies of \(R_i\), one on each constant second-coordinate layer. For agent \(1\), the sets
\[
L_\ell=\{{(x,t):t-c(x)=\ell\pmod q\}},\qquad \ell\in\mathbb Z_q,
\]
partition \(\widetilde W\), and projection restricts to a bijection \(L_\ell\to W\). Thus \(\widetilde R_1\) is also a disjoint union of \(q\) copies of \(R_1\). Reflexivity, symmetry, transitivity, seriality, and Euclideanness therefore transfer relationwise.

**Quadratic worst-case lower bound.** Let \(N_m\) have two agents and \(m\) worlds, with both target relations universal. Let \(p:M\to N_m\) be a surjective bounded morphism from a proper model whose two relations \(S_1,S_2\) are equivalence relations. The back condition implies that every \(S_i\)-equivalence class maps surjectively onto all \(m\) target worlds, so each such class has at least \(m\) elements. Fix one \(S_1\)-class \(C\). It has at least \(m\) elements. No two distinct elements of \(C\) can lie in the same \(S_2\)-class, because then they would be related by both agents, violating properness. Hence \(C\) meets at least \(m\) distinct \(S_2\)-classes, each of size at least \(m\). Therefore \(|M|\ge m^2\). The Bjorndahl--Sink construction attains \(m^2\).

**One-agent boundary.** If a one-agent target contains an off-diagonal edge \(xRy\), choose a preimage \(u\) of \(x\) under any alleged surjective bounded morphism from a proper source. Back supplies \(v\) with \(u\widetilde Rv\) and image \(y\). Since \(x\ne y\), also \(u\ne v\), contradicting one-agent properness. Conversely, if the target has no off-diagonal edge, it is already proper and the identity map is a cover.

## Verification
The bundled `verify_properization.py` independently constructs conflict graphs, computes exact chromatic numbers for small cases, builds the compressed cover, and checks properness and all bounded-morphism back/forth conditions on randomized finite models. It also checks relation-property preservation on randomized equivalence relations and verifies the examples \(\chi(C_5)=3\) and \(\chi(K_5)=5\). Its expected output is `VERIFY_OK`.

## Relationship to prior work
Bjorndahl and Sink introduced a general properization of relational structures and, in the finite case, take \(\widetilde W=W\times W\). They use ordinary second-coordinate layers for all but one agent and a modularly skewed partition for the distinguished agent; projection is a surjective bounded morphism. Their finite construction therefore has \(m^2\) worlds. The present result observes that injective world labels are stronger than necessary: only pairs that are jointly accessible for every agent need different labels. Replacing injective labels by a minimum proper coloring gives the \(m\chi(G_N)\) construction.

The earlier STACS 2022 work on simplicial epistemic models uses an unwinding construction for a particular non-proper canonical model. Bjorndahl and Sink explicitly contrast that approach with their property-preserving construction. Neither inspected source gives the conflict-graph compression or the two-agent S5 size lower bound.

## Limitations
The theorem is finite and assumes at least two agents for the compressed construction. The one-agent obstruction is stated separately. The quantity \(m\chi(G_N)\) is an achieved cover size, not asserted to be the minimum for every individual model. The originality conclusion is limited to the conflict-graph compression, its one-agent boundary, and the stated two-agent S5 worst-case lower bound; terminology outside the inspected modal/simplicial literature could conceal an equivalent construction.

## References
1. Adam Bjorndahl and Philip Sink, *A Note on Proper Relational Structures*, arXiv:2506.17142v1, 20 June 2025. https://arxiv.org/abs/2506.17142
2. Éric Goubault, Jérémy Ledent, and Sergio Rajsbaum, *A Simplicial Model for KB4n: Epistemic Logic with Agents That May Die*, STACS 2022, DOI 10.4230/LIPIcs.STACS.2022.33.
3. Adam Bjorndahl and Philip Sink, *A Semantics for Belief in Simplicial Complexes*, EPTCS 447 (2026), pp. 173--188; arXiv:2512.14647.

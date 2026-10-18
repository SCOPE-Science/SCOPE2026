# Fourteen vertices are necessary and sufficient for reentrant optimal vaccination on rooted trees

## Finding

**Theorem (sharp rooted-tree vaccination threshold).** Let \(T\) be a finite, simple, undirected tree with a fixed initially infected root \(r\) and \(n\ge2\) vertices. Every edge transmits infection independently with the same probability \(p\in(0,1)\) in a one-generation infectious period (Reed–Frost SIR). Exactly one susceptible vertex \(v\ne r\) is fully vaccinated before transmission. Let \(G_v(p)\) be the resulting reduction, compared with no vaccination, in the expected total number of individuals ever infected. Call \(v\) *reentrantly optimal* when there exist \(0<p_1<p_2<p_3<1\) such that \(v\) maximizes \(G_w(p_j)\) among all \(w\ne r\) for \(j=1,3\), but fails to maximize it at \(p_2\).

No tree on at most \(13\) vertices has a reentrantly optimal vertex. There is a \(14\)-vertex tree with a root and two neighbors \(A,B\), for which \(B\) is the **unique** optimal vaccination target for \(p\in(0,\alpha)\cup(\beta,1)\), while \(A\) is unique optimal for \(p\in(\alpha,\beta)\), where \(\alpha\approx0.436911127214511\) and \(\beta\approx0.719739963708202\) are the only roots in \((0,1)\) of
\[
1-3p+p^2+p^3+p^4=0.
\]
The two targets tie at those two points, and no other target is optimal at any \(0<p<1\).

## Assumptions and scope

Vaccination removes one non-root vertex and its contacts before any transmission. Every non-root vertex initially is susceptible. In each infectious generation an infectious individual independently attempts transmission to each susceptible neighbor with probability \(p\), then recovers permanently. On a tree, the final infected cluster is exactly the root cluster of independent bond percolation. No susceptible vertices can infect others until infected. We optimize the *unconditional expected final number saved by the single vaccine*, not the probability of containing an outbreak, the infection peak, or a time-dependent treatment policy. Infection attempts are independent and homogeneous; no background infection, breakthrough infections, or secondary seeding occur.

Root the tree at \(r\). For any \(v\ne r\), its descendants include itself. A root-neighbor branch has a *level profile* \(a=(a_0,a_1,\ldots,a_d)\) with \(a_0=1\) and every \(a_i\) a positive integer: \(a_i\) counts branch vertices at distance \(i\) below the branch head. Its vertex count is \(\sum_i a_i\). Any such positive profile is realized by a tree (attach all vertices on each new level to a chosen vertex on the previous level).

## Proof

**1. Exact objective and neighbor reduction.** On a tree there is a unique root–vertex path. Vaccinating \(v\) removes infection from exactly the vertices in its rooted descendant subtree that otherwise would be reached from \(r\). By linearity of expectation and independence along the unique path,
\[
G_v(p)=\sum_{u\in\operatorname{desc}(v)}p^{d(r,u)}.
\]
If \(v\) is not a root-neighbor, its first ancestor \(w\) adjacent to \(r\) has \(G_w(p)>G_v(p)\) for every \(p\in(0,1)\): the summands for descendants of \(v\) are identical and the difference includes at least \(p\) for \(w\). Thus global optima are precisely among root-neighbor branches. For profile \(a\), the benefit is
\[
B_a(p)=p\sum_{j=0}^d a_jp^j.
\]
For two branch profiles \(a,b\), cancel their identical first terms to obtain
\[
B_a(p)-B_b(p)=p^2Q_{a,b}(p),\qquad Q_{a,b}(p)=\sum_{j\ge1}(a_j-b_j)p^{j-1},
\]
where missing coefficients are zero.

**2. Why two parameter reversals require two interior roots.** If a target is optimal at \(p_1\) and \(p_3\) but not at \(p_2\), choose a root-neighbor competitor that strictly defeats it at \(p_2\). The target's benefit difference with that *fixed* competitor is nonnegative at \(p_1,p_3\) and strictly negative at \(p_2\). By continuity it has two distinct zeros in \((0,1)\). Thus the associated nonzero polynomial \(Q_{a,b}\) must have at least two distinct interior roots.

**3. Exact finite lower bound.** If the whole tree has at most \(13\) vertices, two competing root-neighbor branches have combined size at most \(12\). Every possible level profile of branch size \(s=1\) is \((1)\); for \(s\ge2\) every profile is \((1,c_1,\ldots,c_k)\), with \((c_1,\ldots,c_k)\) a positive integer composition of \(s-1\). Consequently, enumerating the ordered pairs with \(s_a+s_b\le12\) covers *every* pair of branch profiles even in trees with additional branches. There are exactly \(6144\) pairs. Dropping zero coefficients, Descartes' rule of signs excludes two positive roots unless \(Q_{a,b}\) has at least two sign changes. Exactly \(150\) ordered pairs survive this filter. An exact rational Sturm computation on these cases finds \(140\) with zero distinct interior roots and \(10\) with one; none has two. The standalone checker generates every composition, implements rational polynomial division and one-sided Sturm sign variations at \(0\) and \(1\), and prints these counts. These are exhaustive finite computations, not randomized trials. Together with step 2, they rule out reentrance for \(n\le13\).

**4. Sharp fourteen-vertex construction.** Take a root with exactly two branches. The branch at \(A\) has profile \((1,1,4)\): \(A\) has one child, which has four children. The branch at \(B\) has profile \((1,2,1,1,1,1)\): \(B\) has two children; one continues in a chain of four more levels. The tree has \(1+6+7=14\) vertices. Their benefits are
\[
B_A(p)=p+p^2+4p^3,\qquad B_B(p)=p+2p^2+p^3+p^4+p^5+p^6.
\]
Thus
\[
B_A(p)-B_B(p)=p^2(-1+3p-p^2-p^3-p^4).
\]
The parenthesized polynomial is negative at \(p=0\) and \(p=1\), but equals \(1/16>0\) at \(p=1/2\). It therefore has at least two roots in \((0,1)\), and by Descartes' rule it has at most two positive roots, counted with multiplicity (its coefficient signs, in descending powers, have exactly two changes). The roots are distinct and simple, and the displayed optimality intervals follow. Every other vertex is strictly dominated by \(A\) or \(B\), by step 1. This proves the claimed sharpness.

## Verification

Run `python verification/reentry_check.py` using Python 3 with no additional packages. The checker independently enumerates the \(6144\) ordered branch-profile pairs and carries out exact Sturm counts on the \(150\) eligible differences, verifies the construction and both roots, and separately enumerates all \(2^{13}\) edge states of the specified \(14\)-vertex tree at each of \(p=1/10,1/2,9/10\). It directly compares the expected saved populations after deleting candidate vertices, without relying on the derived benefit formula. All checks passed. The polynomial identities and logical reductions in this proof establish the infinite continuum of probability values; the finite enumeration is used only for the finite \(13\)-vertex cutoff.

## Relationship to prior work

Floyd, Kay and Shapiro (2007/2008) proved monotonicity principles for time-independent SIR network vaccination by a transmission/percolation representation; their theorem does not compare the ranking of distinct vaccine targets as \(p\) varies. Shapiro and Delgado-Eckert (2010) studied infection probability and its computational complexity in SIR networks. DuBois (2011), Chapter 3.1, studied selecting epidemic-vaccination targets by expected infection-subtree sizes on large social networks; his inequality and heuristic supply particularly close background for the objective, but do not yield the sharp \(13\)-versus-\(14\) bound or the two-switch construction. Yuan, Alderson, Stromberg and Carlson (2015) studied stochastic vaccine allocation among two non-interacting populations, a different optimization domain.

A related but distinct finite-tree problem concerns which *initial epidemic seed* maximizes expected reach when the seed varies. Our fixed-seed, single-vaccine objective does not follow from a maximization theorem for initial seeds, even if a similar polynomial can occur in examples: its universal lower bound requires the complete root-neighbor profile argument above. We claim no novelty for the underlying bond-percolation representation, the expected-subtree formula considered in isolation, or Descartes/Sturm theory.

## Limitations

The sharp bound is for a single fixed root, one fully effective pre-outbreak vaccine, homogeneous independent transmission, and finite trees. It does not classify arbitrary graphs, multiple vaccines, uncertain infection sources, directed/heterogeneous contacts, imperfect vaccination, or alternative intervention objectives. Repeated numerical or exact evaluations of a particular graph cannot by themselves establish universal minimality; the exhaustive profile enumeration is essential. Other formulations in reliability theory or epidemic-intervention optimization may contain an equivalent sharp cutoff; this bibliographic risk remains despite the targeted primary-source comparison. The theorem is not an empirical vaccination recommendation.

## References

1. W. Floyd, L. Kay, and M. Shapiro, *Some elementary properties of SIR networks, or, Can I get sick because you got vaccinated?*, Bull. Math. Biol. 70 (2008), DOI: 10.1007/s11538-007-9275-0. Author manuscript: https://personal.math.vt.edu/floyd/research/papers/epidemics.pdf (manuscript date 2007-08-21; indexed online 2007-11-30).
2. M. Shapiro and M. Delgado-Eckert, *Finding an individual's probability of infection in an SIR network is NP-hard*, preprint first submitted 2010-01-04, arXiv:1001.0595, https://arxiv.org/abs/1001.0595.
3. T. DuBois, *Using and Manipulating Probabilistic Connectivity in Social Networks*, PhD dissertation, University of Maryland (2011), Chapter 3.1, institutional full text: https://api.drum.lib.umd.edu/server/api/core/bitstreams/5e421ab1-ed23-4f50-a2aa-87f8eada1881/content.
4. E. C. Yuan, D. L. Alderson, S. Stromberg, and J. M. Carlson, *Optimal Vaccination in a Stochastic Epidemic Model of Two Non-Interacting Populations*, PLOS ONE 10 (2015), DOI: 10.1371/journal.pone.0115826.
5. D. Hall and L. Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation* (2023); model comparison only.

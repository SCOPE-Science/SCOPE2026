# Minimum super dominating sets in spiders with two- and three-edge arms

## Finding

Let \(a,b\) be nonnegative integers with \(a+b\geq 3\). Write \(T_{a,b}\) for the tree obtained by joining one endpoint of \(a\) mutually disjoint paths of length two and \(b\) mutually disjoint paths of length three at one common vertex \(c\). The arms are individually labeled, so distinct subsets of vertices are counted separately. Let \(\gamma_{\mathrm{sp}}(T)\) be the minimum size of a *super dominating set*: a subset \(S\) for which every \(w\notin S\) has a neighbor \(v\in S\) satisfying \(N(v)\setminus S=\{w\}\). Let \(N_{\mathrm{sp}}(T)\) count the subsets attaining this minimum.

**Theorem.** For all the indicated parameters,
\[
\gamma_{\mathrm{sp}}(T_{a,b})=
\begin{cases}
a+1,& b=0,\\
a+2b,& b\geq1,
\end{cases}
\qquad
N_{\mathrm{sp}}(T_{a,b})=
\begin{cases}
2^a+a,&b=0,\\
3^b-2^b+b2^{b-1},&b\geq1.
\end{cases}
\]
In particular, when at least one arm has length three, adding arbitrarily many length-two arms does not change the number of minimum super dominating sets. Every minimum set is classified explicitly below.

For the classification, write B for a vertex in \(S\) and W for a vertex outside \(S\), and record an arm from its neighbor of \(c\) outward. When \(b=0\), the minimum sets are exactly (i) \(c\) black, with each two-edge arm independently BW or WB; and (ii) \(c\) white, with exactly one two-edge arm BB and every other arm WB. When \(b\geq1\), the minimum sets are exactly (iii) \(c\) white, every two-edge arm WB, every three-edge arm chosen from BBW, BWB, WBB, with at least one BBW; and (iv) \(c\) black, every two-edge arm BW, exactly one three-edge arm WWB, and every remaining three-edge arm independently BBW or BWB.

## Assumptions and scope

All graphs are finite, simple and undirected. The hub has degree \(a+b\geq3\); all arms have exactly two or three edges, not merely at most three. The super domination condition involves *open* neighborhoods, and a witness must have **exactly one** neighbor outside the chosen set. The theorem enumerates minimum sets (not all super dominating sets), with each vertex individually distinguished. Formulas are unchanged by permuting the arms, but the enumeration does not quotient by graph automorphisms.

## Proof

Write \(B\) for a selected vertex and \(W\) for an unselected vertex. A white leaf requires its only neighbor to be black, and that black neighbor must have no other white neighbor. This observation completely determines the local arm states.

**Local lemma, black hub.** When \(c\in S\), the possible patterns on a length-two arm are BW, WB, and BB. On a length-three arm they are BBW, BWB, WBB, WWB, and BBB. The one-black pattern WWB is special: its first white vertex can only be super dominated by the hub, so it is allowed precisely when this first vertex is the hub's **only white neighbor** among *all* arms. All the other listed patterns satisfy the super domination requirement at white arm vertices without relying on the hub, so impose no further condition.

To check the list, on a two-edge arm \(c-u-v\), simultaneous whiteness of \(u,v\) leaves the white leaf without any black neighbor. All remaining patterns work when \(c\) is black. On a three-edge arm \(c-u-v-w\), if \(w\) is white then \(v,u\) must both be black (BBW). If \(w\) is black, enumerate the four possible memberships of \(u,v\): BWB, WBB, WWB, BBB. In WWB, the white first vertex \(u\) is adjacent only to the black hub and the white \(v\), so its sole possible witness is \(c\); the second white vertex \(v\) is witnessed by the black leaf. This proves both necessity and sufficiency of the stated hub condition.

**Local lemma, white hub.** When \(c\notin S\), every two-edge arm is WB or BB, and every three-edge arm is BBW, BWB, WBB, or BBB. Again all their white internal vertices are independently witnessed. The hub is super dominated exactly when *at least one* two-edge arm has pattern BB or at least one three-edge arm has pattern BBW or BBB. To verify the lists, a white leaf at the end of a two-edge arm would force its middle vertex black, but that middle vertex has both the hub and the leaf white and cannot witness the leaf. Thus the leaf is black. In a three-edge arm, a white leaf forces BBW; when the leaf is black, two consecutive internal white vertices are impossible because the vertex next to the hub would have no black neighbor. The surviving patterns are BWB, WBB, BBB. For the hub to have a black witness with no other white neighbor, its adjacent first vertex must be black and its second vertex also black; this is BB on a short arm, or BBW or BBB on a long arm.

**Minimum cardinality, black hub.** Every two-edge arm costs at least one black vertex. Each three-edge arm costs at least two, except for WWB, which costs one and is possible on at most one arm because the hub must have a unique white neighbor. Consequently, if \(b\geq1\),
\[
|S|\geq1+a+[1+2(b-1)]=a+2b.
\]
Equality forces one WWB arm, all remaining long arms of two black vertices, and every short arm of one black vertex. As the exceptional WWB requires the hub's unique white neighbor, every other arm must begin with B. Thus the short arms are forced BW and the remaining long arms are BBW or BWB. All such patterns are valid. There are \(b2^{b-1}\) choices. If \(b=0\), the minimum with a black hub is \(a+1\), attained by independently choosing BW or WB on each short arm, giving \(2^a\) choices.

**Minimum cardinality, white hub.** Every short arm costs at least one black vertex and each long arm at least two. For \(b\geq1\), equality at \(a+2b\) forces all short arms to be WB and all long arms to have one of the three two-black patterns BBW, BWB, WBB. To witness the white hub, at least one long arm must be BBW. There are \(3^b-2^b\) choices; they are all valid. If \(b=0\), the hub can be witnessed only by a short arm BB, so the minimum size is \(a+1\); equality forces exactly one BB short arm and WB everywhere else, giving \(a\) choices.

Both hub cases attain the displayed lower bounds. Their disjoint counts sum to the claimed formulas, and the equality cases prove the exhaustive classification. \(\square\)

## Verification

The accompanying standalone program `verify.py` reconstructs the graphs as adjacency bitmasks; independently tests the defining private-neighbor condition on every subset of each of 24 profiles with up to 17 vertices (761,216 subsets); then compares **the complete sets of minimum masks** with the classified configurations, not merely their sizes. It additionally tests 66,549 constructed minimum sets across 78 larger profiles and checks the symbolic cardinalities of the classification. Invoke `python verify.py`. Recorded output is supplied in `verification_output.txt`. This finite computational check corroborates, but does not replace, the infinite combinatorial proof.

## Relationship to prior work

Ghanbari, Jäger and Lehtilä introduced \(N_{\mathrm{sp}}(G)\) and determined it for paths, cycles, friendship graphs and several other classes in *Super Domination: Graph Classes, Products and Enumeration* (arXiv:2209.01795, 5 September 2022). In their concluding questions they specifically propose counting minimum super dominating sets in trees. Their path results cover the degenerate case of exactly two arms (not part of the theorem's domain); their friendship result concerns triangular cycles attached at a hub, not trees.

Bujtás, Ghanbari and Klavžar proved the general tree formula \(\gamma_{\mathrm{sp}}(T)=|V(T)|-\nu(T)\), where \(\nu\) denotes maximum matching size, in *Computational complexity aspects of super domination* (arXiv:2302.08862, Theorem 3.1). In particular, **the numerical minimum size is not claimed as a new invariant formula**. Its inclusion here sets the degree at which to enumerate all minimum sets; the new mathematical contribution is their full classification and exact counts on this two-parameter spider family.

Related published results on minimum sets of one-leaf corona graphs apply to a different class: in \(T_{a,b}\) every arm has length at least two and the center has no leaf neighbor, so this spider is not such a corona. The 2024 work *Super Domination Polynomial of a Graph* introduces all-size enumerators and formulas for some graph classes, but its chapter text was not available for a decisive family-by-family comparison; its possible coverage is a bibliographic risk, not evidence of absence.

## Limitations

No formula is asserted for spiders with arms of length one or greater than three, for arbitrary trees, or for the full super domination polynomial. Completeness is for the stated family only. The originality comparison may be incomplete for inaccessible or unindexed treatments, particularly the 2024 chapter just noted. No independent scientific audit has been performed.

## References

1. N. Ghanbari, G. Jäger and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795 (first posted 2022-09-05), §§6–7. https://arxiv.org/abs/2209.01795
2. C. Bujtás, N. Ghanbari and S. Klavžar, *Computational complexity aspects of super domination*, Theoretical Computer Science 975 (2023), 114137, arXiv:2302.08862, Theorem 3.1 and Corollary 3.2. https://doi.org/10.1016/j.tcs.2023.114137
3. P. A. Kaidash, *Super Domination Polynomial of a Graph*, Communications in Computer and Information Science 2239 (2024), 85–95. https://doi.org/10.1007/978-3-031-73365-9_6

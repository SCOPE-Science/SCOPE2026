# A sharp rank-five genericity threshold for finite Paley tournaments

## Finding

Let \(q\ge7\) be any prime power with \(q\equiv3\pmod4\), and let \(T_q\) denote the Paley tournament of order \(q\). In the directed-edge-only first-order language, write \(\mathcal R\) for the countable random (homogeneous) tournament. Then

\[
T_q\equiv_5\mathcal R\quad\Longleftrightarrow\quad q\in\{67,71,79,83\}\ \text{or}\ q\ge107.
\]

Equivalently, exactly these \(T_q\) satisfy the four-point full orientation-extension property \(P_4\). On the entire specified Paley family, \(P_4\) is also equivalent to the weaker-looking common-dominator property \(S_4\). The qualification to Paley tournaments matters: no assertion is made for arbitrary doubly regular tournaments or for greater logical depths. The threshold is sharp as an *eventual* threshold: \(T_{103}\) fails, although \(T_{67}\), \(T_{71}\), \(T_{79}\), and \(T_{83}\) pass.

## Assumptions and scope

The domain of \(T_q\) is \(\mathbb F_q\). For distinct elements \(a,b\), orient \(a\to b\) exactly when \(b-a\) is a nonzero square. Because \(q\equiv3\pmod4\), \(-1\) is a nonsquare, so this defines a tournament.

Property \(P_4\) means that for every four *distinct* vertices \(a_1,\ldots,a_4\) and all choices of signs \(\epsilon_i\in\{-1,1\}\), there is \(z\notin\{a_1,\ldots,a_4\}\) such that \(\chi(z-a_i)=\epsilon_i\), with \(\chi\) the quadratic character extended by \(\chi(0)=0\). Property \(S_4\) asks only for a vertex dominated by all four selected vertices (the pattern with all signs positive). The countable random tournament \(\mathcal R\) realizes every finite prescribed orientation pattern.

The family begins at \(q=7\), excluding the three-vertex case in which the four-point condition is vacuous. The logical language names only equality and a directed binary edge relation; it does not name the field operations.

## Proof

**Large-field lemma.** Fix \(q\equiv3\pmod4\), four distinct elements \(a_1,\ldots,a_4\), and four signs \(\epsilon_i\). The number \(N\) of witnesses is

\[
16N=\sum_{z\notin\{a_1,\ldots,a_4\}}\prod_{i=1}^{4}(1+\epsilon_i\chi(z-a_i)).
\]

Expand by subsets of \(\{1,2,3,4\}\). The constant term contributes \(q-4\). For a single factor, the full character sum is zero; deleting the three positions away from its root changes it by at most three. For two distinct linear factors, the full quadratic-character sum is \(-1\), and removing the two other positions changes it by at most two, so the absolute value is at most three. For three distinct linear factors, the standard quadratic-character Weil bound is \(2\sqrt q\), with one additional removed point contributing at most one. For four distinct factors, the Weil bound is \(3\sqrt q\), and no nonzero terms are removed at the four roots. Consequently,

\[
16N\ge(q-4)-4(3)-6(3)-4(2\sqrt q+1)-3\sqrt q
=q-38-11\sqrt q.
\]

At \(q=191\), the right-hand side is strictly positive and it increases for larger \(q\). Thus **every** admissible prime power \(q\ge191\) satisfies \(P_4\). This is an infinite proof, not a numerical extrapolation.

**Exhaustive bounded range.** The admissible prime powers from seven through 190 are precisely

\[
7,11,19,23,27,31,43,47,59,67,71,79,83,103,107,127,131,139,151,163,167,179.
\]

For these 22 orders, the included C++17 verifier constructs the exact finite field and quadratic-residue orientations, then exhausts every four-subset *containing zero* and each of its sixteen orientation prescriptions. Translation is a tournament automorphism and carries some vertex of any four-subset to zero, so these enumerations exhaust all four-subsets, not merely a sample. For \(q=27\), the verifier uses the explicitly irreducible polynomial \(X^3+2X+1\) over \(\mathbb F_3\); the other orders are prime. All adjacency masks are checked directly against the quadratic-residue definition.

The minimum witness count over every prescription is positive exactly for

\[
q\in\{67,71,79,83,107,127,131,139,151,163,167,179\}.
\]

The verifier separately takes the minimum count in the all-positive pattern (property \(S_4\)). The positivity outcomes agree *exactly* with those for \(P_4\), including all failures. This proves both the finite classification and \(P_4\iff S_4\) for the bounded range. For \(q\ge191\), \(P_4\) was proved above, hence \(S_4\) follows. The reverse implication is therefore established for the entire family by combining these two exhaustive cases.

**Logical step.** If two tournaments satisfy \(P_4\), Duplicator wins the five-round Ehrenfeucht–Fraïssé game: after at most four selections on either side, any new directed-edge pattern over the previously selected vertices can be matched, since \(P_4\) implies the analogous property for fewer than four selected vertices (pad with distinct auxiliary vertices and arbitrary orientation prescriptions). Therefore \(T_q\equiv_5\mathcal R\) whenever \(T_q\) satisfies \(P_4\). Conversely, each fixed four-sign extension axiom is a first-order sentence of quantifier rank five. If any orientation prescription fails for a four-set, its corresponding rank-five sentence separates \(T_q\) from \(\mathcal R\), which satisfies every such axiom. Hence rank-five equivalence is *equivalent* to \(P_4\).

Finally, in \(T_{103}\), the four vertices \(\{0,1,16,47\}\) have no common dominated vertex: this is an explicit failure of \(S_4\) (and \(P_4\)). Together with the positive checks at the allowed orders and the large-field lemma, this makes 107 the *sharp eventual* threshold even though lower admissible orders can satisfy the property.

## Verification

Compile and run the complete, deterministic certificate with

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic paley_tournament_p4_verifier.cpp -o paley_check
./paley_check
```

The attached `paley_tournament_p4_verifier_output.txt` records every eligible order through 190, the number of four-sets containing zero, the minimum witness count across sixteen patterns, the minimum all-positive witness count, and a missing pattern when one exists. It ends with `EXHAUSTIVE_FINITE_CASES_OK`. Code inspects each actual finite-field orientation pattern; finite enumeration is used only below the rigorously proved 191 cutoff. The polynomial \(X^3+2X+1\) has no root in \(\mathbb F_3\), hence is irreducible, and supplies the unique nonprime field appearing in the bounded range.

## Relationship to prior work

Bonato, Gordinowicz and Prałat (2010) study existentially closed tournaments, establish general constructions and bounds, and computationally verify \(T_{67}\) as a four-existentially closed example. Their large-order sufficient condition is not the present exact prime-power membership criterion. Bozóki (2014), drawing on earlier work, records the least *common-dominator* (\(S_4\)) example at prime order 67, but \(S_4\) does not logically imply \(P_4\) for arbitrary tournaments. Brouwer's compiled domination-number table contains an exact independent comparison for the weaker property, including the exceptional order 103; it is not a full sixteen-pattern extension census. Javier, Llano and Zuazua (2026) establish \(P_3\) results, reaffirm \(T_{67}\) has \(P_4\), and ask whether \(S_k\iff P_k\) for vertex-transitive doubly regular tournaments. The present theorem settles their question for \(k=4\) **within the Paley subfamily only**; it does not settle their general question. No checked source states the complete rank-five criterion or proves the exact implication for all prime-power Paley tournaments.

## Limitations

The classification concerns exactly the edge-language rank-five generic theory, not all rank-five equivalence classes among Paley tournaments, not higher quantifier ranks, and not arbitrary vertex-transitive doubly regular tournaments. It relies on the standard Weil character-sum bound for an explicit large-field proof and on a complete finite computation for the residual 22 prime powers. As usual, literature searches do not establish absolute historical priority; an equivalent statement in unindexed sources remains a risk. Independent scientific validation has not been performed.

## References

- A. Bonato, P. Gordinowicz, and P. Prałat, “Bounds and constructions for n-e.c. tournaments,” *Contributions to Discrete Mathematics* 5(2) (2010), 52–66. Published 2010-09-28. https://cdm.ucalgary.ca/article/view/62061
- S. Bozóki, “Nontransitive dice sets,” *Miskolc Mathematical Notes* (2014), especially Proposition 1 and the surrounding discussion. https://real.mtak.hu/62873/1/Bozoki-MiskolcMathNotes-2014.pdf
- N. Y. Javier, B. Llano, and R. Zuazua, “2- and 3-existentially closed tournaments,” *Contributions to Discrete Mathematics* 21(1) (2026), 73–90, especially §4 and Problem 5.6. https://cdm.ucalgary.ca/article/download/78881/58831/277078
- A. E. Brouwer, “Paley graphs,” domination-number tables for Paley tournaments. https://aeb.win.tue.nl/graphs/Paley.html
- R. L. Graham and J. H. Spencer, “A constructive solution to a tournament problem,” *Canadian Mathematical Bulletin* 14 (1971), 45–48. https://doi.org/10.4153/CMB-1971-007-1

# The eight-species threshold for complete coextinction-profile ambiguity in mutualistic networks

## Finding

Consider a finite connected, simple plant–pollinator interaction graph with two known and distinguished guilds. Every species has at least one interaction, and no two species in the same guild have identical neighborhoods. Remove pollinator species uniformly without replacement and declare a plant lost precisely when all its pollinators have been removed. For every possible number of retained pollinators, suppose the entire probability distribution of the number of surviving plants is known.

**Theorem (sharp identification boundary).** For any two such networks with the same positive numbers of plant and pollinator species and **at most seven species in total**, agreement of all these distributions forces a plant-/pollinator-preserving graph isomorphism. The statement is false for **eight** species, even when both networks are connected, contain no equal-neighborhood twins in either guild, and have identical degree multisets within both guilds. Indeed, the following two nonisomorphic four-plant, four-pollinator networks have identical *complete* surviving-plant count distributions at every retention depth, but one contains no four-cycle and the other contains exactly one.

Let the pollinator guild be \(Q=\{q_1,q_2,q_3,q_4\}\), with plant neighborhoods:

| Plant | Network \(A\) | Network \(B\) |
|---|---|---|
| \(p_1\) | \(\{q_1\}\) | \(\{q_1\}\) |
| \(p_2\) | \(\{q_1,q_2\}\) | \(\{q_1,q_2\}\) |
| \(p_3\) | \(\{q_2,q_3\}\) | \(\{q_2,q_3\}\) |
| \(p_4\) | \(\{q_1,q_3,q_4\}\) | \(\{q_2,q_3,q_4\}\) |

For both networks the conditional count histogram \(H(k,y)\), meaning the number of \(k\)-element retained-pollinator subsets that leave \(y\) viable plants, is:

| Retained pollinators \(k\) | Nonzero \((y,H(k,y))\) |
|---:|---|
| \(0\) | \((0,1)\) |
| \(1\) | \((1,1),(2,2),(3,1)\) |
| \(2\) | \((2,1),(3,3),(4,2)\) |
| \(3\) | \((3,1),(4,3)\) |
| \(4\) | \((4,1)\) |

All undisplayed entries vanish. Both plant and pollinator degree multisets are \((1,2,2,3)\). Network \(A\) has no four-cycles; network \(B\) has precisely one four-cycle, so they are not graph isomorphic, even if the guild distinction were forgotten.

**Degree-information theorem.** In any such graph, without an upper size bound, the full set of count distributions determines the degree multiset of *each* guild. Thus the eight-species failure persists even though every individual-guild degree statistic recoverable from this observation is already equal.

## Assumptions and scope

Let \(G=(P\sqcup Q,E)\) be a finite connected simple bipartite graph with distinguished disjoint guilds \(P\) (plants) and \(Q\) (pollinators), \(|P|=m\ge1\), \(|Q|=n\ge1\). No vertex is isolated. In each guild no two distinct vertices have the same open neighborhood in the opposite guild (*bi-twin-free*). The graph isomorphisms considered preserve the two named guilds, but do not presume externally known species labels within either guild.

For \(S\subseteq Q\), define
\[
Y_G(S)=\bigl|\{i\in P:N_G(i)\cap S\ne\varnothing\}\bigr|.
\]
For each integer \(0\le k\le n\), draw \(S_k\) uniformly among the \(\binom nk\) \(k\)-subsets and observe the complete law of \(Y_G(S_k)\), not just its mean or variance. Write
\[
H_G(k,y)=\bigl|\{S\subseteq Q:|S|=k,\;Y_G(S)=y\}\bigr|,
\qquad \Pr(Y_G(S_k)=y)=\frac{H_G(k,y)}{\binom nk}.
\]
Both guild sizes are held fixed when comparing two graphs. This is a one-way, binary dependency model: a plant with at least one surviving pollinator persists, and surviving pollinators do not change partners or disappear in response to plant losses.

## Proof

**1. Why the complete profile is a natural invariant.** Under independent retention of each pollinator with probability \(u\), the probability of observing \(y\) viable plants is
\[
\Pr(Y_G=y)=\sum_{k=0}^n H_G(k,y)\,u^k(1-u)^{n-k}.
\]
For fixed \(n\), the \(n+1\) Bernstein basis polynomials on the right are linearly independent. Therefore two graphs of the same guild sizes have identical complete fixed-\(k\) count distributions **if and only if** they have identical complete survivor-count laws at every independent retention probability \(0<u<1\). No species-by-species incidence information is assumed to be observed.

**2. What the profile determines.** For \(k=1\), \(Y_G(\{q\})\) is exactly the degree of pollinator \(q\), so \(H_G(1,y)\) directly gives the pollinator degree multiset. For a plant \(i\), write \(d_i=|N_G(i)|\). It remains nonviable upon retaining \(S\) exactly when \(S\subseteq Q\setminus N_G(i)\). Thus
\[
F_k:=\binom nk\bigl(m-\mathbb E[Y_G(S_k)]\bigr)
=\sum_{i\in P}\binom{n-d_i}{k}.
\]
With \(b_t=\bigl|\{i\in P:n-d_i=t\}\bigr|\), this is the invertible triangular system \(F_k=\sum_{t=k}^{n}b_t\binom tk\). Its exact inverse is
\[
 b_t=\sum_{k=t}^{n}(-1)^{k-t}\binom kt F_k\qquad(0\le t\le n).
\]
Consequently the plant degree multiset is also determined. The inversion is valid for all finite guild sizes; impossible binomial terms are understood as zero. Equal full count profiles automatically imply equal degree multisets on both sides.

**3. A complete finite identification check below eight species.** Encode each of the \(m\) plant neighborhoods by a distinct nonzero \(n\)-bit integer and sort the row masks. Every such graph is represented by a choice of \(m\) distinct masks from \(\{1,\ldots,2^n-1\}\). Reject a candidate if any pollinator column is zero, if two column masks are identical, or if breadth-first search finds a disconnected bipartite graph. This produces every connected bi-twin-free graph of those guild sizes: no other binary incidence matrices satisfy the assumptions.

To remove only harmless relabelings, for each candidate apply all \(n!\) permutations of pollinator columns, sorting the resulting rows each time, and retain the lexicographically smallest row tuple. Two candidates have the same canonical tuple **if and only if** they are side-preserving isomorphic: every plant permutation is absorbed by row sorting, and every pollinator permutation is explicitly tested. For each canonical candidate, enumerate all \(2^n\) retained-pollinator subsets and record the entire integer array \(H_G(k,y)\).

The exact class counts for nonempty guild-size partitions with at most seven total vertices are: one class at \((m,n)=(1,1),(2,2),(2,3),(3,2)\); six classes at \((3,3)\); and nine classes each at \((3,4)\) and \((4,3)\); all other such partitions have zero classes. There are therefore \(28\) classes in total. No two distinct canonical networks of the same guild sizes have identical \(H_G\). The exhaustive executable `verify.py`, using only standard-library integer operations and finite loops justified above, supplies the reproducible complete enumeration and the exact integer certificate `certificate.json`. This is a complete finite argument, not a random search or a numerical approximation.

**4. The eight-species obstruction.** Under the convention that bit \(j-1\) codes \(q_j\), the four row masks for the displayed networks are
\[
A=(1,3,6,13),\qquad B=(1,3,6,14).
\]
Both pass the connectivity, nonisolation, and two-guild twin checks. Directly inspecting the sixteen possible retained-pollinator subsets yields the displayed common \(H\) table; an independently implemented deletion enumeration in `verify.py` gives the same table. Both have degree multiset \((1,2,2,3)\) in each guild. In \(B\), plants \(p_3,p_4\) both meet pollinators \(q_2,q_3\), creating exactly one \(4\)-cycle. In \(A\), every pair of plants has at most one common pollinator, so there are none. Hence these graphs are distinct up to all graph isomorphisms. By step 1 their count distributions also agree for every independent retention probability.

The full eight-species census contains \(57\) side-preserving connected bi-twin-free classes when \((m,n)=(4,4)\), of which five profile classes contain more than one graph (six excess graphs). This additional count is corroborative, not required for the minimum. Steps 3 and 4 together prove eight is the sharp minimum.

## Verification

The accompanying independently executable Python 3 script `verify.py` uses no third-party packages and carries out exact integer enumeration of all admissible small networks. Invoke `python3 verify.py > certificate.json` in a directory containing the script. Its JSON output includes each guild-size census, every profile collision count, the full witness histogram, both guild degree multisets, and both four-cycle counts. It reconstructs the witness histogram again using a distinct pollinator-deletion enumeration and explicitly excludes side-preserving isomorphism by trying every pollinator permutation. The bundled `certificate.json` is the full expected byte-for-byte program output. No floating-point approximations or random sampling are used.

For this result, the exhaustive claim is finite through seven species; the general degree-recovery statement and equivalence of two sampling descriptions are proved algebraically and do not rely on extrapolating the census.

## Relationship to prior work

Memmott, Waser and Price (2004) used pollinator removal and loss of all pollinators as the plant coextinction mechanism, including random pollinator-removal sequences. The present work takes that established ecological model and asks a different inverse question: whether *all* exact count distributions determine the underlying network. The cited ecological paper does not state this finite reconstruction threshold or the two degree-matched networks.

The graph-theoretic *neighborhood polynomial* of Bergold, Hochstättler and Mayer counts vertex subsets with a *common* neighbor, rather than the full two-parameter histogram of the **size of the union** of their neighborhoods. These polynomials are not identified by their names alone. General neighborhood hypergraph studies retain labeled incidence data, which are stronger than the unlabeled count profiles here. The full text of Boros, Gurvich and Zverovich's neighborhood-hypergraph paper was not available for detailed comparison; equivalence under a different graph-polynomial formulation is therefore a remaining originality risk.

Bane, Pocock and James discuss robustness distributions and ecological knockouts, but not the exact degree-preserving eight-species classification in the stated observation model. Mathematical originality is therefore conditional on the available full-text comparisons, and requires independent bibliographic scrutiny before a publication claim.

## Limitations

The ecological rule models only binary dependencies and first-order plant coextinction caused by random pollinator loss; it ignores interaction strength, quantitative reproductive success, phenological timing, adaptive rewiring, cascading pollinator losses, and observational noise. The sharp minimum requires *connected* bi-twin-free networks and distinguishes ecological guilds. If twins, isolated species or other graph classes are admitted, a different minimum may apply. The theorem is not an impossibility statement for identifying networks from labeled observations of individual species survival, which contain much more information. The classification does not count all larger collisions or characterize the identifiability of arbitrary sized graphs. Originality remains subject to accessible but incomplete literature coverage and independent human examination.

## References

1. J. Memmott, N. M. Waser and M. V. Price (2004), *Tolerance of pollination networks to species extinctions*, Proceedings of the Royal Society B 271:2605–2611, doi:10.1098/rspb.2004.2909. First available online 2004-12-06. Open full text: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf.
2. M. S. Bane, M. J. O. Pocock and R. James (2018), *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*, Ecology and Evolution, doi:10.1002/ece3.4529.
3. H. Bergold, W. Hochstättler and U. Mayer (2022), *The Neighborhood Polynomial of Chordal Graphs*, Discrete Mathematics and Theoretical Computer Science 24, doi:10.46298/dmtcs.8388; arXiv:2008.08349.
4. E. Boros, V. Gurvich and I. Zverovich (2008), *Neighborhood hypergraphs of bipartite graphs*, Journal of Graph Theory, doi:10.1002/jgt.20293. Full technical text not inspected.

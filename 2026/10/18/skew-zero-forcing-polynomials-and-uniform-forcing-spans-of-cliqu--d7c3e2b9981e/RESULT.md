# Skew-zero-forcing polynomials and uniform forcing spans of clique bouquets

## Finding
Let \(r\ge 2\) and let \(n_1,\ldots,n_r\ge2\) be integers. Define the **clique bouquet**
\[
G=K_1\vee\bigl(K_{n_1}\sqcup\cdots\sqcup K_{n_r}\bigr),
\qquad N=|V(G)|=1+\sum_{i=1}^r n_i.
\]
Write \(h\) for its common hub and \(B_i\) for the peripheral clique of size \(n_i\). A skew-zero-forcing set \(S\) initially colors its vertices blue and subsequently permits **any** vertex, blue or white, having exactly one white neighbor to color that neighbor blue. Define the cardinality enumerator
\[
\mathcal Z^-(G;z)=\sum_{S\text{ skew-zero-forcing}}z^{|S|}.
\]
Set
\[
Q_i(z)=z^{n_i}+n_i z^{n_i-1}+\binom{n_i}{2}z^{n_i-2},
\qquad E_i(z)=\binom{n_i}{2}z^{n_i-2}.
\]
**Theorem (complete enumerator).** For all parameters above,
\[
\boxed{\mathcal Z^-(G;z)=(1+z)\prod_{i=1}^r Q_i(z)-\prod_{i=1}^r E_i(z).}
\]
Equivalently, \(S\) is skew-zero-forcing if and only if each peripheral clique contains **at most two initially white vertices** and either \(h\in S\), or at least one peripheral clique contains **at most one** initially white vertex.

The inclusion-minimal skew-zero-forcing sets are exactly the minimum-cardinality ones. Their size and number are respectively
\[
\boxed{Z^-(G)=N-2r}
\]
and
\[
\boxed{m^-(G)=\prod_{i=1}^r\binom{n_i}{2}
+\sum_{j=1}^r n_j\prod_{i\ne j}\binom{n_i}{2}.}
\]
The minimal nonempty skew forts (defined below) are **exactly** the three-element subsets within one \(B_i\), together with the sets containing \(h\) and exactly two vertices from **every** \(B_i\).

The skew-zero-forcing span \(\lambda^-(G)\), the number of cardinalities admitting both forcing and nonforcing sets, satisfies
\[
\boxed{\lambda^-(G)=
\begin{cases}
0,&n_1=\cdots=n_r=2,\\
2r-2,&\max_i n_i\ge3.
\end{cases}}
\]
Thus, as soon as one clique blade has at least three peripheral vertices, the span depends **only** on the number of blades, not on their individual orders.

## Assumptions and scope
All graphs are finite, simple, and undirected. There are \(r\ge2\) pairwise disjoint peripheral complete graphs, each with at least two vertices, all joined to one common hub; no edges connect distinct peripheral cliques. The polynomial enumerates **labeled vertex subsets**, not isomorphism orbits. A white vertex is permitted to initiate a skew force. The zero initial set is included in the polynomial definition, but is not successful in this family.

For any nonempty vertex set \(W\), call \(W\) a **skew fort** if every vertex \(v\) has either zero or at least two neighbors in \(W\), that is, \(|N(v)\cap W|\ne1\). A skew-zero-forcing set succeeds if and only if its initially white complement contains no nonempty skew fort: a fort can never receive its first force; conversely, the nonempty white set remaining when a forcing process stalls is a fort.

## Proof
**1. Classification of minimal forts.** Let \(W\) be any nonempty skew fort and let \(w_i=|W\cap B_i|\).

If \(h\notin W\), then \(w_i=1\) is impossible because the peripheral clique has at least one other vertex witnessing exactly one white neighbor. Likewise \(w_i=2\) is impossible because either one of the two white vertices sees the other as its sole white neighbor. Thus any occupied blade has \(w_i\ge3\). Every triple inside a blade is itself a skew fort: its three white vertices each see two whites; all other vertices see either zero or three. It follows that the inclusion-minimal forts without \(h\) are precisely such triples.

If \(h\in W\), no \(w_i\) may equal zero: an outer vertex in an empty blade would have exactly one neighbor in \(W\), namely \(h\). Nor can \(w_i=1\), because its lone white vertex would have \(h\) as its only white neighbor. Hence \(w_i\ge2\) for every \(i\). Every set containing \(h\) and exactly two peripheral vertices in each blade is itself a skew fort: the hub has \(2r\ge4\) white neighbors, a white peripheral vertex has two, and a peripheral vertex outside the set has three. Such sets are inclusion-minimal; any larger fort containing \(h\) contains one of them, or, if any \(w_i\ge3\), also contains a previously described triple. This completes the classification.

**2. All forcing sets.** By the fort criterion, the white complement of a forcing set may not contain any triple from a single blade, so \(w_i\le2\) for each \(i\). If \(h\) is blue, these conditions suffice, because all minimal forts either contain a triple or contain \(h\). If \(h\) is white, the remaining obstruction is a fort comprising the hub and two vertices of every blade. Under \(w_i\le2\), this obstruction occurs precisely when \(w_1=\cdots=w_r=2\). Thus at least one blade must have \(w_i\le1\), proving the asserted equivalence.

**3. Polynomial.** For each blade the generating function for its selected vertices under \(0\le w_i\le2\) is \(Q_i(z)\). If the hub is blue, its contribution is \(z\prod_iQ_i(z)\). If the hub is white, the initial count is \(\prod_iQ_i(z)\), but exactly the configurations with two white vertices in every blade must be removed; their polynomial is \(\prod_iE_i(z)\). Adding the two disjoint cases gives the formula.

**4. Minimum sets and inclusion minimality.** At least \(n_i-2\) peripheral vertices in each blade are blue. If the hub is blue, this implies size at least \(1+\sum_i(n_i-2)=N-2r\), with equality precisely when \(w_i=2\) throughout. If the hub is white, one blade must have \(w_j\le1\), requiring one more selected peripheral vertex than the baseline \(\sum_i(n_i-2)\); equality requires exactly one blade with \(w_j=1\), every other blade with \(w_i=2\). This proves the minimum and the sum-of-products enumeration.

For inclusion minimality, in a successful set containing a blue hub, a blade with \(w_i<2\) has a removable selected peripheral vertex. When every \(w_i=2\), no blue vertex can be removed without creating a fort. In a successful set with white hub, any blade with \(w_i<1\), or two blades with \(w_i\le1\), similarly provides a removable selected vertex. The remaining inclusion-minimal sets therefore have exactly the equality profiles just counted. All of them have size \(N-2r\).

**5. Failed forcing and span.** If all \(n_i=2\), there are no peripheral triple forts and the unique minimal fort consists of every vertex; thus the empty initial set is the only failure, \(Z^-(G)=1\), and \(\lambda^-(G)=0\). Otherwise, a triple inside a blade of size at least three is a fort, yielding a failed set of size \(N-3\). Every nonempty fort contains at least three vertices, so no set with more than \(N-3\) selected vertices fails. Hence \(F^-(G)=N-3\). By monotonicity under adding blue vertices, every cardinality from \(Z^-(G)\) to \(F^-(G)\) has both a forcing and a failing set, while no other cardinality does. Consequently
\[
\lambda^-(G)=F^-(G)-Z^-(G)+1
=(N-3)-(N-2r)+1=2r-2.
\]
All assertions follow.

## Verification
The standalone file `verify.py` constructs the adjacency graph directly, simulates the skew forcing rule from every initial subset for \(182\) ordered blade-size profiles, and compares the resulting coefficient vector against the stated polynomial. It also compares exact minimum counts and failed-set maxima. For profiles of order at most \(11\), it independently enumerates inclusion-minimal skew forts by inspecting all possible neighbor intersections. The recorded output in `verify_output.txt` is

`VERIFICATION_OK profiles=182 initial_subsets=1291680 fort_subsets=71009`

Run `python3 verify.py` using the standard Python library. Exhaustive finite tests verify the implementation and small instances; they are not substituted for the infinite-family proof above.

## Relationship to prior work
Jacob (2023, arXiv:2309.06234) defines the skew zero forcing polynomial and span, and establishes the zero-span behavior of bouquets of odd cycles by reference to earlier failed-forcing results. This explains the specialization with all \(n_i=2\), which is **not** claimed as new. The exact polynomial, minimal-fort classification, heterogeneous clique sizes, and constant nonzero span for \(\max_i n_i\ge3\) are the new statements here.

Cooper and Fickes (2023, arXiv:2303.17419) develop skew-forcing closure and its links with nullspace and matching structures; their inspected graph results do not give the clique-bouquet cardinality enumeration. Johnson, Vick, and Narayan (2022, arXiv:2209.09379) characterize graphs with failed skew zero forcing number one and recall earlier odd-cycle-bouquet results; those assertions do not imply the present polynomial. Related published results count *standard* zero forcing sets of friendship graphs or dissociation sets of uniform windmills; neither uses this skew color-change rule and hence neither implies the heterogeneous full skew-forcing polynomial.

## Limitations
The proof requires at least two blades, each containing at least two peripheral vertices. It does not classify arbitrary block graphs, graph joins, or bouquet families with singleton blades. The originality comparison is bounded by inspected accessible literature and mathematical-record searches; an unindexed equivalent theorem cannot be excluded. Independent scientific validation has not been performed.

## References
1. Bonnie Jacob, *The zero forcing span of a graph*, first posted 2023-09-12, arXiv:2309.06234, https://arxiv.org/abs/2309.06234.
2. Joshua Cooper and Grant Fickes, *Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs*, first posted 2023-03-30, arXiv:2303.17419, https://arxiv.org/html/2303.17419v1.
3. Aidan Johnson, Andrew E. Vick, and Darren A. Narayan, *Characterization of All Graphs with a Failed Skew Zero Forcing Number of 1*, first posted 2022-09-19, arXiv:2209.09379, https://www.mdpi.com/2227-7390/10/23/4463.
4. L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, arXiv:1404.1618, https://arxiv.org/abs/1404.1618. Historical context for the skew rule; not asserted to enumerate clique bouquets.

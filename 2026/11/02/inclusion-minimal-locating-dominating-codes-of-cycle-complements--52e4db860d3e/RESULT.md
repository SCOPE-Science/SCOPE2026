# Inclusion-minimal locating-dominating codes of cycle complements: finite-state enumeration and sharp upper density

## Finding
For every integer \(n\ge7\), put \(H_n=K_n-E(C_n)\). A locating-dominating set \(S\subseteq V(H_n)\) has the property that the open neighborhoods in \(S\) of distinct outside vertices are distinct and nonempty. It is *inclusion-minimal* if no proper subset has that property. Define
\[
M_n(z)=\sum_{\substack{S\subseteq V(H_n)\\S\text{ inclusion-minimal locating-dominating}}}z^{|S|}.
\]

**Theorem.** Let \(S\) have \(k\) selected vertices, in their circular order on the deleted cycle, and let \(a_0,\ldots,a_{k-1}\) be the numbers of unselected vertices between successive selected vertices. Set \(t=|\{i:a_i=3\}|\), and interpret all indices modulo \(k\). Then \(S\) is inclusion-minimal locating-dominating if and only if all the following hold:

* \(0\le a_i\le3\), \(t\le1\), and no consecutive gaps both have length at least \(2\);
* if \(t=0\), then for every \(i\), writing \(p=a_{i-2}\), \(a=a_{i-1}\), \(b=a_i\), \(q=a_{i+1}\),
\[
(a+b\ge3)\ \lor\ (1\le a+b\le2\ \land\ (p\ge2\lor q\ge2));
\]
* if \(t=1\), the corresponding condition for every \(i\) is
\[
(a+b\ge2)\ \lor\ (a+b=1\ \land\ (p\ge2\lor q\ge2)).
\]

These predicates yield **every coefficient** of \(M_n(z)\) by an explicit matrix expression. For \(t=0\) let the states of \(T_0\) be triples in \(\{0,1,2\}^3\). For \(t=1\) let the states of \(T_1\) be triples in \(\{0,1,2,3\}^3\). A transition \((p,a,b)\to(a,b,q)\) exists when neither \((a,b)\) nor \((b,q)\) is a pair of entries both at least \(2\), and the displayed predicate for \(t\) is true. Give this transition weight \(zu^{q+1}\) in \(T_0\) and \(zu^{q+1}y^{\mathbf1_{\{q=3\}}}\) in \(T_1\); otherwise the entry is zero. Then
\[
\boxed{\displaystyle
\sum_{n\ge7}M_n(z)u^n
=[u^{\ge7}]\left\{-u\frac{\partial}{\partial u}\log\det(I-T_0)
-u\frac{\partial}{\partial u}[y]\log\det(I-T_1)\right\}.}
\]
Here \([y]\) means the coefficient of \(y^1\), and \([u^{\ge7}]\) discards powers below seven. Both determinants are polynomials with constant term one, so their formal logarithms are well-defined.

If \(\Gamma_L(H_n)\) denotes the largest size of an inclusion-minimal locating-dominating set, then
\[
\boxed{\Gamma_L(H_n)\le\left\lfloor\frac{4n}{7}\right\rfloor,
\qquad\limsup_{n\to\infty}\frac{\Gamma_L(H_n)}n=\frac47.}
\]
This density bound is asymptotically sharp; no equality for every finite \(n\) is asserted.

## Assumptions and scope
All graphs are finite, simple and undirected. The cycle \(C_n\) uses a fixed cyclic labeling, with \(n\ge7\); its complement is connected. The counting polynomial concerns labeled vertex subsets of this graph. A statement about inclusion-minimal sets is not a statement merely about minimum-cardinality sets. The lower bound on cardinality \(\lceil(2n-2)/5\rceil\) was determined previously and is not claimed as new. A finite word satisfying the gap conditions necessarily has at least three selected vertices when its total order is at least seven.

## Proof
**1. Locating-dominating gaps.** By Lemma 6 of Abdul Gafur--Saputro (2021), a vertex subset is locating-dominating in \(H_n\), for \(n\ge7\), exactly when every circular gap has length at most three, there is at most one length-three gap, and no two adjacent gaps both have length at least two. These established conditions are the starting point; they are not a contribution of the present result. They also imply at least three selected vertices.

**2. Inclusion-minimality.** Fix a selected vertex with adjacent gaps \(a,b\) and next outer gaps \(p,q\). Deleting the vertex merges \(a,b\) into a single gap of length \(c=a+b+1\), leaving all other gaps unchanged. If there was no length-three gap, the reduced set still satisfies the known locating-dominating characterization exactly when \(a+b=0\), or when \(1\le a+b\le2\) and \(p,q\le1\). Indeed, \(c\le3\) is necessary, and if \(c\ge2\) it cannot touch a neighboring long gap. The negation is precisely the displayed \(t=0\) predicate. If exactly one length-three gap already exists, a deletion with \(a+b\le1\) cannot remove that gap; hence the new gap cannot have length three. The reduced set remains locating-dominating exactly when \(a+b=0\), or \(a+b=1\) and \(p,q\le1\). Its negation is the \(t=1\) predicate. Thus every selected vertex is indispensable exactly under the stated simultaneous local predicates. Since the locating-dominating property is monotone under adding selected vertices, forbidding each single-vertex deletion is equivalent to inclusion-minimality.

**3. Exact enumerator.** For either regime, each closed walk of length \(k\) in its triple-state transfer graph spells a circular list of \(k\) successive gaps, with the transition conditions checking each four-gap window. In the second regime, extracting the coefficient of \(y\) selects precisely one gap of length three. The trace \(\operatorname{tr}(T^k)\) counts rooted circular gap lists with weight \(z^ku^n\) (and, in the second regime, \(y\) to the number of length-three gaps). For a given labeled selected set of size \(k\), there are exactly \(k\) possible distinguished selected vertices; conversely, a fixed rooted gap list admits \(n\) possible choices for the distinguished vertex label. Hence multiplying the rooted-list count by \(n/k\) gives the number of labeled sets. The formal identity
\[
-\log\det(I-T)=\sum_{k\ge1}\frac{\operatorname{tr}(T^k)}k
\]
followed by \(u\partial/\partial u\) performs exactly this factor \(n/k\). Restriction to \(n\ge7\) removes the irrelevant smaller orders. This proves the polynomial identity for every coefficient.

**4. Sharp density upper bound.** Consider the \(64\)-vertex directed graph with states \((p,a,b)\in\{0,1,2,3\}^3\), transitions as in \(T_1\) (ignoring generating-function variables), and integer edge weight \(w((p,a,b),(a,b,q))=4q-3\). The independent finite certificate `density_potential.json` lists one integer \(h(s)\) for each state. The standalone `verify.py` checks, by exact integer arithmetic, all \(136\) allowed edges and verifies
\[
h(a,b,q)\le h(p,a,b)+4q-3.
\]
Thus every closed walk has total edge weight at least zero. Every minimal locating-dominating gap sequence supplies such a closed walk: the \(t=1\) predicate applies directly in the one-long-gap regime, and the stronger \(t=0\) predicate implies it in the zero-long-gap regime. Consequently
\[
0\le\sum_i(4a_i-3)=4(n-k)-3k=4n-7k,
\]
which proves the finite upper bound.

For every integer \(m\ge0\), take the cyclic gap list
\[
(3,0,1,0,2,\underbrace{0,1,0,2,\ldots,0,1,0,2}_{m\text{ copies of }(0,1,0,2)},1).
\]
It has exactly one gap of length three; each pair of long gaps is separated, and all four-gap tests of the \(t=1\) predicate hold (in the repeated interior and across both seams). It therefore defines an inclusion-minimal locating-dominating set with \(k=6+4m\) vertices in a graph of order \(n=13+7m\). Its ratio \(k/n\) tends to \(4/7\), proving the stated limsup equality.

## Verification
The standalone program `verify.py` constructs \(H_n\) using its actual adjacency relation and checks the locating-dominating condition from open-neighborhood fingerprints, then checks inclusion-minimality by removing each selected vertex. This independent graph-level oracle and the four-gap criterion agree on all \(32{,}640\) vertex subsets for \(7\le n\le14\). A separate transfer-walk dynamic program matches the complete coefficient dictionaries at those orders and computes the polynomial through \(n=20\). The independent integer certificate contains \(64\) potentials and satisfies each of the \(136\) edge inequalities. Thirty-one explicit members of the sharpness construction are also checked. Running `python3 verify.py` in a directory containing both `verify.py` and `density_potential.json` reports `VERIFY_OK`.

Examples (all numbers count labeled subsets) are
\[
M_8(z)=8z^3+20z^4,\quad
M_{15}(z)=95z^6+450z^7+15z^8,\quad
M_{16}(z)=16z^6+560z^7+284z^8.
\]
Finite computations corroborate the combinatorial classification and verify the finite potential certificate; they are not used as extrapolated proofs of the infinite enumerator.

## Relationship to prior work
Abdul Gafur--Saputro (2021), Lemma 6, supplies the complete **ordinary locating-dominating membership criterion** for cycle complements and Theorem 2 supplies their **minimum cardinality**. The present theorem credits and uses that lemma, but classifies **inclusion-minimal** members, supplies a new all-cardinality polynomial and establishes the sharp asymptotic behavior of the **upper** locating-domination parameter. Chellali--Mimouni--Slater (2010) introduced the upper parameter and proved general bounds; their accessible abstract does not identify this cycle-complement extremal density. Other locating-dominating results on oriented graphs concern a different optimization and do not imply the present un-oriented minimal-set distribution.

## Limitations
No claim of an exact closed finite-order formula for \(\Gamma_L(H_n)\) is made; the statement proves a universal upper bound and a sharp asymptotic limsup. The finite certificate verifies a fixed, explicitly enumerated state graph rather than extrapolating a numerical pattern. The 2010 full article was not available for complete comparison, and not all potentially relevant later or unindexed papers could be inspected; publication priority remains provisional. Independent mathematical auditing has not been performed.

## References
1. A. K. Abdul Gafur and S. W. Saputro, *On Locating-Dominating Set of Regular Graphs*, Journal of Mathematics (2021), article 8147514, first published 2021-09-25. DOI: 10.1155/2021/8147514. Full open-access article: https://onlinelibrary.wiley.com/doi/10.1155/2021/8147514 . Lemma 6, Theorem 2, Theorem 3.
2. M. Chellali, M. Mimouni, and P. J. Slater, *On locating-domination in graphs*, Discussiones Mathematicae Graph Theory 30 (2010), 223--235. DOI: 10.7151/dmgt.1488. Abstract: https://geodesic.mathdoc.fr/item/DMGT_2010_30_2_a2/ .
3. N. Bousquet, Q. Deschamps, T. Lehtilä, and A. Parreau, *Locating-dominating sets: From graphs to oriented graphs*, Discrete Mathematics 346 (2023), 113124. DOI: 10.1016/j.disc.2022.113124.

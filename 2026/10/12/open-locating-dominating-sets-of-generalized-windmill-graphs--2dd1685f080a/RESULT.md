# Open locating-dominating sets of generalized windmill graphs
## Finding
For integers \(r\ge2\) and \(m\ge2\), let
\[
W_{r,m}=K_1\vee rK_m
\]
with universal center \(c\) and pairwise disjoint peripheral cliques \(B_1,\ldots,B_r\), each of order \(m\). For a vertex set \(S\), write its open signature at \(v\) as \(\sigma_S(v)=N(v)\cap S\). An OLD-set is a set for which every \(\sigma_S(v)\) is nonempty and all these signatures are pairwise distinct.

If \(m\ge3\), then
\[
S	ext{ is an OLD-set}\quad\Longleftrightarrow\quad |B_i\setminus S|\le1	ext{ for every }1\le i\le r.
\]
Consequently the complete cardinality enumerator is
\[
\mathcal O_{r,m}(x)=\sum_{S	ext{ OLD}}x^{|S|}=(1+x)(x^m+m x^{m-1})^r=(1+x)x^{r(m-1)}(m+x)^r.
\]
In particular,
\[
\gamma^{OLD}(W_{r,m})=r(m-1),
\qquad
\#\{S:|S|=\gamma^{OLD},\ S	ext{ OLD}\}=m^r.
\]
Every minimum OLD-set omits the center and exactly one vertex from each peripheral clique.

The friendship boundary \(m=2\) is different. In that case, an OLD-set omitting \(c\) must contain all \(2r\) peripheral vertices; an OLD-set containing \(c\) may omit at most one peripheral vertex. Thus
\[
\mathcal O_{r,2}(x)=(2r+1)x^{2r}+x^{2r+1},
\qquad
\gamma^{OLD}(W_{r,2})=2r,
\]
and there are exactly \(2r+1\) minimum OLD-sets.

## Assumptions and scope
Graphs are finite, simple, and undirected. The parameters satisfy \(r\ge2\) and \(m\ge2\). The polynomial variable records cardinality only. The term “OLD-set” means open-neighborhood locating-dominating set: all vertices, including vertices of the code itself, must receive nonempty pairwise distinct open-neighborhood signatures.

The scalar formula \(\gamma^{OLD}(W_{r,2})=2r\) is not asserted as new: \(W_{r,2}=K_1\vee rP_2\), and Chellali–Jafari Rad–Seo–Slater explicitly identify this family among the connected \(C_4\)-free minimum-degree-two graphs with OLD-number one below the order. The claim retained here is the complete characterization and enumeration for all \(m\ge2\), including the exact friendship-family multiplicity, and the exact \(m\ge3\) formula.

## Proof
Fix an OLD-set \(S\). If two distinct vertices \(u,v\in B_i\) were both omitted from \(S\), then
\[
\sigma_S(u)=\sigma_S(v)=(\{c\}\cap S)\cup(S\cap B_i),
\]
contradicting open separation. Hence every blade omits at most one vertex.

Assume first that \(m\ge3\), and conversely suppose every blade omits at most one vertex. Then every blade contains at least \(m-1\ge2\) selected vertices. If \(c\notin S\), a selected peripheral vertex has at least \(m-2\ge1\) selected neighbors in its own blade, while an omitted peripheral vertex has at least \(m-1\) selected neighbors there; therefore every peripheral signature is nonempty. If \(c\in S\), every peripheral signature contains \(c\). The center itself is dominated because every blade contains selected vertices.

Two distinct peripheral vertices in the same blade are separated because at most one is omitted: if both are selected, their signatures differ by the two vertices themselves; if exactly one is selected, that selected vertex belongs to the omitted vertex’s signature but not to its own. Peripheral vertices in different blades are also separated. When \(c\notin S\), their nonempty signatures are contained in disjoint blades. When \(c\in S\), each peripheral signature contains \(c\) and at least one selected vertex from its own blade, so two different blades still yield different signatures. Finally, \(\sigma_S(c)\) contains selected vertices from every blade. If \(c\notin S\), this cannot equal a peripheral signature, which is contained in one blade; if \(c\in S\), the center signature does not contain \(c\) whereas every peripheral signature does. Thus the condition is sufficient.

For \(m\ge3\), each blade therefore independently contributes either all \(m\) of its vertices or exactly \(m-1\) vertices in \(m\) possible ways, while the center is optional. This gives
\[
(1+x)(x^m+m x^{m-1})^r.
\]
The minimum term is obtained by omitting the center and one vertex per blade, yielding size \(r(m-1)\) and multiplicity \(m^r\).

Now let \(m=2\). The preceding necessity still says at most one vertex can be omitted per blade. If \(c\notin S\) and a blade had only one selected vertex \(u\), then \(u\) would have empty signature because its only neighbors are \(c\) and its omitted mate. Hence every blade must be full. If \(c\in S\), a blade with exactly one selected vertex \(u\) gives \(\sigma_S(u)=\{c\}\); therefore at most one blade can be deficient. Conversely, the full-periphery set with \(c\) omitted is OLD, and with \(c\) selected either no peripheral vertex or any single peripheral vertex may be omitted: the signatures are then visibly nonempty and distinct by blade and mate. This gives \(2r+1\) sets of size \(2r\) and one set of size \(2r+1\), proving the boundary polynomial.

## Verification
The proof is symbolic and covers every \(r\ge2\), \(m\ge2\). An independent finite checker included with this package constructs each tested windmill, enumerates every vertex subset, evaluates the OLD definition directly from open-neighborhood signatures, compares that truth value with the stated characterization, and separately checks the polynomial coefficients and minimum-set count.

Replay command:

`python verify_old_windmills.py`

Expected output:

`VERIFY_OK parameter_pairs=10 subset_checks=22816 minimum_checks=10 max_order=13`

The finite computation is a consistency check, not the proof of the infinite theorem.

## Relationship to prior work
Seo and Slater introduced the OLD-set problem for general graphs. Chellali, Jafari Rad, Seo, and Slater later characterized several extremal values. In particular, their Theorem 3.3 states that among connected \(C_4\)-free graphs of minimum degree at least two, the graphs with OLD-number one below the order are \(C_5\) and \(K_1\vee tP_2\). Thus the friendship scalar \(\gamma^{OLD}(W_{r,2})=2r\) is already covered and is not a novelty claim.

Argiroffo, Bianchi, Lucarini, and Wagler studied OLD-numbers under graph operations such as adding a universal vertex, generalized coronas, and graph squares; their inspected paper does not state a generalized-windmill or friendship classification. Their universal-vertex theorem is formulated for a connected base graph, whereas deleting the center of \(W_{r,m}\) leaves \(rK_m\), which is disconnected for \(r\ge2\).

Generalized windmills are block graphs. The later block-graph work of Chakraborty, Foucaud, Parreau, and Wagler gives linear-time algorithms by reference and proves general bounds, including \(\gamma^{OLD}(G)\le |V(G)|-m_Q(G)-1\) for the relevant connected open-twin-free block graphs. In a generalized windmill every block is a leaf block, so \(m_Q(W_{r,m})=0\), and that theorem gives only \(\gamma^{OLD}(W_{r,m})\le rm\). It neither implies the exact \(r(m-1)\) value for \(m\ge3\) nor classifies or enumerates all OLD-sets. The inspected full text contains no occurrence of “windmill” or “friendship.”

## Limitations
The claim is restricted to the one-center clique windmills \(K_1\vee rK_m\); it does not classify OLD-sets of arbitrary block graphs or unequal-blade clique sums. General block-graph algorithms can compute minimum OLD-numbers instance by instance, so novelty here is attached to the closed all-set characterization and generating polynomial, not to mere computability. The friendship scalar is explicitly excluded from the originality claim. Literature searches can never establish absolute nonexistence of an equivalent unpublished or differently named result; the residual risk is mainly aliasing under “identifying open code” or an unindexed family-specific treatment.

## References
1. S. J. Seo and P. J. Slater, “Open neighborhood locating-dominating sets,” *Australasian Journal of Combinatorics* 46 (2010), 109–119.
2. M. Chellali, N. Jafari Rad, S. J. Seo, and P. J. Slater, “On open neighborhood locating-dominating in graphs,” *Electronic Journal of Graph Theory and Applications* 2(2) (2014), 87–98. DOI: 10.5614/ejgta.2014.2.2.1.
3. G. Argiroffo, S. Bianchi, Y. Lucarini, and A. Wagler, “The Identifying Code, the Locating-dominating, the Open Locating-dominating and the Locating Total-dominating Problems Under Some Graph Operations,” *Electronic Notes in Theoretical Computer Science* 346 (2019), 135–145. DOI: 10.1016/j.entcs.2019.08.013.
4. D. Chakraborty, F. Foucaud, A. Parreau, and A. K. Wagler, “On Three Domination-based Identification Problems in Block Graphs,” *Fundamenta Informaticae* 191(3–4) (2024), 197–229. arXiv:1811.09537.

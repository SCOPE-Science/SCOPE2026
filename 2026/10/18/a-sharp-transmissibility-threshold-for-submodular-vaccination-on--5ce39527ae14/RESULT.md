# A sharp transmissibility threshold for submodular vaccination on every cycle

## Finding
Fix an integer \(n\ge3\), and a root \(0\) on the undirected simple cycle \(C_n\), whose other vertices are \(1,\ldots,n-1\) in cyclic order. All edges independently transmit with probability \(0<p<1\). Before transmission, the nonroot vertices in a chosen set \(S\) receive perfect vaccines and are deleted. Define \(I(S)\) as the number of vertices connected to the root in the random subgraph of retained vertices and transmitting edges (including the root), and let
\[
B(S)=\mathbb E[I(\varnothing)]-\mathbb E[I(S)].
\]
Then \(B\) is monotone, and **it is submodular on every subset of nonroot vertices if and only if**
\[
\boxed{p\le\frac{2}{n-1}.}
\]
For \(1\le i<j\le n-1\), put \(A=i\), \(C=n-j\), and \(b=j-i\). The exact two-vaccine interaction at empty background is
\[
\Delta_{i,j}(p):=B(\{i,j\})-B(\{i\})-B(\{j\})+B(\varnothing)
=(n-1)p^n-\sum_{k=n-i}^{n-1}p^k-\sum_{k=j}^{n-1}p^k.
\]
Every such interaction obeys
\[
\Delta_{i,j}(p)\le p^{n-1}((n-1)p-2),
\]
with equality only for \(i=1\) and \(j=n-1\). When \(b=1\), \(\Delta_{i,j}(p)<0\) for all \(p\in(0,1)\); when \(b\ge2\), it has exactly one zero \(p_{i,j}\in(0,1)\), changing from negative to positive there. After any nonempty existing vaccine set, all second differences are nonpositive. On every finite rooted tree, and more generally on a rooted forest, vaccination benefit is a monotone weighted coverage function for arbitrary independent heterogeneous edge probabilities. In particular, four vertices are the smallest simple-graph order capable of non-submodularity: on \(C_4\) the interaction of the two root neighbors is \(p^3(3p-2)\), positive exactly when \(p>2/3\).

## Assumptions and scope
The outbreak is a one-source Reed–Frost/live-edge epidemic with independent undirected edges; deleting a vaccinated vertex prevents infection in that vertex and blocks transmission through it. Exactly one fixed root is initially infected, is never vaccinated, and every surviving vertex is counted at most once. An equivalent experiment first independently samples all open edges, then deletes vaccinated vertices; the final infected set is the connected component of the root. Probabilities are homogeneous on the cycle and may differ on the forest. The statement covers every vaccine set including the empty and full nonroot set. All inequalities are exact in \(0<p<1\); no independence among overlapping infection-path events is assumed.

For a set function on the eligible vertex set, submodularity means that for every background \(S\) and two distinct vertices \(u,v\notin S\), the discrete second difference
\[
B(S\cup\{u,v\})-B(S\cup\{u\})-B(S\cup\{v\})+B(S)
\]
is nonpositive. This criterion is equivalent to diminishing marginal returns, including when \(S\) is empty.

## Proof
**1. Tree and forest lemma.** For each nonroot vertex \(v\) connected to the root in the original forest, let \(P_v\) be the unique vertex-path from the root to \(v\), and let \(w_v\) be the product of its edge transmission probabilities. The event that \(v\) becomes infected after vaccinating \(S\) is precisely that all edges of \(P_v\) transmit and that \(S\cap(P_v\setminus\{0\})=\varnothing\). Therefore
\[
B(S)=\sum_{v\ne0} w_v\,\mathbf1\{S\cap(P_v\setminus\{0\})\ne\varnothing\}.
\]
This is a nonnegative linear combination of coverage indicators. Each indicator is monotone submodular: adding \(u\) can change it only from zero to one, and only when no earlier chosen vertex lies on the path. Thus \(B\) is monotone submodular. Vertices originally disconnected from the root have weight zero.

**2. Expected infection counts on the cycle.** With no vaccinated vertex, each \(k\in\{1,\ldots,n-1\}\) has two edge-disjoint root paths of lengths \(k\) and \(n-k\), so inclusion–exclusion gives infection probability \(p^k+p^{n-k}-p^n\). Consequently,
\[
\mathbb E[I(\varnothing)]=1+2\sum_{k=1}^{n-1}p^k-(n-1)p^n.
\]
If only vertex \(i\) is vaccinated, the remaining graph is a path and the root has two arms with lengths \(i-1\) and \(n-i-1\), giving
\[
\mathbb E[I(\{i\})]=1+\sum_{k=1}^{i-1}p^k+\sum_{k=1}^{n-i-1}p^k.
\]
If \(i<j\) are both vaccinated, only the two arms at the root can be infected, so
\[
\mathbb E[I(\{i,j\})]=1+\sum_{k=1}^{i-1}p^k+\sum_{k=1}^{n-j-1}p^k.
\]
Substituting these three identities in the definition of \(\Delta_{i,j}\), with \(\Delta=B(\{i,j\})-B(\{i\})-B(\{j\})+B(\varnothing)\), yields the asserted exact formula. This is an algebraic identity, with sums over empty ranges understood as zero.

**3. Empty-background phase boundary.** Since \(i\ge1\) and \(n-j\ge1\), both negative sums in \(\Delta_{i,j}\) contain at least \(p^{n-1}\). Thus
\[
\Delta_{i,j}(p)\le(n-1)p^n-2p^{n-1}=p^{n-1}((n-1)p-2).
\]
For \(0<p<1\), strictness holds unless \(i=n-j=1\). Therefore all empty-background second differences are nonpositive if \(p\le2/(n-1)\). For \(n\ge4\) and \(p>2/(n-1)\), choosing \(i=1\) and \(j=n-1\) makes the second difference positive. For \(n=3\), the threshold equals one and the permitted interval is entirely submodular.

For pair-specific behavior, division by positive \(p^n\) gives
\[
\frac{\Delta_{i,j}(p)}{p^n}=n-1-\sum_{h=1}^{i}p^{-h}-\sum_{h=1}^{n-j}p^{-h}.
\]
The right side is strictly increasing on \((0,1)\), tends to \(-\infty\) as \(p\downarrow0\), and tends to \(j-i-1=b-1\) as \(p\uparrow1\). It is therefore strictly negative for adjacent \(i,j\), and for each separation \(b\ge2\) it crosses zero exactly once by continuity.

**4. All nonempty backgrounds.** Fix a nonempty vaccine set \(S\) excluding \(0\). The remaining graph \(C_n\setminus S\) is a forest. For any additional eligible vaccine set \(T\), the marginal prevented infections \(B(S\cup T)-B(S)\) equal the reduction in root-connected infection count between that forest and its deletion by \(T\). The forest lemma proves this marginal-benefit function of \(T\) is submodular; therefore every second difference of \(B\) based at nonempty \(S\) is nonpositive. Together with step 3, this proves the if-and-only-if theorem.

**5. Minimum network order.** Every simple contact graph on at most three vertices is a forest or a triangle (possibly disconnected). In a forest apply step 1; for a triangle apply the \(n=3\) result; components not containing the root are irrelevant. On \(C_4\), the two neighbors \(1\) and \(3\) give \(\Delta_{1,3}=p^3(3p-2)>0\) whenever \(p>2/3\). Thus four is the sharp minimum order of a simple undirected counterexample.

## Verification
The accompanying standalone `verify.py` independently enumerates all edge-open states and all vaccine subsets for cycles of orders \(3\) through \(8\), at four rational transmission probabilities, checking every two-vaccine interaction exactly using integers and comparing with the closed polynomial. For every nonempty vaccine background it checks submodularity. Separately, it constructs all \(1,441\) Prüfer-coded labeled rooted trees on orders \(2\) through \(6\), and independently compares all vaccine-set infection counts with the path-coverage expression at rational transmission probability \(2/5\). Run `python3 verify.py`. These finite checks test the algebra and boundary cases; the unrestricted claims follow from the five analytic steps above.

## Relationship to prior work
Altarelli et al. (2013/2014) formulate network immunization in SIR-type processes and develop message-passing optimization, not an exact cycle-wide characterization of submodularity. Holme (2017) evaluates exact outbreak and vaccination importance for small graphs, focusing on optimal set rankings and averaged initial sources, not all subsets' diminishing returns on arbitrary-length cycles. Li et al. (2023) prove a tree-network monotone-submodular reward under delayed immunization: the tree conclusion here is compatible with their result, while the sharp cycle phase boundary concerns a different graph family and immediate vaccine effect. Srivastava and Teng (2024, withdrawn 2026 because of a proof flaw) explicitly discuss general failure of submodularity; neither that broad observation nor any withdrawn approximation conclusion is presented as new or used in this proof. The mathematical contribution asserted here is the exact if-and-only-if cycle threshold, all-pair phase classification, and its smallest simple-graph witness.

## Limitations
The theorem assumes one fixed root, independent homogeneous edge transmissibilities on an undirected cycle, perfect pre-outbreak vaccines, and infection counted through live-edge reachability. It does not establish the same threshold for a random initial source, directed edges, temporal dynamics, vaccination delays, graph families with multiple independent cycles, or correlated transmission. Its general novelty against all graph reliability literature has not been independently certified. The withdrawn 2024 paper is cited only as evidence that general non-submodularity has been discussed, not as an accepted proof of any approximation bound.

## References
1. F. Altarelli, A. Braunstein, L. Dall'Asta, J. R. Wakeling, and R. Zecchina, *Containing epidemic outbreaks by message-passing techniques*, arXiv:1309.2805 (first public 2013-09-11); Physical Review X **4**, 021024 (2014). https://arxiv.org/abs/1309.2805
2. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, Physical Review E **96**, 062305 (2017). https://doi.org/10.1103/PhysRevE.96.062305
3. S. Li, X. Huang, C.-H. Lee, and D. Y. Eun, *Controlling epidemic spread under immunization delay constraints*, IFIP Networking (2023), arXiv:2307.06889. https://arxiv.org/abs/2307.06889
4. A. Srivastava and S.-H. Teng, *Overcoming Non-Submodularity: Towards Constant Approximation for Network Immunization*, arXiv:2410.19205 (submitted 2024; withdrawn in 2026, authors reporting a flaw in an approximation proof). https://arxiv.org/abs/2410.19205

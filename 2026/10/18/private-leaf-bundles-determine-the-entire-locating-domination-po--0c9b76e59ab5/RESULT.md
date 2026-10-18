# Private-leaf bundles determine the entire locating-domination polynomial and the exact domination–location partitions

## Finding
Let \(H\) be any finite simple graph on an indexed vertex set \(\{v_1,\ldots,v_n\}\) with \(n\ge1\). For arbitrary integers \(k_i\ge1\), attach to \(v_i\) a set \(L_i\) of \(k_i\) new degree-one vertices, each adjacent only to \(v_i\). Write \(G\) for the resulting graph, \(K=\sum_i k_i\), and \(s=|\{i:k_i=1\}|\). The graph \(H\) may be disconnected or edgeless.

A locating-dominating (LD) set \(X\) dominates every vertex outside \(X\) and assigns distinct nonempty sets \(N_G(u)\cap X\) to all distinct vertices \(u\notin X\). Let \(\mathcal L_G(z)=\sum_{X\text{ LD}}z^{|X|}\) denote the location-domination polynomial.

**Complete LD characterization.** A set \(X\subseteq V(G)\) is locating-dominating if and only if, independently for every \(i\), it has exactly one of these local forms:

* \(L_i\subseteq X\), with \(v_i\) either in or out of \(X\); or
* \(v_i\in X\) and \(X\cap L_i=L_i\setminus\{\ell\}\), for a unique chosen \(\ell\in L_i\).

It follows that
\[
\boxed{\mathcal L_G(z)=z^K\prod_{i=1}^{n}(k_i+1+z).}
\]
In particular, \(\gamma_{LD}(G)=K\), and exactly \(\prod_i(k_i+1)\) LD sets have minimum cardinality. The polynomial is independent of every edge of \(H\) and has only real nonpositive zeros.

**Exact complementary partitions.** Consider *ordered* bipartitions \(V(G)=D\sqcup X\), where \(D\) is dominating and \(X\) is locating-dominating (a DLDS-partition). These are precisely the \(2^s\) selections satisfying the following independent rules:

* If \(k_i\ge2\), then \(v_i\in D\) and \(L_i\subseteq X\).
* If \(k_i=1\), exactly one of \(v_i\), its private leaf, lies in \(D\), and the other lies in \(X\).

Every such partition satisfies \(|D|=n\), \(|X|=K\) and
\[\boxed{\gamma(G)+\gamma_{LD}(G)=|V(G)|=n+K.}\]
Indeed, the \(D\)-parts are exactly the minimum dominating sets of \(G\), of which there are \(2^s\).

Finally, \(G\) admits a bipartition into **two locating-dominating sets** if and only if \(k_i=1\) for every \(i\). In this case there are exactly \(2^n\) ordered such bipartitions and \(2^{n-1}\) unordered ones.

## Assumptions and scope
All graphs are finite, simple, undirected, and vertex-labelled when counting distinct sets. No connectedness or structural restriction is imposed on the core \(H\). For each core vertex, at least one independent private leaf is required, and leaves have no edges except the prescribed single incident edge. The domination convention for a set \(S\) is that every vertex outside \(S\) has a neighbor in \(S\). Location distinguishes **only vertices outside the code**, by their open neighborhoods intersected with the code. The empty core is excluded by \(n\ge1\); singleton bundles and singleton cores are included.

## Proof
**1. Necessary local conditions.** Fix \(i\). Distinct leaves \(a,b\in L_i\) have identical open neighborhood \(\{v_i\}\). If both were outside an LD set \(X\), they would have identical traces on \(X\), violating location. Thus at least \(k_i-1\) leaves of \(L_i\) belong to \(X\). If precisely one leaf \(\ell\) is outside \(X\), domination of that leaf forces \(v_i\in X\). If no leaf is outside \(X\), the status of \(v_i\) is unrestricted. These are the stated local forms.

**2. Sufficiency and global independence.** Suppose the local forms hold at every \(i\). Every omitted leaf \(\ell\in L_i\setminus X\) has the nonempty trace \(N_G(\ell)\cap X=\{v_i\}\). The omitted center \(v_j\), if any, has \(L_j\subseteq N_G(v_j)\cap X\), since the local rule requires \(L_j\subseteq X\) whenever \(v_j\notin X\). Hence all omitted centers have nonempty traces, and traces of centers from distinct bundles differ because one contains \(L_i\) and the other contains \(L_j\). No omitted-center trace is a singleton core vertex, since it contains a private leaf; omitted-leaf traces are pairwise distinct singleton core vertices. Therefore the set \(X\) dominates and locates every vertex outside it, regardless of edges of \(H\).

**3. Polynomial and minimum sets.** In the first local form with \(v_i\notin X\), there is one choice of weight \(z^{k_i}\). In the first with \(v_i\in X\), there is one choice of weight \(z^{k_i+1}\). In the second form there are \(k_i\) choices of the omitted leaf, each of weight \(z^{k_i}\). Thus the independent local generating factor is \(z^{k_i}(k_i+1+z)\). Their product is \(\mathcal L_G(z)\). Its smallest exponent \(K\) has coefficient \(\prod_i(k_i+1)\). The factorization gives the zeros at \(z=0\) and \(z=-(k_i+1)\) with multiplicities. In particular all nonzero coefficients form a log-concave sequence.

**4. Characterization of DLDS partitions.** Set \(D=V(G)\setminus X\) for an LD set \(X\). If a leaf \(\ell\in L_i\) is in \(X\), the only possible neighbor of \(\ell\) in \(D\) is \(v_i\); therefore domination by \(D\) forces \(v_i\in D\). For \(k_i\ge2\), every LD-local form has at least one leaf in \(X\), so \(v_i\in D\); the LD-local forms then force all of \(L_i\) into \(X\). For \(k_i=1\), the only possibilities are to choose either the center in \(D\) and the leaf in \(X\), or the leaf in \(D\) and the center in \(X\). Conversely, in each stated configuration, every vertex of \(X\) has a neighbor in \(D\): either its center or its private leaf. The LD proof above applies to \(X\), and there are \(2^s\) such independent choices.

**5. Optimality and two-code partitions.** Every dominating set must meet each disjoint closed leaf bundle \(B_i=\{v_i\}\cup L_i\): otherwise none of its leaves is dominated. Thus \(\gamma(G)\ge n\). The entire core \(V(H)\) dominates \(G\), so equality holds. A dominating set of size \(n\) meets every \(B_i\) in exactly one vertex. For \(k_i\ge2\), that vertex must be \(v_i\); for \(k_i=1\) it can be either endpoint. This is precisely the family of \(D\)-parts classified above.

If some \(k_i\ge2\), every DLDS-partition has \(v_i\in D\) and all \(k_i\) leaves in \(X\). Those leaves are two or more vertices outside \(D\) with identical \(D\)-traces \(\{v_i\}\), so \(D\) cannot be LD. Conversely if every \(k_i=1\), every choice of one endpoint per private edge as \(D\) leaves the opposite endpoint in \(X\). The local LD characterization applies to **both** parts. There are \(2^n\) ordered choices, and complement interchanges pair them without fixed points, giving \(2^{n-1}\) unordered bipartitions. This proves every assertion.

## Verification
The included `verify.py` implements adjacency matrices as vertex-neighborhood bitmasks and independently enumerates every vertex subset. It compares the full LD polynomial coefficient-by-coefficient, the number of DLDS partitions, the number of two-LD partitions, and the domination number with the formulas above. Testing covers all labelled core graphs on up to four vertices with local sizes in \(\{1,2\}\), as well as all core graphs on up to three vertices with local sizes in \(\{1,2,3\}\). The completed run reports `VERIFY_OK graphs=1335 vertex_subsets=1518440 full_LD_polynomial=pass DLDS_partition_count=pass two_LD_partition_count=pass domination_number=pass`. The proof is for arbitrary \(n\), \(H\), and positive bundle sizes; finite enumeration does not establish the unrestricted claim.

## Relationship to prior work
Chakraborty, Foucaud, Henning, and Laihonen prove that every isolate-free graph admits a DLDS partition and give the bound \(\gamma(G)+\gamma_{LD}(G)\le |V(G)|\). Their 2026 article explicitly gives the one-leaf corona as an equality example but does not enumerate its DLDS partitions or the complete LD polynomial. The present theorem classifies and counts every DLDS partition and extends the equality class to arbitrary nonuniform bundles of independent leaves.

Canoy, Malacas, and Tarepe (2014, Theorem 3.1) give an all-set characterization for corona products whose two factors are nontrivial **connected** graphs. A bundle of two or more independent leaves is disconnected, while a one-leaf bundle is trivial, so those hypotheses do not cover the family here; their theorem also gives no heterogeneous-bundle polynomial or DLDS count. González Yero, Kuziak, and Rondón Aguilar study minimum locating-domination parameters of ordinary corona products. Their relevant section treats parameter values and bounds; it does not give the full LD polynomial or the complementary-partition count for nonuniform independent pendant bundles. Fazil, Hussain, Akbar, and Ali introduce the location-domination polynomial and evaluate other graph families, but do not provide the present leaf-bundle formula. Previously known twin-set arguments explain part of the lower-bound mechanism; the full local sufficiency, polynomial, and two kinds of partition enumeration are established here. The graph families overlap only at ordinary uniform coronas; a theorem for all such coronas does not by itself count all valid codes or partitions.

## Limitations
Private leaves must have degree exactly one and form independent bundles; adding other edges incident to them can destroy the local classification. The result is an exact theorem for this graph construction, not a classification of arbitrary isolate-free graphs. It does not establish bibliographic priority against inaccessible or unindexed literature, and the computations are finite consistency checks rather than independent validation of the unrestricted proof.

## References
1. D. Chakraborty, F. Foucaud, M. A. Henning, T. Laihonen, *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*, Electronic Journal of Combinatorics 33(1), P1.51 (published March 13, 2026), DOI:10.37236/14049; arXiv:2610.03131 (subsequent posting).
2. I. González Yero, D. Kuziak, A. Rondón Aguilar, *Coloring, location and domination of corona graphs*, arXiv:1204.0647 (first submitted April 3, 2012), especially section 4.
3. M. Fazil, I. F. Hussain, A. Akbar, U. Ali, *On some variations of dominating identification in graphs*, Kuwait Journal of Science 49(4) (2022), DOI:10.48129/kjs.13175, sections 2–3.
4. S. R. Canoy Jr., G. A. Malacas, D. Tarepe, *Locating-Dominating Sets in Graphs*, Applied Mathematical Sciences 8 (2014), 4381–4388, DOI:10.12988/ams.2014.46400, Theorem 3.1.
5. F. Foucaud, P. V. Maniya, K. Paul, D. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933 (2025), contextual comparison.

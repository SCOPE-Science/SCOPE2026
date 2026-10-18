# Sharp edge-addition slowdowns in three finite voter-consensus rules

## Finding

Let \(T_R(G)\) denote the expectation, over independent uniformly fair binary initial opinions and the updating randomness, of the number of attempted single updates before all opinions agree in a finite connected undirected simple graph \(G\), for each of the three rules \(R\in\{\mathrm{VM},\mathrm{LD},\mathrm{IP}\}\) defined below. All self-loops in the opinion-configuration Markov chain count as elapsed updates.

**Sharp network-size boundary.** For a connected graph \(G\) and a pair \(e\) of nonadjacent vertices, the first possible strict inequality \(T_R(G+e)>T_R(G)\), over all such \(G\), occurs at \(\lvert V(G)\rvert=4\) for node-copy/voter updating (VM), at \(4\) for invasion updating (IP), and at \(5\) for link updating (LD). At size four, exactly \(2\) of the \(6\) unlabelled distinguished-edge addition types are slowdowns for VM; precisely \(1\) is a slowdown for IP; and all \(6\) **strictly accelerate** LD.

In particular, using \(S_4\) for the four-vertex star and *paw* for the graph obtained by joining two of its leaves, the VM slowdown is \(T_{\mathrm{VM}}(\text{paw})-T_{\mathrm{VM}}(S_4)=155/208>0\); the identical added edge accelerates LD by \(1/17\) update attempts. Under IP, adding a diagonal to \(C_4\) increases the mean by \(35/88\). For LD the first slowdown is witnessed by the five-vertex star \(S_5\) with an edge added between two leaves: \(T_{\mathrm{LD}}(S_5+e)-T_{\mathrm{LD}}(S_5)=32327/78888>0\).

## Assumptions and scope

All graphs are finite, connected, undirected, simple, and labelled for the exhaustive calculation, with relabelling used only to identify equivalent graph-plus-new-edge cases. At each vertex the opinion is either zero or one. Initially, the opinions are independent Bernoulli variables with success probability \(1/2\); in particular the all-zero and all-one initial states contribute zero to the unconditional mean.

Each attempt is exactly one of the following random operations, always consuming one unit even if it changes no opinion:

* **VM:** choose a vertex uniformly, choose one of its neighbours uniformly, and copy the neighbour's opinion into the chosen vertex.
* **IP:** choose a vertex uniformly, choose one of its neighbours uniformly, and copy the chosen vertex's opinion into that neighbour.
* **LD:** choose an undirected edge uniformly, then choose one endpoint with probability \(1/2\) to copy the other endpoint's opinion.

For graph order \(n\), degrees \(d_i\), and size \(m\), the transition probability associated with copying opinion from \(j\) to \(i\) along an oriented edge is respectively \(1/(nd_i)\) for VM, \(1/(nd_j)\) for IP, and \(1/(2m)\) for LD. These probabilities include attempted copies between equal opinions. The primary classification is MSC2020 91D30 (social networks and opinion dynamics).

## Proof

**Exact Markov identity.** Index the \(2^n-2\) nonconstant configurations by bit vectors \(\sigma\in\{0,1\}^n\), and let \(Q_R(G)\) be the substochastic transition matrix restricted to those configurations. For each transient configuration, the first-step equation is \(t_\sigma=1+\sum_\tau Q_{\sigma\tau}t_\tau\). Because \(G\) is finite and connected, from each nonconstant state there is a positive-probability finite sequence of permitted opinion copies leading to consensus; the two monochromatic configurations are absorbing. Thus transient states are transient in the Markov-chain sense, \(I-Q_R(G)\) is invertible, and
\[
T_R(G)=2^{-n}\boldsymbol 1^{\mathsf T}(I-Q_R(G))^{-1}\boldsymbol 1.
\]
This identity is evaluated over the rational field, including every unchanged-opinion event.

**Exhaustion through four vertices.** At order two there is no nonedge of a connected graph. At order three the sole pair orbit is the two-edge path becoming a triangle; the respective differences \(T_R(G+e)-T_R(G)\) for VM, LD, IP are \(0,-1/2,-3/2\). At order four every connected graph with an available missing edge is a star, a path, a paw, a four-cycle, or a diamond. The exhaustive graph-with-marked-nonedge classification has exactly six orbits. Write \(P_4\) for the four-vertex path, \(C_4\) for the four-cycle, and \(K_4\) for the clique; a diamond is \(K_4\) with one edge removed. The following rational table gives **after minus before**, counting update attempts, and exhausts all six pair types:

| Edge insertion | VM | LD | IP |
|:--|--:|--:|--:|
| \(S_4\to\text{paw}\) | \(155/208\) | \(-1/17\) | \(-681/152\) |
| \(P_4\to\text{paw}\) | \(-1567/1456\) | \(-235/238\) | \(-415/152\) |
| \(P_4\to C_4\) | \(-4/7\) | \(-27/14\) | \(-6\) |
| \(\text{paw}\to\text{diamond}\) | \(35/1872\) | \(-499/476\) | \(-2401/836\) |
| \(C_4\to\text{diamond}\) | \(-35/72\) | \(-3/28\) | \(35/88\) |
| \(\text{diamond}\to K_4\) | \(-1/72\) | \(-11/28\) | \(-79/88\) |

The exact transient linear-system solutions that generate the table are reproducible with the accompanying `verify_exact.py`. That program independently constructs the source configurations, transition probabilities, and complete graph/marked-nonedge orbits by enumerating all labelled edge subsets of \(K_4\) and canonicalizing under all vertex permutations; it asserts that the six listed pairs match the entire set. The numbers are rational equalities, not numerical approximations or sampling estimates. The table proves both positive-update-rule cutoffs at four and excludes any LD slowdown through four.

**Five-vertex LD witness.** With vertex set \(\{0,1,2,3,4\}\), take \(S_5\) with edges \(\{01,02,03,04\}\), where \(ij\) denotes the edge joining vertices \(i\) and \(j\), and add \(e=\{1,2\}\). Exact solution of the \(30\)-state transient LD equations yields
\[
T_{\mathrm{LD}}(S_5)=\frac{613}{48},\qquad
T_{\mathrm{LD}}(S_5+e)=\frac{693195}{52592},\qquad
T_{\mathrm{LD}}(S_5+e)-T_{\mathrm{LD}}(S_5)=\frac{32327}{78888}>0.
\]
Together with the complete smaller-order exclusion, this proves the sharp LD cutoff at five, without asserting any unexamined classification of all five-vertex insertions.

## Verification

Run `python3 verify_exact.py` using standard Python 3. It solves the rational first-step equations using exact `fractions.Fraction` Gaussian elimination, checks all six four-vertex marked-edge orbits, checks the three-vertex sole orbit and two-vertex empty set, verifies the signs and counts for all rules, and reproduces the five-vertex LD fractions. No stochastic simulations, approximate eigenvalues, external tables, network access or third-party dependencies are required. The underlying four-vertex means for star, path, paw, cycle, diamond and clique are printed by the checker. A separately constructed symbolic exact matrix implementation agreed with the entries, but no claim of independent external audit is made.

## Relationship to prior work

Sood, Antal and Redner (2008) define and compare the VM, IP and LD updating mechanisms and show the relevance of degree heterogeneity. Iwamasa and Masuda (2014), particularly their Section III and four-vertex paw illustration, solve finite-state voter-consensus equations and compare networks that maximize consensus time by the three rules, while using balanced rather than i.i.d. fair initial opinions and measuring each update as \(1/n\) time. Their graph-optimization and asymptotic results do not state the exact local single-edge insertion cutoff or its complete first-layer rule-specific signs established here. Masuda (2014) analyzes community-bridge density in a two-clique family under link dynamics; that family-level question does not imply the arbitrary-graph minimal boundary. Cooper, Dyer, Frieze and Rivera (2016) analyze discordant-only voting, where an update is conditioned on a disagreement; those clocks and transition kernels differ from those studied here.

A search of alternative descriptions (voter absorption, edge augmentation, Braess-type slowing, copying/invasion/link updates) and relevant literature did not identify a statement subsuming this three-rule minimum-order classification. This is a best-knowledge comparison, not a proof of universal absence from all literature.

## Limitations

The theorem concerns expected **attempted-update count** under **i.i.d. fair initial configurations** and exactly the stated three update protocols. Conditioning on a balanced configuration, measuring only opinion changes, or changing continuous-time rate normalizations gives a different observable; those variants are not claimed. The classification is complete for up to four vertices only; the five-vertex LD portion proves existence of one witness, not a full census or an infinite-family phenomenon. Published work already provides the Markov-equation method and broad edge-density effects, so novelty is restricted to the exact small-order and cross-rule boundary, rather than to a new voter process or general nonmonotonicity principle.

## References

1. V. Sood, T. Antal and S. Redner, *Voter Models on Heterogeneous Networks*, Physical Review E 77 (2008), 041121, arXiv:0712.4288. https://arxiv.org/abs/0712.4288
2. Y. Iwamasa and N. Masuda, *Networks maximizing the consensus time of voter models*, Physical Review E 90 (2014), 012816, arXiv:1404.6360; publicly posted April 25, 2014. https://arxiv.org/abs/1404.6360
3. N. Masuda, *Voter model on the two-clique graph*, Physical Review E 90 (2014), 012802, arXiv:1403.4763. https://arxiv.org/abs/1403.4763
4. C. Cooper, M. Dyer, A. Frieze and N. Rivera, *Discordant voting processes on finite graphs*, arXiv:1604.06884 (initially posted 2016). https://arxiv.org/abs/1604.06884

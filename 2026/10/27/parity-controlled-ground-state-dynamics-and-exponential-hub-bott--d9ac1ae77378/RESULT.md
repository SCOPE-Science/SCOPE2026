# Parity-controlled ground-state dynamics and exponential hub bottlenecks on clique windmills

## Finding

Let \(G_{s,r}=K_1\vee(rK_s)\) be the graph formed by gluing \(r\) complete graphs of order \(s+1\) at a single hub, with integers \(s,r\ge1\). At each discrete time choose one of its \(N=rs+1\) vertices uniformly, and update its binary spin to the *minority* of its closed neighbourhood (retain the spin in a tie). Let \(\mathcal A\) be the union of recurrent communicating classes. Then **\(\mathcal A\) is exactly the set of maximum-cut spin configurations**. More precisely, fix the hub spin \(h\), and let \(k_j\) count spins different from \(h\) in peripheral clique \(j\).

**Odd \(s=2\ell+1\), \(\ell\ge0\):** a configuration belongs to \(\mathcal A\) exactly when \(k_j=\ell+1\) for every \(j\). Each such configuration is absorbing. Hence there are exactly
\[
2\binom{2\ell+1}{\ell+1}^{r}
\]
recurrent singleton classes.

**Even \(s=2\ell\), \(\ell\ge1\):** a configuration belongs to \(\mathcal A\) exactly when \(k_j\in\{\ell,\ell+1\}\) for every \(j\). All these configurations form **one** irreducible, aperiodic recurrent class of cardinality
\[
2\left[\binom{2\ell}{\ell}+\binom{2\ell}{\ell+1}\right]^r.
\]
Its stationary distribution is uniform, and the total-variation mixing time of the chain restricted to \(\mathcal A\) obeys
\[
t_{\mathrm{mix}}(1/4)\ \ge\ \left\lceil\frac{2\ell r+1}{4}\left(\frac{2\ell+1}{\ell+1}\right)^r\right\rceil.
\]
The factor exponential in \(r\) arises from the need to balance *every* peripheral clique simultaneously before the hub can change state.

Despite that exponential internal mixing obstruction, entrance into \(\mathcal A\) is fast for either parity. If \(T=\inf\{t\ge0:X_t\in\mathcal A\}\), then for every initial spin configuration
\[
\mathbb E[T]\le\frac{(rs+1)rs(s+1)}{2\delta_s},\qquad
\delta_s=\begin{cases}1&\text{if }s\text{ is odd},\\2&\text{if }s\text{ is even}.\end{cases}
\]
All statements hold for labelled vertices, all \(s,r\ge1\), and the stated tie convention.

## Assumptions and scope

A clique windmill has one distinguished hub \(v_0\), and disjoint labelled peripheral blocks \(V_1,\ldots,V_r\) of size \(s\). Each set \(\{v_0\}\cup V_j\) induces a complete graph, and there are no edges between distinct peripheral blocks. An update chooses one vertex uniformly from all \(N=rs+1\) vertices, including vertices that would not change. For a selected vertex, the minority is computed including the selected vertex itself. With binary spins \(0,1\), it flips exactly if its closed-neighbourhood count of its current spin strictly exceeds that of the other spin; exact ties retain the current spin. All time and mixing estimates count attempted single-vertex selections.

For a finite Markov chain, \(\mathcal A\) denotes the union of its closed irreducible communicating classes. The full chain can have transient states; mixing time above is defined for its unique irreducible restriction to \(\mathcal A\) when \(s\) is even. Mixing time is the least integer \(t\) at which the worst-case total-variation distance to stationarity does not exceed \(1/4\).

## Proof

**1. Local energy descent.** Let \(M(c)\) be the number of monochromatic (same-spin) undirected edges. If a vertex of degree \(d\), having \(u\) neighbours sharing its current spin, flips, then
\[
M(c')-M(c)=d-2u.
\]
By the closed-neighbourhood minority rule, it flips precisely when \(2(u+1)>d+1\), equivalently \(u\ge\lceil d/2\rceil\). Thus \(M\) never increases. A peripheral vertex has degree \(s\). For hub spin \(h\) and \(k_j\) opposite spins in block \(j\), a peripheral spin equal to \(h\) has \(s-k_j\) equal-spin neighbours, while an opposite spin has \(k_j-1\) equal-spin neighbours.

**2. Odd peripheral size.** Put \(s=2\ell+1\). A peripheral spin equal to \(h\) flips exactly when \(k_j\le\ell\); an opposite spin flips exactly when \(k_j\ge\ell+2\). Each such flip strictly decreases \(M\), by at least one. Therefore all peripheral vertices are inactive if and only if \(k_j=\ell+1\) in every block. In that case the hub has exactly \(r\ell\) equal-spin neighbours, whereas its degree is \(r(2\ell+1)\); the hub is inactive as well. Such states are absorbing.

Every state outside this set has a peripheral update that strictly decreases \(M\), so none lies in a closed communicating class. Since the graph is finite and the displayed states are absorbing, these states are precisely \(\mathcal A\). Each block has \(\binom{2\ell+1}{\ell+1}\) opposite-spin choices once \(h\) is fixed, giving the claimed singleton-class census.

**3. Even peripheral size.** Put \(s=2\ell\). Outside the interval \(k_j\in\{\ell,\ell+1\}\), a peripheral vertex is available for a strictly energy-decreasing flip: if \(k_j<\ell\), flip a spin equal to \(h\), increasing \(k_j\); if \(k_j>\ell+1\), flip a spin opposite to \(h\), decreasing \(k_j\). The energy drops by at least two. In the interval, only zero-energy peripheral flips occur. For \(k_j=\ell\), a spin equal to \(h\) may flip, producing \(k_j=\ell+1\); for \(k_j=\ell+1\), an opposite spin may flip, producing \(k_j=\ell\). Both moves are reversible.

The hub has degree \(2\ell r\), and has \(\sum_j(2\ell-k_j)\) equal-spin neighbours. On the displayed interval this is at most \(\ell r\), with equality exactly when **all** \(k_j=\ell\). Therefore the hub is inactive unless all blocks have exactly \(\ell\) opposite spins, when it can flip at zero energy. This hub flip exchanges the two hub colours and leaves every block at \(k_j=\ell\). Consequently the entire displayed set \(\mathcal B\) is closed.

For fixed hub colour, the permitted peripheral transitions in one block form the inclusion graph joining \(\ell\)-element and \((\ell+1)\)-element subsets of a \(2\ell\)-set. This graph is connected: two \(\ell\)-subsets are related by single-element exchanges, each realized via an intermediate \((\ell+1)\)-subset; every larger subset is adjacent to a smaller one. Taking products shows that each hub-colour sector of \(\mathcal B\) is connected. An all-\(\ell\) configuration supplies a hub-flip edge between the sectors. Thus \(\mathcal B\) is one irreducible communicating class. Every allowed transition is reversible with the same probability \(1/N\), so uniform measure is stationary. There are self-loops (for example, the hub is inactive whenever one block has \(k_j=\ell+1\)), making the chain aperiodic. An outside state always has a strictly decreasing peripheral move and therefore cannot be recurrent. Hence \(\mathcal A=\mathcal B\), with the stated cardinality.

**4. Maximum cuts and entrance-time bound.** The \(r\) complete graphs of order \(s+1\) share vertices but have disjoint edge sets. In each, the number of monochromatic edges is minimized precisely when its two colour classes differ in size by at most one. For odd \(s\), this condition is exactly \(k_j=\ell+1\); for even \(s\), it is exactly \(k_j\in\{\ell,\ell+1\}\). Thus the identified recurrent configurations are **all** global ground states (maximum cuts), not just local-energy traps.

Outside \(\mathcal A\), at least one peripheral vertex has a strictly decreasing move. Since that vertex is selected with probability \(1/N\), the conditional drift of nonnegative \(M\) is at most \(-\delta_s/N\), with \(\delta_s=1\) for odd \(s\) and \(2\) for even \(s\). Stopping this drift at \(T\), then taking expectations and monotone limits, yields \(\mathbb E[T]\le N M(c_0)/\delta_s\). The total number of edges is \(r\binom{s+1}{2}=rs(s+1)/2\), so the asserted uniform bound follows.

**5. Exponential mixing obstruction for even \(s\).** Write \(C=\binom{2\ell}{\ell}\), \(B=\binom{2\ell}{\ell+1}\), and \(q=C/(C+B)=(\ell+1)/(2\ell+1)\). Under uniform stationarity, exactly half the states have hub spin zero. Denote that half by \(S\). A transition from \(S\) to its complement must select the hub in a configuration with all \(k_j=\ell\). Such configurations comprise fraction \(q^r\) of \(S\). Therefore the exact stationary conductance across the hub-colour cut is
\[
\Phi(S)=\frac{Q(S,S^c)}{\pi(S)}=\frac{q^r}{N}.
\]
Start from \(\pi(\cdot\mid S)\). Its law after any number of updates is coordinatewise at most \(2\pi\), by stationarity and positivity of the transition kernel. Hence at each time the probability of crossing from \(S\) to \(S^c\) is at most \(2Q(S,S^c)=\Phi(S)\). By a union bound, the probability of being outside \(S\) at time \(t\) is at most \(t\Phi(S)\), whereas \(\pi(S^c)=1/2\). Its total-variation distance is at least \(1/2-t\Phi(S)\). As a mixture of deterministic starts cannot be farther than every deterministic start, the claimed lower bound on \(t_{\mathrm{mix}}(1/4)\) follows.

## Verification

The standalone script `verify.py` constructs the exact transition graph for each listed small instance, checks that the monochromatic-edge energy never increases, enumerates all terminal strongly connected components independently of the claimed formulas, compares their union against the predicted block-count criterion, and verifies the recurrent class cardinalities and reversibility. Run `python verify.py` with Python 3. The recorded output `verification_output.txt` ends with `CHECK_OK cases 21`. All tested models have at most eleven vertices; these finite checks are diagnostic, not substitutes for the arbitrary-parameter proof.

## Relationship to prior work

Regnault, Rouquier and Thierry's *Stochastic Minority on Graphs* (early public preprint in April 2008; arXiv version 2010) supplies the precise closed-neighbourhood update, energy monotonicity, and its clique attractor theorem. Its Theorem 4.1 already settles the **single-clique** case \(r=1\), with the corresponding even/odd clique behaviour. The contribution here is the full all-\(r\) gluing classification, the absence of nonground recurrence, the polynomial entrance bound, and the explicit exponentially small hub-crossing conductance for all even peripheral sizes. The energy argument alone does not count communicating classes or bound their mixing.

Other antiferromagnetic Ising and Glauber-mixing results concern different graphs, temperatures, signs or transition conventions; ferromagnetic or positive-temperature mixing assertions cannot be imported into this zero-temperature antiferromagnetic chain without further hypotheses. Searches for windmill, friendship-graph, glued-clique, block-graph and antiferromagnetic minority formulations found no equivalent result in the inspected accessible primary material or indexed summaries. This is a bounded literature assessment, not a proof of global novelty.

## Limitations

No sharp upper bound for mixing within the even-\(s\) recurrent class is asserted. The provided entrance bound is uniform and polynomial but not optimized. The result requires exact uniform, one-site selection and the closed-neighbourhood minority convention; synchronous updates, open-neighbourhood minority, finite-temperature heat-bath chains and nonuniform selection rates need not obey these formulas. The earlier April 2008 preprint landing page was metadata-accessible but full text was access-restricted; the accessible later full-text version was read instead. Independent external validation has not been performed.

## References

1. D. Regnault, J.-B. Rouquier and E. Thierry, *Stochastic Minority on Graphs*, HAL hal-00272271, first preprint 15 April 2008; expanded text arXiv:1011.5119, first arXiv posting 23 November 2010. Accessible full text: https://ar5iv.labs.arxiv.org/html/1011.5119 . Relevant material: §§2, 3.1, 4.1, particularly the energy lemma and Theorem 4.1.
2. J. Ding and Y. Peres, *Mixing time for the Ising model: a uniform lower bound for all graphs*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 47 (2011), 1020–1028, https://www.numdam.org/articles/10.1214/10-AIHP402/ . Background comparison only; it addresses ferromagnetic Ising Glauber dynamics, not the process proved here.

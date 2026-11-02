# Sharp one-edge inhibition bounds for fractional-threshold social cascades

## Finding

Fix a uniform adoption fraction \(0<\phi<1\). For any connected simple undirected graph \(G\) with \(n\ge3\) vertices, one seed \(s\), and an absent edge \(e\), compare the eventual irreversible adopter sets before and after adding \(e\). Define the worst single-tie loss

\[
L(n,\phi)=\max_{G,s,e}\bigl(|A(G,s,\phi)|-|A(G+e,s,\phi)|\bigr).
\]

Put \(k=\lfloor1/\phi\rfloor\). The complete sharp classification is

\[
\boxed{L(n,\phi)=\begin{cases}
0,&3\le n\le k+1,\\
2,&\phi>1/2\quad(\text{hence }k=1,\ n\ge3),\\
n-1,&0<\phi\le1/2,\quad n\ge k+2.
\end{cases}}
\]

The minimum order of a graph in which adding one edge reduces final adoption is \(k+2\). There is a sharp qualitative change at \(\phi=1/2\): strictly above it the loss is at most two independent of graph order, while at or below it one added tie can prevent every nonseed vertex from adopting. The original graph can reach full adoption in every extremal example.

## Assumptions and scope

All graphs are finite, simple, undirected, connected, and initially have at least one nonedge available for insertion. The vertex set and the unique seed are fixed when an edge is added. The seed remains active forever. Other vertices begin inactive and update synchronously: an inactive vertex of positive degree adopts permanently exactly when the fraction of its neighbors active at the preceding step is at least \(\phi\). Connectedness ensures positive degrees. The final active set \(A(G,s,\phi)\) exists after at most \(n-1\) rounds with an adoption. Ties at the threshold adopt. The maximum is over every eligible triple \((G,s,e)\) on \(n\) vertices.

## Proof

**1. Below the first order threshold no edge can be harmful.** Put \(k=\lfloor1/\phi\rfloor\), so \(1/(k+1)<\phi\le1/k\). If \(n\le k+1\), every vertex degree in either \(G\) or \(G+e\) is at most \(n-1\le k\). A single active neighbor therefore supplies at least \(1/k\ge\phi\) of the neighbor set. Connectedness and induction on distance from the seed imply eventual adoption of every vertex in both graphs. Hence \(L(n,\phi)=0\).

**2. The upper bound for \(\phi>1/2\).** Starting from exactly one seed \(s\), any vertex newly adopting in the first round has at least one active neighbor, necessarily \(s\). If its degree were at least two, its active-neighbor fraction would be at most \(1/2<\phi\). Thus the first-round adopters are precisely the degree-one neighbors of \(s\). They have no neighbors other than \(s\), so they cannot trigger any additional adoption. Consequently

\[
A(G,s,\phi)=\{s\}\cup\{v:\deg_G(v)=1,\ sv\in E(G)\}.
\]

Adding one edge can change the degree-one status of at most its two endpoints. Every other former adopting leaf remains a leaf attached to \(s\) and still adopts. The lost set has size at most two, proving \(L(n,\phi)\le2\). For every \(n\ge3\), take the star centered at the seed and add an edge between any two leaves. All leaves adopt before insertion, but precisely those two have degree two afterward and remain inactive; the remaining leaves adopt. Therefore \(L(n,\phi)=2\).

**3. The sharp low-threshold construction.** Suppose \(0<\phi\le1/2\); thus \(k\ge2\). Fix any \(n\ge k+2\). Use vertices \(0,1,\dots,n-1\) with seed \(0\). Add edges \((0,1)\), \((1,j)\) for every \(2\le j\le k\), and \((j,j+1)\) for every \(k\le j<n-1\). The vertex \(1\) has exactly \(k\) neighbors (the seed, \(k-2\) pendant leaves, and vertex \(k\) at the beginning of a path); all internal vertices on the path have degree two. In the original tree, vertex \(1\) adopts from the seed because \(1/k\ge\phi\). Its leaves adopt; adoption then advances along the path because \(1/2\ge\phi\). Hence all \(n\) vertices eventually adopt.

Now insert the absent edge \((1,n-1)\). The gate vertex \(1\) has degree \(k+1\), and its only active neighbor is vertex \(0\), supplying just \(1/(k+1)<\phi\). No other inactive vertex is adjacent to the seed, so no vertex can be the first additional adopter. The final active set consists only of the seed. The loss is \(n-1\), which is the largest conceivable loss since the seed is permanently active. This proves the remaining formula and all its sharpness statements. \(\square\)

The three cases exhaust all \(0<\phi<1\) and \(n\ge3\), including reciprocal-integer threshold boundaries. No finite-graph census is needed for the universal proof.

## Verification

Run `python3 verify.py` using Python 3 with no additional dependencies. It checks exact rational arithmetic for 128,360 comparisons across 767 connected noncomplete labeled graphs on three through five vertices and eight rational thresholds, and checks 64 explicit sharp witnesses at and beyond the minimum order. The analytical proof, rather than these finite tests, certifies the all-order and all-threshold statement.

## Relationship to prior work

Watts (2002) introduced the social-cascade framework and expressly identified the vulnerable-degree condition \(\deg(v)\le\lfloor1/\phi\rfloor\) for a node exposed to one adopter. Whitney (2010) studied finite random-network cascade dynamics, while Singh, Sreenivasan, Szymanski and Korniss (2013) investigated single- and multiple-initiator cascades and clustering. The general dense-cluster obstruction in Easley and Kleinberg, *Networks, Crowds, and Markets*, chapter 19, also applies to the model. These results supply the mechanism and some general termination criteria; none of the inspected statements gives the extremal loss \(L(n,\phi)\) under one adversarial edge insertion, its minimum network order, and its discontinuity at one-half. These conclusions require the two-sided graph construction and worst-case upper bounds above. Lack of a matching located statement does not prove worldwide priority.

## Limitations

Only one permanently active seed, an initially connected undirected graph, simultaneous irreversible deterministic updates, and a common fractional threshold are considered. The result is a worst-case possibility, not a prediction of typical social-network outcomes; fixed absolute-number thresholds, fixed per-edge influence weights, stochastic adoption, and interventions involving deletion/rewiring are different models. Priority relative to unindexed network-extremal notes remains uncertain. At high thresholds the inability to propagate beyond one-step leaves is a genuine restrictive model feature, not an empirical statement about all social contagion.

## References

1. D. J. Watts, “A simple model of global cascades on random networks,” *PNAS* **99** (2002), 5766–5771, published April 30, 2002. https://doi.org/10.1073/pnas.082090499
2. D. E. Whitney, “Dynamic theory of cascades on finite clustered random networks with a threshold rule,” *Physical Review E* **82** (2010), 066110. https://doi.org/10.1103/PhysRevE.82.066110
3. P. Singh, S. Sreenivasan, B. K. Szymanski, G. Korniss, “Threshold-limited spreading in social networks with multiple initiators,” *Scientific Reports* **3** (2013), 2330. https://doi.org/10.1038/srep02330
4. D. Easley and J. Kleinberg, *Networks, Crowds, and Markets*, chapter 19, section 19.3, Cambridge University Press (2010). https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch19.pdf

# A single tie creates absorbing polarization: the sharp five-agent boundary and a persistent star-family effect

## Finding

For a connected finite simple undirected network, give each vertex an initial binary opinion independently and uniformly. At each discrete time choose one vertex uniformly and independently; it flips exactly when strictly more than half of its neighbors hold the opposite opinion. A tie preserves its current opinion. Write \(p(G)\) for the probability of eventual *polarized absorption*, meaning an absorbing state containing both opinions, and \(T(G)\) for the expected number of attempted vertex updates until absorption, counting unchanged attempts.

**Sharp threshold and classification.** A single edge addition can change \(p(G)=0\) to \(p(G+e)>0\) first on five vertices. At that order there are exactly two distinct isomorphism classes of *edge-marked transitions* \((G,e)\), represented on vertices \(\{0,1,2,3,4\}\) by:

1. A four-leaf star, \(E(G)=\{01,02,03,04\}\), with new edge \(e=12\). Here \(p(G)=0\), \(p(G+e)=7/48\), \(T(G)=105/16\), and \(T(G+e)=355/64\).
2. A triangle with two leaves on distinct triangle vertices, \(E(G)=\{01,02,03,12,14\}\), with new edge \(e=34\). Here \(p(G)=0\), \(p(G+e)=31/192\), \(T(G)=713/96\), and \(T(G+e)=545/96\).

The complete labeled count is \(90\) transitions: \(30\) of the first marked type and \(60\) of the second. There are no such transitions on fewer than five vertices.

**Persistence on expanding stars.** For each integer \(m\ge4\), let \(H_m\) be the star with \(m\) leaves after connecting two of its leaves. The unmodified star has \(p=0\). There is an exact finite-sum expression below for \(q_m=p(H_m)\), and
\[
\lim_{m\to\infty}q_m=\frac14.
\]
Thus adding one edge to a connected tree can create absorbing disagreement with a probability that approaches one quarter even as the number of agents grows.

## Assumptions and scope

All graph edges are unweighted, all initial opinions are independently fair, and the updating vertex is sampled uniformly at each attempt. Ties cause no change, a convention essential to the conclusions. The graph remains connected after edge insertion. An *absorbing configuration* permits no opinion-changing update; because ties preserve opinions, an absorbing configuration is precisely a weak local majority at every vertex. Polarization excludes the two unanimous configurations. Claimed finite classifications concern connected simple graphs and one new **nonedge**. The asymptotic statement concerns only the specified star family. No result here addresses synchronous updating, random tie flipping, asymmetric update frequencies, or general noisy epidemic/contact processes.

## Proof

### Finite absorption and potential

For a coloring \(s\), let \(D(s)\) count edges with distinct endpoint opinions. Flipping a vertex with degree \(d\) and \(a>d/2\) disagreeing neighbors changes \(D\) by \(d-2a\le-1\). Thus the directed graph of genuine flips is acyclic. Uniformly sampling vertices gives almost-sure eventual absorption in at most \(|E|\) genuine flips; idle attempts are geometrically integrable. All absorbing colorings are exactly those satisfying \(2a_v\le d_v\) at every vertex.

### The lower boundary below five vertices

In a connected graph, an absorbing nonunanimous coloring has no monochromatic singleton color class, because the singleton's neighbors all oppose it and it would flip. Consequently any such graph needs at least four vertices. On exactly four vertices, both color classes must have size two. Each vertex must have an internal same-color neighbor, so each color class induces an edge, and each vertex has at most one cross-color neighbor. Connectedness then forces exactly one or two cross-color edges; the underlying graph is a four-vertex path or a four-cycle. The path is a tree and hence cannot arise by adding an edge while preserving connectedness of the predecessor. Deleting any edge of the four-cycle leaves a path, which itself already admits a polarized absorbing coloring (the two consecutive vertices of each color). Thus a connected graph on at most four vertices cannot *acquire its first* polarized absorbing state by adding one edge. Since every absorbing coloring has strictly positive initial probability, this proves the four-vertex obstruction for \(p\), not only for graph existence.

### Exhaustive five-vertex classification and exact probabilities

The program `verify_majority.py` uses no graph database. For each \(n\in\{2,3,4,5\}\), it enumerates the \(2^{\binom n2}\) labeled simple graphs using edge bitmasks; tests connectedness by repeated neighbor closure; and tests each of the \(2^n-2\) nonunanimous opinions using the exact integer inequality \(2a_v\le d_v\). For each connected graph lacking a polarized absorbing state, it tests *every nonedge* as a single edge insertion. Each successful edge-marked pair is canonically relabeled by minimizing its ordered list of old edges and its distinguished new edge over *all* \(n!\) vertex permutations. This finite exhaustive procedure yields \(1,4,38,728\) connected labeled graphs for \(n=2,3,4,5\), respectively; zero successful marked pairs before five vertices; and exactly \(90\) successful marked pairs forming the two stated isomorphism classes. The script's source specifies the entire domain and tests, rather than relying on a precomputed catalog or finite random samples.

For each representative, let \(F\) denote the vertices whose opinions would strictly improve by flipping. If \(F\ne\varnothing\), first-step conditioning on the next effective flip gives the exact recurrences
\[
P(s)=\frac{1}{|F|}\sum_{v\in F}P(s\oplus v),\qquad
U(s)=\frac{n}{|F|}+\frac{1}{|F|}\sum_{v\in F}U(s\oplus v),
\]
with boundary \(P(s)=1\) on polarized absorbing states, \(P(s)=0\) on unanimous absorbing states, and \(U(s)=0\) for any absorbing state. Strict decrease of \(D\) makes these recurrences triangular. Averaging their exact rational solutions over all \(2^n\) initial colorings proves the four probability and time values above. Independently, `independent_markov.py` constructs the entire \(32\)-state transition matrix for each of the four five-vertex networks, solves \((I-Q)P=r\) and \((I-Q)U=\mathbf1\) by exact rational Gaussian elimination, and obtains precisely the same values. It finds absorbing states indexed \(\{0,31\}\) before each addition, and \(\{0,6,25,31\}\) and \(\{0,7,24,31\}\) respectively afterward.

### Exact star-family formula and nonvanishing limit

Fix an initial hub opinion as reference. Of the \(m-2\) unlinked leaves, let \(J\sim\operatorname{Bin}(m-2,1/2)\) count those initially opposed to the hub, and put \(h=\lfloor m/2\rfloor\). Classify the two linked leaves initially as both opposed, both agreeing, or mixed. Set, for integers \(0\le j\le m-2\),
\[
O_j=\begin{cases}1,&j<h-1,\\ (h-1)/(j+1),&j\ge h-1,\end{cases}
\qquad
S_j=\begin{cases}0,&j<h+1,\\ (j-h)/(j+1),&j\ge h+1.\end{cases}
\]
Define \(M_{-1}=0\) and
\[
M_j=\frac{jM_{j-1}+S_j}{j+1+\mathbf1_{\{j\ge h\}}}.
\]
Then the exact probability is
\[
q_m=\frac{1}{2^{m}}\sum_{j=0}^{m-2}\binom{m-2}{j}\bigl(O_j+S_j+2M_j\bigr).
\]
To prove the formula, expose only *effective* update clocks; all vertices update at identical rate, so among presently flippable vertices the next flip is uniform. Ordinary leaves opposed to the fixed hub flip toward it at total rate \(j\). If both linked leaves oppose the hub they are protected by their mutual tie and a potential hub flip occurs at rate one exactly for \(j\ge h-1\); surviving the race until \(j<h-1\) has telescoping probability \((h-1)/(j+1)\), giving \(O_j\). If both linked leaves agree with the hub, only the hub can flip against an ordinary-leaf majority, available at rate one for \(j\ge h+1\), and surviving ordinary-leaf depletion until that threshold gives \(S_j\). For the mixed pair, the opposed linked leaf can align at rate one, leading to the agreeing-pair state \(S_j\); the hub can flip at rate one if \(j\ge h\), which cannot lead to polarization; and the \(j\) opposed ordinary leaves can align, leaving the mixed state with index \(j-1\). This is exactly the displayed recurrence for \(M_j\). The three initial linked-pair possibilities have weights \(1/4,1/4,1/2\), yielding the finite sum. `star_family.py` verifies the rational values for \(m=4,\ldots,8\) and evaluates larger instances.

For the limit, a hub can flip **at most once**: before its first flip the number of its disagreeing leaves cannot increase, and immediately after any hub flip fewer than half its leaves disagree; subsequent leaves can only realign toward it. Write \(T=h-1\) and \(J\sim\operatorname{Bin}(m-2,1/2)\). Any hub flip requires at least \(T\) ordinary leaves still initially opposed. Ignoring any extra aligning linked-leaf changes, the competing clocks give
\[
\Pr(\text{hub ever flips})\le
\mathbb E\left[\frac{(J+1-T)_+}{J+1}\right]
\le \frac{\sqrt{m-2}/2+3/2}{h-1}\xrightarrow[m\to\infty]{}0.
\]
Indeed, the upper bound is the probability that a unit-rate hub clock rings before at least \(J-T+1\) ordinary leaves have independently realigned; the race telescopes. The final inequality uses \(\mathbb E|J-\mathbb EJ|\le\sqrt{m-2}/2\) and \(\mathbb EJ+1-T\le3/2\). When the hub never flips, final polarization occurs **if and only if** the two joined leaves were *initially both opposed* to the hub: they then mutually protect their discordance, whereas a mixed pair or initially aligned pair ultimately aligns. That initial event has probability \(1/4\). Its indicator can disagree with eventual polarization only if the hub flips, so \(|q_m-1/4|\le\Pr(\text{hub ever flips})\), completing the proof.

## Verification

Run `python3 verify_majority.py`, `python3 independent_markov.py`, and `python3 star_family.py` in the same directory, with Python 3 standard library only. The first script exhausts connected labeled graphs on at most five vertices, tests each admissible edge insertion, reduces all successful marked pairs under every permutation, and calculates exact absorbing probabilities and attempted-update times. The second independently solves all four five-vertex absorbing Markov systems as rational linear equations; the third evaluates the star-family recurrence and checks initial exact fractions. The programs are included in full, not referenced externally. No infinite-state computation is claimed: the family limit follows from the analytic bound in the proof.

## Relationship to prior work

Baek, Ha and Jeong (2011; arXiv:1112.5927, Sections II–IV) study absorption and nonconsensus in random-network zero-temperature Glauber dynamics. Their random equal-spin initialization and **random flips at tied neighborhoods** differ from the present independent fair initialization and strict flip/no-flip rule, and their thermodynamic network ensemble statistics do not establish minimal edge-insertion thresholds. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014; arXiv:1405.2486, Sections 1–3) analyze **synchronous** majority dynamics on unimodular and random graphs; their positive and negative consensus phenomena likewise do not imply the present asynchronous fixed-network edge intervention. Mohan and Prałat (2023; arXiv:2309.04691, Sections 1–4) analyze asynchronous majority announcements on binomial random graphs with initially unannounced public opinions, biased private signals, and private-signal tie breaking. Those different initial/update conventions and their random-network limiting claims do not yield the exact pair classification or probability expressions here. Standard ferromagnetic local potential arguments underpin the elementary absorption lemma; the claim of novelty is confined to the *sharp edge-created-polarization boundary, complete marked five-agent classes, exact probabilities/times, and persistent single-edge star limit*, not to the existence of nonconsensus majority equilibria in general.

## Limitations

This is a deterministic-graph and exact finite-probability statement under a specific tie-retention convention, with an analytic limit for a specific star family. It does not imply increasing polarization under arbitrary link additions, robustness to nonuniform initial opinions, or any socially causal conclusion without model validation. The finite census is complete only for graph orders at most five. Literature overlap cannot be ruled out absolutely, especially equivalent formulations as local minima of the binary coordination/Ising cut potential; no independent external audit has been performed.

## References

1. Y. Baek, M. Ha and H. Jeong, *Absorbing states of zero-temperature Glauber dynamics in random networks*, arXiv:1112.5927 (first publicly posted 2011-12-27), Phys. Rev. E 85, 031123 (2012). https://arxiv.org/html/1112.5927v2
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (2014). https://arxiv.org/html/1405.2486v1
3. D. Mohan and P. Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs*, arXiv:2309.04691 (first publicly posted 2023-09-09). https://arxiv.org/html/2309.04691v2

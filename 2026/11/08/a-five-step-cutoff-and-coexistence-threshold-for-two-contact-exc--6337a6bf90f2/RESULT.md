# A five-step cutoff and coexistence threshold for two-contact excitation on complete bipartite graphs

## Finding

For every pair of integers \(m,n\ge1\), consider synchronous three-color Greenberg–Hastings dynamics on the labelled simple graph \(K_{m,n}\), with **excitation threshold two**: states \(1\to2\to0\) update unconditionally, and a state-zero vertex changes to state one precisely when at least two of its neighbors are in state one. Write \(T(x)\) for the first time the full labelled configuration is periodic and \(p(x)\) for its eventual least temporal period.

**Theorem.** Every configuration enters periodic behavior by time five, the only possible eventual least periods are \(1,3,4\), and the only fixed configuration is all-zero. For all \(m,n\),
\[
F^{17}=F^5.
\]
The sharp maximum first-entry time \(\tau(m,n)=\max_xT(x)\) is
\[
\tau(m,n)=\begin{cases}
2,&m=n=1,\\
3,&\min(m,n)=1<\max(m,n)\ \text{or}\ m=n=2,\\
4,&\min(m,n)=2<\max(m,n)\ \text{or}\ m=n=3,\\
5,&\min(m,n)\ge3,\ \max(m,n)\ge4.
\end{cases}
\]
Define
\[
E_s=\sum_{a,b,c\ge2\atop a+b+c=s}\frac{s!}{a!b!c!},\qquad
R_s=\sum_{j=2}^{s-2}\binom{s}{j},
\]
with empty sums zero. Exactly \(E_mE_n\) configurations are already on primitive three-cycles, exactly \(2R_mR_n\) are already on primitive four-cycles, and one configuration is fixed. Thus three-cycles exist exactly when \(\min(m,n)\ge6\), and four-cycles exactly when \(\min(m,n)\ge4\). Their orbit counts are \(E_mE_n/3\) and \(R_mR_n/2\), respectively.

There is also an **exact joint first-entry/period census** for every \(m,n\), not merely the recurrent-state census. Let \(\mathcal C=\{0,1,2\}^6\), with profile coordinates \((a_0,a_1,a_2,b_0,b_1,b_2)\). Define \(\operatorname{cap}(u)=\min(u,2)\) and the map \(\Phi:\mathcal C\to\mathcal C\): on each shore \((h_0,h_1,h_2)\), with opposing shore \((j_0,j_1,j_2)\), set
\[
\phi(h;j)=\begin{cases}(h_2,h_0,h_1),&j_1=2,\\
(\operatorname{cap}(h_0+h_2),0,h_1),&j_1<2.
\end{cases}
\]
Then \(\Phi(a,b)=(\phi(a;b),\phi(b;a))\). For \(c\in\mathcal C\), let \(t(c)\) be the first \(0\le t\le5\) such that \(\Phi^t(c)\) lies in the following recurrent set, and let \(p(c)\) be the indicated period:
\[
\begin{aligned}
\mathcal R_1&=\{(i,0,0,j,0,0):0\le i,j\le2\},\\
\mathcal R_3&=\{(2,2,2,2,2,2)\},\\
\mathcal R_4&=\{(2,0,2,2,2,0),(2,2,0,2,0,2)\}.
\end{aligned}
\]
All 729 profiles enter the union of these 12 states by time five. Put \(g_0(z)=1\), \(g_1(z)=z\), and \(g_2(z)=e^z-1-z\). For each \(t\in\{0,1,2,3,4,5\}\) and \(p\in\{1,3,4\}\), the exact number of **labelled** configurations with first-entry time \(t\) and eventual period \(p\) is
\[
\boxed{N_{t,p}(m,n)=m!n!\,[z^mw^n]\!\sum_{c\in\mathcal C:\ (t(c),p(c))=(t,p)}\ \prod_{i=0}^2g_{c_i}(z)\prod_{i=3}^5g_{c_i}(w).}
\]
All unlisted classes have zero population; this is a finite 729-profile formula involving no simulation of the \(3^{m+n}\) labelled states. The 12 nonempty abstract temporal classes and their abstract profile counts are recorded in the verification section and exhaust the 729 profiles.

## Assumptions and scope

The shores are nonempty and labelled. The graph has no loops or same-shore edges. Vertices update simultaneously, based only on the previous time slice. Threshold two means **at least two distinct excited neighbors**, so all vertices of one shore share the same stimulation predicate. The result concerns deterministic finite-state dynamics, not stochastic excitations or general noncomplete bipartite graphs. The generating functions above are formal exponential series; coefficient extraction is exact over the rational numbers.

## Proof

**1. Exact saturated quotient.** For a full configuration \(x\), let \(a_i\) and \(b_i\) count the vertices of color \(i\) in each shore. The one-step counts in a shore are \((a_2,a_0,a_1)\) if the other shore has at least two excited vertices and \((a_0+a_2,0,a_1)\) otherwise. Truncating each count at two commutes with both updates since \(\operatorname{cap}(u+v)=\operatorname{cap}(\operatorname{cap}(u)+\operatorname{cap}(v))\). Hence the diagram from full labelled states to \(\mathcal C\) commutes exactly with \(F\) and \(\Phi\) at every time. This quotient is valid for arbitrarily large shores because stimulation depends only on whether the opposing excited count is \(0,1\), or at least \(2\).

**2. Exhaustive finite lemma.** The 729 abstract profiles, including profiles corresponding to empty shores, are partitioned by the explicitly given transition formula. Direct exhaustive evaluation shows that \(\mathcal R_1\) comprises nine fixed profiles, \(\mathcal R_3\) one fixed profile, and \(\mathcal R_4\) one two-cycle. Every other profile enters one of them in at most five steps. The exact table of \(\#\{c:(t(c),p(c))=(t,p)\}\), with columns \(p=1,3,4\), is:

| \(t\) | \(p=1\) | \(p=3\) | \(p=4\) |
|---:|---:|---:|---:|
| 0 | 9 | 1 | 2 |
| 1 | 72 | 0 | 10 |
| 2 | 360 | 0 | 30 |
| 3 | 160 | 0 | 8 |
| 4 | 51 | 0 | 2 |
| 5 | 24 | 0 | 0 |

The 729-entry universal assertion is a finite lemma with a complete standalone verification algorithm in `verify_symbolic.py`: its loop visits **every** element of \(\{0,1,2\}^6\), computes each transition by the displayed formula, asserts the exact table, and asserts recurrence by time five. Because the quotient is proved for all shore sizes, this is an exhaustive **symbolic** certificate, not an extrapolation from a bounded set of graphs.

**3. Lifting recurrent profiles to actual periodic states.** Every full state over \(\mathcal R_1\) is all-zero. Every full state over \(\mathcal R_3\) has at least two vertices of each color on each shore; every time step rotates all colors, so the least period is three. In \(\mathcal R_4\), one shore has at least two vertices in states zero and two and none in state one, while the other has at least two vertices in states zero and one and none in state two, or vice versa. The stimulation predicates alternate each update, and applying the four successive local maps to each of the two occupied colors returns every vertex to its original color. No such configuration returns after one or two steps (its phase sets do not), hence the least period is four. Conversely, a full periodic state must have a periodic saturated image, so the finite lemma excludes all other recurrent structures. If a full state entered its periodic orbit earlier than its saturated profile reached the displayed recurrent set, its saturated image would already have been periodic, a contradiction. Thus \(T(x)=t(\operatorname{sat}(x))\) and \(p(x)=p(\operatorname{sat}(x))\). The least common multiple of \(1,3,4\) is twelve, giving \(F^{17}=F^5\).

**4. Recurrent counts and sharp threshold.** A period-three state requires all three colors to appear at least twice on each shore. Multinomial allocation gives \(E_mE_n\); existence is equivalent to both shores having at least six vertices. For a period-four state each shore uses exactly two specified colors, each occupied at least twice, in one of two orientations; allocation gives \(2R_mR_n\), possible exactly when both shores have at least four vertices. The only fixed state is all-zero. Divide primitive-state counts by the respective least period to obtain orbit counts.

**5. Sharp first-entry bound.** For each \(s\ge1\), a three-vector \(a\in\{0,1,2\}^3\) is realizable as truncated counts on a shore of size \(s\) exactly when either \(a\) has a coordinate equal to two and \(\sum a_i\le s\), or \(a\) has no coordinate two and \(\sum a_i=s\). In particular, realizability classes stabilize once \(s\ge6\). The finite lemma, restricted to the realizable profiles for \(1\le m,n\le6\), yields the following exact sharp-max matrix, rows and columns indexed by shore size 1 through 6:
\[
\begin{pmatrix}2&3&3&3&3&3\\3&3&4&4&4&4\\3&4&4&5&5&5\\3&4&5&5&5&5\\3&4&5&5&5&5\\3&4&5&5&5&5\end{pmatrix}.
\]
Stabilization of feasible saturated classes for \(s\ge6\) extends this finite verification to all shore sizes, proving the stated piecewise sharp formula. For example, the configuration with shore colors \((0,0,1)\) and \((0,0,1,1)\) has first-entry time five on \(K_{3,4}\), and additional zeros on either shore preserve its saturated trajectory and its first-entry time.

**6. Exact basin coefficient formula.** For each coordinate a truncated count zero has exponential generating function \(1\), truncated count one has \(z\), and truncated count two (meaning two or more actual vertices) has \(e^z-1-z\). Taking products for the three colors on each shore and extracting \(m!n![z^mw^n]\) supplies exactly the labelled multinomial weights of each abstract profile. Selecting profiles by \((t,p)\) therefore gives the asserted joint census, including every transient basin.

## Verification

Execute `python3 verify_symbolic.py` and `python3 verify_direct.py` in a directory containing the two standalone scripts. The captured results are in `verify_symbolic.out` and `verify_direct.out`.

The first program exhaustively checks the full 729-element symbolic quotient, every recurrent target, the complete abstract entrance table, and the sharp-size matrix through six (which suffices for all sizes by the proved realizability saturation). The second uses **direct vertex-by-vertex labelled dynamics**, verifies the quotient's predicted first-entry/least-period for every configuration on all 25 graphs with \(1\le m,n\le5\) and on \(K_{6,6}\), and independently checks the multinomial class weights. The total direct corpus is **663,210 labelled configurations**. Both scripts passed, with their output bytes reproducible from the packaged code.

These finite labelled tests are independent checks; the unrestricted theorem follows from the exact quotient lemma and the corresponding mathematical lifting and counting arguments, not from finite-size extrapolation.

## Relationship to prior work

Fisch, Gravner and Griffeath's 1991 threshold–range paper develops the multicolor Greenberg–Hastings framework and excitation thresholds in planar lattices. Their March and April 1993 arXiv records establish dated archival access to the foundational literature. Gravner–Lyu–Sivakoff (2016) studies the three-color **threshold-one** process on arbitrary graphs. Bello–Sivakoff (2021) treats **threshold at least two**, but on infinite regular trees, establishing probabilistic fixation/fluctuation regimes. None of those inspected main results supplies the finite complete-bipartite threshold-two temporal-basin formula, sharp entry-time matrix, or simultaneous three/four-cycle census.

Earlier complete-bipartite results for threshold one concern a **different update map**. Threshold two creates genuinely new density conditions: three-cycles require at least six vertices per shore and four-cycles at least four, whereas the threshold-one requirements are different. A threshold-one counting theorem cannot be substituted for the present rule. See `REVIEW.md` and `AUDIT.json` for recorded priority comparisons and risks.

## Limitations

The theorem assumes exactly three colors, threshold exactly two, and a complete bipartite graph with both shores nonempty. The 729-state symbolic certificate is a finite exhaustive argument with transparent program and exact combinatorial derivation; no independent formal certification or independent audit is claimed. Historical priority remains qualified by incompletely indexed literature, particularly threshold-range models on other graph families. This result does not determine behavior for general graphs, other thresholds, or stochastic state updates.

## References

1. R. Fisch, J. Gravner, D. Griffeath, “Threshold-range scaling of excitable cellular automata,” *Statistics and Computing* **1** (1991), 23–39. DOI: `10.1007/BF01890834`; authors' accessible full text: `https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf`; preprint `arXiv:patt-sol/9304001`, first posted 1993-04-02.
2. R. Fisch, J. Gravner, D. Griffeath, “Metastability in the Greenberg–Hastings Model,” *Annals of Applied Probability* **3** (1993), 935–967; `arXiv:patt-sol/9303005`, first posted 1993-03-23.
3. J. Gravner, H. Lyu, D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” `arXiv:1610.07320v1`, first posted 2016-10-24.
4. J. Bello, D. Sivakoff, “Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees,” `arXiv:2108.06404v1`, first posted 2021-08-13.

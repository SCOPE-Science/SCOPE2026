# Twin-block rigidity of unsharp implication and its Poisson sharpness law

## Finding

**Theorem (incidence-section rigidity and graph-incidence sharpness law).** Let \(V\) be a nonempty finite set of points, let \(B\) be a finite set of distinct block-elements with nonempty incidences \(I_b\subseteq V\), and form the poset \(P(V,B,I)\) with order relations \(v<b<1\) precisely when \(v\in I_b\), together with reflexivity, transitivity, and no other comparabilities. Write \(N(v)=\{b\in B:v\in I_b\}\).

1. Every principal section \([y,1]\) is pseudocomplemented if and only if \(|N(v)|\le2\) for every point \(v\).
2. Subject to this condition, equip \(P\) with the set-valued implication of Chajda and Länger, \(x\to y=\{z^{y}:z\in\operatorname{Min}U(x,y)\}\), where \(z^{y}\) denotes the pseudocomplement of \(z\) in \([y,1]\). An implication value is nonsingleton if and only if \(x\ne y\) are points with \(N(x)=N(y)=\{b,c\}\) for distinct block-elements \(b,c\). In that event, \(x\to y=\{b,c\}\). Consequently, the number \(U(P)\) of ordered pairs with nonsingleton implication is exactly
   \[
   U(P)=\sum_{\{b,c\}\in\binom{B}{2}} t_{bc}(t_{bc}-1),\qquad
   t_{bc}=|\{v\in V:N(v)=\{b,c\}\}|.
   \]
3. Specialize to the loopless multigraph-incidence poset of a multigraph \(G\), with vertices as points and distinct edge-occurrences as blocks, each block incident with exactly its two endpoints. Sections are pseudocomplemented exactly when \(\Delta(G)\le2\), and then \(U(P_G)=2D(G)\), where \(D(G)\) is the number of double-edge components (two vertices joined by two parallel edges).
4. On \([n]\) let edges of a multigraph be indistinguishable except for their endpoints and multiplicity; let \(\mathcal G_n\) be the set of all loopless multigraphs with maximum degree at most two, and put \(\mathcal G_0=\{\varnothing\}\). The exact marked exponential generating function is
   \[
   \sum_{n\ge0}\frac{z^n}{n!}\sum_{G\in\mathcal G_n}t^{D(G)}
   =(1-z)^{-1/2}\exp\!\left(\frac{z}{2(1-z)}+\frac{(2t-1)z^2}{4}\right).
   \]
   If \(G_n\) is uniform on \(\mathcal G_n\), then
   \[
   D(G_n)\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}(1/2),\qquad
   \lim_{n\to\infty}\Pr\bigl(\forall x,y\in P_{G_n},\ |x\to y|=1\bigr)=e^{-1/2}.
   \]
   Equivalently, the number of nonsingleton ordered implication entries converges in distribution to twice a Poisson random variable of mean \(1/2\).

## Assumptions and scope

The point set is nonempty. Blocks are distinct elements even when they have identical incidences; no block is empty. The extra top element \(1\) is a new element, not an existing block. An isolated point is permitted, and \(B\) may be empty. Each interval \([y,1]\) is considered with its own bottom \(y\); the definition of pseudocomplement in that interval is the greatest element \(c\ge y\) satisfying \(L(z,c)\cap[y,1]=\{y\}\). The expression \(U(x,y)\) is the common upper cone, and \(\operatorname{Min}\) takes its minimal elements. All counts concern **ordered** arguments \((x,y)\) and distinguish a set-valued implication from an ordinary single-valued operation.

In the multigraph subfamily the graph edges are occurrences, and any two occurrences with the same endpoint pair remain distinct poset elements. There are no loops, no edge colors, and no labels on individual parallel edges. The graph's vertex labels are \(1,\ldots,n\). A component with two vertices joined by two edges is a cycle of length two, not a simple graph cycle. There are no isolated edge-elements, because every graph edge has two endpoints.

## Proof

**Sections.** For a block-element \(b\), \([b,1]=\{b,1\}\), and \([1,1]\) is trivial. For a point \(v\), the section \([v,1]\) consists of its bottom \(v\), the \(d(v)=|N(v)|\) incomparable block-elements above it, and its top \(1\). At degree zero or one this is a chain; at degree two it is a four-element Boolean diamond. All are pseudocomplemented. At degree at least three, fix a block-element \(b\ge v\). Every different block-element above \(v\) has common lower cone \(\{v\}\) with \(b\) inside the section. At least two such elements are incomparable, and no common upper element can be their pseudocomplement because their only common upper bound is \(1\), which is not disjoint from \(b\) above \(v\). Hence \(b\) has no greatest disjoint companion in \([v,1]\). This proves the equivalence.

**Localization of nonsingleton implication.** A value \(x\to y\) can have more than one element only if \(\operatorname{Min}U(x,y)\) has at least two elements. If \(x\le y\) or \(y\le x\), its minimal common upper element is unique. If \(x,y\) are distinct block-elements, or one is a block-element and the other an incomparable point, their sole minimal common upper element is \(1\). Thus only distinct incomparable points can qualify. Their common upper cone has minimal elements precisely the common incident block-elements \(N(x)\cap N(y)\), unless this intersection is empty, in which case the only minimal common upper element is \(1\). Since degrees are at most two, at least two common blocks occur exactly when \(N(x)=N(y)=\{b,c\}\). In \([y,1]\), the pseudocomplements of the two coatoms \(b,c\) are respectively \(c,b\), so their image set is exactly \(\{b,c\}\). Conversely the singleton-common-upper cases yield singleton values. Grouping vertices by their common two-block neighborhood proves the formula for \(U(P)\).

**Graph components.** The incidence degree of a point equals its multigraph degree. A finite loopless multigraph of maximum degree two has components consisting of isolated vertices, paths on at least two vertices, simple cycles on at least three vertices, or pairs of vertices joined by two parallel edges. Its only distinct vertices with the same two-edge neighborhood are the two endpoints of a double-edge component. Each such component contributes exactly its two ordered cross-pairs; all other components contribute zero. Hence \(U(P_G)=2D(G)\).

**Exact enumeration.** For the labelled exponential formula, one isolated vertex has connected-component series \(z\). For every \(r\ge2\), labelled paths on \(r\) vertices number \(r!/2\), giving series \(\sum_{r\ge2}z^r/2\). For every \(r\ge3\), labelled undirected cycles number \((r-1)!/2\), giving \(\sum_{r\ge3}z^r/(2r)\). A double-edge component has one structure on a fixed two-set, giving \(tz^2/2\). Summing these four connected series and exponentiating yields
\[
\exp\!\left(z+\sum_{r\ge2}\frac{z^r}{2}+\sum_{r\ge3}\frac{z^r}{2r}+\frac{tz^2}{2}\right)
=(1-z)^{-1/2}\exp\!\left(\frac{z}{2(1-z)}+\frac{(2t-1)z^2}{4}\right).
\]

**Poisson limit, with explicit coefficient justification.** Set
\[
G(z)=(1-z)^{-1/2}\exp\!\left(\frac{z}{2(1-z)}\right)=\sum_{n\ge0}g_nz^n,
\qquad
F(z,1)=G(z)e^{z^2/4}=\sum_{n\ge0}b_nz^n.
\]
The coefficients \(g_n\) are strictly positive and nondecreasing: \(g_0=g_1=1\) and the differential identity \((1-z)^2G'(z)=(1-z/2)G(z)\) implies, for every \(n\ge1\),
\[
(n+1)(g_{n+1}-g_n)=n(g_n-g_{n-1})+\frac12g_{n-1}\ge0.
\]
Furthermore expand \(g_n=\sum_{j=0}^nw_{n,j}\) with
\[
w_{n,j}=\frac{2^{-j}}{j!}\binom{n-1/2}{n-j},\qquad
\frac{w_{n,j+1}}{w_{n,j}}=\frac{n-j}{2(j+1)(j+1/2)}.
\]
For \(m=\lceil\sqrt n\rceil\), the last ratio is at most \(1/2\) when \(j\ge m\). Hence the probability distribution proportional to \(w_{n,j}\) has mean at most \(m+2\). Since \(w_{n-1,j}/w_{n,j}=(n-j)/(n-1/2)\) for \(j\le n-1\), this proves \(g_{n-1}/g_n\to1\). By iterating, \(g_{n-r}/g_n\to1\) for each fixed integer \(r\ge0\). The convolution identity
\[
b_n=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{g_{n-2j}}{4^jj!}
\]
and monotonicity \(g_{n-2j}\le g_n\) permit dominated convergence, so \(b_n/g_n\to e^{1/4}\) and therefore \(b_{n-r}/b_n\to1\) for every fixed \(r\). Monotonicity of \(b_n\) also follows from that of \(g_n\).

Marking the double-edge components in the generating function gives the exact factorial moments, for all \(r\ge0\),
\[
\mathbb E[(D(G_n))_r]=\frac{1}{2^r}\frac{b_{n-2r}}{b_n}\ \longrightarrow\ 2^{-r},
\]
where \(b_k:=0\) for \(k<0\). Because \(b_{n-2r}\le b_n\), these moments are uniformly bounded by \(2^{-r}\). The finite factorial-moment inversion formula and dominated convergence then give \(\Pr[D(G_n)=s]\to e^{-1/2}(1/2)^s/s!\) for each \(s\ge0\), establishing the Poisson limit. The implication is singleton everywhere precisely when \(D(G_n)=0\), completing the proof.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It constructs order relations and pseudocomplements directly, independently checks all pairwise implications for 441 labelled nonempty incidence systems with up to three points and three blocks, and enumerates loopless multigraphs on up to five labelled vertices to check the predicted ambiguity count. It also compares exact rational generating-function coefficients with exhaustive graph counts and computes the finite-size sharpness ratio through order 35. Run using `python verify.py` alongside this document. Finite checks corroborate the structural and counting formulas; the unrestricted statements and asymptotics are supplied by the preceding proof, not by extrapolation from these checks.

## Relationship to prior work

Chajda and Länger, *Implication in finite posets with pseudocomplemented sections* (arXiv:2108.09548v1, 2021-08-21), introduced the exact set-valued implication used here, derived its I-algebra properties, and gave small explicit non-singleton examples, notably Example 2.7. **Those definitions and examples are prior results, not claimed here.** The new assertion is the incidence-section degree characterization, exact twin-block criterion for every permitted incidence system, and its graph-incidence distribution and limiting sharpness law. Chajda, Länger, and Paseka, *Sectionally Pseudocomplemented Posets* (arXiv:1905.09343v1; subsequently in *Order*), study a related but distinct notion of sectional pseudocomplementation. Chajda and Länger, *The intuitionistic-like logic based on a poset* (arXiv:2308.11350v1), study another poset-based implication approach. Classical labelled path-and-cycle enumeration supplies the combinatorial part of the proof; its independent discovery is not claimed.

## Limitations

This classification depends on the three-level point/block/top incidence construction and does not describe arbitrary finite posets with pseudocomplemented sections. The Poisson limit concerns the **uniform** distribution over labelled loopless multigraphs of maximum degree two, with parallel-edge occurrences indistinguishable apart from multiplicity. It is not a statement about uniform simple graphs, Erdos–Renyi graphs without degree conditioning, arbitrary hypergraphs, or a different implication operator. The Poisson law for marked double-edge components follows from classical labelled-component asymptotics; novelty, if established by independent scrutiny, lies in its precise connection to the unsharp-implication spectrum. Earlier equivalent classifications under alternative incidence or logical terminology may exist; no independent originality audit has been performed.

## References

1. I. Chajda and H. Länger, “Implication in finite posets with pseudocomplemented sections,” arXiv:2108.09548v1 (2021-08-21), https://arxiv.org/abs/2108.09548 . See Definition 2.1, Lemma 2.3, and Example 2.7.
2. I. Chajda, H. Länger, and J. Paseka, “Sectionally Pseudocomplemented Posets,” arXiv:1905.09343v1 (2019-05-22); *Order* 38 (2021), 527–546, https://arxiv.org/abs/1905.09343 .
3. I. Chajda and H. Länger, “The intuitionistic-like logic based on a poset,” arXiv:2308.11350v1 (2023), https://arxiv.org/abs/2308.11350 .

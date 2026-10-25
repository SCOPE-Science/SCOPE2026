# A sharp six-vertex clustering reversal in two-seed social contagion

## Finding

Under deterministic two-neighbor adoption from exactly two uniformly chosen distinct initial adopters, an arbitrary finite network with one universally connected individual has an **exact closed-form cascade-size distribution** determined solely by the sizes of the connected communities remaining after removing that individual. Concentrating peripheral community sizes (at fixed number of communities) strictly increases the expected final adoption count.

There is also a sharp, degree-controlled counterexample to the inference that more triangles must give a larger expected adoption cascade. For every integer \(n\ge6\), the connected networks
\[
G_n=K_1\vee P_{n-1},\qquad Q_n=K_1\vee(K_3\sqcup P_{n-4})
\]
have identical degree multisets \(\{n-1,2,2,\underbrace{3,\ldots,3}_{n-3}\}\) and identical edge counts \(2n-3\); yet \(Q_n\) has exactly one more triangle than \(G_n\), while
\[
\mathbb E X(G_n)=n,\qquad
\mathbb E X(Q_n)=n-\frac{3(n-4)(n+1)}{n(n-1)}<n.
\]
No connected simple graph pair with this degree-controlled strict reversal exists on fewer than six vertices. The strict statement includes *global transitivity*: because the degree sequences coincide, the number of connected triples coincides, so triangle count and transitivity rise together.

## Assumptions and scope

All graphs are finite, undirected, simple and unweighted. A vertex is initially active or inactive; active vertices never deactivate. Two distinct vertices are selected uniformly among all unordered pairs as the only initial active set. At each synchronous round an inactive vertex activates if it has **at least two distinct currently active neighbors**. This is an absolute, not a fractional, threshold. \(X(G)\) is the eventual number of active vertices.

For the general law, write \(G=K_1\vee H\), where \(K_1\vee H\) adds one hub joined to every vertex of a graph \(H\) with \(m\ge2\) vertices; \(n=m+1\). Let the connected components of \(H\) have sizes \(s_1,\ldots,s_c\ge1\), with \(\sum_i s_i=m\). Then the probability-generating function, with repeated exponents intentionally combined, is
\[
\boxed{\mathbb E[z^{X(G)}]=\frac{\displaystyle\sum_{i=1}^c\binom{s_i+1}{2}z^{1+s_i}+\displaystyle\sum_{1\le i<j\le c}s_i s_j z^{1+s_i+s_j}}{\binom n2}}.
\]
In particular,
\[
\boxed{\mathbb E X(G)=1+\frac{\sum_{i=1}^c s_i^2(2n-1-s_i)}{n(n-1)}}.
\]
This determines *all* moments and finite-sample tail probabilities, not only the mean.

At fixed \(n\) and component count \(c\), the mean is strictly maximized by the component-size multiset \((n-c,1,\ldots,1)\) and strictly minimized by the components differing in size by at most one; the optimizers are unique as multisets, subject to the trivial case in which there is only one feasible multiset. The strict inequality is for genuinely distinct feasible size profiles.

## Proof

**1. Exact final active set.** If the hub is a seed, it is immediately active. If neither seed is the hub, the hub has two active neighbors and becomes active at round one. Once active, the hub together with one active peripheral vertex causes every peripheral neighbor of that vertex to activate; induction along a path fills the entire connected component of \(H\) containing a seed. Conversely, a component containing no seed has no initially active peripheral vertex. Its vertices are never activated because they see, at most, the active hub outside the component and no active peripheral neighbor inside. Therefore the final active set consists precisely of the hub plus the union of the peripheral components that intersect the seed pair.

**2. The exact distribution.** For a fixed peripheral component of size \(s_i\), the seed pair lies within that component, or comprises the hub and one of its vertices, in exactly \(\binom{s_i}{2}+s_i=\binom{s_i+1}{2}\) ways. In that event the final size is \(1+s_i\). A seed in each of two distinct components \(i,j\) occurs in exactly \(s_i s_j\) ways and yields final size \(1+s_i+s_j\). These exhaustive, disjoint classes total \(\binom n2\) unordered pairs. This proves the generating function.

**3. The mean and concentration extremum.** Component \(i\) is hit by at least one seed with probability
\[
1-\frac{\binom{n-s_i}{2}}{\binom n2}
=\frac{s_i(2n-1-s_i)}{n(n-1)}.
\]
Linearity of expectation over component-hit indicators gives the displayed mean. Let \(f(s)=s^2(2n-1-s)/[n(n-1)]\). For two components of positive sizes \(a\ge b\), a real transfer \(t>0\) from the smaller component to the larger satisfies
\[
\frac{d}{dt}[f(a+t)+f(b-t)]
=\frac{(a-b+2t)[4n-2-3(a+b)]}{n(n-1)}>0
\]
while both sizes remain positive: since \(a+b\le n-1\), the second bracket is at least \(n+1\). Thus every unit transfer toward a more concentrated positive integer partition strictly increases the mean. Repeated transfers establish the unique extreme size multisets. The derivative argument does not claim that \(f\) is convex on its entire unconstrained one-variable range; only the feasible fixed-sum pair transfer is needed.

**4. The infinite same-degree, more-triangles, smaller-cascade family.** The peripheral path in \(G_n\) is connected, so step 1 makes \(X(G_n)=n\) for every pair. The periphery of \(Q_n\) has exactly two components, of sizes \(3\) and \(n-4\). The only way to fail to activate all vertices is for both seeds to be drawn from just one peripheral component, or for one seed to be the hub and the other to lie in just one component. Applying step 3, or averaging the two nonhit components directly, yields
\[
 n-\mathbb E X(Q_n)
=\frac{3(n-4)(n+1)}{n(n-1)}>0.
\]
Both peripheries contain \(n-2\) edges. Adding the hub gives \(2n-3\) total edges. Both have two peripheral vertices of degree one and \(n-3\) peripheral vertices of degree two; their hub has degree \(n-1\). Thus their *whole* degree multisets agree. Every peripheral edge creates a triangle through the hub; only \(Q_n\) contains the additional peripheral triangle from \(K_3\). Consequently their triangle counts are respectively \(n-2\) and \(n-1\). Their equal degree multisets also force equal connected-triple counts \(\sum_v\binom{\deg v}{2}\), establishing strict transitivity reversal.

**5. Sharpness at six vertices.** Enumerate all \(2^{\binom n2}\) labeled simple graphs on \(n=2,3,4,5\) vertices and discard disconnected graphs. For each connected graph compute its sorted degree multiset, the number of triangles, and its mean final size by simulating all \(\binom n2\) seed pairs with exact integer arithmetic, dividing by the number of pairs at the end. The connected counts are \(1,4,38,728\), respectively. At \(n=5\) the only same-degree classes with two different triangle counts have degree profiles \((1,2,2,2,3)\), where the zero- and one-triangle means are \(13/5\) and \(14/5\), and \((2,2,2,3,3)\), where the means are \(16/5\) and \(7/2\), respectively. All other degree groups at \(n\le5\) have a single triangle count. Hence none provides a strict increase in triangle count accompanied by a strict decrease in the mean. The full enumeration is finite and exhausts the defined class; the standalone verifier supplies replayable independent arithmetic paths for the final-size simulation and the component-law calculation.

For \(n=6\), \(G_6\) activates all six sites for every one of its 15 seed pairs. \(Q_6\) has the final-size frequencies \(X=3\) (3 pairs), \(X=4\) (6 pairs), \(X=6\) (6 pairs), hence mean \(23/5\). They have common degree profile \((2,2,3,3,3,5)\), but four and five triangles, respectively. This realizes the claimed first strict reversal.

## Verification

Run `python3 artifacts/verify_cone.py` with Python 3; no third-party libraries are required. `artifacts/verification_certificate.json` gives the expected exact output summary. The verifier enumerates all 33,866 peripheral simple graphs on two through six vertices and directly simulates 704,182 distinct cone seed-pair experiments, comparing their complete final-size histograms to the closed-form law and comparing means as reduced rationals. It separately enumerates *every* labeled connected graph of orders two through five, checking the claimed sharp threshold, and checks six members of the infinite family. The finite enumeration is exhaustive only in the expressly stated finite ranges; the proof in steps 1–4 establishes the general assertions for every allowed graph size.

## Relationship to prior work

Watts (2002) studies threshold-driven global social cascades on sparse random networks; the threshold there is a **fraction** of active neighbors, whereas the present problem uses an absolute threshold of two on fixed, hub-containing finite graphs. Centola and Macy (2007) show the importance of structural reinforcement in complex contagions and compare clustered and rewired social networks, but their seeding, network families and outcomes differ from the uniformly seeded finite cone law, and they do not imply the degree-preserving six-vertex sharp cutoff. Amini and Fountoulakis (2011 preprint) study bootstrap-percolation thresholds in random power-law graphs, not exact two-seed final distributions on arbitrary graph cones. Closely related finite threshold-diffusion optimization results study *minimum deliberately selected contagious seed sets*, rather than the final-size distribution under exactly two uniformly random seeds. These distinctions are comparisons of the mathematical statements and hypotheses, not a claim that searches establish universal uniqueness.

## Limitations

This is an idealized irreversible **absolute two-neighbor** adoption model with exactly two uniformly random distinct initial adopters and one universal hub in the main closed-form law. It does not cover fractional adoption thresholds, random individual transmission failures, time-varying links, nonlinear utilities, or an arbitrary number of seeds. Higher clustering is measured by the number of triangles (and therefore by global transitivity in the degree-matched family), not by every definition of local clustering. The strict counterexample is specific to connected finite simple graphs and mean final activation; it does not assert that triangles generally suppress contagion. Finite enumeration is used only for minimality through five vertices; no computer search proves an infinite assertion. Independent literature review may uncover an equivalent result under different terminology.

## References

1. Duncan J. Watts, “A simple model of global cascades on random networks,” *PNAS* 99 (2002), 5766–5771, DOI: 10.1073/pnas.082090499. Public date: 2002-04-30. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC122850/.
2. Damon Centola and Michael Macy, “Complex Contagions and the Weakness of Long Ties,” *American Journal of Sociology* 113 (2007), 702–734, DOI: 10.1086/521935. Open full text: https://ndg.asc.upenn.edu/wp-content/uploads/2016/04/Centola-Macy-2007-AJS.pdf.
3. Hamed Amini and Nikolaos Fountoulakis, “Bootstrap percolation in power-law random graphs,” arXiv:1111.1339 (first posted 2011-11-05), https://arxiv.org/abs/1111.1339.

# Exact parity bias for circular triads in uniform random tournaments

## Finding
For each integer \(n\ge3\), form a labeled random tournament by independently assigning the direction of each pair with probability one half. Let \(C_n\) denote the number of unordered vertex triples whose three arcs form a directed cycle. Set \(m=\binom n2\) and \(k=\lfloor(n-1)/2\rfloor\). Then
\[
\mathbb E[(-1)^{C_n}]=2^{-k},\qquad
\#\{C_n\text{ even}\}-\#\{C_n\text{ odd}\}=2^{m-k},
\]
and consequently
\[
\mathbb P(C_n\text{ even})=\frac{1+2^{-k}}2,\qquad
\mathbb P(C_n\text{ odd})=\frac{1-2^{-k}}2.
\]
These formulas hold for every order, not merely asymptotically. The positive bias is unchanged when passing from odd order \(2j+1\) to the next even order \(2j+2\).

## Assumptions and scope
The vertex set is \(\{1,\ldots,n\}\); its \(m\) unordered pairs receive independent, fair orientations. An unoriented three-element subset contributes one to \(C_n\) precisely if its three arcs form a directed cycle. No conditioning on score sequences, strong connectivity, or regularity is imposed. The same argument actually covers \(n=2\), when \(C_2=0\), but the theorem concerns the first nontrivial orders \(n\ge3\).

## Proof
Write \(d_v\) for the outdegree of vertex \(v\). Every transitive vertex triple has exactly one dominating vertex, whereas no cyclic triple has a vertex dominating the other two. Thus the *deterministic* identity
\[
C_n=\binom n3-\sum_{v=1}^{n}\binom{d_v}{2}
\]
holds for every tournament.

For every nonnegative integer \(d\), direct verification in the four residue classes modulo four gives
\[
(-1)^{\binom d2}=\frac{(1-i)i^d+(1+i)(-i)^d}{2}
 =\frac12\sum_{\varepsilon\in\{-1,1\}}(1-i\varepsilon)(i\varepsilon)^d.
\]
Apply this identity independently at each vertex. For a sign vector \(\varepsilon=(\varepsilon_v)_{v=1}^n\), the expectation of \(\prod_v(i\varepsilon_v)^{d_v}\) factors over the \(m\) independently oriented edges. A single edge between \(u\) and \(v\) contributes \((i\varepsilon_u+i\varepsilon_v)/2\). This factor vanishes whenever \(\varepsilon_u\ne\varepsilon_v\). Because the complete graph is connected, the only surviving sign vectors have all signs equal. It follows, with \(M=\binom n3\), that
\[
\begin{aligned}
\mathbb E[(-1)^{C_n}]
&=(-1)^M 2^{-n}\left[(1-i)^n i^m+(1+i)^n(-i)^m\right]\\
&=(-1)^M 2^{1-n/2}\cos\left(\frac{\pi n(n-2)}4\right).
\end{aligned}
\]
Here the second identity uses \(1\pm i=\sqrt2 e^{\pm i\pi/4}\) and \(m=\binom n2\). For even \(n\), the product of \((-1)^M\) and the cosine is \(1\); for odd \(n\), it is \(1/\sqrt2\). This follows directly by checking the residues \(n\bmod8\), noting the parity of \(\binom n3\). Hence both cases simplify to
\[
\mathbb E[(-1)^{C_n}]=2^{-\lfloor(n-1)/2\rfloor}.
\]
Finally, the expectation of \((-1)^{C_n}\) is the difference between the probabilities of even and odd \(C_n\), and these probabilities sum to one. There are exactly \(2^m\) equiprobable labeled tournaments, yielding the stated signed counts. This proves every claim. \(\square\)

## Verification
The included standalone `verify.py` uses only the Python standard library. It independently counts all directed 3-cycles in every labeled tournament on three, four, five, and six vertices and checks them against the outdegree identity and the proposed parity counts. The observed even/odd counts are respectively \((6,2)\), \((48,16)\), \((640,384)\), and \((20480,12288)\). A separate integer-Gaussian-arithmetic computation verifies the intermediate roots-of-unity expression against the closed bias for every integer order from two through one hundred. These finite checks supplement, but do not replace, the unrestricted proof above.

To reproduce, run `python3 verify.py` in the directory containing that file. It prints `VERIFY_OK` on success.

## Relationship to prior work
Circular-triad counting and the associated paired-comparison consistency coefficient originate in Kendall and Babington Smith (1940), whose first four moments are described by Chatterjee and Bhattacharya (2026, introduction). These polynomial moment identities do not determine parity of a count with order-dependent unbounded support. Andersson (1998) studies asymptotic distributions of subgraph counts, and Komarov and Mackey (2014) study counts of five-cycles; neither supplies the present exact parity-bias statement. Harris and McShane (2024) derive generating functions for tournaments with a *fixed specified number* of circular triads, with explicit sequences for counts from zero to fourteen; their finite-count expansions do not establish an all-order signed sum over every possible count. Chatterjee and Bhattacharya (2026) study three asymptotic fluctuation regimes for general inhomogeneous tournaments, but no finite-order parity law is stated in the sections inspected. The exact alternating sum is obtained here by a separate roots-of-unity cancellation.

## Limitations
The theorem applies to independent fair directions on complete graphs, not biased or latent-variable tournament models. It gives the parity marginal, not the full circular-triad distribution or independence from another statistic. No claim is made that the parity law is new beyond the sources compared: especially the full original 1940 article could not be inspected through the available access route; its potential undiscovered discussion of signed counts is a residual historical-priority risk. The result has not undergone independent validation.

## References
- M. G. Kendall and B. Babington Smith, *On the Method of Paired Comparisons*, Biometrika **31** (1940), 324–345. DOI: 10.1093/biomet/31.3-4.324.
- P. Andersson, *On the Asymptotic Distributions of Subgraph Counts in a Random Tournament*, Random Structures & Algorithms **13** (1998), 249–260. DOI: 10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V.
- N. Komarov and J. Mackey, *On the Number of 5-Cycles in a Tournament*, arXiv:1410.6828 (first submitted 2014-10-24).
- I. R. Harris and R. P. A. McShane, *Counting Tournaments with a Specified Number of Circular Triads*, Journal of Integer Sequences **27** (2024), Article 24.8.7. https://cs.uwaterloo.ca/journals/JIS/VOL27/McShane/mcshane1.pdf.
- S. Chatterjee and B. B. Bhattacharya, *Transitivity in Inhomogeneous Random Tournaments*, arXiv:2606.02340v1 (2026), especially Introduction and Section 2.

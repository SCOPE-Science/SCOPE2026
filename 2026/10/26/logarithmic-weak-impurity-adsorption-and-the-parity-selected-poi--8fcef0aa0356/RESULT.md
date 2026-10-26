# Logarithmic weak-impurity adsorption and the parity-selected Poisson-binomial jamming law

## Finding

Let \(r\ge2\) be fixed. Start from a graph with \(n\) vertices, of which \(n-r\) form a complete graph, while the remaining \(r\) *impurity* vertices are mutually nonadjacent and each connects to every ordinary vertex. Every ordinary–ordinary edge has an independent rate-one Poisson dimer-attempt process. Every edge from impurity \(i\) to an ordinary vertex has attempt rate \(c_i/\log n\), where \(c_i>0\) is fixed. An attempt succeeds exactly when both endpoints are vacant; accepted dimers remain permanently.

Let \(R_n\subseteq\{1,\ldots,r\}\) denote the labels of impurity vertices left vacant at jamming, and let \(W_n\in\{0,1\}\) be the number of vacant ordinary vertices. For any sequence of \(n\to\infty\) of fixed parity, their joint law converges in total variation to the following explicit finite experiment:

First, independently retain each impurity \(i\) in a set \(S\) with probability \(p_i=e^{-c_i}\). Put \(q=|S|\). When \(n+q\) is even, the output is \((R,W)=(S,0)\). When \(n+q\) is odd and \(q=0\), the output is \((\varnothing,1)\). When \(n+q\) is odd and \(q>0\), select \(I\in S\) with probability \(c_I/\sum_{j\in S}c_j\) and output \((S\setminus\{I\},0)\). This is a parity-selected, labeled Poisson-binomial law, rather than a homogeneous Poisson vacancy count.

For exactly two impurities and even \(n\ge4\), a stronger **finite-size identity** holds for any positive impurity-edge rates \(\lambda_1,\lambda_2\):

\[
\Pr(W_n+|R_n|=2)
=\prod_{j=1}^{(n-2)/2}\frac{2j-1}{2j-1+2(\lambda_1+\lambda_2)}.
\]

In the weak-rate scaling \(\lambda_i=c_i/\log n\), this probability tends to \(e^{-(c_1+c_2)}\). Thus even networks attain complete coverage with limiting probability \(1-e^{-(c_1+c_2)}\). For odd networks with two impurities, exactly one vertex remains vacant, and its limiting probabilities are

\[
\begin{aligned}
\Pr(\text{ordinary vacancy})&=(1-e^{-c_1})(1-e^{-c_2}),\\
\Pr(\text{impurity 1 vacancy})&=e^{-c_1}(1-e^{-c_2})+e^{-(c_1+c_2)}\frac{c_2}{c_1+c_2},\\
\Pr(\text{impurity 2 vacancy})&=e^{-c_2}(1-e^{-c_1})+e^{-(c_1+c_2)}\frac{c_1}{c_1+c_2}.
\end{aligned}
\]

## Assumptions and scope

Here \(n\) is an integer at least \(r+2\), \(r\) and all \(c_i>0\) stay fixed while \(n\to\infty\); the two parity subsequences are treated separately. Graph edges have independent homogeneous-in-time exponential attempt clocks with the rates specified above. Adsorption is irreversible, and no edges join two impurities. The finite two-impurity product holds for arbitrary fixed positive \(\lambda_i\), without a weak-rate hypothesis. The joint limit concerns the terminal **labels** and the ordinary vacancy indicator, not merely the number of deposited dimers or coverage density.

The choice \(1/\log n\) is a transition scale: for common impurity rate \(a_i\varepsilon_n\) with fixed \(a_i>0\) and \(\varepsilon_n\to0\), all impurities are captured during the bulk adsorption stage with probability tending to one when \(\varepsilon_n\log n\to\infty\), and none are captured during that stage with probability tending to one when \(\varepsilon_n\log n\to0\). In the latter case a possible final solitary ordinary vertex still forces exactly one terminal impurity capture. These limiting regimes follow from the same exposure proof; no claim of a finite-size uniform error bound is made.

## Proof

**1. Reduced Markov chain and parity.** Write \(k\) for the number of vacant ordinary vertices and \(A\subseteq\{1,\ldots,r\}\) for the set of vacant impurities. The total successful-deposition rate is

\[
D(k,A)=\frac{k(k-1)}2+k\sum_{i\in A}\lambda_{i,n}.
\]

An ordinary–ordinary deposition takes \((k,A)\) to \((k-2,A)\) at rate \(k(k-1)/2\); a deposition using impurity \(i\) takes it to \((k-1,A\setminus\{i\})\) at rate \(k\lambda_{i,n}\). Every transition removes precisely two vertices. From any state with \(k\ge2\), an ordinary edge is available. At \(k=1\), precisely one impurity is captured if any remain, chosen proportionally to the \(\lambda_{i,n}\); otherwise the ordinary vertex stays vacant. At \(k=0\), all remaining impurities are isolated. These observations already identify the terminal parity correction once the identities of the bulk-surviving impurities are known.

**2. Concentration of the ordinary-site exposure.** Put \(K_n=\lceil(\log n)^2\rceil\) and let \(\tau_n\) be the first time \(k\le K_n\). Define the accumulated site exposure

\[
E_n=\int_0^{\tau_n} k(t)\,dt.
\]

At each visited level \(k>K_n\), conditional on the present impurity set, the expected contribution \(k\Delta t\) of that holding interval is

\[
\frac{2}{k-1+2\sum_{i\in A}\lambda_{i,n}},
\]

and its conditional variance is the square of this quantity. At most \(r\) transitions lower \(k\) by one; all others lower it by two. Comparing the resulting mesh with \(\int_{K_n}^{n-r}du/u\), and using \(\sum_i\lambda_{i,n}=O(1/\log n)\), gives, uniformly over the possible visited levels,

\[
\sum_{\text{visited }k>K_n}\frac{2}{k-1+2\sum_{i\in A_k}\lambda_{i,n}}
=\log\frac{n-r}{K_n}+O_r(K_n^{-1}).
\]

The martingale of centered holding contributions has total conditional variance bounded by \(4\sum_{k>K_n}(k-1)^{-2}=O(K_n^{-1})\). Therefore \(E_n=\log(n/K_n)+o_{\Pr}(1)\) and, in particular,

\[
E_n/\log n\xrightarrow{\Pr}1.
\]

**3. Independent one-shot capture limits.** For each impurity choose independently a unit exponential threshold \(\xi_i\), and fire its first successful edge when its integrated hazard \(\lambda_{i,n}\int k(t)dt\) reaches \(\xi_i\), provided that impurity is still vacant. This is the standard independent exponential-clock construction and is valid even though the ordinary-site process responds to impurity captures. Impurity \(i\) is captured by \(\tau_n\) if and only if \(\xi_i\le\lambda_{i,n}E_n\). Since \(\lambda_{i,n}=c_i/\log n\), the joint indicators converge under this coupling to \(\mathbf1_{\{\xi_i\le c_i\}}\), with no threshold ties almost surely. Consequently the bulk-surviving set converges jointly to independent Bernoulli survival indicators of probabilities \(e^{-c_i}\).

**4. No intermediate late captures.** For \(2\le k\le K_n\), the chance that the next successful dimer uses an impurity, conditional on any current impurity set, is at most \(2\sum_i\lambda_{i,n}/(k-1)\). Each level \(k\) can be visited at most once, hence a union bound yields

\[
\Pr(\text{any impurity capture at }2\le k\le K_n)
\le\frac{2\sum_i c_i}{\log n}\sum_{j=1}^{K_n-1}\frac1j
=O_{\mathbf c}\!\left(\frac{\log\log n}{\log n}\right)\longrightarrow0.
\]

Ordinary–ordinary dimers therefore reduce \(k\) to zero or one, except on an event of vanishing probability. If \(q\) impurities survive the bulk and \(r-q\) have already been captured, the remaining ordinary count has parity \(n-r-(r-q)\equiv n+q\pmod2\). The \(k=1\) rule in step 1 gives exactly the stated size-biased deletion and the possible ordinary vacancy. Since there are only finitely many terminal states, the coupled convergence gives total-variation convergence.

**5. Exact two-impurity identity.** With \(r=2\) and even \(n\), precisely two impurities remain vacant if and only if no impurity is ever matched. Conditional on this event still being possible, normal vacancies decrease through \(n-2,n-4,\ldots,2\). At the stage with \(k=2j\), the probability of choosing an ordinary edge rather than either impurity edge is \((2j-1)/(2j-1+2(\lambda_1+\lambda_2))\). Multiplication gives the exact product. With \(\lambda_i=c_i/\log n\), the logarithm of the product is \(-(\lambda_1+\lambda_2)\log n+o(1)\), giving \(e^{-(c_1+c_2)}\). Substituting the four possibilities for two independent Bernoulli bulk survivors yields the three odd-size vacancy probabilities.

## Verification

The accompanying standalone \`verify.py\` compares the reduced Markov chain against an independently implemented labeled-graph rate recursion using exact rational arithmetic; checks the exact even-size product for two impurities; and compares finite-size numerical distributions with the explicit limiting law. The program completed 72 grouped assertions (24 labeled/reduced, 30 product/support, 18 finite-size consistency). The asymptotic statement is established by the proof above, not by the finite computations.

## Relationship to prior work

The random-greedy matching setup follows the weighted-edge framework of Miller and Pritikin (1997). Their cited work focuses on worst-case matching-size performance, whereas the present object is a fixed number of labeled, one-shot impurity sites in a dense reactive clique at vanishing edge rates, with an exact terminal joint law. Bennett and Bohman (2012) study nearly perfect greedy matching in regular hypergraphs with low codegrees, not this heterogeneous high-degree impurity model. Dhara, van Leeuwaarden, and Mukherjee (2016) analyze vertex-activation adsorption on sparse Erdős–Rényi graphs, again with different dynamics and observables. The homogeneous complete-graph monomer–dimer process has a parity-corrected **Poisson** limit: it does not imply the present capped, impurity-labeled Bernoulli law or the terminal size-biased selection. No exhaustive priority claim is made.

## Limitations

The theorem assumes a fixed finite number of impurities, equal ordinary-edge rates, strictly positive fixed impurity rate coefficients, no impurity–impurity edges, and the particular logarithmic weak-coupling regime. The labels of already matched ordinary vertices are not analyzed, and the result does not address physical-time adsorption durations or growing numbers of impurities. A relevant earlier paper on weighted random greedy matching could be examined only at the abstract level, so unrecognized broader coverage remains a historical-priority risk.

## References

1. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581, first posted 2012-10-12. https://arxiv.org/abs/1210.3581
2. S. Dhara, J. S. H. van Leeuwaarden, and D. Mukherjee, *Generalized random sequential adsorption on Erdős–Rényi random graphs*, arXiv:1604.03918, first posted 2016-04-13. https://arxiv.org/abs/1604.03918
3. Z. Miller and D. Pritikin, *On randomized greedy matchings*, Random Structures & Algorithms 10 (1997), 353–383. DOI:10.1002/(SICI)1098-2418(199705)10:3<353::AID-RSA5>3.0.CO;2-V.
4. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401. DOI:10.1137/0402034.

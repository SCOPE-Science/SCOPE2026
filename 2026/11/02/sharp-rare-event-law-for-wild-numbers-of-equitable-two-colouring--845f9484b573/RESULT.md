# Sharp rare-event law for wild numbers of equitable two-colourings of complete graphs

## Finding

Fix an integer \(n\geq4\). Choose uniformly among the equitable, surjective, labelled red–blue edge-colourings of the complete graph \(K_n\): the two colour classes have sizes differing by at most one. Let \(W_n\) be the *wild number*: the minimum number of edges whose designation as wild makes both spanning monochromatic graphs connected when every wild edge is available to both colours. Write
\[
N=\binom n2,\qquad m=\left\lfloor\frac N2\right\rfloor,\qquad d=n-1,
\qquad p_n=n\frac{(m)_d+(N-m)_d}{(N)_d},
\]
where \((a)_d=a(a-1)\cdots(a-d+1)\), taken as zero when \(d>a\) for nonnegative integers \(a\).

**Theorem.** As \(n\to\infty\), the expectation and the entire positive-wild-number rare-event regime obey
\[
\begin{aligned}
\mathbb E[W_n]&=p_n+O(n^2 4^{-n}),\\
\Pr(W_n=1)&=p_n+O(n^2 4^{-n}),\\
\Pr(W_n\geq2)&=O(n^2 4^{-n}),\\
\Pr(W_n=0)&=1-p_n+O(n^2 4^{-n}),
\end{aligned}
\]
and
\[
\boxed{\quad p_n=\frac{4}{e}\,n2^{-n}\bigl(1+O(n^{-1})\bigr).\quad}
\]
The constants implied by the big-O terms are absolute. Consequently, conditional on \(W_n>0\), with probability tending to one there is exactly **one vertex isolated in exactly one colour**, while the complementary colour and the remaining vertices of the disconnected colour each form connected graphs. In particular, conditional on failure to have a spanning tree in each colour, exactly one wild edge suffices with probability tending to one.

The sharp factor \(e^{-1}\) differs from the independent fair-edge model: conditioning on near-half colour-class sizes suppresses a prescribed monochromatic-isolate event by an asymptotic factor \(e^{-1}\).

## Assumptions and scope

The graph is the simple labelled complete graph \(K_n\). Colours are named red and blue; neither proper edge colouring nor balance at individual vertices is assumed. *Equitable* means exactly the global constraint \(\bigl||E_{\rm red}|-|E_{\rm blue}|\bigr|\leq1\). Every such labelled colouring is equally likely. If \(N\) is odd, each orientation of the two possible colour-class sizes is equally likely, and exchanging the colour names leaves \(W_n\) invariant. It therefore suffices to expose a uniformly random red edge set of size \(m\), with its complement blue.

Both monochromatic spanning graphs have positive edge count for \(n\ge4\). A connected component is understood to include isolated vertices. The symbol \(O(\cdot)\) refers to uniform asymptotic bounds as \(n\) tends to infinity; no assertion of exact equality with the leading term is made for finite \(n\).

## Proof

**1. Component reduction.** For an arbitrary two-edge-coloured graph, the known two-colour wild-number identity is
\[
W_n=(\kappa(G_{\rm red})-1)+(\kappa(G_{\rm blue})-1),
\]
where \(\kappa\) is the number of components of a spanning subgraph. The two graphs here are complements, so at least one is connected. This identity is a previously established result, not a new lemma.

For each colour \(c\), let \(I_c\) denote the number of isolated vertices and \(J_c\geq1\) the number of connected components containing an edge. Then \(\kappa(G_c)-1=I_c+J_c-1\). Define \(I=I_{\rm red}+I_{\rm blue}\). It follows that
\[
W_n=I+(J_{\rm red}-1)+(J_{\rm blue}-1),
\]
with every summand nonnegative. If \(J_c\geq2\), at least \(J_c-1\) of its nontrivial components have between \(2\) and \(\lfloor n/2\rfloor\) vertices. Thus \(W_n-I\) is bounded by the total number of such small nontrivial components, counted in both colour classes.

**2. Uniform probability of a disconnected vertex subset.** A fixed set of \(t\) edges is absent from a uniformly chosen edge class of size \(a\) with probability
\[
\frac{(N-a)_t}{(N)_t};
\]
zero is assigned when the number of required absent edges exceeds the number available. Here \(a\) is either \(m\) or \(N-m\). Since \(\max\{m,N-m\}=\lceil N/2\rceil\), for every \(0\leq t\leq N\),
\[
\frac{(N-a)_t}{(N)_t}
\leq\left(\frac{\lceil N/2\rceil}{N}\right)^t
\leq e\,2^{-t}.
\]
Indeed, \(\lceil N/2\rceil/N\leq(1+1/N)/2\) and \((1+1/N)^t\leq e\).

For a prescribed vertex subset \(S\) of cardinality \(k\), an entire monochromatic component can be contained in \(S\) only if the \(k(n-k)\) edges crossing \(S\) are absent in that colour. Define
\[
R_n=\sum_{k=2}^{\lfloor n/2\rfloor}\binom nk2^{-k(n-k)}.
\]
The cut bound gives
\[
0\leq \mathbb E[W_n-I]\leq 2eR_n.
\]
We verify \(R_n=O(n^2 4^{-n})\). The term \(k=2\) is \(\binom n2 2^{-2(n-2)}\). For \(3\leq k\leq n/2\), the exact identity
\[
k(n-k)=2(n-2)+(k-2)(n-k-2)
\]
and \(n-k-2\geq n/2-2\) imply
\[
\sum_{k=3}^{\lfloor n/2\rfloor}\binom nk2^{-k(n-k)}
\leq n^2 2^{-2(n-2)}\sum_{j\geq1}\left(n2^{-n/2+2}\right)^j.
\]
For all sufficiently large \(n\), the geometric series has bounded sum; the finitely many smaller \(n\) are absorbed into the absolute constant. This proves \(R_n=O(n^2 4^{-n})\) and therefore
\[
\mathbb E[W_n]=\mathbb E[I]+O(n^2 4^{-n}).
\]

**3. Exact singleton contribution and overlap control.** A prescribed vertex is isolated in red exactly when its \(d=n-1\) incident edges are all blue. The probability is \((N-m)_d/(N)_d\). Its probability of being isolated in blue is \((m)_d/(N)_d\). Linearity of expectation gives the *exact* identity
\[
\mathbb E[I]=n\frac{(N-m)_d+(m)_d}{(N)_d}=p_n.
\]
Two distinct vertices cannot be isolated in opposite colours: the edge joining them would have to receive both colours. The same vertex cannot be isolated in both colours. Two vertices both isolated in one colour require \(2n-3\) specified edges to be absent in that colour. By the preceding bound and a union bound,
\[
\Pr(I\geq2)=O\!\left(n^2 2^{-(2n-3)}\right)=O(n^2 4^{-n}).
\]
Let \(B\) be the event that either colour has a nontrivial connected component of size at most \(n/2\), *and* at least one other nontrivial component. The cut bound gives \(\Pr(B)\leq2eR_n=O(n^2 4^{-n})\). Outside \(B\), each colour has exactly one nontrivial component, so \(W_n=I\). Outside \(B\cup\{I\geq2\}\), the wild number equals zero or one according to whether there is a single isolated vertex. Since \(0\leq\mathbb E[I]-\Pr(I\geq1)\leq\mathbb E[I(I-1)]\), the same pair-isolation estimate also yields \(\Pr(I\geq1)=p_n+O(n^2 4^{-n})\). Combining these facts proves all four claimed expectation and probability error bounds. It also proves that a nonzero wild number is asymptotically caused by one monochromatically isolated vertex, with no other components outside the giant connected remainder.

**4. Leading constant.** For either \(a\in\{m,N-m\}\), write \(a=N/2+O(1)\). The falling-factorial ratio satisfies
\[
\begin{aligned}
\log\frac{(a)_d}{(N)_d}
&=-d\log2-\frac{d(d-1)}{2N}+O(n^{-1})\\
&=-d\log2-1+O(n^{-1}),
\end{aligned}
\]
because \(d=n-1\), \(N=n(n-1)/2\), and the sum of quadratic Taylor remainders is \(O(d^3/N^2)=O(n^{-1})\). The \(O(1)\) parity displacement of \(a\) contributes only \(O(d/N)=O(n^{-1})\). Therefore
\[
\frac{(a)_d}{(N)_d}=e^{-1}2^{-(n-1)}\bigl(1+O(n^{-1})\bigr)
\]
for both choices of \(a\), giving \(p_n=(4/e)n2^{-n}(1+O(n^{-1}))\). Finally, the probability of the error event is \(O(n^2 4^{-n})=o(n2^{-n})\), establishing the asserted conditional conclusions.

## Verification

The standalone Python 3 standard-library program `verify.py` exhaustively enumerates all uniform \(m\)-edge red sets for \(n=4,5,6,7\), evaluates both monochromatic component counts, and confirms the exact distributions:
\[
\begin{array}{c|ccc}
n&\#(W=0)&\#(W=1)&\#(W=2)\\\hline
4&12&8&0\\
5&192&60&0\\
6&5430&1005&0\\
7&321930&30765&21
\end{array}
\]
The number of inspected red sets is \(359423\). The program independently counts isolated monochromatic vertices in every case and compares their exact rational expectation to \(p_n\). It also computes finite numerical convergence diagnostics for the leading factor at \(n=16,32,64,128,256\). On replay, the output is:

`VERIFY_OK exhaustive_colorings=359423 dimensions=4..7 exact_isolate_identities=4 numerical_ratio_cases=5`

The infinite error estimates and asymptotic constant follow from the displayed proof, not from the finite tests.

## Relationship to prior work

Dawkins, Nappo, Tong and Zimbizi establish the component identity and show only \(\mathbb E[W_n]\to0\) for uniformly random equitable two-colourings of \(K_n\); see their Section 3.2.1. The present theorem identifies the sharp coefficient \(4/e\), gives the first exponentially smaller error relative to the exact singleton term \(p_n\), and classifies the dominant rare event.

Bender, Canfield and McKay's 1990 enumeration of connected graphs with prescribed edge count gives a classical broader fixed-edge random-graph framework. Their printed Corollary 3 is a **relative** estimate for the overwhelming connected-graph count, so it does not determine the exponentially small disconnection probability, its prefactor, or the two-complement-colour wild-number distribution established here. Classical independent-edge connectivity bounds, such as those cited in the 2026 paper, are also not interchangeable with fixed-edge balance: the leading constant changes by \(e^{-1}\). The fixed-edge isolated-vertex mechanism itself is standard and is not claimed as a newly invented random-graph principle.

## Limitations

The probability law assumes a uniformly random *globally equitable* assignment of two named colours to the edges of a complete graph. It is not a result for proper edge-colourings, vertexwise regular colour degrees, arbitrary colour proportions, incomplete host graphs, or more than two colours. The error terms are asymptotic and are not supplied with optimized explicit finite-\(n\) constants. While the most directly relevant accessible primary works were compared, independent assessment and comprehensive historical-priority verification are not claimed.

## References

1. A. Dawkins, A. Nappo, J. Tong and C. Zimbizi, *Wild number for spanning trees in complete and complete bipartite graphs*, arXiv:2610.22142v1 (first publicly posted 2026-10-15), especially Section 2 and Section 3.2.1. https://arxiv.org/html/2610.22142
2. E. A. Bender, E. R. Canfield and B. D. McKay, *The asymptotic number of labeled connected graphs with a given number of vertices and edges*, Random Structures & Algorithms **1** (1990), 127–169, Theorem 1 and Corollary 3. https://users.cecs.anu.edu.au/~bdm/papers/BCM_Connected1.pdf
3. E. A. Bender, E. R. Canfield and B. D. McKay, *Asymptotic properties of labeled connected graphs*, Random Structures & Algorithms **3** (1992), 183–202. https://doi.org/10.1002/rsa.3240030208

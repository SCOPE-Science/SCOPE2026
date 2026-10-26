# Antipodal delay and the extremal schedule count for sequential Rule 254 on cycles

## Finding

For each integer \(n\ge3\), let \(C_n\) be the labeled cyclic graph with vertices \(0,\ldots,n-1\). Fix a permutation \(\pi\) of the vertices and update them one at a time in that order, using the three-site OR rule
\[
x_i\longleftarrow x_{i-1}\lor x_i\lor x_{i+1} \qquad(i\bmod n).
\]
A complete visit is one *sweep*, whose map is \(F_\pi\). For every nonzero binary state \(x\), let \(\tau_\pi(x)\) be its first sweep number at the all-one state, and define \(T(\pi)=\max_{x\ne0}\tau_\pi(x)\).

**Theorem.** For every \(n\ge3\),
\[
\max_{\pi}T(\pi)=\left\lfloor\frac n2\right\rfloor.
\]
For each even \(n=2m\ge6\), exactly
\[
n^2\binom{n-2}{m-1}
\]
of the \(n!\) labeled permutation sweeps attain \(T(\pi)=m\). Therefore for a uniformly random permutation sweep,
\[
\Pr\{T(\pi)=m\}=\frac{n}{(n-1)((m-1)!)^2}.
\]
For \(n=4\), all \(24\) orders attain the maximum \(2\).

More precisely, let \(\rho(i)\in\{1,\ldots,n\}\) be the position of vertex \(i\) in \(\pi\). For even \(n=2m\), a given source \(s\) requires exactly \(m\) sweeps if and only if the ranks strictly decrease along both paths from its two neighbors to its antipode \(s+m\):
\[
\rho(s+1)>\rho(s+2)>\cdots>\rho(s+m),\qquad
\rho(s-1)>\rho(s-2)>\cdots>\rho(s-m).
\]
For \(n\ge6\) at most one source has this property. Here all vertex arithmetic is modulo \(n\).

## Assumptions and scope

Updates occur sequentially with immediate use of changed values. The same fixed permutation is repeated in every sweep. The three-site Boolean OR local rule is elementary cellular automaton Rule 254 under Wolfram's binary convention. The two uniform configurations are fixed; the zero state is excluded from \(T\), since it does not converge to the one state. Configurations and schedules are labeled, not identified under rotation or reflection. All quantifiers concern every integer ring size and every permutation order in the stated ranges; no randomness assumption is needed for the counting theorem.

## Proof

**1. The singleton reduction and path-clock lemma.** Coordinatewise OR is monotone and commutes with Boolean union, and the same is true of the sweep map and its iterates. Thus the time for any nonzero initial set to fill the ring is no greater than the time for each singleton that it contains. Consequently, the maximum over all nonzero initial states equals the maximum over singleton seeds.

Fix an initially occupied source \(s\) and a simple path \(s=v_0,v_1,\ldots,v_\ell=t\) of adjacent vertices. The earliest sweep in which infection can travel through this ordered path and reach \(t\) is
\[
1+\sum_{j=1}^{\ell-1}\mathbf1_{\{\rho(v_{j+1})<\rho(v_j)\}}.
\]
Indeed the first neighbor of the initially occupied source is infected during the first sweep, regardless of the source's rank. Each successive neighbor is infected in the *same* sweep precisely if it is updated later than the preceding newly infected neighbor; otherwise it waits until the next sweep. This is an induction on path length. Conversely, trace any first-infection event backward to an already infected neighboring vertex. Lexicographic sweep/update chronology strictly decreases along the backward chain, so it contains no repeated vertex; on a cycle such a chain follows one of the two simple arcs. The actual first-infection time of a vertex is therefore the minimum of the displayed costs for the two arcs joining source and target. In particular this time is at most the shorter arc length, and every singleton fills the ring within \(\lfloor n/2\rfloor\) sweeps.

**2. Sharpness at every size.** Choose a source \(s\) and a vertex \(t\) at cyclic distance \(\lfloor n/2\rfloor\). Arrange the ranks strictly decreasing on both arcs directed from \(s\) toward \(t\), with \(t\) ranked first and \(s\) ranked arbitrarily. The interior vertices of the two arcs form disjoint chains and can be interleaved, so the requirements are compatible. The short arc needs precisely \(\lfloor n/2\rfloor\) sweeps, and the other arc needs at least this many. Thus \(T(\pi)\) reaches the universal upper bound.

**3. Exact extremal characterization for even rings.** Write \(n=2m\). A vertex can first be reached in sweep \(m\) only if it is at graph distance \(m\) from the singleton source, hence is the unique antipode. Both arcs then have \(m\) edges. The path-clock formula equals \(m\) on each precisely when all \(m-1\) rank comparisons after the first edge are descents. This is exactly the pair of displayed strict chains. The antipode has lower rank than all other vertices except possibly the source.

**4. Count for a fixed source.** For fixed \(s\), the two chains share only their final vertex \(t=s+m\), which must have the smallest rank among the other \(n-1\) vertices. The remaining \(n-2\) vertices split into two chains, each with \(m-1\) vertices. There are \(\binom{n-2}{m-1}\) interleavings preserving these two orders. Insert the source into any of \(n\) positions: exactly \(n\binom{n-2}{m-1}\) orders witness that particular source.

**5. Distinct sources do not overlap for \(m\ge3\).** Suppose distinct sources \(s,u\) both witness the extremal time; write their antipodes \(t=s+m\) and \(v=u+m\). Each antipode must have the smallest rank among all vertices other than its own source. As the antipodes are distinct, they have ranks \(1\) and \(2\). Assume \(\rho(t)=1\) and \(\rho(v)=2\). The rank-one vertex \(t\) must equal the other source \(u\), else the minimality of \(v\) among vertices other than \(u\) fails. Hence \(u=t\) and \(v=s\). But the strict rank chain from \(s\) to \(t\) gives \(\rho(s+1)>\rho(s+2)\), while the reverse strict chain from \(t\) to \(s\) gives \(\rho(s+2)>\rho(s+1)\), a contradiction when \(m\ge3\). Thus the \(n\) witness-source sets are disjoint and their total cardinality is \(n^2\binom{n-2}{m-1}\).

For \(n=4\), choose the globally lowest-rank vertex \(t\). Its antipodal source \(s\) witnesses the required descents along the two length-two arcs. Therefore all \(4!=24\) orders are extremal, without a uniqueness claim. Dividing the even-ring count by \(n!\) and simplifying gives the stated probability.

## Verification

Compile the accompanying independent brute-force implementation using `c++ -std=c++17 -O2 verify.cpp -o verify` and execute `./verify`. It enumerates every update order for rings of size \(3\) through \(10\) and every singleton source; for sizes \(3\) through \(7\), it additionally enumerates every initial binary state, checking the singleton reduction. For even rings, it tests the exact extremal schedule count and uniqueness of extremal witnesses. The completed run reported `VERIFY_OK permutations=4037910 singleton_tests=39916794 all_state_tests=695472`, including extremal counts \(216\), \(1280\) and \(7000\) at sizes \(6\), \(8\), \(10\). The proof, not finite computation, establishes all-size claims.

## Relationship to prior work

The asynchronous-update framework, finite-ring setting, and eventual qualitative dynamics of elementary rules are developed by Macauley, McCammond and Mortveit in *Order Independence in Asynchronous Cellular Automata* (2007, arXiv:0707.2360); their Rule 128 duality analysis is relevant to Rule 254's limiting states. Their later *Dynamics Groups of Asynchronous Cellular Automata* (2008, arXiv:0808.1238) treats periodic points and dynamics groups, including the Rule 128/254 duality. The present theorem instead gives sharp **sweep-by-sweep transients** and an exact labeled schedule census, neither supplied by those results. General synchronous/asynchronous update comparisons do not determine this extremal count. Prior-result equivalence under rule complementation has been considered: complementing Rule 254 gives Rule 128, but does not produce the claimed latency census from the existing periodic-state classifications.

## Limitations

The count concerns even rings with a *fixed permutation repeated at every sweep* and maximal transient over nonzero initial states; it is not a distribution of settling times across all states or across arbitrary time-dependent schedules. The theorem does not enumerate every intermediate transient value. The stochastic statement randomizes the permutation once, not at every sweep. Literature searches and inspection of the nearest primary papers cannot certify absolute historical priority; combinatorial scheduling literature may contain an equivalent count. No independent audit has been performed.

## References

1. M. Macauley, J. McCammond, H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360 (first available 2007-07-16).
2. M. Macauley, J. McCammond, H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238 (2008).
3. B. Schönfisch and A. de Roos, *Synchronous and asynchronous updating in cellular automata*, Biosystems 51 (1999), 123–143 (background only; abstract consulted).

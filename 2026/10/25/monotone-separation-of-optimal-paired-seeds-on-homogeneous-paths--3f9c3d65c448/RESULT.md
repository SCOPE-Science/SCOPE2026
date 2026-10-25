# Monotone separation of optimal paired seeds on homogeneous paths

## Finding

**Theorem (complete two-seed phase diagram).** Fix an integer \(n\ge 2\). On the undirected path \(P_n\), place two distinct initially active seeds. Each edge independently transmits activation with the same probability \(0<p<1\); maximize the expected number of eventually active vertices. If the seed distance is \(b\), and \(a\) and \(c\) are the numbers of vertices outside the seed interval to its left and right, respectively, then \(a+b+c=n-1\), and
\[
F_{n,p}(a,b,c)=2+\sum_{j=1}^{a}p^j+\sum_{j=1}^{c}p^j+2\sum_{j=1}^{b-1}p^j-(b-1)p^b.
\]
For every fixed \(b\), the optimum has tails \(\{a,c\}=\{\lfloor(n-1-b)/2\rfloor,\lceil(n-1-b)/2\rceil\}\); these are the only optimal placements at that distance, up to reflection. Set \(N=n-1\) and \(b_0=\lceil(n+1)/3\rceil\). For each \(b_0\le b<N\), define \(h_b=\lceil(N-b)/2\rceil\) and let \(\theta_b\in(0,1)\) be the unique root of
\[
p^{b-h_b}[1+b(1-p)]=1.
\]
Then \(0<\theta_{b_0}<\theta_{b_0+1}<\cdots<\theta_{N-1}<1\). As \(p\) increases from zero to one, the globally optimal seed distance visits successively **every** integer \(b_0,b_0+1,\ldots,N\), moving forward at exactly these thresholds and never backward. Between thresholds the optimal distance is unique; at a threshold precisely two consecutive distances maximize expectation. When \(b_0=N\), there is no transition. The smallest path with a nontrivial transition is \(P_4\), at \(p=1/2\).

## Assumptions and scope

The graph has labeled vertices \(0,1,\ldots,n-1\) in path order. The two seeds are distinct, fixed in advance, and active with certainty. All edges are undirected and independently live with the same probability \(p\); eventual activation is the union of the live-edge connected components containing either seed. Equivalently, activation traverses any open path from either seed. The optimization is over all unordered pairs of vertices, without costs or constraints other than selecting exactly two. Statements hold for every integer \(n\ge2\) and real \(p\in(0,1)\). At \(p=0\), every two-seed pair has expected spread two; at \(p=1\), every pair reaches all vertices, so the endpoint nonuniqueness is deliberately excluded.

## Proof

**1. Exact influence polynomial.** Write the seed locations \(u<v\), with \(a=u\), \(b=v-u\), and \(c=n-1-v\). A vertex at distance \(j\) outside the two-seed interval is reached with probability \(p^j\). For an interior vertex at distance \(j\) from \(u\), its two routes to seeds are edge-disjoint, so inclusion–exclusion gives activation probability \(p^j+p^{b-j}-p^b\). Summing the two seeds, the two tails, and the \(b-1\) interior vertices yields the displayed formula. This derivation is exact for every \(p\), not an asymptotic approximation.

**2. Fixed-gap balancing.** For fixed \(b\), only \(\sum_{j=1}^{a}p^j+\sum_{j=1}^{c}p^j\) depends on the tail split. If \(c\ge a+2\), transferring one vertex from the longer tail to the shorter tail changes this expression by \(p^{a+1}-p^c>0\), since \(0<p<1\). Repeating gives exactly the balanced split, with equality only between reflected placements when tail counts differ by one.

**3. The adjacent-gap identity.** Let \(H_n(b;p)\) be the maximum expected spread among seed pairs at distance \(b\), attained by balancing. When \(b\) is increased by one, the shorter of the two old outer tails loses a final term \(p^{h_b}\), with \(h_b=\lceil(N-b)/2\rceil\). Direct subtraction of the interior sums gives
\[
H_n(b+1;p)-H_n(b;p)=p^b[1+b(1-p)]-p^{h_b},\qquad 1\le b<N.
\]
Define \(R_b(p)=p^{b-h_b}[1+b(1-p)]\). The increment has the sign of \(R_b(p)-1\), because \(p^{h_b}>0\).

**4. Strict unimodality in distance.** Since \(h_b-h_{b+1}\in\{0,1\}\),
\[
\frac{R_{b+1}(p)}{R_b(p)}
=p^{1+h_b-h_{b+1}}\frac{1+(b+1)(1-p)}{1+b(1-p)}
\le p(2-p)<1.
\]
Thus the \(R_b\) decrease strictly with \(b\). Consequently the signs of consecutive increments \(H_n(b+1;p)-H_n(b;p)\) change from positive to negative at most once, and a zero increment is possible at only one value of \(b\). Therefore the gap optima are either one distance or two adjacent distances. This establishes global, not merely local, optimality.

**5. First possible optimum and threshold existence.** For \(b<b_0=\lceil(n+1)/3\rceil\), one has \(b\le h_b\). Hence \(p^{b-h_b}\ge1\) and \(1+b(1-p)>1\), so \(R_b>1\); these distances cannot optimize. For \(b\ge b_0\), \(r_b=b-h_b>0\). Consider
\[
g_b(p)=r_b\log p+\log[1+b(1-p)].
\]
It is strictly concave on \((0,1)\), with \(g_b(p)\to-\infty\) as \(p\downarrow0\), \(g_b(1)=0\), and \(g_b'(1)=r_b-b=-h_b<0\). Thus it is positive just to the left of one and crosses zero at exactly one interior point \(\theta_b\). For \(p<\theta_b\), \(R_b<1\); for \(\theta_b<p<1\), \(R_b>1\). The strict decrease \(R_{b+1}(p)<R_b(p)\) makes the interior crossing points strictly ordered: \(\theta_b<\theta_{b+1}\).

**6. Complete phase diagram.** For a fixed \(p\), unimodality determines the maximum by the first nonpositive increment; all smaller distances below \(b_0\) have positive increments. Before \(\theta_{b_0}\), gap \(b_0\) is optimal; after \(\theta_{N-1}\), gap \(N\) is optimal. In every intervening phase the maximizing gap advances by one at the next strictly ordered threshold, with a two-gap tie only at that threshold. Tails must be balanced by step 2. If \(N=b_0\), the endpoint gap is always optimal. For \(n=2,3\), this leaves no transition; for \(n=4\), \(b_0=2\), \(N=3\), and
\[
H_4(3;p)-H_4(2;p)=p(1-p)(2p-1),
\]
so the unique interior switching point is \(p=1/2\), proving the sharp four-vertex minimum.

## Verification

The accompanying dependency-free `verify_pair_influence.py` uses integer polynomial coefficients and `fractions.Fraction` arithmetic. Its deterministic output is `certificate.json`. The script checks, independently of the proof: 495 complete independent live-edge enumerations for two seeds on paths of orders two through ten at three rational probabilities; 408 balanced-placement exact polynomial identities; 7,153 fixed-gap rational balancing comparisons; 1,428 optimal-gap tests for path orders through 69; and 47,838 exact rational adjacent-gap identities. The two files were executed and compared byte for byte within the packaged run. These finite checks corroborate but do not replace the arbitrary-\(n\) proof above. To reproduce, run `python3 verify_pair_influence.py` and compare standard output with `certificate.json` after ignoring the certificate's final newline if any (the captured file has the exact single serialized JSON object plus newline).

## Relationship to prior work

Kempe, Kleinberg, and Tardos [1] formulated influence maximization under independent-cascade dynamics and the live-edge framework; they studied general networks and approximation guarantees, not the present complete two-seed optimal-distance phase diagram on paths. Khanna and Lucier [2] studied approximation in undirected influence networks; their inspected article does not state this phase diagram. Mouravski [3] studied influence maximization on paths and reports an optimization algorithm in the accessible thesis abstract. The complete thesis text was not accessible for inspection, making coverage of the new exact threshold and monotonicity theorem a residual literature risk. The present claim is not the previously known computational solvability of placement on paths: it is the closed-form, all-sizes, all-probabilities ordering of optimal distances and their strictly ordered algebraic thresholds.

## Limitations

The conclusions are restricted to homogeneous, independent edge transmissions on an undirected path and exactly two deterministic seeds. They do not establish analogous monotonicity for heterogeneous edges, directed influence with asymmetric transmission, cyclic or branching networks, unequal seed costs, correlated activations, or three or more seeds. The minimum-size result is for a *change in optimal distance with transmission probability*, not the general complexity of influence maximization. A pertinent path-optimization thesis [3] was not fully accessible, so a fully exhaustive originality audit awaits that full text; scientific novelty should not be interpreted as independently certified.

## References

[1] D. Kempe, J. Kleinberg, and É. Tardos, *Maximizing the Spread of Influence through a Social Network*, KDD 2003, 137–146, first published 24 August 2003. DOI: 10.1145/956750.956769. Open author-hosted technical text: https://www.cs.cornell.edu/home/kleinber/kdd03-inf.pdf.

[2] S. Khanna and B. Lucier, *Influence Maximization in Undirected Networks*, SODA 2014; first online 18 December 2013. DOI: 10.1137/1.9781611973402.109. Lawful full-text repository: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Influence-Maximization-in-Undirected-Networks.pdf.

[3] A. Mouravski, *Influence Maximization on Families of Graphs*, Rochester Institute of Technology MSc thesis, 2011. Accessible bibliographic record and abstract: https://repository.rit.edu/theses/351/; full technical text not retrieved.

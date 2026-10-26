# Logarithmic stabilization of random weak directed-path endomorphisms

## Finding

For every integer \(n\ge2\), let \(\mathcal C_n\) be the monoid of all maps \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\) satisfying \(f(i+1)-f(i)\in\{0,1\}\) for every \(1\le i<n\). This is simultaneously the monoid of weak endomorphisms of the directed path and the monoid of order-preserving full contractions of the finite chain. Define its **stabilization index** by
\[
 T(f)=\min\{t\ge0:f^{t+1}=f^t\},
\]
where \(f^0\) is the identity. Let \(F_n\) be uniformly random in \(\mathcal C_n\). Then:

1. Every \(f\) has a nonempty interval \([a,b]\cap\mathbb Z\) of fixed points, and its stabilized power is the clipping map \(f^{T(f)}(i)=\min\{b,\max\{a,i\}\}\).
2. The sharp worst-case index is \(\max_{f\in\mathcal C_n}T(f)=n-1\), attained **only** by the right shift \(f(i)=\min\{i+1,n\}\) and the left shift \(f(i)=\max\{i-1,1\}\).
3. The typical index has a sharp logarithmic scale:
\[
 \frac{T(F_n)}{\log_2 n}\xrightarrow[n\to\infty]{\mathbb P}1,
 \qquad
 \mathbb E\!\left[\left(\frac{T(F_n)}{\log_2 n}\right)^p\right]\longrightarrow1
 \quad\text{for every real }p>0.
\]
Moreover, for each fixed \(\delta\in(0,1)\) there are constants \(c_\delta,C_\delta>0\) such that, for all sufficiently large \(n\),
\[
 \mathbb P\!\left(\left|T(F_n)/\log_2n-1\right|>\delta\right)
 \le C_\delta n^{-c_\delta}.
\]

Thus worst-case stabilization is linear but typical stabilization is logarithmic with leading constant one, including convergence of all positive moments of the normalized index.

## Assumptions and scope

All maps are **full**, order-preserving and nonexpansive on the indicated integer chain; they are not arbitrary order-preserving maps. Products and powers mean ordinary composition. The uniform distribution assigns equal probability to every map, not to every fixed interval. The asymptotic limit is along positive integers \(n\to\infty\), and the moment parameter is any fixed real \(p>0\). No independence of the two side lengths is assumed. The known finite count \(|\mathcal C_n|=(n+1)2^{n-2}\) for \(n\ge2\) is used, but is not presented as new.

## Proof

**1. Fixed interval and eventual clipping.** Put \(g(i)=f(i)-i\). Since consecutive increments of \(f\) lie in \(\{0,1\}\), the integers \(g(i)\) are nonincreasing with steps \(0\) or \(-1\). Also \(g(1)\ge0\) and \(g(n)\le0\). Therefore its zero set is a nonempty interval \([a,b]\cap\mathbb Z\). For \(i<a\), \(i<f(i)\le a\); for \(i>b\), \(b\le f(i)<i\); and \(f(i)=i\) for \(a\le i\le b\). Every orbit outside the fixed interval moves strictly toward its nearest fixed endpoint and enters it in at most \(n-1\) steps. Monotonicity of each iterate shows that the endpoint orbits, started at \(1\) and \(n\), are slowest on their respective sides. It follows that the eventual idempotent power is exactly the displayed clipping map.

**2. Sharp extremal index.** Any nonstationary orbit is a strictly monotone path through distinct integers, hence consists of at most \(n-1\) strict transitions. If \(T(f)=n-1\), one endpoint orbit must traverse every integer from one end of the chain to the other, so successive changes are all exactly \(+1\) or all exactly \(-1\). This forces exactly one of the two stated shifts. Both have index \(n-1\).

**3. Conditional Bernoulli representation.** Fix the exact fixed interval \([a,b]\). Write \(u=a-1\), \(v=n-b\). On the left, the step directly adjacent to \(a\) must be flat, since \(f(a-1)=a\). All other \(u-1\) permitted adjacent steps are freely and independently either flat or increasing. On the right the first step must likewise be flat, and the other \(v-1\) steps are unrestricted binary choices. Therefore the number of maps with this fixed interval is \(w(u)w(v)\), where \(w(0)=1\) and \(w(s)=2^{s-1}\) for \(s\ge1\). Conditioned on \([a,b]\), the free choices on the two sides are independent fair bits.

For a side of length \(s\ge1\), measure distances \(d\) to its fixed endpoint. In distance coordinates the map becomes
\[
 H_s(0)=H_s(1)=0,\qquad H_s(d)=\sum_{j=1}^{d-1}B_j\quad(2\le d\le s),
\]
with independent Bernoulli \(B_j\) of parameter \(1/2\). Define \(\tau_s\) as the number of iterates of \(H_s\) needed to take \(s\) to zero, and put \(\tau_0=0\). The endpoint argument gives the exact identity
\[
 T(f)=\max\{\tau_u,\tau_v\}.
\]
Notice that conditional independence is claimed only for the bit strings given the fixed interval; the side lengths themselves are not independent.

**4. Fixed-interval length is tight.** Let \(R=b-a+1=n-u-v\). The already-known fixed-point enumeration for this monoid states that, for \(1\le r<n\), the number of maps with \(R=r\) is \((n-r+3)2^{n-r-2}\), and for \(r=n\) it is one. Dividing by \((n+1)2^{n-2}\), for every \(n\ge2\) and integer \(m\ge1\), a geometric-tail estimate gives
\[
 \mathbb P(R\ge m)\le 10\,2^{-m}.
\]
One may also obtain the same bound by summing the weights \(w(u)w(v)\), without using the published enumeration. In particular, the event \(R\le n/2\) fails with exponentially small probability; on that event \(\max\{u,v\}\ge n/4\).

**5. Uniform prefix concentration and hitting-time bounds.** Couple each side's bits to an infinite independent fair-bit sequence and write \(H(d)=\sum_{j=1}^{d-1}B_j\). For every fixed \(\varepsilon\in(0,1/4)\), Hoeffding's inequality and a geometric union bound give constants \(A_\varepsilon,c_\varepsilon>0\) such that for all integers \(k\ge 2/\varepsilon\),
\[
 \mathbb P\bigl(\exists d\ge k:\ |H(d)-d/2|>\varepsilon d\bigr)
 \le A_\varepsilon e^{-c_\varepsilon k}.
\]
Here the \(1/2\)-unit bias between \(\mathbb E H(d)=(d-1)/2\) and \(d/2\) is absorbed by choosing \(k\ge2/\varepsilon\). Thus there is a random cutoff \(K_\varepsilon\), with exponentially decaying tail and all finite moments, such that for every \(d\ge K_\varepsilon\),
\[
 \alpha d\le H(d)\le\beta d,
 \qquad\alpha=\tfrac12-\varepsilon,\quad\beta=\tfrac12+\varepsilon.
\]
For an initial side length \(s\ge K_\varepsilon\), let \(L_s\) be the first iterate with distance below \(K_\varepsilon\). Then, by iterative comparison,
\[
 \frac{\log(s/K_\varepsilon)}{\log(1/\alpha)}
 \le L_s\le
 \frac{\log(s/K_\varepsilon)}{\log(1/\beta)}+2.
\]
All subsequent iterates strictly decrease the nonzero distance, so \(L_s\le\tau_s\le L_s+K_\varepsilon\). If \(s<K_\varepsilon\), simply \(\tau_s\le s<K_\varepsilon\). These inequalities hold for every \(s\) simultaneously under the same coupling.

**6. Probability and moment limits.** Fix \(\delta\in(0,1)\). Select \(\varepsilon>0\) so small that the reciprocals of \(\log_2(1/\alpha)\) and \(\log_2(1/\beta)\) differ from one by less than \(\delta/4\). Take \(k_n=\lceil\eta\log_2 n\rceil\), with \(\eta>0\) sufficiently small depending on \(\delta\). With probability at least \(1-Cn^{-c}\), both side sequences obey the preceding concentration inequalities with cutoff \(k_n\), while \(R\le n/2\). Since both lengths are at most \(n\) and one is at least \(n/4\), the hitting-time estimates imply, for all sufficiently large \(n\),
\[
 (1-\delta)\log_2n\le T(F_n)\le(1+\delta)\log_2n.
\]
The complement probability is polynomially small, as asserted. Finally fix one \(\varepsilon\), for example \(1/8\). The simultaneous upper bound above, applied to the two coupled infinite bit strings, gives a constant \(C\) with
\[
 T(F_n)\le C\log(n+1)+K_\varepsilon^{(L)}+K_\varepsilon^{(R)}+4.
\]
Both cutoffs have exponential tails uniformly in \(n\). Hence \(\{(T(F_n)/\log_2 n)^p:n\ge2\}\) is uniformly integrable for every real \(p>0\), and convergence in probability implies convergence of its expectations to one. This proves all parts.

## Verification

The accompanying standalone standard-library script `check_stabilization.py` exhaustively enumerates every map for \(2\le n\le11\). It checks the fixed interval and clipping limit, the sharp upper bound and exactly two extremizers, the known map count and fixed-point count, and independently reconstructs the two Bernoulli-prefix hitting processes for each map. Example stabilization-index distributions (ordered by index from zero) are \((1,9,8,2)\) at \(n=4\), \((1,20,55,26,8,2)\) at \(n=6\), and \((1,54,877,1041,523,208,76,26,8,2)\) at \(n=10\). All assertions pass. These finite checks are not used as an infinite proof: the concentration argument in the previous section supplies that proof.

## Relationship to prior work

Adeshola and Umar [1] consider exactly the same monoid under the name \(\mathcal{OCT}_n\), determine image-rank/fixed-point distributions (Proposition 2.3 and Corollaries 2.9–2.10), and give the total size used in Step 4. Fernandes and Paulista [2] study the same monoid as weak directed-path endomorphisms, count its idempotents, classify regular elements, and determine monoid rank. The examined full texts do not state the stabilization-index distribution or the logarithmic limit law for its uniform random element. The novelty asserted here is the **iterated-power dynamical dichotomy and limit law**, not any of those earlier enumerations or the clipping-idempotent classification by itself.

## Limitations

The asymptotic is for the uniform distribution on the full order-preserving contraction monoid; it does not automatically extend to arbitrary monotone transformations, to nonuniform sampling, or to order-reversing contractions. Polynomial tail constants depend on the chosen fixed relative error; no limiting centered fluctuation distribution or sharp additive error for \(\mathbb E T(F_n)\) is asserted. Search and comparison cannot establish exhaustive global priority; an earlier result phrased in finite dynamical-systems or prefix-count terminology remains a possible originality risk. The finite script verifies only the listed small sizes.

## References

[1] A. D. Adeshola and A. Umar, “Combinatorial results for certain semigroups of order-preserving full contraction mappings of a finite chain,” arXiv:1303.7428, 2013. Full text: https://arxiv.org/html/1303.7428v2 .

[2] V. H. Fernandes and T. Paulista, “On the Rank of Monoids of Endomorphisms of a Finite Directed Path,” arXiv:2112.13427, first submitted 2021-12-26. Full text: https://arxiv.org/html/2112.13427v1 .

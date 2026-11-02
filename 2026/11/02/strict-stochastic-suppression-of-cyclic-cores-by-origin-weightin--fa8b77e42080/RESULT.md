# Strict stochastic suppression of cyclic cores by origin weighting in random mappings

## Finding

For each integer \(n\ge2\), let \(F\) be a function from \([n]\) to \([n]\). Write \(C(F)\) for the number of vertices on directed cycles of its functional digraph and \(L(F)\) for the number of vertices of indegree zero (origins). For every real \(t\ge1\), give each function probability proportional to \(t^{L(F)}\); let \(C_{n,t}\) denote its cyclic-vertex count. Then, for every \(1\le s<t<\infty\) and every integer \(2\le k\le n\),

\[
\Pr(C_{n,t}\ge k)<\Pr(C_{n,s}\ge k).
\]

Thus increasing the reward for origins *strictly decreases the entire cyclic-core size in first-order stochastic order*, for every finite size, not merely its mean. The following exact positive-mixture identity is a simultaneous quantitative form. Write

\[
 a_{n,r}=\binom nr\left(1-\frac rn\right)^n,\qquad
 W_n(t)=\sum_{r=0}^{n-1}a_{n,r}(t-1)^r.
\]

For \(t\ge1\) and \(1\le k\le n\),

\[
 \Pr(C_{n,t}\ge k)=\frac{1}{W_n(t)}
 \sum_{r=0}^{n-1}a_{n,r}(t-1)^r
 \frac{(n-r)_{\underline{k}}}{(n-r)^k},
\]

where \((m)_{\underline{k}}=m(m-1)\cdots(m-k+1)\) for \(k\le m\) and is zero for \(k>m\). The term for \(r=0\) is the ordinary random-mapping law.

At the unbiased point \(t=1\), a related exact dependence identity has a sharp asymptotic consequence. If \(C_n=C_{n,1}\) and \(L_n=L(F)\) under the uniform measure, then

\[
\operatorname{Cov}(C_n,L_n)
=n\left(1-\frac1n\right)^n
\left(\mathbb E C_{n-1}-\mathbb E C_n\right)
\sim-e^{-1}\sqrt{\frac{\pi n}{8}}.
\]

Consequently the covariance is negative for every \(n\ge2\), while the correlation tends to zero:

\[
\sqrt n\,\operatorname{Corr}(C_n,L_n)
\longrightarrow
-\frac{e^{-1}\sqrt{\pi/8}}
{\sqrt{(2-\pi/2)(e^{-1}-2e^{-2})}}
\approx-1.128627916.
\]

These statements form one dependence-and-order theorem for the same natural pair of mapping statistics.

## Assumptions and scope

The state space consists of all \(n^n\) functions \([n]\to[n]\), including loops and all cycle lengths. Its directed edge convention is \(v\to F(v)\). An origin is a vertex receiving **no** directed edges, and a cyclic vertex is a vertex lying on a directed cycle. Every map has at least one cyclic vertex and at most \(n-1\) origins. The tilt \(t^{L(F)}\) is defined for finite real \(t\ge1\). Independent uniform arrows give the baseline law at \(t=1\). Strictness is asserted only for the integer tails \(2\le k\le n\), because the tail at \(k=1\) is identically one. The exact covariance statement concerns the uniform measure, not arbitrary \(t\).

## Proof

**1. Prescribed-origin identity.** Fix \(r\in\{0,\ldots,n-1\}\) and \(r\) distinct designated vertices. The event that all those vertices have indegree zero means every one of the \(n\) independent outgoing arrows avoids that designated set; its probability is \(((n-r)/n)^n\). Conditional on this event, the outgoing arrows of the remaining \(n-r\) vertices are independent uniform choices among those \(n-r\) vertices. Every designated vertex is a leaf feeding into that complement, so no designated vertex lies on a cycle and the cyclic-vertex count is exactly that of a uniform mapping on \(n-r\) vertices. Summing over ordered choices gives, for every bounded \(g\),

\[
\mathbb E\big[(L_n)_{\underline r}g(C_n)\big]
=(n)_{\underline r}\left(1-\frac rn\right)^n
\mathbb E[g(C_{n-r})]. \tag{1}
\]

Here \(C_m\) on the right always denotes the uniformly sampled mapping of \(m\) vertices, and \(r=0\) means the ordinary expectation. In particular, taking \(g=1\) supplies all factorial moments of \(L_n\).

**2. Mixture under origin tilting.** For \(t\ge1\), expand the nonnegative polynomial \(t^{L_n}=(1+(t-1))^{L_n}\). Since \(\binom{L_n}{r}=(L_n)_{\underline r}/r!\), identity (1) yields

\[
\mathbb E[t^{L_n}g(C_n)]
=\sum_{r=0}^{n-1}\binom nr\left(1-\frac rn\right)^n
 (t-1)^r\mathbb E[g(C_{n-r})]. \tag{2}
\]

The coefficient at \(r=n\) vanishes because no function has all vertices of indegree zero. Choosing \(g=1\) gives the normalization \(W_n(t)>0\). Dividing (2) by that normalization proves an exact mixture, with weights proportional to \(a_{n,r}(t-1)^r\), of the uniform laws \(C_{n-r}\).

**3. Strict monotonicity.** For any \(m\ge1\), fix \(1\le j\le m\). Choose the \(j\) cyclic labels, permute them into cycles, then connect every other vertex as a forest directed toward the cyclic set. The number of such rooted forests is \(j m^{m-j-1}\), by the directed matrix-tree theorem; the expression is also valid for \(j=m\). Thus

\[
\Pr(C_m=j)=\frac{j(m)_{\underline j}}{m^{j+1}},\qquad
\Pr(C_m\ge k)=\frac{(m)_{\underline k}}{m^k}. \tag{3}
\]

The tail follows by telescoping. For each \(k\ge2\), the latter tail is strictly increasing in \(m\) once it becomes positive, because it equals \(\prod_{i=0}^{k-1}(1-i/m)\). In the mixture (2), its value as a function of \(r\) is therefore nonincreasing and nonconstant. For \(1<s<t\), the ratio between the \(r\)-weights at \(t\) and \(s\) is a positive constant times \(((t-1)/(s-1))^r\), strictly increasing in \(r\); hence the mixing index is strictly increasing in likelihood-ratio order. Its expectation of any nonconstant nonincreasing function, including the tail in (3), strictly decreases. If \(s=1\), the original mixture is concentrated at \(r=0\), whereas the tilt at \(t>1\) gives positive weight to \(r\ge1\), and the same strict inequality follows. This proves the full claimed stochastic ordering and tail formula.

**4. Exact dependence and asymptotics.** Setting \(r=1\) and \(g(C)=C\) in (1), then subtracting the product of the means, proves the covariance formula in the Finding section. Its sign is strictly negative because \(\mathbb E C_m=\sum_{k=1}^m(m)_{\underline k}/m^k\) strictly increases with \(m\).

For completeness, put \(h_{m,k}=(m)_{\underline k}/m^k\). The product formula and dominated Riemann sums imply

\[
\frac{\mathbb E C_n}{\sqrt n}\to\sqrt{\frac\pi2},\quad
\frac{\operatorname{Var}C_n}{n}\to 2-\frac\pi2,\quad
\sqrt n\left(\mathbb E C_n-\mathbb E C_{n-1}\right)
\to\frac12\int_0^\infty x^2e^{-x^2/2}\,dx=\sqrt{\frac\pi8}. \tag{4}
\]

For the last convergence, on the scale \(k=x\sqrt n\), the product \(h_{n,k}\) tends to \(e^{-x^2/2}\), and \(n(h_{n,k}-h_{n-1,k})\to(x^2/2)e^{-x^2/2}\). The difference is bounded uniformly for \(k\le n/2\) by a constant times \((k^2/n^2)e^{-k(k-1)/(2n)}\); the remaining \(k>n/2\) terms are exponentially small. This justifies the Riemann limit. The variance limit follows from \(\mathbb E C_n^2=\sum_{k=1}^n(2k-1)h_{n,k}\).

Finally, empty-box indicators for the \(n\) independent arrows give \(p_n=(1-1/n)^n\), \(q_n=(1-2/n)^n\), and

\[
\operatorname{Var}L_n=np_n+n(n-1)q_n-n^2p_n^2,
\qquad\frac{\operatorname{Var}L_n}{n}\to e^{-1}-2e^{-2}. \tag{5}
\]

Combining (4) and (5) with the exact covariance proves both asymptotic statements.

A useful finite conditional refinement follows from the same forest count: given \(C_n=c<n\) and the \(c\) cyclic roots, write \(m=n-c\). The polynomial enumerating forests by the parent weights \(w_v\) is \((\sum_{v\text{ root}}w_v)(\sum_v w_v)^{m-1}\). Therefore for \(0\le r\le m\),

\[
\mathbb E[(L_n)_{\underline r}\mid C_n=c]
=(m)_{\underline r}\left(1-\frac rn\right)^{m-1}. \tag{6}
\]

This is the factorial-moment law of empty occupancy boxes among the \(m\) noncyclic positions after \(m-1\) independent uniformly placed balls in \(n\) boxes. For \(c=n\), \(L_n=0\) deterministically. The conditional fact is used as an independent finite verification route, not as a separately claimed novelty.

## Verification

Run `python3 verify.py` from the directory containing this document and the supplied verifier. The checker exhaustively visits all mappings on \(2\) through \(7\) vertices, including all \(823543\) maps at size seven, comparing exact rational cyclic tails, prescribed-origin factorial moments, conditional occupancy moments, the tilted mixture at several pairs of weights, strict tail inequalities, and the covariance identity. It also compares finite approximations to the analytic adjacent-mean asymptotic. The executed checker reports **486 exact assertions passed**. Finite enumeration is not an infinite proof; all-size conclusions follow from steps 1–4.

## Relationship to prior work

Arney and Bender (1982) introduced origin weighting and constraints in random mapping models and developed generating functions and asymptotics for origins and cyclic structures. Their equation (7.1) marks **number of cycles**, not **number of cyclic vertices**, and their Table II includes asymptotic core-size behavior. The present strict stochastic comparison of every cyclic-vertex tail as origin fugacity varies is different from those generating functions and marginal asymptotics. Their prior framework supplies important context; this is not a claim to have introduced origin weighting.

Hansen and Jaworski (2006, Theorem 1) gave a general exact distribution of cyclic-vertex counts for random mappings specified by an exchangeable indegree vector; their formula is sufficiently broad to permit algebraic specialization to the origin-weighted model. The specific theorem proved here is instead the **all-size, all-parameter stochastic comparison** between different origin weights, with a positive mixture construction and strict likelihood-ratio argument. The underlying marginal distribution is therefore not asserted to be independently novel. Hansen and Jaworski (2010) also treated mappings conditioned on their number of cyclic vertices and a rooted-forest representation. These antecedents make the historical novelty judgment qualified, rather than certain.

## Limitations

The proven stochastic ordering is restricted to weights \(1\le s<t<\infty\); an extension below weight one is not proved here. The conditional-forest and factorial-moment identities are traditional counting techniques, and previous broad joint generating-function or indegree-distribution theorems may imply some recorded corollaries. The status of any earlier *equivalent stochastic-order formulation* remains subject to independent specialist review, particularly in the older random-mapping and occupancy literature. The correlation constant refers to the uniform law only. No inference about statistical independence is asserted, and the exact covariance is negative despite a correlation vanishing in magnitude.

## References

- J. Arney and E. A. Bender, “Random mappings with constraints on coalescence and number of origins,” *Pacific Journal of Mathematics* **103** (1982), 269–294, https://doi.org/10.2140/pjm.1982.103.269 . Full text: https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-p.pdf .
- J. Hansen and J. Jaworski, “A new random mapping model,” initial public arXiv version dated 2006-03-22, https://arxiv.org/abs/math/0603529 ; full text https://arxiv.org/pdf/math/0603529 . See especially §2–3 and Theorem 1.
- J. Hansen and J. Jaworski, “Random mappings with a given number of cyclical points,” *Ars Combinatoria* **94** (2010), 341–359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ .
- P. Flajolet and A. M. Odlyzko, “Random Mapping Statistics,” in *EUROCRYPT '89*, LNCS **434** (1990), 329–354. Bibliography: https://algo.inria.fr/flajolet/Publications/ .

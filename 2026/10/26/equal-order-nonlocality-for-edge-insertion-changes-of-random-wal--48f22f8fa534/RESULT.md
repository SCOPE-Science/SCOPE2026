# Equal-order nonlocality for edge-insertion changes of random-walk cover time

## Finding
For every integer \(r\ge1\), there exist connected finite simple graphs \(G_r^{+}\) and \(G_r^{-}\), each on exactly \(n=r+K+4\) vertices with \(K=\max\{100,4r+10\}\), and three distinct marked vertices \(s,u,v\), such that the following hold simultaneously.

1. The edge \(uv\) is absent, and the induced radius-\(r\) neighborhoods of \(\{s,u,v\}\), with the three marks distinguished and **each visible vertex labelled by its degree in the ambient graph**, are isomorphic.
2. Both graphs have \(d_s=d_u=d_v=1\), \(\operatorname{dist}(s,\{u,v\})=2\), and unit-edge effective resistance \(R_{uv}=2\).
3. The fixed-start simple-random-walk cover-time response to inserting \(uv\) has opposite strict signs:

\[
\delta_s(G_r^{+};uv)>0>\delta_s(G_r^{-};uv),\qquad
\delta_s(G;uv)=\mathbb E_s\tau_{\mathrm{cov}}(G+uv)-\mathbb E_s\tau_{\mathrm{cov}}(G).
\]

In particular, even graph order appended to all the above local and marked scalar data cannot determine the sign of an edge-insertion cover-time change. The equal-order strengthening was posed explicitly as an open problem by Si [1, Section 7].

## Assumptions and scope
Every edge has unit conductance and the walk is discrete-time, non-lazy simple random walk. The start is the marked leaf \(s\). Set \(K=\max\{100,4r+10\}\) and \(q=r+K\). Both graphs have distinct vertices \(c,s,u,v\) and the edges \(cs,cu,cv\).

For \(G_r^{+}\), attach at \(c\) the path \(c-p_1-\cdots-p_q\). There are no other edges.

For \(G_r^{-}\), attach the path \(c-p_1-\cdots-p_r-t\), and let \(t\) belong to a complete graph on \(K\) vertices, with the other \(K-1\) clique vertices distinct from all those already named. There are no other edges. Thus the clique is a **terminal**, one-bridge attachment, not a clique containing \(c\).

The vertex counts are respectively \(4+q\) and \(4+r+K\), hence equal. Every graph in the theorem is finite, connected and simple, and \(uv\) is a nonedge.

## Proof
**1. Local and electrical data.** The vertices at distance at most \(r\) from the marked set are precisely \(\{s,u,v,c,p_1,\ldots,p_{r-1}\}\) (with an empty path segment for \(r=1\)). They induce three leaf edges at \(c\) and the visible stem. In both full graphs, the marked leaf degrees are \(1\), \(d_c=4\), and every visible \(p_j\) has ambient degree \(2\); the next stem vertex is outside the ball. The marked distance is \(2\). The edges \(uc\), \(cv\) form the unique path between \(u,v\) and are bridges, so the two resistances add to \(R_{uv}=2\). This proves all local and scalar equalities, **including graph order**.

**2. Exact cut-vertex response.** We state and reconstruct the cut-vertex transfer identity of [1, Theorem 3.2] in the present normalization. Let an arbitrary nonempty remote graph attach at \(c\), with the same three marked leaves, and put \(m=|E(G)|\). Give each directed edge leaving \(c\) an independent rate-one Poisson clock; attach to each ringing time an independent complete excursion along that edge back to \(c\). The chronological excursion sequence has exactly the law of successive random-walk excursions. Define \(T\) as the first artificial time by which remote excursion paths have visited all remote vertices; put \(a=\mathbb E e^{-T}\), \(b=\mathbb E e^{-3T/2}\). Let \(J\ge0\) be the expected unused physical suffix (from first completion until return to \(c\)) of the terminal remote excursion conditional on its observed precompletion path. The remote process, and hence \((T,J)\), is independent of the local completion processes.

Before insertion, visiting both local leaves has artificial survival function \(\Pr(A>t)=2e^{-t}-e^{-2t}\). After insertion, the two transient states of the local triangle (neither endpoint visited; exactly one visited) have decay rates \(2\) and \(3/2\), respectively, giving \(\Pr(B>t)=2e^{-3t/2}-e^{-2t}\). By the elementary stopped-excursion identity, Kac's return formula and Poissonization, the expected physical length of all *complete* excursions up to any integrable artificial completion time \(Z\) is \(2m\mathbb EZ\) before insertion and \(2(m+1)\mathbb EZ\) afterward. This identity is valid even though the terminal excursion duration depends on its discovery marks: its length is independent of the event of survival **before** that excursion.

If local coverage finishes last, the unused suffix of its terminal excursion has mean \(1\) before, and \(2\) after, insertion. If remote coverage finishes last, the unused suffix has conditional mean \(J\) on either graph. Accounting for the forced first step \(s\to c\) gives
\[
C_0=1+2m\mathbb E\max(T,A)-\Pr(A>T)-\mathbb E[J\mathbf1_{\{T>A\}}],
\]
\[
C_1=1+2(m+1)\mathbb E\max(T,B)-2\Pr(B>T)-\mathbb E[J\mathbf1_{\{T>B\}}].
\]
For \(X\perp T\), the identity \(\mathbb E\max(T,X)=\mathbb ET+\int_0^\infty\Pr(X>t)\Pr(T\le t)dt\) and integration by parts yield
\[
\mathbb E\max(T,A)=\mathbb ET+2a-\tfrac12\mathbb E e^{-2T},\quad
\mathbb E\max(T,B)=\mathbb ET+\tfrac43b-\tfrac12\mathbb E e^{-2T}.
\]
Similarly, \(\Pr(A>T)=2a-\mathbb E e^{-2T}\) and \(\Pr(B>T)=2b-\mathbb E e^{-2T}\). Conditional independence gives the remote suffix difference \(2\mathbb E[J(e^{-T}-e^{-3T/2})]\). Subtracting and simplifying proves the exact identity
\[
\boxed{\delta_s(G;uv)=2\mathbb ET-2(2m-1)(a-\tfrac23b)-2\mathbb E[J(e^{-T}-e^{-3T/2})].}\tag{1}
\]
All expectations are finite: on any fixed finite connected graph, a fixed finite collection of possible return excursions covers the remote vertices with a positive probability in each independent block; excursion lengths and the stopping time have geometric-tail bounds.

**3. Strict positive response for a path.** For the remote path of length \(q\), each rate-one departure along \(cp_1\) reaches \(p_q\) before returning to \(c\) with gambler's-ruin probability \(1/q\). Hence \(T\sim\operatorname{Exp}(1/q)\), so \(\mathbb ET=q\), \(a=1/(q+1)\), \(b=2/(3q+2)\). Conditional on reaching \(p_q\), the mean hitting time back to \(c\) is \(q^2\); therefore \(J=q^2\). With \(m=q+3\), (1) simplifies **exactly** to
\[
\boxed{\delta_s(G_r^{+};uv)=\frac{2(6q^3+5q^2-23q-10)}{3(q+1)(3q+2)}.}\tag{2}
\]
The polynomial numerator inside the parentheses equals \(12\) at \(q=2\), and its derivative \(18q^2+10q-23\) is positive for every \(q\ge2\). Since \(q=r+K\ge101\), (2) is strictly positive.

**4. A single-excursion clique-covering bound.** In \(G_r^{-}\), the only departure from \(c\) into the remote graph is along \(cp_1\), and the corresponding rate-one clock carries independent return excursions. By gambler's ruin on the stem, any such excursion first reaches the clique gateway \(t\) before returning to \(c\) with probability \(1/(r+1)\).

Once at \(t\), couple the walk with ordinary simple random walk on the complete graph of order \(K\): at each visit to \(t\), allow an additional exit along the bridge back to \(p_r\) with conditional probability \(1/K\); otherwise select a uniformly random clique neighbor. At any other clique vertex, select a uniformly random distinct clique vertex. Let \(d=\lceil3(K-1)\log K\rceil\). In the un-killed clique walk started at \(t\), a specified different vertex remains unvisited after \(d\) steps with probability \((1-1/(K-1))^d\). Union bounding over all other vertices shows that failure to see the entire clique by then has probability at most \((K-1)e^{-d/(K-1)}\le K^{-2}\).

For this walk, the expected number of visits to \(t\) among instants \(0,\ldots,d-1\) is at most \(1+d/(K-1)\) (each positive-time probability of being at \(t\) is at most \(1/(K-1)\)). The union bound on possible bridge exits is therefore at most \((1+d/(K-1))/K\). Combining the two bad events and the definition of \(d\), the chance of covering the whole clique before exiting is at least
\[
1-\frac1{K^2}-\frac{1+3\log K+1/(K-1)}K>\frac12
\qquad(K\ge100).
\]
The last inequality holds at \(K=100\) and the subtracted expression decreases for \(K\ge100\). Any such successful excursion visits all stem vertices as well, so its probability of covering the **entire remote graph** is at least \(h=1/[2(r+1)]\). By independent marking and Poisson thinning, the first individually covering remote excursion arrives no later stochastically than an \(\operatorname{Exp}(h)\) variable; remote coverage can only be earlier. Thus
\[
\mathbb ET\le 2(r+1),\qquad a=\mathbb E e^{-T}\ge\frac{h}{1+h}=\frac1{2r+3}.
\]

**5. Strict negative response for the clique-tail graph.** In (1), \(J\ge0\), \(e^{-T}-e^{-3T/2}\ge0\), and \(b\le a\); hence \(a-\tfrac23b\ge a/3\). The original edge count for the clique-tail graph is \(m=r+4+\binom K2\), and therefore
\[
\delta_s(G_r^{-};uv)
\le4(r+1)-\frac{2}{3}\frac{K(K-1)+2r+7}{2r+3}<0.
\]
The strict final inequality is equivalent to \(K(K-1)>12r^2+28r+11\). Our explicit choice \(K\ge4r+10\) satisfies it because \((4r+10)(4r+9)-(12r^2+28r+11)=4r^2+48r+79>0\). Both signs and all matching data follow. \(\square\)

## Verification
The standalone `verify.py` calculates expected discrete-time cover times for small graphs **independently of the excursion transfer formula**, using exact-rational Bellman equations on the visited-set state space. It checks the fully marked radius-\(r\) neighborhood, the exact rational positive response (2), and strictly negative rational responses for three equal-order examples, including \((r,K)=(1,3)\) and \((2,4)\). It also evaluates the coupon/exit upper bound and the strict sign inequalities for 203 different radii, with displayed samples extending to \(r=100000\). Run with `python verify.py` from the directory containing the file. The accompanying `verification_output.txt` is an actual run record. Finite tests are corroboration, **not** proof of the infinitely quantified result; the proof is Steps 1–5.

## Relationship to prior work
Si [1] proved arbitrary-radius local sign nonlocality with different-order graphs, derived the exact transfer formula (1), and explicitly asked whether opposite-sign witnesses can be made the **same order**. The present construction addresses that missing order constraint, using an endpoint clique behind the radius cutoff rather than a clique attached directly to \(c\). Identity (1) and the general phenomenon of edge-insertion sign reversal are prior results, not claimed as new. Barlow, Ding, Nachmias and Peres [2] gave a universal multiplicative upper bound on cover-time increase after one edge insertion; this does not imply the exact local-data-matched opposite signs at equal order. Ding, Lee and Peres [3] gave cover-time comparisons with majorizing measures, up to universal constants, also not an exact insertion-sign criterion. The novelty claim is limited to the **equal-order, arbitrary-radius strict-sign construction** in the Finding section.

## Limitations
The construction permits large graphs (\(K\ge100\)) and does not claim minimal witness order or degree bounds, or a polynomial-time cover-time sign algorithm. It addresses fixed-start, not worst-start, cover time. Its proof uses the already published cut-vertex transfer identity, which is reconstructed above. Exhaustive historical priority is not guaranteed; an equivalent subsequently disseminated construction could exist. No independent mathematical review has been performed.

## References
1. Ian Meng Si, *Nonlocality of Cover-Time Changes Under Edge Addition*, arXiv:2608.27474v1 (first public 2026-08-19), in particular Sections 3.4 and 7. https://arxiv.org/html/2608.27474v1
2. M. T. Barlow, J. Ding, A. Nachmias, and Y. Peres, *The Evolution of the Cover Time*, Combinatorics, Probability and Computing 20 (2011), 331–345; arXiv:1001.0609. https://arxiv.org/abs/1001.0609
3. J. Ding, J. R. Lee, and Y. Peres, *Cover times, blanket times, and majorizing measures*, Annals of Mathematics 175 (2012), 1409–1471; arXiv:1004.4371. https://arxiv.org/abs/1004.4371

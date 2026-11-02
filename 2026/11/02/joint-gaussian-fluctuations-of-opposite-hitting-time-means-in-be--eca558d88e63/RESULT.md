# Joint Gaussian fluctuations of opposite hitting-time means in Bernoulli recursive trees

## Finding

For a finite Bernoulli recursive tree defined below, let \(H_N^+\) and \(H_N^-\) be the conditional (tree-wise) mean first-passage times of simple random walk from the oldest vertex to the newest vertex and in the opposite direction. For every fixed \(p\in(0,1)\), set \(q=1-p\), \(\mu=2-p\), and \(v=pq\). As \(N\to\infty\), with probability and weak convergence referring to the randomness of the tree,

\[
\left(\frac{H_N^+-N^2/\mu}{N^{3/2}},\frac{H_N^--N^2/\mu}{N^{3/2}}\right)
\ \Rightarrow\
\mathcal N_2\!\left(0,\frac{4v}{3\mu^3}
\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\right).
\]

Both means also satisfy \(H_N^+/N^2\to1/\mu\) and \(H_N^-/N^2\to1/\mu\) almost surely under a common infinite sequence of attachment decisions. In particular, the limiting correlation of the *Gaussian fluctuations* is \(1/2\), independent of the attachment parameter. The statement concerns fluctuations of conditional expected hitting times across random trees, **not** a central limit theorem for an individual walk's random hitting time.

## Assumptions and scope

The vertices are \(v_0,v_1,\ldots,v_N\). The edge from \(v_1\) to \(v_0\) is deterministic. Independently for each \(2\le j\le N\), attach \(v_j\) to \(v_{j-1}\) with probability \(p\in(0,1)\) and to \(v_{j-2}\) with probability \(q=1-p\). The resulting connected graph \(T_N\) is a tree with exactly \(N\) edges. Once \(T_N\) is fixed, simple random walk jumps uniformly among neighbors and \(\tau_x=\inf\{t\ge0:X_t=x\}\). Define

\[
H_N^+=\mathbb E_{v_0}^{T_N}[\tau_{v_N}],\qquad
H_N^-=\mathbb E_{v_N}^{T_N}[\tau_{v_0}].
\]

The attachment choices are the only source of randomness when taking the displayed weak limit. The endpoint parameters \(p=0,1\), nonuniform attachments, and dynamic/infinite-volume walk hitting times are outside this claim.

## Proof

**1. Exact finite-tree hitting identities.** Let \(b\) denote the numerical label of any vertex on the unique root-to-\(v_N\) path, excluding \(v_0\). Write \(M_b\) for the number of vertices on the root side of the edge joining \(v_b\) to its parent. For any finite tree, the expected walk time to cross this oriented edge from the root side is \(2M_b-1\): excursions into each of the \(M_b-1\) root-side edges contribute two traversals on average, followed by the final crossing. Summing successive edge-hitting expectations gives

\[
H_N^+=\sum_{b\text{ on the root-to-}v_N\text{ path}}(2M_b-1).
\]

Let \(D_N\) be the path length and \(A_N\) the sum of its positive vertex labels. The commute-time identity for unit-resistance trees gives

\[
H_N^++H_N^-=2ND_N.
\]

These are deterministic identities for each realized tree.

**2. Uniform geometric control of side branches.** For a path label \(b\), all vertices with labels below \(b\) are on the root side of its parent edge. Let \(c_j\) indicate whether \(v_j\) is descended from \(v_b\), with \(c_b=1\). Its possible values above \(b\) obey the copy recursion

\[
c_j=\begin{cases}c_{j-1},&v_j\text{ attaches to }v_{j-1},\\c_{j-2},&v_j\text{ attaches to }v_{j-2}.\end{cases}
\]

If \(c_{b+1}=1\), all subsequent indicators equal one. Otherwise \((c_b,c_{b+1})=(1,0)\). Since \(b\) is on the path to \(N\), necessarily \(c_N=1\). Two successive zero indicators would be absorbing and are therefore impossible before \(N\). Until two successive ones occur (which are likewise absorbing), the indicators must alternate and each further continuation of the alternating pattern requires a second-predecessor attachment. Consequently the number \(\delta_b\) of later indices not descended from \(b\) is at most \(L_N+1\), where \(L_N\) is the longest run of second-predecessor attachments among vertices \(2,\ldots,N\). Thus

\[
M_b=b+\delta_b,\qquad0\le\delta_b\le L_N+1.
\]

It follows *pathwise* that

\[
\left|H_N^+-2A_N\right|\le N(2L_N+3).
\]

Since \(\Pr(L_N\ge k)\le Nq^k\), a union bound and Borel--Cantelli yield \(L_N=O(\log N)\) almost surely. In particular \(H_N^+-2A_N=o(N^{3/2})\) almost surely.

**3. Backwards ancestry is a renewal process.** Starting at the newest vertex, each ancestor step reduces its label by one with probability \(p\) or two with probability \(q\). The sampled attachment variables belong to distinct decreasing labels, so the successive steps are independent. Let \(Y_1,Y_2,\ldots\) be independent with \(\Pr(Y_i=1)=p\), \(\Pr(Y_i=2)=q\), and set \(S_0=0\), \(S_k=\sum_{i=1}^{k}Y_i\). Define the inverse renewal count

\[
K_x=\#\{k\ge0:S_k<x\},\quad x\in\{1,2,\ldots\}.
\]

The deterministic final attachment from label one to zero changes no positive path label or path length. For each \(N\), jointly in distribution,

\[
D_N=K_N,\qquad A_N=\sum_{k:S_k<N}(N-S_k)=\sum_{x=1}^{N}K_x.
\]

The entire pair uses the *same* renewal sequence. These identities hold in joint law for each \(N\); no independence between rooted path labels is asserted.

**4. Joint inverse-renewal limit.** The increments have mean \(\mu=2-p\) and variance \(v=pq\). The functional central limit theorem for the inverse of a positive-drift renewal sum gives

\[
\left(\frac{K_{\lfloor Nt\rfloor}-Nt/\mu}{\sqrt N}\right)_{0\le t\le1}
\Rightarrow -\frac{\sqrt v}{\mu^{3/2}}(B_t)_{0\le t\le1},
\]

where \(B\) is standard Brownian motion. Summation (a Riemann integral) and evaluation at \(t=1\) therefore imply, jointly,

\[
\left(\frac{A_N-N^2/(2\mu)}{N^{3/2}},
\frac{D_N-N/\mu}{\sqrt N}\right)
\Rightarrow -\frac{\sqrt v}{\mu^{3/2}}
\left(\int_0^1B_t\,dt,\ B_1\right).
\]

Combining Steps 1--3 and the commute identity, the two standardized mean hitting times converge jointly to

\[
-\frac{2\sqrt v}{\mu^{3/2}}
\left(\int_0^1B_t\,dt,\ B_1-\int_0^1B_t\,dt\right).
\]

The Brownian variance identities

\[
\operatorname{Var}\!\left(\int_0^1B_t\,dt\right)=\frac13,
\quad\operatorname{Cov}\!\left(\int_0^1B_t\,dt,B_1\right)=\frac12
\]

show that both coordinates have variance \(4v/(3\mu^3)\) and their covariance is \(2v/(3\mu^3)\), proving the asserted covariance matrix and universal half-correlation.

**5. Almost-sure leading order.** The renewal count has exponentially small linear-deviation probabilities by Hoeffding bounds for the bounded increments \(Y_i\). A union bound over \(1\le x\le N\) implies that the probability of a fixed linear deviation anywhere in the renewal counting profile up to \(N\) decays exponentially (up to a polynomial factor). Borel--Cantelli and \(A_N=\sum_{x=1}^NK_x\) yield \(A_N/N^2\to1/(2\mu)\) and \(D_N/N\to1/\mu\) almost surely in the original tree environment, using only their correct marginal laws at each \(N\). Together with the pathwise bound in Step 2 and the commute identity, this proves the stated two almost-sure laws. No across-\(N\) identification of the auxiliary renewal sequences is used.

## Verification

The standalone Python script `verify.py` enumerates every attachment configuration for \(1\le N\le12\), checks the root-component hitting formula, the commute identity, and the longest-run error bound; for \(N\le7\) it independently solves the exact rational first-step linear systems in both directions. It also checks pure-path boundaries and performs reproducible finite-size diagnostics at three interior parameter values. See `verification_output.txt` for the actual output. The completed script passed **4,898,253 deterministic assertions**. Finite experiments do not establish the stated weak or almost-sure limits; these follow from Steps 2--5.

## Relationship to prior work

Tang, Wang and Wu (2026) introduce precisely this Bernoulli recursive-tree model and establish its one-ended geometry and infinite-collision property. The present result asks a distinct finite-tree first-passage question and gives a joint fluctuation law, an explicit covariance matrix and a parameter-independent correlation. Georgakopoulos and Wagner (arXiv:1302.3212), especially Lemma 4.2, supply general deterministic hitting-time identities for trees; the general commute formula is also classical. The model-specific geometric run bound and the common backwards-renewal representation are required to obtain the new stochastic limit. Oosthuizen and Wagner (2017) study hitting-time distributions on other random-tree ensembles, including the standard uniform random recursive tree, where the cited root hitting-time scales differ from the quadratic scaling here.

## Limitations

The limit is annealed over attachment environments for *quenched conditional means*, not a walk-path fluctuation theorem. It assumes fixed \(0<p<1\) and the special two-possible-parent rule; endpoint parameter limits and larger attachment windows are not addressed. The analytic proof uses classical inverse-renewal invariance principles and deterministic tree hitting identities; those ingredients are not claimed as discoveries. Historical priority of the joint model-specific statement requires independent literature review, particularly of generalized random-tree first-passage theory. A relevant 2017 comparison was available at abstract level only; no claim of full-text inspection is made for it.

## References

1. J.-s. Tang, F. Wang, X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences* (first public version 2026-07-03), https://arxiv.org/abs/2607.02916 .
2. A. Georgakopoulos and S. Wagner, *Hitting Times, Cover Cost, and the Wiener Index of a Tree*, arXiv:1302.3212 (2013), https://arxiv.org/abs/1302.3212 ; Journal of Graph Theory 84 (2017), 311--326.
3. J. Oosthuizen and S. Wagner, *On the distribution of random walk hitting times in random trees*, ANALCO 2017, 73--84, https://doi.org/10.1137/1.9781611974775.7 .
4. Classical renewal functional central limit theorem and continuous mapping for inverse counting processes; the required transform is derived explicitly in Step 4.

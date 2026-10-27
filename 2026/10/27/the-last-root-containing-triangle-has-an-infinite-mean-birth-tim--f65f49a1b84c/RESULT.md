# The last root-containing triangle has an infinite-mean birth time in a two-parent recursive graph

## Finding
For a uniform two-parent random recursive directed acyclic graph, forget edge orientation and collapse parallel edges. Let \(L\) be the last vertex-arrival time at which a **new simple triangle containing vertex \(1\)** is formed, setting \(L=0\) if no such triangle exists. Then \(L<\infty\) almost surely, while
\[
\Pr\{L>N\}=\frac{4\log N+4+4\gamma-2\zeta(2)}{N}+O\!\left(\frac{(\log N)^2}{N^2}\right),\qquad N\longrightarrow\infty,
\]
where \(\gamma\) is Euler's constant. Consequently \(\mathbb E[L^a]<\infty\) for \(0<a<1\) and \(\mathbb E[L^a]=\infty\) for \(a\ge1\). Although the final birth time has infinite mean, the total number of root-containing triangles has the finite expectation \(4\zeta(3)-\tfrac32\zeta(4)\).

This is an extreme-arrival statement, not a claim about the total number of triangles in the graph or about marked multigraph copies.

## Assumptions and scope
Start with vertex \(1\). Independently for each integer \(t\ge2\), the new vertex \(t\) chooses two parents independently and uniformly from \(\{1,\ldots,t-1\}\), with replacement. Retain only simple undirected adjacencies when detecting triangles. A rooted triangle consists of three distinct vertices, one being \(1\); it is born when its largest-labelled vertex arrives. Let \(Y_t\) be the indicator that at least one such triangle is born at time \(t\). As there are only two parent slots, at most one *distinct* rooted triangle can be born at each arrival. Set \(L=\sup\{t\ge3:Y_t=1\}\), with the empty supremum defined as zero. All assertions refer to the common infinite coupling of the arrival steps. The integer cutoff \(N\) tends to infinity.

## Proof
**One-arrival identity.** Let \(D_q\) be the number of distinct neighbours of root \(1\) among vertices \(2,\ldots,q\), after arrival \(q\). For each arrival \(u\ge2\) independently, the indicator of root adjacency is Bernoulli with parameter
\[
p_u=1-\left(1-\frac1{u-1}\right)^2=\frac2{u-1}-\frac1{(u-1)^2}.
\]
Hence, writing \(H_k^{(r)}=\sum_{j=1}^k j^{-r}\) and \(H_k=H_k^{(1)}\),
\[
\mu_q:=\mathbb ED_q=2H_{q-1}-H_{q-1}^{(2)}.
\]
Conditionally on all choices through vertex \(t-1\), a rooted triangle is born precisely if the two choices at \(t\) are \((1,j)\) or \((j,1)\) for some *distinct* earlier root neighbour \(j\). Therefore
\[
\mathbb P(Y_t=1\mid\mathcal F_{t-1})=\frac{2D_{t-1}}{(t-1)^2},\qquad
\mathbb EY_t=\frac{2\mu_{t-1}}{(t-1)^2}.
\]
These identities remain valid when the two parents happen to coincide, since then neither ordered pair is of the required form.

**Tail first moment.** Put \(Z_N=\sum_{t>N}Y_t\). Absolute convergence follows because \(\mu_q=O(\log q)\). From the previous identity,
\[
\mathbb EZ_N=\sum_{q=N}^{\infty}\frac{2\big(2H_{q-1}-H_{q-1}^{(2)}\big)}{q^2}.
\]
The standard harmonic-number expansions, with their ordinary remainder estimates, give
\[
2\big(2H_{q-1}-H_{q-1}^{(2)}\big)
=4\log q+4\gamma-2\zeta(2)+O(q^{-1}).
\]
Integral comparison (or Euler summation) gives
\[
\sum_{q=N}^{\infty}\frac1{q^2}=N^{-1}+O(N^{-2}),\qquad
\sum_{q=N}^{\infty}\frac{\log q}{q^2}=\frac{\log N+1}{N}+O\!\left(\frac{\log N}{N^2}\right).
\]
Thus
\[
\mathbb EZ_N=\frac{4\log N+4+4\gamma-2\zeta(2)}N+O\!\left(\frac{\log N}{N^2}\right).
\]

**Two-arrival control.** If \(3\le s<t\), the occurrence of \(Y_s=1\) forces vertex \(s\) to become a new root neighbour, so \(D_s=D_{s-1}+1\) on that event. Independence of later root-adjacency indicators and the conditional triangle probability imply the **exact** pair identity
\[
\mathbb E(Y_sY_t)=\frac{4}{(s-1)^2(t-1)^2}\left\{\mathbb E[D_{s-1}(D_{s-1}+1)]
+\mu_{s-1}\sum_{u=s+1}^{t-1}p_u\right\}.
\]
Here \(\mathbb ED_q^2=\mu_q^2+\sum_{u=2}^q p_u(1-p_u)=O((\log q)^2)\). The expression in braces is therefore at most \(C(1+\log t)^2\) for \(t>s\), for an absolute constant \(C\). More precisely, expanding the two contributions and summing first over \(s\), then over \(t\), using \(\sum_{s>N}(1+\log s)^2/s^2=O((\log N)^2/N)\) and \(\sum_{t>N}t^{-2}=O(N^{-1})\), yields
\[
\sum_{N<s<t}\mathbb E(Y_sY_t)=O\!\left(\frac{(\log N)^2}{N^2}\right).
\]
For clarity, the mixed term satisfies \(\sum_{u=s+1}^{t-1}p_u\le2\log t+C\) and \(\mu_{s-1}\le2\log s+C\); hence its aggregate is controlled by the same product of logarithmic harmonic tails.

By the first two Bonferroni inequalities,
\[
0\le\mathbb EZ_N-\mathbb P(Z_N\ge1)
\le\sum_{N<s<t}\mathbb E(Y_sY_t).
\]
Since \(\{L>N\}=\{Z_N\ge1\}\), combining these estimates proves the stated two-term tail expansion. Also \(\sum_t\mathbb EY_t<\infty\), so the first Borel–Cantelli lemma proves \(L<\infty\) almost surely. The tail-integration identity \(\mathbb EL^a=a\int_0^\infty x^{a-1}\mathbb P(L>x)\,dx\), for \(a>0\), and the positive leading term \(4\log N/N\), yield the stated sharp moment cutoff.

**Expected number of rooted triangles.** Summing \(\mathbb EY_t\) over \(t\), and using the classical double-zeta identities \(\sum_{q\ge1}H_{q-1}/q^2=\zeta(3)\) and \(\sum_{q\ge1}H_{q-1}^{(2)}/q^2=\tfrac34\zeta(4)\), gives \(\mathbb E\sum_tY_t=4\zeta(3)-\tfrac32\zeta(4)\). This is a supporting consequence, not a separate originality claim.

## Verification
The standalone `verify.py` checks the one-arrival and two-arrival formulas against exhaustive enumeration of all \((5!)^2=14{,}400\) directed attachment configurations through vertex \(6\), with exact rational arithmetic. It checks \(15\) marginal and pair moments, plus \(36\) exact finite-window comparison inequalities from an independent dynamic program. Its numerical truncated-tail diagnostics are *not* a proof of the asymptotic expansion. Run with `python3 verify.py`; no dependencies beyond the Python standard library. The unrestricted result follows from the analytic estimates above.

## Relationship to prior work
Briend, Calvillo and Lugosi (2022), arXiv:2207.14601v1, study root inference in recursive DAGs using double cycles, and explicitly discuss why triangles are an unreliable alternative (Remark 1); they do not state the last-birth-time law for *rooted simple triangles*. Janson (2023), arXiv:2302.12467v1, concerns descendant counts, not the birth time of rooted cycles. Björklund, Holmgren, Janson and Lo (2023), arXiv:2311.04184v1, give asymptotic approximations for *global* counts of cycles and other subgraphs in uniform attachment **multigraphs** (their Example 2.1, Theorems 3.1 and 3.5), but not the root-marked last-arrival tail; their global triangle-count order does not determine this statistic. These are statement-and-implication comparisons, not uniqueness proofs.

## Limitations
The result concerns two independently sampled parents per arrival, with parallel edges collapsed when counting **distinct simple triangles**. It does not establish an analogous theorem for arbitrary parent counts, multigraph-copy multiplicity, or last arrivals of other motifs. The priority assessment is based on inspected primary results and searches and is not an independent comprehensive bibliographic certification. No independent audit has been performed.

## References
- S. Briend, F. Calvillo and G. Lugosi, *Archaeology of random recursive dags and Cooper-Frieze random networks*, arXiv:2207.14601v1 (29 July 2022), especially Remark 1 and Section 3.
- S. Janson, *The number of descendants in a random directed acyclic graph*, arXiv:2302.12467v1 (24 February 2023), Introduction and main theorem.
- J. Björklund, C. Holmgren, S. Janson and B. Lo, *Approximation of Subgraph Counts in the Uniform Attachment Model*, arXiv:2311.04184v1 (7 November 2023), Example 2.1 and Theorems 3.1 and 3.5.

# Clique-bouquet flooding: a sharp \(\log\log n\) shift and a harmonic source penalty

## Finding

Let \(G_{n,m}=K_1\vee(nK_m)\) be \(n\) disjoint cliques of order \(m\), all joined to the same hub \(o\), with \(n,m\ge1\). Put independent rate-one exponential passage times on **every edge**. Let \(T^o_{n,m}\) be the first-passage flooding time from the hub, and \(T^v_{n,m}\) that from any fixed nonhub vertex. Write \(r_k=k(m+1-k)\), and let \(E_k\) be mutually independent exponentials of rates \(r_k\) for \(1\le k\le m\). Let \(Y_m=\sum_{k=1}^m E_k\). Let \(J\) be uniform on \(\{1,\ldots,m\}\), independent of these exponentials, and let \(M_q\) be the maximum of \(q\) independent copies of \(Y_m\), independent of \((J,E_1,\ldots,E_m)\), with \(M_0=0\). For every finite \(n,m\),

\[
T^o_{n,m}\overset d=M_n,\qquad
T^v_{n,m}\overset d=
\sum_{k=1}^{J}E_k+
\max\left\{\sum_{k=J+1}^{m}E_k,M_{n-1}\right\}.
\]

In particular, the hub-source law has exact cumulative distribution function \(\Pr(T^o_{n,m}\le t)=\Pr(Y_m\le t)^n\) for all \(t\ge0\), and \(\mathbb E e^{-sY_m}=\prod_{k=1}^m r_k/(r_k+s)\) for \(s\ge0\).

For each **fixed** integer \(m\ge2\) and \(n\to\infty\), put
\[
b_{n,m}=\frac{\log n+\log\log n+2\log(m-1)}m.
\]
If \(G\) is standard Gumbel, \(\Pr(G\le x)=\exp(-e^{-x})\), and \(H_m=\sum_{k=1}^m1/k\), then
\[
m(T^o_{n,m}-b_{n,m})\Longrightarrow G,
\qquad
m(T^v_{n,m}-b_{n,m})\Longrightarrow G+mH,
\]
where \(H=\sum_{k=1}^J E_k\) and \(G\) is independent of \(H\). Moreover,
\[
\mathbb E T^o_{n,m}=b_{n,m}+\frac{\gamma}{m}+o(1),
\qquad
\mathbb E T^v_{n,m}-\mathbb E T^o_{n,m}\longrightarrow\frac{H_m}{m}.
\]
Here \(\gamma\) is Euler's constant. The limiting leaf-source law is a genuine convolution rather than just a shifted Gumbel.

The boundary \(m=1\) is different: \(G_{n,1}\) is a star, and \(T^o_{n,1}\) is a maximum of \(n\) independent rate-one exponentials, hence has Gumbel centering \(\log n\) with **no** \(\log\log n\) term. Its exact leaf-versus-hub expected penalty is \(1-1/n\).

## Assumptions and scope

The graph has one hub joined to all vertices in \(n\) pairwise disjoint complete \(m\)-vertex petals. Edge passage times are independent \(\operatorname{Exp}(1)\) random variables sampled once, and distance is the minimum total weight over all graph paths. Flooding time is the maximum such distance from the stated source. There is no recovery, reinfection or dynamically varying graph. The finite identities are for every \(n,m\ge1\); the asymptotic laws fix \(m\) before taking \(n\to\infty\).

## Proof

**1. Exact passage-time decomposition.** An independent exponential-edge first-passage exploration from an infected set is a continuous-time pure-birth infection: each edge with exactly one infected endpoint has an independent residual rate-one clock. In a complete graph of order \(m+1\), when exactly \(k\) vertices have been infected, there are exactly \(r_k=k(m+1-k)\) edges crossing the cut. Consequently the successive holding times are independent \(E_k\sim\operatorname{Exp}(r_k)\). Their sum is \(Y_m\).

When the source is the hub, petals share no other vertices or edges. The passage times restricted to distinct petals are independent. All petals have been covered precisely when the last petal finishes, proving the first distributional identity and the Laplace transform.

When the source \(v\) belongs to one petal, all infection remains within its clique of order \(m+1\) until the hub is reached. At its \(k\)-th infection, the newly infected vertex is uniformly distributed among the still susceptible vertices, independently of the holding time, because all cut edges have the same rate. Hence the hub's rank \(J\) among the \(m\) subsequently infected vertices is uniform, independently of the successive holding times. The time to reach the hub is \(H=\sum_{k=1}^J E_k\); the remaining clearance time in the source petal, measured from hub infection, is \(R=\sum_{k=J+1}^m E_k\). Once the hub is reached, all other petals start independent fresh infections with completion times distributed as \(Y_m\), independent of \((J,E_k)\). This proves the second identity, including the possible case \(n=1\).

**2. An exact tail constant.** For \(m\ge2\), the slowest rate \(r_k=m\) occurs at exactly \(k=1,m\). All the internal rates satisfy \(r_k>m\) when \(2\le k\le m-1\). Write \(Y_m=X+Z\), with \(X\) the sum of two independent rate-\(m\) exponentials and \(Z\) the independent sum over internal stages (zero if \(m=2\)). The moment-generating factor at the slow rate telescopes:
\[
\mathbb E e^{mZ}
=\prod_{k=2}^{m-1}\frac{k(m+1-k)}{k(m+1-k)-m}
=\prod_{k=2}^{m-1}\frac{k}{k-1}\frac{m+1-k}{m-k}
=(m-1)^2.
\]
Since \(\Pr(X>t)=(1+mt)e^{-mt}\) and \(Z\) has a strictly faster exponential tail, convolution gives
\[
\Pr(Y_m>t)=m(m-1)^2\,t e^{-mt}+O_m(e^{-mt})\qquad(t\to\infty).
\]
For \(m=2\) this holds directly with the exact expression \(\Pr(Y_2>t)=(1+2t)e^{-2t}\).

**3. Extreme-value law and means.** Substituting \(t=b_{n,m}+x/m\) into the preceding tail gives \(n\Pr(Y_m>t)\to e^{-x}\) for each real \(x\). Therefore
\[
\Pr\{m(M_n-b_{n,m})\le x\}
=\bigl(1-\Pr(Y_m>b_{n,m}+x/m)\bigr)^n
\longrightarrow\exp(-e^{-x}).
\]
The same estimate gives two positive constants \(c_m,C_m\) such that \(c_m(1+t)e^{-mt}\le\Pr(Y_m>t)\le C_m(1+t)e^{-mt}\) for all \(t\ge0\). A union bound controls the centered maximum's right tail by an integrable multiple of \((1+x)e^{-x}\). For the left tail, the inequality \((1-u)^n\le e^{-nu}\), split at half the centering, gives a uniform double-exponential tail on the first region and a superpolynomially small probability on the remaining region of length \(O(\log n)\). Thus the centered maxima are uniformly integrable, so their means converge to the Gumbel mean \(\gamma\). This proves the hub expectation formula.

**4. Leaf-source penalty and independence.** The random variables \(H\) and \(R\) have fixed, finite exponential moments in a neighborhood of zero. Since \(M_{n-1}\to\infty\) in probability, \(\max\{R,M_{n-1}\}-M_{n-1}\to0\) in probability and \(L^1\); indeed it is between zero and \(R\mathbf1_{\{R>M_{n-1}\}}\), whose expectation tends to zero. Also \(M_{n-1}\) is independent of \(H\) and has the same Gumbel limit as \(M_n\). Slutsky's theorem gives the stated independent convolution limit and, using the mean convergence in step 3, the source penalty. Finally,
\[
\mathbb EH=\sum_{k=1}^m\Pr(J\ge k)\frac1{r_k}
=\frac1m\sum_{k=1}^m\frac{m-k+1}{k(m-k+1)}
=\frac{H_m}{m}.
\]
For \(m=1\), the exact identities reduce to \(T^o_{n,1}=M_n\) and \(T^v_{n,1}\overset d=E_1+M_{n-1}\). Since \(\mathbb EM_n=H_n\), the final boundary statement follows.

## Verification

Run `python3 verify_windmill.py` with Python 3.9 or later; no third-party packages are required. The program uses an independent full-graph infection-state recurrence with exact rational arithmetic, compares it with exact finite petal-distribution formulas in the triangular-petal case, verifies the harmonic source-delay identity and telescoping factors through a large range of fixed petal sizes, evaluates independent phase-type tails by Poisson uniformization, and compares against seeded simulations of **static exponential edge weights** using Dijkstra's algorithm. A checked execution passed 187 exact or numerical assertions. The analytic proof above, not the finite experiments, establishes the all-size and limiting statements.

## Relationship to prior work

Leskelä and Ngo, *First passage percolation in sparse random graphs with boundary weights* (arXiv:1806.09568, 2018), develop flooding asymptotics for configuration-model networks with bounded \((2+\varepsilon)\)-degree moments. The hub of \(G_{n,m}\) has degree \(nm\), so that assumption fails. Mountford and Saliba, *Flooding and Diameter in General Weighted Random Graphs* (arXiv:1909.04563, 2019), likewise study random configuration-model graphs subject to bounded degree moments and establish leading-order logarithmic laws. Van der Hofstad and Lodewijks, *Long-range first-passage percolation on the complete graph* (arXiv:2311.16088, 2023), study spatial complete graphs rather than a fixed-petal articulation geometry. The elementary clique pure-birth representation and the general Gumbel maximum principle are standard ingredients, not asserted as new. The claimed contribution is their exact joint finite-source classification on clique bouquets, the telescoped \(\log\log n\) centering, and the explicit harmonic source penalty. No universal historical priority is claimed.

## Limitations

The asymptotic statements require fixed \(m\); allowing \(m=m_n\to\infty\) is not covered. All rates are homogeneous and exponential, and the source must be either the unique hub or a nonhub vertex of the prescribed homogeneous graph. Neither a general graph theorem nor an analogous claim for arbitrary edge-weight distributions is proved. The comparisons do not constitute a complete historical novelty guarantee. No independent audit has been performed.

## References

1. L. Leskelä and H. Ngo, *First passage percolation in sparse random graphs with boundary weights*, arXiv:1806.09568 (first posted 2018-06-25), https://arxiv.org/abs/1806.09568.
2. T. Mountford and J. Saliba, *Flooding and Diameter in General Weighted Random Graphs*, arXiv:1909.04563 (first posted 2019-09-10), https://arxiv.org/html/1909.04563v1.
3. R. van der Hofstad and B. Lodewijks, *Long-range first-passage percolation on the complete graph*, arXiv:2311.16088 (first posted 2023-11-27), https://arxiv.org/abs/2311.16088.

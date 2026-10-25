# Three thresholds for the degree of a vertex avoiding short cycles in a random graph

## Finding

Fix \(c>0\) and \(0<\alpha<1\). Let \(G_n\sim G(n,p_n)\), with \(p_n=c n^{-\alpha}\), for integers \(n\) sufficiently large that \(p_n<1\). Distinguish a vertex \(v\); let \(E_n\) be the event that **no triangle and no simple four-cycle contains \(v\)**. Let \(D_n=\deg(v)\). This event is also equivalent to the absence of collisions between the root's distinct neighbors at distances one and two: the neighbors are pairwise nonadjacent and no two share another neighbor.

**Theorem.** Under conditioning on \(E_n\), the following convergences hold in probability:
\[
\begin{array}{ll}
D_n\longrightarrow 1, &0<\alpha<1/2,\\
D_n/\log n\longrightarrow 1/(2c^2), &\alpha=1/2,\\
D_n/(n^{2\alpha-1}\log n)\longrightarrow (2-3\alpha)/c^2, &1/2<\alpha<2/3,\\
D_n/n^{1/3}\longrightarrow W(c^3)/c^2, &\alpha=2/3,\\
D_n/(c n^{1-\alpha})\longrightarrow1, &2/3<\alpha<1.
\end{array}
\]
Here \(W\) is the nonnegative real inverse of \(w\mapsto we^w\). More uniformly, for \(\alpha\ge1/2\), set \(x_n=W(n^2p_n^3)/(np_n^2)\). Then \(D_n/x_n\to1\) in conditional probability.

The conditioning probability has the following additional complete leading-order regimes. Write \(a_c=W(c^3)/c^3\) and \(\phi_c=1-a_c-c^3a_c^2/2\), which is strictly positive. Then
\[
-\log\Pr(E_n)\sim
\begin{cases}
cn^{1-\alpha},&0<\alpha<2/3,\\
c\phi_c n^{1/3},&\alpha=2/3,\\
(c^4/2)n^{3-4\alpha},&2/3<\alpha<3/4.
\end{cases}
\]
At \(\alpha=3/4\), \(\Pr(E_n)\to\exp(-c^4/2)\), and at \(3/4<\alpha<1\), \(\Pr(E_n)\to1\).

At the middle critical point \(\alpha=2/3\), the conditional variable \(D_n/(np_n)\) also satisfies a large-deviation principle on \([0,\infty)\) with speed \(np_n\) and good rate function
\[
I_c(a)=a\log a-a+1+\frac{c^3a^2}{2}-\phi_c,\qquad a\ge0,
\]
where \(0\log0=0\). Its unique zero is \(a_c\).

## Assumptions and scope

All graphs are simple, undirected, and labeled; edges are independent. A four-cycle uses four distinct vertices, and only cycles **containing the distinguished vertex** are forbidden. In particular other parts of the graph need not be triangle-free or square-free. Conditional assertions apply along positive integers \(n\to\infty\), with fixed \(c,\alpha\); they make no uniform-in-parameter assertion.

For every integer \(n\ge2\) and every \(0<p<1\), write \(m=n-1\), \(q=1-p\), and
\[
B_d(p)=\begin{cases}1,&d=0,\\ q^d+dpq^{d-1},&1\le d\le m.\end{cases}
\]
Then the **exact**, not asymptotic, joint weights are
\[
\boxed{\Pr(D_n=d,E_n)=w_{n,p}(d)
=\binom md p^d q^{m-d+\binom d2}B_d(p)^{m-d},\quad 0\le d\le m.}
\]
Hence \(\Pr(D_n=d\mid E_n)=w_{n,p}(d)/\sum_{j=0}^m w_{n,p}(j)\).

## Proof

**1. Exact counting.** Condition on the \(d\) neighbors of \(v\). Avoiding triangles forces all \(\binom d2\) edges inside that set to be absent. Avoiding four-cycles then forces each of the \(m-d\) outside vertices to have *at most one* edge to the \(d\) neighbors. Its probability is \(B_d(p)\). These edge families are disjoint and independent; edges inside the outside set are unrestricted. This proves the weight formula. Conversely, if both conditions hold, no triangle or four-cycle through \(v\) exists.

For \(1\le d\le m-1\), cancellation yields the exact adjacent weight ratio
\[
\boxed{\frac{w_{n,p}(d+1)}{w_{n,p}(d)}=
\frac{(m-d)p}{(d+1)(1+(d-1)p)}
\left(1-\frac{dp^2}{1+(d-1)p}\right)^{m-d-1}.}
\tag{1}
\]
The separate ratio at zero is \(w(1)/w(0)=mp/q\). These expressions are positive for \(0<p<1\).

**2. Sparse-degree collapse.** Suppose \(\alpha<1/2\). Set \(\lambda=np\), so \(\lambda\to\infty\), \(np^2\gg\log n\), and \(\lambda=o(n)\). Uniformly for integers \(1\le d\le\lfloor\lambda\rfloor\), equation (1), \(1-u\le e^{-u}\), and the monotonicity of \(d/(1+(d-1)p)\) give
\[
\frac{w(d+1)}{w(d)}\le \lambda\exp\bigl(-(1-o(1))np^2/(1+p)\bigr)=o(1).
\]
For \(d>\lambda\), equation (1) gives \(w(d+1)/w(d)\le\lambda/(d+1)<1\). The first \(\lfloor\lambda\rfloor\) ratios are uniformly exponentially small in \(np^2\), and the remaining \(O(n)\) terms cannot compensate. Consequently \(\sum_{d\ge2}w(d)=o(w(1))\). Also \(w(0)/w(1)=q/(mp)=o(1)\). Thus \(\Pr(D_n=1\mid E_n)\to1\).

**3. The Lambert saddle.** Suppose \(\alpha\ge1/2\), and let \(\lambda=np\), \(\beta=np^2\), \(z=n^2p^3=\lambda\beta\). The positive solution of
\[
\log(\lambda/x)=\beta x
\]
is \(x=x_n=W(z)/\beta\). For all such \(\alpha\), \(x\to\infty\), \(x=o(n)\), and \(px\to0\). Expanding the logarithm of (1) uniformly for integer \(1\le d\le(1+\varepsilon)x\), for any fixed \(\varepsilon>0\), gives
\[
\log\frac{w(d+1)}{w(d)}
=\log\frac{\lambda}{d+1}-\beta d+o(1).
\tag{2}
\]
Indeed the discarded contributions are bounded by constants times \(p+d/n+\beta d\,(pd+d/n+p)+n d^2p^4\), all tending to zero uniformly in that range, since \(\beta x=W(z)=O(\log n)\), \(px\to0\), and \(x/n\to0\). Formula (2) shows that, for every fixed \(\varepsilon\in(0,1)\), the successive ratios exceed \(1+\delta_\varepsilon\) below \((1-\varepsilon)x\), and fall below \(1-\delta_\varepsilon\) between \((1+\varepsilon/2)x\) and \((1+\varepsilon)x\), for some \(\delta_\varepsilon>0\) and all large \(n\).

For the remaining right tail \((1+\varepsilon)x\le d\le\lambda\), the exact ratio satisfies
\[
\log\frac{w(d+1)}{w(d)}\le
\log\frac\lambda{d+1}
-\frac{(n-d-2)dp^2}{1+(d-1)p}.
\tag{3}
\]
The right side is bounded above by the decreasing function \(\log(\lambda/d)-(1-o(1))\beta d/(1+dp)\), whose value at \((1+\varepsilon)x\) is at most a fixed negative constant. For \(d>\lambda\), (1) directly gives \(w(d+1)/w(d)\le\lambda/(d+1)<1\). Geometric bounds from (2)–(3) make the total mass outside \([(1-\varepsilon)x,(1+\varepsilon)x]\) negligible relative to the mass inside, proving \(D_n/x_n\to1\) under conditioning.

Using \(W(t)\sim t\) as \(t\downarrow0\), \(W(t)\sim\log t\) as \(t\to\infty\), and \(W(c^3)>0\), yields the four asserted scales for \(\alpha\ge1/2\). This also proves that all five degree regimes hold.

**4. Probability when \(\alpha<2/3\).** The single-neighbor weight gives \(\Pr(E_n)\ge w(1)=mpq^{m-1}=\exp(-(1+o(1))\lambda)\). Conversely fix \(\varepsilon\in(0,1)\) and divide the event according to \(D_n\le\varepsilon\lambda\) and its complement. A binomial Chernoff estimate bounds the first part by \(\exp[-\lambda(1-\varepsilon+\varepsilon\log\varepsilon+o(1))]\). On \(\varepsilon\lambda<D_n\le n/2\), the outside-vertex factor is bounded by
\[
B_d(p)^{m-d}\le \exp\bigl[-c_\varepsilon n\min\{(\lambda p)^2,\lambda p\}\bigr],
\]
using \(B_d(p)=q^{d-1}(1+(d-1)p)\) and the elementary inequality \(t-\log(1+t)\ge c\min(t^2,t)\). Its exponent is \(\omega(\lambda)\) because \(\lambda p=np^2\) and \(\alpha<2/3\). On \(D_n>n/2\), the missing triangle edges contribute at most \(\exp(-pn^2/9)=\exp(-\omega(\lambda))\). Letting \(\varepsilon\downarrow0\) proves \(-\log\Pr(E_n)\sim\lambda\).

**5. The middle critical large deviations.** At \(\alpha=2/3\), \(\lambda=c n^{1/3}\), \(z=c^3\), and, uniformly for \(d/\lambda\) in a compact subset of \([0,\infty)\), Stirling's formula and the exact weights give
\[
\frac1\lambda\log w(d)
= -\left[a\log a-a+1+\frac{c^3a^2}2\right]+o(1),
\qquad a=d/\lambda.
\]
The bracket has unique minimizer \(a_c=W(c^3)/c^3\) and minimum \(\phi_c=1-a_c-c^3a_c^2/2>0\). Binomial Chernoff tails give exponential tightness at speed \(\lambda\); discrete Laplace upper and lower bounds therefore prove both the claimed good conditional large-deviation principle and \(-\log\Pr(E_n)\sim\lambda\phi_c\).

**6. The last rarity transition.** If \(\alpha>2/3\), then under the *unconditioned* binomial law \(D_n/\lambda\to1\). For degrees in a fixed relative neighborhood of \(\lambda\), \(dp=o(1)\), and expansion of the exact conditional constraint gives uniformly
\[
\log\bigl(q^{\binom d2}B_d(p)^{m-d}\bigr)
=-\frac{n d^2p^2}{2}(1+o(1)).
\]
The exponent at \(d\sim\lambda\) is \(K_n=n^3p^4/2\), with \(K_n=o(\lambda)\). Binomial large-deviation bounds show the atypical-degree contribution is \(\exp(-\Omega(\lambda))\). Sandwiching by the typical-degree window and then shrinking its relative width proves \(-\log\Pr(E_n)\sim K_n\) when \(2/3<\alpha<3/4\), and \(\Pr(E_n)\to e^{-c^4/2}\) when \(\alpha=3/4\). Finally, for \(\alpha>3/4\), the expected number of triangles or four-cycles containing the root is \(O(n^2p^3+n^3p^4)=o(1)\); Markov's inequality gives \(\Pr(E_n)\to1\).

## Verification

A standalone exact checker, `verify.py`, enumerates all labeled simple graphs on \(2\) through \(6\) vertices, detects root triangles and root four-cycles directly, and compares every degree-and-edge-count coefficient with a second closed count. It also checks the rational joint weights at three probabilities and independently checks every admissible adjacent-ratio identity. Running `python verify.py` yields **285 exact assertions passed**. These finite checks supplement, not replace, the unrestricted proofs above.

## Relationship to prior work

Janson and Ruciński (2009), arXiv:0905.0972, investigate **upper tails** of rooted subgraph counts, including examples of cycles. Their Theorem 3.1 and Examples 3.3–3.5 concern upper-tail events and do not specify a root-degree law conditional on simultaneous zero counts of rooted triangles and squares. Stark and Wormald (2016), arXiv:1608.05193, derive probabilities for **absence of a fixed subgraph throughout the entire graph**, not a joint single-vertex avoidance event or conditional degree phase diagram. Prior single-root triangle exclusion yields a different exact weight lacking the factor \(B_d(p)^{m-d}\); it cannot imply the additional square-avoidance transition at \(\alpha=2/3\). The elementary conditional edge decomposition is compatible with broad classical theory but the full combination and priority remain subject to outside checking.

## Limitations

The critical large-deviation result holds only at \(\alpha=2/3\). No central limit theorem or explicit error bound is established for conditional degrees. The rare-event probability at \(\alpha<2/3\) is determined only logarithmically; finer prefactors are not claimed. The event is rooted avoidance, not global girth at least five. Scientific priority beyond the inspected literature remains uncertain; the exact law could be derivable from more general earlier enumeration.

## References

1. S. Janson and A. Ruciński, *Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs*, arXiv:0905.0972, first posted 2009-05-07, https://arxiv.org/abs/0905.0972.
2. D. Stark and N. Wormald, *The probability of nonexistence of a subgraph in a moderately sparse random graph*, arXiv:1608.05193, first posted 2016-08-18, https://arxiv.org/abs/1608.05193.

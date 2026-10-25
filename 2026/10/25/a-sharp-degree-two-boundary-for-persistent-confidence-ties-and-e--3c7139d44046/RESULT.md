# A sharp degree-two boundary for persistent confidence ties and exact cycle dissipation

## Finding

For the asynchronous self-inclusive social Hegselmann–Krause model on a finite undirected simple graph \(G\), the following universal graph property holds:

> For **every** real Euclidean opinion dimension \(d\geq1\), confidence radius \(\varepsilon>0\), initial opinion configuration and finite sequence of activated vertices, an influence edge that is active at one time is active at all subsequent times.

The property holds **if and only if** the maximum vertex degree satisfies \(\Delta(G)\leq2\). Thus precisely disjoint unions of paths, cycles and isolated vertices have irreversible confidence ties under arbitrary asynchronous activation. Their influence graphs can change strictly at most \(|E(G)|\) times, exclusively by gaining edges.

Furthermore, on a cycle \(C_n\), \(n\geq3\), when all social edges are initially active and vertices are selected independently and uniformly at random, the conditional Dirichlet-energy contraction is sharp:

\[
\mathbb E[\mathcal E_{t+1}\mid x_t]\leq q_n\,\mathcal E_t,\qquad
q_n=1-\frac{16\sin^2(\pi/n)}{9n}.
\]

The factor \(q_n\) is the smallest uniform valid one-step factor over all nonconstant states with every edge active. For \(0<\delta<\varepsilon\), the first time \(T_\delta\) at which all social edges have length at most \(\delta\) satisfies

\[
\Pr(T_\delta>t)\leq
\min\!\left\{1,\frac{\mathcal E_0}{\delta^2}q_n^t\right\}
\qquad(t=0,1,2,\ldots).
\]

Here \(\mathcal E_t=\sum_{\{u,v\}\in E(C_n)}\|x_t(u)-x_t(v)\|_2^2\). In particular, almost-sure consensus holds on an initially active cycle, with an explicit geometric tail for reaching each positive tolerance.

## Assumptions and scope

The social network \(G=(V,E)\) is finite, simple, undirected; its maximum degree is \(\Delta(G)\). Every vertex \(v\) has opinion \(x_t(v)\in\mathbb R^d\). The confidence radius \(\varepsilon>0\) is fixed throughout. An edge \(\{u,v\}\in E\) belongs to the influence graph \(I_t\) precisely when \(\|x_t(u)-x_t(v)\|_2\leq\varepsilon\); ties at the threshold count as active. On activation of a single vertex \(v\), define \(A_t(v)=\{u:\{u,v\}\in I_t\}\) and update

\[
x_{t+1}(v)=\frac{x_t(v)+\sum_{u\in A_t(v)}x_t(u)}{1+|A_t(v)|},
\]

leaving all other opinions unchanged. The universal persistence assertion concerns **all** possible activation choices and initial states; no randomness is assumed for it. The cycle dissipation and probability statements assume independent uniform vertex activations and \(I_0=G=C_n\). The graph characterization and its proof also work for opinions in any real normed vector space, with norm replacing Euclidean distance; the energy statements use Euclidean squared norm.

## Proof

**1. Local contact persistence at degree two.** Suppose \(\{u,v\}\) is active and vertex \(v\) is selected. Write \(a=x_t(u)\), \(b=x_t(v)\). If \(v\) has no other active neighbor, the new opinion at \(v\) is \((a+b)/2\), and the new edge length is half the old one. If \(v\) has exactly one other active neighbor \(w\) with opinion \(c\), then

\[
\left\|\frac{a+b+c}{3}-a\right\|
\leq\frac{\|b-a\|+\|c-a\|}{3}
\leq\frac{\varepsilon+2\varepsilon}{3}=\varepsilon,
\]

where \(\|c-a\|\leq\|c-b\|+\|b-a\|\leq2\varepsilon\). If another vertex, rather than \(u\) or \(v\), is activated, the distance along \(\{u,v\}\) is unchanged. Thus each active edge survives every update whenever both endpoints have graph degree at most two. Induction yields \(I_t\subseteq I_{t+1}\) for all \(t\), with at most \(|E|\) strict additions.

**2. Sharp converse.** If a vertex \(v\) has degree \(k\geq3\), assign scalar opinions \(x(v)=0\), \(x(u)=-\varepsilon\) to one neighbor \(u\), and \(+\varepsilon\) to each of the other \(k-1\) neighbors. Opinions on all other vertices are arbitrary. All \(k\) edges incident to \(v\) are active. Updating \(v\) once moves it to \((k-2)\varepsilon/(k+1)>0\). The previously active edge \(\{u,v\}\) then has length

\[
\varepsilon\left(1+\frac{k-2}{k+1}\right)>\varepsilon,
\]

so it is lost. The smallest connected witness is the four-vertex star, whose center moves from \(0\) to \(\varepsilon/4\) with neighbor opinions \((-\varepsilon,+\varepsilon,+\varepsilon)\). Therefore the universal contact-persistence property is equivalent to \(\Delta(G)\leq2\).

**3. Exact one-vertex energy identity.** For a fully active social network, let \(d_v\) be the degree of \(v\), let \(L\) be its usual combinatorial graph Laplacian, and write \(S_v=\sum_{u\sim v}(x(v)-x(u))=(Lx)_v\). The asynchronous update is \(x'(v)=x(v)-S_v/(d_v+1)\). Only edges incident to \(v\) change. Expanding their squared lengths gives the exact identity

\[
\mathcal E(x)-\mathcal E(x')=
\frac{d_v+2}{(d_v+1)^2}\|S_v\|_2^2.
\]

This holds in every finite Euclidean dimension and includes the zero-gradient case.

**4. Cycle contraction and optimal constant.** On \(C_n\), all degrees are two, and by Part 1 no edge ceases to be active. Averaging Part 3 over the \(n\) equally likely choices gives the *equality*

\[
\mathbb E[\mathcal E_{t+1}\mid x_t]
=\mathcal E_t-\frac{4}{9n}\sum_{v\in V}\|(Lx_t)_v\|_2^2.
\]

The cycle Laplacian has eigenvalues \(4\sin^2(\pi j/n)\) for \(0\leq j<n\), and its least positive eigenvalue is \(\lambda_2=4\sin^2(\pi/n)\). Spectral decomposition gives

\[
\sum_v\|(Lx)_v\|_2^2\geq\lambda_2\sum_{\{u,v\}\in E}\|x(u)-x(v)\|_2^2.
\]

This proves the announced coefficient \(q_n=1-4\lambda_2/(9n)\). Equality is attained at any nonconstant first-harmonic state \(x(v)=c+\eta\cos(2\pi v/n)\,e\), where \(e\) is a unit opinion vector, \(c\) any fixed vector, and \(0<\eta<\varepsilon/2\). Such a state has all edges active, proving *one-step* sharpness. No claim of equality in the multi-step tail is made.

**5. Hitting-time bound.** Iterating conditional expectation yields \(\mathbb E\mathcal E_t\leq q_n^t\mathcal E_0\). Whenever \(T_\delta>t\), at least one edge at time \(t\) has length greater than \(\delta\), hence \(\mathcal E_t>\delta^2\). Markov's inequality yields the displayed probability bound. Since \(0<q_n<1\), every positive tolerance is reached almost surely, and by intersecting the probability-one events over \(\delta=1,1/2,\ldots\) (restricted to \(\delta<\varepsilon\)) all neighbor differences tend to zero. Cycle connectivity implies consensus in the sense that all pairwise opinion distances tend to zero.

## Verification

A standalone, dependency-free Python program `hk_contact_monotonicity_verifier.py` checks 163,105 exact rational first-update cases over every labeled simple graph with at most four vertices and integer opinions in \([-2,2]\), confirms breaking-edge constructions for 23 labeled graphs with a vertex of degree at least three, and runs 84,000 further exact rational updates on paths and cycles. It also checks the analytic cycle contraction factor numerically on 16 cycle lengths \(3\) through \(18\), using first-harmonic test states. It prints `PASS` on success. These finite checks are secondary evidence, not a proof of the graph-family or spectral theorems.

## Relationship to prior work

Berenbrink et al. (2022), arXiv:2201.12923, analyze precisely the asynchronous self-inclusive social Hegselmann–Krause model and establish expected \(\delta\)-stability bounds on arbitrary networks. Their Section 3, Theorem 5 treats the special case in which the influence graph is assumed to remain equal to the social graph and cites an initially equally spaced path as an example. The present theorem instead **characterizes all graphs on which every initially active tie persists for every state and every activation sequence**, and derives the explicit optimal one-step cycle energy factor. Their conditional bound is not an equivalent graph characterization.

Parasnis, Franceschetti and Touri (2019), arXiv:1909.03485, analyze *synchronous* social Hegselmann–Krause updates, with links that may merge or break, and obtain conditional spectral estimates and bounds for slowly merging structures. Synchronous averaging is not the single-vertex protocol analyzed here; its conditional graph-stability claims do not establish the degree-two if-and-only-if criterion.

Li, Luo and Porter (2023), arXiv:2303.07563, study changing dyadic confidence bounds, with synchronous Hegselmann–Krause and asynchronous pairwise Deffuant–Weisbuch updates. Those dynamics do not give the fixed-confidence, single-vertex mean-update statement above. Standard Fourier diagonalization of a fixed cycle Laplacian is used here after proving full contact persistence; this spectral ingredient alone is not claimed as new.

## Limitations

The contact-persistence classification depends on the **self-inclusive arithmetic mean**, one activated vertex at a time, a fixed common symmetric confidence radius and an undirected social graph. Pairwise Deffuant updating, synchronous updating, stubborn agents, changing trust thresholds, or weighted means are not covered. The rate formula requires initially active *all* edges of a cycle, not an arbitrary initially fragmented cycle. The exact rate refers to worst-case conditional **one-step** Dirichlet-energy contraction, not the true asymptotic Lyapunov exponent or the optimal multi-step tail constant. A literature-equivalent presentation outside the inspected sources remains possible; no independent review has been performed.

## References

1. P. Berenbrink, M. Hoefer, D. Kaaser, P. Lenzner, M. Rau and D. Schmand, *Asynchronous Opinion Dynamics in Social Networks*, arXiv:2201.12923, first posted 2022-01-30. https://arxiv.org/abs/2201.12923
2. R. Parasnis, M. Franceschetti and B. Touri, *On the Convergence Properties of Social Hegselmann-Krause Dynamics*, arXiv:1909.03485, first posted 2019-09-08. https://arxiv.org/abs/1909.03485
3. G. J. Li, J. Luo and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, first posted 2023-03-14. https://arxiv.org/abs/2303.07563

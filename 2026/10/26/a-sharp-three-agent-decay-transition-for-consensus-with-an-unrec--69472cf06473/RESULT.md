# A sharp three-agent decay transition for consensus with an unreceptive dyad

## Finding

In the synchronous adaptive-confidence Hegselmann–Krause (HK) model of Li, Luo, and Porter on the complete three-vertex network, let initially ordered opinions satisfy \(0<x_1(0)<x_2(0)<x_3(0)<1\). Set \(u=x_2(0)-x_1(0)\), \(v=x_3(0)-x_2(0)\), and \(D=u+v\). If the common initial confidence is \(\max\{u,v\}<c_0\le D\), the initial effective network is precisely the path \(1-2-3\). For every \(0<\gamma\le1\), the confidence-decay factor \(\delta\) has a **sharp transition at \(1/2\)**:

1. When \(0<\delta\le1/2\), the outer dyad \((1,3)\) remains unreceptive at **every finite time**, although all three opinions tend to the same limit \(m=(2x_1(0)+3x_2(0)+2x_3(0))/7\). Its confidence is exactly \(c_{13}(t)=c_0\delta^t\to0\); the two receptive confidences tend to \(1\). No finite-time exact opinion consensus occurs under the strict initial ordering.
2. When \(1/2<\delta<1\), the outer dyad becomes receptive for the first time at the exact integer
   \[
   t_* =\min\{t\in\mathbb Z_{\ge0}:(2\delta)^t>D/c_0\}
        =\left\lfloor\frac{\log(D/c_0)}{\log(2\delta)}\right\rfloor+1.
   \]
   All three opinions become **exactly equal at time \(t_*+1\)**, to
   \[
   m+\frac{v-u}{21}\left(-\frac16\right)^{t_*}.
   \]
   Every dyadic confidence subsequently tends to \(1\).

In this model, **three vertices are minimal** for a mutually unreceptive dyad whose agents nevertheless have the same limiting opinion. The \(\delta<1/2\) regime includes a nonempty open set of initial opinions, confidence bounds, and confidence-update parameters, rather than an isolated trajectory. The result is a precise sufficient-and-necessary classification **within the stated initial path sector**, not a classification of arbitrary three-agent initial configurations.

## Assumptions and scope

The underlying graph is the **complete** undirected graph \(K_3\), so dyad \((1,3)\) exists even when absent from the time-dependent **effective** graph. At integer time \(t\), define the receptive indicator by the *strict* test \(|x_i(t)-x_j(t)|<c_{ij}(t)\). Every opinion is synchronously replaced by the arithmetic mean of itself and all receptive neighbors. After testing receptiveness at time \(t\), update each confidence by
\[
c_{ij}(t+1)=\begin{cases}
c_{ij}(t)+\gamma[1-c_{ij}(t)]&\text{if receptive},\\
\delta c_{ij}(t)&\text{otherwise}.
\end{cases}
\]
Initially \(c_{ij}(0)=c_0\) for all three dyads, with \(0<c_0<1\), \(0<\gamma\le1\), and \(0<\delta<1\). The stated strict ordering and gap condition imply \(u,v>0\), and the two adjacent dyads initially receptive while the outer dyad is not. The equality case \(c_0=D\) is excluded from outer receptiveness by the strict test. The result holds for every real-valued initial tuple satisfying these constraints, not only rational examples.

## Proof

**Path invariance until the first outer activation.** On the effective path \(1-2-3\), the synchronous self-inclusive opinion matrix is
\[
P=\begin{pmatrix}
1/2&1/2&0\\
1/3&1/3&1/3\\
0&1/2&1/2
\end{pmatrix}.
\]
Let \(u_t=x_2(t)-x_1(t)\), \(v_t=x_3(t)-x_2(t)\). While that path is effective, direct subtraction gives
\[
u_{t+1}=\frac{u_t+2v_t}{6},\qquad
v_{t+1}=\frac{2u_t+v_t}{6}.
\]
Consequently \(u_t,v_t>0\), and both are at most \(\max\{u,v\}/2^t<c_0\) by induction. The receptive confidence updates obey \(c_{12}(t)=c_{23}(t)=1-(1-c_0)(1-\gamma)^t\ge c_0\); thus the two path edges cannot lose receptiveness while the outer edge is absent. Also,
\[
u_t+v_t=\frac{D}{2^t},\qquad
u_t-v_t=(u-v)\left(-\frac16\right)^t.
\]
Therefore, at every time before the first activation, \(|x_3(t)-x_1(t)|=D/2^t\) and \(c_{13}(t)=c_0\delta^t\). The absent edge becomes receptive **if and only if** \((2\delta)^t>D/c_0\).

**Decay transition.** If \(2\delta\le1\), the last inequality never holds because \(D/c_0\ge1\). Induction proves permanent effective-path dynamics and \(c_{13}(t)\to0\). The positive gaps both tend to zero, so all opinions converge to a common value without becoming equal at any finite time. The left stationary vector of \(P\) is \((2,3,2)/7\), which yields the stated weighted mean \(m\). If \(2\delta>1\), the strict inequality first holds at the given \(t_*\). All three dyads then influence opinions, so the next synchronous update replaces every opinion with the arithmetic mean of the three opinions at \(t_*\). This equal state is invariant and all dyads remain receptive thereafter.

**Value of the consensus.** Before activation, \(2x_1(t)+3x_2(t)+2x_3(t)=7m\). Using the gap difference, the ordinary three-opinion average satisfies
\[
\frac{x_1(t)+x_2(t)+x_3(t)}3
=m+\frac{v-u}{21}\left(-\frac16\right)^t.
\]
Evaluating at \(t=t_*\) gives the displayed exact finite-time consensus. The confidence conclusions follow by iterating the relevant affine updates.

**Minimality.** A graph on fewer than three vertices has at most one dyad. On two vertices, an initially receptive dyad causes exact agreement after the first synchronous averaging step and remains receptive because its confidence is positive. An initially unreceptive dyad causes no opinion change; its two opinions can then have the same limit only if they were initially identical, which would make them receptive since \(c_0>0\). Thus the phenomenon is impossible below three vertices. For \(0<\delta<1/2\), the strict inequalities \(u>0\), \(v>0\), \(\max(u,v)<c_0<D\) define a nonempty open set with permanent nonreceptiveness and limiting agreement.

## Verification

The supplied \(\texttt{verify.py}\) uses the standard library's exact rational arithmetic to independently implement the strict confidence test, simultaneous opinion averaging, and adaptive confidence updates. It checks all trajectory identities, initial-sector inequalities, receptive statuses, first activation, permanent missing edges, and exact consensus values in 72 admissible parameter families for 15 updates each. It additionally checks the critical equality case and the explicit finite activation example. These computations corroborate, rather than replace, the all-real-parameter analytical argument above.

For example, with \((x_1(0),x_2(0),x_3(0))=(1/10,2/5,4/5)\), \(c_0=1/2\), and \(\gamma=1/3\), \(\delta=2/5\) gives eternal effective-path interaction and limit \(3/7\), while \(\delta=3/5\) gives \(t_*=2\) and exact consensus at \(t=3\) with opinion \(463/1080\).

## Relationship to prior work

Li, Luo, and Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, formulate precisely this synchronous adaptive-confidence rule (their equations (2.2)–(2.3)); their Theorems 3.2 and 3.6 give general limiting-confidence and effective-graph stabilization properties. Their simulations explicitly exhibit and discuss same-limit, nonreceptive dyads; they do **not** present the exact three-agent construction, the sharp \(\delta=1/2\) phase threshold, first activation time, or minimality proof above in their analyzed mathematical statements. The phenomenon itself and the dynamics are credited to those authors. The manuscript by Kan, Feng, and Porter concerns adaptive network **rewiring** in an asynchronous bounded-confidence model, rather than the dyadic-confidence evolution studied here. Classical stochastic-matrix consensus accounts for the path's stationary weighted mean but not the adaptive-threshold dichotomy.

## Limitations

This theorem is confined to the complete three-agent network with the specific initial effective-path sector, synchronous self-inclusive averaging, homogeneous initial confidence, and multiplicative decay of unreceptive confidences. It does not characterize arbitrary initial confidence heterogeneity, other network sizes, asynchronous Deffuant–Weisbuch updates, noisy opinions, rewiring, or the probability of the behavior under random initial data. The sharp \(1/2\) threshold is **sector-specific**, not universal across adaptive-confidence systems. Publication-priority comparison is based on inspected primary literature and mathematical search, not an exhaustive proof of novelty; no independent mathematical validation has been performed.

## References

1. Grace J. Li, Jiajie Luo, and Mason A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563 (first public version, March 14, 2023); *SIAM Journal on Applied Dynamical Systems* **24** (2025), 994–1041, DOI: 10.1137/23M1558951. Public author manuscript: https://www.math.ucla.edu/~mason/papers/BCM-dynamic-April2025.pdf
2. Grace J. Li, dissertation, 2024, Chapter 5 on adaptive-confidence opinion dynamics, https://escholarship.org/uc/item/2rg9t8zw
3. Kaidi Kan, Weituo Feng, and Mason A. Porter, *An Adaptive Bounded-Confidence Model of Opinion Dynamics on Networks*, *Journal of Complex Networks* (2023), DOI: 10.1093/comnet/cnac055; arXiv:2112.05856.

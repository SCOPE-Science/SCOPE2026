# A sharp three-agent confidence threshold between consensus and persistent opinion fluctuations

## Finding

For the pure neighborhood Deffuant–Weisbuch (NDW) model of Krishnagopal and Porter on the fixed three-vertex path, the initial **leaf gap alone** determines a sharp global phase transition. Let the ordered initial opinions be \(0\le a_0\le c_0\le b_0\le1\), with \(a_0<b_0\); write \(d=b_0-a_0>0\). Each time step selects independently and uniformly one of the two path edges. With one-edge updating, homogeneous confidence \(0<\epsilon\le1\), pure neighborhood tuning \(\sigma=0\), and compromise strength \(0<\rho\le1/2\), the following dichotomy holds.

**Closed-leaf regime:** if \(\epsilon\le d/2\), both leaf opinions stay exactly at \(a_0,b_0\). The center opinion does not converge almost surely, but its law converges exponentially in \(1\)-Wasserstein distance to the unique probability law
\[
\nu=\mathcal L\left(\rho\sum_{j=0}^{\infty}(1-\rho)^j A_j\right),
\qquad \Pr(A_j=a_0)=\Pr(A_j=b_0)=\tfrac12,
\]
where the \(A_j\) are independent. This law has
\[
\mathbb E_{\nu}[C]=\frac{a_0+b_0}{2},\qquad
\operatorname{Var}_{\nu}(C)=\frac{\rho d^2}{4(2-\rho)}.
\]
The pathwise Cesàro mean of the center converges to \((a_0+b_0)/2\) almost surely, despite the failure of pointwise convergence. At \(\rho=1/2\), the limiting law is **exactly uniform on \([a_0,b_0]\)**.

**Open-leaf regime:** if \(\epsilon>d/2\), every selected edge updates both endpoints forever. All three opinions converge almost surely to the conserved mean
\[
\bar x=\frac{a_0+c_0+b_0}{3}.
\]
Writing \(V_t=\sum_{v\in\{a,c,b\}}(v_t-\bar x)^2\), the quantitative bound is
\[
\mathbb E[V_t]\le[1-\rho(1-\rho)]^t V_0.
\]
Equality at the confidence boundary belongs to the **closed** regime because the model's receptiveness comparison is strict.

The stationary affine-recursion calculations in the closed regime and conventional symmetric gossip convergence in the open regime have known analogues. The finding is their **exact confidence-induced transition in this specific endogenous, directionally gated neighborhood model**, rather than a claim to have discovered Bernoulli convolutions or stubborn-agent opinion fluctuations in general.

## Assumptions and scope

The graph is the fixed undirected path \(L-C-R\) with endpoint opinions \(a_t,b_t\) and center opinion \(c_t\). No edges are rewired and each discrete step samples one of the two edges with probability \(1/2\), independently of earlier samples. The opinions initially lie in the interval and satisfy \(0\le a_0\le c_0\le b_0\le1\) and \(a_0<b_0\); the positive parameters obey \(\rho\in(0,1/2]\), \(\epsilon\in(0,1]\), and neighborhood mixing \(\sigma=0\).

For adjacent nodes \(i,j\), write \(N(j)\) for the fixed graph neighbors of \(j\), and define the **directed neighborhood confidence distance**
\[
d(i,j)=\left|x_i-\frac1{|N(j)|}\sum_{k\in N(j)}x_k\right|.
\]
When edge \(\{i,j\}\) is selected, each endpoint updates against the other's **pre-update** value independently according to
\[
x_i'=x_i+\rho(x_j-x_i)\mathbf 1_{\{d(i,j)<\epsilon\}},\qquad
x_j'=x_j+\rho(x_i-x_j)\mathbf 1_{\{d(j,i)<\epsilon\}}.
\]
This is Eq. (3), with \(\sigma=0\) and one selected edge, of the corrected public manuscript [1]. The quantifiers concern every deterministic ordered initial triple and every allowed positive parameter, with probabilistic statements over the independent edge draws. At each update, unselected nodes remain unchanged.

## Proof

**1. Directed confidence distances collapse.** The two leaves have the sole neighbor \(C\), whereas \(C\) has exactly the neighbors \(L,R\). Hence, at every time,
\[
d(C,L)=d(C,R)=0,
\qquad d(L,C)=d(R,C)=\frac{|b_t-a_t|}{2}.
\]
Since \(\epsilon>0\), the center always updates when incident to the selected edge. The two leaves are simultaneously receptive precisely when \(|b_t-a_t|<2\epsilon\). This common gate depends on the leaf gap only, not on the center opinion.

**2. Closed-leaf branch is permanent.** If initially \(d\ge2\epsilon\), neither leaf updates on any selected edge. Their gap stays exactly \(d\) by induction. Let \(A_t\) be the initial opinion of the selected leaf. The sequence \((A_t)_{t\ge0}\) is independent and has equal probabilities on \(a_0,b_0\). The center therefore obeys
\[
c_{t+1}=(1-\rho)c_t+\rho A_t.
\]
Set \(q=1-\rho\in[1/2,1)\). Iterating gives \(c_t=q^tc_0+\rho\sum_{j=0}^{t-1}q^{t-1-j}A_j\). Reversing the order of the independent inputs shows this has the distribution of \(q^tc_0+\rho\sum_{j=0}^{t-1}q^jA_j\). By absolute summability the latter converges almost surely under a coupling to \(Y=\rho\sum_{j\ge0}q^jA_j\). Two copies driven by the same inputs contract exactly by \(q^t\), proving both uniqueness of its invariant law and
\[
W_1(\mathcal L(c_t),\nu)\le q^t d.
\]
Independence gives \(\mathbb E A=(a_0+b_0)/2\), \(\operatorname{Var}(A)=d^2/4\), and
\[
\mathbb E Y=\rho\frac{\mathbb EA}{1-q}=\mathbb EA,
\qquad \operatorname{Var}(Y)=\frac{\rho^2\operatorname{Var}(A)}{1-q^2}=\frac{\rho d^2}{4(2-\rho)}.
\]
If \(c_t\) converged, then \(A_t=[c_{t+1}-qc_t]/\rho\) would converge. Independent fair draws hit each distinct endpoint infinitely often almost surely, so \(A_t\) does not converge. This proves nonconvergence of \(c_t\). Summing the recurrence gives
\[
\frac1T\sum_{t=0}^{T-1}c_t
=\frac1T\sum_{t=0}^{T-1}A_t-\frac{c_T-c_0}{\rho T}
\longrightarrow\frac{a_0+b_0}{2}
\]
almost surely, using the strong law and boundedness of the opinions. At \(\rho=1/2\), \(Y=a_0+d\sum_{j\ge0}2^{-j-1}B_j\), with fair independent bits \(B_j\). Its binary-expansion law is uniform on \([a_0,b_0]\) (the possible double expansions have probability zero).

**3. Open-leaf branch stays open.** Suppose \(d<2\epsilon\). If \(a_t\le c_t\le b_t\) and the left edge is selected, both nodes move symmetrically:
\[
(a_{t+1},c_{t+1})=((1-\rho)a_t+\rho c_t,\ \rho a_t+(1-\rho)c_t).
\]
Because \(\rho\le1/2\), these two new values remain ordered within \([a_t,c_t]\); the right edge analogously preserves \(c\le b\). Every update consequently preserves the order \(a_t\le c_t\le b_t\) and makes \(a_t\) nondecreasing and \(b_t\) nonincreasing. In particular \(b_t-a_t\le d<2\epsilon\) always, so the two directed leaf gates remain open and all subsequent selected edges execute symmetric compromise.

The sum \(a_t+c_t+b_t\) is invariant. A symmetric compromise on edge \(\{i,j\}\) reduces the squared deviation from the conserved mean by exactly \(2\rho(1-\rho)(x_i-x_j)^2\). Therefore, conditional on the current state,
\[
\mathbb E[V_{t+1}\mid\mathcal F_t]
=V_t-\rho(1-\rho)\bigl[(a_t-c_t)^2+(c_t-b_t)^2\bigr].
\]
The elementary exact identity
\[
(a_t-c_t)^2+(c_t-b_t)^2-V_t
=\frac{(a_t+b_t-2c_t)^2}{3}\ge0
\]
yields \(\mathbb E[V_{t+1}]\le(1-\rho(1-\rho))\mathbb E[V_t]\), and iteration gives the announced bound. Since \(V_t\ge0\), Markov's inequality and the first Borel–Cantelli lemma show \(V_t\to0\) almost surely. All components must therefore converge to the same conserved mean.

**4. Sharpness.** The leaf gate has the strict comparison \(d/2<\epsilon\), not a non-strict comparison. Equality exactly reproduces the frozen branch, while every positive excess opens both leaves and yields consensus. Both phases occur for the same ordered initial data by changing only \(\epsilon\); thus the boundary cannot be shifted.

## Verification

The self-contained Python 3 file `verify.py` uses only the standard library and exact rational arithmetic. Run `python3 verify.py` after extracting this package. It independently computes directed neighbor-mean distances before simultaneous endpoint updates, enumerates 36,828 edge-word trajectories of lengths zero through nine across multiple confidence and compromise parameters, checks 224 exact one-edge energy identities, checks 27 exact finite-time affine-recursion moment identities, and checks the uniform dyadic meshes for ten depths. All assertions passed. Finite enumeration does **not** establish infinite-time statements; those follow from the proofs above.

## Relationship to prior work

Krishnagopal and Porter [1] introduced the directed neighborhood confidence rule, including the pure-transitive \(\sigma=0\) endpoint, and investigated simulation behavior. Their displayed update Eq. (3) fixes the precise orientation and threshold used here; the inspected main text, figures, and conclusions do not give the sharp three-node path classification.

Acemoğlu, Como, Fagnani, and Ozdaglar [2], especially Section 2.1, already analyze a single ordinary opinion agent interacting with two **exogenously stubborn** agents. That prior theorem covers the classical persistent-fluctuation mechanism, the affine recursion, and the uniform binary-expansion example **after the leaves are known to be frozen**. The new step here is an endogenous, necessary-and-sufficient confidence gate in the distinct NDW model, together with the adjoining all-responsive consensus branch. We do not claim the classical stationary calculations separately as novel.

Zhang, Yuan, Wang, Altafini, and Shi [3] prove nonconvergent fluctuations for different bounded-confidence dynamics in which randomized neighborhood **clique means** determine updates. Their update rules and hypotheses are different; they do not supply this path-specific cutoff by implication. The more general theory of iterated random affine functions, of course, accounts for the invariant-law construction once the reduction is made.

## Limitations

The analysis concerns a fixed undirected three-vertex path, one independent uniform edge choice per time step, pure neighborhood tuning, a homogeneous strict threshold, \(0<\rho\le1/2\), and initially ordered opinions with center between distinct leaves. It does not classify larger graphs, mixed dyadic–transitive confidence, rewiring, nonuniform or dependent edge selection, or unordered initial triples. The a.s. consensus conclusion is asymptotic, not finite-time exact equality. The nonconvergent branch is in fact a familiar stubborn-agent process in disguise; the claimed contribution is the complete NDW threshold across both branches, and broader bibliographic equivalences remain possible.

## References

[1] S. Krishnagopal and M. A. Porter, “Bounded-Confidence Models of Opinion Dynamics with Neighborhood Effects,” arXiv:2402.05368, first posted 8 February 2024, revised 22 May 2025. Model equations and discussion: https://arxiv.org/html/2402.05368v2 ; version history: https://arxiv.org/abs/2402.05368 .

[2] D. Acemoğlu, G. Como, F. Fagnani, and A. Ozdaglar, “Opinion fluctuations and disagreement in social networks,” Mathematics of Operations Research 38 (2013), 1–27. Open full text: https://arxiv.org/abs/1009.2653 .

[3] J. Zhang, D. Yuan, L. Wang, C. Altafini, and G. Shi, “Dynamics of Opinions with Bounded Confidence in Social Cliques: Emergence of Fluctuations,” arXiv:2107.04948, 11 July 2021. Full text: https://arxiv.org/abs/2107.04948 .

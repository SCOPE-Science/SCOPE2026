# Rank-controlled synchronization and bounded population sums in a Fibonacci Hopfield map

## Finding
For the piecewise-affine Hopfield family of Pires, the Hausdorff dimension of the full one-step output set equals the algebraic rank of the positive coupling matrix. One-step collapse to the Perron ray occurs precisely for rank-one coupling. At that rank, every initial condition shares aperiodic Cantor limit dynamics, and the total activation is an **exact bounded coboundary** with uniformly bounded centered orbit sums.

## Assumptions and scope
Let \(n\ge2\), \(X=[0,1]^n\), and let \(W=(w_{ij})\) be strictly positive with \(3/4<\sum_j w_{ij}<1\). By Perron–Frobenius, take \(Wv=\rho v\), \(v_i>0\), \(\sum_i v_i=1\), so \(3/4<\rho<1\). Define the Fibonacci binary word \(\omega_k=2+\lfloor(k+1)\varphi\rfloor-\lfloor(k+2)\varphi\rfloor\), \(\varphi=(1+\sqrt5)/2\), and \(\delta=1/2+(1/4)\sum_{k\ge0}\omega_k2^{-k}\). Set \(d=2(1-\delta)\) and
\[
\widetilde g(t)=\begin{cases}t/2+\delta,&0\le t<d,\\t/2+\delta-1,&d\le t\le1,\\\delta-1/2,&t\ge1.\end{cases}
\]
The network is \(F_i(x)=v_i\widetilde g((Wx)_i/(\rho v_i))\). All inputs belong to \(X\); dimensions mean Hausdorff dimension of the set itself (not the dimension of an invariant measure). Write \(g=\widetilde g|_{[0,1]}\), \(L=\{tv:0\le t\le1\}\), and \(\alpha=(3-\sqrt5)/2\).

## Proof
**One-step image rank.** Each scalar activation has at most three affine pieces, of slope \(0\) or \(1/(2\rho)\) as a function of \((Wx)_i\). The cube has a finite polyhedral partition on each of whose cells \(F\) has affine derivative \(D W/(2\rho)\) for a diagonal \(0/1\)-matrix \(D\). Its image has Hausdorff dimension at most \(\operatorname{rank}W\). Conversely, in a sufficiently small relatively open cube with positive coordinates near zero, every preactivation lies strictly below \(d\rho v_i\). There \(F(x)=\delta v+Wx/(2\rho)\), whose image has Hausdorff dimension exactly \(\operatorname{rank}W\). Thus \(\dim_{H}F(X)=\operatorname{rank}W\).

**Rank-one criterion.** If \(F(X)\subset L\), then for each coordinate direction \(e_j\), the difference \(F(\varepsilon e_j)-F(0)=\varepsilon We_j/(2\rho)\) lies in \(\operatorname{span}(v)\) for small \(\varepsilon>0\). Every column of \(W\) therefore lies in that one-dimensional subspace and \(\operatorname{rank}W=1\). Conversely, if the positive \(W\) has rank one, write \(W=\rho v q^\top/(q^\top v)\) with \(q>0\). For \(x\in X\), \(F(x)=v\widetilde g(q^\top x/(q^\top v))\in L\). On \(L\), \(F(tv)=v g(t)\). A nonempty concrete family is \(W=(\rho/n)\mathbf 1\mathbf 1^\top\), \(3/4<\rho<1\), \(v=\mathbf 1/n\).

**Aperiodicity and common limit set.** Gaivão–Pires, Lemma 6, proves that \(g\) admits a continuous nondecreasing surjective \(h:[0,1]\to[0,1]\) with \(h\circ g=T\circ h\), where \(T(u)=u+\alpha-\mathbf 1_{\{u\ge1-\alpha\}}\), that \(h^{-1}(1-\alpha)=\{d\}\), and that all scalar trajectories have one common Cantor omega-limit set \(C\). Irrationality of \(\alpha\) rules out scalar periodic points: if \(g^p(t)=t\), then \(T^p(h(t))=h(t)\), impossible. Since every vector trajectory enters \(L\) after one step, \(\omega_F(x)=vC\) for every \(x\), and \(F\) has no periodic points.

**Cohomological identity.** By monotonicity and uniqueness of \(h^{-1}(1-\alpha)\), the branch indicators coincide: \(I(t)=\mathbf1_{\{t\ge d\}}=\mathbf1_{\{h(t)\ge1-\alpha\}}\). Hence
\[
g(t)=t/2+\delta-I(t),\qquad h(g(t))=h(t)+\alpha-I(t).
\]
Subtracting the two identities gives the **pointwise** equality
\[
t-2(\delta-\alpha)=H(t)-H(g(t)),\qquad H(t)=2(t-h(t)).
\]
Take \(s_k=\sum_i(F^k(x))_i\) for \(k\ge1\). Rank-one collapse gives \(s_k\in[0,1]\) and \(s_{k+1}=g(s_k)\). Telescoping proves
\[
\sum_{k=1}^N\big(s_k-2(\delta-\alpha)\big)=H(s_1)-H(s_{N+1}).
\]
The improved uniform constant \(2\) (rather than \(4\) from separate sup-norm bounds) follows because \(h\) is nondecreasing and maps \([0,1]\) onto itself: for any \(a<b\), \((b-h(b))-(a-h(a))\le b-a\le1\), and the reverse difference is at most \(h(b)-h(a)\le1\). Thus \(\operatorname{osc}H\le2\). The bound is uniform in \(N\), \(x\), \(n\), and eligible rank-one \(W\).

**Unique invariant probability.** Every invariant probability is supported on \(L\), since \(F(X)\subset L\). Under \(h\), its scalar projection must be invariant under irrational rotation \(T\), hence Lebesgue measure. A continuous monotone map has at most countably many fibers containing two distinct points (their open interiors are disjoint). Thus the Lebesgue almost-everywhere inverse of \(h\) uniquely determines the scalar invariant probability, and the inverse is equivariant almost everywhere by \(h\circ g=T\circ h\). This also constructs an invariant probability; it is supported on \(C\). Integrating the coboundary yields its total-population mean \(2(\delta-\alpha)\) and its \(i\)-th coordinate mean \(2v_i(\delta-\alpha)\).

## Verification
The accompanying standard-library checker uses exact rational enclosures for \(\delta\), integer-square-root certification of the Fibonacci digits, and verified branch choices for five rational starts over 55 iterations. It passes 275 certified branch steps and corresponding finite Sturmian-count comparisons. These checks supplement, but do not replace, the infinite semiconjugacy theorem and the full symbolic proof above. The rank and cohomology identities can also be reproduced directly by substitutions shown in the proof.

## Relationship to prior work
Pires's 2022 construction establishes an invariant Perron ray and chaotic Cantor dynamics there for *arbitrary* eligible positive matrices. It does **not** characterize global one-step collapse by rank or establish the all-initial-data quantitative population-sum law. Gaivão and Pires's earlier 2022 interval result supplies the semiconjugacy and common scalar Cantor limit used as input here; the rotation step-frequency and bounded-remainder phenomenon are classical. The present conclusion is the exact coupling-rank classification together with the network-level finite-time coboundary and uniform discrepancy, not a new claim about the existence of the scalar Cantor set.

## Limitations
The bounded-sum and common-limit assertions require exactly rank-one coupling; the image-dimension identity alone holds for every eligible positive \(W\). No stability under rank-two perturbations, a sharp optimal discrepancy constant, or claims about finite-precision numerical iterations are made. This is an analytical specialization of known scalar semiconjugacy theory, not an independent rediscovery of it. Independent mathematical audit has not been performed.

## References
1. Benito Pires, *A chaotic discrete-time continuous-state Hopfield network with piecewise-affine activation functions*, arXiv:2210.00414 (first public 2022-10-02); Discrete and Continuous Dynamical Systems B 28 (2023), 4683–4691, DOI 10.3934/dcdsb.2023035. Theorem 2.3 and proof, especially its invariant-ray equations.
2. José Pedro Gaivão and Benito Pires, *Chaotic time series in financial processes consisting of savings with piecewise constant monthly contributions*, arXiv:2206.11933 (first public 2022-06-23), Lemma 6 and its rotation semiconjugacy.

# Orientation splitting and signed Gaussian decoupling for local meandric loops

## Finding
Let \(n\ge4\), and choose independently and uniformly two noncrossing perfect matchings of \(\{1,\ldots,2n\}\), drawn respectively above and below a line. Write \(X_n\) for the number of common consecutive edges, and \(Y_{+,n}\), respectively \(Y_{-,n}\), for the number of four-consecutive-vertex meandric components in which the upper matching has two parallel nearest-neighbor edges and the lower matching has the nested pair, respectively the reverse orientation. Put \(Y_n=Y_{+,n}+Y_{-,n}\) and \(D_n=Y_{+,n}-Y_{-,n}\).

**Exact fair orientation and signed decoupling.** Conditionally on \((X_n,Y_n)\), \(Y_{+,n}\) is exactly \(\operatorname{Bin}(Y_n,1/2)\). In fact, this holds conditionally on all orientation-blind component information. In conjunction with the established univariate central limit theorem for \(X_n\), this yields the joint limit
\[
\left(\frac{X_n-n/8}{\sqrt n},\frac{D_n}{\sqrt n}\right)
\Longrightarrow (G,H),\qquad
G\sim N(0,13/128),\quad H\sim N(0,1/64),\quad G\perp H.
\]
Despite this asymptotic independence, both distinct orientation counts have strictly negative covariance with \(X_n\) at every finite \(n\ge4\), and \(Y_{+,n}\) and \(Y_{-,n}\) likewise have strictly negative covariance.

Writing \(C_k=\binom{2k}{k}/(k+1)\) and \(q_r=C_{n-r}/C_n\), their exact joint factorial moments are
\[
\begin{aligned}
\mathbb E X_n&=(2n-1)q_1^2,&
\mathbb E Y_{+,n}=\mathbb E Y_{-,n}&=(2n-3)q_2^2,\\
\mathbb E(X_n)_2&=(2n-2)(2n-3)q_2^2,&
\mathbb E[X_nY_{\pm,n}]&=((2n-6)(2n-3)+2)q_3^2,\\
\mathbb E[(Y_{\pm,n})_2]&=(2n-6)(2n-7)q_4^2,&
\mathbb E[Y_{+,n}Y_{-,n}]&=(2n-6)(2n-7)q_4^2.
\end{aligned}
\]
The limiting covariance matrix, with coordinates in the order \((X_n,Y_{+,n},Y_{-,n})\) and centered/scaled by \(\sqrt n\), is
\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}(X_n,Y_{+,n},Y_{-,n})=
\begin{pmatrix}
13/128&-5/2048&-5/2048\\
-5/2048&249/32768&-7/32768\\
-5/2048&-7/32768&249/32768
\end{pmatrix}.
\]
The covariance limit is **not** a claim that the full three-dimensional centered vector has a Gaussian limit.

## Assumptions and scope
The two matchings are independent, uniform and noncrossing; there are \(C_n^2\) equally likely pairs. For an interval \((i,i+1)\), an \(X_n\) occurrence means both matchings include that edge. For four consecutive vertices \((i,i+1,i+2,i+3)\), a positive occurrence means that the upper matching includes \((i,i+1),(i+2,i+3)\) while the lower includes \((i,i+3),(i+1,i+2)\). A negative occurrence interchanges upper and lower. Each such local configuration is a full four-vertex component. The definitions include all admissible positions, not just even starts. Write \((Z)_2=Z(Z-1)\).

## Proof
**Catalan deletion.** If a given collection of \(r\) vertex-disjoint consecutive two-vertex blocks is required to be paired internally in a noncrossing matching, contracting/deleting these forced local arcs leaves an arbitrary noncrossing matching on \(2(n-r)\) vertices; the probability is \(q_r\). Similarly, imposing disjoint prescribed four-vertex local patterns forces \(2r\) arcs and leaves \(C_{n-2r}\) possibilities. Deletion is a bijection because the forced local arcs can be reinserted without crossing external arcs. Independence of the upper and lower matchings squares the relevant Catalan ratio.

**Counting placements.** There are \(2n-1\) short-edge placements and \(2n-3\) four-vertex placements of each orientation. For two distinct short-edge events to be jointly possible, their two-vertex intervals must be disjoint: the number of ordered pairs is \((2n-2)(2n-3)\). A short-edge interval and a four-vertex interval must likewise be disjoint: the number of ordered placements is \((2n-6)(2n-3)+2\), obtained by summing the available positions to the left and right of every four-vertex interval. Two four-vertex component intervals must be disjoint: their ordered count is \((2n-6)(2n-7)\). A component of one orientation cannot occupy the same four vertices as a component of the other orientation. The displayed factorial-moment identities follow by linearity.

**Strict covariance signs.** Subtracting the products of the exact means yields
\[
\operatorname{Cov}(X_n,Y_{\pm,n})=
-\frac{n^2(n+1)^2(10n^3-41n^2+32n+11)}{64(2n-5)(2n-3)^2(2n-1)^3}.
\]
The numerator's cubic is positive at \(n=3\), and its forward difference \(30n^2-52n+1\) is positive for every integer \(n\ge3\). Similarly,
\[
\operatorname{Cov}(Y_{+,n},Y_{-,n})=-
\frac{n^2(n+1)^2 P(n)}{256(2n-7)(2n-5)^2(2n-3)^2(2n-1)^4},
\]
where
\[
P(4+u)=28u^6+412u^5+2331u^4+6266u^3+7919u^2+3816u+72>0\quad(u\ge0).
\]
The stated strict signs hold for every \(n\ge4\). Taylor expansion of the rational Catalan ratios in the exact moments gives all entries of the displayed limiting covariance matrix. In particular, \(\mathbb E Y_n/n\to1/64\) and \(\operatorname{Var}(Y_n)/n\to121/8192\), so \(Y_n/n\to1/64\) in \(L^2\).

**Fair orientation and the bivariate limit.** At any chosen four-vertex component, swap its local upper and lower pairings. Both local pairings are noncrossing, all four vertices are matched internally, and no outside arc is changed. Swapping at distinct components commutes, preserves the uniform measure, and does not alter short loops or the orientation-blind remainder of either matching. The orbit of a configuration under these independent involutions has exactly \(2^{Y_n}\) elements. Thus, conditionally on the orbit and hence on \((X_n,Y_n)\), the signs are independent fair Bernoulli marks. Consequently \(\mathbb E[\exp(isD_n/\sqrt n)\mid\text{orientation-blind data}]=\cos(s/\sqrt n)^{Y_n}\), which converges in probability and in \(L^1\) to \(\exp(-s^2/128)\). Janson and Thévenin's short-loop central limit theorem states \((X_n-n/8)/\sqrt n\Longrightarrow N(0,13/128)\). For all fixed real \(s,t\), multiply the conditional characteristic function by \(\exp(it(X_n-n/8)/\sqrt n)\), take expectations, and use bounded convergence in probability to factor the limiting characteristic function. Lévy's theorem gives the asserted **independent** bivariate Gaussian limit.

## Verification
The accompanying independent enumeration checker `check_meanders.py` enumerates all \(C_n^2\) pairs of matchings for \(2\le n\le7\), totaling \(203454\) configurations. It checks Catalan moments, sign covariances, and exact conditional binomial counts using rational arithmetic. These finite computations do not prove the statements for arbitrary \(n\); the Catalan bijection, algebraic sign argument, and characteristic-function proof do.

## Relationship to prior work
Janson and Thévenin (2023) established the asymptotic normality, mean and variance of the two-vertex component count \(X_n\), and studied marginal counts of fixed component shapes. Their paper identifies a joint central limit theorem for different shapes as a separate unverified question. The present theorem uses the known marginal short-loop CLT but proves exact conditional splitting of the two oriented four-vertex local component counts, the cross-covariance matrix, and an independent **signed** bivariate Gaussian limit. It does not assert or require a general joint CLT for all component counts. Féray and Thévenin (2023) investigate component frequencies and the infinite noodle from a different limiting perspective; Borga, Gwynne, and Park (2023) examine geometric and macroscopic behavior.

## Limitations
The independent signed limit concerns the difference of the two orientations, rather than the separate Gaussian fluctuations of their sum. No full multivariate central limit theorem for arbitrary meandric component shapes follows. The exact finite-covariance signs and the covariance matrix apply only to the specified local component patterns and to two independent uniform noncrossing perfect matchings. Historical priority beyond inspected primary sources is not independently certified.

## References
1. Svante Janson and Paul Thévenin, *Central limit theorem for components in meandric systems through high moments*, arXiv:2303.01900 (first public version March 3, 2023), particularly Sections 3–5 and discussion of multivariate extensions; https://arxiv.org/abs/2303.01900 .
2. Valentin Féray and Paul Thévenin, *Components in meandric systems and the infinite noodle*, arXiv:2201.11572 (first public version January 27, 2022); https://arxiv.org/abs/2201.11572 .
3. Jacopo Borga, Ewain Gwynne, and Minjae Park, *On the geometry of uniform meandric systems*, arXiv:2212.00534 (first public version December 1, 2022); https://arxiv.org/abs/2212.00534 .

# Multiscale threshold correlations and Bernoulli-factor rigidity for Chebyshev maps

## Finding

Fix an integer \(q\ge2\), let \(T_q:[-1,1]\to[-1,1]\) be the first-kind Chebyshev map \(T_q(x)=\cos(q\arccos x)\), and let \(X\) have probability density \(1/(\pi\sqrt{1-x^2})\). For \(0<p<1\), write \(c_p=\cos(\pi p)\) and observe the stationary binary process
\[
B_k=\mathbf{1}_{\{T_q^{\circ k}(X)>c_p\}},\qquad k\ge0.
\]
Its marginal success probability is \(p\). For each lag \(n\ge1\), set \(Q=q^n\), \(j=\lfloor Qp\rfloor\), and \(\theta=Qp-j\in[0,1)\). Then
\[
\operatorname{Cov}(B_0,B_n)=\begin{cases}
0,&\theta=0,\\
\displaystyle \frac1Q\min\{(1-p)\theta,\ p(1-\theta)\},&0<\theta<1,\ j\text{ even},\\
\displaystyle-\frac1Q\min\{p\theta,\ (1-p)(1-\theta)\},&0<\theta<1,\ j\text{ odd}.
\end{cases}
\]
In particular,
\[
|\operatorname{Cov}(B_0,B_n)|\le p(1-p)q^{-n},
\qquad
\operatorname{Cov}(B_0,B_n)=0\iff q^np\in\mathbb Z.
\]
The following *single-lag rigidity* equivalence holds:
\[
\operatorname{Cov}(B_0,B_1)=0
\quad\Longleftrightarrow\quad
p\in\left\{\frac1q,\ldots,\frac{q-1}{q}\right\}
\quad\Longleftrightarrow\quad
(B_k)_{k\ge0}\text{ is i.i.d. Bernoulli}(p).
\]
For \(q\ge3\), these are precisely \(q-1\) nontrivial independently distributed binary threshold factors, none generating for the original map: their symbolic entropy \(H(p)=-p\log p-(1-p)\log(1-p)\) is less than the full map entropy \(\log q\). Zero covariance at a *higher* lag alone does not force independence: for \(q=2\), \(p=1/4\), the lag-two covariance is zero but the lag-one covariance is \(1/16\).

## Assumptions and scope

The invariant initial law is essential: \(X\) has the arcsine law on the closed interval \([-1,1]\), and \(q\ge2\) is any *integer*. Thresholds satisfy \(0<p<1\); endpoint thresholds yield constant observations and are intentionally excluded. All orbit-time indices are nonnegative integers and every covariance formula is valid at every positive integer lag. Branch and threshold endpoints are null sets under the invariant law, so the choice of strict versus weak inequality is immaterial. The Bernoulli statement means that all finite binary word probabilities factor, not merely that covariances vanish. The finding concerns statistical symbolic factors, not a topological conjugacy between the entire map and a binary shift.

## Proof

**1. Uniform-coordinate conjugacy and full branches.** Let \(U=\pi^{-1}\arccos X\), which is uniform on \([0,1]\). The polynomial identity \(T_q(\cos(\pi u))=\cos(q\pi u)\) conjugates the Chebyshev map almost everywhere to the \(q\)-branch zigzag map
\[
g_q(u)=\pi^{-1}\arccos(\cos(q\pi u)).
\]
On the branch \(I_r=[r/q,(r+1)/q]\), it is affine with slope \(q\) if \(r\) is even and slope \(-q\) if \(r\) is odd, mapping every branch *onto* \([0,1]\). Lebesgue measure is invariant: for integrable \(f\), the transfer operator satisfies \(\mathcal Lf(v)=q^{-1}\sum_{r=0}^{q-1}f(h_r(v))\), where each \(h_r\) is the inverse branch. By Chebyshev composition, \(g_q^{\circ n}=g_{q^n}\) for all integer \(n\ge1\). Finally \(B_k=\mathbf1_{\{g_q^{\circ k}(U)<p\}}\), so \(\mathbb EB_k=p\).

**2. Exact two-time overlap.** Fix \(n\ge1\), put \(Q=q^n\), and partition \([0,1]\) into its \(Q\) equal monotone branches for \(g_Q\). Let \(j=\lfloor Qp\rfloor\) and \(\delta=p-j/Q=\theta/Q\). Every one of the first \(j\) *complete* branches is contained in \([0,p]\) and contributes exactly \(p/Q\) to the length of \([0,p]\cap g_Q^{-1}[0,p]\). The only possible further contribution comes from the incomplete \(j\)-th branch of length \(\delta\).

If \(j\) is even, this additional overlap is \(\min\{\delta,p/Q\}\), because this branch starts at image zero. If \(j\) is odd, it is \(\max\{0,\delta-(1-p)/Q\}\), because this branch starts at image one. Thus
\[
\mathbb E(B_0B_n)=\frac{jp}{Q}+
\begin{cases}
\min\{\delta,p/Q\},&j\text{ even},\\
\max\{0,\delta-(1-p)/Q\},&j\text{ odd}.
\end{cases}
\]
Subtract \(p^2\), use \(j/Q=p-\delta\), and simplify: for even \(j\), the result is \(Q^{-1}\min\{(1-p)\theta,p(1-\theta)\}\); for odd \(j\), it is \(-Q^{-1}\min\{p\theta,(1-p)(1-\theta)\}\). If \(\theta=0\), the overlap is exactly \(p^2\). For \(0<\theta<1\), all factors in the displayed minima are strictly positive, proving the exact vanishing criterion and the alternating sign. The elementary inequality
\[
\min\{(1-p)\theta,p(1-\theta)\}\le p(1-p)
\]
(and its odd-branch counterpart, maximizing at \(\theta=1-p\)) proves the exponential bound.

**3. One-lag zero implies complete independence.** At lag one, the proved vanishing criterion says precisely \(p=j/q\) for an integer \(1\le j<q\). Let \(A=[0,p)\), a union (up to endpoints) of \(j\) *complete* inverse branches of \(g_q\). The transfer operator satisfies
\[
\mathcal L\mathbf1_A=p\mathbf1_{[0,1]},\qquad
\mathcal L\mathbf1_{A^c}=(1-p)\mathbf1_{[0,1]}.
\]
For any finite binary word \(b_0,\dots,b_{m-1}\in\{0,1\}\), the integral of its cylinder indicator is
\[
\int_0^1\prod_{k=0}^{m-1}\mathbf1_{A_{b_k}}(g_q^{\circ k}(u))\,du,
\quad A_1=A,\ A_0=A^c.
\]
Transfer the first factor to the next time. The displayed transfer identities replace it by the scalar \(p\) when \(b_0=1\), or \(1-p\) when \(b_0=0\). Repeating yields
\[
\mathbb P(B_0=b_0,\ldots,B_{m-1}=b_{m-1})
=\prod_{k=0}^{m-1}p^{b_k}(1-p)^{1-b_k}.
\]
This proves i.i.d. Bernoulli. Conversely, independence forces lag-one covariance zero and therefore the same grid threshold.

**4. Non-generating factors.** The \(q\)-full-branch partition has uniform \(q^m\) length-\(m\) cylinders, each of measure \(q^{-m}\), and generates modulo endpoint exceptions. Its entropy is \(\log q\). The i.i.d. binary observation has entropy \(H(p)\le\log2<\log q\) for \(q\ge3\), hence cannot be a generating partition. All \(q-1\) grid thresholds yield different \(p\), and these are the only nonconstant threshold observations with the stated independence property.

## Verification

The standalone exact-rational checker `verify.py` reconstructs overlap intervals from each branch, independently evaluates the closed formula for degrees \(2\le q\le8\), lags \(1\le n\le3\), and several rational thresholds, including grid boundaries. It also enumerates *all* binary words of lengths two through four at every nontrivial grid threshold of these degrees, confirming the Bernoulli factorization exactly, and checks the higher-lag-zero counterexample. The checker returned `VERIFY_OK`. Finite computations only corroborate the universally quantified argument above.

## Relationship to prior work

Bollt, Stanford, Lai, and Życzkowski (2000, 2001) show that a misplaced binary threshold can distort symbolic dynamics and entropy in the classical one-hump tent map. Pfante, Olbrich, Bertschinger, Ay, and Jost (2013 preprint/2014 journal article) analyze information-theoretic closure and Markov partitions for that tent map and its iterates. A 2015 study of causation entropy explicitly examines threshold symbolizations of the degree-two tent map. Yan and Beck (2020) treat smooth Chebyshev-orbit correlation functions and generalizations. These precedents supply the motivation, full-branch conjugacy, or special cases; this finding gives an explicit covariance for *every* binary threshold and *every* lag at *every* integer degree, together with the rigidity equivalence between a single zero covariance and fully independent symbolic factors. No uniqueness beyond the fixed one-threshold family is asserted. The 2013 preprint of Pfante and colleagues was located but its complete text could not be obtained for direct statement-by-statement comparison; this is a residual bibliographic risk, not evidence of noncoverage.

## Limitations

The result does not extend as stated to arbitrary invariant initial distributions, asymmetric or non-full-branch maps, higher-alphabet partitions, or thresholds defined by observables other than the Chebyshev coordinate. It does not claim statistical independence for non-grid thresholds or deduce high-order independence merely from higher-lag covariance zero. The theorem does not assert bibliographic priority without further independent literature examination, particularly of detailed coarse-graining results for tent-map iterates.

## References

1. E. M. Bollt, T. Stanford, Y.-C. Lai, K. Życzkowski, *Validity of Threshold-Crossing Analysis of Symbolic Dynamics from Chaotic Time Series*, Physical Review Letters **85** (2000), 3524; DOI: 10.1103/PhysRevLett.85.3524 (public date 2000-10-16).
2. E. M. Bollt, T. Stanford, Y.-C. Lai, K. Życzkowski, *What symbolic dynamics do we get with a misplaced partition?*, Physica D **154** (2001), 259–286; DOI: 10.1016/S0167-2789(01)00242-1.
3. O. Pfante, E. Olbrich, N. Bertschinger, N. Ay, J. Jost, *Closure Measures and the Tent Map*, Max Planck Institute MiS preprint 108/2013 (public 2013-11-25), and *Chaos* **24** (2014), 013136; DOI: 10.1063/1.4869075.
4. *Causation Entropy from Symbolic Representations of Dynamical Systems*, arXiv:1507.07262v1 (2015), section IV.
5. J. Yan, C. Beck, *Distinguished correlation properties of Chebyshev dynamical systems and their generalisations*, arXiv:2006.06786 (2020), sections 2 and 4.

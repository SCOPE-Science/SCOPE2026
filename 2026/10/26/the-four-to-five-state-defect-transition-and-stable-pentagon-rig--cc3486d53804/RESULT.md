# Quantitative pentagon rigidity for the planar quadratic defect

## Finding

Let \(\xi\) have exactly five distinct atoms \(x_j\in\mathbb R^2\), with positive masses \(w_j\), and suppose
\[
\mathbb E\xi=0,\qquad \mathbb E\xi\xi^{\mathsf T}=I_2,\qquad \mathbb E\xi^{\otimes3}=0.
\]
Set
\[
\Lambda=\sup_{A=A^{\mathsf T},\ \operatorname{tr}A=0,\ \|A\|_F=1}\frac14\mathbb E(\xi^{\mathsf T}A\xi)^2.
\]
If \(0\le\Lambda-1/4\le\varepsilon\le10^{-8}\), there are a rotation angle \(\theta\) and a relabeling \(j=0,\dots,4\) for which, writing \(u(\phi)=(\cos\phi,\sin\phi)\),
\[
\left|w_j-\frac15\right|\le6\sqrt\varepsilon,
\qquad
\bigl\|x_j-\sqrt2\,u(\theta+2\pi j/5)\bigr\|_2\le440\sqrt\varepsilon
\]
for every \(j\). In particular, no lower bound on the five masses or any separation of atoms is assumed; the near-minimal defect supplies them.

## Assumptions and scope

Here the Frobenius norm is the Euclidean matrix norm \(\|A\|_F^2=\sum_{i,j}A_{ij}^2\). The defect involves only the trace-free symmetric quadratic sector, not full BSDE approximation error. The claim is the quantitative estimate for five positive atoms, not a new exact cubature classification or a claim of optimal constants or exponent. Exact equality identifies the reference design, while the estimate controls the actual masses and positions of nearly optimal rules, which need not lie on a circle.

## Proof

Use the orthonormal basis \(A_1=2^{-1/2}\operatorname{diag}(1,-1)\), \(A_2=2^{-1/2}\begin{pmatrix}0&1\\1&0\end{pmatrix}\) of the trace-free symmetric sector. Let \(K_{ij}=\frac14\mathbb E[(\xi^{\mathsf T}A_i\xi)(\xi^{\mathsf T}A_j\xi)]\); then \(\Lambda=\lambda_{\max}(K)\). Put \(s=|\xi|^2/2\). The identities \(\mathbb E s=1\) and \(\operatorname{tr}K=\frac18\mathbb E|\xi|^4=\frac12\mathbb E s^2\) give \(\Lambda\ge1/4\). A uniform pentagon on the circle of radius \(\sqrt2\) has the first four angular moments zero; this gives the required moments and \(K=I_2/4\). Under the assumed upper bound, \(\operatorname{tr}K\le1/2+2\varepsilon\), and the smaller eigenvalue is at least \(1/4-\varepsilon\) because the trace is at least \(1/2\). Consequently
\[
\mathbb E(s-1)^2\le4\varepsilon,\qquad \|K-I_2/4\|_{\rm op}\le\varepsilon.
\]

Write \(\xi_1+i\xi_2=\sqrt{2s}\,z\) with \(|z|=1\), choosing an arbitrary direction at zero, and let \(m_k=\mathbb E z^k\). The exact moment constraints give \(\mathbb E s^{k/2}z^k=0\) for \(k=1,2,3\). For the first two moments, Cauchy–Schwarz and \(|\sqrt{s}-1|\le|s-1|\) give \(|m_k|\le2\sqrt\varepsilon\). For the third use \(|s^{3/2}-1|\le\tfrac32|s-1|(1+\sqrt{s})\) and \(\mathbb E(1+\sqrt{s})^2\le4\) to get \(|m_3|\le6\sqrt\varepsilon\). For the fourth, expansion in the chosen basis gives
\[
\mathbb E(\xi_1+i\xi_2)^4=8(K_{11}-K_{22})+16iK_{12}.
\]
In particular \(|\mathbb Es^2z^4|\le8\varepsilon\): the modulus after dividing by four is twice the eigenvalue gap of \(K\), and this gap is at most \(2\varepsilon\). Also
\[
\mathbb E|s^2-1|\le \bigl(\mathbb E(s-1)^2\mathbb E(s+1)^2\bigr)^{1/2}\le5\sqrt\varepsilon,
\]
since \(\mathbb E(s+1)^2=4+\mathbb E(s-1)^2\). Thus \(|m_4|\le6\sqrt\varepsilon\) on the given range. Below we use the common weaker bound \(7\sqrt\varepsilon\) for \(k=1,2,3,4\).

For \(0\le k,j\le4\) define the square matrix \(V_{kj}=\sqrt{w_j}z_j^k\). The diagonal of \(VV^*\) is one and its off-diagonal entries are the first four moments or their conjugates. The maximum absolute row sum bounds the operator norm of the Hermitian matrix \(VV^*-I_5\) by \(28\sqrt\varepsilon<1\). Thus \(V\) is invertible and \(V^*V-I_5\) has the same norm bound. The diagonal now gives \(|5w_j-1|\le28\sqrt\varepsilon\) and \(w_j\ge0.19\). For \(i\ne j\), dividing the corresponding off-diagonal bound by \(\sqrt{w_iw_j}\) yields
\[
\left|\sum_{k=0}^4(z_j/z_i)^k\right|\le150\sqrt\varepsilon,
\qquad
\left|(z_j/z_i)^5-1\right|\le300\sqrt\varepsilon.
\]
The second inequality results from multiplying the geometric sum by \(z_j/z_i-1\), whose modulus is at most two.

Relative to a reference node \(z_0\), assign each \(z_j/z_0\) a nearest fifth root of unity. If the angular distance to that root is \(2x\le\pi/5\), then \(\sin(5x)\ge\sin x\) on \([0,\pi/10]\); the preceding estimate therefore bounds the chord distance to the assigned root by \(300\sqrt\varepsilon\). The reference node is assigned the root 1. If two nodes had the same assigned root, their ratio \(w\) would satisfy \(|w-1|\le600\sqrt\varepsilon\). Telescoping each power gives \(|\sum_{k=0}^4w^k-5|\le10|w-1|\), so the sum would have modulus at least \(4.4\), contradicting its upper bound \(150\sqrt\varepsilon\le0.015\). The assignment is therefore bijective. Relabel the nodes by these roots and take \(\theta=\arg z_0\).

The radial estimate and \(w_j\ge0.19\) give \(|s_j-1|\le5\sqrt\varepsilon\) for every atom; in particular none is zero. The radial and angular estimates together yield
\[
\bigl\|x_j-\sqrt2\,u(\theta+2\pi j/5)\bigr\|_2
\le\sqrt2(5+300)\sqrt\varepsilon\le440\sqrt\varepsilon.
\]
The diagonal estimate gives the asserted weight bound. All bounds are non-strict, including at \(\varepsilon=0\).

## Relationship to prior work

Tanaka's universal trace-free defect bound and its equality characterization by normalized weighted spherical 4-designs give the baseline \(1/4\) here. At equality with five atoms the angular problem is the five-node positive quadrature rule on the unit circle exact through trigonometric degree four. This exact rule is classical: in the unit-circle quadrature description of Peherstorfer, the node polynomial for Haar measure has the form \(z^5+\eta\), \(|\eta|=1\), giving a uniform regular pentagon. The quantitative comparison starts instead with small defect excess for a genuinely planar law. It uses radial concentration and the full operator bound to obtain an approximate square moment matrix before deriving atomwise bounds. It is not an estimate assuming beforehand that nodes are on the circle or close to prescribed locations.

## Verification and limitations

The argument above establishes the inequalities for all laws under the stated assumptions. The accompanying tests in the original package for regular polygons and perturbed Vandermonde matrices are illustrations; the perturbed samples need not satisfy the theorem's exact low-order moments and are not a proof of stability. No optimal constants, optimal exponent, or extension to more than five atoms is asserted.

## References

1. A. Tanaka, *Third-moment cancellation and predictable representation in finite-state BSDE approximation*, [arXiv:2610.20880v1](https://arxiv.org/abs/2610.20880), Theorem 6.3 and Corollary 6.4.
2. F. Peherstorfer, *Positive trigonometric Quadrature Formulas and Quadrature on the Unit Circle*, [arXiv:1001.2451](https://arxiv.org/abs/1001.2451), equations (4) and (9).

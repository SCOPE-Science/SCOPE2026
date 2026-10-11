# Exact arithmetic rank of two-hole cyclic Gabor measurements

## Finding
Let \(N\ge5\) be an integer and \(1\le a<N\). Put \(d=\gcd(N,a)\), \(q=N/d\), and let \(g\in\mathbb C^N\) be the unit vector whose entries are zero at \(0,a\) and equal \(1/\sqrt{N-2}\) elsewhere. For \(r,s\in\mathbb Z_N\), let \(P_{r,s}\) be the orthogonal rank-one projector onto \(M_sT_rg\), where \(T_rg(t)=g(t-r)\) and \(M_sg(t)=e^{2\pi ist/N}g(t)\). Let \(R_N(a)\) be the complex dimension of the span of all \(N^2\) such projectors.

Define \(H_N=0\) for odd \(N\), and for even \(N\) set
\[
H_N=\sum_{h\mid N/2}h\,\varphi(N/h).
\]
Also put
\[
J_d=\sum_{t=0}^{d-1}\gcd(2t+1,d).
\]
Then the **exact rank-deficiency formula**, valid without primality or coprimality assumptions, is
\[
\boxed{N^2-R_N(a)=H_N+\mathbf1_{2\mid q}\left(d(N-2)+2d\,\mathbf1_{q=2}-\frac q2J_d\right)+4d\,\mathbf1_{3\mid q}.}
\]
Here \(\mathbf1_{\mathcal E}\) is one when the stated condition holds and zero otherwise. In particular, for odd \(N\), this Gabor measurement is informationally complete if and only if \(3\nmid q\); all even \(N\) are incomplete. The odd composite example \(N=15\) distinguishes spacing: \(R_{15}(1)=221\), \(R_{15}(3)=225\), and \(R_{15}(5)=205\).

## Assumptions and scope
This is a statement about **linear operator-span informational completeness** for a full cyclic Weyl--Heisenberg orbit of \(N^2\) rank-one projectors. It does not assert an equivalence between failure of operator informational completeness and failure of nonlinear pure-state phase retrieval. The complex span dimension is the rank of the projector Gram matrix. The normalization \(1/\sqrt{N-2}\) changes ambiguity values by a nonzero common factor and hence cannot change the rank. The complementary support has exactly two missing points, not two supported points.

## Proof
By the Gabor Gram-spectrum theorem of Goldberger--Kang--Okoudjou [1, Theorem 1], \(R_N(a)\) equals the number of nonzero Weyl ambiguity coefficients. We give the remaining all-dimensional zero count directly.

Write \(W=\mathbb Z_N\setminus\{0,a\}\), \(\omega=e^{2\pi i/N}\), and for \(\ell,k\in\mathbb Z_N\) define the unnormalized ambiguity sum
\[
A(\ell,k)=\sum_{t\in W\cap(W+\ell)}\omega^{kt}.
\]
All \(A(\ell,0)\) are nonzero because at most four locations are removed and \(N\ge5\). For nonzero \(k\), the complete character sum vanishes, so \(A(\ell,k)\) is the negative of the character sum over \(\{0,a\}\cup\{\ell,\ell+a\}\). Set \(u=\omega^{ka}\) and \(v=\omega^{k\ell}\). There are exactly three mutually exclusive geometries:

1. If \(\ell=0\), the deleted sum is \(1+u\).
2. If \(q\ge3\) and \(\ell=\pm a\), the deleted sum is a unit-modulus multiple of \(1+u+u^2\). When \(q=2\), the two special lags coincide, and the deleted sum is again \(1+u\).
3. At all other lags the four deleted points are distinct and the sum factors as \((1+u)(1+v)\).

Thus the only root-of-unity cancellations are \(u=-1\), \(v=-1\), and, at the two special lags with \(q\ge3\), \(u\) a primitive cube root of unity. The first condition has exactly \(d\) frequency solutions precisely when \(q\) is even; the third has exactly \(2d\) solutions precisely when \(3\mid q\), yielding \(4d\) disjoint zeros from the two special lags.

To count the second condition, for every nonzero lag \(\ell\) the congruence \(k\ell\equiv N/2\pmod N\) has \(\gcd(\ell,N)\) solutions if \(N\) is even and \(\gcd(\ell,N)\mid N/2\), and has none otherwise. Summing over nonzero lags gives exactly \(H_N\), by grouping lags according to \(h=\gcd(\ell,N)\).

It remains to count overlaps of the first two cancellation conditions. Suppose \(q\) is even. Its \(d\) solutions to \(u=-1\) can be parameterized by
\[
k=\frac q2(2t+1),\qquad t=0,\ldots,d-1,
\]
modulo \(N\). Each has \(\gcd(k,N)=(q/2)\gcd(2t+1,d)\) solutions to \(k\ell\equiv N/2\pmod N\); in particular, the total two-condition intersection, before excluding special lags, has size \((q/2)J_d\). When \(q\ge4\), the special lags \(\pm a\) are excluded from both two-point and four-point-factor zeros; exactly \(2d\) of the second-condition points and \(2d\) intersections are removed. The first-condition region has size \(d(N-2)\), so their union has cardinality
\[
H_N-2d+d(N-2)-\left(\frac q2J_d-2d\right)=H_N+d(N-2)-\frac q2J_d.
\]
When \(q=2\), the single special lag \(a=-a\) instead has the valid factor \(1+u\); the first-condition region has \(dN\) points, and its union with the second has cardinality \(H_N+dN-(q/2)J_d\). Both cases equal the claimed \(\mathbf1_{2\mid q}\) correction plus \(H_N\). The primitive-cube-root zeros at the special lags are disjoint from these sets, so adding \(4d\,\mathbf1_{3\mid q}\) completes the proof.

Finally, \(H_N>0\) for every even \(N\), as the lag \(\ell=1\) admits \(k=N/2\). If \(N\) is odd, \(q\) is odd and the formula collapses to \(N^2-R_N(a)=4d\,\mathbf1_{3\mid q}\), proving the completeness criterion.

## Verification
The included standalone `CHECK.py` uses only the Python standard library. Execute `python3 CHECK.py` to verify exactly every \((N,a)\) with \(5\le N\le35\) and \(1\le a<N\), for a total of \(589\) pairs. It computes each ambiguity sum as an integer polynomial modulo the cyclotomic polynomial \(\Phi_N\), and counts exact algebraic zeros; there is no floating-point tolerance or numerical-rank threshold. The independent integer-remainder census agrees with the arithmetic formula at every case. The unrestricted theorem follows from the preceding proof, not from this finite check.

## Relationship to prior work
Goldberger--Kang--Okoudjou [1] established the precise rank/ambiguity equivalence and classified several generic or small-support cases; those ingredients are **not** claimed as new. Bojarovska--Flinth [2] established a nonzero-ambiguity sufficient condition and treated characteristic functions of certain difference sets. The present complement of a two-point set is not one of those difference sets for \(N\ge5\), because its pair-count parameter would be \((N-2)(N-3)/(N-1)=N-4+2/(N-1)\), not an integer. Previous rank classifications for consecutive rectangular indicators cover the special case where \(\gcd(N,a)=1\), up to affine unit reindexing, but do not imply the nonunit-distance cases or the spacing-sensitive rank variation at \(N=15\). The new claim is the **complete nonunit-inclusive arithmetic rank formula** and its explicit torsion criterion; the coprime-distance cases and general spectral rank criterion are credited antecedents.

## Limitations
This determines exact rank, not the nonzero eigenvalue sizes, frame condition numbers, robustness to noise, or minimum measurement subset size. For \(N<5\), overlapping deleted-site cases require separate treatment and are not claimed. Published literature and database searches cannot rule out an unindexed equivalent two-hole classification; such a source would affect originality, not the algebraic proof.

## References
[1] A. Goldberger, S. Kang, K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (public 2021-06-02), Theorem 1; https://arxiv.org/abs/2106.01509.

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v2 (2015), Theorem 2.3 and Section 2.3.2; https://arxiv.org/abs/1503.05800.

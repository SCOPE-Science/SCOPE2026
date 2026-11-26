# Sharp asymptotics for duplicate generators of embedded cyclic transformation submonoids

## Finding

For a positive integer \(n\), let \(T_n\) be the monoid of all self-maps of \([n]\). Let \(M_n\) count the distinct subsets \(\langle f\rangle_1=\{1_n,f,f^2,\ldots\}\) of \(T_n\). Let \(A_n\) count the maps \(f\) for which there is a different \(g\) with \(\langle g\rangle_1=\langle f\rangle_1\). If \(\rho\) is the unique positive solution of \(\rho e^\rho=1\), then
\[
\boxed{\quad n^n-M_n\sim A_n\sim\frac{n!\,\rho^{-n}}{1+\rho}\quad}\qquad(n\to\infty).
\]
Thus the probability that a uniformly random map has another generator for its submonoid satisfies
\[
\frac{A_n}{n^n}\sim\frac{\sqrt{2\pi n}}{1+\rho}\left(\frac1{e\rho}\right)^n.
\]
Here \(\rho>1/e\) since \((1/e)\exp(1/e)<1\). The deficit and the number of maps with another generator are different statistics, even though their leading asymptotics coincide.

## Assumptions and scope

The cyclic submonoid always includes the ambient identity, even for noninvertible \(f\); equality means equality as subsets, not isomorphism or conjugacy. The height \(h(f)\) is the maximum distance to a directed cycle in the functional digraph, and the period \(p(f)\) is the least common multiple of its cycle lengths. The argument is for labeled total self-maps. The totient \(\varphi\) has \(\varphi(1)=1\).

## Proof

**Generator multiplicities.** The first repeat in the sequence of nonnegative powers of \(f\) is \(f^{h+p}=f^h\), where \(h=h(f)\) and \(p=p(f)\). Indeed, an equality \(f^{i+d}=f^i\) with \(d>0\) makes every point of \(f^i([n])\) periodic, so \(i\ge h\); it also forces every cycle length to divide \(d\). Conversely these two conditions give the equality at every vertex. If \(h\ge2\), any other generator would have to be \(1_n\) or a power with exponent at least two; no such generator can recover \(f\), which has no equal power of higher exponent. If \(h=0\), the powers form a cyclic permutation group of order \(p\), with \(\varphi(p)\) generators. If \(h=1\), the positive powers form a cyclic group of order \(p\) with identity \(f^p\ne 1_n\), and exactly the same totient count applies. Hence every non-singleton generator fiber consists of maps of height at most one, with fiber size \(\varphi(p)\).

**The auxiliary class of shallow maps.** Denote by \(H_n\) the number of maps with \(h\le1\), and by \(G_n\) their total weight when each map contributes the reciprocal of its fiber size \(\varphi(p)\). Then \(n^n-M_n=H_n-G_n\). A shallow functional digraph is a labeled set of directed cycles; each cycle vertex carries an unordered set of leaves. The exponential generating function for one decorated vertex is \(T(z)=ze^z\). A cycle of length \(j\) has series \(T(z)^j/j\), so with the empty object counted once,
\[
\sum_{n\ge0}H_n\frac{z^n}{n!}=\exp\!\left(\sum_{j\ge1}\frac{T(z)^j}{j}\right)=\frac1{1-ze^z}.
\]
For \(|z|<\rho\), \(|ze^z|<1\); on the boundary equality \(|ze^z|=1\) holds only at \(z=\rho\). There the denominator has nonzero derivative and the principal part is \((1+\rho)^{-1}(1-z/\rho)^{-1}\). The zeros of the denominator are isolated, so subtracting this principal part leaves an analytic function on a disk of radius strictly greater than \(\rho\). Coefficient estimation gives \(H_n\sim n!\rho^{-n}/(1+\rho)\).

**The reciprocal-totient weight does not affect the leading term.** For any fixed \(B\), the set of periods with \(\varphi(p)\le B\) is finite. For example, for each prime power \(\ell^k\), the ratio \(\varphi(\ell^k)^2/\ell^k=\ell^{k-2}(\ell-1)^2\) is at least one except for \(\ell^k=2\), when it is one-half; multiplicativity yields \(\varphi(p)^2\ge p/2\). Let \(D\) be a common multiple of those finitely many periods. The shallow maps with period dividing \(D\) have exponential generating function
\[
\exp\!\left(\sum_{j\mid D}\frac{(ze^z)^j}{j}\right).
\]
It is entire, so on any fixed circle of radius \(R>\rho\) its Cauchy bound is \(O(n!R^{-n})=o(H_n)\). Off this bounded-totient class, each shallow map's weight is at most \(1/B\). Thus \(0\le G_n/H_n\le o(1)+1/B\). Letting \(n\to\infty\) and then \(B\to\infty\) gives \(G_n=o(H_n)\) and the sharp deficit asymptotic.

Finally, a map has a second generator exactly when its height is at most one and \(\varphi(p)>1\). The excluded shallow maps, with \(p=1\) or \(2\), are counted by the same entire series with \(D=2\), so \(A_n\sim H_n\) as well. Applying Stirling's formula proves the probability estimate.

## Verification and limitations

The accompanying finite checkers compare literal generated submonoids with the exact height/period census through degree six, and evaluate exact deficits by permutation cycle types through degree eighteen. These are bounded checks of the finite quantities entering the proof, not evidence for the asymptotic by extrapolation. The proof of the leading coefficient uses the unique dominant pole and the negligible bounded-totient class, not a fit to finite data.

## Relationship to other work

Elliott, Levine and Mitchell [1] count abstract isomorphism types, not these embedded subsets. The exact embedded census, the height/period refinement and generator multiplicities are given in [2]; [3] also refines by stable rank. Those counts are background here and are not asserted to be new. The related monounary-algebra count [4] already contains the shallow mapping series and its pole asymptotic. The contribution here is the sharp equivalent for the true duplicate-generator deficit and the exceptional probability: a bound by the shallow-map count cannot give the leading constant without controlling the reciprocal-totient weight.

## References

1. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, Communications in Algebra 51 (2023), 4654–4661, https://arxiv.org/abs/2303.12387.
2. *Embedded monogenic transformation submonoids refined by tail depth and cycle period*, Resultary record 98527f06f325, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-embedded-monogenic-transformation-submonoids-refined-by-tail-dep--98527f06f325.
3. *Embedded monogenic transformation monoids: a joint threshold-period-rank census*, Resultary record 98804c666169, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-embedded-monogenic-transformation-monoids-a-joint-threshold-peri--98804c666169.
4. *Labeled enumeration and asymptotic rarity of finite polymorphism-homogeneous monounary algebras*, Resultary record 396b39babc15, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-labeled-enumeration-and-asymptotic-rarity-of-finite-polymorphism--396b39babc15.

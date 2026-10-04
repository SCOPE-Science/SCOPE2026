# A split-pair upper fence for the first odd planar \(p\)-frame transition

## Finding
For an ordered multiset \(X=\{x_i\}_{i=1}^N\) of unit vectors in \(\mathbb R^2\), write
\[
\operatorname{FP}_{p,N,2}(X)=\sum_{i\ne j}|\langle x_i,x_j\rangle|^p.
\]
For odd \(N=2k+1\), let \(X^\perp_{2k+1}\) be the repeated orthonormal configuration with \(k+1\) copies of one coordinate direction and \(k\) copies of the orthogonal direction. Following Ben Av--Chen--Goldberger--Kang--Okoudjou, define \(p(2k+1)\) as the supremum of the numbers \(p_0\) for which \(X^\perp_{2k+1}\) is globally minimizing for every \(0<p<p_0\).

Fix \(0<\alpha<\pi/4\), put \(c=\cos\alpha\), \(s=\sin\alpha\), and \(d=\cos(2\alpha)\), and define \(q_k(\alpha)\) to be the unique solution in \((0,2)\) of
\[
2(k-1)c^q+2ks^q+d^q=2k-1.
\]
Then
\[
p(2k+1)\le q_k(\alpha)<2.
\]
Furthermore,
\[
\lim_{k\to\infty}k\bigl(2-q_k(\alpha)\bigr)
=
C(\alpha):=
\frac{1-2c^2+d^2}{2\bigl(c^2\log c+s^2\log s\bigr)} >0.
\]
At \(\alpha=\pi/8\), this gives
\[
\liminf_{k\to\infty}k\bigl(2-p(2k+1)\bigr)\ge C(\pi/8)=0.497260512828602\ldots.
\]
Thus the first odd planar phase transition, if it converges to \(2\) as conjectured, cannot approach \(2\) faster than order \(1/k\). For the first unresolved odd size \(N=5\), the choice \(\alpha=\pi/7\) yields
\[
p(5)\le q_2(\pi/7)=1.777662643085260\ldots,
\]
a simple algebraic-angle certificate lying extremely close to the numerical transition reported in the motivating paper.

## Assumptions and scope
The result concerns the discrete real planar \(p\)-frame potential with \(p>0\). It does not identify the true minimizer after the first transition, prove monotonicity of \(p(2k+1)\), or prove the conjectured limit \(p(2k+1)\to2\). The decimal values above are reproducible numerical evaluations of exact scalar root equations; the inequalities and asymptotic statement do not depend on those decimals.

## Proof
Represent a unit vector by its projective angle. Besides \(X^\perp_{2k+1}\), consider the split-pair configuration \(Y_{k,\alpha}\) consisting of \(k\) copies at angle \(0\), \(k-1\) copies at angle \(\pi/2\), and one copy at each of \(\pi/2-\alpha\) and \(\pi/2+\alpha\). Since the potential is an ordered sum, it is twice the sum over unordered pairs.

For \(X^\perp_{2k+1}\), the unordered contribution is
\[
\binom{k+1}{2}+\binom{k}{2}=k^2.
\]
For \(Y_{k,\alpha}\), the two repeated blocks contribute \((k-1)^2\). Each of the two split vectors has inner-product magnitude \(s\) with each of the \(k\) vectors at angle \(0\), giving \(2ks^p\). It has inner-product magnitude \(c\) with each of the \(k-1\) vectors at angle \(\pi/2\), giving \(2(k-1)c^p\). The two split vectors have mutual inner-product magnitude \(d\), giving \(d^p\). Therefore the unordered energy difference is
\[
F_k(p;\alpha)
=2(k-1)c^p+2ks^p+d^p-(2k-1).
\]
All three bases \(c,s,d\) lie in \((0,1)\), so \(F_k(p;\alpha)\) is strictly decreasing. As \(p\downarrow0\), its limit is \(2k>0\). At \(p=2\), using \(c^2+s^2=1\),
\[
F_k(2;\alpha)=1-2c^2+d^2=2s^2\bigl(2s^2-1\bigr)<0,
\]
because \(0<s^2<1/2\). Hence there is a unique \(q_k(\alpha)\in(0,2)\) with \(F_k(q_k(\alpha);\alpha)=0\), and \(Y_{k,\alpha}\) has strictly smaller potential than \(X^\perp_{2k+1}\) for every \(p>q_k(\alpha)\). This proves \(p(2k+1)\le q_k(\alpha)\).

For the asymptotics, write
\[
A(p)=c^p+s^p-1,
\qquad
B(p)=1-2c^p+d^p.
\]
The root equation is \(2kA(q_k)+B(q_k)=0\). For every fixed \(p<2\), one has \(A(p)>0\), while \(A(2)=0\), so the strict monotonicity of \(F_k\) implies \(q_k\to2\). By the mean-value theorem, for some \(\xi_k\in(q_k,2)\),
\[
A(q_k)=A'(\xi_k)(q_k-2).
\]
Consequently
\[
k(2-q_k)=\frac{-B(q_k)}{2\bigl(-A'(\xi_k)\bigr)}.
\]
Passing to the limit and using \(A'(2)=c^2\log c+s^2\log s<0\) gives the displayed constant \(C(\alpha)\). The inequality for \(p(2k+1)\) then gives the corresponding lower bound on the transition gap.

For \(\alpha=\pi/8\), \(c^2=(2+\sqrt2)/4\), \(s^2=(2-\sqrt2)/4\), and \(d^2=1/2\), so the constant is an explicit logarithmic expression. For \(k=2\) and \(\alpha=\pi/7\), the same monotone root equation gives the stated upper fence for \(p(5)\).

## Verification
The bundled `verify.py` independently recomputes the pair-count formula from the angle multiset, bisects the scalar root equation for several values of \(k\), checks the sign change and strict decrease, and confirms convergence of \(k(2-q_k(\pi/8))\) toward the closed-form constant. It also reproduces the \(\alpha=\pi/7\), \(k=2\) decimal. These computations are consistency checks; the proof above is analytic.

## Relationship to prior work
Ben Av, Chen, Goldberger, Kang, and Okoudjou define the odd-size threshold \(p(N)\), conjecture that \(p(2k+1)\) increases to \(2\), and report numerical phase transitions, including the first \(N=5\) transition near \(1.77766251887019\). Their paper proves the repeated-orthonormal minimizer only through \(p\le \log 3/\log 2\) for general odd \(N\), and its later phase-transition statements are numerical conjectures. The split-pair comparison here supplies an analytic all-odd-size upper fence and a quantitative order-\(1/k\) obstruction on how fast a first transition can approach \(2\).

Glazyrin and Park earlier proved repeated-orthonormal minimization in the plane on a uniform small-\(p\) interval and developed lower-bound methods for \(p\)-frame energies. Their results provide lower-side information and do not imply the explicit competing family, the root equation above, or the transition-gap asymptotic.

## Limitations
The bound is one-sided. It does not prove that \(q_k(\alpha)\) is the actual transition, nor that the split-pair family is globally optimal after transition. The asymptotic constant depends on the chosen \(\alpha\); optimizing it is a separate scalar problem and is not claimed here. The close agreement of the \(N=5\), \(\alpha=\pi/7\) certificate with the published numerical conjecture is suggestive but is not used as evidence of equality.

## References
1. R. Ben Av, X. Chen, A. Goldberger, S. Kang, K. A. Okoudjou, *Phase transitions for the minimizers of the \(p\)-frame potentials in \(\mathbb R^2\)*, arXiv:2212.04444, first submitted 2022-12-08; SIAM Journal on Discrete Mathematics 38 (2024), 2243--2259, DOI 10.1137/22M1539915.
2. A. Glazyrin, J. Park, *Repeated minimizers of \(p\)-frame energies*, arXiv:1901.06096; SIAM Journal on Discrete Mathematics 34 (2020), 2411--2423, DOI 10.1137/19M1282702.

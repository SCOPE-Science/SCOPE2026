# All-coupling antipodal optimality for two repulsive point interactions on a loop
## Finding
Consider a loop of length \(2\pi\) carrying exactly two identical repulsive delta interactions of strength \(\alpha>0\). If the two complementary arc lengths are \(a\in(0,2\pi)\) and \(b=2\pi-a\), then the ground-state eigenvalue \(\lambda_1(\alpha,a)\) is uniquely maximized when \(a=b=\pi\).

Writing \(k(a)=\sqrt{\lambda_1(\alpha,a)}\), the ground state is characterized exactly by
\[
\alpha=k\left[\tan\left(\frac{ka}2\right)+\tan\left(\frac{kb}2\right)\right],
\qquad
0<k<\frac{\pi}{\max\{a,b\}}.
\]
For the antipodal configuration, its wave number \(k_*\in(0,1)\) is the unique solution of
\[
\alpha=2k_*\tan\left(\frac{\pi k_*}2\right).
\]
For every \(a\ne\pi\), one has \(k(a)<k_*\), and therefore \(\lambda_1(\alpha,a)<\lambda_1(\alpha,\pi)\).

## Assumptions and scope
The operator is the periodic one-dimensional Laplacian with two delta interactions of equal positive strength, in the normalization used by Exner for a loop of circumference \(2\pi\). Across each interaction the eigenfunction is continuous and its derivative has the jump \(\psi'(y+)-\psi'(y-)=\alpha\psi(y)\). The claim concerns the lowest eigenvalue only. Rotations and reflection identify configurations with the same unordered pair of complementary arc lengths. No claim is made here for \(N\ge3\), unequal interaction strengths, magnetic flux, or non-delta vertex conditions.

## Proof
The quadratic form is nonnegative and is strictly positive on constants because \(\alpha>0\), so the ground-state eigenvalue is positive. The connected one-dimensional problem has a simple strictly positive ground state. Reflection of the loop through the two interaction sites preserves the operator and swaps the two sites. Simplicity and positivity therefore force the ground state to be reflection-invariant, so it takes the same positive value \(c\) at both interaction sites and is symmetric on each complementary arc.

On an arc of length \(L\in\{a,b\}\), a positive solution of \(-u''=k^2u\) with the common endpoint value \(c\) is
\[
u_L(x)=c\,\frac{\cos(k(x-L/2))}{\cos(kL/2)}.
\]
Strict positivity on the full arc forces \(0<kL/2<\pi/2\). Hence any ground-state wave number lies in
\[
0<k<\frac{\pi}{\max\{a,b\}}.
\]
At an endpoint the outgoing derivative contributed by that arc is \(ck\tan(kL/2)\). The delta jump condition therefore becomes
\[
\alpha=k\left[\tan\left(\frac{ka}2\right)+\tan\left(\frac{kb}2\right)\right]=:F_a(k).
\]
On the stated interval, \(F_a(0)=0\), \(F_a\) is strictly increasing, and \(F_a(k)\to+\infty\) at the right endpoint. Thus there is exactly one ground-state root \(k(a)\).

Because \(\max\{a,b\}\ge\pi\), this root satisfies \(k(a)<1\). Both arguments \(k(a)a/2\) and \(k(a)b/2\) therefore lie in \((0,\pi/2)\), where \(\tan\) is strictly convex. Jensen's inequality gives
\[
\tan\left(\frac{k(a)a}2\right)+\tan\left(\frac{k(a)b}2\right)
\ge 2\tan\left(\frac{\pi k(a)}2\right),
\]
with equality exactly when \(a=b=\pi\). Hence
\[
\alpha=F_a(k(a))\ge F_\pi(k(a))
=2k(a)\tan\left(\frac{\pi k(a)}2\right).
\]
The function \(F_\pi(k)=2k\tan(\pi k/2)\) is strictly increasing on \((0,1)\). If \(k_*\) is its unique root at value \(\alpha\), then \(k(a)\le k_*\), with strict inequality whenever \(a\ne\pi\). Squaring proves the asserted strict ground-state inequality.

## Verification
A standalone verifier accompanies this result. It independently forms the two-delta transfer matrix around the loop, checks that roots of the displayed scalar equation satisfy the periodic monodromy condition, and numerically stress-tests the strict antipodal inequality for weak, intermediate, and strong repulsive couplings and a range of asymmetric separations. These finite checks corroborate, but do not replace, the analytic proof for all \(\alpha>0\) and all \(a\in(0,2\pi)\).

## Relationship to prior work
Exner's 2019 paper formulates this loop model, proves equal spacing is optimal for weak repulsion and again for sufficiently strong repulsion, and then states the all-coupling assertion as Conjecture 5.1. The present result closes the entire intermediate-coupling gap for the first nontrivial case \(N=2\). The same paper explicitly notes why its preceding convex-resolvent argument does not handle general repulsive coupling. Earlier point-interaction polygon optimization concerns point interactions in \(\mathbb{R}^2\) or \(\mathbb{R}^3\), not repulsive delta interactions on a one-dimensional periodic loop, so it does not imply the claim here.

## Limitations
The proof exploits a special \(N=2\) reflection that reduces the ground state to two scalar arc solutions with equal endpoint values. For \(N\ge3\), different interaction-site amplitudes generally remain coupled, so this argument does not establish the full conjecture. The verifier samples finite parameter sets and is not an exhaustive numerical certificate.

## References
1. Pavel Exner, *An optimization problem for finite point interaction families*, Journal of Physics A: Mathematical and Theoretical 52 (2019), 405302. arXiv:1906.01229; DOI:10.1088/1751-8121/ab3d82.
2. Pavel Exner, *An isoperimetric problem for point interactions*, Journal of Physics A: Mathematical and General 38 (2005), 4795-4802. arXiv:math-ph/0406017; DOI:10.1088/0305-4470/38/22/004.

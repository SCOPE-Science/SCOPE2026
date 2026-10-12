# Exact-width repair of the any-dimensional extremality test
## Finding
Let \(g\ge2\), let \(p\) be prime, and let \(A/\mathbb F_{p^2}\) be an abelian variety of dimension \(g\). Consider the one-sign maximality test that samples a uniformly random point \(P\in A(\mathbb F_{p^2})\) and accepts when
\[
[p+1]P=0.
\]
If \(A\) is not maximal, then its false-positive probability is at most
\[
B_g(p)=\min\left\{1,\frac{(p+1)^{2g}-(p-1)^{2g}}{(p-1)^{2g}}\right\}.
\]
The analogous one-sign minimality test, which accepts when \([p-1]P=0\), satisfies the same bound for every non-minimal \(A\). Consequently, \(k\) independent repetitions of either one-sign test have false-positive probability at most \(B_g(p)^k\).

This gives a rigorous exact-width repair of the probability argument in Theorem 4.1 of arXiv:2610.01924v1. For \(g\ge2\), the threshold \(4gp^{2g-1}\) used in that proof is smaller than the Hasse--Weil width and therefore does not follow from the cited width lemma. The asymptotic conclusion \(O(p^{-1})\) survives after replacing that threshold by the exact width.

## Assumptions and scope
The statement concerns the \(\mathbb F_{p^2}\) extremality branch and uniform sampling from the finite group \(A(\mathbb F_{p^2})\). It is branchwise: maximality uses \([p+1]P=0\), while minimality uses \([p-1]P=0\). No claim is made here about the sharper, surface-specific tests later in the source, nor about a test that accepts the union of both signs in one trial.

Write
\[
W_g(p)=(p+1)^{2g}-(p-1)^{2g}.
\]
This is the exact width of the Hasse--Weil interval over \(\mathbb F_{p^2}\). The Hasse--Weil lower endpoint is \((p-1)^{2g}\).

## Proof
For the maximality branch, let
\[
H_+=A(\mathbb F_{p^2})[p+1].
\]
Because \(H_+\subseteq A[p+1]\cong(\mathbb Z/(p+1)\mathbb Z)^{2g}\), its order divides \((p+1)^{2g}\). The number \((p+1)^{2g}\) is itself the upper endpoint of the Hasse--Weil interval.

Suppose \(|H_+|>W_g(p)\). Two distinct multiples of \(|H_+|\) cannot both lie in an interval of width strictly smaller than \(|H_+|\). Both \(|A(\mathbb F_{p^2})|\) and \((p+1)^{2g}\) are multiples of \(|H_+|\) lying in the Hasse--Weil interval, so they must be equal. Hence \(A\) is maximal. Taking the contrapositive gives
\[
A\text{ non-maximal}\quad\Longrightarrow\quad |H_+|\le W_g(p).
\]
For a uniform random point, acceptance is exactly the event \(P\in H_+\). Therefore
\[
\Pr([p+1]P=0)=\frac{|H_+|}{|A(\mathbb F_{p^2})|}
\le\frac{W_g(p)}{(p-1)^{2g}}.
\]
Capping the right-hand side by \(1\) yields \(B_g(p)\).

For minimality, use
\[
H_-=A(\mathbb F_{p^2})[p-1].
\]
Now \(|H_-|\) divides the lower endpoint \((p-1)^{2g}\). If \(|H_-|>W_g(p)\), uniqueness of a multiple in the Hasse--Weil interval forces \(|A(\mathbb F_{p^2})|=(p-1)^{2g}\), so \(A\) is minimal. The same contrapositive and denominator bound give \(B_g(p)\).

Finally, expanding the exact width gives
\[
W_g(p)=2\sum_{r=0}^{g-1}\binom{2g}{2r+1}p^{2g-2r-1}
=4gp^{2g-1}+2\sum_{r=1}^{g-1}\binom{2g}{2r+1}p^{2g-2r-1}.
\]
When \(g\ge2\), the second sum is strictly positive, so
\[
W_g(p)>4gp^{2g-1}.
\]
Thus the cited width lemma cannot by itself justify the smaller threshold used in the proof of Theorem 4.1. For example, in dimension \(2\),
\[
W_2(p)=8p^3+8p,
\]
not \(8p^3\). Retaining the exact width proves the displayed bound above, and since \(W_g(p)/(p-1)^{2g}=O(p^{-1})\) for fixed \(g\), it repairs the theorem's asymptotic error estimate. Independence gives the \(k\)-fold power bound.

## Verification
The accompanying `verify.py` uses only exact integer and rational arithmetic. It checks the binomial expansion of \(W_g(p)\), the strict positive correction to \(4gp^{2g-1}\) for a grid of dimensions and primes, the dimension-two identity \(W_2(p)=8p^3+8p\), and the fact that the exact-width probability bound has the claimed fixed-\(g\) \(p^{-1}\) scale. Its replay output is recorded in `verification_output.txt`.

The computation is not the proof of the all-\(g\) statement; the proof is the interval-multiple argument and binomial identity above.

## Relationship to prior work
Corte-Real Santos, Lorenzon, and Reijnders state the exact Hasse--Weil interval and a width-bound lemma, then use it to generalize Sutherland's Monte Carlo extremality idea to arbitrary-dimensional abelian varieties. In the proof of their Theorem 4.1 they replace the exact width by \(4gp^{2g-1}\). For \(g\ge2\), that replacement is smaller than the exact width, so the displayed implication is not supplied by their lemma. The present finding is the correction of that proof step and the resulting explicit rigorous error bound; it does not claim that the theorem's asymptotic \(O(p^{-1})\) conclusion is false.

Sutherland's earlier elliptic-curve Monte Carlo argument uses the one-dimensional Hasse interval, whose exact width is \(4\sqrt q\), and proves an explicit false-positive bound in dimension one. It does not state the arbitrary-dimensional exact-width correction above.

Targeted statement-level searches for the source identifier, Theorem 4.1, the threshold \(4gp^{2g-1}\), exact-width extremality error bounds, and equivalent torsion-subgroup formulations found no published correction or stronger arbitrary-dimensional statement covering this claim.

## Limitations
The result repairs the width-bound proof and gives a rigorous universal upper bound; it does not prove that the bound is optimal, nor does it prove that the smaller threshold \(4gp^{2g-1}\) is impossible by some additional structural argument not present in the cited proof. The probability statement is for uniform independent samples and for one chosen sign at a time.

The originality search cannot rule out an unpublished observation or an unindexed note. The mathematical correction is elementary once the exact width and the displayed proof are compared, but its value is that it restores a rigorous error estimate for a newly proposed arbitrary-dimensional verification algorithm.

## References
1. Maria Corte-Real Santos, Gioella Lorenzon, and Krijn Reijnders, “Supersingularity and Superspeciality Verification of Abelian Surfaces,” arXiv:2610.01924v1, 2026.
2. Andrew V. Sutherland, “Identifying supersingular elliptic curves,” LMS Journal of Computation and Mathematics 15 (2012), 317–325; arXiv:1107.1140.

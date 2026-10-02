# Uniform Besicovitch constants above the anisotropic threshold

## Result

Fix \(n\ge1\) and \(a\ge2\). For \(p\ge a\), put
\[
d_{p,a}\big((x,t),(y,s)\big)
=
\left(|x-y|^p+|t-s|^{p/a}\right)^{1/p}
\quad\text{on }\mathbb R^n\times\mathbb R .
\]
There is a finite constant \(B(n,a)\), independent of \(p\), such that every
\((\mathbb R^n\times\mathbb R,d_{p,a})\) with \(p\ge a\) has the strong
Besicovitch covering property with covering multiplicity at most \(B(n,a)\).

Equivalently, the positive side of the mixed-power parabolic family is
uniform in the exponent \(p\) once \(n\) and the anisotropy \(a\ge2\) are
fixed.

The exact threshold \(p\ge a\) itself is prior: a previously published result
proves strong BCP for \(p\ge a\) and failure of weak BCP for \(p<a\) for every
\(a\ge1\). The claim here is only the uniformity of the positive covering
constant for \(a\ge2\).

## Proof

Write \(q=p/a\ge1\). Ball volume has the form
\[
|B_{d_{p,a}}(z,r)|=c_{n,a,p}r^{n+a}.
\]
The constant \(c_{n,a,p}\) cancels from all same-metric packing ratios, so
within one radius scale the usual disjoint-shrink volume argument depends
only on \(n+a\).

It remains to bound the number of widely separated occupied radius scales
uniformly in \(p\). Normalize a ball under test to the unit ball and partition
spatial directions into finitely many caps such that vectors in one cap obey
\[
\langle x_i,x_j\rangle\ge\frac{99}{100}|x_i||x_j|.
\]

Consider a center-excluding family meeting the unit ball, with
\(t_j\ge10\), \(|x_j|\ge10\), and all spatial directions in one such cap.
Order it so \(|x_1|\ge|x_2|\ge\cdots\). The standard near-ray estimate gives
\[
c_p |x_j|^{p-1}|x_{j+1}|
\le
|t_{j+1}-t_j|^q-(t_j-1)^q,
\qquad
c_p=\frac7{10}\left(\frac9{10}\right)^{p-2}.
\]
The right side is positive, hence
\[
t_{j+1}>2t_j-1\ge\frac32t_j.
\]
Moreover
\[
t_2^{1/a}>
c_p^{1/p}|x_1|^{1-1/p}|x_2|^{1/p}
\ge\frac45|x_2|,
\]
because \(c_p^{1/p}\ge4/5\) for all \(p\ge2\).

Choose \(N_a\) so that
\[
\frac45\left(\frac32\right)^{(N_a-2)/a}
\ge
2\left(\frac{20}{17}\right)^{1/a}.
\]
Then a family with at least \(N_a+1\) members would satisfy
\[
t_{N_a}^{1/a}
\ge
2\left(\frac{20}{17}\right)^{1/a}|x_{N_a}|.
\]
Using exclusion in the reverse direction gives
\[
(t_{N_a+1}-1)^q-(t_{N_a+1}-t_{N_a})^q
\le
\left(\frac{17}{20}\right)^q t_{N_a}^q.
\]
Since the left side is nondecreasing in \(t_{N_a+1}\), while
\(t_{N_a+1}\ge3t_{N_a}/2\) and \(t_{N_a}\ge10\), it is at least
\[
\left[\left(\frac75\right)^q-\left(\frac12\right)^q\right]t_{N_a}^q.
\]
For \(q\ge1\),
\[
\left(\frac75\right)^q>
\left(\frac12\right)^q+\left(\frac{17}{20}\right)^q,
\]
a contradiction. Thus this mixed large-coordinate class contains at most
\(N_a\) widely separated scales, independently of \(p\). Reflection handles
large negative time.

For bounded spatial coordinate and very large positive time, set
\[
T_a=20^a+2.
\]
There cannot be two centers with \(|x_j|\le10\) and \(t_j\ge T_a\), because
center exclusion would imply
\[
(t_1-1)^q-(t_1-t_2)^q\le20^p,
\]
whereas convexity gives
\[
(t_1-1)^q-(t_1-t_2)^q
\ge (T_a-1)^q>20^p.
\]
Again the negative-time case is identical.

For bounded time and large spatial coordinate in one cap, two centers would
give the standard spatial estimate
\[
70\,9^{p-2}
\le |t_1-t_2|^q
\le20^q
\le20^{p/2},
\]
which is impossible for every \(p\ge2\). Hence there is at most one such
widely separated scale.

Finally choose a radius scale ratio \(M_a\) larger than
\(10+T_a^{1/a}\) and the fixed greedy constants. Balls in one scale have a
uniform packing bound depending only on \(n+a\). Representatives from scales
separated by an intervening scale are pairwise center-excluding. After the
normalization above, every sufficiently large-radius center lies in one of
the three uniformly bounded geometric classes, while centers with both
coordinates bounded can occupy only finitely many large scales because the
origin is excluded from every earlier ball. Summing over the finitely many
spatial caps and the two time signs gives a uniform backward-intersection
bound depending only on \(n,a\).

Coloring the greedy intersection graph with one more color than that bound
splits the selected family into uniformly many disjoint subfamilies. The
standard maximal-radius greedy covering then proves strong BCP with a
constant \(B(n,a)\) independent of \(p\ge a\).

## Originality boundary

The phase transition \(p=a\) is not claimed here. A previously published
result proves the stronger threshold theorem for all anisotropies \(a\ge1\).
Dobronravov proved the \(a=2\) threshold in the original parabolic family.

The surviving contribution is quantitative uniformity: for every fixed
\(n\) and \(a\ge2\), one covering multiplicity works simultaneously for the
entire half-line \(p\ge a\). The earlier all-anisotropy proof uses constants
that depend explicitly on \(p\); the argument above removes that dependence.

## Limitations

The proof uses \(a\ge2\), in particular in the bounded-time spatial estimate.
No uniform statement is claimed for \(1\le a<2\), for \(p=\infty\), or for
several distinct anisotropic coordinates. No optimal value of \(B(n,a)\) is
claimed.

## References

1. N. Dobronravov, *Besicovitch's covering theorem in the parabolic metric*,
   arXiv:2609.15560 (2026).
2. *Sharp anisotropy threshold for mixed-power parabolic balls*,
   published 18 September 2026,
   https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-anisotropic-parabolic-besicovitch-threshold--51dd101ca283
3. E. Le Donne and S. Rigot, *Besicovitch Covering Property on graded groups
   and applications to measure differentiation*, J. Reine Angew. Math. 750
   (2019), 241--297.

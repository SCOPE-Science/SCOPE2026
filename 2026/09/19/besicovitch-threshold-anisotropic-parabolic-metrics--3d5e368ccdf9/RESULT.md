# Besicovitch threshold for anisotropic parabolic metrics

## Result

Let \(n\ge 1\), let \(a\ge 2\), and for \(1\le p<\infty\) define
\[
d_{p,a}\big((x,t),(y,s)\big)
=
\left(
 |x-y|^p+|t-s|^{p/a}
\right)^{1/p},
\qquad (x,t),(y,s)\in\mathbb R^n\times\mathbb R .
\tag{1}
\]
Then:

1. if \(p\ge a\), \((\mathbb R^n\times\mathbb R,d_{p,a})\) satisfies the
   strong Besicovitch covering property;
2. if \(1\le p<a\), it does not even satisfy the weak Besicovitch covering
   property.

Thus the exact transition is
\[
\boxed{\quad p=a.\quad}
\tag{2}
\]

Moreover, for fixed \(n\) and \(a\), the strong Besicovitch constants in the
range \(p\ge a\) can be chosen uniformly in \(p\).

For \(a=2\), (2) is the theorem of N. Dobronravov,
*Besicovitch's covering theorem in the parabolic metric*,
arXiv:2609.15560. The contribution here is the full higher-anisotropy
classification \(a\ge2\), including uniformity in \(p\ge a\).

The restriction \(a\ge2\) is substantive in the present proof. The range
\(1<a<2\), where \(a\le p<2\) is possible, is not claimed.

## Metric and homogeneity

The map
\[
\rho_a(t,s)=|t-s|^{1/a}
\]
is a metric for \(a\ge1\), and (1) is the \(\ell^p\)-product of the Euclidean
metric and \(\rho_a\); hence it is a metric for \(p\ge1\).

With anisotropic dilations
\[
\delta_r(x,t)=(rx,r^a t),
\]
one has
\[
d_{p,a}(\delta_r z,\delta_r w)=r\,d_{p,a}(z,w).
\tag{3}
\]
Lebesgue measure therefore satisfies
\[
|B_{d_{p,a}}(z,r)|=c_{n,a,p}\,r^{n+a}.
\tag{4}
\]
Only the exponent \(n+a\), not the value of \(c_{n,a,p}\), is used below.

## Positive direction: \(p\ge a\ge2\)

Put
\[
q=\frac pa\ge1.
\tag{5}
\]
The proof follows the classical Besicovitch selection argument once three
geometric facts are available. We give the modifications because they also
show that all constants can be made independent of \(p\ge a\).

A ball meeting the unit ball obeys the elementary lower estimate
\[
d_{p,a}\big(B_1(0),(x,t)\big)^p
\ge
\max\{|x|-1,0\}^p+\max\{|t|-1,0\}^{q}.
\tag{6}
\]
We also repeatedly use, for \(r\ge1\) and \(0\le v\le u\),
\[
u^r-v^r\ge u^{r-1}(u-v).
\tag{7}
\]

### 1. Large spatial and time coordinates in one narrow cone

Consider a finite Besicovitch family of balls
\[
\mathcal F=\{B_{r_j}(x_j,t_j)\}
\]
such that every ball meets \(B_1(0)\), every center lies outside every other
ball,
\[
t_j\ge10,\qquad |x_j|\ge10,
\tag{8}
\]
and
\[
\langle x_i,x_j\rangle\ge\frac{99}{100}|x_i||x_j|.
\tag{9}
\]
Reorder so that
\[
|x_1|\ge|x_2|\ge\cdots.
\tag{10}
\]

Exactly as in the spatial part of Dobronravov's Lemma 2.3, (6), center
exclusion and (9) give
\[
c_p |x_j|^{p-1}|x_{j+1}|
\le
|t_{j+1}-t_j|^q-(t_j-1)^q,
\qquad
c_p=\frac7{10}\left(\frac9{10}\right)^{p-2}.
\tag{11}
\]
The right-hand side is positive. Since both times are at least \(10\), this
forces
\[
t_{j+1}>2t_j-1\ge\frac32t_j.
\tag{12}
\]
For \(j=1\), (11) also gives
\[
t_2^{1/a}
>
c_p^{1/p}|x_1|^{1-1/p}|x_2|^{1/p}
\ge \frac45|x_2|,
\tag{13}
\]
because \(c_p^{1/p}\ge4/5\) for every \(p\ge2\).

Choose an integer \(N_a\ge2\) such that
\[
\frac45\left(\frac32\right)^{(N_a-2)/a}
\ge
2\left(\frac{20}{17}\right)^{1/a}.
\tag{14}
\]
If the family had at least \(N_a+1\) members, (12)--(14) would imply
\[
t_{N_a}^{1/a}
\ge
2\left(\frac{20}{17}\right)^{1/a}|x_{N_a}|.
\tag{15}
\]
Using the ball centered at \((x_{N_a+1},t_{N_a+1})\), its intersection with
the unit ball, and exclusion of \((x_{N_a},t_{N_a})\), we obtain
\[
(t_{N_a+1}-1)^q-(t_{N_a+1}-t_{N_a})^q
\le
2^p|x_{N_a}|^p
\le
\left(\frac{17}{20}\right)^q t_{N_a}^q.
\tag{16}
\]
For \(u\ge t_{N_a}\), the function
\[
u\longmapsto (u-1)^q-(u-t_{N_a})^q
\]
is nondecreasing. By (12) and \(t_{N_a}\ge10\), the left side of (16) is at
least
\[
\left[
 \left(\frac75\right)^q-\left(\frac12\right)^q
\right]t_{N_a}^q.
\tag{17}
\]
But for \(q\ge1\),
\[
\left(\frac75\right)^q
>
\left(\frac12+\frac{17}{20}\right)^q
\ge
\left(\frac12\right)^q+\left(\frac{17}{20}\right)^q,
\]
contradicting (16). Hence
\[
\#\mathcal F\le N_a.
\tag{18}
\]
The same conclusion holds for \(t_j\le-10\) by reflection.

### 2. Bounded spatial coordinate and very large time coordinate

Set
\[
T_a=20^a+2.
\tag{19}
\]
There cannot be two centers with
\[
t_j\ge T_a,\qquad |x_j|\le10
\tag{20}
\]
in such a family. Indeed, if \(t_1\ge t_2\), then (6) and center exclusion
give
\[
(t_1-1)^q-(t_1-t_2)^q\le20^p.
\tag{21}
\]
By (7),
\[
(t_1-1)^q-(t_1-t_2)^q
\ge
(t_1-1)^{q-1}(t_2-1)
\ge
(T_a-1)^q
>
(20^a)^q
=
20^p,
\]
a contradiction. The negative-time case is identical.

### 3. Bounded time coordinate and large spatial coordinate

If
\[
|t_j|\le10,\qquad |x_j|\ge10
\tag{22}
\]
and the vectors \(x_j\) satisfy (9), there is at most one ball. The spatial
calculation in Dobronravov's Lemma 2.5 is unchanged because \(p\ge a\ge2\).
For two centers, ordered by \(|x_1|\ge|x_2|\), it yields
\[
70\,9^{p-2}
\le
|t_1-t_2|^q
\le
20^q
\le
20^{p/2},
\tag{23}
\]
which is impossible for \(p\ge2\).

### Completion of the covering argument

We briefly record why the preceding bounds imply strong BCP.

Fix a greedy selection parameter, for example \(\theta=1\). In a
\(\theta\)-Besicovitch sequence, the balls with radii in one geometric scale
have pairwise disjoint fixed-factor shrinks. By (4), a volume comparison
bounds the number of such balls meeting a fixed ball; the bound depends only
on \(n,a\) and the scale ratio. This is the same packing step as in the
standard Euclidean proof, with homogeneous dimension \(n+a\).

Partition the Euclidean directions into finitely many caps in which (9)
holds. Choose a scale ratio \(M_a>1\) sufficiently large that
\[
M_a> 10+T_a^{1/a}
\tag{24}
\]
and larger than the fixed greedy constants. If two occupied scale bins differ
by at least two, selecting one ball from each gives full pairwise center
exclusion: the larger ball occurs earlier in the greedy sequence, while the
radius gap makes its center lie outside the smaller ball.

After normalizing the ball being tested to \(B_1(0)\), balls of radius
greater than \(M_a\) cannot have simultaneously
\[
|x|\le10,\qquad |t|\le T_a,
\]
because their centers have \(d_{p,a}\)-distance at most
\(10+T_a^{1/a}<M_a\) from the origin, while the origin must lie outside the
ball. Thus every large-radius ball falls into one of the three geometric
classes above (with the two time signs separated). Equations (18), (21) and
(23) therefore bound, in each directional cap, the number of widely separated
occupied scale bins. The within-bin packing bound then gives a uniform bound
on the number of earlier selected balls meeting any selected ball.

Consequently every greedy Besicovitch sequence splits into finitely many
pairwise disjoint subsequences. The usual greedy covering construction then
covers every bounded set of centers. All constants used here depend only on
\(n\) and \(a\), not on \(p\ge a\). This proves s-BCP.

## Negative direction: \(1\le p<a\)

Now
\[
q=\frac pa\in(0,1).
\tag{25}
\]
We construct an infinite Besicovitch family.

Choose \(t_1<t_2<\cdots\), all at least \(1\), recursively and sufficiently
rapidly increasing. Put
\[
r_j=(t_j+1)^{1/a},
\qquad
|x_j|^p=q(t_j+1)^{q-1},
\tag{26}
\]
with all \(x_j\) on the same fixed ray. Since \(q-1<0\), the numbers
\(|x_j|\) decrease to zero. We choose each new \(t_j\) so large that for all
\(i<j\),
\[
(|x_i|-|x_j|)^p
\ge
(t_i+1)(t_j+1)^{q-1}.
\tag{27}
\]
This is possible because, for fixed \(i\), the left side tends to
\(|x_i|^p>0\) while the right side tends to zero.

First, every ball contains the origin. Indeed, concavity of \(u^q\) gives
\[
(t+1)^q-t^q
=
\int_t^{t+1}q\,u^{q-1}\,du
\ge
q(t+1)^{q-1},
\]
hence
\[
d_{p,a}\big((0,0),(x_j,t_j)\big)^p
=
q(t_j+1)^{q-1}+t_j^q
\le
(t_j+1)^q
=
r_j^p.
\tag{28}
\]

Second, if \(i<j\), then
\[
\begin{aligned}
(t_j-t_i)^q
&=
(t_j+1)^q
\left(1-\frac{t_i+1}{t_j+1}\right)^q\\
&>
(t_j+1)^q-(t_i+1)(t_j+1)^{q-1},
\end{aligned}
\tag{29}
\]
because \(0<q<1\) and \((1-u)^q>1-u\) for \(0<u<1\). Combining (27) and
(29),
\[
d_{p,a}\big((x_i,t_i),(x_j,t_j)\big)^p
>
(t_j+1)^q
=
r_j^p.
\tag{30}
\]
Since \(r_i<r_j\), (30) puts each center outside every other ball.

Thus
\[
\{B_{r_j}(x_j,t_j)\}_{j=1}^\infty
\]
is an infinite Besicovitch family with common intersection point \(0\).
Therefore w-BCP fails.

## Context and originality

Dobronravov proved the exact \(p=2\) transition for the standard parabolic
anisotropy \(a=2\):
\[
d_p((x,t),(y,s))
=
\bigl(|x-y|^p+|t-s|^{p/2}\bigr)^{1/p}.
\]
His positive proof isolates three metric-specific geometric lemmas and then
uses the standard Besicovitch packing/greedy argument; his negative proof
constructs an infinite family when \(p<2\).

Le Donne and Rigot classify which positively graded groups admit *some*
homogeneous (quasi-)distance with BCP, and emphasize that BCP is not stable
under bi-Lipschitz changes of homogeneous metric. Their existence theorem does
not classify the particular family (1). Itoh proves the strong covering
theorem for the max-type standard parabolic metric
\(\max\{|x-y|,|t-s|^{1/2}\}\).

To the best of our knowledge, the exact threshold (2) for arbitrary
anisotropy \(a\ge2\), and the uniform-in-\(p\) positive conclusion, have not
appeared previously. Searches included anisotropic and snowflaked product
metrics, homogeneous distances on graded Abelian groups, higher-order
parabolic metrics, weak/strong Besicovitch covering properties, and equivalent
formulations of (1). No theorem covering this two-parameter family was found.

The motivating parabolic preprint is very recent, so a contemporaneous
unindexed observation remains a residual originality risk. No inaccessible
paper was identified whose available theorem statement or metadata gave
concrete evidence of prior coverage.

## Limitations

- The theorem is stated for \(a\ge2\). It does not settle \(1<a<2\) in the
  intermediate range \(a\le p<2\).
- The max metric \(p=\infty\) is not included.
- No optimal numerical Besicovitch constant is claimed.
- The result concerns this explicit Abelian anisotropic metric family; it is
  not a classification of homogeneous metrics on general graded groups.

## References

1. N. Dobronravov, *Besicovitch's covering theorem in the parabolic metric*,
   arXiv:2609.15560v1 (2026).
2. E. Le Donne and S. Rigot, *Besicovitch Covering Property on graded groups
   and applications to measure differentiation*, J. Reine Angew. Math. 750
   (2019), 241--297; arXiv:1512.04936.
3. T. Itoh, *The Besicovitch covering theorem for parabolic balls in Euclidean
   space*, Hiroshima Math. J. 48 (2018), 279--289.

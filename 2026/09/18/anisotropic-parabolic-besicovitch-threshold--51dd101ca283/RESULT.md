# Sharp anisotropy threshold for mixed-power parabolic balls

## Statement

Let \(n\ge 1\), \(\kappa\ge 1\), and \(1\le p<\infty\). On \(\mathbb R^n\times\mathbb R\) define
\[
d_{p,\kappa}((x,t),(y,s))
=\left(|x-y|^p+|t-s|^{p/\kappa}\right)^{1/p}.
\]
This is a metric: it is the \(\ell_p\)-product of the Euclidean metric on \(\mathbb R^n\) and the snowflaked metric \(|t-s|^{1/\kappa}\) on \(\mathbb R\). It is homogeneous under
\[
\delta_r(x,t)=(rx,r^\kappa t),\qquad
 d_{p,\kappa}(\delta_r z,\delta_r z')=r d_{p,\kappa}(z,z').
\]

**Theorem.** The metric space \((\mathbb R^n\times\mathbb R,d_{p,\kappa})\) satisfies the strong Besicovitch covering property if and only if
\[
\boxed{p\ge \kappa.}
\]
More precisely, if \(1\le p<\kappa\), then the weak Besicovitch covering property already fails: there is an infinite family of closed \(d_{p,\kappa}\)-balls with a common point such that no center lies in any other ball.

For \(\kappa=2\) this is exactly the threshold proved by Dobronravov for the usual mixed-power parabolic metric. The result identifies the general threshold as convexity of the vertical power \(p/\kappa\): the positive regime is \(p/\kappa\ge1\), while the negative construction is driven by concavity when \(p/\kappa<1\).

## Proof

Write
\[
\sigma=\frac p\kappa.
\]
The volume of a radius-\(r\) ball is \(c_{n,p,\kappa}r^{n+\kappa}\), by the anisotropic dilation above.

### 1. Failure of w-BCP when \(p<\kappa\)

Assume \(0<\sigma<1\). Choose a strictly increasing sequence \(t_j\to\infty\), recursively as fast as needed below, and set
\[
r_j=(t_j+1)^{1/\kappa},\qquad
 a_j^p=\sigma(t_j+1)^{\sigma-1},\qquad
 x_j=a_j e_1.
\]
Since \(\sigma-1<0\), the numbers \(a_j\) decrease to zero. Choose \(t_{j+1}\) so large that
\[
(a_j-a_{j+1})^p>
\frac{t_j+1}{(t_{j+1}+1)^{1-\sigma}}. \tag{1}
\]
This is possible because the left side tends to \(a_j^p>0\) and the right side tends to zero as \(t_{j+1}\to\infty\).

Concavity of \(u^\sigma\) gives, for \(u=t_j+1\),
\[
(u-1)^\sigma+\sigma u^{\sigma-1}\le u^\sigma.
\]
Hence
\[
d_{p,\kappa}((0,0),(x_j,t_j))^p
=a_j^p+t_j^\sigma
\le(t_j+1)^\sigma=r_j^p,
\]
so every ball \(B_j=B_{r_j}(x_j,t_j)\) contains the origin.

If \(i<j\), then \(0<u=(t_i+1)/(t_j+1)<1\) and, since \(0<\sigma<1\),
\[
(1-u)^\sigma>1-u.
\]
Therefore
\[
(t_j-t_i)^\sigma
>(t_j+1)^\sigma-
\frac{t_i+1}{(t_j+1)^{1-\sigma}}. \tag{2}
\]
Also \(a_i-a_j\ge a_i-a_{i+1}\), and (1) implies
\[
(a_i-a_j)^p>
\frac{t_i+1}{(t_j+1)^{1-\sigma}}. \tag{3}
\]
Adding (2) and (3) yields
\[
d_{p,\kappa}((x_i,t_i),(x_j,t_j))^p
>(t_j+1)^\sigma=r_j^p.
\]
Since \(r_i<r_j\), each of the two centers lies outside the other's ball. Thus \(\{B_j\}\) is an infinite Besicovitch family, so w-BCP fails.

### 2. A near-ray deficit for the positive regime

Now assume \(p\ge\kappa\), so \(\sigma\ge1\). We first isolate the only spatial estimate needed below.

Suppose \(u,v\in\mathbb R^n\), \(a=|u|\ge b=|v|\ge8\), and
\[
\langle u,v\rangle\ge0.99ab.
\]
Then
\[
|u-v|^2\le a^2+b^2-1.98ab\le(a-b/4)^2.
\]
Since \(b\ge8\), \(a-b/4\le a-2\), and for every \(p\ge1\),
\[
\begin{aligned}
(a-1)^p-|u-v|^p
&\ge (a-1)^p-(a-b/4)^p\\
&\ge (a-1)^{p-1}(b/4-1)\\
&\ge 2^{-(p+2)}a^{p-1}b. \tag{4}
\end{aligned}
\]
Denote \(c_p=2^{-(p+2)}\).

We use three consequences of (4). In all of them the balls meet the unit ball and their centers are pairwise excluded from one another.

**Mixed large-coordinate lemma.** Fix the angular condition above. Among balls with
\[
t_j\ge10,\qquad |x_j|\ge8,
\]
there are only finitely many, with a bound depending on \(p,\kappa\).

Indeed, order them so that \(a_j=|x_j|\) is nonincreasing. Meeting the unit ball gives
\[
r_j^p\ge(a_j-1)^p+(t_j-1)^\sigma.
\]
Exclusion of the next center and (4) imply
\[
0<c_pa_j^{p-1}a_{j+1}
\le |t_{j+1}-t_j|^\sigma-(t_j-1)^\sigma.
\]
Because every \(t_j\ge10\), the right side can be positive only on the upward branch, hence
\[
t_{j+1}>2t_j-1\ge\frac32t_j. \tag{5}
\]
Moreover
\[
c_pa_{j+1}^p<t_{j+1}^\sigma,
\]
so \(a_2\le C_p t_2^{1/\kappa}\). Combining this with monotonicity of \(a_j\) and (5),
\[
a_m\le C_p(3/2)^{-(m-2)/\kappa}t_m^{1/\kappa}. \tag{6}
\]
Now use exclusion in the reverse direction between the \(m\)-th and \((m+1)\)-st centers:
\[
(t_{m+1}-1)^\sigma-(t_{m+1}-t_m)^\sigma
\le |x_m-x_{m+1}|^p\le(2a_m)^p. \tag{7}
\]
For \(\sigma\ge1\), the function
\[
z\mapsto(z-1)^\sigma-(z-t_m)^\sigma
\]
is nondecreasing on \([t_m,\infty)\). Using (5) and \(t_m\ge10\), the left side of (7) is at least
\[
(1.4^\sigma-0.5^\sigma)t_m^\sigma.
\]
By (6), the right side is at most
\[
2^pC_p^p(3/2)^{-\sigma(m-2)}t_m^\sigma,
\]
which is impossible for all sufficiently large \(m\). This proves the lemma. Reflection in \(t\) gives the analogous statement for \(t_j\le-10\).

**Vertical lemma.** Fix \(X_0=8\) and choose \(T_0\) so that
\[
(T_0-1)^\sigma>(2X_0)^p.
\]
Then among pairwise center-excluding balls meeting the unit ball with
\[
t_j\ge T_0,\qquad |x_j|\le X_0,
\]
there is at most one. For if \(t_1\ge t_2\), then
\[
(t_1-1)^\sigma-(t_1-t_2)^\sigma<(2X_0)^p,
\]
whereas convexity gives
\[
(t_1-1)^\sigma-(t_1-t_2)^\sigma
\ge(t_1-1)^{\sigma-1}(t_2-1)
\ge(T_0-1)^\sigma.
\]
Again the negative-time statement follows by reflection.

**Horizontal lemma.** Choose \(X_1>X_0\) so large that
\[
c_pX_1^p>(2T_0)^\sigma.
\]
Under the same angular condition, there is at most one pairwise center-excluding ball meeting the unit ball with
\[
|t_j|\le T_0,\qquad |x_j|\ge X_1.
\]
Indeed, after ordering \(|x_1|\ge|x_2|\), (4) and the exclusion inequality give
\[
c_pX_1^p
\le(|x_1|-1)^p-|x_1-x_2|^p
\le|t_1-t_2|^\sigma
\le(2T_0)^\sigma,
\]
a contradiction.

### 3. From the local lemmas to s-BCP

The remaining argument is the standard Besicovitch selection proof, with only the homogeneous dimension changed.

Fix a small selection parameter \(q>0\). A greedy selected sequence satisfies: if \(j<i\), then
\[
r_i\le(1+q)r_j,
\qquad z_i\notin B_{r_j}(z_j).
\]
Consequently the shrunken balls \(B_{r_j/(3+q)}(z_j)\) are disjoint. Because ball volume scales as \(r^{n+\kappa}\), the number of selected balls in any fixed radius annulus that can meet a given ball is uniformly bounded.

Normalize the latter ball to \(B_1(0)\) by translation and \(\delta_r\). Partition the spatial sphere into finitely many caps so that vectors in one cap satisfy the \(0.99\)-angular condition. Bucket all earlier radii by powers of a fixed \(M>2+q\). Representatives from radius buckets separated by at least one intervening bucket have pairwise center exclusion: one-sided exclusion gives distance at least the larger radius, which is then also larger than the smaller radius.

For sufficiently large radius buckets, every center meeting \(B_1(0)\) falls into one of four types:

1. \(|x|\ge X_0\) and \(|t|\ge10\): the mixed lemma applies in each spatial cap and each sign of \(t\);
2. \(|x|\le X_0\) and \(|t|\ge T_0\): the vertical lemma applies;
3. \(|x|\ge X_1\) and \(|t|\le T_0\): the horizontal lemma applies in each spatial cap;
4. \(|x|\le X_1\) and \(|t|\le T_0\): the center lies in a fixed bounded set.

The fourth type can occur only in boundedly many large-radius buckets, because the normalized target center is excluded from every earlier ball, so \(r<d_{p,\kappa}(z,0)\) there. The first three types have only boundedly many occupied separated buckets by the local lemmas. Together with the fixed-annulus packing bound, this yields a uniform bound on the number of earlier selected balls meeting any selected ball.

The intersection graph of the greedy sequence therefore has uniformly bounded backward degree and can be colored with finitely many colors, each color class consisting of pairwise disjoint balls. The usual maximal-radius greedy selection covers the original bounded set of centers; if the available radii are unbounded, one sufficiently large centered ball covers the bounded set immediately. Hence s-BCP holds.

This proves the sharp dichotomy.

## Relation to prior results

Dobronravov proved the exact classification for the fixed parabolic anisotropy \(\kappa=2\): s-BCP for \(p\ge2\), and failure of w-BCP for \(p<2\). The proof above both extends the negative family and replaces the spatial estimate in the positive argument by the near-ray deficit (4), which remains valid for every \(p\ge1\); the threshold then comes entirely from convexity of the vertical exponent \(p/\kappa\).

Itoh proved s-BCP for the max parabolic metric \(\max\{|x-y|,|t-s|^{1/2}\}\). Aimar--Forzani treated a different family of anisotropic quasi-balls
\[
\sum_i\left(\frac{|x_i-y_i|}{r^{a_i}}\right)^q\le1
\]
with a common power \(q\), obtaining the threshold \(q\ge \max a_i/\min a_i\). That family does not specialize to the present mixed-power balls when \(\kappa\ne1\), because the present spatial and temporal powers are \(p\) and \(p/\kappa\), respectively. Le Donne--Rigot classified which graded groups admit *some* homogeneous (quasi-)distance with BCP; that structural existence theorem does not decide BCP for this explicit distance family.

## Limitations

The theorem concerns one anisotropic coordinate and finite \(p\). It does not determine optimal Besicovitch constants, does not treat \(p=\infty\), multiple distinct anisotropic coordinates, or quasi-metric regimes with \(p<1\) or \(\kappa<1\).

## References

1. N. Dobronravov, *Besicovitch's covering theorem in the parabolic metric*, arXiv:2609.15560v1 (2026), https://arxiv.org/abs/2609.15560.
2. T. Itoh, *The Besicovitch covering theorem for parabolic balls in Euclidean space*, Hiroshima Math. J. 48 (2018), 279--289, doi:10.32917/hmj/1544238028.
3. H. Aimar and L. Forzani, *On the Besicovitch Property for Parabolic Balls*, Real Anal. Exchange 27 (2001/02), 261--268, doi:10.2307/44154122.
4. E. Le Donne and S. Rigot, *Besicovitch Covering Property on graded groups and applications to measure differentiation*, J. Reine Angew. Math. 750 (2019), 241--297, doi:10.1515/crelle-2016-0051.

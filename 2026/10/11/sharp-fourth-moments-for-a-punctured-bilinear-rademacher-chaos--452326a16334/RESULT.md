# Sharp fourth moments for a punctured bilinear Rademacher chaos

## Finding

For each integer \(n\ge 2\), let \(\varepsilon_1,\ldots,\varepsilon_n,\eta_1,\ldots,\eta_n\) be mutually independent uniform signs. Define the real subspace
\[
X_n=\operatorname{span}_{\mathbb R}\{\varepsilon_i\eta_j:1\le i,j\le n,\ (i,j)\ne(n,n)\}\subset L^4(\{-1,1\}^{2n}).
\]
For arbitrary real coefficients on its \(n^2-1\) displayed characters set
\[
Q_a=\sum_{(i,j)\ne(n,n)}a_{ij}\varepsilon_i\eta_j,
\qquad B=\sum_{(i,j)\ne(n,n)}a_{ij}^2=\mathbb E Q_a^2.
\]
Then the following coefficient is **exactly sharp**:
\[
\boxed{\mathbb E Q_a^4\le C_n B^2,\qquad
C_n=3-\frac1{n-1}+\frac{(6n-11)^2}{6n^2-11n+1}.}
\]
Equivalently, the precise norm of the identity embedding of \(X_n\), endowed with its \(L^2\) norm, into \(L^4\) is \(C_n^{1/4}\). For example \(C_2=7/3\), \(C_3=52/11\), and \(C_4=931/159\).

All nonzero equality cases are described as follows. Let \(k=n-1\), choose \(s>0\), arbitrary row signs \(\sigma_i\in\{-1,1\}\) and column signs \(\tau_j\in\{-1,1\}\), and put
\[
a_{ij}=\begin{cases}
 s\sigma_i\tau_j\sqrt{(6k-5)/(3k-2)},&1\le i,j\le k,\\
 s\sigma_i\tau_j,&\text{exactly one of }i,j\text{ equals }n,\\
 0,&i=j=n.
\end{cases}
\]
These and only these nonzero arrays attain equality. The case \(n=2\) uses the same description and has three equal coefficient magnitudes.

## Assumptions and scope

All scalars are real. Signs are independent, symmetric, and sampled under the normalized counting measure, so \(\mathbb E1=1\). The only excluded character is \(\varepsilon_n\eta_n\); there are no diagonal exclusions at other positions. The bound holds for every real coefficient array, without rank or positivity assumptions. The coefficient \(C_n\) depends only on \(n\ge2\), and the zero array satisfies the inequality trivially.

## Proof

**Step 1: exact fourth-moment expansion.** Regard each allowed coefficient as the weight of an edge of the bipartite graph \(K_{n,n}\setminus\{(n,n)\}\). Orthogonality of the sign characters shows that a product of four distinct edge characters has nonzero expectation exactly when those four edges form a rectangle (a simple four-cycle); the expectation then equals one. Terms with repeated edges yield the other contributions. Consequently, writing \(\mathcal R\) for the set of rectangles,
\[
\mathbb E Q_a^4
 =3B^2-2\sum_e a_e^4+24\sum_{R\in\mathcal R}\prod_{e\in R}a_e.\tag{1}
\]
Replacing each coefficient by its absolute value leaves the first two terms unchanged and cannot decrease the last. Thus it suffices initially to optimize nonnegative weights.

**Step 2: rigorous root-mean-square symmetrization.** Set \(k=n-1\) and first equalize the \(k\) upper-row entries of *each* column \(j\): replace \(a_{ij}\), for \(1\le i\le k\), by \(\sqrt{S_j/k}\), where \(S_j=\sum_{i=1}^k a_{ij}^2\); keep the bottom-row entries unchanged. This preserves \(B\), and \(\sum a_e^4\) does not increase by Cauchy--Schwarz.

To verify the rectangle term rather than assume a symmetrization principle, fix two distinct columns \(j,\ell\) and write \(u_i=a_{ij}\), \(v_i=a_{i\ell}\) for \(i\le k\). Rectangles whose two rows are upper rows contribute
\[
\sum_{i<i'}u_iu_{i'}v_iv_{i'}
\le\sqrt{\Big(\sum_{i<i'}u_i^2u_{i'}^2\Big)
\Big(\sum_{i<i'}v_i^2v_{i'}^2\Big)}
\le \frac{k-1}{2k}S_jS_\ell.\tag{2}
\]
Here the last inequality follows by \(\sum_{i<i'}u_i^2u_{i'}^2\le(k-1)(\sum_i u_i^2)^2/(2k)\). Rectangles whose second row is the bottom row contribute
\[
a_{nj}a_{n\ell}\sum_{i=1}^k u_iv_i
\le a_{nj}a_{n\ell}\sqrt{S_jS_\ell}.\tag{3}
\]
Each displayed upper bound is exactly attained after the proposed equalization. Thus the sum of rectangle contributions cannot decrease. By equation (1), the fourth moment cannot decrease.

Perform the transpose operation next, equalizing each row across its first \(k\) columns. The same proof applies to these columns. We conclude that an optimizer exists in the three-block family
\[
a_{ij}=\begin{cases}t,&i,j\le k,\\u,&i\le k,j=n,\\v,&i=n,j\le k,\\0,&i=j=n,\end{cases}
\qquad t,u,v\ge0.\tag{4}
\]
Moreover, if \(k\ge2\), equality in each quartic Cauchy--Schwarz step forces the magnitudes to have already been constant within every equalized group. This observation will identify every equality case.

**Step 3: solve the exact three-block problem.** In (4), the coefficient energy and quartic self-terms are
\[
B=k^2t^2+k(u^2+v^2),\qquad
\sum_e a_e^4=k^2t^4+k(u^4+v^4).
\]
There are \(\binom{k}{2}^2\) upper-left rectangles, and \(k\binom{k}{2}\) of each of the two mixed types. Accordingly,
\[
\sum_{R\in\mathcal R}\prod_{e\in R}a_e
=\binom{k}{2}^2t^4+k\binom{k}{2}t^2(u^2+v^2).\tag{5}
\]
For \(B>0\), set \(p=k^2t^2/B\), \(q=ku^2/B\), and \(r=kv^2/B\). They are nonnegative and sum to one. Substitution into (1) gives
\[
F_k(p,q,r):=\frac{\mathbb E Q_a^4}{B^2}
=3+\frac{6(k-1)^2-2}{k^2}p^2
 -\frac2k(q^2+r^2)+\frac{12(k-1)}k p(q+r).\tag{6}
\]
For fixed \(p\), the strictly concave quadratic term in \(q,r\) is maximized precisely when \(q=r=(1-p)/2\). The resulting polynomial in \(p\) is
\[
G_k(p)=3-\frac1k+\frac{12k-10}{k}p
-\frac{6k^2+k-4}{k^2}p^2.\tag{7}
\]
For all \(k\ge1\), its strictly interior maximum occurs at
\[
p_* =\frac{k(6k-5)}{6k^2+k-4},\qquad
q_*=r_* =\frac{3k-2}{6k^2+k-4}.\tag{8}
\]
In particular \(0<p_*<1\) and the corresponding ratio of block magnitudes is \(t^2/u^2=(6k-5)/(3k-2)\), with \(u=v>0\). Completing the square yields the **exact three-block deficit**
\[
C_n-F_k(p,q,r)=\frac{6k^2+k-4}{k^2}(p-p_*)^2
+\frac{(q-r)^2}{k},\qquad p+q+r=1.\tag{9}
\]
Its vanishing proves the proposed constant and sharpness, with formula (8) determining the complete positive extremal pattern. The identity (9) is asserted for the three-block family; it is not presented as an unproved arbitrary-coefficient stability inequality.

**Step 4: equality and sign switching.** For \(k\ge2\), equality in (2) and the strictly convex fourth-power step of each successive symmetrization forces every upper-row column and every first-\(k\)-column row to have constant magnitudes. Equation (9) then forces exactly the magnitudes of the statement, all strictly positive. For \(k=1\), (6) directly gives three equal nonzero magnitudes. Equality when passing from signed to absolute coefficients requires a positive product of signs around every rectangle. Every cycle of \(K_{n,n}\setminus\{(n,n)\}\) is generated over \(\mathbb F_2\) by its rectangles: any cycle of length at least six has at least two possible chords and at most one unavailable edge, so it has an available chord; repeatedly split until only rectangles remain. (For \(n=2\), the graph is a tree.) Hence the sign product is positive around every cycle, and a spanning-tree assignment expresses every edge sign as a row sign times a column sign. Conversely, every such sign switching leaves \(\mathbb E Q_a^4\) unchanged. This completes the classification.

## Verification

The companion file `verify.py` is a standalone exact-arithmetic verifier requiring Python 3 and `sympy`. Run `python3 verify.py`. It checks (6)--(9) symbolically; sharp constants and extremizers for the first three dimensions; exact direct sign enumeration for \(n=2,3\); random integer-coefficient diagnostics; and the binary cycle-space rank in dimensions \(2\) through \(6\). The actual run returned `VERIFY_OK`. These finite checks corroborate the algebra but **do not replace** the all-\(n\) symmetrization and graph-theoretic proof above.

## Relationship to prior work

General fourth-moment estimates for bilinear and higher-order Rademacher forms, including Ibragimov--Sharakhmetov--Cecen [1], concern random-variable moment constraints and complete coefficient patterns. Pass--Spektor [2] studies varying the joint law of pairwise-independent signs. Döbler--Krokowski [3] studies fourth moments as a criterion for normal approximation of homogeneous Rademacher chaos. Those results motivate the setting and furnish broad bounds or other conclusions; their inspected principal theorems do not specify this punctured coefficient-space norm or its two-level equality pattern.

As a direct benchmark, retaining **all** \(n^2\) products \(\varepsilon_i\eta_j\) yields the sharp fourth-moment ratio \((3-2/n)^2\) by finite-dimensional scalar Khintchine and tensorization. The missing single character creates a strict, exactly measured loss: with \(k=n-1\),
\[
\left(3-\frac2n\right)^2-C_n
=\frac{4(9k^3+3k^2-6k-1)}{k(k+1)^2(6k^2+k-4)}>0,
\qquad
\lim_{n\to\infty} n^2\left[\left(3-\frac2n\right)^2-C_n\right]=6.\tag{10}
\]
Neither the unrestricted sharp constant nor a dimension-free hypercontractive bound determines this strict deficit, its finite-dimensional rational expression, or the new extremizers.

## Limitations

The result assumes real coefficients, independent symmetric signs, one missing corner of a square bipartite interaction pattern, and exponent four. It is not a claim about complex coefficients, multiple deleted edges, higher moments, or the Euclidean Banach--Mazur distance of the subspace. A search of accessible mathematical records cannot exclude every unindexed earlier equivalent. No independent audit is asserted.

## References

[1] R. Ibragimov, Sh. Sharakhmetov and A. Cecen, *Exact Estimates for Moments of Random Bilinear Forms*, arXiv:math/9909111 (first submitted 20 September 1999), especially Sections 1--3 and Theorems 4--8. https://arxiv.org/abs/math/9909111

[2] B. Pass and S. Spektor, *On Khinchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859 (2014), especially Theorem 2.1. https://arxiv.org/abs/1412.7859

[3] C. Döbler and K. Krokowski, *On the Fourth Moment Condition for Rademacher Chaos*, arXiv:1706.00751 (2017), especially the introduction and Theorem 1.1. https://arxiv.org/abs/1706.00751

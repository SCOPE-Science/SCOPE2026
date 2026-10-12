# Sharp three-summand point concentration at the first fractional atom cap

## Finding

For an integer-valued random variable \(X\), put
\[
Q(X)=\sup_{k\in\mathbb Z}\Pr(X=k).
\]
Let \(X_1,X_2,X_3\) be **independent**, not necessarily identically distributed, integer-valued random variables. For every \(\alpha\in[1/3,1/2]\), assume \(Q(X_i)\leq\alpha\) for \(i=1,2,3\). Then the optimal universal bound is
\[
\boxed{Q(X_1+X_2+X_3)\leq F(\alpha):=
\begin{cases}
\alpha(7\alpha^2-6\alpha+2),&1/3\leq\alpha\leq2/5,\\
3\alpha^2(1-\alpha),&2/5\leq\alpha\leq1/2.
\end{cases}}
\]
Both branches are **attained for every allowed** \(\alpha\). Let \(\beta=1-2\alpha\), and let \(U\) and \(V\) take values in \(\{0,1,2\}\) with respective probability vectors \((\beta,\alpha,\alpha)\) and \((\alpha,\alpha,\beta)\). For \(\alpha\leq2/5\), independent \(U_1,U_2,V_3\) attain equality at sum \(3\). For \(\alpha\geq2/5\), three independent copies of \(U\) attain equality at sum \(4\). Thus there is a genuine optimizer-orientation transition at \(\alpha=2/5\), with \(F(2/5)=36/125\).

This is an exact three-summand equal-cap case of the signed minimal-variance extremizer inequality formulated as Conjecture 1.3 in Kurauskas (2026). The result makes no assertion for a different number of summands, unequal caps, noninteger groups, or \(\alpha\) outside this interval.

## Assumptions and scope

The supports may be arbitrary countable subsets of \(\mathbb Z\), with no moment, boundedness, or shape assumptions. Only independence and the same individual upper bound \(Q(X_i)\leq\alpha\) are imposed. For \(\alpha\in(1/3,1/2)\), define
\[
\beta=1-2\alpha>0,\qquad \delta=3\alpha-1>0,
\qquad \alpha=\beta+\delta.
\]
We use \(1_A\) for the indicator function of a finite integer set \(A\), and for finite \(A,B,C\subset\mathbb Z\) write
\[
R(A,B,C;k)=\#\{(a,b,c)\in A\times B\times C:a+b+c=k\}.
\]

## Proof

**1. Reduction to three-atom extreme laws.** Fix \(\alpha\in(1/3,1/2)\) and a finite set \(T\subset\mathbb Z\). In the polytope of mass functions supported in \(T\) satisfying \(0\leq p_x\leq\alpha\) and \(\sum_{x\in T}p_x=1\), any extreme point has at most one coordinate strictly between \(0\) and \(\alpha\). Otherwise two such coordinates can be perturbed in opposite directions. The only possible extreme points consequently assign \(\alpha\) to two sites, \(\beta=1-2\alpha\) to a third, and zero elsewhere. Conversely these are extreme points. Each mass function in the finite polytope is a convex combination of them.

At a fixed target integer \(k\), \(\Pr(X_1+X_2+X_3=k)\) is separately affine in each mass function. It therefore suffices to bound all triples of three-atom extreme laws. For arbitrary infinite supports, choose finite sets retaining mass at least \(1-\varepsilon\), and move the remaining mass (at most \(\varepsilon\leq\alpha\)) to one unused site of each law. The resulting finite laws still respect the cap, their total-variation distances tend to zero, and hence so do their convolution probabilities. The same argument includes the endpoints: at \(\alpha=1/3\) the extreme laws are uniform on three sites; at \(\alpha=1/2\) they are uniform on two sites, equivalently with \(\beta=0\) and a dummy third site.

For each extreme law, let \(S_i\subset\mathbb Z\) be its three sites and \(H_i\subset S_i\) its two sites with mass \(\alpha\). The mass function equals
\[
p_i=\beta 1_{S_i}+\delta 1_{H_i}.
\]
This equality remains true at both endpoints if \(\delta=0\) or \(\beta=0\), with dummy zero-weight sites allowed.

**2. Counting bounds.** For arbitrary three-element sets \(A,B,C\) and two-element sets \(H,H',H''\), and any integer \(k\),
\[
\begin{aligned}
R(A,B,C;k)&\leq7,\\
R(H,B,C;k)&\leq5,\\
R(H,H',C;k)&\leq4,\\
R(H,H',H'';k)&\leq3.
\end{aligned}
\tag{1}
\]
Indeed, the convolution of two indicators of three-element sets has individual multiplicities at most \(3\), and multiplicity \(3\) at **at most one** target: if every element of \(B\) matches one of \(C\), the latter must be a translate of \(-B\), determining the target uniquely. The sum of the three largest multiplicities is therefore at most \(3+2+2=7\), and the sum of the two largest is at most \(3+2=5\). The third inequality follows by selecting the four possible ordered pairs from two two-element sets. In the convolution of two two-element indicators, multiplicity \(2\) occurs at at most one target, so its two largest multiplicities sum to at most \(2+1=3\).

**3. The necessary one-unit incompatibility.** Suppose the first bound in (1) is sharp, that is \(R(S_1,S_2,S_3;k)=7\). Fix \(S_2,S_3\) and denote \(r(t)=R(S_2,S_3,\{0\};t)\). In order that three values of \(r\) sum to \(7\), they must be \(3,2,2\). The unique target \(t_0\) having multiplicity \(3\) forces \(S_3=t_0-S_2\). Then \(r(t_0+h)\) counts ordered differences of elements of \(S_2\) equal to \(h\). A nonzero difference occurs twice among a three-element set only if that set is a three-term arithmetic progression, with \(|h|\) its common spacing. The two multiplicity-\(2\) targets are \(t_0-h\) and \(t_0+h\), so \(S_1\) must be a translated progression with the same spacing. Repeating for cyclically permuted pairs yields
\[
S_i=\{u_i,u_i+h,u_i+2h\}\quad(i=1,2,3),
\qquad k=u_1+u_2+u_3+3h,
\tag{2}
\]
for some \(h\in\mathbb Z_{>0}\).

Suppose additionally that all **three** two-heavy-one-full counts in (1) were equal to \(4\):
\[
R(H_1,H_2,S_3;k)=R(H_1,H_3,S_2;k)=R(H_2,H_3,S_1;k)=4.
\tag{3}
\]
After translating and dividing the site indices by \(h\), every \(H_i\) is a two-element subset of \(\{0,1,2\}\), and the four sums of any pair \(H_i,H_j\) would all have to belong to \(\{1,2,3\}\). This forces both pair subsets to be **adjacent**, hence to be \(\{e_i,e_i+1\}\) with \(e_i\in\{0,1\}\). Their four pair sums have minimum \(e_i+e_j\) and maximum \(e_i+e_j+2\), so containing all four in \(\{1,2,3\}\) requires \(e_i+e_j=1\). The three pairs would demand
\[
e_1+e_2=e_1+e_3=e_2+e_3=1,
\]
which is impossible for binary \(e_1,e_2,e_3\). Thus whenever the first count is \(7\), **at least one** two-heavy-one-full count is at most \(3\).

**4. Weighted expansion and sharp envelope.** Expanding the three mass functions gives at a fixed target \(k\)
\[
\begin{aligned}
P_k={}&\beta^3 R(S_1,S_2,S_3;k)\\
&+\beta^2\delta\sum_i R(H_i,S_j,S_\ell;k)\\
&+\beta\delta^2\sum_{i<j}R(H_i,H_j,S_\ell;k)
+\delta^3R(H_1,H_2,H_3;k),
\end{aligned}
\tag{4}
\]
where in each summand \(\{i,j,\ell\}=\{1,2,3\}\). Bound (1) implies the naive maximum
\[
P_k\leq W:=7\beta^3+15\beta^2\delta+12\beta\delta^2+3\delta^3.
\]
But if the first count is at most \(6\), the weighted deficit from \(W\) is at least \(\beta^3\). If it equals \(7\), Step 3 forces a deficit of at least \(\beta\delta^2\). Therefore for **every** extreme triple
\[
P_k\leq W-\min\{\beta^3,\beta\delta^2\}.
\tag{5}
\]
This also holds at the endpoints by nonnegativity and continuity. Because \(\beta-\delta=2-5\alpha\), elementary expansion gives
\[
W-\beta\delta^2=7\alpha^3-6\alpha^2+2\alpha
\quad(\alpha\leq2/5),
\]
\[
W-\beta^3=3\alpha^2(1-\alpha)
\quad(\alpha\geq2/5).
\]
Taking the supremum over \(k\), then the finite-law approximation limit from Step 1, proves the proposed upper bound.

**5. Exact attainment.** For independent \(U_1,U_2\) having probabilities \((\beta,\alpha,\alpha)\) at \(0,1,2\) and independent \(V_3\) having \((\alpha,\alpha,\beta)\), direct convolution at the target \(3\) yields
\[
\Pr(U_1+U_2+V_3=3)=7\alpha^3-6\alpha^2+2\alpha.
\]
For three independent copies \(U_1,U_2,U_3\), direct convolution at the target \(4\) yields
\[
\Pr(U_1+U_2+U_3=4)=3\alpha^2(1-\alpha).
\]
The difference between these two attained expressions is \(\alpha(5\alpha-2)(2\alpha-1)\), showing which construction dominates on each subinterval. They meet at the interior boundary \(\alpha=2/5\). This proves optimality and completes the theorem. \(\square\)

## Verification

The self-contained script `check_concentration.py` uses integer arithmetic only. It exhaustively optimizes the third extreme law against every pair of extreme three-site laws with sites in \(\{0,\ldots,7\}\), for seven rational atom caps on both sides of the transition. Its exact finite-bound assertions passed for \(197568\) pair instances; it separately verified \(81\) instances of the heavy-set incompatibility on equal-spaced progressions. Exact polynomial identities and attainable configurations were checked analytically in Step 5. These **finite** checks are corroboration: the unrestricted theorem follows from Steps 1–5, not finite enumeration.

Reproduce with Python 3 using `python check_concentration.py` from the directory containing that standalone file. No nonstandard packages or external data are needed.

## Relationship to prior work

Kurauskas (2026), arXiv:2603.11043, states the exact signed-extremizer assertion as Conjecture 1.3 and establishes an **asymptotic** version under a large-variance condition; it explicitly identifies earlier exact ranges \(\alpha^{-1}\in[1,2]\cup\mathbb N\). For \(\alpha\in(1/3,1/2)\), the present finite-\(n\) regime has \(\alpha^{-1}\in(2,3)\) and is not one of those ranges. The 2026 article's arguments for large variance do not yield this exact three-summand formula.

Juškevičius and Kurauskas (2020/2021), arXiv:1912.08770, prove a sharp bound for **even** numbers of summands under common atom caps, and the known uniform inverse-integer endpoints; their odd-summand open-problem discussion does not establish this three-summand interior. Madiman, Wang and Woo (2017/2019), arXiv:1712.00913, establish convolution majorization for \(\#\)-log-concave laws. A general extreme law with light mass between two heavy masses is not \(\#\)-log-concave; that theorem does not on its own imply (5) for **all** admissible laws. The interval-concentration inequality of Juškevičius (2024) is a different concentration functional, as the 2026 source emphasizes. The known discrete rearrangement inequalities explain the equal-atom endpoints but do not supply the simultaneous weighted-count obstruction in Step 3.

## Limitations

The result assumes exactly three independent integer-valued summands, a common cap, and \(1/3\leq\alpha\leq1/2\). It gives the sharp maximal point mass but does **not** classify all equality cases, heterogeneous caps, or longer odd sums. An equivalent unindexed result could exist; searching titles, aliases, published records and primary mathematical implications cannot establish priority conclusively. Computational evidence is finite; no independent external audit has been performed.

## References

1. V. Kurauskas, *An asymptotically optimal bound for the concentration function of a sum of independent integer random variables*, arXiv:2603.11043 (first public 11 March 2026), https://arxiv.org/abs/2603.11043 , especially Introduction, Conjecture 1.3, and Theorem 2.27.
2. T. Juškevičius and V. Kurauskas, *On Littlewood–Offord theory for arbitrary distributions*, arXiv:1912.08770 (first public 18 December 2019), https://arxiv.org/abs/1912.08770 , Theorem 1 and Sections 3 and 5; published as *On the Littlewood–Offord problem for arbitrary distributions*, Random Structures & Algorithms 58 (2021), 370–380.
3. M. Madiman, L. Wang and J. O. Woo, *Majorization and Rényi Entropy Inequalities via Sperner Theory*, arXiv:1712.00913, https://arxiv.org/abs/1712.00913 , Definition 1.2 and Theorem 1.4; Discrete Mathematics 342 (2019), 2911–2923.
4. T. Juškevičius, *The sharp form of the Kolmogorov–Rogozin inequality and a conjecture of Leader–Radcliffe*, Bulletin of the London Mathematical Society 56 (2024), 3289–3299, https://doi.org/10.1112/blms.13132 .

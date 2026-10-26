# Sharp asymptotic variation amplification on complete bipartite graphs

## Finding

For every pair of integers \(2\le a\le b\), let \(K_{a,b}\) be the unweighted complete bipartite graph. Let \(\mathcal M\) be the centered Hardy–Littlewood maximal operator formed from uniform averages on graph-distance balls, and \(\operatorname{Var}_G f=\sum_{\{u,v\}\in E(G)}|f(u)-f(v)|\). Define
\[
C_{a,b}=\sup_{\operatorname{Var}_G(f)>0}\frac{\operatorname{Var}_G(\mathcal Mf)}{\operatorname{Var}_G(f)}.
\]
Then the following explicit two-sided bounds hold for **every** \(2\le a\le b\):
\[
\boxed{2-\frac{3}{a+1}-\frac{a-1}{a+b}\ \le C_{a,b}\le\ 1+\frac{ab}{(a+1)(a+b)}<2.}
\]
The difference between the displayed upper and lower bounds is exactly
\[
\frac{2(a+b)-1}{(a+1)(a+b)}<\frac2{a+1}.
\]
Both bounds therefore determine the **sharp joint asymptotic constant**, uniformly in relative community size:
\[
\boxed{C_{a,b}=2-\frac{a}{a+b}+O\!\left(\frac1a\right),\qquad a\to\infty,\ b\ge a.}
\]
Equivalently, if \(a_k,b_k\to\infty\) and \(a_k/(a_k+b_k)\to\rho\in[0,1]\), then \(C_{a_k,b_k}\to1+\max\{\rho,1-\rho\}\). In particular, the balanced-family limit is \(3/2\); when one part is negligible relative to the other but both grow, the limit is \(2\). Thus \(\sup_{a,b\ge2}C_{a,b}=2\), but no individual graph reaches that supremum. Already \(K_{4,4}\) admits \(\operatorname{Var}_G(\mathcal Mf)/\operatorname{Var}_G(f)=41/40>1\).

These are sharp **limits** of the actual operator constants; the theorem does **not** assert that either finite-size bound is the exact finite-size optimum.

## Assumptions and scope

All vertices have counting measure, all edges unit length, and all graph-distance balls include the center. There are precisely three distinct radii: \(0\), \(1\), \(2\). Functions are arbitrary real-valued vertex functions; \(\mathcal M\) averages their absolute values. The variation is the sum over unoriented cross-part edges (not twice that sum), and is a seminorm annihilating constants. The source population sizes satisfy \(a,b\ge2\). The relevant research object is graph total-variation regularity of a nonlinear maximal operator, rather than a graph \(L^p\)-operator norm.

## Proof

**Reduction to nonnegative data.** Replacing \(f\) by \(|f|\) leaves \(\mathcal Mf\) unchanged and cannot increase edge variation. Write \(f\ge0\) as \(x_1,\ldots,x_a\) on the first part and \(y_1,\ldots,y_b\) on the second. Put
\[
\alpha=\frac1a\sum_i x_i,\qquad \beta=\frac1b\sum_jy_j,\qquad \mu=\frac{a\alpha+b\beta}{a+b}.
\]
The three balls give the exact formulas
\[
\mathcal Mf(x_i)=\max\left\{x_i,\frac{x_i+b\beta}{b+1},\mu\right\},\quad
\mathcal Mf(y_j)=\max\left\{y_j,\frac{y_j+a\alpha}{a+1},\mu\right\}.
\]

**Upper bound.** Suppose first that \(\alpha\ge\beta\). Then \(\beta\le\mu\le\alpha\), and the first formula reduces to \(\mathcal Mf(x_i)=T(x_i)\), where \(T(s)=\max\{s,\mu\}\). Define \(e_j=\mathcal Mf(y_j)-T(y_j)\). For \(y_j\le\mu\) and \(y_j\ge\mu\) separately, the second formula gives
\[
0\le e_j\le\frac{a}{a+1}(\alpha-\mu)
=\frac{ab}{(a+1)(a+b)}(\alpha-\beta).
\]
Since \(T\) is one-Lipschitz, for every cross-part edge
\[
|\mathcal Mf(x_i)-\mathcal Mf(y_j)|
\le|x_i-y_j|+e_j.
\]
Summing over all \(ab\) edges and using the triangle/Jensen inequality
\[
\operatorname{Var}_G(f)=\sum_{i,j}|x_i-y_j|\ge ab|\alpha-\beta|
\]
yields
\[
\operatorname{Var}_G(\mathcal Mf)
\le\left(1+\frac{ab}{(a+1)(a+b)}\right)\operatorname{Var}_G(f).
\]
If \(\beta\ge\alpha\), exchange the two parts: the same reasoning gives \(1+ab/((b+1)(a+b))\). Taking the weaker of these estimates and using \(a\le b\) establishes the stated upper bound. Since \(ab/((a+1)(a+b))<1\), it is strictly below \(2\).

**Lower bound.** On the smaller part choose a marked vertex \(x_1\), set \(f(x_1)=1\), and set \(f=0\) elsewhere. Then \(\operatorname{Var}_G(f)=b\), while the maximal function takes values \(1\) at \(x_1\), \(1/(a+b)\) at all other first-part vertices, and \(1/(a+1)\) on the second part. Consequently
\[
\frac{\operatorname{Var}_G(\mathcal Mf)}{\operatorname{Var}_G(f)}
=\left(1-\frac1{a+1}\right)
 +(a-1)\left(\frac1{a+1}-\frac1{a+b}\right)
=2-\frac3{a+1}-\frac{a-1}{a+b}.
\]
Elementary subtraction gives the claimed precise upper–lower gap.

**Joint asymptotics and optimal limiting value.** The upper bound equals \(2-a/(a+b)-b/((a+1)(a+b))\); the lower bound equals \(2-a/(a+b)+1/(a+b)-3/(a+1)\). They differ from \(2-a/(a+b)\) by at most \(3/(a+1)\), uniformly in \(b\ge a\). Taking either fixed positive fraction or a vanishing smaller-part fraction proves every claimed joint limit. Since the finite upper bound is always below \(2\) while a sequence with \(a\to\infty\) and \(b/a\to\infty\) has lower bound tending to \(2\), the global supremum is \(2\) and is not attained. For \(a=b=4\), the point-mass value is \(2-3/5-3/8=41/40\).

## Verification

An independent standard-library Python script, `check.py`, constructs the three-ball maximal values using rational arithmetic and checks the analytic pointwise intermediate inequalities, variation bound, explicit point-mass ratio, and upper–lower gap. It exhaustively tests ternary-valued functions on several graphs through \(K_{4,4}\), and additionally samples deterministic rational-valued vectors for larger and more unbalanced graphs. At package creation the script completed 126102 exact-rational assertions and checks. The universal result is proved in the preceding paragraphs; finite tests alone are not used as an infinite proof.

## Relationship to prior work

Bober–Carneiro–Hughes–Pierce (2010; arXiv:1005.3030) established seminal discrete one-dimensional variation estimates. Soria–Tradacete (2014; arXiv:1410.6204) studied finite-graph maximal operators but principally their \(\ell^p\) and weak-type norms, not the variation ratio here. González-Riquelme–Madrid (arXiv:2005.03146 and arXiv:2011.02630) studied sharp maximal variation on complete graphs and stars. González-Riquelme–Kovač–Madrid (arXiv:2603.12462) determined the complete-graph constants, examined all connected graphs with at most five vertices, and constructed finite graphs with arbitrarily large variational constants. Their examined statements do not imply uniform boundedness or this sharp joint asymptotic law specifically on large complete bipartite graphs.

## Limitations

The exact optimum for each fixed pair \((a,b)\) is **not** determined; only explicit bounds and their shared sharp joint asymptotic are proved. The order of convergence requires the smaller population size to grow. There is no claim about fixed-small-part limits, graph types beyond complete bipartite graphs, or nonlinear Sobolev regularity on general graphs. A relevant Liu–Xue (2021) primary article on finite-graph maximal variation could not be inspected in full; equivalent prior coverage under graph-variation terminology remains a historical-priority risk. The proof and arithmetic tests are not a substitute for independent mathematical review.

## References

1. J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030 (first submitted 2010-05-17). https://arxiv.org/abs/1005.3030
2. J. Soria, P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first submitted 2014-10-22). https://arxiv.org/abs/1410.6204
3. C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146. https://arxiv.org/abs/2005.03146
4. C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630. https://arxiv.org/abs/2011.02630
5. C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462. https://arxiv.org/abs/2603.12462
6. F. Liu, Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, DOI:10.1007/s13348-020-00290-6 (2021). https://doi.org/10.1007/s13348-020-00290-6

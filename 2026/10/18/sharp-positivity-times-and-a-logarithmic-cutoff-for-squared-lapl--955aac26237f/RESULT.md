# Sharp positivity times and a logarithmic cutoff for squared-Laplacian heat on Boolean cubes

## Finding
Let \(Q_d\) be the Boolean \(d\)-cube, \(d\ge2\), with its unnormalized graph Laplacian \(L_d\). For \(t\ge0\) let \(T_d(t)=\exp(-tL_d^2)\), acting on real functions on the cube. There is exactly one number \(\tau_d>0\) such that
\[
T_d(t)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad t=0\ \text{or}\ t\ge\tau_d.
\]
The thresholds satisfy \(0<\tau_2<\tau_3<\cdots\) and \(\tau_d<\tfrac14\log d\). For \(d\ge3\), \(\tau_d\) is the **largest** positive-time zero of the *antipodal* kernel (and its only zero after \(\tau_{d-1}\)); \(\tau_2\) is the unique positive-time zero. Equivalently each recovery time solves
\[
\sum_{j=0}^d(-1)^j\binom dj\exp(-4t j^2)=0.
\]
At \(t=\tau_d\) exactly the antipodal matrix entries vanish and all other entries are strictly positive. Every matrix entry is strictly positive at \(t>\tau_d\). Moreover,
\[
\boxed{\displaystyle\tau_d=\frac{\log d}{4}-\frac{1}{8d^2}+\frac{1}{8d^3}+O(d^{-4})}\qquad(d\to\infty).
\]
Since every row of \(T_d(t)\) sums to one, its sharp maximum-norm amplification is \(1\) precisely at these positivity times and is strictly greater than \(1\) for \(0<t<\tau_d\). In particular, the transition occurs on a logarithmic rather than a dimension-independent time scale. The \(d=2\) case is included as the induction base, not claimed as a new independent result.

## Assumptions and scope
The vertices of \(Q_d\) are \(\{0,1\}^d\), adjacent exactly when they differ in one coordinate; each edge has weight one. Thus \((L_df)(x)=\sum_{i=1}^d(f(x)-f(x\oplus e_i))\), where \(\oplus\) denotes coordinatewise addition modulo two. We use the ordinary real coordinate order and \(\ell^\infty\) norm. The assertion concerns *operator positivity at each time*, not eventual positivity of one initial vector. For vertices at Hamming distance \(k\), write \(h_{d,k}(t)\) for their common matrix entry. The convention is \(0\le k\le d\); binomial coefficients outside their natural range vanish. All bounds and equalities use this exact, unnormalized Laplacian.

## Proof
**1. Exact Fourier kernel and two dimension identities.** For \(A\subseteq[d]\) the Walsh character \(\chi_A(x)=(-1)^{\sum_{i\in A}x_i}\) is an eigenfunction of \(L_d\) with eigenvalue \(2|A|\). Therefore
\[
h_{d,k}(t)=2^{-d}\sum_{j=0}^d C_{d,k,j}z^{j^2},\quad z=e^{-4t},\quad
C_{d,k,j}=\sum_{a=0}^j(-1)^a\binom ka\binom{d-k}{j-a}.
\]
In particular \(2^dh_{d,d}(t)=p_d(z):=\sum_{j=0}^d(-1)^j\binom dj z^{j^2}\). Splitting Walsh characters according to whether they contain the last coordinate gives, for \(0\le k<d\),
\[
h_{d,k}(t)+h_{d,k+1}(t)=h_{d-1,k}(t),\qquad
h_{d,k}(t)-h_{d,k+1}(t)
=z\,[T_{d-1}(t)e^{-4tL_{d-1}}]_{0,x_k},
\]
where \(x_k\) is any vertex at distance \(k\) from \(0\) in \(Q_{d-1}\). The first identity is also exactly the one-coordinate marginalization of the kernel. Ordinary graph heat \(e^{-4tL_{d-1}}\) has strictly positive entries for \(t>0\): writing \(L_{d-1}=(d-1)I-A\) reduces this to the matrix exponential of the nonnegative connected adjacency matrix. Consequently, whenever \(t>0\) and \(T_{d-1}(t)\) is entrywise nonnegative, all the second-identity differences are *strictly positive*, because \(T_{d-1}(t)\) has nonnegative rows summing to one.

**2. A quantitative necessary condition for positive kernels.** Suppose \(d=m\ge3\), \(t>0\), and \(T_m(t)\) is entrywise nonnegative. Its row from the origin defines a probability distribution on \(\{0,1\}^m\). Let \(Y_i=(-1)^{X_i}\), where \(X\) has this distribution, so the Walsh spectrum gives \(\mathbb E Y_i=z\) and \(\mathbb E(Y_iY_j)=z^4\) for distinct \(i,j\). Then
\[
0\le\operatorname{Var}\Bigl(\sum_iY_i\Bigr)
=m(1-z^2)\bigl(1-(m-1)z^2\bigr).
\]
As \(0<z<1\), this implies \(z^2\le1/(m-1)\), or
\[
t\ge\tfrac18\log(m-1). \tag{1}
\]
This is only a necessary bound, used to control a derivative; it is not asserted to be the sharp positivity cutoff.

**3. Base cases.** For \(d=2\), \(p_2(z)=1-2z+z^4=(z-1)(z^3+z^2+z-1)\). The cubic is strictly increasing on \((0,1)\), with a unique zero \(a\) there, so the only nonzero recovery time is \(\tau_2=-\tfrac14\log a\). The remaining distances are positive at all \(t>0\): directly, \(h_{2,0}=(1+2z+z^4)/4\) and \(h_{2,1}=(1-z^4)/4\). At \(t=1/8\), \(3/5<z=e^{-1/2}<2/3\) and \(p_2(z)<p_2(3/5)=-44/625<0\), so \(\tau_2>1/8\). The implication that positivity excludes negative antipodal entries holds for all times by this explicit formula.

For \(d=3\), the induction below already applies because \(4e^{-12\tau_2}<4e^{-3/2}<1\). After establishing existence and uniqueness of \(\tau_3\) by that step, note that at \(t=1/4\), with \(4/11<z=e^{-1}<10/27\),
\[
p_3(z)=1-3z+3z^4-z^9<1-12/11+3(10/27)^4<0.
\]
Thus \(\tau_3>1/4\). The elementary displayed exponential bounds follow, for example, by truncating the positive Taylor series for \(e\) and bounding its geometric remainder; no numerical root estimate enters the proof.

**4. Strict increase and unique recovery in all dimensions.** Inductively assume that \(T_{d-1}\) is entrywise nonnegative exactly at zero or at and after its positive cutoff \(\tau_{d-1}\), and that its antipodal entry vanishes at that cutoff. For every \(0<t<\tau_{d-1}\), the first identity in step 1 shows that positivity of \(T_d(t)\) would imply positivity of \(T_{d-1}(t)\), a contradiction. At \(t=\tau_{d-1}\), all the differences in step 1 are strictly positive, and, applying both identities at \(k=d-1\),
\[
h_{d,d}(\tau_{d-1})
=\tfrac12\bigl(h_{d-1,d-1}(\tau_{d-1})
-[h_{d,d-1}(\tau_{d-1})-h_{d,d}(\tau_{d-1})]\bigr)<0.
\]
For \(t\ge\tau_{d-1}\), the radial entries \(h_{d,k}(t)\) decrease *strictly* with \(k\). Hence entrywise positivity is equivalent to nonnegativity of just \(h_{d,d}(t)\).

To show this last entry crosses zero exactly once, set \(A_j=j^2\binom dj z^{j^2}\) for \(1\le j\le d\). Then
\[
\frac{d}{dt}p_d(e^{-4t})=4(A_1-A_2+A_3-\cdots),\qquad
\frac{A_{j+1}}{A_j}=\frac{(d-j)(j+1)}{j^2}z^{2j+1}\le2(d-1)z^3.
\]
For \(d=3\), the latter upper bound is less than one for \(t\ge\tau_2>1/8\). For \(4\le d\le7\), it is less than one for \(t\ge\tau_{d-1}\ge\tau_3>1/4\), since \(2(d-1)e^{-3}\le12e^{-3}<1\). For \(d\ge8\), applying (1) at \(m=d-1\) and \(t=\tau_{d-1}\) gives
\[
2(d-1)z^3\le\frac{2(d-1)}{(d-2)^{3/2}}<1.
\]
(The last strict inequality holds at \(d=8\) and its left side decreases thereafter.) Thus in every induction step \(A_1>A_2>\cdots>A_d>0\) on the entire interval \([\tau_{d-1},\infty)\). The alternating sum above is strictly positive, proving that \(h_{d,d}(t)\) increases strictly there. It begins negative and converges to \(2^{-d}>0\), so it crosses zero once, at \(\tau_d>\tau_{d-1}\). At that time all other distances are strictly positive by the radial difference identity; afterwards every entry is strictly positive. This closes the induction and excludes all earlier positive times.

**5. Sharp logarithmic asymptotics.** At \(t_0=(\log d)/4\), we have \(z=1/d\) and the first two terms in \(p_d\) cancel. The remaining alternating tail, starting with \(+\binom d2d^{-4}\), is strictly positive because its magnitudes strictly decrease. Therefore \(\tau_d<t_0\): for \(d\ge3\), the induction gives \(\tau_{d-1}<(\log(d-1))/4<t_0\) and the antipodal entry is increasing on that interval, while \(d=2\) follows directly.

For a matching lower bracket, set \(t_-=t_0-d^{-2}\) and \(z_-=d^{-1}e^{4/d^2}\). For large \(d\), \(1-dz_-=-4d^{-2}+O(d^{-4})\), the \(j=2\) contribution is \(\frac12d^{-2}+O(d^{-3})\), and the sum of all \(j\ge3\) contributions is \(O(d^{-6})\). The last assertion follows uniformly for \(z\le2/d\) from \(j^2\ge9+7(j-3)\) for \(j\ge3\) and the binomial bound \(\binom dj\le d^j/j!\). For all sufficiently large \(d\), \(t_->\tfrac14\log(d-1)>\tau_{d-1}\), because \(\tfrac14\log(d/(d-1))>d^{-2}\). Thus the strict antipodal monotonicity established in step 4 applies to this bracket. Hence \(p_d(z_-)<0\) and \(t_-<\tau_d<t_0\) for all sufficiently large \(d\), giving \(\tau_d=t_0+O(d^{-2})\). At the unique root, \(z=d^{-1}(1+O(d^{-2}))\), and the root identity refines to
\[
dz=1+\binom d2z^4+O(d^{-6})
=1+\frac{1}{2d^2}-\frac{1}{2d^3}+O(d^{-4}).
\]
Taking \(-\frac14\log z\) gives the asserted three-term expansion.

**6. Norm criterion.** The constant vector is fixed by \(T_d(t)\) because \(L_d\mathbf 1=0\); thus every row sums to one. Its exact \(\ell^\infty\)-operator norm is the maximum absolute row sum. An entrywise nonnegative row has absolute sum one; any negative entry makes its absolute sum strictly greater than one. This establishes the sharp norm criterion.

## Verification
The standalone script `hypercube_biharmonic_checker.py` uses only Python's standard library. It independently compares the Krawtchouk-grouped formula with an ungrouped Walsh sum using exact rational arithmetic, brackets positive antipodal zeros at high decimal precision, checks strict distance ordering and monotone thresholds in finite dimensions, and tests the quantitative asymptotic remainder. Its recorded run passed 1,936 finite checks. The proof above, including the variance inequality, uniform alternating-series dominance, and asymptotic remainder bound, supplies the infinite-dimensional-index conclusions; no finite test is treated as an exhaustive proof.

## Relationship to prior work
Daners, Glück and Kennedy [1,2] establish qualitative spectral criteria and examples for eventually positive semigroups, including fourth-order generators; their theorems do not calculate this Boolean-cube kernel, its antipodal minimizer, or its sharp dimensional threshold. Gazzola and Grunau [3] prove eventual **local** positivity for continuum biharmonic heat while global positivity may fail; their setting is not a finite hypercube. A published three-spectral-value positivity-time theorem [4] yields a no-gap conclusion for operators with at most three distinct spectral values. The generator here has \(d+1\) distinct spectral values, so that theorem does not imply the no-gap conclusion for \(d\ge3\). The antipodal entry can have earlier positive-time zeros in dimensions at least four; the theorem asserts the final crossing, not uniqueness of antipodal zeros at all positive times. The two-dimensional cube is also a complete bipartite graph and its finite exact cutoff is already encompassed by known complete-multipartite squared-Laplacian calculations; the new assertion is the uniform higher-cube single-cutoff theorem and its sharp asymptotic expansion. The known ordinary graph heat semigroup is a distinct, positive semigroup and gives no corresponding result for the square of the graph Laplacian.

## Limitations
The result is restricted to the unit-edge Boolean hypercube, the squared unnormalized Laplacian, and the coordinatewise positive cone. Before the previous-dimension recovery time, the antipodal entry need not be monotone or of one sign; in fact for \(d=4\), \(p_4(e^{-4t})=192t^2+O(t^3)>0\) at sufficiently small positive times, but is negative at \(t=\tau_3\), proving there is an earlier positive-time zero. The final-crossing characterization is not a claim of global uniqueness of its positive-time zeros. It does not establish analogous monotonicity for arbitrary vertex-transitive graphs, weighted cubes, resolvent families, or general spectral functions. Novelty comparisons are based on inspected primary texts, bibliographic queries, and accessible mathematical records; an earlier equivalent presentation in radial positive-definite Fourier multiplier language remains possible. Independent scientific or historical-priority validation has not been performed.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294 (first public version 2015-11-17), https://arxiv.org/abs/1511.05294 .

[2] D. Daners, J. Glück, J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020 (2015), https://arxiv.org/abs/1511.09020 .

[3] F. Gazzola, H.-C. Grunau, *Eventual local positivity for a biharmonic heat equation in \(\mathbb R^n\)*, Discrete Contin. Dyn. Syst. Ser. S 1 (2008), 83–87; https://gazzola.faculty.polimi.it/ggpoitiers.pdf .

[4] *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups*, published mathematical record (2026), identifier `2026/10/11/SCOPE-a-three-spectral-value-barrier-for-gaps-in-positivity-times-of-s--da21753d4271`.

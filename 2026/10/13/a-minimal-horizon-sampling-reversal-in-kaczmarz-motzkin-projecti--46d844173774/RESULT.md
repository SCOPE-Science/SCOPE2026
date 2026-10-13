# A minimal-horizon sampling reversal in Kaczmarz–Motzkin projection

## Finding

For a consistent, nonsingular, three-equation linear system with equally normalized rows, making the random sample larger in the sampling Kaczmarz–Motzkin (SKM) method need not improve expected squared solution error after two projections. In fact, there is an explicit open interval of initial vectors for which sample size two **strictly beats both** ordinary randomized Kaczmarz (sample size one) **and** fully greedy maximal-residual Kaczmarz (sample size three), with the latter performing strictly worst.

Put
\[
 B=\begin{pmatrix}3&-4&2\\3&-2&-4\\2&3&-4\end{pmatrix},\qquad
 A=B/\sqrt{29},\qquad b=0,\qquad
 x_0(t)=(-10,t,-30)^{\mathsf T}.
\]
For every real \(1/2\le t\le3/2\), run exactly two SKM projections with fresh, independently and uniformly chosen subsets of a fixed size \(\beta\in\{1,2,3\}\) at each step, with maximal **absolute** row residual used inside each subset. Write \(F_\beta(t)=\mathbb E\|x_2^{(\beta)}(t)\|_2^2\). Then
\[
\begin{aligned}
F_1(t)&=\frac{4(26103t^2-839010t+30675050)}{219501},\\
F_2(t)&=\frac{2(43707t^2-2466480t+57312850)}{219501},\\
F_3(t)&=\frac{4(2836t^2-170920t+3628725)}{24389},
\end{aligned}
\]
and the inequalities are strict:
\[
F_2(t)<F_1(t)<F_3(t).
\]
The violation occurs at the **earliest possible projection horizon**: for any initial error and any normalized consistent system, the expected squared error after one SKM step is nonincreasing in \(\beta\).

At \(t=1\) the three exact two-step risks are respectively \(119448572/219501\), \(109780154/219501\), and \(13842564/24389\).

## Assumptions and scope

The solver treats equations, not inequalities; row selection is without replacement *within* each sample, with independent sample sets across iterations. Ties, when present in other inputs, may be resolved arbitrarily; the constructed sample paths have no relevant ties throughout the stated parameter interval. All projections have unit relaxation, and errors are Euclidean. Since \(\det B=70\ne0\) and each row of \(B\) has squared norm \(29\), \(A\) is nonsingular with unit Euclidean row norms. The unique solution of \(Ax=0\) is zero, so squared iterate norm equals squared solution error.

For a row index \(i\in\{1,2,3\}\), let \(b_i\) be the corresponding integer row of \(B\), and define \(P_i=I-b_i^{\mathsf T}b_i/29\). Here the numerator denotes the column-by-row outer product. At a state \(x\), a uniform subset \(S\subseteq\{1,2,3\}\) of size \(\beta\) is chosen; select \(i\in S\) maximizing \(|b_i x|\) and update \(x\leftarrow P_i x\). Using \(B\), instead of \(A\), to compare residual magnitudes is legitimate because every residual has the same positive scale \(1/\sqrt{29}\).

## Proof

First, the projection identity gives \(\|P_i x\|_2^2=\|x\|_2^2-(b_i x)^2/29\). If \(\beta\) increases by one, one can couple its uniform random subset to the smaller uniform subset by taking the first \(\beta\) and first \(\beta+1\) positions of the same uniform random permutation of the three row indices. The maximum squared residual is nondecreasing under that inclusion. Thus the expected first-step squared error is nonincreasing in sample size for **every** normalized consistent system, proving minimality of the two-step horizon.

To calculate two steps, write \(r_i(x)=b_i x\) and enumerate the \(\binom3\beta^2\) equally likely, ordered pairs of sampling subsets. The initial unnormalized residuals are
\[
(r_1,r_2,r_3)=(-90-4t,\ 90-2t,\ 100+3t).
\]
For \(\beta=2\), the first subset choices \(\{1,2\},\{1,3\},\{2,3\}\) select respectively rows \(1,3,3\). After projecting onto row one, the residuals are
\[
(r_1,r_2,r_3)=\tfrac1{29}(0,3420-22t,1640+31t),
\]
so those three second-subset choices select respectively rows \(2,3,2\). After projecting onto row three, they are
\[
(r_1,r_2,r_3)=\tfrac1{29}(-1210-74t,1010-106t,0),
\]
so the three second-subset choices select respectively rows \(1,1,2\). For \(\beta=3\) both full-subset choices deterministically pick rows \(3,1\). For \(\beta=1\), each of the nine pairs of singleton subsets occurs with probability \(1/9\), regardless of residual size. The above selections are strict for the whole stated interval; the absolute-affine comparisons may be checked at endpoints, or by the strictly positive squared-residual margin quadratics reconstructed by the standalone checker.

In particular the complete second-step expectations equal
\[
 F_1(t)=\frac19\sum_{i,j=1}^{3}\|P_jP_i x_0(t)\|_2^2,\qquad
 F_2(t)=\frac19\sum_{S,T\in\binom{\{1,2,3\}}2}\|P_{j(T,P_{i(S,x_0)}x_0)}P_{i(S,x_0)}x_0\|_2^2,
\]
where \(i(S,x)\) means the row of \(S\) having largest absolute \(b_i x\), and \(j(T,y)\) is the analogous choice for the second sample. The full greedy risk is \(F_3(t)=\|P_1P_3x_0(t)\|_2^2\). Multiplying these explicit rational projectors yields the three quadratic formulas in the Finding section. No limiting argument or numerical approximation is used.

Finally the differences factor into
\[
F_1(t)-F_2(t)=\frac{2(2833t^2+262820t+1345750)}{73167}>0,
\]
\[
F_3(t)-F_1(t)=\frac{4(1983475-699270t-579t^2)}{219501}>0.
\]
The first numerator is positive for positive \(t\). The second is strictly decreasing on the displayed nonnegative interval, and at \(t=3/2\) it remains positive. These inequalities prove the claimed strict ordering on the entire interval. By continuity and strictness they also persist for sufficiently small perturbations of \(t\) within the real line; no tie convention is needed.

## Verification

Run `python3 verify.py` with the Python standard library. It checks \(\det B=70\), squared row norms \(29\), all strict residual-comparison margins over the **entire** parameter interval (including interior quadratic extrema), reconstructs every one of the \(9+9+1\) ordered sample paths as rational affine iterates, checks all three expected-error polynomial coefficients, and verifies that both difference polynomials remain positive over the full interval. The calculations use exact rational arithmetic; finite-grid experiments are neither needed nor used as proof.

## Relationship to prior work

Haddock and Ma [1] specify the identical random-subset-then-maximum-absolute-residual SKM rule for equations, derive convergence-rate improvements from sample size, and distinguish its two endpoint rules; their displayed bounds are upper estimates, not a theorem that the **actual** expected squared error is ordered by sample size at every multi-step horizon. Nutini and collaborators [2] derive one-step progress and orthogonality-graph multi-step *bounds* for greedy Kaczmarz, rather than the exact three-way sample-size comparison for the matrix here. De Loera, Haddock, and Needell [3] introduced the random-sampling Motzkin combination primarily for inequalities and analyze worst-case guarantees and running-cost tradeoffs, rather than the displayed strict two-projection equality-system reversal. These statements are compared by their hypotheses and conclusions, not merely by title or matching vocabulary. The presented counterexample is compatible with all three analyses.

## Limitations

This theorem is about the exact two-step expected **solution error** on the displayed three-row consistent family. It does not assert an asymptotic rate reversal, superior computation time at sample size two, a general optimal sampling policy, or analogous behavior for every starting vector. The finding also does not imply a violation of conditional one-step descent, which holds. An exhaustive priority guarantee over unpublished or unindexed work is unavailable.

## References

1. J. Haddock and A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz–Motzkin*, arXiv:1912.03544 (first version 2019-12-07), https://arxiv.org/abs/1912.03544; in particular the algorithm and Section 2.
2. J. Nutini, M. Schmidt, B. Sepehry, H. Koepke, I. Laradji, A. Virani, *Convergence Rates for Greedy Kaczmarz Algorithms, and Faster Randomized Kaczmarz Rules Using the Orthogonality Graph*, UAI 2016, https://www.auai.org/uai2016/proceedings/papers/77.pdf, especially Sections 4 and 9.
3. J. A. De Loera, J. Haddock, and D. Needell, *A Sampling Kaczmarz–Motzkin Algorithm for Linear Feasibility*, arXiv:1605.01418, https://arxiv.org/abs/1605.01418, especially Sections 2 and 4.

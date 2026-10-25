# A dimension-sharp reshuffling reversal in Euclidean coordinate-descent risk

## Finding

Let \(H\) be a real symmetric positive-definite Hessian and let exact coordinate descent minimize \(f(x)=\tfrac12(x-x_*)^{\mathsf T}H(x-x_*)\) along the selected coordinate. Compare, over one epoch of \(n\) coordinate evaluations starting from the same deterministic point, independent uniform draws with replacement (IID) and a uniformly random permutation (RR). Expectations are over the coordinate choices, and the measured error is the squared Euclidean distance to \(x_*\), not the function value.

**Two-coordinate identity.** For every \(H=\begin{psmallmatrix}a&c\\c&b\end{psmallmatrix}\succ0\), every initial error \(e=x_0-x_*\), and both equal-cost schemes of two evaluations,
\[
\mathbb E_{\mathrm{IID}}\|e_2\|_2^2-\mathbb E_{\mathrm{RR}}\|e_2\|_2^2
=\frac14\left(1-\frac{c^4}{a^2b^2}\right)\|e\|_2^2>0
\qquad(e\ne0).
\]
Thus RR has the strictly smaller expected squared Euclidean error for every nonzero start on every two-coordinate strictly convex quadratic. The gap is isotropic despite unequal diagonal curvatures.

**Three-coordinate reversal with opposite objective ordering.** In dimension three, take
\[
H=\begin{pmatrix}1&3/4&1/4\\3/4&1&3/4\\1/4&3/4&1\end{pmatrix},\qquad x_*=0,\qquad e=(0,1,0)^{\mathsf T}.
\]
The matrix is positive definite, yet exhaustive exact evaluation of the \(6\) RR and \(27\) IID paths gives
\[
\begin{aligned}
\mathbb E_{\mathrm{RR}}\|e_3\|_2^2&=\frac{1899}{2048},&
\mathbb E_{\mathrm{IID}}\|e_3\|_2^2&=\frac{12331}{13824},\\
\mathbb E_{\mathrm{RR}}\|e_3\|_2^2-\mathbb E_{\mathrm{IID}}\|e_3\|_2^2&=\frac{1949}{55296}>0.
\end{aligned}
\]
At the same time, RR has **smaller** expected squared Hessian-energy norm on exactly the same example:
\[
\begin{aligned}
\mathbb E_{\mathrm{RR}}(e_3^{\mathsf T}He_3)&=\frac{213}{2048},&
\mathbb E_{\mathrm{IID}}(e_3^{\mathsf T}He_3)&=\frac{1765}{13824},\\
\mathbb E_{\mathrm{RR}}(e_3^{\mathsf T}He_3)-\mathbb E_{\mathrm{IID}}(e_3^{\mathsf T}He_3)&=-\frac{1309}{55296}<0.
\end{aligned}
\]
For \(n=1\), the two samplers coincide. Consequently, three coordinates are the smallest dimension in which one-epoch RR can have *larger expected Euclidean squared solution error* than IID coordinate descent on a strictly convex quadratic.

## Assumptions and scope

The Hessian is real symmetric positive definite and the coordinate update uses the **exact minimizing step**, with no momentum, noise, relaxation, approximate solves, or coordinate importance weights. Every scheme starts at the identical deterministic \(x_0\); the RR epoch samples each of \(n\) coordinates exactly once in uniform random order; IID independently samples uniformly from \(\{1,\dots,n\}\) on each of the same \(n\) evaluations. The coordinate update is
\[
e\longmapsto T_i e,\qquad
T_i=I-\frac{e_ie_i^{\mathsf T}H}{H_{ii}},
\]
where \(e_i\) in the formula denotes the \(i\)-th standard basis vector; elsewhere \(e\) denotes the error. For a sampled path \((i_1,\ldots,i_n)\), the terminal error is \(T_{i_n}\cdots T_{i_1}e\). No claim is made about arbitrary numbers of epochs or about norm-uniform ordering in dimensions above three.

## Proof

**Two coordinates.** Write \(q=c^2/(ab)\in[0,1)\). The one-coordinate error maps are idempotent and have the exact forms
\[
T_1=\begin{pmatrix}0&-c/a\\0&1\end{pmatrix},\qquad
T_2=\begin{pmatrix}1&0\\-c/b&0\end{pmatrix},
\qquad T_i^2=T_i.
\]
The four equally likely IID paths have maps \(T_1\), \(T_2\), \(T_2T_1\), and \(T_1T_2\); the two equally likely RR paths have the last two maps. Direct multiplication gives the expected Euclidean Gram operators
\[
\begin{aligned}
G_{\mathrm{RR}}&=\frac12\operatorname{diag}\!\left(q^2+\frac{c^2}{b^2},\ q^2+\frac{c^2}{a^2}\right),\\
G_{\mathrm{IID}}&=\frac14\operatorname{diag}\!\left(1+q^2+\frac{2c^2}{b^2},\ 1+q^2+\frac{2c^2}{a^2}\right).
\end{aligned}
\]
Subtracting yields \(G_{\mathrm{IID}}-G_{\mathrm{RR}}=(1-q^2)I/4\), and positive definiteness gives \(q<1\). Applying this identity to every error \(e\) proves the stated universal strict comparison.

**Three coordinates.** The leading principal minors of the displayed rational Hessian are \(1\), \(7/16\), and \(3/32\), so Sylvester's criterion proves positive definiteness. Because its diagonal is \(1\), the three error maps simplify to \(T_i=I-e_ie_i^{\mathsf T}H\). For an initial error \((0,1,0)^{\mathsf T}\), choosing coordinate two first gives zero error; the first choices one and three are symmetric under reflection. Exhaustively multiply the remaining maps, retaining all terms with exact rational arithmetic. When the first coordinate is one, the sums of the squared Euclidean terminal norms over the two RR completions and nine IID completions are, respectively,
\[
\frac{5697}{2048}\qquad\text{and}\qquad\frac{12331}{1024}.
\]
The sums of the terminal \(H\)-energy norms over the same completions are, respectively,
\[
\frac{639}{2048}\qquad\text{and}\qquad\frac{1765}{1024}.
\]
The identical four totals hold when the first chosen coordinate is three; all totals vanish when it is two. Divide the combined RR sums by \(3!=6\) and the IID sums by \(3^3=27\) to obtain the four asserted exact expected values. Their differences reduce to \(1949/55296\) and \(-1309/55296\), proving simultaneous Euclidean worsening and objective improvement. Finally, a single coordinate is visited with certainty when \(n=1\), and the two-coordinate identity excludes reversals for \(n=2\); hence the counterexample dimension is minimal.

## Verification

The standalone `verify.py` rederives the generic two-coordinate Gram identity symbolically, checks all three Sylvester minors, and enumerates every \(6\) RR and \(27\) IID three-coordinate path using rational arithmetic. It asserts the grouped sums, four exact expected norms, and both strict rational inequalities. Run `python verify.py` in an environment with SymPy installed; the script prints `PASS` only after all assertions succeed. This verification is reproducible finite arithmetic; the dimension-two universal assertion is independently proved above by an exact identity valid for arbitrary positive-definite input.

## Relationship to prior work

Gürbüzbalaban, Ozdaglar, Vanli and Wright [1] formalize RR/RPCD and independent RCD for exact coordinate descent and compare several convergence criteria. Their quantitative RR advantage applies to a specialized diagonally dominant Hessian family and yields rate bounds; it does not state this all-Hessian exact two-coordinate Euclidean identity or the three-coordinate Euclidean/objective reversal. Lee and Wright [2] analyze a distinct special Hessian family and asymptotic/objective convergence. Oswald and Zhou [3] prove randomized SOR energy-seminorm bounds, not an all-start exact Euclidean one-epoch ordering. Lai and Lim [4] address a noncommutative arithmetic–geometric mean inequality for **symmetric positive-semidefinite factors**; the coordinate error maps \(T_i\) here are generally nonsymmetric in the Euclidean inner product. Their statements therefore do not imply the present Euclidean Gram comparison or exclude the exhibited three-coordinate example.

Earlier two-coordinate expected-*objective* ordering results for relaxed coordinate descent do not imply an expected-*Euclidean*-error identity; these are different quadratic forms. Conversely, the three-dimensional counterexample retains improved expected objective, making the distinction substantive rather than terminological.

## Limitations

This is a one-epoch, equal-evaluation-cost comparison for exact coordinate minimization. The dimension-three construction proves existence, not a complete characterization of all reversing Hessians, nor a reversal for every higher dimension. It is not a claim about asymptotic rates, expected iterate vectors, Kaczmarz schemes with orthogonal error projections, or nonquadratic objectives. The cited literature was compared for mathematical implication, but unindexed specialized equivalents remain a publication-priority risk. No independent validation is claimed.

## References

[1] M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli, S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200 (first posted 2018-03-22); *Mathematical Programming* 181 (2020), 349–376.

[2] S. J. Wright and C.-P. Lee, *Analyzing Random Permutations for Cyclic Coordinate Descent*, arXiv:1706.00908 (first posted 2017-06-03); accessible full text arXiv:1706.00908v4.

[3] P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, arXiv:1510.04727 (2015), *Numerische Mathematik* 135 (2017), 1207–1230.

[4] Z. Lai and L.-H. Lim, *Recht–Ré Noncommutative Arithmetic-Geometric Mean Conjecture is False*, arXiv:2006.01510 (2020).

# Sharp linear Lipschitz extension to the edge midpoints of a regular simplex

## Finding

For every integer \(n\ge3\), let \(V=\{v_1,\ldots,v_n\}\) be the vertices of a regular Euclidean \((n-1)\)-simplex of side length \(1\), and put \(m_{ij}=(v_i+v_j)/2\), \(S=V\cup\{m_{ij}:i<j\}\). Give both sets the induced Euclidean metrics. Among all bounded real-linear extension operators \(E:\operatorname{Lip}(V)/\mathbb R\to\operatorname{Lip}(S)/\mathbb R\), whose restrictions recover the initial function modulo constants, the sharp norm is

\[
\Lambda_n=\inf_E\|E\|=\begin{cases}
8-4\sqrt3,&n=3,\\
\dfrac{2\sqrt2(n-1)}{n\sqrt2+n-2},&n\ge4.
\end{cases}
\]

The norm is computed using the Lipschitz seminorm, \(\operatorname{Lip}(f)=\max_{x\ne y}|f(x)-f(y)|/\|x-y\|_2\). The infimum is attained by a positive, constant-preserving, permutation-equivariant extension:

\[
(E_nf)(v_i)=f(v_i),\qquad (E_nf)(m_{ij})=a_n(f(v_i)+f(v_j))+b_n\sum_{k\ne i,j}f(v_k),
\]
\[
 t_3=6\sqrt3-10,\quad t_n=\frac{n-1}{n\sqrt2+n-2}\ (n\ge4),\qquad
 a_n=\frac{1+(n-2)t_n}{n},\quad b_n=\frac{1-2t_n}{n}.
\]

Every \(a_n,b_n\) is strictly positive. This equivariant optimizer is unique *within the permutation-equivariant family*; uniqueness among all extension operators is not asserted. The sequence \(\Lambda_n\) is strictly increasing, and \(\lim_{n\to\infty}\Lambda_n=4-2\sqrt2\). By comparison, the arithmetic edge-interpolant \(f(m_{ij})=(f(v_i)+f(v_j))/2\) has norm \(2/\sqrt3\) when \(n=3\), and \(\sqrt2\) when \(n\ge4\).

## Assumptions and scope

All quantities refer to real-valued scalar functions, Euclidean pairwise distances inherited from the ambient simplex, and **simultaneous linear** extension to all midpoints. The domain and target are finite-dimensional spaces modulo constant functions. Equivalently, one may work with real-linear maps on raw functions that preserve constants and agree with the input on the original vertices. The theorem does not minimize the Lipschitz constant separately for each input; nonlinear scalar McShane extensions need no norm increase, but are not a common linear operator. No extension to the entire continuous simplex is claimed.

## Proof

**1. Reduction to one parameter.** The permutation group on \(n\) vertices acts by isometries on both finite metric sets and on their Lipschitz seminorm spaces. Conjugating any extension by each permutation and averaging yields an extension of no greater operator norm. Choose the raw-function normalization described above. For an equivariant extension the row of coefficients at \(m_{ij}\) is constant at the two endpoints and constant at the other vertices. Denote these two coefficients by \(a,b\). Preservation of constants forces \(2a+(n-2)b=1\). Writing \(t=a-b\) gives

\[
 a=\frac{1+(n-2)t}{n},\qquad b=\frac{1-2t}{n}.
\]

Thus the global infimum is the infimum over \(t\in\mathbb R\) of the norm of this one-parameter family. Indeed, the averaging argument proves the lower bound on every original operator, while every such row with the normalization equation defines an admissible extension.

**2. Exact finite pair norm.** Every pair of distinct original vertices has distance \(1\), so \(\operatorname{Lip}_V(f)=\max_i f(v_i)-\min_i f(v_i)\). If real coefficients \(c_i\) sum to zero, then

\[
\sup_{\operatorname{Lip}_V(f)\le1}\left|\sum_i c_i f(v_i)\right|=\frac12\sum_i|c_i|.
\]

This follows by subtracting the minimum of the input and maximizing a linear functional over \([0,1]^n\); the positive-coefficient indicator attains equality. Hence each pair of target points has an exact Lipschitz operator contribution given by half the \(\ell_1\) norm of its coefficient difference, divided by its Euclidean separation.

The five geometrically possible pair types give the following exact contributions:

\[
\begin{array}{c|c|c}
\text{pair type}&\text{distance}&\text{operator contribution}\\\hline
\text{two vertices}&1&1\\
\text{vertex and incident midpoint}&1/2&I=|1-a|+|a|+(n-2)|b|\\
\text{vertex and nonincident midpoint}&\sqrt3/2&N=(|1-b|+2|a|+(n-3)|b|)/\sqrt3\\
\text{midpoints sharing a vertex}&1/2&S_0=2|t|\\
\text{disjoint midpoints}&1/\sqrt2&D_0=2\sqrt2|t|
\end{array}
\]

The last pair type exists only for \(n\ge4\). For example, the nonincident vertex-to-midpoint row has entries \(1-b,-a,-a,-b,\ldots,-b\); the disjoint-midpoint row has two entries \(t\), two entries \(-t\), and all others zero. The Euclidean distances follow from \(\|\sum_i c_i v_i\|_2^2=\frac12\sum_i c_i^2\) for any \(\sum_i c_i=0\). The resulting norm is exactly \(\max\{1,I,N,S_0,D_0\}\), with \(D_0\) omitted for \(n=3\).

**3. Lower bound for \(n\ge4\).** Independently of the signs of \(a,b,t\), the triangle inequality gives

\[
I\ge1+(n-2)b=\frac{2(n-1)-2(n-2)t}{n},\qquad D_0=2\sqrt2|t|\ge2\sqrt2 t.
\]

The maximum of these two affine lower bounds, one decreasing and one increasing in \(t\), has the minimum

\[
t_* = \frac{n-1}{n\sqrt2+n-2},\qquad L=2\sqrt2 t_*.
\]

At this value \(0<t_*<1/2\), so \(0<a,b<1\). Consequently \(I=1+(n-2)b=L\), \(D_0=L\), \(S_0\le L\), and \(1\le L\). Moreover \(N=2(1-b)/\sqrt3\) and \(N\le L\), since this inequality reduces to \(\sqrt6\ge1+\sqrt2\). Thus \(\|E_{t_*}\|=L\) and the lower bound is attained.

**4. The triangular case \(n=3\).** Here disjoint pairs of midpoints do not exist. The incident and nonincident terms give, for every real \(t\),

\[
I\ge\frac{4-2t}{3},\qquad N\ge\frac{4+4t}{3\sqrt3}.
\]

Their decreasing/increasing affine maximum has its unique minimum at \(t_*=6\sqrt3-10\), where the common value is \(8-4\sqrt3\). Here \(0<t_*<1/2\), the weights are positive, both lower bounds are attained, \(S_0=2t_*<8-4\sqrt3\), and the vertex contribution is \(1<8-4\sqrt3\). Therefore this value is globally optimal.

**5. Limits, monotonicity, and the standard interpolant.** For \(n\ge4\), treating \(n\) as a real variable, the derivative of \((n-1)/(n(1+\sqrt2)-2)\) is positive because its numerator after cancellation is \(\sqrt2-1>0\). The case \(\Lambda_3<\Lambda_4\) follows from the displayed exact formulas. The limit is \(2\sqrt2/(1+\sqrt2)=4-2\sqrt2\). For arithmetic midpoint interpolation \(t=1/2\), \(a=1/2,b=0\), and the orbit formula gives the claimed \(2/\sqrt3\) and \(\sqrt2\). This completes the proof.

## Verification

The optional standalone program `verify_simplex_midpoint.py` computes all five orbit expressions for \(3\le n\le10\). For \(n=3,4,5,6\), it additionally constructs **all** zero-one extremal boundary inputs and all target pairs and solves the resulting unsymmetrized linear program using NumPy and SciPy HiGHS. The four computed unrestricted minima, to 12 decimal places, are respectively \(1.071796769724\), \(1.108194187554\), \(1.123387183001\), and \(1.132704598305\), agreeing with the theorem to less than \(2\cdot10^{-8}\). The LP tests are finite corroboration; global all-dimensional correctness follows from the analytical averaging, orbit calculation, and affine-envelope proof above. Run `python verify_simplex_midpoint.py` with NumPy and SciPy installed.

## Relationship to prior work

The numerical-index work of Cobollo, Guirao, and Montesinos develops the Banach-space/Lipschitz-free setting and associated finite-metric operator methods, but studies numerical radii of operators on three-point free spaces, not the minimum norm of a simultaneous linear extension to a simplex's complete midpoint set. Basso develops general Lipschitz extension results, including simplicial settings and barycentric approaches; the general constants and constructions do not give the present exact minimax formula. Bruè, Di Marino, and Stra develop linear Lipschitz extension through random projections on doubling sets, but the corresponding general existence framework does not specify the sharp finite-configuration constant above. Existing one-point-center extension formulas for regular polygons and hypercubes involve a single new point rather than \(\binom n2\) edge midpoints; specifically, they do not imply the disjoint-midpoint constraint responsible for the \(n\ge4\) branch. Symmetry averaging itself is standard and is not claimed as new.

## Limitations

The theorem concerns one regular Euclidean simplex and its full collection of edge midpoints, not arbitrary simplices, other interpolation nodes, complex-valued functions, or extension to the whole simplex. The general absence of equivalent calculations under different terminology is not certified; an unindexed optimal finite linear-extension result could cover this formula. No independent mathematical audit has been performed.

## References

1. Ch. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (publicly posted 2023-04-25), https://arxiv.org/html/2304.13183v1.
2. G. Basso, *Lipschitz extension theorems with explicit constants*, arXiv:2310.13554 (publicly posted 2023-10-20), https://arxiv.org/html/2310.13554v3.
3. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and C1 extension operators through random projection*, arXiv:1801.07533v1 (publicly posted 2018-01-23), https://arxiv.org/abs/1801.07533.

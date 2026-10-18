# Sharp projection constants and a dimensional phase transition in finite quadratic Lorentz spaces

## Finding
For each integer \(n\ge3\) and real \(0\le t\le1\), equip \(\mathbb R^n\) with the rearrangement-invariant quadratic Lorentz norm
\[
N_t(x)=\left(t\sum_{i=1}^n x_i^2+(1-t)\max_{1\le i\le n}|x_i|^2\right)^{1/2}.
\]
For \(0<t\le1\), it is the weighted Lorentz norm with weights \((1,t,\ldots,t)\) at exponent two. At \(t=0\), it is the sup norm. Let \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and let \(\lambda_n(t)\) be the infimum of \(\|Q\|_{N_t\to N_t}\) over bounded linear projections with range \(H_n\). Then
\[
\boxed{\lambda_n(t)^2=\begin{cases}
\dfrac{4(n-1)(n-1+t)}{n^2\bigl(1+(n-1)t\bigr)},& 0\le t\le\dfrac1{n-1},\\[6pt]
1+\dfrac{(n-1)(1-t)^2}{n^2t},&\dfrac1{n-1}\le t\le1.
\end{cases}}
\]
The coordinate-centering projection \(P x=x-(\sum_i x_i/n)\mathbf1\) attains the infimum. For the first branch the vector \((1,-1,\ldots,-1)\) attains its norm, and for the second branch \(((n-1)t,-1,\ldots,-1)\) does so. At \(t=1\) every nonzero zero-sum vector is also a norm-attainer. The breakpoint \(t=1/(n-1)\) marks a genuine switch in the canonical extremal input's coordinate ratio.

## Assumptions and scope
The field is real, the dimension satisfies \(n\ge3\), and \(0\le t\le1\). The operator norm is induced by the same \(N_t\) on both the domain and codomain. Projection means \(Q^2=Q\) with exactly the indicated range; the claim is the *relative* projection constant, not the absolute projection constant of \(H_n\) under arbitrary embeddings. The endpoint \(t=0\) is included by the given norm formula, although some Lorentz definitions assume strictly positive weights.

## Proof
**(1) Symmetry reduces the minimum to centering.** Any projection onto the codimension-one kernel of \(f(x)=\sum_i x_i\) is \(Q=I-f\otimes u\) with \(f(u)=1\). Averaging its permutation conjugates over the full permutation group preserves the projection property and gives \(P=I-f\otimes(\mathbf1/n)\). Since each permutation is an \(N_t\)-isometry and the operator norm is convex, \(\|P\|\le\|Q\|\). Thus \(\lambda_n(t)=\|P\|\).

**(2) Quotient-by-constants reduction.** For \(y\in H_n\setminus\{0\}\), its preimages under \(P\) are exactly \(y+c\mathbf1\), so
\[
\|P\|^2=\sup_{y\in H_n\setminus\{0\}}
\frac{N_t(y)^2}{\min_{c\in\mathbb R}N_t(y+c\mathbf1)^2}.
\]
By scaling, changing every sign, and permuting coordinates, normalize the maximum and minimum of \(y\) to \(1+a\) and \(a-1\) respectively, where \(0\le a\le a_*=(n-2)/n\). The upper bound on \(a\) follows from the zero sum and the fact that each remaining coordinate is at least \(a-1\). Write \(S=\sum_i y_i^2\). Convexity of the square and the zero sum give
\[
S\ge 2+\frac{2n}{n-2}a^2,
\]
with equality exactly when the remaining \(n-2\) coordinates all equal \(-2a/(n-2)\). This equality choice is feasible for every stated \(a\).

**(3) Optimize the shift exactly.** Since \(\max_i|y_i+c|=1+|a+c|\),
\[
N_t(y+c\mathbf1)^2=tS+ntc^2+(1-t)(1+|a+c|)^2.
\]
Minimizing the scalar convex quadratic on the two half-lines yields
\[
\min_c N_t(y+c\mathbf1)^2=tS+nta^2+(1-t)-
\frac{\bigl[nta-(1-t)\bigr]_+^2}{1+(n-1)t},
\]
where \([z]_+=\max\{z,0\}\). Because this minimum never exceeds \(N_t(y)^2=tS+(1-t)(1+a)^2\), their quotient is nonincreasing in \(S\) for fixed \(a\): both numerator and denominator contain the identical term \(tS\). Therefore it suffices to use the sharp lower value of \(S\).

**(4) Show that the unique scalar maximum lies at the endpoint, except for the Hilbert endpoint.** After substituting this minimum \(S\), define
\[
U(a)=1+t+2(1-t)a+\left(1-t+\frac{2nt}{n-2}\right)a^2,
\]
\[
V(a)=1+t+\frac{n^2t}{n-2}a^2-
\frac{\bigl[nta-(1-t)\bigr]_+^2}{1+(n-1)t}.
\]
Then \(\lambda_n(t)^2=\max_{0\le a\le a_*}U(a)/V(a)\). We verify this ratio is nondecreasing. For the first branch \(nta\le1-t\), let \(V_1=1+t+n^2ta^2/(n-2)\). The derivative numerator \(D_1=U'V_1-UV_1'\) is a concave quadratic in \(a\) because its leading coefficient is \(2n^2t(t-1)/(n-2)\le0\). At the left endpoint it has value \(2(1-t^2)\ge0\). If the right endpoint of this branch is \(a_*\), then necessarily \(t\le1/(n-1)\), and
\[
D_1(a_*)=\frac{4(n-1+t)(1-(n-1)t)}n\ge0.
\]
If instead the branch ends at \(a_0=(1-t)/(nt)\), then \(t\ge1/(n-1)\), and
\[
D_1(a_0)=\frac{4(1-t)^2((n-1)t-1)}{nt(n-2)}\ge0.
\]
A concave function lies above the chord joining its endpoints, so \(D_1\ge0\) throughout this branch. At \(t=0\), the whole interval is the first branch and the same conclusion follows directly.

On the second branch, \(nta\ge1-t\), direct differentiation and factorization give
\[
U'V-V'U=\frac{4t(a+1)(1-t)^2\bigl((n-2)-na\bigr)}{(n-2)\bigl(1+(n-1)t\bigr)}\ge0
\]
for \(a\le a_*\). Thus the maximum is at \(a=a_*\). Its equality configuration is \(y\propto(n-1,-1,\ldots,-1)\).

**(5) Evaluate both regimes.** At \(a_*=(n-2)/n\),
\[
U(a_*)=\frac{4(n-1)(n-1+t)}{n^2},\qquad
V_1(a_*)=1+(n-1)t.
\]
When \(t\ge1/(n-1)\), the active-shift branch instead gives
\[
V(a_*)=\frac{4(n-1)t}{1+(n-1)t}.
\]
Dividing and simplifying proves both formulas, including agreement at their common boundary. Undoing the optimizing constant shift gives the source vectors stated in the Finding. In particular \(\lambda_n(0)=2(n-1)/n\) and \(\lambda_n(1)=1\). For every \(0\le t<1\), the formula gives \(\lambda_n(t)>1\): in the second branch this is immediate; in the first the numerator minus the denominator's scaled counterpart simplifies to a positive expression on the specified parameter range.

## Verification
The self-contained rational-arithmetic checker `checks/check_projection.py` evaluates both branches and equality vectors for rational parameters across dimensions, enumerates a finite grid of source vectors to check the proved bound, and confirms the exact scalar reduction on rational grids. It uses only the Python standard library and is supplementary to the analytic proof. Separately, numerical stress tests checked 52 dimension–parameter combinations with 15,000 randomized source vectors per combination; no violation was found. Such finite tests do not establish the universal theorem, which follows from the calculations above.

## Relationship to prior work
Randrianantoanina's 1997 full-length preprint *One-complemented subspaces of real sequence spaces* (arXiv:math/9702214, Theorem 3 and Corollary 4) treats 1-complemented hyperplanes of real Lorentz sequence spaces and establishes qualitative restrictions on norm-one projections. The same author's 2001 full-text survey *Norm One Projections in Banach Spaces* (arXiv:math/0110171, sections on Lorentz spaces and minimal projections) reviews related structural theorems. These treatments do not supply the exact greater-than-one optimal projection norms, all-dimensional piecewise parameter formula, or maximizing inputs above. The 1994 paper *Contractive projections and isometries in sequence spaces* (arXiv:math/9403207) is earlier context for norm-one projection geometry. The research-record comparisons also included the different centering problem in standard \(\ell_p\) geometry and projection problems for finite metric free spaces; their results do not imply this weighted Lorentz formula.

## Limitations
The statement is for the given real finite-dimensional quadratic Lorentz norm and the particular sum-zero hyperplane; no conclusion is made for other weight sequences, general hyperplanes, infinite-dimensional limits as operators, or complex scalars. It establishes an optimal *value* and a canonical norm-attaining projection, not uniqueness among all optimizers. Broader bibliographic coverage cannot exclude an equivalent older derivation not retrieved or indexed. Independent review has not been performed.

## References
1. B. Randrianantoanina, *Contractive projections and isometries in sequence spaces*, arXiv:math/9403207 (public preprint, 1994-03-04).
2. B. Randrianantoanina, *One-complemented subspaces of real sequence spaces*, arXiv:math/9702214 (public preprint, 1997-02-24), especially Theorem 3 and the discussion of real Lorentz hyperplanes.
3. B. Randrianantoanina, *Norm One Projections in Banach Spaces*, arXiv:math/0110171 (public preprint, 2001-10-16), sections on Lorentz sequence spaces and minimal projections.

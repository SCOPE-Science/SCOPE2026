# A sharp large-step positivity threshold for two-stage Lobatto IIIC on absorbing birth chains

## Finding

The two-stage Lobatto IIIC Runge–Kutta method, applied without modification to a unit-rate absorbing pure-birth chain of \(n\ge2\) states, has an exactly classifiable entrywise-nonnegative endpoint matrix. Let \(Q_n\) be the \(n\times n\) continuous-time generator with \((Q_n)_{i,i}=-1\) and \((Q_n)_{i,i+1}=1\) for \(1\le i<n\), and with zero last row. For \(h\ge0\), define

\[
M_n(h)=R(hQ_n),\qquad R(z)=\frac{1}{1-z+z^2/2}.
\]

For \(2\le n\le4\), every \(h\ge0\) yields an entrywise-nonnegative matrix. For \(n\ge5\), the exact domain is

\[
\boxed{\{0\}\cup[h_n,\infty),\qquad
h_n=\cot\!\left(\frac{3\pi}{4(n-1)}\right)-1.}
\]

At \(h=h_n>0\) the only nonstructural zero entry is the transition from state \(1\) to the absorbing state \(n\); every structurally allowed entry is strictly positive for \(h>h_n\). In particular, the first two algebraically simple examples are \(h_7=\sqrt2\) and \(h_{10}=1+\sqrt3\), and

\[
h_n=\frac{4(n-1)}{3\pi}-1-\frac{\pi}{4(n-1)}+O(n^{-3}).
\]

Thus for \(n\ge5\) *arbitrarily small positive steps fail positivity*, whereas sufficiently large steps recover positivity; the required positive step grows linearly with chain length. This statement concerns endpoint entrywise nonnegativity, not internal stages or numerical accuracy.

## Assumptions and scope

The chain has exactly \(n\) ordered states, one-way jumps \(i\to i+1\) at unit rate for \(1\le i<n\), and the final state is absorbing. The unmodified two-stage Lobatto IIIC tableau is

\[
A=\begin{pmatrix}\tfrac12&-\tfrac12\\\tfrac12&\tfrac12\end{pmatrix},
\qquad b=\begin{pmatrix}\tfrac12\\\tfrac12\end{pmatrix}.
\]

The stability function follows directly from \(R(z)=1+zb^\mathsf T(I-zA)^{-1}\mathbf1\). The matrix \(M_n(h)\) is row-stochastic for all \(h\ge0\), since \(Q_n\mathbf1=0\) and \(R(0)=1\). The only property under study is nonnegativity of *all* endpoint entries. There is no claim of nonnegative internal stage vectors, nonnegative evolution for arbitrary generators, or an accuracy improvement at large step sizes.

## Proof

For \(h>0\), let

\[
D=h^2+2h+2,\quad A_h=1+h+\frac{h^2}{2},\quad
\theta=\arctan\frac1{1+h}\in(0,\pi/4),\quad
q=\frac{h}{\sqrt D}=\cos\theta-\sin\theta\in(0,1).
\]

Write \(S\) for the forward shift on the \(n-1\) transient states. The transient block of \(Q_n\) equals \(S-I\). Hence the transient block of \(M_n(h)\) is the polynomial truncation of the rational series

\[
\frac{1}{1+h(1-t)+\frac{h^2}{2}(1-t)^2}
=\frac{1/A_h}{1-2q\cos\theta\,t+q^2t^2}
=\sum_{k\ge0}c_k t^k.
\]

The sine generating-function identity gives, for all integers \(k\ge0\),

\[
\boxed{c_k=\frac{q^k\sin((k+1)\theta)}{A_h\sin\theta}.}
\]

Consequently \((M_n(h))_{ij}=c_{j-i}\) whenever \(1\le i\le j<n\), and lower-triangular transient entries vanish. Row-stochasticity gives \((M_n(h))_{i,n}=1-\sum_{k=0}^{n-i-1}c_k\) for \(i<n\). The infinite series sums to one because its generating function is one at \(t=1\) and \(q<1\). For any integer \(r\ge0\), direct summation of the complex geometric series yields

\[
1-\sum_{k=0}^{r}c_k
=q^{r+1}\big[\cos((r+1)\theta)+\sin((r+1)\theta)\big].
\]

Indeed, before simplification the right side is

\[
\frac{q^{r+1}}{\sin\theta}\left[\sin((r+2)\theta)-q\sin((r+1)\theta)\right],
\]

and \(q=\cos\theta-\sin\theta\) gives the claimed factor. Thus the exact absorption entries are

\[
\boxed{(M_n(h))_{i,n}=q^{n-i}
\big[\cos((n-i)\theta)+\sin((n-i)\theta)\big]}
\qquad(1\le i<n).
\]

**Sufficiency.** If \((n-1)\theta\le3\pi/4\), then all values \(k\theta\), for integers \(1\le k\le n-1\), lie in \((0,3\pi/4]\). Therefore every absorption entry is nonnegative. For every transient coefficient used in the finite matrix, \((k+1)\theta\le3\pi/4<\pi\), so \(c_k>0\). All other entries are structural zeros or the absorbing diagonal one, hence \(M_n(h)\ge0\) entrywise.

**Necessity.** Suppose \((n-1)\theta>3\pi/4\). Choose the smallest positive integer \(k\) with \(k\theta>3\pi/4\). Then \(k\le n-1\), and because \(0<\theta<\pi/4\),

\[
3\pi/4<k\theta<\pi.
\]

On this interval \(\cos(k\theta)+\sin(k\theta)<0\). The absorbing entry from state \(n-k\) to state \(n\) is therefore strictly negative. Thus no positive step outside the angular condition is feasible. Since \(\theta(h)\) is strictly decreasing from \(\pi/4\) to zero, the condition holds for all \(h>0\) if \(n\le4\), and exactly for \(h\ge h_n\) when \(n\ge5\). Finally \(M_n(0)=I\) is nonnegative.

At the positive boundary \((n-1)\theta=3\pi/4\), only \(k=n-1\) makes the bracket vanish; all smaller positive \(k\) and all needed transient coefficients give strict positivity. The cotangent series \(\cot x=x^{-1}-x/3+O(x^3)\) gives the displayed asymptotics. This completes the proof for every integer \(n\ge2\) and every real \(h\ge0\).

## Verification

The standalone Python 3 file `verify.py` uses exact rational arithmetic to construct the endpoint matrix via its coefficient recurrence and, independently, via direct inversion of \(I-hQ_n+(h^2/2)Q_n^2\). In its executed test suite it passed **26,022 assertion groups**, including matrix inversion comparisons, row-stochasticity, exact signs and trigonometric closed forms over sizes \(2\) through \(41\) and multiple rational step sizes. Small boundary checks include the negative/positive pairs \((n,h)=(5,1/4),(5,1/2)\), \((6,1/2),(6,1)\), \((7,7/5),(7,3/2)\), and \((10,5/2),(10,3)\). The all-size conclusion is analytic; finite computational checks are supplemental and do not certify the infinite quantifiers.

To rerun: `python3 verify.py` from the directory containing the file.

## Relationship to prior work

Lóczi and Ketcheson (2013, arXiv:1303.6651v1) study rational absolute monotonicity and its role in positivity guarantees; their bounds concern general numerical schemes rather than the exact endpoint sign domain for this particular absorbing birth chain. Higueras, Ketcheson and Kocsis (arXiv:1505.04024v1, 2015; the later revision was separately inspected) study monotonicity-preserving *perturbations* to methods, whereas the present result treats unmodified two-stage Lobatto IIIC. The latter method has the \([0/2]\) Padé stability function, but a stability function's general absolute-monotonicity radius does not determine a graph-specific large-step recovery interval. The exact angular threshold, every-state classification, boundary zeros, and linear-length asymptotic are the claimed contribution. Prior analyses of higher-order \([2/2]\) Padé, Radau IIA and related endpoint maps have different stability functions, so their sign results do not imply this theorem by a relabeling of the step size.

## Limitations

The result assumes a unit-rate, unidirectional path with one absorbing terminal state. Unequal birth rates, branching chains, other implicit tableaux, nonlinear systems and internal-stage positivity are not classified. A large step may have substantial time-discretization error even when the endpoint matrix is stochastic. Historical specialist overlap remains possible.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first posted 2013-03-26), https://arxiv.org/abs/1303.6651.
2. I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024v1 (first posted 2015-05-15), https://arxiv.org/abs/1505.04024.
3. E. Hairer and G. Wanner, *Solving Ordinary Differential Equations II*, Springer (1996), Chapter IV, Lobatto IIIC tableau (bibliographic background).

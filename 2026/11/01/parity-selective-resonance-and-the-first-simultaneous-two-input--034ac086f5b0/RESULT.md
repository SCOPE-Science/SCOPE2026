# Parity-selective resonance and the first simultaneous two-input control failure on weighted ladders

## Finding
For every integer \(n\geq2\), let a two-rail ladder have positive longitudinal conductances \(w_1,\ldots,w_{n-1}\) that satisfy \(w_i=w_{n-i}\), and a constant positive rung conductance \(g\). Use two independent point actuators: one at the first vertex of the upper rail, and the other at the last vertex of either the upper rail (*same-rail placement*) or lower rail (*opposite-rail placement*).

Let \(0=\lambda_0<\lambda_1<\cdots<\lambda_{n-1}\) be the ordered eigenvalues of the weighted path Laplacian with longitudinal conductances \(w_i\). The exact controllable-subspace dimensions are
\[
\begin{aligned}
r_{\mathrm{same}}(g)&=2n-\#\{(i,j):0\leq j<i<n,\ \lambda_i-\lambda_j=2g,\ i-j\ \text{even}\},\\
r_{\mathrm{opposite}}(g)&=2n-\#\{(i,j):0\leq j<i<n,\ \lambda_i-\lambda_j=2g,\ i-j\ \text{odd}\}.
\end{aligned}
\]
In particular each placement is fully controllable except at a finite set of explicit positive spectral-gap/2 values. At every resonance the two placements lose complementary classes of path-eigenvalue collisions. Multiple collisions can cause larger simultaneous losses; each distinct ordered pair contributes exactly one lost dimension for the indicated placement.

For the unit-weight longitudinal path, **six rungs is the smallest size** admitting any \(g>0\) at which *both* placements fail simultaneously. At \(n=6\) and \(g=1/2\), their ranks are \(11\) and \(10\), respectively, out of \(12\). For each integer \(2\le n\le5\) and each \(g>0\), at least one of the two placements is fully controllable (the successful placement may depend on \(g\)). This sharp minimality statement concerns unit longitudinal weights, not all palindromic choices.

## Assumptions and scope
Let \(P\) be the real symmetric weighted path Laplacian on \(n\) vertices, \(P_{i,i+1}=P_{i+1,i}=-w_i\), \(P_{11}=w_1\), \(P_{nn}=w_{n-1}\), and each other diagonal is the sum of incident weights. All \(w_i>0\) and \(w_i=w_{n-i}\). Define
\[
L=P\otimes I_2+gI_n\otimes\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad g>0.
\]
Index vertices by \((i,\mathrm{upper})\) and \((i,\mathrm{lower})\). Dynamics are \(\dot z=-Lz+Bu\), with the two columns of \(B\) being unit coordinate vectors at \((1,\mathrm{upper})\) and at either \((n,\mathrm{upper})\) or \((n,\mathrm{lower})\). The controllability rank is the rank of \([B,LB,\ldots,L^{2n-1}B]\). No assertion is made for nonsymmetric paths, unequal rung conductances, different input configurations, or directed edges.

For direct polynomial evaluation, put
\[
E(x)=\prod_{\substack{0\le k<n\\k\ \mathrm{even}}}(x-\lambda_k),\qquad
O(x)=\prod_{\substack{0\le k<n\\k\ \mathrm{odd}}}(x-\lambda_k),\quad d=2g.
\]
All these factors have simple real roots. The exact deficits admit equivalent, potentially computationally useful polynomial formulas:
\[
\begin{aligned}
2n-r_{\mathrm{same}}&=\deg\gcd(E(x),E(x+d))+\deg\gcd(O(x),O(x+d)),\\
2n-r_{\mathrm{opposite}}&=\deg\gcd(E(x),O(x+d))+\deg\gcd(O(x),E(x+d)).
\end{aligned}
\]
Here \(\gcd\) is the monic polynomial gcd over a field containing the path weights and \(g\); its degree is independent of the choice of such a field if these numbers are represented exactly.

## Proof
**1. Ordered path modes and reflection parity.** Since \(P\) is a symmetric irreducible tridiagonal matrix (all subdiagonals are nonzero), its eigenvalues are real and simple. Its eigenvectors have nonzero first and last coordinates: otherwise the first or last eigenvector equation, iterated along the path, would force every coordinate to vanish. Because \(w_i=w_{n-i}\), \(P\) commutes with path reversal \(R\). Each one-dimensional eigenspace therefore has reversal eigenvalue \(+1\) or \(-1\). Interpolate the positive symmetric weights continuously to all-one weights. The spectrum stays simple, so the reversal signs of the eigenvectors cannot change. For the unit-weight path, the \(k\)-th ordered eigenmode is \(\cos((i-1/2)k\pi/n)\), whose reversal sign is \((-1)^k\). Thus for every positive palindromic weighting, each ordered normalized eigenvector \(\phi_k\) satisfies \(\phi_k(n)=(-1)^k\phi_k(1)\) with \(\phi_k(1)\neq0\).

**2. Ladder modes and collision blocks.** The rung matrix has normalized eigenvectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\), with eigenvalues \(0\) and \(2g\). Therefore \(L\) has the two branches \(\lambda_k\) and \(\lambda_k+2g\), each simple within its branch. A multiple eigenvalue can occur only when \(\lambda_i=\lambda_j+2g\), necessarily \(i>j\). Each such eigenvalue has multiplicity exactly two, and no eigenvalue can belong to two distinct collision pairs because either branch individually has a simple spectrum.

**3. PBH evaluation for the two input placements.** The pair \((-L,B)\) is controllable on the eigenspace of a real symmetric \(L\) exactly when the restriction of \(B^T\) to that eigenspace is injective. At a noncollision eigenvalue, the upper-rail endpoint input has nonzero projection, so no rank is lost. At a collision \(\lambda_i=\lambda_j+2g\), take the plus-rail mode with path index \(i\) and minus-rail mode with index \(j\). Up to the nonzero factors \(\phi_i(1)/\sqrt2\) and \(\phi_j(1)/\sqrt2\), their two input-projection columns are
\[
\binom{1}{(-1)^i},\qquad\binom{1}{s(-1)^j},\quad
s=\begin{cases}+1&\text{same rail},\\-1&\text{opposite rails}.
\end{cases}
\]
They become dependent precisely when \((-1)^i=s(-1)^j\). Hence the same-rail placement loses one direction if and only if \(i-j\) is even, while the opposite-rail placement loses one if and only if \(i-j\) is odd. Since collision eigenspaces are orthogonal and spectrally distinct, the deficiencies add, proving both rank formulas. Equating roots of a polynomial and its translated polynomial produces the stated gcd formulas; simple roots ensure each common root contributes exactly one to its degree.

**4. Sharp first simultaneous failure for unit longitudinal weights.** With \(w_i=1\), the ordered path spectrum is \(\lambda_k=2-2\cos(k\pi/n)\). A rung strength makes both placements uncontrollable exactly when the same positive spectral gap occurs between some even-index-separated pair and some odd-index-separated pair. The exhaustive sets of positive gaps for the parity classes, with repetitions removed, are:

- \(n=2\): even \(\varnothing\); odd \(\{2\}\).
- \(n=3\): even \(\{3\}\); odd \(\{1,2\}\).
- \(n=4\): even \(\{2,2\sqrt2\}\); odd \(\{2-\sqrt2,\sqrt2,2+\sqrt2\}\).
- \(n=5\): even \(\{(5-\sqrt5)/2,\sqrt5,(5+\sqrt5)/2\}\); odd \(\{(3-\sqrt5)/2,1,\sqrt5-1,(3+\sqrt5)/2,1+\sqrt5\}\).

Each listed pair of sets is disjoint. At \(n=6\), the path spectrum is \(\{0,2-\sqrt3,1,2,3,2+\sqrt3\}\). The gap \(1\) occurs between indices \((2,0)\), \((3,2)\), and \((4,3)\): the first has even index separation and the remaining two have odd separation. Taking \(2g=1\) thus gives ranks \(12-1=11\) and \(12-2=10\). This proves existence and minimality. The distinct common gap \(2\) at \(n=6\) similarly gives ranks \((11,11)\) when \(g=1\).

## Verification
The self-contained `verify.py` implements two mathematically different rank calculations in exact arithmetic. One constructs the two reflection-parity characteristic polynomials, computes the four translated gcd degrees, and predicts both ranks. The other builds the full \(2n\)-dimensional ladder Laplacian and independently computes the exact Kalman-matrix ranks. The supplied program passes 42 comparisons for uniform paths with \(2\le n\le7\) and heterogeneous positive palindromic rational weights, checks four exact resonance boundary assertions (including an algebraic strength \(g=\sqrt2/2\)), and exhaustively compares even/odd spectral-gap sets for the unit paths \(2\le n\le6\).

Run `python verify.py` with Python 3 and SymPy installed. These finite checks independently corroborate specific examples; they are not used in place of the all-dimensional analytic argument above.

## Relationship to prior work
Rahmani, Ji, Mesbahi and Egerstedt (2009) establish a general relationship between graph symmetry, equitable partitions, and multi-leader controllability; the available abstract does not give an explicit two-rail spectral-gap rank classification. Monshizadeh, Zhang and Camlibel (2014) give zero-forcing criteria for strong structural controllability for whole qualitative matrix classes, whereas this result concerns exact controllability for a specified parametrized symmetric Laplacian. Yuan, Zhao, Wang, Di and Lai (2014), in Section 2.3 and Appendix C, analyze spectral multiplicity and minimum driver-node counts for multiplex diffusion, including full interlayer coupling, but not the dimensions of the reachable subspaces under these two prescribed pairs of endpoint actuators. The eigenvalue splitting used here is compatible with their general multiplex factorization; the new conclusion hinges on endpoint reversal parity, exact resonance multiplicity, and the sharp six-rung comparison.

The potentially relevant 2024 paper of Wang and Zhang, *Controllability of Symmetric Double Layer Networks*, could not be fully inspected despite searches of available preprint and open-access sources. Its title and subject create a genuine historical-overlap risk, not an established contradiction. No claim is made that the present theorem exhausts or supersedes the broader literature on Cartesian-product controllability.

## Limitations
The proof assumes strictly positive and mirror-palindromic longitudinal conductances and a uniform positive rung conductance. Its minimum-size statement is specific to unit longitudinal weights and the two stated endpoint placements. The results do not characterize minimum actuator counts or optimal control energy, nor do they establish a broader structural-controllability theorem. Independent mathematical audit has not been performed. Completeness of the historical literature comparison is limited by inaccessible specialized sources.

## References
1. A. Rahmani, M. Ji, M. Mesbahi, and M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM J. Control Optim. 48 (2009), 162–186, DOI: https://doi.org/10.1137/060674909 (first public online date 2009-02-11; abstract accessible).
2. N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, 2014, https://arxiv.org/abs/1403.4868 (version 1, 2014-03-19; open full text inspected).
3. Z. Yuan, C. Zhao, W.-X. Wang, Z. Di, and Y.-C. Lai, *Exact controllability of multiplex networks*, New Journal of Physics 16 (2014) 103036, https://doi.org/10.1088/1367-2630/16/10/103036 (relevant sections and Appendix C inspected in https://chaos1.la.asu.edu/~yclai/papers/NJP_2014_YZWDL.pdf).
4. J. Wang and Q. Zhang, *Controllability of Symmetric Double Layer Networks*, IEEE CCCI 2024, pp. 1–7 (bibliographic record at https://dblp.org/rec/conf/ccci/WangZ24; full text unavailable in this review).

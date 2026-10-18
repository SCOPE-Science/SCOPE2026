# Exact cut-space projection constants of weighted multibranch diamonds

## Finding

For each integer \(m\ge3\), consider the connected graph \(G=K_{2,m}\), with terminals \(u,v\), internal vertices \(z_1,\ldots,z_m\), and edges oriented \(u\to z_i\to v\). Fix arbitrary real numbers \(r_i>0\) and assign **both** edges of the \(i\)-th branch length \(r_i\). Let \(X=\ell_{1,r}(E(G);\mathbb R)\), with edge norm
\[
\|x\|_{1,r}=\sum_{i=1}^m r_i\bigl(|x_{i,1}|+|x_{i,2}|\bigr),
\]
and let \(B(G)=\operatorname{ran}D^{\mathsf T}\subset X\) be the graph cut (gradient) subspace, where \(D\) is the oriented incidence operator. Its relative projection constant, taken over **all** real linear projections with range \(B(G)\), is
\[
\boxed{\lambda(B(G),X)=1+\left(\sum_{i=1}^m\frac{r_i}{R-r_i}\right)^{-1},\qquad R=\sum_{i=1}^m r_i.}
\]
An explicit norm-minimizing projection is given in the proof; no restriction to graph-equivariant projections is part of the theorem.

There are sharp global consequences: for every positive weight vector,
\[
1<\lambda(B(G),X)\le2-\frac1m,
\]
with equality on the right **if and only if all branch lengths coincide**. The infimum over positive length vectors is \(1\), approached (but never attained) when one branch becomes overwhelmingly longer than the others.

For \(m=k+1\ge3\) and \(r_1=\cdots=r_k=1\), \(r_{k+1}=t\ge1\), the dependence is the rational function
\[
\lambda=1+\frac{k(k+t-1)}{k^2+kt+t^2-t},\qquad
\frac{d\lambda}{dt}=-\frac{k(t-1)(2k+t-1)}{(k^2+kt+t^2-t)^2}.
\]
Thus the loss of complementability is stationary at the unweighted point, then strictly decreases for all \(t>1\), with \(\lambda-1\sim k/t\). For unit weights \(\lambda=2-1/m\); this differs from the previously reported cycle-space value \(2-2/m\) for the same unweighted graph. The result is specifically about the **cut space**, not the cycle space.

## Assumptions and scope

All scalars and linear projections are real. Each of the \(2m\) oriented edges is a separate coordinate of \(X\). The two edges along any particular branch have the same positive length, but different branches can have arbitrary positive lengths. The theorem is an ambient relative projection-norm statement; no Banach–Mazur distance, Hilbert norm, or nonlinear retraction is claimed. The graph's shortest-path metric is well defined: the direct edge from a terminal to an internal vertex is strictly shorter than an alternate three-edge walk, so every edge is geodesic. The cut space has dimension \(m+1\), hence codimension \(m-1\ge2\). The restriction \(m\ge3\) also distinguishes this result from the classical hyperplane case.

## Proof

**1. Identify the subspace.** For an arbitrary edge vector, write
\[
s_i=\frac{x_{i,1}+x_{i,2}}2,\qquad d_i=\frac{x_{i,1}-x_{i,2}}2.
\]
If \(x=D^{\mathsf T}f\) is a vertex potential's edge gradient, then \(x_{i,1}+x_{i,2}=f(v)-f(u)\) for every \(i\). Conversely, if these sums all agree, choose the terminal potential difference to be this common sum and choose each interior potential to realize \(x_{i,1}\). Thus
\[
B(G)=\{x:s_1=\cdots=s_m\},\qquad
\|x\|_{1,r}=2\sum_i r_i\max\{|s_i|,|d_i|\}.
\]

**2. Reduce all projections, not merely symmetric candidates.** Independently exchanging the two edge coordinates in branch \(i\) preserves both the weighted ambient norm and \(B(G)\). These \(m\) commuting exchanges generate a group of order \(2^m\). Average any projection \(P:X\to B(G)\) over conjugation by this group. The average is still a projection onto \(B(G)\), since every conjugate acts as the identity on \(B(G)\), and by convexity its norm does not increase.

In \((s,d)\) coordinates, the group acts trivially on the \(m\)-dimensional \(s\)-space and changes the sign of each \(d_i\) independently. A commuting linear operator cannot mix different sign characters. Because each \(d_i\)-line already lies in \(B(G)\), any commuting projection fixes it. Its action on \(s\) must map onto the constant-sum line and fix that line. Consequently **every averaged projection** has the form
\[
P_\alpha(s,d)=(\bar s\mathbf 1,d),\qquad
\bar s=\sum_{j=1}^m\alpha_js_j,\qquad \sum_j\alpha_j=1,
\]
with real coefficients \(\alpha_j\), potentially negative. Every such \(P_\alpha\) is indeed a projection onto \(B(G)\).

**3. Compute exact weighted column norms.** Take a standard basis vector at either edge of branch \(j\). Its image under \(P_\alpha\) has, on branch \(j\), entries \((\alpha_j+1)/2\) and \((\alpha_j-1)/2\), and on each other branch, entries \(\alpha_j/2\) and \(\alpha_j/2\). The weighted \(\ell_1\) matrix-column norm is therefore, exactly,
\[
F_j(\alpha_j)=\max\{1,|\alpha_j|\}+\frac{R-r_j}{r_j}|\alpha_j|.
\]
Both edge columns of branch \(j\) have this same norm, so \(\|P_\alpha\|=\max_jF_j(\alpha_j)\).

**4. Sharp lower bound and attaining projection.** Put \(c_j=(R-r_j)/r_j>0\) and \(H=\sum_j1/c_j\). For arbitrary real coefficients satisfying \(\sum_j\alpha_j=1\),
\[
\|P_\alpha\|\ge1+\max_j c_j|\alpha_j|
\ge1+\frac{\sum_j|\alpha_j|}{\sum_jc_j^{-1}}
\ge1+\frac1H.
\]
These inequalities are valid for all signs and sizes of coefficients, not just those within a simplex. Choose
\[
\alpha_j=\frac{1/c_j}{H}=\frac{r_j/(R-r_j)}{\sum_i r_i/(R-r_i)}.
\]
Then \(0<\alpha_j<1\), \(\sum_j\alpha_j=1\), and \(c_j\alpha_j=1/H\) for every \(j\). Hence \(F_j(\alpha_j)=1+1/H\) for every \(j\). This gives the asserted norm and attains the bound over all projections by the averaging argument.

**5. Extremal weight geometry.** Normalize \(\sum_i r_i=R\), with \(R>0\) fixed. The function \(f(x)=x/(R-x)\) satisfies \(f''(x)=2R/(R-x)^3>0\) for \(0<x<R\). By strict Jensen,
\[
H=\sum_i f(r_i)\ge m f(R/m)=\frac{m}{m-1},
\]
with equality only for \(r_1=\cdots=r_m\). Thus \(\lambda\le 1+(m-1)/m=2-1/m\), and equality is rigid. As \(r_1/R\uparrow1\), the summand \(r_1/(R-r_1)\) diverges, giving \(\lambda\downarrow1\). Conversely \(H\) is finite for every strictly positive finite vector, so \(\lambda>1\).

For the one-defect family, substitution \(R=k+t\) yields \(H=k/(k+t-1)+t/k\). Elementary simplification and differentiation give the formulas and strict decrease for \(t>1\). Expanding the rational function at infinity yields \(\lambda-1\sim k/t\).

## Verification

The self-contained Python 3 file `verify_exact.py` uses `fractions.Fraction` only. It checks 120 rational-weight configurations, including varying dimensions and boundary-like weight patterns. For each, it reconstructs the full \(2m\)-by-\(2m\) projection matrix, proves the displayed matrix is idempotent by exact multiplication, checks its range and its action on a basis of the cut space, and checks every weighted column norm against the claimed rational formula. It also checks the lower-bound equality equations exactly.

The separate `verify_lp.py` uses NumPy and SciPy's `linprog` to minimize over **unrestricted, unsymmetrized** projection matrices satisfying the defining range and idempotence-on-range linear constraints. With a fixed pseudorandom seed it compares 50 instances, dimensions \(m=2,3,4,5,6\), against the closed formula. The 50 runs pass within \(10^{-8}\). For the theorem's stated range \(m\ge3\), 40 of these are direct cross-checks. These finite computations corroborate, but do not prove, the assertions for all dimensions and real weights; that role belongs to the argument above.

Run from the directory containing these files:

```sh
python3 verify_exact.py
python3 verify_lp.py
```

The second command requires SciPy and NumPy. Neither script is needed to read or validate the analytical proof.

## Relationship to prior work

The cut-space and weighted edge representation, and the connection with transportation-cost/Lipschitz-free spaces, are established in Dilworth–Kutzarova–Ostrovskii (2023, §§1.1–1.4). Its principal projection results concern **cycle spaces** of tori and Hamming graphs. Its discussion of the cut space supplies the framework, but not the present weighted \(K_{2,m}\) minimum over projections **onto the cut space**.

Dilworth–Kutzarova–Ostrovskii (2018, §5.1) explicitly treat unweighted multibranching diamonds \(K_{2,m}\) and state the constant \(2(m-1)/m\) for a **cycle-space** projection. At unit weights the cut-space constant determined here is instead \(2-1/m\). These are different ranges and different exact invariants; one numerical value does not imply the other.

Blatter–Cheney (1974) determines classical projection constants onto **hyperplanes** in sequence spaces. The present cut subspace has codimension \(m-1\ge2\), so that theorem is not directly applicable. General averaging of projections is also classical and is employed here only as a method; the new content claimed is the exact higher-codimension weighted cut formula and rigid/extreme-weight consequences. No claim of novelty is made for the basic theory of graph cuts, weighted \(\ell_1\) norms, or symmetry averaging.

## Limitations

The two edges on each branch must have equal weight; no formula is claimed for arbitrary independent weights on all \(2m\) edges. The theorem concerns a finite-dimensional ambient **relative** projection constant, not an absolute projection constant or an optimal map in \(\ell_\infty\). It does not determine minimum cycle projections for heterogeneous weights or projection constants for iterated diamond graphs. Bibliographic comparison has sampled the most relevant accessible primary sections and mathematical-record searches; an unindexed or differently stated general projection result could still subsume this calculation. Independent review has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first public 2023-05-21, https://arxiv.org/pdf/2305.12582 (especially §§1.1, 1.3, 1.6, 2.1).
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, first public 2018-07-10, https://arxiv.org/pdf/1807.03814 (especially §5.1).
3. J. Blatter, E. W. Cheney, *Minimal projections on hyperplanes in sequence spaces*, Ann. Mat. Pura Appl. 101 (1974), 215–227, https://doi.org/10.1007/BF02417105.

# A shear-strength autocorrelation law and exceptional first-lag cancellation for hyperbolic cat maps

## Finding
For every integer \(k\ge1\), let
\[
T_k(x,y)=((k^2+1)x+ky,\;kx+y)\pmod 1,
\qquad f(x,y)=(\{x\}-1/2)(\{y\}-1/2).
\]
For Haar-uniform \(X\in\mathbb T^2\), write \(C_k(n)=\mathbb E[f(X)f(T_k^nX)]\). Then
\[
\boxed{C_k(1)=-\frac{(k^2-1)(5k^2+4)}{720k^2(k^2+1)^2}.}
\]
In particular, \(C_1(1)=0\), \(C_k(1)<0\) for every integer \(k\ge2\), and \(C_k(1)=-1/(144k^2)+O(k^{-4})\). Nevertheless
\[
\boxed{C_1(2)=-\frac{121}{81000}\ne0.}
\]
This is a first-lag cancellation, not complete temporal independence.

## Assumptions and scope
The matrix \(A_k=\bigl(\begin{smallmatrix} k^2+1&k\\k&1\end{smallmatrix}\bigr)\) is integral with determinant one and trace greater than two, hence defines a hyperbolic Haar-preserving torus automorphism. The fractional parts in \(f\) use representatives in \([0,1)\); discontinuities along coordinate seams have Haar measure zero. The mean of \(f\) is zero and its variance is \(1/144\). Claims concern this particular observable, one lag for all stated shear strengths, and two lags only when \(k=1\).

## Proof
**Step 1: absolute Fourier reduction.** Put \(B_1(t)=\{t\}-1/2\). Its Fourier coefficients are \(\widehat B_1(m)=-1/(2\pi i m)\) when \(m\ne0\). Parseval and the unimodular action on characters give
\[
C_k(1)=\frac1{16\pi^4}\!\sum_{\substack{m,r\in\mathbb Z\\mr(r-km)(m+kr)\ne0}}
\frac1{mr(r-km)(m+kr)}.
\]
The sum is absolutely convergent: splitting the \(r\)-sum into bounded distances from the three possible resonances and their complement bounds the slice for large \(|m|\) by \(O_k((1+\log|m|)/|m|^3)\); the remaining central slices are finite. Thus rearrangement and summation by \(m\) are justified.

**Step 2: evaluate the inner arithmetic sum.** Partial fractions yield
\[
\frac1{mr(r-km)(m+kr)}
=-\frac1{k m^3r}
+\frac1{k m^3(k^2+1)(r-km)}
+\frac{k}{m^3(k^2+1)(r+m/k)}.
\]
The excluded denominators are deleted before summation. Pairing positive and negative integers and using \(\sum_{r\in\mathbb Z}(r+t)^{-1}=\pi\cot(\pi t)\) in its symmetric interpretation gives the following exact full inner sums:
\[
S_m=\begin{cases}
-\dfrac{(k^2+2)(k^4-k^2-1)}{k^2(k^2+1)^2m^4}
+\dfrac{k\pi\cot(\pi m/k)}{(k^2+1)m^3},&k\nmid m,\\[6pt]
-\dfrac{(k^2-1)(k^2+2)(2k^2+1)}{k^2(k^2+1)^2m^4},&k\mid m.
\end{cases}
\]
These expressions include the correction for the excluded pole \(r=km\) and the excluded zero of \(r+m/k\) when present; direct substitution also covers \(k=1\).

**Step 3: finish the residue sums.** The classical sums
\[
\sum_{m\ne0}m^{-4}=\frac{\pi^4}{45},\qquad
\sum_{k\nmid m}\frac{\cot(\pi m/k)}{m^3}
=\frac{\pi^3(k^2-1)(k^2-4)}{45k^3}
\]
follow by residue classes and derivatives of the cotangent identity. In the latter, use
\(\sum_{h=1}^{k-1}\csc^2(\pi h/k)=(k^2-1)/3\) and
\(\sum_{h=1}^{k-1}\csc^4(\pi h/k)=(k^4+10k^2-11)/45\).
For \(k=1\), the excluded-class sum is empty. Substituting the displayed sums for \(S_m\) and collecting terms gives exactly the rational formula in the Finding. Its numerator is zero at the single allowed integer \(k=1\) and positive otherwise. Expansion in \(k^{-1}\) proves the large-shear asymptotic.

**Step 4: exceptional second lag.** The square of \(A_1\) is \(\bigl(\begin{smallmatrix}5&3\\3&2\end{smallmatrix}\bigr)\). Partition \([0,1]^2\) by the strips \(i\le5x+3y<i+1\) and \(j\le3x+2y<j+1\); each nonempty intersection is a rational convex polygon. On it, integrate exactly the quartic polynomial
\((x-1/2)(y-1/2)(5x+3y-i-1/2)(3x+2y-j-1/2)\).
For its twelve nonzero cell integrals, the groups of four equal values are
\[
\begin{aligned}
&(i,j)=(0,0),(3,1),(4,3),(7,4):&&41/303750,\\
&(i,j)=(1,0),(1,1),(6,3),(6,4):&&-73/324000,\\
&(i,j)=(2,1),(3,2),(4,2),(5,3):&&-43/151875.
\end{aligned}
\]
Their sum is \(4(41/303750-73/324000-43/151875)=-121/81000\). Exact rational triangle integration is also independently implemented in `check.py`: fan-triangulate each clipped polygon and integrate a product of four affine forms by the barycentric simplex formula \(\int_{\Delta}\prod_{t=1}^4L_t=|\det(v_1-v_0,v_2-v_0)|\sum_{\sigma\in\{0,1,2\}^4}\prod_{a=0}^2 n_a(\sigma)!\prod_tL_t(v_{\sigma_t})/6!\).

## Verification
The self-contained `check.py` reconstructs the exact inverse-image polygonal partition, triangulates it in rational arithmetic and evaluates each polynomial moment without floating-point error. Executed successfully for fourteen integer shear strengths, matching the general closed rational formula, and independently for the exceptional two-lag map, including all twelve nonzero cell contributions. The Fourier evaluation proves the infinite parameter family; testing finitely many values alone would not.

## Relationship to prior work
Hu and Rosenhaus, *Correlation functions in linear chaotic maps* (arXiv:2204.13655, first available 2022-04-28), express the two-point correlation of products of first Bernoulli polynomials for cat maps as an infinite Fourier sum and explicitly leave its analytic evaluation open in their discussion of equation (3.20). The proof above evaluates that kind of sum for a natural full integer-shear family and explains the exceptional cancellation at the classical cat parameter. Hill, Sturman and Wilson (arXiv:2112.05463) study mixing from orthogonal shears, but do not state this observable-specific coefficient or the isolated first-lag cancellation. Classical general decay results concern a different level of quantitative information.

## Limitations
The discontinuous bilinear observable is fixed, not a classification of arbitrary observables. The two-lag value is proved at \(k=1\) only; no explicit formula for all lags is asserted. Existing general Fourier expansions provide an implicit representation but not the evaluated closed coefficient. An older potentially relevant article by Crawford and Cary (1983) was not accessible in full text; publication-priority uncertainty remains. Independent scientific validation has not been performed.

## References
- Xu-Yao Hu and Vladimir Rosenhaus, *Correlation functions in linear chaotic maps*, arXiv:2204.13655 (2022), especially equation (3.20) and its discussion.
- Joe Myers Hill, Rob Sturman and Mark C. T. Wilson, *Exponential Mixing by Orthogonal Non-Monotonic Shears*, arXiv:2112.05463 (2021).
- J. D. Crawford and J. R. Cary, *Decay of correlations in a chaotic measure-preserving transformation*, Physica D 6 (1983), 223–232, DOI:10.1016/0167-2789(83)90007-6 (full text not accessed).

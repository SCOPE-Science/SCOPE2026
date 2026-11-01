# Sharp dimension–degree frontier and infinite-sphere lift for affine Bernstein kernels

## Finding

For every integer \(d\ge2\), let \(S^d=\{x\in\mathbb R^{d+1}:\|x\|=1\}\). A continuous real function \(f:[-1,1]\to\mathbb R\) is **zonal positive definite on** \(S^d\) when every matrix \((f(x_i\cdot x_j))_{i,j=1}^M\), for every finite choice of \(x_i\in S^d\), is positive semidefinite. For every integer \(n\ge1\), set
\[
(\mathcal B_n f)(t)=\sum_{j=0}^n\binom nj
 f\!\left(-1+\frac{2j}{n}\right)
 \left(\frac{1+t}{2}\right)^j
 \left(\frac{1-t}{2}\right)^{n-j}.
\]
**Theorem (exact frontier and strengthened positive direction).** The operator \(\mathcal B_n\) maps *every* zonal positive-definite function on \(S^d\) to a zonal positive-definite function on \(S^d\) if and only if
\[
\boxed{1\le n\le d+1.}
\]
Moreover, whenever \(n\le d+1\), for every such input \(f\) there are coefficients \(a_0,\ldots,a_n\ge0\) with
\[
\boxed{(\mathcal B_n f)(t)=\sum_{k=0}^n a_k t^k.}
\]
Consequently the *same output* is positive definite on spheres of **all** dimensions, not just on \(S^d\). If \(n\ge d+2\), the positive-definite input given by the normalized Gegenbauer polynomial of degree \(n+2\) has an output with a strictly negative degree-\(n\) Gegenbauer coefficient, and preservation fails.

The new assertion is the unrestricted finite-dimensional positive direction, its nonnegative power-coefficient mechanism, and the resulting all-dimensional lift. The high-degree Gegenbauer obstruction and the \(S^2\) instance were established in preceding work and are reproduced for an integrated sharp theorem; they are not asserted to be new here.

## Assumptions and scope

All dimensions and degrees are integers with \(d\ge2\) and \(n\ge1\). Positive-definiteness always means **positive semidefiniteness** of every finite Gram matrix; strict positive-definiteness is not claimed. The input is an arbitrary continuous real zonal positive-definite function, with no differentiability, sign, monotonicity, or finite Gegenbauer-expansion assumption. The affine Bernstein nodes are the equally spaced points \(-1+2j/n\) on the dot-product interval; this is **not** the geodesic-distance Bernstein operator on \(S^1\). The claim is about preservation of the complete positive-definite cone, not approximation error for any one input.

Write \(\lambda=(d-1)/2>0\), \(C_m^\lambda\) for the classical Gegenbauer polynomial, and
\[
Q_m^{(d)}(t)=\frac{C_m^\lambda(t)}{C_m^\lambda(1)},\qquad C_m^\lambda(1)=\frac{(2\lambda)_m}{m!}.
\]
By Schoenberg's theorem, the \(Q_m^{(d)}\) are zonal positive definite, and a continuous zonal function is positive definite if and only if all its Gegenbauer coefficients are nonnegative. Here \((u)_m\) is the rising factorial. The proof uses only this classical characterization for the converse.

## Proof

**1. Hypercube restriction and nonnegative Fourier–Walsh coefficients.** Assume \(n\le d+1\). Let \(H_n=\{-1,1\}^n\) with coordinatewise multiplication, and put
\[
v_\epsilon=\frac1{\sqrt n}(\epsilon_1,\ldots,\epsilon_n,0,\ldots,0)\in S^d,
\qquad
h(\epsilon)=f\!\left(\frac1n\sum_{i=1}^n\epsilon_i\right).
\]
There are \(d+1-n\) trailing zeros. The normalized vectors satisfy
\[
v_\epsilon\cdot v_\eta=\frac1n\sum_{i=1}^n\epsilon_i\eta_i.
\]
Thus \(h(\epsilon\eta)=f(v_\epsilon\cdot v_\eta)\), and the full \(2^n\)-by-\(2^n\) group-convolution matrix \((h(\epsilon\eta))_{\epsilon,\eta\in H_n}\) is positive semidefinite by hypothesis.

For each subset \(A\subseteq\{1,\ldots,n\}\), write \(\chi_A(\epsilon)=\prod_{i\in A}\epsilon_i\). The Walsh coefficient
\[
\widehat h(A)=2^{-n}\sum_{\epsilon\in H_n}h(\epsilon)\chi_A(\epsilon)
\]
is nonnegative: the quadratic form of that positive-semidefinite convolution matrix on the real vector \((\chi_A(\epsilon))_\epsilon\) is exactly \(2^{2n}\widehat h(A)\ge0\). Fourier inversion on the Boolean group therefore yields the finite identity
\[
h(\epsilon)=\sum_{A\subseteq[n]}\widehat h(A)\chi_A(\epsilon),\qquad \widehat h(A)\ge0.
\]
This uses positivity on a *single explicitly embedded hypercube* rather than any input assumption on spheres of unbounded dimension.

**2. Bernstein sampling as an independent-sign expectation.** Fix any \(t\in[-1,1]\), and let \(Z_1,\ldots,Z_n\) be independent random signs with \(\Pr(Z_i=1)=(1+t)/2\), so \(\mathbb E Z_i=t\). If \(J\) is the number of positive signs then \(J\sim\mathrm{Binomial}(n,(1+t)/2)\), and
\[
\mathcal B_n f(t)=\mathbb E h(Z_1,\ldots,Z_n).
\]
Taking expectations in the Walsh inversion formula gives, **identically as a polynomial in \(t\)**,
\[
\mathcal B_n f(t)=\sum_{A\subseteq[n]}\widehat h(A)t^{|A|}
=\sum_{k=0}^n a_k t^k,
\qquad
 a_k=\sum_{|A|=k}\widehat h(A)\ge0.
\]
For any sphere \(S^D\), integer \(D\ge1\), the kernel \((x\cdot y)^k=\langle x^{\otimes k},y^{\otimes k}\rangle\) is positive semidefinite (with the constant kernel for \(k=0\)). Hence the nonnegative combination \(\mathcal B_n f(x\cdot y)\) is positive semidefinite on **every** \(S^D\). This proves both sufficiency and the stronger infinite-sphere lift. No limit passage or asymptotic argument is needed.

**3. Sharp obstruction at the first forbidden degree and thereafter.** Assume \(n\ge d+2\). Take \(f=Q_{n+2}^{(d)}\); this is a valid positive-definite input. Define the coefficient \([Q_n^{(d)}]p\) as the coefficient of \(Q_n^{(d)}\) in the unique finite Gegenbauer expansion of a polynomial \(p\) of degree at most \(n\). We show
\[
\boxed{
[Q_n^{(d)}] \mathcal B_n[Q_{n+2}^{(d)}]
=\frac{n!}{n^n}\,
\frac{(n+\lambda)(d+1-n)}{3n}\,
\frac{(n+1)(n+2)}{(n+d-1)(n+d)}.
}
\]
The formula is strictly negative because \(d+1-n<0\) and every other factor is positive.

For completeness, derive the coefficient independently. Set \(x_j=-1+2j/n\) and \(\Delta_n u=\sum_{j=0}^n(-1)^{n-j}\binom nj u(x_j)\). The leading monomial coefficient of \(\mathcal B_n u\) is \(2^{-n}\Delta_n u\), and \(\Delta_n\) kills all polynomials of degree below \(n\). The exact exponential-generating identity is
\[
\sum_{j=0}^n(-1)^{n-j}\binom nj e^{zx_j}
=\bigl(2\sinh(z/n)\bigr)^n
=\left(\frac{2z}{n}\right)^n
\left(1+\frac{z^2}{6n}+O(z^4)\right).
\]
Consequently
\[
2^{-n}\Delta_n(x^n)=\frac{n!}{n^n},\qquad
2^{-n}\Delta_n(x^{n+2})=\frac{n!}{n^n}\frac{(n+1)(n+2)}{6n}.
\]
Write \(L_m=[x^m]C_m^\lambda\) for the leading coefficient. The standard Gegenbauer power formula gives
\[
 L_m=\frac{2^m(\lambda)_m}{m!},
 \qquad [x^{m-2}]C_m^\lambda
 =-L_m\frac{m(m-1)}{4(m+\lambda-1)}.
\]
Only the two highest terms of \(C_{n+2}^\lambda\) survive \(\Delta_n\), so the leading power coefficient of \(\mathcal B_n[Q_{n+2}^{(d)}]\) equals
\[
\frac{n!}{n^n}\frac{L_{n+2}}{C_{n+2}^\lambda(1)}
\frac{(n+1)(n+2)(d+1-n)}{12n(n+\lambda+1)}.
\]
The leading power coefficient of \(Q_n^{(d)}\) is \(L_n/C_n^\lambda(1)\). Dividing, and using
\[
\frac{L_{n+2}}{L_n}=\frac{4(n+\lambda)(n+\lambda+1)}{(n+1)(n+2)},
\qquad
\frac{C_n^\lambda(1)}{C_{n+2}^\lambda(1)}=
\frac{(n+1)(n+2)}{(n+d-1)(n+d)},
\]
produces the boxed coefficient formula. A polynomial with a negative Gegenbauer coefficient cannot be positive definite on \(S^d\) by Schoenberg's theorem, proving necessity. The boundary case \(n=d+1\) has zero for this particular coefficient but was already proved positive for *all* inputs in Steps 1–2. Together these steps prove the exact if-and-only-if classification.

## Verification

The proof is exact and includes the complete quantifiers over continuous inputs, all finite point configurations, dimensions and degrees. The positive direction uses a finite hypercube Gram matrix, exact Walsh inversion and elementary binomial moments. The negative direction uses a finite-difference generating function and the classical Gegenbauer leading coefficients. The algebraic obstruction formula was independently checked against direct symbolic Bernstein expansion for \(2\le d\le8\) and \(1\le n\le10\). The accompanying \(\texttt{CHECK.py}\) uses exact rational arithmetic in SymPy to check the Walsh-coefficient identity and positivity for representative Gegenbauer inputs, together with the symbolic obstruction formula. In a direct run, it passed 2,298 exact assertions. Those finite checks are supplementary; the universal claim follows from the proof above.

## Relationship to prior work

Otten, Nguyen and Watts (arXiv:2608.04836, first publicly posted August 5, 2026) prove preservation of *geodesic-distance* Bernstein approximation on the circle. Their Section 4 explains the failure of the ordinary affine operator at degree four on \(S^2\), poses a higher-dimensional Bernstein-type question, and treats a **different** power-Bernstein construction when the *input* is already positive definite on \(S^\infty\). None of these conclusions gives the present low-degree preservation for **arbitrary inputs only assumed positive definite on one finite-dimensional sphere**. In fact, the power-coefficient conclusion here is stronger than merely preserving the original sphere.

A preceding mathematical finding, *A sharp degree frontier for affine Bernstein approximation of spherical positive-definite kernels* (2026), already established the complete \(S^2\) frontier and the above high-degree Gegenbauer obstruction for general \(d\). Those components are explicitly credited as prior rather than being assigned novelty here. The new result establishes the previously untreated implication \(n\le d+1\Rightarrow\mathcal B_n\) is positive-definite preserving for **every** integer \(d\ge3\), including its explicit Walsh coefficient decomposition and the all-spheres positivity lift. Standard dimension-hopping operators act on a different mapping and do not imply this finite-node Bernstein property.

The proof's hypercube restriction is a use of classical finite-group positive definiteness, rather than a claim of a new finite-group Fourier theorem. Searches for equivalent Bernstein/Gegenbauer classifications and broader positivity-preservation results found no statement that entails the complete dimension–degree frontier. These negative search outcomes are not a proof of historical uniqueness.

## Limitations

The theorem concerns only the ordinary affine Bernstein operator in the **dot-product** variable and non-strict positive definiteness. It makes no claim about geodesic Bernstein interpolation in higher dimensions, strict positive definiteness, generalized Bernstein operators, accuracy rates, or the effect of arbitrary node perturbations. It does not assert the Walsh embedding is the unique proof. Historical literature not fully indexed may contain an equivalent construction; scientific originality has not been independently audited. The small-degree mechanism applies to continuous inputs but only at the integer sphere-dimension threshold stated here.

## References

1. M. Otten, N. Nguyen, and T. W. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836 (2026), especially Section 4. First public posting: 2026-08-05. https://arxiv.org/abs/2608.04836
2. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.
3. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli 19 (2013), 1327–1349; arXiv:1111.7077. https://arxiv.org/abs/1111.7077
4. R. K. Beatson and W. zu Castell, *Dimension hopping and families of strictly positive definite zonal basis functions on spheres*, Journal of Approximation Theory 221 (2017), 22–37; arXiv:1510.08658. https://arxiv.org/abs/1510.08658
5. *A sharp degree frontier for affine Bernstein approximation of spherical positive-definite kernels*, preceding mathematical finding (2026; no external publication claimed).

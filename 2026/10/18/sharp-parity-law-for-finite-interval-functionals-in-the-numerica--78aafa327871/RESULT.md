# Sharp parity law for finite interval functionals in the numerical-radius shift norm

## Finding
Let \(T_a\) be the complex unilateral weighted shift on \(\ell^2(\mathbb N)\) with \(T_a e_j=a_j e_{j+1}\), and equip \(\ell^\infty(\mathbb N)\) with the equivalent norm \(\|a\|_w=w(T_a)\). For integers \(r,k\ge1\) set \(L_{r,k}(a)=\sum_{j=r}^{r+k-1}a_j\). Then

\[
\boxed{\|L_{r,k}\|_{(\ell^\infty,\|\cdot\|_w)^*}=2\sqrt{\left\lceil\frac{k+1}{2}\right\rceil\left\lfloor\frac{k+1}{2}\right\rfloor}=\begin{cases}k+1,&k\text{ odd},\\\sqrt{k(k+2)},&k\text{ even}.\end{cases}}
\]

The bound is attained by a finitely supported sequence. Up to multiplication by one common unimodular scalar, **the finitely supported extremizer whose weights vanish outside the specified interval and whose numerical-radius norm is one is unique**. Its exact profile is as follows. For odd \(k=2q-1\), the successive interval weights are \((2,0,2,0,\ldots,0,2)\). For even \(k=2q\), put \(\alpha=\sqrt{q/(q+1)}\); for every \(j=0,\ldots,q-1\), the two successive weights are

\[
 a_{r+2j}=\frac{2\alpha(q-j)}{q},\qquad
 a_{r+2j+1}=\frac{2\alpha(j+1)}{q}.
\]

In particular, the sharp finite-average bound is \(\sup_{\|a\|_w\le1}|k^{-1}L_{r,k}(a)|=(k+1)/k\) for odd lengths and \(\sqrt{1+2/k}\) for even lengths. For even lengths it strictly improves the uniform-vector finite-block estimate \((k+1)/k\).

## Assumptions and scope
All Banach spaces and Hilbert spaces in the theorem are complex; the same formula holds for real weight sequences because nonnegative real extremizers suffice. The index set is \(\mathbb N=\{1,2,\ldots\}\), the interval length and starting index are arbitrary positive integers, and the ambient weight sequence can be any bounded sequence, not just a finitely supported one. The numerical radius is \(w(T)=\sup_{\|x\|_2=1}|\langle Tx,x\rangle|\). Uniqueness is asserted **only among sequences vanishing outside the specified interval**, not for arbitrary ambient extensions. The rank-one case \(k=1\) is included.

## Proof
**1. A sharp candidate universal bound.** Multiplying the basis vectors successively by unit scalars gauges every complex weighted shift to its absolute-value weights, without changing numerical radius. Consequently
\[
\|a\|_w=\sup_{\substack{x_j\ge0\\\sum_j x_j^2=1}}\sum_{j\ge1}|a_j|x_jx_{j+1}.
\]
Fix an interval of \(k\) edges, and let \(N=k+1\), \(m=\lceil N/2\rceil\), \(n=\lfloor N/2\rfloor\). On its \(N\) consecutive vertices choose the unit vector with entries \(1/\sqrt{2m}\) at positions of even local parity and \(1/\sqrt{2n}\) at positions of odd local parity (and zero elsewhere). Each of these groups has exactly its indicated size, and every interval edge has product \(1/(2\sqrt{mn})\). Therefore, for every bounded weight sequence,
\[
 \|a\|_w\ge\frac{1}{2\sqrt{mn}}\sum_{j=r}^{r+k-1}|a_j|
 \ge\frac{|L_{r,k}(a)|}{2\sqrt{mn}}.
\]
This proves \(\|L_{r,k}\|\le2\sqrt{mn}\), including the exact boundary normalizations.

**2. Saturation for odd lengths.** For \(k=2q-1\), let the interval weights alternate \(2,0,2,\ldots,2\), with all outside weights zero. The symmetric matrix \(J=(T_a+T_a^*)/2\) is a direct sum of \(q\) copies of \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), plus zero isolated coordinates. Hence \(w(T_a)=\|J\|=1\) while the sum of the weights is \(2q=k+1=2\sqrt{mn}\).

**3. Saturation for even lengths.** Write \(k=2q\), \(\alpha=\sqrt{q/(q+1)}\), and define the \(2q\) positive interval weights \(c_{2j}=2\alpha(q-j)/q\) and \(c_{2j+1}=2\alpha(j+1)/q\) for \(0\le j<q\), using local edge indices \(0,\ldots,2q-1\). Set all other weights to zero. On the \(2q+1\) local vertices choose
\[
 x_{2j}=\frac1{\sqrt{2(q+1)}}\quad(0\le j\le q),\qquad
 x_{2j+1}=\frac1{\sqrt{2q}}\quad(0\le j<q).
\]
The vector \(x\) is positive and unit. For the symmetric nonnegative Jacobi matrix \(J\) whose off-diagonal entries equal \(c_i/2\), the equations \(Jx=x\) reduce, at each even vertex, to \(c_{2j-1}+c_{2j}=2\alpha\), and at each odd vertex to \(c_{2j}+c_{2j+1}=2/\alpha\), with nonexistent endpoint terms treated as zero. The displayed weights satisfy both identities, including endpoints, because \(\alpha^2=q/(q+1)\). A nonnegative symmetric matrix with a strictly positive unit eigenvector of eigenvalue one has largest eigenvalue one: for example conjugate by the positive diagonal matrix formed from \(x\) to obtain a nonnegative row-stochastic matrix. Thus \(w(T_a)=\|J\|=1\). The weight sum is
\[
\sum_{j=0}^{q-1}(c_{2j}+c_{2j+1})
=\frac{2\alpha}{q}\sum_{j=0}^{q-1}(q+1)
=2\alpha(q+1)=2\sqrt{q(q+1)}=2\sqrt{mn}.
\]
The universal bound is attained.

**4. Uniqueness on the specified support.** Suppose \(a\) is supported on this interval, \(\|a\|_w=1\), and \(|L_{r,k}(a)|=2\sqrt{mn}\). Equality in the triangle inequality makes all nonzero entries share one phase, so after common rotation we may take the interval weights nonnegative. Equality in the test-vector lower bound means the strictly positive vector \(x\) from Step 1 has Rayleigh quotient one for the real symmetric Jacobi matrix \(J\) with spectral top one. Hence \(Jx=x\). Its equation at the left endpoint determines the first edge weight uniquely; each next vertex equation determines the next weight inductively. Since the displayed odd and even profiles both satisfy the equations and achieve the bound, they are the only solutions. This includes the zero entries in the odd case and proves the asserted uniqueness.

## Verification
The accompanying `CHECK.py` reproduces the finite-dimensional eigen-equation profiles for all interval lengths from \(1\) through \(120\), using exact rational identities for the even cases and independent matrix-eigenvalue checks, and tests the universal inequality on \(2800\) seeded random finite matrices. It is supplementary finite verification: the preceding analytical argument, not the numerical tests, establishes the result for all lengths, all starting positions, and all bounded sequences. Execute from a Python environment with NumPy using `python CHECK.py`.

## Relationship to prior work
Sharif [1, Section 2, Theorem 2.1 proof, displayed inequality (10)] obtains the finite uniform-vector estimate \(\sum_{j=r}^{r+k-1}|a_j|\le(k+1)\|a\|_w\) as part of a Banach-limit asymptotic theorem. Its Section 2 Examples 2.8–2.9 identify the norm \(2\) of a single coordinate evaluation, corresponding to the first odd-length case here. The present theorem computes the **exact** norm of every consecutive finite-block sum, characterizes all finite-support equality profiles, and identifies a strict even-length improvement. The known general characterizations of weighted-shift numerical-radius contractions and determinant methods for evaluating specified weighted shifts [2,3] are compatible with this calculation but do not themselves state this sharp interval-functional law or these equality profiles. The block support is different from the periodic finite-dimensional model considered in [1, Example 1.6].

## Limitations
This is a theorem for unweighted **consecutive** coordinate sums in the numerical-radius norm of unilateral Hilbert-space weighted shifts. It does not classify arbitrary linear combinations of coordinates, nor arbitrary operator-valued shifts. The uniqueness statement excludes sequences with nonzero weights outside the interval. Literature equivalences expressed as weighted-path eigenvalue optimization may remain outside the inspected sources; independence of earlier discovery is not claimed.

## References
[1] A. Sharif, *On the numerical radius of weighted shifts on ℓ² as a norm on ℓ∞ and connections to Banach limits*, arXiv:2303.00876v1 (first public March 2, 2023); revised v2 (Aug. 3, 2023). https://arxiv.org/abs/2303.00876 and https://arxiv.org/html/2303.00876v2

[2] B. Undrakh, M.-T. Chien, H. Nakazato, A. Vandanjav, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra **30** (2015), 944–963. DOI:10.13001/1081-3810.2821.

[3] D. Chakraborty, S. Ojha, R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, Operators and Matrices **16** (2022). DOI:10.7153/oam-2022-16-75.

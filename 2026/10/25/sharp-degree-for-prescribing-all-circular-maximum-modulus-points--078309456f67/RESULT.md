# Sharp degree for prescribing all circular maximum-modulus points of an outer polynomial

## Finding

**Sharp universal angular interpolation theorem.** Fix an integer \(N\ge2\). Given an arbitrary set \(E\) of \(N\) distinct points of the unit circle \(\mathbb T=\{z\in\mathbb C:|z|=1\}\), there is a polynomial \(p\) such that
\[
\deg p=N+1,\qquad p(0)>0,\qquad p'(0)\ne0,\qquad p(z)\ne0\quad(|z|\le1),
\]
and such that its *entire set* of maximizers of boundary modulus is exactly
\[
\bigl\{z\in\mathbb T:|p(z)|=\max_{|w|=1}|p(w)|\bigr\}=E.
\]
Moreover, the degree \(N+1\) is the best possible **uniform** bound for the class of zero-free polynomials with nonzero linear coefficient: if \(E\) is the set of vertices of a rotated regular \(N\)-gon, no polynomial of degree at most \(N\) satisfying the same three conditions can have precisely \(E\) as its circle-maximizer set.

In particular, a zero-free polynomial with first nonconstant Taylor term of order one can have arbitrarily many specified maximum-modulus points on a *single* circle, but achieving arbitrary angular configurations with these requirements has a sharp worst-case degree cost.

## Assumptions and scope

No angular-separation or arithmetic restrictions are imposed on the distinct points of \(E\). The polynomial coefficients may be complex, and the construction is existential via an outer Fejér–Riesz factor. A polynomial is called *outer* here if it has no zeros in the open unit disk; the constructed polynomial has the stronger property of having no zeros even on its boundary. The degree-optimality statement is a **worst-case** statement, witnessed by each rotated regular polygon, not a claim that every configuration requires degree \(N+1\).

This theorem concerns prescribed maxima on the circle of radius one and no other radii. Rescaling the argument produces an analogous result on any prescribed positive radius. No claim is made about the connected components of the full global maximum-modulus set away from that circle.

## Proof

**Step 1: A nonnegative trigonometric polynomial with precisely the required zeros and a nonzero first Fourier coefficient.** Write
\[
Q(z)=\prod_{\xi\in E}(z-\xi)=\sum_{j=0}^Nq_jz^j.
\]
Because \(E\subset\mathbb T\), both \(q_0\) and \(q_N\) are nonzero. Let
\[
G(z)=|Q(z)|^2=\sum_{k=-N}^{N}h_kz^k\quad(|z|=1),
\qquad h_k=\sum_{j=0}^{N-k}q_{j+k}\overline{q_j}\quad(0\le k\le N).
\]
Here \(h_{-k}=\overline{h_k}\) and \(h_0=\sum_{j=0}^N|q_j|^2\). By Cauchy–Schwarz and the nonzero endpoint coefficients,
\[
|h_2|\le\Bigl(\sum_{j=2}^N|q_j|^2\Bigr)^{1/2}
\Bigl(\sum_{j=0}^{N-2}|q_j|^2\Bigr)^{1/2}<h_0.
\]
Hence \(h_0+h_2\ne0\). Select \(\varepsilon\in\{1/4,-1/4\}\) so that
\[
H_1:=h_1+\varepsilon(h_0+h_2)\ne0.
\]
At most one of the two choices could make this expression zero. The circle function
\[
H(z)=(1+\varepsilon z+\varepsilon z^{-1})|Q(z)|^2\quad(|z|=1)
\]
is nonnegative, vanishes exactly on \(E\), and has strictly positive prefactor \(1+2\varepsilon\operatorname{Re}z\ge1/2\). Its Fourier coefficient at frequency one is \(H_1\ne0\), and its top positive coefficient at frequency \(N+1\) is \(\varepsilon q_N\overline{q_0}\ne0\). Thus its exact trigonometric degree is \(N+1\).

**Step 2: Strict positive spectral factorization.** Choose a real number \(M>\max_{|z|=1}H(z)\) and put
\[
T_M(z)=M-H(z)>0\qquad(|z|=1).
\]
The classical Fejér–Riesz theorem gives a polynomial \(p_M\) of degree at most \(N+1\) such that \(|p_M(z)|^2=T_M(z)\) on \(\mathbb T\). Since \(T_M\) is strictly positive, choose the *outer* spectral factor: for every reciprocal-conjugate pair of roots of the polynomial obtained from \(z^{N+1}T_M(z)\), take the root outside the closed unit disk. In this way \(p_M\) is zero-free for \(|z|\le1\). Its degree is exactly \(N+1\), because the top Fourier coefficient of \(|p_M|^2\) equals the product of its leading coefficient with the conjugate of its nonzero constant coefficient and must equal the nonzero top Fourier coefficient of \(T_M\). Multiply by a constant of modulus one to ensure \(p_M(0)>0\).

The identity \(|p_M|^2=M-H\) says that \(|p_M|^2\) reaches its largest value \(M\) exactly at the zeros of \(H\), namely the set \(E\).

**Step 3: Force the first coefficient to be nonzero.** Because \(p_M\) has no zeros in the closed disk, its analytic logarithm has a Taylor expansion around zero. Taking the first positive Fourier coefficient on the boundary of
\(\log |p_M|^2=\log T_M\) gives the exact identity
\[
\frac{p_M'(0)}{p_M(0)}=\frac{1}{2\pi}\int_{0}^{2\pi}
\log(M-H(e^{it}))e^{-it}\,dt.
\]
For large \(M\), the uniformly convergent expansion of the real logarithm yields
\[
\frac{p_M'(0)}{p_M(0)}=-\frac{H_1}{M}+O(M^{-2}).
\]
Since \(H_1\ne0\), the derivative \(p_M'(0)\) is nonzero for every sufficiently large \(M\). Choose such an \(M\) to complete existence.

**Step 4: The regular-polygon lower bound.** Let \(E=\{z\in\mathbb T:z^N=\omega\}\) for a fixed \(\omega\in\mathbb T\). Suppose a polynomial \(p\) has exact circle maximum set \(E\), is zero-free on \(|z|\le1\), and has \(p'(0)\ne0\). Put
\[
S(z)=M-|p(z)|^2\quad(|z|=1),\qquad M=\max_{|z|=1}|p(z)|^2.
\]
The real nonnegative trigonometric polynomial \(S\) is not identically zero, since otherwise \(|p|\) would be constant and every point of the circle would maximize it. Every root in \(E\) has even multiplicity in the real angular variable. If \(d=\deg p\), then \(z^dS(z)\) is an ordinary polynomial of degree at most \(2d\). Thus its \(N\) distinct boundary roots, each of multiplicity at least two, force \(d\ge N\).

If \(d=N\), equality of the degree bound forces the Laurent-polynomial identity
\[
S(z)=C|z^N-\omega|^2\qquad(z\in\mathbb T)
\]
for some \(C>0\). Since \(p\) has no boundary zeros, \(S\) cannot attain \(M\), and therefore \(M>4C\). Choose unique real numbers \(a>b>0\) with \(a^2+b^2=M-2C\) and \(ab=C\). Then
\[
|p(z)|^2=M-C|z^N-\omega|^2=|a+b\overline\omega z^N|^2
\qquad(z\in\mathbb T).
\]
The binomial \(B(z)=a+b\overline\omega z^N\) is zero-free on the closed disk. So are \(p\) and \(1/p\) there. Consequently \(p/B\) and \(B/p\) are holomorphic in the disk, continuous on its closure and have boundary modulus one. Applying the maximum-modulus principle to both ratios shows \(p/B\) is a constant of modulus one. But \(N\ge2\) implies \(B'(0)=0\), so \(p'(0)=0\), contradiction. Thus \(d\ge N+1\), and Step 2 attains equality.

## Verification

A standalone supplementary script, `verify.py`, computes polynomial coefficients, forms the positive trigonometric polynomial, selects outside-disk roots of its spectral Laurent polynomial, reconstructs a zero-free factor numerically, and compares the boundary modulus identity. Four separate configurations of sizes two, three, three and four passed; these include a regular polygon and irregular angular positions. It also confirms a nonzero linear coefficient and the selected root positions. Its execution prints `VERIFY_OK numerical spectral factors for four independent patterns`.

The finite floating-point checks are **not** proofs of either the all-configuration existence theorem or the degree lower bound. Those follow from the exact analytic Steps 1–4. The script assumes NumPy; no precomputed certificate is required.

## Relationship to prior work

The recent maximum-modulus exceptional-circle example of Yunpeng Li gives arbitrary multiplicities for a particular regular angular pattern, via an exponential of a polynomial, while its principal theorem controls multiplicity away from isolated exceptional radii. The result here instead interpolates **any** finite set of angles on one circle using a zero-free polynomial of exact sharp *uniform* degree and with nonzero first derivative. The interpolation of Pardo-Simón and Sixsmith (2026) concerns points on **pairwise distinct radii**, and their polynomial construction (2021/2022) concerns features of the full maximum-modulus set at specified **distinct positive radii**. Neither gives the same-circle sharp-degree statement. Classical Fejér–Riesz factorization is the essential existing ingredient, but the nonzero first-coefficient perturbation and the extremal regular-polygon obstruction are the deductions established here.

## Limitations

The minimum degree may be smaller for special nonregular configurations; no pointwise degree classification is asserted. The result does not prescribe boundary values of the polynomial, does not imply any lower bound on the separation between maximizers, and does not control maximum-modulus points off the selected circle. The theorem is reviewed analytically in the present manuscript but has not received an independent mathematical audit. An abstract-only 2025 paper on complex polynomial maximum modulus remains an acknowledged bibliographic coverage risk.

## References

1. Yunpeng Li, *Maximum-modulus points on concentric circles*, arXiv:2610.15067v1 (first posted 2026-10-10), especially Section 4, Example 4.2.
2. L. Pardo-Simón and D. J. Sixsmith, *A finite-order answer to a problem of Erdős on maximum modulus points*, arXiv:2607.09462v1 (2026), introduction and interpolation theorem.
3. L. Pardo-Simón and D. J. Sixsmith, *The Maximum Modulus Set of a Polynomial*, Computational Methods and Function Theory **22** (2022), 207–214, DOI: 10.1007/s40315-021-00368-7, Theorems 1.2 and 1.3 and proofs.
4. Fejér–Riesz spectral factorization (classical); for a modern discussion see T. T. Georgiou and A. Lindquist, *On a Fejer-Riesz factorization of generalized trigonometric polynomials*, arXiv:2005.11920 (2020).
5. G. J. O. Jameson, *The maximum modulus of a complex polynomial on the unit circle*, Mathematical Gazette **109** (2025), 119–123, DOI: 10.1017/mag.2025.17 (only the publicly accessible extract checked; full text unavailable).

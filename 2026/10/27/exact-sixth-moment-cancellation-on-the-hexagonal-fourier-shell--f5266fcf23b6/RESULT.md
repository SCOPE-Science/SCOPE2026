# Exact sixth-moment cancellation on the hexagonal Fourier shell

## Finding

Let \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\) have probability Haar measure, and let the ordered six-point frequency shell be
\[
\Lambda=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)).
\]
For every six complex coefficients \(c_0,\ldots,c_5\) with \(|c_j|=1\), set
\[
P_c(t)=\sum_{j=0}^{5}c_j e^{i\langle\Lambda_j,t\rangle},\qquad M_6(c)=\int_{\mathbb T^2}|P_c(t)|^6\,dt.
\]
The *exact phase-only sixth-moment range* is
\[
\boxed{546\le M_6(c)\le2040}.
\]
Every value in this interval occurs, by continuity and connectedness of the coefficient phase torus. Both bounds are sharp, and all equality cases are classified below.

There is a unique multiplication by a global unimodular constant and a torus character \(e^{i\langle \Lambda_j,t_0\rangle}\) making the first three coefficients equal to \(1\). Denote the remaining coefficients in this gauge by \(u,v,w\in\mathbb S^1\), and put
\[
Q=\left|1+\frac uv+\frac wv\right|^2,\qquad h=\frac{uw}{v}.
\]
The following *global exact stability identities* hold:
\[
\boxed{M_6(c)-546=126Q+9(1+Q)|1+h|^2},
\]
\[
\boxed{2040-M_6(c)=162(9-Q)+9(1+Q)|1-h|^2}.
\]
In particular the lower equality cases, after this gauge fixing, are exactly
\[
(u,v,w)=(-\omega,-1,-\omega^2)\quad\text{or}\quad(-\omega^2,-1,-\omega),
\qquad\omega=e^{2\pi i/3}.
\]
The upper equality case is uniquely \((u,v,w)=(1,1,1)\). Thus the lower endpoint has exactly two phase-modulation orbits and the upper endpoint one.

If in addition all original coefficients are \(q\)-th roots of unity for an integer \(q\ge1\), then the lower endpoint \(546\) is attainable **if and only if** \(6\mid q\); when so, exactly \(2q^3\) coefficient six-tuples attain it. The upper endpoint \(2040\) is attainable for every \(q\), by exactly \(q^3\) six-tuples.

## Assumptions and scope

The six frequencies form the smallest nonzero shell \(x^2+xy+y^2=1\) of the triangular (Eisenstein) frequency lattice \(\mathbb Z^2\). The exponent \(6\) refers to the sixth power of the absolute value. No coefficient magnitude is optimized: all six magnitudes are fixed to one. Integration is over the **continuous** two-torus with mass one; no finite-grid aliasing is assumed. The integer \(q\) applies only to the optional phase-alphabet consequence.

## Proof

**1. Unique phase-modulation gauge.** Multiplying the coefficient \(c_j\) by \(\lambda e^{i\langle\Lambda_j,t_0\rangle}\) does not change its magnitude, and translates the polynomial up to a global unimodular factor. The integer matrix with rows \((1,\Lambda_j)\) for \(j=0,1,2\) is
\[
B=\begin{pmatrix}1&1&0\\1&0&1\\1&-1&1\end{pmatrix},\qquad\det B=1.
\]
It is consequently an automorphism of the three-dimensional phase torus and makes the first three coefficients uniquely equal to \(1\). Since \(B^{-1}\) is integral, the same operation stays inside the \(q\)-th-root phase alphabet when the original coefficients do.

**2. Exact sixth moment.** Fourier orthogonality gives the completely finite identity
\[
M_6(c)=\sum_{s\in\mathbb Z^2}\left|\sum_{i,j,k:\,\Lambda_i+\Lambda_j+\Lambda_k=s}c_ic_jc_k\right|^2.
\]
There are exactly \(37\) different triple sums. In the gauge \((1,1,1,u,v,w)\), straightforward grouping of the ordered triples and their conjugates gives
\[
\begin{aligned}
M_6={}&996+288\operatorname{Re}(u/v+v/w+u/w)+72\operatorname{Re}(uw/v)\\
&+18\operatorname{Re}(w+u+v/w^2+uw^2/v^2+u^2w/v^2+u^2/v).
\end{aligned}
\]
This expansion can also be reproduced independently by the standalone exact symbolic checker `verify.py`, which enumerates all \(216\) ordered triples and groups them by their vector sum.

**3. Factorization and both endpoints.** Write \(r=u/v\), \(s=w/v\), so \(|r|=|s|=1\), and set \(z=1+r+s\). The elementary identities
\[
3+2\operatorname{Re}(r+s+r/s)=|z|^2,
\]
\[
r+s+r^2+s^2+rs^2+r^2s+4rs=rs(1+|z|^2)
\]
follow from \(rs\overline z=r+s+rs\). Substitution yields
\[
M_6=564+144|z|^2+18(1+|z|^2)\operatorname{Re}(vrs).
\]
Since \(vrs=h\) and \(|h|=1\), rewriting \(\operatorname{Re}h\) in terms of \(|1\pm h|^2\) proves the two boxed deficit identities. Their nonnegative terms prove both endpoint inequalities using \(0\le Q\le9\).

**4. All equality cases.** The lower deficit vanishes precisely when \(z=0\) and \(h=-1\). Three unit complex numbers \(1,r,s\) sum to zero if and only if \(\{r,s\}=\{\omega,\omega^2\}\). Thus \(rs=1\), \(v=-1\), and \((u,w)=(-\omega,-\omega^2)\) in either order. Conversely these two triples satisfy the exact deficit. The upper deficit vanishes precisely when \(|z|=3\) and \(h=1\). Equality in the triangle inequality gives \(r=s=1\); then \(v=1\), so \(u=v=w=1\). Gauge uniqueness proves no further orbits exist.

**5. Root-of-unity phases and orbit counts.** The gauge map is an automorphism of \((\mu_q)^6\) under the free action of \((\mu_q)^3\), because \(\det B=1\). The two lower-gauge triples require primitive sixth roots \(-\omega\), \(-\omega^2\), so they belong to \((\mu_q)^3\) exactly when \(6\mid q\). Each of the two representatives then has \(q^3\) preimages; the upper representative has \(q^3\). All are distinct since the gauge action is free.

## Verification

Run `python verify.py` from the directory containing this file. The checker enumerates triple-frequency coincidences independently of the displayed formula, compares the resulting Laurent polynomial exactly to the factored identity, checks both equality representatives and the integer gauge determinant, and cross-checks three moments using nonaliasing \(31\times31\) Fourier quadrature. It prints a `PASS` line on success. The exact algebraic computation checks the finite enumeration; the universal optimization and equality classification are the analytical arguments above.

## Relationship to prior work

Mudgal's *Additive energies on spheres* (arXiv:2105.06925, initial posting 14 May 2021) studies higher additive energies and restriction-type upper estimates for lattice sets on spheres in dimensions three and four. Its framework explains the mathematical motivation for triple-sum multiplicities, but its estimates do not supply an exact **minimum over six complex coefficient phases** on this two-dimensional shell.

Ciccone and Gonçalves, *Sharp Fourier Extension on the Circle under arithmetic constraints* (arXiv:2208.09441, initial posting 19 August 2022), establish a sharp Euclidean Fourier extension **upper** inequality for circle data with certain one-dimensional Fourier supports. Their extension operator from circular surface measure to \(\mathbb R^2\), integral norm, assumptions and objective differ from the periodic \(\mathbb T^2\) phase-only **lower** moment calculated here; the sixth-root phase cancellation is not a corollary of their theorem.

Related calculations for the triangular six-point *degree-two aperture* concern a different six-frequency subset, whose convex hull is a triangle rather than a centrally symmetric hexagon, and a different (fourth) Fourier moment. Neither an invertible affine frequency map nor the cited fourth-moment result implies this sixth-moment identity.

## Limitations

The theorem concerns this exact six-frequency shell and unit-modulus coefficients. It does not claim unrestricted \(\ell^2\)-to-\(L^6\) optimization, higher Eisenstein shells, finite torus sampling with possible aliasing, or a universal criterion for arbitrary frequency configurations. Algebraic novelty is supported by targeted literature and indexed-result comparisons but is not an independent bibliographic certification; older equivalent formulas may exist.

## References

1. A. Mudgal, *Additive energies on spheres*, arXiv:2105.06925 (v1, 2021-05-14); Journal of the London Mathematical Society 106 (2022), 2927–2958. https://arxiv.org/abs/2105.06925 .
2. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle under arithmetic constraints*, arXiv:2208.09441 (v1, 2022-08-19). https://arxiv.org/html/2208.09441v2 .

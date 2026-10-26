# A reentrant degree-six interpolation defect on the regular truncated tetrahedron

## Finding

Let \(X\subset S^2\) be the twelve vertices of the regular truncated tetrahedron, realized as
\[
X=\left\{\frac{(\varepsilon_1a_1,\varepsilon_2a_2,\varepsilon_3a_3)}{\sqrt{11}}:
(a_1,a_2,a_3)\in\{(3,1,1),(1,3,1),(1,1,3)\},\quad
\varepsilon_i\in\{-1,1\},\quad \varepsilon_1\varepsilon_2\varepsilon_3=1\right\}.
\]
For each integer \(\ell\ge0\), let \(\mathcal H_\ell\) be the real spherical harmonics of **exact** degree \(\ell\) on \(S^2\), and let \(E_\ell:\mathcal H_\ell\to\mathbb R^X\) evaluate functions at the twelve vertices. Then
\[
\boxed{\operatorname{rank}E_\ell=
\begin{cases}
2\ell+1,&0\le\ell\le5,\\
9,&\ell=6,\\
12,&\ell\ge7.
\end{cases}}
\]
In particular, exact-degree interpolation first becomes surjective at degree \(7\), and remains surjective in **every** higher degree; degree \(6\) has a three-dimensional data obstruction, even though degree \(5\) has rank \(11\). The sharp persistent interpolation threshold is \(7\).

The rank-six defect is tied to the uniform truncation. Replace the coordinate \(3\) above by any real parameter \(a>1\), replace \(\sqrt{11}\) by \(\sqrt{a^2+2}\), and call the resulting orbit \(X_a\). There exists \(\epsilon>0\) such that, for \(0<|a-3|<\epsilon\), the degree-six evaluation map on \(X_a\) **is** surjective. Thus the degree-six failure at the regular member is an isolated geometric resonance, not a generic dimensional obstruction. This statement makes no assertion about all other values of \(a\).

## Assumptions and scope

The twelve vertices are ordered first by the position \(j=1,2,3\) of the distinguished coordinate, then by the lexicographic signs \((-,-,+),(-,+,-),(+,-,-),(+,+,+)\). The orbit at \(a=3\) has its four off-diagonal inner products and multiplicities, from any fixed vertex, equal to
\[
-\frac9{11}\ (2\text{ times}),\qquad
-\frac5{11}\ (2\text{ times}),\qquad
-\frac1{11}\ (4\text{ times}),\qquad
\frac7{11}\ (3\text{ times}).
\]
The equalities of the relevant edge inner products \((a^2-2)/(a^2+2)\) and \((2a+1)/(a^2+2)\) occur at the unique parameter \(a=3\) among \(a>1\), where the tetrahedrally symmetric orbit is the Archimedean uniform truncated tetrahedron. The result concerns real exact-degree spherical harmonics, not cumulative degree-at-most polynomial interpolation, cubature precision, or noisy numerical conditioning.

## Proof

**Addition theorem.** Write \(P_\ell\) for the Legendre polynomial with \(P_\ell(1)=1\). The spherical addition formula identifies the positive-semidefinite matrix
\[
G_\ell=\big(P_\ell(u\cdot v)\big)_{u,v\in X}
=\frac{4\pi}{2\ell+1}E_\ell E_\ell^{\mathsf T}
\]
for orthonormal real spherical harmonics. Consequently \(\operatorname{rank}G_\ell=\operatorname{rank}E_\ell\). All matrix entries are rational and can be computed exactly from the displayed dot products and the recurrence
\[
(\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t),
\quad P_0(t)=1,\quad P_1(t)=t.
\]

**The exceptional low degrees.** Over \(\mathbb F_{1000000007}\), whose characteristic does not divide any denominator occurring in the recurrence through degree \(324\), exact Gaussian elimination on \(G_\ell\), for \(0\le\ell\le6\), gives respective ranks
\[
1,\ 3,\ 5,\ 7,\ 9,\ 11,\ 9.
\]
A nonzero minor modulo the stated prime is a nonzero rational minor. For \(0\le\ell\le5\), the universal harmonic dimension \(\dim\mathcal H_\ell=2\ell+1\) provides the matching upper bound. For \(\ell=6\), the three following independent integer vectors, in the vertex ordering specified above, are **exact rational** null vectors of \(G_6\):
\[
\begin{aligned}
w_1&=(-1,1,1,-1,1,-1,-1,1,0,0,0,0),\\
w_2&=(-1,1,0,0,1,0,-1,0,0,-1,1,0),\\
w_3&=(0,0,1,-1,1,0,-1,0,-1,0,0,1).
\end{aligned}
\]
Exact substitution into \(P_6\) proves \(G_6w_i=0\); hence rank is at most \(9\), while its modular rank supplies the matching lower bound. These are the three independent degree-six linear restrictions on possible vertex data.

**All degrees from seven through 324.** The file `verify.py`, requiring only the Python standard library, constructs all twelve vertices, evaluates the Legendre recurrence in the field \(\mathbb F_{1000000007}\), and performs exact elimination for every integer \(7\le\ell\le324\). It asserts rank \(12\) in each case and returns a SHA-256 checksum for its 325-element rank sequence. Since the computed determinants are nonzero in a field, the rational Gram matrices are nonsingular in those degrees. This is a *finite exhaustive* check only of the explicitly bounded interval.

**Every degree at least 325.** We give an analytic bound independent of any finite enumeration. The elementary Laplace integral for Legendre polynomials, with \(x=\cos\theta\in(-1,1)\), reads
\[
P_\ell(\cos\theta)=\frac1\pi\int_0^\pi
\big(\cos\theta+i\sin\theta\cos\phi\big)^\ell\,d\phi.
\]
Using \(|\cos\theta+i\sin\theta\cos\phi|^2=1-\sin^2\theta\sin^2\phi\), the bound \(1-u\le e^{-u}\), and \(\sin\phi\ge2\min\{\phi,\pi-\phi\}/\pi\), one obtains for every integer \(\ell\ge1\)
\[
|P_\ell(x)|\le \frac1\pi\int_0^\pi e^{-\ell(1-x^2)\sin^2\phi/2}\,d\phi
\le\sqrt{\frac{\pi}{2\ell}}\frac1{\sqrt{1-x^2}}.
\]
For the four off-diagonal inner products, the lower bounds on \(\sqrt{1-x^2}\) are, respectively, \(57/100,89/100,99/100,77/100\); each is verified by squaring rational numbers. The weighted reciprocal sum is strictly smaller than
\[
\frac{200}{57}+\frac{200}{89}+\frac{400}{99}+\frac{300}{77}
=\frac{1458700}{106533}<14.
\]
The classical rational bound \(\pi<22/7\) yields \(\sqrt{\pi/2}<9/7\). Hence the sum of the absolute off-diagonal entries in each row of \(G_\ell\) is strictly less than \(18/\sqrt\ell<1\) whenever \(\ell\ge325\). Since every diagonal entry equals \(1\), strict diagonal dominance makes \(G_\ell\) positive definite for all such \(\ell\). Together with the finite certificate this proves the complete infinite-degree classification.

**Isolation under nonuniform truncation.** For \(a>1\), every entry of \(G_6(a)\) is a rational function of \(a\) with denominator a power of \(a^2+2\), hence its determinant is a rational function. The same exact modular checker finds rank \(12\) for \(a=2\), proving its numerator is not identically zero. Therefore it has only finitely many real zeros. Because the just-proved null vectors show it vanishes at \(a=3\), that zero is isolated. In a sufficiently small punctured neighborhood of \(a=3\) no other zero occurs, proving the deformation statement.

## Verification

Run `python3 verify.py`. The program checks primality of the modulus, unique vertex construction, all low-degree modular ranks, all 318 complete-rank degrees from \(7\) to \(324\), all three exact rational null-vector identities at degree \(6\), and nonsingularity of the deformed degree-six matrix at \(a=2\). It also checks the rational lower bounds used in the analytic large-degree step. No floating-point matrix rank test is used. The expected deterministic summary is reproduced in `certificate.json`. The large-degree step is an analytic argument, not a claim inferred from the code.

## Relationship to prior work

The 12-state truncated-tetrahedral spin configuration appears explicitly in Krčmár, Gendiar and Nishino (first public preprint 30 December 2015; their Section II and Table I), whose investigation concerns a phase diagram rather than exact-degree spherical-harmonic interpolation. General spherical interpolation and cubature research, including An–Chen–Sloan–Womersley and Zhou–Chen, examines fundamental polynomial spaces and well-conditioned designs, but does not, in the portions checked, give the displayed fixed-degree rank sequence. Misner's cubic-grid harmonic extraction is a different discretization problem. This result is not a reclassification of lower-degree cubature accuracy: it isolates a nonmonotone rank loss at an exact harmonic degree, with a sharp persistent recovery and a local geometric resonance.

## Limitations

The result is for one natural twelve-point spherical orbit. It supplies no quantitative condition-number bounds, noise stability, all-parameter classification of \(X_a\), or results on spin-model phase transitions. Although primary literature and mathematical-record searches were compared, unindexed equivalent calculations remain possible. The modular finite certificate must be rerun from the embedded file; it is not an external or independent mathematical audit.

## References

1. R. Krčmár, A. Gendiar, T. Nishino, *Phase diagram of truncated tetrahedral model*, arXiv:1512.09059 (first version 30 December 2015), especially Section II and Table I. https://arxiv.org/abs/1512.09059
2. C. An, X. Chen, I. H. Sloan, R. S. Womersley, *Well conditioned spherical designs for integration and interpolation on the two-sphere*, SIAM J. Numer. Anal. 48 (2010), 2135–2157, DOI 10.1137/100795140.
3. Y. Zhou, X. Chen, *Spherical \(t_\epsilon\)-designs for approximations on the sphere*, arXiv:1502.03562 (12 February 2015). https://arxiv.org/abs/1502.03562
4. C. W. Misner, *Spherical harmonic decomposition on a cubic grid*, arXiv:gr-qc/9910044 (12 October 1999). https://arxiv.org/abs/gr-qc/9910044

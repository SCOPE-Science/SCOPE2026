# Least-common-multiple resonance in the excluded area of rotated regular polygons

## Finding
For every pair of integers \(n,m\ge3\), positive circumradii \(r,s\), and relative orientation \(\theta\in\mathbb R\), the excluded area of two planar regular polygons is an **exact folded-cosine wave**. Let
\[
\begin{gathered}
g=\gcd(n,m),\qquad L=\operatorname{lcm}(n,m)=nm/g,\qquad a=\pi/L,\\
N=n/g,\qquad
A_{n,m}=\frac{nr^2}{2}\sin\frac{2\pi}{n}+\frac{ms^2}{2}\sin\frac{2\pi}{m},\\
B_{n,m}=\frac{grs\sin(\pi/n)\sin(\pi/m)}{\sin a},\\
\delta(\theta)=\operatorname{dist}\!\left(\frac\pi n-\pi-\theta-(N-1)a,\;2a\mathbb Z\right)\in[0,a].
\end{gathered}
\]
Then, exactly,
\[
\boxed{E_{n,m}(\theta)=A_{n,m}+2B_{n,m}\cos\delta(\theta).}
\]
There are precisely \(L\) equally spaced maxima and \(L\) equally spaced minima modulo \(2\pi\). Their sharp difference is \(2B_{n,m}(1-\cos a)\).

If \(\Theta\) is uniform on \([0,2\pi)\), then \(\delta(\Theta)\) is uniform on \([0,a]\). Consequently, writing \(E=E_{n,m}(\Theta)\), for \(A_{n,m}+2B_{n,m}\cos a\le z\le A_{n,m}+2B_{n,m}\),
\[
\begin{aligned}
\mathbb P(E\le z)&=1-\frac1a\arccos\!\left(\frac{z-A_{n,m}}{2B_{n,m}}\right),\\
\mathbb E E&=A_{n,m}+\frac{2B_{n,m}\sin a}{a}
=A_{n,m}+\frac{\operatorname{per}(P_n(r))\operatorname{per}(P_m(s))}{2\pi},\\
\operatorname{Var}(E)&=4B_{n,m}^2\left[\frac12+\frac{\sin(2a)}{4a}-\left(\frac{\sin a}{a}\right)^2\right].
\end{aligned}
\]
The distribution function is zero below the displayed interval and one above it.

For the additional fixed-area normalization \(\operatorname{area}(P_n(r))=\operatorname{area}(P_m(s))=A_0>0\), let both \(n,m\to\infty\), without any restriction on their relative growth. Then
\[
\frac{L^2}{A_0}\bigl(E_{\max}-E_{\min}\bigr)\longrightarrow\pi^2,\qquad
\frac{L^4}{A_0^2}\operatorname{Var}(E)\longrightarrow\frac{4\pi^4}{45}.
\]
Also \((E-E_{\min})/(E_{\max}-E_{\min})\) converges in distribution to \(1-U^2\), for \(U\) uniform on \([0,1]\). In particular, along pairs with \(n=m=k\), the angular range decays like \(A_0\pi^2/k^2\); along consecutive orders \(n=k,m=k+1\) it decays like \(A_0\pi^2/k^4\).

## Assumptions and scope
The regular polygon \(P_n(r)\subset\mathbb R^2\) has vertices \(r(\cos(2\pi j/n),\sin(2\pi j/n))\) for integers \(0\le j<n\). The polygon \(P_m(s)\) is defined analogously. Let \(R_\theta\) be counterclockwise rotation and let the **excluded area** be
\[
E_{n,m}(\theta)=\operatorname{area}\bigl(P_n(r)+(-R_\theta P_m(s))\bigr).
\]
The Minkowski sum here is the locus of disallowed relative translation vectors for nonoverlapping placements with fixed orientations. All areas are Euclidean, the circumradii are positive, and \(\operatorname{dist}(x,2a\mathbb Z)=\min_{k\in\mathbb Z}|x-2ak|\). The formulas are identities for every angle, including orientation values at which the polygonal normal fans share rays.

## Proof
**Step 1 (mixed-area identity).** For planar convex polygons \(P,Q\), the planar mixed-area formula, obtained by summing the support-height contribution of each edge of \(P\), is
\[
\operatorname{area}(P+Q)=\operatorname{area}(P)+\operatorname{area}(Q)
+\sum_{e\text{ edge of }P}|e|\,h_Q(\nu_e),
\]
where \(\nu_e\) is the outer unit normal. This remains valid when either polygon's edges are parallel to the other's. Every edge of \(P_n(r)\) has length \(2r\sin(\pi/n)\), and its normal angle is \(\pi/n+2\pi i/n\), with \(0\le i<n\). For \(Q=-R_\theta P_m(s)\), rotational symmetry gives
\[
h_Q(t)=s\cos\operatorname{dist}\bigl(t-\theta-\pi,(2\pi/m)\mathbb Z\bigr).
\]
Set \(\gamma=\pi/n-\theta-\pi\). The cross term is therefore
\[
2rs\sin\frac\pi n\sum_{i=0}^{n-1}
\cos\operatorname{dist}\!\left(\gamma+\frac{2\pi i}{n},\frac{2\pi}{m}\mathbb Z\right).
\]

**Step 2 (the arithmetic resonance).** Put \(M=m/g\) and \(N=n/g\), so \(\gcd(M,N)=1\) and \(2\pi/n=2aM\). Modulo \(2\pi/m=2Na\), the \(n\) normal angles consist of \(g\) copies of the \(N\) equally spaced residues \(\gamma+2aj\), for \(0\le j<N\). Choose \(t\in[-a,a]\) congruent to \(\gamma+(N-1)a\) modulo \(2a\). Representatives of these \(N\) residues in \([-Na,Na]\) are, as a multiset,
\[
t+(2j-N+1)a,\qquad 0\le j<N.
\]
Their absolute values do not exceed \(Na=\pi/m\), so these are precisely the nearest-angle representatives of the support function. The trigonometric progression gives
\[
\sum_{j=0}^{N-1}\cos\bigl(t+(2j-N+1)a\bigr)
=\frac{\sin(Na)}{\sin a}\cos t
=\frac{\sin(\pi/m)}{\sin a}\cos t.
\]
Because \(\gamma+(N-1)a\) and \(\gamma-(N-1)a\) differ by an integral multiple of \(2a\), \(|t|=\delta(\theta)\). Substitution into Step 1 proves the exact profile with the stated coefficient \(B_{n,m}\). Positivity of \(B_{n,m}\) and strict decrease of cosine on \([0,a]\), with \(0<a\le\pi/3\), prove both sharp endpoints and their multiplicities.

**Step 3 (uniform-angle law).** The map \(\theta\mapsto\delta(\theta)\) folds each period of length \(2a\) onto \([0,a]\), giving the uniform law for \(\delta\) when \(\theta\) is Haar-uniform. Applying the strictly decreasing cosine and integrating \(\cos t\) and \(\cos^2t\) over \([0,a]\) proves the distribution and moments. Since \(gL=nm\), and the perimeters are \(2nr\sin(\pi/n)\) and \(2ms\sin(\pi/m)\), the mean simplifies to the classical kinematic mean displayed above.

**Step 4 (asymptotic arithmetic contrast).** Equal area \(A_0\) fixes the radii by \(r^2=A_0/[n\sin(\pi/n)\cos(\pi/n)]\), and similarly for \(s\). Hence
\[
\frac{B_{n,m}}{A_0}
=\frac{g}{\sin(\pi/L)}\sqrt{\frac{\tan(\pi/n)\tan(\pi/m)}{nm}}
\longrightarrow1
\quad(n,m\to\infty).
\]
Taylor expansion yields \(2B(1-\cos a)=Ba^2+O(Ba^4)\). With \(\delta=aU\), the centered variation has leading term \(-Ba^2(U^2-1/3)\), and \(\operatorname{Var}(U^2)=4/45\). Uniform Taylor bounds on \([0,1]\) give the variance and weak-limit statements, without a relative-growth restriction on the two orders. Finally, \(\operatorname{lcm}(k,k)=k\) and \(\operatorname{lcm}(k,k+1)=k(k+1)\), proving the announced order-of-magnitude contrast.

## Verification
The accompanying standard-library Python script `checker.py` independently constructs Minkowski sums by taking convex hulls of all pairwise vertex sums and computes their areas via the shoelace formula. It compares these results against the closed formula at 1,360 deterministic angle and shape samples, checks sharp extrema in six normalized cases, and checks Haar means numerically in four cases; 1,376 checks passed. The script is a finite computational cross-check, not a substitute for the preceding unrestricted proof. Reproduce with `python3 checker.py`.

As a sanity check, for \(n=3\), \(m=4\), and unit area for both polygons, the exact maximal excluded area evaluates numerically to \(4.935779650\ldots\), consistent with the fixed-orientation triangle-square entry in the motivating source.

## Relationship to prior work
Aref Abbasi Moud (arXiv:2606.21812, first public version 20 June 2026) evaluates excluded areas for **aligned** regular-polygon binary mixtures and uses them to interpret random sequential adsorption. The present result evaluates the entire **relative-angle law** for arbitrary side counts and gives its sharp arithmetic oscillation and probability distribution. Geigenfeind and de las Heras (arXiv:1902.05961, first posted 15 February 2019) study angle-dependent excluded areas, including the single-species equilateral-triangle and square cases; their inspected regular-polygon discussion does not state the all-pair exact least-common-multiple formula. The mean also agrees with the classical planar principal kinematic identity and is not claimed as new by itself.

## Limitations
The theorem concerns two individual regular polygons in the Euclidean plane, their pairwise exclusion area and independent uniform relative orientation. It does not determine random-sequential-adsorption saturation densities, many-body packing corrections, or excluded-area profiles of arbitrary irregular or nonconvex shapes. Standard mixed-area identities underpin the calculation; priority over uncatalogued earlier exact trigonometric evaluations has not been independently certified. Computer checks are finite corroboration only.

## References
- A. Abbasi Moud, *Saturation Coverage in Binary Mixtures of Oriented Regular Polygons via Random Sequential Adsorption*, arXiv:2606.21812, initial version dated 20 June 2026, https://arxiv.org/abs/2606.21812.
- T. Geigenfeind and D. de las Heras, *The excluded area of two-dimensional hard particles*, arXiv:1902.05961, initial version dated 15 February 2019, https://arxiv.org/abs/1902.05961.
- R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press, 2014 (standard mixed-volume and support-function identities).

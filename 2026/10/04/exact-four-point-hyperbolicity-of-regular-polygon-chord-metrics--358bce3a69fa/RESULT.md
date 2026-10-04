# Exact four-point hyperbolicity of regular polygon chord metrics

## Finding

Let \(V_n\) be the vertex set of a regular Euclidean \(n\)-gon of circumradius \(R>0\), equipped with the ambient Euclidean chord metric. Let \(\delta(V_n)\) denote the Gromov four-point hyperbolicity constant in the convention
\[
d(w,x)+d(y,z)\le
\max\{d(w,y)+d(x,z),d(w,z)+d(x,y)\}+2\delta.
\]
For every \(n\ge4\), put \(h=\pi/(2n)\). Then
\[
\frac{\delta(V_n)}R=
\begin{cases}
2-\sqrt2,&n\equiv0\pmod4,\\
4\cos h\,\sin^2(kh),&n=4k+1,\\
4\cos h\,\sin(kh)\sin((k+1)h),&n=4k+2,\\
4\sin(kh)\sin((k+1)h),&n=4k+3.
\end{cases}
\]

A maximizing quadruple is obtained by making the four successive cyclic gap counts as balanced as possible:
\[
(k,k,k,k),\quad
(k,k,k,k+1),\quad
(k,k,k+1,k+1),\quad
(k,k+1,k+1,k+1)
\]
in the four residue classes of \(n\) modulo \(4\), respectively, up to cyclic order and reversal. Consequently,
\[
\delta(V_n)\longrightarrow(2-\sqrt2)R,
\]
and the limiting value is already attained exactly for every \(n\) divisible by \(4\).

## Assumptions and scope

Distances are straight Euclidean chord distances between polygon vertices. This is not the shortest-path metric of the cycle graph drawn by the polygon edges. The result concerns the standard four-point hyperbolicity constant of the finite metric space \(V_n\), rather than thin-triangle hyperbolicity of the filled polygon or of its boundary as a geodesic space.

The literature motivation is that Gromov hyperbolicity measures worst-case deviation from tree-like metric structure, while finite non-geodesic metric spaces arise naturally in Vietoris–Rips constructions. Chatterjee and Sloman emphasize the worst-case character of the standard invariant, and Bauer and Roll use the same four-point convention for finite metric spaces in their study of Vietoris–Rips filtrations.

## Proof

Choose four distinct vertices in cyclic order and let their positive integer gap counts be \(a,b,c,d\), with
\[
a+b+c+d=n.
\]
Set
\[
A=\frac{\pi a}{n},\quad
B=\frac{\pi b}{n},\quad
C=\frac{\pi c}{n},\quad
D=\frac{\pi d}{n},
\]
so \(A+B+C+D=\pi\). The chord subtending a gap \(j\) has length
\[
2R\sin\!\left(\frac{\pi j}{n}\right).
\]

For the three pair-sums in the four-point condition, write
\[
S_1=2R(\sin A+\sin C),\qquad
S_2=2R(\sin B+\sin D),
\]
and
\[
S_3=2R\bigl(\sin(A+B)+\sin(B+C)\bigr).
\]
The diagonal pairing \(S_3\) is the largest. Indeed,
\[
S_3-S_1=
8R\cos\!\left(\frac{A-C}{2}\right)
\sin\!\left(\frac B2\right)
\sin\!\left(\frac D2\right)\ge0,
\]
and similarly
\[
S_3-S_2=
8R\cos\!\left(\frac{B-D}{2}\right)
\sin\!\left(\frac A2\right)
\sin\!\left(\frac C2\right)\ge0.
\]
Therefore the contribution of this quadruple to hyperbolicity is
\[
4R\min\!\left\{
\cos\!\left(\frac{A-C}{2}\right)\sin\!\left(\frac B2\right)\sin\!\left(\frac D2\right),
\cos\!\left(\frac{B-D}{2}\right)\sin\!\left(\frac A2\right)\sin\!\left(\frac C2\right)
\right\}.
\]

Put \(p=a+c\) and \(q=b+d=n-p\), and interchange the two opposite gap-pairs if necessary so that \(p\le q\). Thus
\[
2\le p\le\left\lfloor\frac n2\right\rfloor.
\]
With \(h=\pi/(2n)\), the second term in the minimum gives
\[
\delta_{\{a,b,c,d\}}
\le
4R\cos((b-d)h)\sin(ah)\sin(ch).
\]
For fixed \(p\) and \(q\), the cosine is maximized by balancing \(b,d\), and the sine product is maximized by balancing \(a,c\). Hence
\[
\delta_{\{a,b,c,d\}}\le U_n(p),
\]
where
\[
U_n(p)=
4R\cos(\varepsilon_q h)
\sin\!\left(\left\lfloor\frac p2\right\rfloor h\right)
\sin\!\left(\left\lceil\frac p2\right\rceil h\right),
\]
and \(\varepsilon_q\) is \(0\) for even \(q\) and \(1\) for odd \(q\).

The sequence \(U_n(p)\) is strictly increasing for
\[
2\le p\le\left\lfloor\frac n2\right\rfloor.
\]
For even \(n\),
\[
U_n(2m)=4R\sin^2(mh),\qquad
U_n(2m+1)=4R\cos h\,\sin(mh)\sin((m+1)h),
\]
and the two successive differences are positive because
\[
\cos h\,\sin((m+1)h)-\sin(mh)
=\sin h\,\cos((m+1)h)>0
\]
and
\[
\sin((m+1)h)-\cos h\,\sin(mh)
=\sin h\,\cos(mh)>0.
\]
For odd \(n\), the same two identities apply after the parity factor \(\cos h\) switches to the even values of \(p\). Thus the global maximum occurs at
\[
p=\left\lfloor\frac n2\right\rfloor.
\]

Balancing both opposite gap-pairs at this terminal value produces the four displayed gap patterns. In each residue class, the other member of the minimum is equal to or larger than the upper-bound term, by one of the same two positive trigonometric differences. Hence the upper bound is attained.

Substitution gives the stated piecewise formulas. In particular, when \(n=4k\), one has \(kh=\pi/8\), so
\[
\delta(V_n)=4R\sin^2\!\left(\frac{\pi}{8}\right)
=(2-\sqrt2)R.
\]
The other three residue-class formulas converge to the same value as \(n\to\infty\).

## Verification

The algebraic proof is independent of finite enumeration. As a reproducibility check, the accompanying `verify.py` enumerates every four-vertex subset for each \(4\le n\le60\), computes the three four-point pair-sums directly from chord lengths, and compares the resulting maximum against both the closed formula and the balanced-gap witness. It prints `VERIFY_OK n=4..60`.

The checker is not used to infer the theorem for arbitrary \(n\); that step is supplied by the monotonic upper-bound argument above. Repeated-point quadruples cannot increase the four-point defect, so enumerating distinct four-subsets is sufficient for the finite checks.

## Relationship to prior work

Chatterjee and Sloman describe standard Gromov hyperbolicity as a worst-case measure of deviation from tree structure and develop an average analogue. Their paper gives the general invariant, not this regular-polygon chord calculation.

Bauer and Roll explicitly use the four-point inequality for finite metric spaces and relate hyperbolicity to Vietoris–Rips filtrations. Their full text contains no occurrence of “polygon” or “circle,” and does not state a regular cyclic point-set formula.

Graph-hyperbolicity results for the cycle graph \(C_n\) are not equivalent. In that setting the metric is shortest-path length along unit graph edges, and the known graph constant grows linearly with \(n\). Here the metric is the bounded Euclidean chord metric on the same visual vertex arrangement; the exact constant instead stays bounded and converges to \((2-\sqrt2)R\).

Targeted searches for regular polygons, cyclic Euclidean point sets, chord metrics, four-point constants, and balanced cyclic quadruples did not locate an equivalent statement or a stronger result implying the piecewise formula.

## Limitations

The theorem concerns equally spaced points on one Euclidean circle and ambient chord distance. It does not classify arbitrary cyclic point sets, perturbed regular polygons, intrinsic boundary metrics, or geodesic cycle graphs. The literature search was targeted rather than exhaustive, so an older equivalent calculation under different metric-geometry terminology remains a residual risk.

## References

S. Chatterjee and L. Sloman, “Average Gromov hyperbolicity and the Parisi ansatz,” arXiv:1907.03203, first submitted 2019-07-06.

U. Bauer and F. Roll, “Gromov Hyperbolicity, Geodesic Defect, and Apparent Pairs in Vietoris–Rips Filtrations,” arXiv:2112.06781, first submitted 2021-12-13.

J. Méndez, R. Reyes, J. M. Rodríguez, and J. M. Sigarreta, “Gromov hyperbolicity of Johnson and Kneser graphs,” Aequationes Mathematicae 98 (2024), 661–686, DOI 10.1007/s00010-024-01076-y.

# Exact harmonic–arithmetic contraction for regular polygons

## Finding

Let \(P_n\subset\mathbb R^2\) be a regular Euclidean \(n\)-gon centered at the origin, \(n\ge3\). Define
\[
A_n=\frac{P_n-P_n}{2}
\]
and
\[
H_n=\left(\frac{P_n^{\circ}-P_n^{\circ}}{2}\right)^{\circ}.
\]
These are respectively the arithmetic and harmonic means of \(P_n\) and \(-P_n\).

Let \(\beta_n\) be the optimal homothetic factor, with translations allowed in the optimality test, such that
\[
H_n\subset^{\mathrm{opt}}\beta_n A_n.
\]
Then
\[
\beta_n=
\begin{cases}
1,&n\text{ even},\\[1mm]
\displaystyle\frac{4s_n}{(s_n+1)^2}
=\frac{\cos(\pi/n)}{\cos^4(\pi/(2n))},&n\text{ odd},
\end{cases}
\]
where for odd \(n\)
\[
s_n=\sec(\pi/n)
\]
is the Minkowski asymmetry of \(P_n\).

For odd \(n\), the two symmetrizations are regular \(2n\)-gons with vertex directions shifted by half a sector. Thus every odd regular polygon attains the sharp planar lower envelope
\[
\frac{4s}{(s+1)^2}
\]
for the harmonic-to-arithmetic contraction factor at its own asymmetry \(s=s_n\). The triangle case gives the previously published value \(8/9\); the cases of odd \(n\ge5\) form a canonical infinite equality family. In addition,
\[
1-\beta_n=\frac{\pi^4}{16n^4}+O(n^{-6}).
\]

## Assumptions and scope

The polar is taken with respect to the polygon center, which is the origin. The notation \(K\subset^{\mathrm{opt}}C\) means \(K\subset C\), but no translate of a smaller positive homothet of \(C\) contains \(K\).

The source literature studies exactly this harmonic-versus-arithmetic containment problem as a function of Minkowski asymmetry. It supplies the planar sharp lower envelope for the contraction factor and, separately, computes the reverse arithmetic-to-harmonic factor for centered regular odd polygons. The result here identifies the missing forward factor for that same canonical family.

## Proof

The even case is immediate: a centered regular even polygon is centrally symmetric, so
\[
P_n=-P_n,
\]
and both symmetrizations equal \(P_n\). Hence \(\beta_n=1\).

Assume from now on that \(n\) is odd and normalize the circumradius of \(P_n\) to \(1\). Put
\[
\theta=\frac{\pi}{n},\qquad r=\cos\theta,\qquad c=\cos\frac{\theta}{2}.
\]
The inradius is \(r\), so the Minkowski asymmetry is
\[
s_n=\frac1r.
\]
The polar of a centered regular odd polygon is a rotated regular polygon with circumradius \(1/r\). For odd \(n\), the required rotation agrees with negation modulo the rotational symmetry, and therefore
\[
P_n^{\circ}=s_n(-P_n).
\]
It follows that
\[
\frac{P_n^{\circ}-P_n^{\circ}}2=s_nA_n,
\]
and hence
\[
H_n=(s_nA_n)^{\circ}=rA_n^{\circ}.
\]

We next identify \(A_n\). Write the vertices of \(P_n\) as the unit complex numbers \(z_j\). The extreme differences are obtained from vertex pairs separated by \((n-1)/2\) edges. Their half-differences have modulus
\[
\frac12\left|z_j-z_{j+(n-1)/2}\right|
=\sin\!\left(\frac{n-1}{2n}\pi\right)
=c.
\]
Together with their negatives these give \(2n\) equally spaced directions, so \(A_n\) is a regular \(2n\)-gon of circumradius \(c\). Its inradius is therefore
\[
c\cos\frac{\pi}{2n}=c^2.
\]

Consequently, \(A_n^{\circ}\) is a regular \(2n\)-gon rotated by \(\pi/(2n)\) relative to \(A_n\), with circumradius \(1/c^2\). Thus \(H_n=rA_n^{\circ}\) has circumradius
\[
\frac{r}{c^2},
\]
and each vertex direction of \(H_n\) is an outer-normal direction of a side of \(A_n\).

For a factor \(\beta>0\), the boundary of \(\beta A_n\) in such a side-normal direction lies at distance \(\beta c^2\) from the origin. Therefore
\[
H_n\subseteq\beta A_n
\]
holds exactly when
\[
\frac{r}{c^2}\le\beta c^2.
\]
The least centered factor is thus
\[
\beta_n=\frac{r}{c^4}.
\]
At equality, opposite vertices of \(H_n\) touch opposite supporting sides of \(\beta_nA_n\). Their supporting-strip width is therefore exactly the width of \(\beta_nA_n\) in that normal direction. Translation does not change width, so no factor smaller than \(1\) applied to \(\beta_nA_n\) can contain \(H_n\). This proves optimality even when translations are allowed.

Finally,
\[
c^2=\frac{1+r}{2},
\]
so
\[
\beta_n=\frac{4r}{(1+r)^2}=\frac{4s_n}{(s_n+1)^2}.
\]
Taylor expansion at \(\theta=0\) gives
\[
\beta_n=1-\frac{\theta^4}{16}-\frac{\theta^6}{48}+O(\theta^8),
\]
which yields the stated asymptotic after substituting \(\theta=\pi/n\).

## Verification

The proof is exact and valid for every \(n\ge3\). The accompanying `verify.py` independently reconstructs the polygonal operations from vertices: it forms the difference body by convex hull, computes polars from supporting edges, and obtains the smallest centered harmonic-to-arithmetic containment factor from support inequalities.

For every \(3\le n\le51\), the checker compares the reconstructed factor with the closed formula. For odd \(n\), it also verifies that both symmetrizations have \(2n\) vertices, checks their predicted circumradii, and reproduces the already published reverse factor \((s_n+1)/2\). It prints

`VERIFY_OK regular polygon harmonic-arithmetic contraction n=3..51`

The finite replay is a consistency check only; it is not used to infer the all-\(n\) theorem.

## Relationship to prior work

Brandenberg, von Dichter, and González Merino introduced the planar asymmetry threshold for optimal harmonic-to-arithmetic containment. Their 2020 preprint explicitly gives the centered equilateral-triangle factor \(8/9\) and observes that centered regular odd polygons do not generally have factor \(1\).

Their 2021 follow-up determines sharp asymmetry-dependent bounds for the contraction factor. In dimension two, its Theorem 1.7 gives the sharp lower envelope
\[
\beta_1(s)=\frac{4s}{(s+1)^2}.
\]
The same paper's Example 4.2 studies centered regular odd polygons in the reverse direction and proves
\[
A_n\subset^{\mathrm{opt}}\frac{s_n+1}{2}H_n.
\]
Neither statement determines the forward factor for regular odd polygons with \(n\ge5\): the universal lower envelope supplies only a lower bound for that family, while the reverse containment does not supply the missing upper bound. The regular \(2n\)-gon polarity calculation above closes that comparison and shows that the canonical family itself hits the lower envelope.

Targeted searches for the exact secant formula, the regular-polygon forward factor, harmonic/arithmetic symmetrization containment, and equivalent regular-polar formulations did not locate an equivalent statement for odd \(n\ge5\).

## Limitations

The calculation uses Euclidean regularity. It does not classify all planar bodies attaining the lower envelope, nor all cyclic, equiangular, or affine-regular polygons. Affine images inherit the same optimal factor by affine invariance, but no claim is made that they exhaust equality cases.

The triangle endpoint \(n=3\) is prior work and is included only to make the formula complete. The same 2021 paper already contains a detailed reverse-containment calculation for all centered regular odd polygons; the new content is the forward factor for odd \(n\ge5\), its equality with the sharp lower envelope, and the resulting asymptotic profile.

## References

R. Brandenberg, K. von Dichter, and B. González Merino, “Relating Symmetrizations of Convex Bodies: Once More the Golden Ratio,” arXiv:2006.07259, first submitted 2020-06-12; later American Mathematical Monthly 129 (2022), 352–362, DOI 10.1080/00029890.2022.2043113.

R. Brandenberg, K. von Dichter, and B. González Merino, “Tightening and reversing the arithmetic-harmonic mean inequality for symmetrizations of convex sets,” arXiv:2112.13590, first submitted 2021-12-27; later Communications in Contemporary Mathematics 25 (2023), DOI 10.1142/S0219199722500456.

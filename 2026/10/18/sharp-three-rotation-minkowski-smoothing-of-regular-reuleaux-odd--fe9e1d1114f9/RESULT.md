# Sharp three-rotation Minkowski smoothing of regular Reuleaux odd-gons

## Finding
For every odd integer \(n\ge3\) and width \(w>0\), let \(R_n(w)\subset\mathbb R^2\) be the centered regular Reuleaux \(n\)-gon of Euclidean constant width \(w\). For arbitrary three angles \(\theta_1,\theta_2,\theta_3\in\mathbb R\), put
\[
M=\frac13\bigl(\mathcal R_{\theta_1}R_n(w)+\mathcal R_{\theta_2}R_n(w)+\mathcal R_{\theta_3}R_n(w)\bigr),
\]
where addition is Minkowski addition. Then
\[
\boxed{\operatorname{area}(M)\le w^2\left(\frac{5\pi}{18}-\frac n6\tan\frac{\pi}{6n}\right).}
\]
Equality holds if and only if the three angles, reduced modulo \(2\pi/n\), are precisely a translate of
\[
\left\{0,\frac{2\pi}{3n},\frac{4\pi}{3n}\right\}.
\]
At equality the convex body itself, up to a rotation, is
\[
\boxed{M=\frac23B_w+\frac13R_{3n}(w),}
\]
where \(B_w\) is the centered disk of radius \(w/2\). Its strict deficit from the disk area is exactly
\[
\frac{\pi w^2}{4}-\max\operatorname{area}(M)
=\frac19\left(\frac{\pi w^2}{4}-\operatorname{area}(R_{3n}(w))\right)
=\frac{\pi^3w^2}{3888n^2}+O(w^2n^{-4}).
\]
The optimal area increases strictly as odd \(n\) increases, and is never equal to the disk area for finite \(n\).

## Assumptions and scope
\(R_n(w)\) has \(n\) circular boundary arcs of radius \(w\), each subtending the central angle \(\pi/n\), between successive vertices of a regular \(n\)-gon. Its generating polygon has circumradius \(w/(2\cos(\pi/(2n)))\). Rotation \(\mathcal R_\theta\) is about the common center. The three summands have equal weights; the theorem does not optimize over unequal weights or arbitrary constant-width bodies. Angles are taken modulo the intrinsic \(2\pi/n\) symmetry of \(R_n(w)\).

## Proof
Scale to \(w=1\), write \(\alpha=\pi/n\), \(\beta=\alpha/2\), \(L=2\alpha\). For a support function \(h\), its curvature radius in the normal-angle coordinate is \(\rho=h+h''\) almost everywhere. In a suitable angular origin, \(\rho\) is the alternating square wave taking values one and zero on consecutive intervals of length \(\alpha\). It has mean \(1/2\), and its only nonconstant Fourier modes are odd multiples of \(n\), with cosine amplitudes \(2(-1)^{(\ell-1)/2}/(\pi\ell)\), \(\ell\ge1\) odd. Dividing these coefficients by \(1-n^2\ell^2\) gives the support coefficients. The identity
\[
\operatorname{area}(K)=\tfrac12\int_0^{2\pi}(h^2-(h')^2)\,d\theta
\]
therefore implies, for the mean of TWO copies at relative angle \(t\), the disk-area deficit
\[
f_n(t):=\frac\pi4-\operatorname{area}\left(\frac{R_n+\mathcal R_tR_n}{2}\right)
=\frac1\pi\sum_{\substack{\ell\ge1\\\ell\ {\rm odd}}}
\frac{1+\cos(n\ell t)}{\ell^2(n^2\ell^2-1)}.\tag{1}
\]
The sum is absolutely convergent and defines an even \(L\)-periodic function. Direct partial fractions or the cosine expansion of \(\sin(\beta-t)\) give, for \(0\le t\le\alpha\),
\[
\operatorname{area}\left(\frac{R_n+\mathcal R_tR_n}{2}\right)
=\frac\pi2-\frac n4\left(t+\frac{\sin\beta+\sin(\beta-t)}{\cos\beta}\right).\tag{2}
\]
To verify (2) without relying on a tabulated Fourier series, differentiate (1) twice and use the cosine coefficients on \([0,\pi]\) of \(\frac{\pi}{4n\cos\beta}\sin(\beta-x/n)\), which are exactly \((n^2\ell^2-1)^{-1}\) for positive odd \(\ell\) and zero for even \(\ell\). The conditions \(f_n'(0)=0\) and \(f_n(\alpha)=0\) determine both integration constants. In particular,
\[
f_n(0)=\frac n2\tan\beta-\frac\pi4>0,\quad f_n(\alpha)=0,\quad f_n(t)+f_n(\alpha-t)=f_n(0),\tag{3}
\]
and
\[
f_n'(t)=-\frac{n}{2\cos\beta}\sin\frac t2\sin\frac{\alpha-t}{2}\quad(0<t<\alpha).\tag{4}
\]
Thus \(f_n\) decreases strictly on \((0,\alpha)\). Moreover \(f_n'\) has the same value at two points of this interval only if they are equal or add to \(\alpha\): the product of the two sines in (4) increases strictly until \(\alpha/2\) and then decreases strictly.

For three angles, applying the same Fourier area identity to the sum of three support functions yields
\[
\frac\pi4-\operatorname{area}(M)
=\frac49\bigl[f_n(\theta_1-\theta_2)+f_n(\theta_2-\theta_3)+f_n(\theta_3-\theta_1)\bigr]-\frac13f_n(0).\tag{5}
\]
Order the three distinct angles cyclically modulo \(L\), and denote their successive nonnegative gaps by \(a,b,c\), so \(a+b+c=L\). Evenness and periodicity convert the bracket in (5) to \(F(a,b,c)=f_n(a)+f_n(b)+f_n(c)\). We prove that it has the unique minimum at \(a=b=c=L/3\).

If a gap exceeds \(\alpha=L/2\), the derivative of \(f_n\) on that gap is positive while the derivatives on the other two gaps are negative; no constrained interior stationary point is possible. If all three gaps lie strictly between zero and \(\alpha\), the stationary equations require equal derivatives. By (4) each gap takes one of the two complementary values \(t,\alpha-t\). A mixture of these two values, with sum \(2\alpha\), forces \(t=0\) or \(t=\alpha\), contrary to strict interiority. Thus the only interior stationary triple is \(a=b=c=2\alpha/3\). At a boundary with one gap zero, (3) and positivity give \(F\ge f_n(0)\); a boundary with one gap \(\alpha\) gives \(F=f_n(0)\) by (3).

It remains to prove that the equally spaced triple beats every boundary. Set
\[
S_n=\sum_{\substack{\ell\ge1\\\ell\ {\rm odd}}}\frac1{\ell^2(n^2\ell^2-1)},\qquad
T_n=\sum_{\substack{\ell\ge1\\\ell\ {\rm odd},\,3\mid\ell}}\frac1{\ell^2(n^2\ell^2-1)}.
\]
The cosine values at \(2\pi\ell/3\) are \(1\) when \(3\mid\ell\) and \(-1/2\) otherwise, so
\[
f_n(0)-3f_n(L/3)=\frac{S_n-9T_n}{2\pi}>0.\tag{6}
\]
Indeed, \(9T_n=\sum_{j\ge1,\,j\ {\rm odd}}[j^2(9n^2j^2-1)]^{-1}<S_n\) term by term. Compactness of the closed gap simplex, the stationary-point classification, and (6) prove global optimality and equality uniqueness.

At equality, the three curvature square waves at shifts \(0,L/3,2L/3\) average to a square wave taking values \(1/3\) and \(2/3\) on alternating arcs of length \(\pi/(3n)\). This is the curvature of \(\frac23B_1+\frac13R_{3n}(1)\), up to rotation. Equality of curvature and of symmetry-centered support functions proves the body identity, not just equality of area. The known regular-Reuleaux area \(\operatorname{area}(R_m(1))=\frac12(\pi-m\tan(\pi/(2m)))\) now gives
\[
\frac\pi4-\max\operatorname{area}(M)
=\frac19\left(\frac{3n}{2}\tan\frac\pi{6n}-\frac\pi4\right),
\]
which simplifies to the asserted formula. Strict increase in odd \(n\) follows from strict decrease of \(x\mapsto x\tan(c/x)\) for \(x>2c/\pi\): with \(u=c/x\), \(\tan u-u\sec^2u<0\) for \(0<u<\pi/2\). The Taylor series of \(\tan\) supplies the stated \(n^{-2}\) asymptotic. Scaling restores \(w^2\).

## Verification
Execute `python3 verify.py` from this package directory. The standalone script checks (1) against Fourier truncations across six odd polygon orders and seven angles, evaluates (5) at 30,000 pseudorandom triples, verifies exact optimal-area identities numerically, and independently generates boundary points by intersecting the defining unit disks for nine representative three-copy configurations. The finite numerical tests provide reproducible regression evidence, not the all-angle inequality or equality classification; those are proved analytically above. Expected successful output starts `VERIFY_OK`.

## Relationship to prior work
The Fourier area formula and harmonic representation for regular Reuleaux polygons are classical and are developed in Resnikoff's 2015 full text; they are premises rather than new claims. A published 2026 note gives the full TWO-copy rotation profile specifically for the Reuleaux triangle; that result supplies a closely related kernel but has neither the three-point constrained extremal problem nor the unique three-copy optimizer. Falco and Myroshnychenko's 2026 theorem identifies minimum-area constant-width bodies under specified finite symmetry groups, not maximum-area equal-weight Minkowski means of three rotated fixed summands. The present result solves a distinct, global three-rotation optimization for every odd order and identifies the optimal body exactly. Classical Reuleaux areas and disk comparison are not claimed as new.

## Limitations
The theorem concerns three equally weighted rotated copies of a fixed *regular* Reuleaux odd-gon. It does not assert optimality of equal spacing for four or more summands, for unequal weights, or for arbitrary constant-width bodies. The argument gives uniqueness modulo common rotation, permutation, and intrinsic polygon symmetry. Historical coverage of this specific three-copy extremum in unindexed work remains possible; the current literature comparison is not a proof of priority. No independent scientific audit has been performed.

## References
1. H. L. Resnikoff, *On Curves and Surfaces of Constant Width*, arXiv:1504.06733v1, publicly submitted 25 April 2015, https://arxiv.org/html/1504.06733v1.
2. G. T. Sallee, *Maximal Areas of Reuleaux Polygons*, Canadian Mathematical Bulletin 13 (1970), 175–179, DOI: 10.4153/CMB-1970-037-1.
3. *Exact rotational Minkowski-average area profile of the Reuleaux triangle*, 2026 published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rotational-minkowski-average-area-profile-of-the-reuleaux--53c190e0340e.
4. J. Falco and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125v1, publicly submitted 5 August 2026, https://arxiv.org/abs/2608.05125.
5. M. Craizer and H. Martini, *Involutes of Polygons of Constant Width in Minkowski Planes*, arXiv:1406.3205v1, 12 June 2014, https://arxiv.org/abs/1406.3205.

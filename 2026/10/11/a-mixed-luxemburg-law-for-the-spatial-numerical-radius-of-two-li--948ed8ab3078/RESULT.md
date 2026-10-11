# A mixed-Luxemburg law for the spatial numerical radius of two-link shifts

## Finding

Let \(1<p<\infty\), \(q=p/(p-1)\), and let \(S_{a,b}\) act on real or complex \(\ell_p^3\) by
\[
S_{a,b}(z_1,z_2,z_3)=(a z_2,b z_3,0),\qquad a,b\in\mathbb C
\]
(with real \(a,b\) over the real field). Its spatial numerical radius is
\[
v_p(S_{a,b})=\sup_{\|z\|_p=1}\left|\sum_{j=1}^3 |z_j|^{p-2}\overline{z_j}(S_{a,b}z)_j\right|,
\]
where \(|z_j|^{p-2}\overline{z_j}=0\) when \(z_j=0\). Write \(A=|a|\), \(B=|b|\) and
\[
k_p=\frac{(p-1)^{1/q}}p,
\quad
L_{p,q}(A,B)=\inf\left\{\lambda>0:\left(\frac A\lambda\right)^p+\left(\frac B\lambda\right)^q\le1\right\}.
\]
The infimum is defined to be zero if \(A=B=0\). Then **for every pair of weights**
\[
\boxed{v_p(S_{a,b})=k_p L_{p,q}(A,B).}
\]
Equivalently, if \(A+B>0\), the radius \(w=v_p(S_{a,b})\) is the unique positive root of
\[
\boxed{(p-1)^{p-1}\left(\frac{A}{p w}\right)^p+(p-1)\left(\frac{B}{p w}\right)^q=1.}
\]
For complex scalars the entire spatial numerical range is the closed disk \(\{z\in\mathbb C:|z|\le w\}\). For real scalars it is \([-w,w]\). Furthermore \(k_p=k_q\), giving the exact reversal/duality identity
\[
\boxed{v_p(S_{a,b})=v_q(S_{b,a}).}
\]
At the Hilbert exponent, \(v_2(S_{a,b})=\tfrac12\sqrt{A^2+B^2}\). At exponent four, if \(A>B>0\), then
\[
\boxed{v_4(S_{a,b})>v_4(S_{b,a}).}
\]
For example, weights \((2,1)\) and \((1,2)\) give approximately \(1.26677874170883\) and \(1.18733148093846\), respectively, whereas the Hilbert numerical radius is unchanged on reversing the weights.

## Assumptions and scope

The norm is the standard real or complex \(\ell_p^3\) norm, and the numerical radius is the Banach-space spatial radius associated with the unique norming functional in the smooth range \(1<p<\infty\), **not** the spectral radius, operator norm, or Hilbert-space inner-product numerical radius outside \(p=2\). The weights may vanish or be complex. The mixed-exponent expression uses the specified ordered weights: exchanging them usually changes the radius. No statement is asserted at \(p=1\) or \(p=\infty\).

## Proof

**Reduction.** The normalized duality map on the unit sphere is \(J_p(z)_j=|z_j|^{p-2}\overline{z_j}\). Taking absolute values and the triangle inequality yields
\[
v_p(S_{a,b})\le \max_{x^p+y^p+z^p=1,\ x,y,z\ge0}\bigl(Ax^{p-1}y+By^{p-1}z\bigr).
\]
Equality follows by choosing positive coordinates after removing the phases of the two nonzero weights by a diagonal isometry. Hence this maximum equals the spatial radius. The proof for zero weights follows either from the same one-link optimization or by continuity; below assume \(A,B>0\).

**Interior and unique root.** The maximum is positive, so \(y>0\). If \(x=0\), adding \(x=\varepsilon\) improves the numerator by \(Ay\varepsilon^{p-1}\), while changing its homogeneous denominator only by order \(\varepsilon^p\); thus the boundary is not optimal. If \(z=0\), adding \(z=\varepsilon\) gains \(By^{p-1}\varepsilon\) against a denominator loss of order \(\varepsilon^p\). Consequently every maximizer has \(x,y,z>0\). Put \(u=x/y\), \(v=z/y\). By homogeneity its value is
\[
R(u,v)=\frac{Au^{p-1}+Bv}{1+u^p+v^p},\qquad u,v>0.
\]
At an interior maximum \(w=R(u,v)\), partial differentiation gives
\[
puw=(p-1)A,\qquad pv^{p-1}w=B.
\]
Using \(w(1+u^p+v^p)=Au^{p-1}+Bv\), these identities imply
\[
1=\frac{u^p}{p-1}+(p-1)v^p.
\]
Substitution gives exactly the displayed scalar equation in \(w\). The left-hand side is a strictly decreasing continuous function of \(w>0\), tending from infinity to zero. It has a unique positive root. The maximum exists by compactness and must be this root, proving the formula without assuming an unproved uniqueness of the optimizing vector.

**Luxemburg identification, duality, and full numerical range.** Since \(k_p^p=(p-1)^{p-1}/p^p\) and \(k_p^q=(p-1)/p^q\), the root equation is equivalent to \((A/(w/k_p))^p+(B/(w/k_p))^q=1\). This proves the Luxemburg formula, including zero-weight cases by continuity. Direct algebra yields \(k_p=k_q\); exchanging \(p\) and \(q\) and the ordered weights leaves the mixed norm equation unchanged. On complex \(\ell_p^3\), conjugation by the diagonal isometries \(\operatorname{diag}(1,e^{it},e^{2it})\) rotates the numerical range through \(e^{it}\). The continuous modulus of the spatial numerical-range map takes every value between zero (at a coordinate vector) and its attained maximum \(w\), and rotations fill the disk. Over the real field the unit sphere is connected, and opposite phase choices attain \(\pm w\); the image is the interval between them.

**Strict quartic orientation.** Fix \(p=4\) and \(A>B>0\), and set \(C=A^{4/3}\), \(D=B^{4/3}\), \(H=C^2+CD+D^2\). Writing \(Z=(4v_4(S_{b,a}))^{4/3}\), the root equation for reversed weights is
\[
F_{D,C}(Z)=3Z^3-9CZ^2-81D^3=0.
\]
This cubic has exactly one positive root: it decreases from a negative value until \(2C\) and then strictly increases. At \(3\sqrt H\) its value is \(81(H^{3/2}-CH-D^3)>0\). Positivity follows from
\[
H^3-(CH+D^3)^2=CD(C^4+3C^3D+3C^2D^2+3CD^3+D^4)>0.
\]
Thus \(Z^2<9H\). Evaluating the cubic for the original ordered weights at this same \(Z\) gives
\[
F_{C,D}(Z)=3Z^3-9DZ^2-81C^3
=9(C-D)(Z^2-9H)<0.
\]
As \(F_{C,D}\) also has one positive root, its root is larger than \(Z\). The map \(w\mapsto(4w)^{4/3}\) is increasing, hence \(v_4(S_{a,b})>v_4(S_{b,a})\). This argument covers all positive strict weight inequalities, not merely sampled choices.

## Verification

The accompanying standalone `verification.py` uses deterministic bisection on the proven scalar equation, reconstructs the maximizing positive vector from the two stationary identities, checks conjugate-exponent reversal and the Hilbert specialization, and compares the formula against many independently sampled normalized vectors and quartic reversed-weight cases. Run `python verification.py` (Python 3 standard library only). The program is a finite consistency check; global optimality, the closed-disk description, and strict quartic ordering are established by the preceding analysis, not by sampling.

## Relationship to prior work

Gau and Wu's 2014 preprint on block-shift numerical radii (arXiv:1410.0339v1, October 1, 2014) gives Hilbert-space bounds and equality criteria for block shifts. Undrakh, Nakazato, Vandanjav and Chien (2015) use Hermitian-part spectra for Hilbert weighted shifts. Those Hilbert results recover the \(p=2\) behavior but do not yield the ordered \(p\)-dependent mixed Luxemburg law.

An and Heo (2022, Example 2.4) computed the disk and radius \(k_p\) for the single-weight \(2\times2\) nilpotent shift on complex \(\ell_p^2\); this is the axis restriction \(A=0\) or \(B=0\), whereas two consecutive nonzero weights give the mixed exponents and quartic orientation asymmetry above. The 2012 Hilbert weighted-shift permutation study of Chang and Wang addresses rearrangements in \(\ell_2\), not the Banach-space spatial numerical radius. Results about disk-contractivity of analytic functions of the \(\ell_p\) shift do not assert a spatial numerical-radius identity. Similarity of terminology alone does not establish novelty: an unlocated older characterization of three-coordinate Banach numerical ranges remains a genuine bibliographic risk.

## Limitations

This is a complete formula for the two-edge, three-coordinate nilpotent shift only. No formula for longer shifts or all finite-dimensional operators is claimed. The sharp quartic orientation inequality does not claim the same ordering for arbitrary \(p\). The proof is self-contained, but originality has been evaluated only against the recorded literature searches and inspected sources; independent verification and a comprehensive bibliographic audit have not occurred.

## References

1. H.-L. Gau and P. Y. Wu, *Upper and Lower Bounds for Numerical Radii of Block Shifts*, arXiv:1410.0339v1 (first publicly dated 2014-10-01), https://arxiv.org/pdf/1410.0339.
2. B. Undrakh, H. Nakazato, A. Vandanjav, and M.-T. Chien, *The Numerical Radius of a Weighted Shift Operator*, Electronic Journal of Linear Algebra 30 (2015), 944–963, https://doi.org/10.13001/1081-3810.2821.
3. I. J. An and J. Heo, *Numerical Ranges and Complex Symmetric Operators in Semi-Inner-Product Spaces*, Journal of Inequalities and Applications 2022:150, https://doi.org/10.1186/s13660-022-02886-x.
4. C.-T. Chang and K.-Z. Wang, *Maximizing Numerical Radii of Weighted Shifts under Weight Permutations*, J. Math. Anal. Appl. 394 (2012), 592–602, https://doi.org/10.1016/j.jmaa.2012.04.039.

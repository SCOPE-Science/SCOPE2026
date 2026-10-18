# The exact real \(\operatorname{SUNTF}(2,5,R)\) existence threshold

## Finding
For an integer \(R\geq 1\), let \(\operatorname{SUNTF}_{\mathbb R}(2,5,R)\) denote \(R\) real unit-norm tight-frame layers, each consisting of five vectors in \(\mathbb R^2\), such that the mean over layers of every off-diagonal squared inner product is independent of the column pair. Then
\[
\boxed{\operatorname{SUNTF}_{\mathbb R}(2,5,R)\text{ exists if and only if }R\geq2.}
\]
In particular, an exact algebraic three-layer construction solves the open real \(\operatorname{SUNTF}(2,5,3)\) case raised in Example 4.4 of Brinkley--Fickus--Jasper--Mixon (2026), and the least eventual-existence threshold is \(R_{\mathbb R}(2,5)=2\).

## Assumptions and scope
The field is \(\mathbb R\); each layer has ambient dimension \(2\) and consists of precisely \(5\) unit vectors; the layer count \(R\) is an arbitrary positive integer. A unit-norm tight frame \((u_{rj})_{j=0}^4\) here means
\[
\sum_{j=0}^{4}u_{rj}u_{rj}^{\mathsf T}=\frac52 I_2.
\]
Stratification means that for all distinct \(j,k\in\{0,1,2,3,4\}\), the expression
\[
\frac1R\sum_{r=0}^{R-1}|\langle u_{rj},u_{rk}\rangle|^2
\]
has the same value. The tight-frame identity forces this value to be the exact Welch average \(3/8\), since for each fixed column the sum of its squared inner products with the other four columns is \(5/2-1=3/2\).

## Proof
**The doubled-angle reduction.** If \(w=e^{i\theta}\), put \(u(w)=(\cos(\theta/2),\sin(\theta/2))\in\mathbb R^2\), with any consistent argument choice. Its sign is irrelevant. The identities
\[
u(w)u(w)^{\mathsf T}=\frac12
\begin{pmatrix}1+\operatorname{Re}w&\operatorname{Im}w\\
\operatorname{Im}w&1-\operatorname{Re}w\end{pmatrix}
\quad\text{and}\quad
|\langle u(w),u(v)\rangle|^2=
\frac{1+\operatorname{Re}(w\overline v)}2
\]
follow from the double-angle formulas. In particular, five unit phasors whose sum is zero give a real unit-norm tight frame with frame bound \(5/2\).

**Three exact layers.** Set
\[
s=\sqrt{\frac32},\quad a=\frac{s-1}{2},\quad
b=\frac{s}{2},\quad c=\sqrt{1-a^2},\quad
d=\sqrt{1-b^2}=\sqrt{\frac58}.
\]
Take the five unit phasors
\[
z_0=1,\qquad z_1=a+ic,\qquad z_2=a-ic,\qquad
z_3=-b+id,\qquad z_4=-b-id.
\]
They satisfy
\[
z_0+z_1+z_2=s,\qquad z_3+z_4=-s,
\qquad\sum_{j=0}^{4}z_j=0.
\]
For layer \(r\in\{0,1,2\}\), set
\[
w_{rj}=
\begin{cases}
z_{(j+r)\bmod 3},&j\in\{0,1,2\},\\
z_j,&j\in\{3,4\},
\end{cases}
\qquad u_{rj}=u(w_{rj}).
\]
Every layer has zero phasor sum, so every layer is a real unit-norm tight frame in \(\mathbb R^2\).

For distinct columns \(j,k\), write
\[
A_{jk}=\sum_{r=0}^{2}\operatorname{Re}
(w_{rj}\overline{w_{rk}}).
\]
There are exactly three cases, exhausting the ten unordered pairs.

If \(j,k\in\{0,1,2\}\), cyclic shifts traverse the three unordered pairs from \(z_0,z_1,z_2\), hence
\[
A_{jk}=\frac{|z_0+z_1+z_2|^2-3}{2}
=\frac{3/2-3}{2}=-\frac34.
\]
If exactly one of \(j,k\) lies in \(\{0,1,2\}\), the other being \(\ell\in\{3,4\}\), then
\[
A_{jk}=\operatorname{Re}(s\overline{z_\ell})
=-sb=-\frac34.
\]
Finally, for \(\{j,k\}=\{3,4\}\),
\[
A_{34}=3\operatorname{Re}(z_3\overline{z_4})
=3(2b^2-1)=-\frac34.
\]
Consequently, for every distinct pair,
\[
\frac13\sum_{r=0}^{2}
|\langle u_{rj},u_{rk}\rangle|^2
=\frac{3+A_{jk}}6=\boxed{\frac38}.
\]
This verifies a real \(\operatorname{SUNTF}(2,5,3)\) with an explicit radical certificate, and no optimization, numerical approximation, or existence theorem is needed.

**Two layers and every larger number.** Let \(\zeta=e^{2\pi i/5}\), and for \(j=0,\ldots,4\), choose the two doubled-angle phasors \(\zeta^j\) and \(\zeta^{2j}\). Each five-phasor row has sum zero. For any \(j\neq k\),
\[
\cos\!\left(\frac{2\pi(j-k)}5\right)
+\cos\!\left(\frac{4\pi(j-k)}5\right)=-\frac12,
\]
so the two layers also have averaged squared overlap \(3/8\). When stratified systems with the same five columns and squared overlap \(3/8\) are stacked, each original frame layer remains tight and the pooled average is still \(3/8\). Every integer \(R\geq2\) is of the form \(R=2p+3q\) for nonnegative integers \(p,q\), proving existence for all such \(R\).

**No one-layer system.** If \(R=1\), the stratification equations and tightness would force five equiangular real unit vectors in \(\mathbb R^2\) with squared inner products \(3/8\). Their doubled-angle phasors would have planar real Gram matrix with diagonal entries \(1\) and off-diagonal entries \(2(3/8)-1=-1/4\). This matrix is
\[
G=\frac54I_5-\frac14\boldsymbol1\boldsymbol1^{\mathsf T}.
\]
It has eigenvalues \(0\) once and \(5/4\) four times, hence rank \(4\). As a Gram matrix of five vectors in \(\mathbb R^2\), it would have rank at most \(2\), a contradiction. This completes the classification.

## Verification
The complete exact algebraic certificate is implemented in `three_layer_suntf_checker.py`, runnable with Python 3 and SymPy 1.12 or later. It checks unit moduli, the balanced zero-sum equations, all ten off-diagonal three-layer overlap identities, the two-layer pentagonal cosine identities, and the exact rank-four obstruction for one layer. These symbolic finite calculations mirror the proof; the stacking step is a direct exact identity valid for every integer \(R\geq2\), not a finite computational extrapolation.

## Relationship to prior work
Brinkley, Fickus, Jasper and Mixon introduce the SUNTF framework in *Incoherent filter banks*, arXiv:2610.05302v1 (first public version 4 October 2026), Definition 3.2. Their Example 3.3 provides a real two-layer system, and Example 4.4 provides a real five-layer system; by stacking, they establish existence for all \(R\geq4\) and explicitly identify the three-layer case as unsolved. The construction and rank obstruction above determine the exact threshold \(2\). Earlier general tight-fusion-frame existence results do not alone imply the aligned, layerwise stratification identities proved here.

## Limitations
Only the real \((D,N)=(2,5)\) family and the layer-count existence problem are classified. The proof does not assert uniqueness of the three-layer construction, classification of other parameters, or any equi-isoclinic property. Algebraic existence is proved without claiming that the particular system is uniquely optimal among other constructions or that its applications are quantitatively improved.

## References
1. W. J. Brinkley, M. Fickus, J. Jasper and D. G. Mixon, *Incoherent filter banks*, arXiv:2610.05302v1, 4 October 2026, Definition 3.2 and Examples 3.3, 4.4; https://arxiv.org/html/2610.05302v1.
2. W. J. Brinkley, *Grassmannian Codes from Stratified Frames*, M.S. thesis, Air Force Institute of Technology, 2025. Bibliographic precursor cited by reference 6 of item 1; https://scholar.afit.edu/etd/8306/. Its full text was not available for comparison.

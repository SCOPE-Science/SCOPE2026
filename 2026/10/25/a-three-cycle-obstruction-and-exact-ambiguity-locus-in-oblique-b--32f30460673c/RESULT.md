# A three-cycle obstruction and exact ambiguity locus in oblique box-section tomography

## Finding
Let \(d\ge3\) and let \(B(a)=\prod_{i=1}^d[-a_i/2,a_i/2]\) be an axis-aligned box with unknown positive, axis-labelled side lengths \(a_i\). Its *parallel-section function* in the unit normal direction \(u\) is
\[
A_{a,u}(t)=\operatorname{vol}_{d-1}\{z\in B(a):\langle z,u\rangle=t\},\qquad t\in\mathbb R.
\]
For **every** two unit normals \(u,v\) with all coordinates nonzero, there exist two distinct such boxes of the same total volume whose two entire parallel-section functions coincide, including at every noncentral offset. The obstruction is a three-coordinate permutation switch; it is not eliminated by knowing the total volume.

In dimension three a complete classification is possible. Put \(p_i=|u_i|\) and \(r_i=|v_i|/p_i\). Suppose the three positive ratios \(r_1,r_2,r_3\) are pairwise distinct. Apart from identical boxes, **all** pairs with identical complete section data in the two normals are, for a unique positive scale \(c\), precisely the unordered pair whose side-length vectors are
\[
\boxed{\quad a= c\left(\frac{r_2}{p_1},\frac{r_3}{p_2},\frac{r_1}{p_3}\right),\qquad
 b=c\left(\frac{r_3}{p_1},\frac{r_1}{p_2},\frac{r_2}{p_3}\right).\quad}
\]
Here uniqueness of \(c\) refers to a specified unequal pair; varying \(c\) gives the entire exceptional locus. Thus a generic full-support pair of views is one-to-one except for exactly one scale family of two-to-one fibers. Three fixed full-support directions suffice for *every* axis-aligned box in dimension three, so the sharp minimum among such oblique viewing schemes is three. Explicitly, one may use the unit normalizations of \((1,1,1)\), \((1,2,1)\), and \((1,1,2)\).

## Assumptions and scope
The coordinate frame and centering of the box are known and fixed; the side lengths are positive but not presumed ordered. Equality means pointwise equality of the full section functions for all \(t\in\mathbb R\), not just central sections and not X-rays along lines. Directions are fixed in advance, independently of the unknown box. The lower bound requires two *full-support* directions, i.e. all their coordinates are nonzero. The exact two-to-one classification is for dimension three with distinct absolute coordinate ratios; the universal two-view obstruction holds for every \(d\ge3\), including ratio coincidences. The third-view sufficiency statement is confined to dimension three. No statement of a three-view threshold is made for higher dimensions or arbitrary-oriented parallelotopes.

## Proof
**1. Exact information carried by one section profile.** The Fourier slice identity and Fubini's theorem give
\[
\int_{\mathbb R} e^{ist}A_{a,u}(t)\,dt
=\int_{B(a)}e^{is\langle z,u\rangle}\,dz
=\left(\prod_i a_i\right)\prod_i\operatorname{sinc}\left(\frac{s|u_i|a_i}{2}\right),
\]
where \(\operatorname{sinc}(z)=\sin(z)/z\), with value one at zero. Integrating the profile recovers the box volume. Furthermore, near zero, the Weierstrass product for sine implies
\[
\log\operatorname{sinc}(z)=-\sum_{k\ge1}\frac{\zeta(2k)}{k\pi^{2k}}z^{2k}.
\]
All displayed coefficients are nonzero. Consequently the derivatives through order \(2d\) of the normalized Fourier transform recover the first \(d\) power sums of \((|u_i|a_i)^2\). Newton's identities recover the multiset \(\{|u_i|a_i:1\le i\le d\}\), with multiplicities. Conversely that multiset together with the volume determines the entire section function by the product formula. When all coordinates of \(u\) are nonzero, the volume is already determined by this multiset because \(\prod_i a_i=\prod_i (|u_i|a_i)/\prod_i |u_i|\). Therefore a full-support section profile is equivalent to the multiset of positive weighted widths.

**2. A two-view switch in every dimension at least three.** Set \(p_i=|u_i|\) and \(r_i=|v_i|/p_i>0\). On any selected three axes (relabelled \(1,2,3\)), define two first-view weighted-width triples
\[
 x=c(r_2,r_3,r_1),\qquad y=c(r_3,r_1,r_2),\qquad c>0.
\]
These are permutations. Their second-view weighted widths also coincide as multisets, because
\[
 (r_1x_1,r_2x_2,r_3x_3)
 =c(r_1r_2,r_2r_3,r_3r_1),
\]
while
\[
 (r_1y_1,r_2y_2,r_3y_3)
 =c(r_1r_3,r_2r_1,r_3r_2).
\]
Both volume products agree. Divide the first-view widths by \(p_i\) to obtain two box side-length vectors, assigning all remaining \(d-3\) side lengths identically. If the ratios are not all equal, choose a triple containing unequal ratios; then the boxes differ. If all ratios are equal, take any unequal positive weighted widths on two axes and interchange them instead: both views again agree. This proves the universal full-support two-view obstruction.

The boxes need not even be congruent. For unnormalized view vectors \((1,2,3)\) and \((2,3,5)\) in \(\mathbb R^3\) (normalization only rescales the profile coordinate \(t\)), an explicit pair is
\[
\left(\frac32,\frac56,\frac23\right),\qquad
\left(\frac53,1,\frac12\right).
\]
They both have volume \(5/6\). The first weighted-width multisets are \(\{3/2,5/3,2\}\), and the second are \(\{3,5/2,10/3\}\). Their unordered actual side-length lists differ, so they are noncongruent.

**3. Completeness of the exceptional three-dimensional family.** Assume \(d=3\) and the \(r_i\) are pairwise distinct. If boxes \(a,b\) have identical first sections, set \(x_i=p_i a_i\) and \(y_i=p_i b_i\). Step 1 shows that \(y\) permutes \(x\). If the permutation is a transposition of indices \(i,j\), equality of the sums of second-view widths forces \((r_i-r_j)(x_i-x_j)=0\), so the swap changes no coordinate and \(a=b\). Thus any distinct pair must be related by a three-cycle.

For the cycle \(y=(x_2,x_3,x_1)\), equality of the first two elementary symmetric functions of \((r_1x_1,r_2x_2,r_3x_3)\) and \((r_1x_2,r_2x_3,r_3x_1)\) gives two identities. The first is
\[
(r_1-r_3)x_1+(r_2-r_1)x_2+(r_3-r_2)x_3=0.
\]
Eliminate \(x_1\) from the second identity using the first. Exact factorization gives
\[
\frac{(r_1-r_2)(r_2-r_3)}{r_1-r_3}
 (x_2-x_3)(r_1x_2-r_3x_3)=0.
\]
Distinctness of the \(r_i\) makes the prefactor nonzero. If \(x_2=x_3\), the first identity yields \(x_1=x_2=x_3\), hence \(y=x\). Otherwise \(r_1x_2=r_3x_3\) and substitution yields \(x_1=(r_2/r_1)x_3\): precisely \(x=c(r_2,r_3,r_1)\) and \(y=c(r_3,r_1,r_2)\). The inverse three-cycle reverses the same unordered pair. The degree-three elementary symmetric functions agree automatically, because both weighted triples have the same coordinate product. Hence these and only these exceptional pairs have equal second-view width multisets. Step 1 transfers the classification to entire section functions.

**4. Three explicit oblique directions recover the box.** For any unit normal \(u\), the normalized second moment of its complete section profile is
\[
\frac{\int t^2 A_{a,u}(t)\,dt}{\int A_{a,u}(t)\,dt}
 =\frac1{12}\sum_{i=1}^3u_i^2a_i^2.
\]
This follows by independently integrating the centered uniform coordinate variables on the box. For the three proposed directions the coefficient matrix of the squared side lengths is
\[
 M=\begin{pmatrix}1/3&1/3&1/3\\1/6&4/6&1/6\\1/6&1/6&4/6\end{pmatrix},\qquad \det M=1/12\ne0.
\]
In fact \(M^{-1}=\begin{pmatrix}5&-2&-2\\-1&2&0\\-1&0&2\end{pmatrix}\). Thus the three variances recover the positive \(a_i^2\), hence the labelled side lengths. Steps 2 and 4 prove sharpness among full-support triples in dimension three.

## Verification
Run `python verify.py` in the same directory as this document, using Python 3 and SymPy. It verifies the symbolic factorization for arbitrary indeterminate ratios, the elementary-symmetric equalities of the exceptional pair, an exhaustive six-permutation check for a rational ratio triple, and the determinant and inversion of the three-view second-moment matrix. These computations test the algebra but do not substitute for the general proof. The proof's only analytic ingredient is the standard sine-product expansion, explicitly displayed above.

## Relationship to prior work
Fish, Ryabogin, Sun and Yaskin (arXiv:2610.10229v1, 2026-10-07) study determination from parallel-section functions and prove rigidity results involving a continuum of directions or infinitely many offsets. Their paper provides the motivating inverse problem and terminology; its statements do not classify the finite, fixed, two-oblique-direction data for coordinate boxes. A distinct recent finding, *Sharp finite-moment tomography of orthotopes in every dimension* (published-finding corpus, 2026-10-11), reconstructs **unordered** side lengths from moments of random **projection volumes**; it does not address axis-labelled sides from fixed-direction complete **section** profiles, nor the above exceptional two-to-one locus. Gardner and Gritzmann (1997) address lattice-point X-rays of finite sets, and the classical box-spline literature treats convolution representations; neither accessible result directly gives this continuous two-view axis-labelled classification. Full-source equivalence beyond the materials inspected remains a literature risk.

## Limitations
A pair of normals with zero coordinates falls outside the two-view obstruction: for example, two coordinate-axis section profiles already determine a three-dimensional axis-aligned box, using widths and total volume. The exact classification assumes pairwise distinct ratios; coincident ratios can cause additional ambiguity. For \(d>3\), only the universal two-view failure is asserted, not a universal sharp minimum number of full-support directions. The normals and coordinate axes are known exactly, and no robustness or noisy-measurement bounds are proved. The mathematical novelty has not been independently certified; unindexed classical tomography or spline literature could contain an equivalent description.

## References
1. A. Fish, D. Ryabogin, W. R. Sun and V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1, submitted 2026-10-07, especially pp. 1–4 and the rigidity results in Sections 4–6. https://arxiv.org/abs/2610.10229
2. *Sharp finite-moment tomography of orthotopes in every dimension*, publicly available geometric research finding (2026-10-11). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-finite-moment-tomography-of-orthotopes-in-every-dimension--cb0a2e3c75db
3. R. J. Gardner, *Geometric Tomography*, second edition, Cambridge University Press, 2006, Chapters 1–2 and 7 (background; not asserted to have been inspected in full). https://doi.org/10.1017/CBO9781107341029
4. R. J. Gardner and P. Gritzmann, *Discrete tomography: Determination of finite sets by X-rays*, Transactions of the AMS, 1997 (different object and different X-ray data). https://portal.fis.tum.de/en/publications/discrete-tomography-determination-of-finite-sets-by-x-rays/
5. C. de Boor, K. Höllig and S. Riemenschneider, *Box Splines*, Springer, 1993 (standard spline-background text; not inspected in full). https://doi.org/10.1007/978-1-4757-2244-1

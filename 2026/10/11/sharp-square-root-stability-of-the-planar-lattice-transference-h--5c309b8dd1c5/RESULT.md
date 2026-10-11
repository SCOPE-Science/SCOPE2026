# Sharp square-root stability of the planar lattice-transference hexagon in its blocking chamber

## Finding
Let the six lattice points, indexed cyclically modulo six, be
\[
q_0=(-1,-1),\ q_1=(0,-1),\ q_2=(1,0),\ q_3=(1,1),\ q_4=(0,1),\ q_5=(-1,0),
\]
and write \(r_i=q_{i-1}+q_i\) and \(S_i=\operatorname{conv}\{q_{i-1},r_i,q_i\}\). Consider any origin-symmetric *convex hexagon* \(K=\operatorname{conv}\{p_0,\ldots,p_5\}\) whose vertices occur in the stated cyclic order, satisfy \(p_i\in\operatorname{int}(S_i)\), and for which \(q_i\in[p_i,p_{i+1}]\) for every \(i\). Put
\[
H=\operatorname{conv}\{(q_{i-1}+r_i+q_i)/3:0\le i<6\}
=\tfrac23\operatorname{conv}\{\pm(2,1),\pm(1,2),\pm(-1,1)\}.
\]
With successive-minimum notation relative to \(\mathbb Z^2\), let
\[
\varepsilon(K)=\frac43-\lambda_1(K)\lambda_1(K^*).
\]
Then \(\varepsilon(K)\ge0\). If \(\varepsilon(K)\le1/90\), the ordinary Euclidean Hausdorff distance satisfies
\[
\boxed{d_{\mathrm H}(K,H)\le10\sqrt{\varepsilon(K)}.}
\]
The power \(1/2\) is optimal *within this same blocking chamber*: a continuous family \(K_t\) of such hexagons for \(0<|t|\le1/10\) has \(\varepsilon(K_t)\to0\) and
\[
d_{\mathrm H}(K_t,H)\ge\tfrac14\sqrt{\varepsilon(K_t)}.
\]
This is a chamberwise normalized quantitative statement; it does not assert globally uniform stability under arbitrary lattice coordinate changes or for other blocking configurations.

## Assumptions and scope
The polar \(K^*=\{y:\langle x,y\rangle\le1\ \forall x\in K\}\) is taken with respect to the standard Euclidean pairing, and \(\lambda_1(C)=\inf\{s>0:(sC)\cap(\mathbb Z^2\setminus\{0\})\ne\varnothing\}\). The lattice width is \(w(C)=\min_{z\in\mathbb Z^2\setminus\{0\}}\bigl(\max_{x\in C}\langle z,x\rangle-\min_{x\in C}\langle z,x\rangle\bigr)\). Thus for origin-symmetric \(C\), \(w(C)=2\lambda_1(C^*)\). Euclidean Hausdorff distance is the supremum distance between corresponding support functions over unit directions.

All assumptions on \(K\) in the Finding are required, in particular the exact six boundary blockers and the fixed lattice normalization. Write uniquely
\[
p_i=a_iq_{i-1}+b_ir_i+c_iq_i,\qquad a_i,b_i,c_i>0,\quad a_i+b_i+c_i=1.
\]
Central symmetry gives \((a_{i+3},b_{i+3},c_{i+3})=(a_i,b_i,c_i)\). Set \(m=\min\{b_0,b_1,b_2\}\). The parameter \(\varepsilon\) above is exactly \(1/3-m\).

## Proof
**1. Lattice normalization and deficit.** Define \(R=\operatorname{conv}\{r_0,\ldots,r_5\}\). Its complete set of lattice points is
\[
R\cap\mathbb Z^2=\{0\}\cup\{q_0,\ldots,q_5\}\cup\{r_0,\ldots,r_5\}.
\]
This follows by the six edge half-plane tests on the integer box \([-2,2]^2\); the standalone checker makes the complete 25-point test exact. We have \(K\subset R\), no \(r_i\) belongs to \(K\), and all \(q_i\) lie on its boundary; therefore \(0\) is its unique interior lattice point and \(\lambda_1(K)=1\). For a primitive \(z=(z_1,z_2)\in\mathbb Z^2\),
\[
w(\operatorname{conv}\{q_i\},z)=2\max\{|z_1|,|z_2|,|z_1+z_2|\}.
\]
Unless \(z\) is, up to sign, \((1,0),(0,1),(1,-1)\), this width is at least four. In the three exceptional directions the supporting vertices give exactly the three widths \(2+2b_0,2+2b_1,2+2b_2\), each less than four. Hence
\[
w(K)=2+2m,\quad \lambda_1(K)\lambda_1(K^*)=1+m,\quad \varepsilon=\tfrac13-m.
\]

**2. Exact collinearity identity.** Using \(r_i=q_{i-1}+q_i\) and \(q_{i+1}=q_i-q_{i-1}\), the determinant of \(p_i-q_i\) and \(p_{i+1}-q_i\) vanishes precisely when \(b_i b_{i+1}=a_i c_{i+1}\). Multiply these six identities and use antipodal symmetry and positivity to obtain
\[
(b_0b_1b_2)^2=(a_0c_0)(a_1c_1)(a_2c_2).\tag{1}
\]
The arithmetic–geometric mean bound \(a_ib_ic_i\le1/27\) and (1) imply \(b_0b_1b_2\le1/27\). Furthermore,
\[
\prod_{i=0}^2\frac{2b_i}{1-b_i}\le1.
\]
If all three \(b_i>1/3\), the last product would exceed one. Thus \(m\le1/3\), proving \(\varepsilon\ge0\).

**3. Quantitative control of every barycentric coordinate.** Assume \(0\le\varepsilon\le1/90\). Since each \(b_i\ge m=1/3-\varepsilon\) and \(\prod b_i\le1/27\),
\[
\frac13-\varepsilon\le b_i\le\frac1{27(1/3-\varepsilon)^2}
=\frac1{3(1-3\varepsilon)^2}\le\frac13+3\varepsilon.\tag{2}
\]
The final comparison follows on this stated interval by multiplying by the positive denominator and using \(27\varepsilon^2-15\varepsilon+1\ge0\).

Set \(d_i=a_i-c_i\) and \(T=\prod_{i=0}^2\frac{2b_i}{1-b_i}\). Identity (1) gives the exact factorization
\[
T^2=\prod_{i=0}^2\left(1-\frac{d_i^2}{(1-b_i)^2}\right).\tag{3}
\]
Every factor is in \((0,1]\). Because \(b_i\ge1/3-\varepsilon\),
\[
T\ge\left(\frac{1-3\varepsilon}{1+3\varepsilon/2}\right)^3
\ge(1-\tfrac92\varepsilon)^3,
\quad 1-T^2\le27\varepsilon.\tag{4}
\]
The last step uses Bernoulli's inequality and \(0\le\varepsilon\le1/90\). Each factor in (3) is at least their product, so \(|d_i|\le(1-b_i)\sqrt{27\varepsilon}\le\sqrt{27\varepsilon}\). Combining this with (2) and \(a_i=(1-b_i+d_i)/2\), \(c_i=(1-b_i-d_i)/2\), yields
\[
|a_i-1/3|,\ |c_i-1/3|\le\frac{3\varepsilon+\sqrt{27\varepsilon}}2\le3\sqrt\varepsilon,
\qquad |b_i-1/3|\le3\varepsilon.\tag{5}
\]
The estimates apply to all six indices by antipodal symmetry. As \(\|q_i\|\le\sqrt2\) and \(\|r_i\|\le\sqrt5\), corresponding vertices of \(K\) and \(H\) satisfy
\[
\|p_i-(q_{i-1}+r_i+q_i)/3\|
\le6\sqrt2\sqrt\varepsilon+3\sqrt5\varepsilon
\le10\sqrt\varepsilon.\tag{6}
\]
Convex combinations of corresponding vertices give both Hausdorff inclusions and the claimed bound.

**4. Sharpness within the same class.** For \(0<|t|\le1/10\), define
\[
 b(t)=\frac{-1+2\sqrt{1-3t^2}}3,\qquad
 a(t)=\frac{1-b(t)}2+t,\qquad
 c(t)=\frac{1-b(t)}2-t,
\]
\[
p_i(t)=a(t)q_{i-1}+b(t)r_i+c(t)q_i,
\qquad K_t=\operatorname{conv}\{p_0(t),\ldots,p_5(t)\}.
\]
All coefficients are positive and sum to one, and direct expansion gives \(a(t)c(t)=b(t)^2\). Therefore every \(q_i\) lies strictly on the segment joining \(p_i(t)\) and \(p_{i+1}(t)\); successive oriented edge determinants equal \(1+b(t)>0\), so \(K_t\) is an admissible centrally symmetric convex hexagon. The exact deficit is
\[
\varepsilon(K_t)=\frac23\bigl(1-\sqrt{1-3t^2}\bigr),
\qquad t^2\le\varepsilon(K_t)\le2t^2.
\]
For \(u=(-1,-1)/\sqrt2\), the supports obey \(h_H(u)=\sqrt2\) and
\[
h_{K_t}(u)=\frac{1+\sqrt{1-3t^2}+|t|}{\sqrt2}.
\]
Hence, since \(1-\sqrt{1-3t^2}\le3t^2\),
\[
d_{\mathrm H}(K_t,H)\ge h_{K_t}(u)-h_H(u)
\ge\frac{|t|-3t^2}{\sqrt2}\ge\frac{|t|}{2\sqrt2}
\ge\frac14\sqrt{\varepsilon(K_t)}.
\]
No estimate \(d_{\mathrm H}(K,H)\le C\varepsilon(K)^\beta\) can hold uniformly over this class near \(H\) with any fixed \(\beta>1/2\), because \(\varepsilon(K_t)\asymp t^2\) while the distance is bounded below by a positive multiple of \(|t|\).

## Verification
Run the standalone standard-library program `python verify.py`. It exhaustively enumerates all 25 lattice candidates in the auxiliary bounding square; then checks collinearity, central symmetry, positive barycentric coordinates, the product identity, all three short-direction widths, and the Hausdorff bound in 1500 independently generated exact-rational admissible blocking hexagons. Finally, it checks 201 rational sample parameters of the sharpness family using rational square-root enclosures. The program returns `VERIFY_OK`. These finite tests are **not** a proof for infinitely many parameters; the analytic argument above establishes that claim.

## Relationship to prior work
Averkov, Codenotti, Freyer and Huang (2026), Theorem 1.4, prove the sharp universal planar bound \(\lambda_1(K)\lambda_1(K^*)\le4/3\) and identify the same normalized hexagon as the unique extremizer up to unimodular maps and scaling. Their Section 4.2 supplies the blocking-region parametrization and an exact product identity but does not state a Hausdorff near-equality modulus or exhibit its optimal exponent. The present result uses their natural six-blocker chamber and develops a quantitative near-equality estimate together with a nontrivial sharpness deformation. Bárány and Füredi (2001) had previously established a related lattice-width/lattice-diameter estimate; the available abstract and the cited comparison in the 2026 paper do not determine the chamberwise Hausdorff stability exponent. The full earlier article was not reliably available for exhaustive comparison.

## Limitations
This is a local normalized statement conditional on belonging to the specified six-blocker chamber, not a global stability theorem for all planar symmetric convex bodies. It does not optimize the constant \(10\), determine the best small-deficit threshold, or claim that the exact equality shape is new. Possible earlier unpublished or unindexed variants of the quantitative estimate remain an originality risk. The finite checker does not certify the infinite analytic proof, and no independent audit has been performed.

## References
1. G. Averkov, G. Codenotti, A. Freyer, K. Huang, *Exact Flatness Constant for One-Point Convex Bodies and the Discrete Isominwidth Problem: The Planar Case*, arXiv:2604.27260v1 (2026), Theorem 1.4 and Section 4.2, https://arxiv.org/pdf/2604.27260.
2. I. Bárány, Z. Füredi, *On the lattice diameter of a convex polygon*, Discrete Mathematics **241** (2001), 41–50, https://doi.org/10.1016/S0012-365X(01)00145-5.

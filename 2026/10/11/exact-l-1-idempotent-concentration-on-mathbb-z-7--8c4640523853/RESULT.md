# Exact \(L^1\) idempotent concentration on \(\mathbb Z_7\)
## Finding
Let \(e_7(t)=\exp(2\pi i t/7)\). For every nonempty \(H\subseteq\mathbb Z_7\), put
\[
R_H(x)=\sum_{h\in H}e_7(hx),
\qquad
C(H)=\frac{2|R_H(1)|}{\sum_{x\in\mathbb Z_7}|R_H(x)|}.
\]
Then the unrestricted finite-cyclic endpoint concentration constant at the nonzero target is
\[
\gamma_1^{\sharp}(7)=\max_{\varnothing\ne H\subseteq\mathbb Z_7}C(H)=\gamma_*,
\]
where
\[
\gamma_*
=
\frac{2\bigl(1+2\cos(2\pi/7)\bigr)}
{5+4\bigl(\cos(2\pi/7)+\cos(4\pi/7)-\cos(6\pi/7)\bigr)}
=0.4402496918696974939591035885409904\ldots .
\]
Equivalently, \(\gamma_*\) is the unique positive root of
\[
97X^3+44X^2-20X-8=0.
\]
Equality holds exactly for the seven consecutive triples
\[
H=\{b,b+1,b+2\},\qquad b\in\mathbb Z_7.
\]
By multiplication of the variable by a nonzero residue, the same value is obtained at every nonzero target.

## Assumptions and scope
The group is \(\mathbb Z_7\), all sums in the denominator use ordinary counting measure, and the numerator is twice the mass at the selected nonzero target, matching the finite-group \(p=1\) concentration normalization. The zero idempotent is excluded because its ratio is undefined. No restriction on \(|H|\) is imposed in the maximum.

The result is finite and exact. It determines \(\gamma_1^{\sharp}(7)\); it does not determine \(\gamma_1^{\sharp}(q)\) for arbitrary prime \(q\), nor the uniform asymptotic constant.

## Proof
Write \(m=|H|\) and \(K_H(x)=R_H(x)\). For the complement \(H^c\), character orthogonality gives
\[
K_{H^c}(x)=-K_H(x)\quad(x\ne0),
\qquad K_H(0)=m,
\qquad K_{H^c}(0)=7-m.
\]
Thus \(H\) and \(H^c\) have the same numerator, while for \(m\le3\) the complement has a strictly larger denominator. It therefore suffices to consider \(m=1,2,3\).

For \(m=1\), every sample has modulus \(1\), hence
\[
C(H)=\frac27.
\]

For \(m=2\), translation reduces the support to \(\{0,d\}\). Multiplication by a unit permutes the denominator samples, so the denominator is independent of \(d\), while the numerator is maximized for \(d\equiv\pm1\pmod7\). The finite cosine sum gives
\[
rac{2|1+e_7(1)|}{\sum_{x=0}^6|1+e_7(x)|}
=2\sin(\pi/14)\cos(\pi/7)=:r_2.
\]
Eliminating the seventh-root trigonometric quantities gives
\[
8r_2^3+8r_2^2-2r_2-1=0.
\]
This polynomial has one positive root, and its value at \(41/100\) is \(9521/125000>0\), so \(r_2<41/100\).

Now let \(m=3\). The affine group of \(\mathbb Z_7\) has exactly two orbits on three-subsets. The arithmetic-progression orbit has \(21\) members and representative \(\{0,1,2\}\); the other orbit has \(14\) members and representative \(D=\{0,1,3\}\). Indeed the first orbit consists of the \(21\) sets \(\{b-d,b,b+d\}\), while the stabilizer of \(D\) has the three affine maps \((a,b)=(1,0),(2,1),(4,3)\), so its orbit has size \(42/3=14\). These disjoint orbits exhaust the \(35\) three-subsets.

For an arithmetic progression \(H=\{b,b+d,b+2d\}\), translation only modulates the samples and the denominator is independent of the nonzero step \(d\). For the representative with step \(1\),
\[
|1+e_7(x)+e_7(2x)|=|1+2\cos(2\pi x/7)|.
\]
The signs are positive for \(x\equiv0,\pm1,\pm2\) and negative for \(x\equiv\pm3\), hence the denominator is
\[
D_3=5+4\bigl(\cos(2\pi/7)+\cos(4\pi/7)-\cos(6\pi/7)\bigr).
\]
The target numerator is largest for \(d\equiv\pm1\), because the \(d\equiv\pm2\) value is \(2(1+2\cos(4\pi/7))\), while the \(d\equiv\pm3\) value is \(2(-1-2\cos(6\pi/7))<2\), whereas the \(d\equiv\pm1\) value is \(2(1+2\cos(2\pi/7))>2\). Therefore the best three-point arithmetic progression has ratio exactly \(\gamma_*\).

For \(D=\{0,1,3\}\), the six ordered nonzero differences run through every element of \(\mathbb Z_7\setminus\{0\}\) exactly once. Consequently, for every \(x\ne0\),
\[
|K_D(x)|^2
=3+\sum_{r=1}^6 e_7(rx)=2.
\]
Every affine image in this orbit therefore has the same nonzero sample modulus \(\sqrt2\), and its concentration ratio is
\[
r_D=rac{2\sqrt2}{3+6\sqrt2}=rac{8-2\sqrt2}{21}<\frac14.
\]

Finally, direct elimination in the real seventh-cyclotomic field gives
\[
97\gamma_*^3+44\gamma_*^2-20\gamma_*-8=0.
\]
The coefficient sign pattern has exactly one sign change, so there is exactly one positive root. The polynomial is negative at \(11/25\) and positive at \(441/1000\), hence
\[
\gamma_*\in(11/25,441/1000).
\]
Thus \(\gamma_*>11/25>41/100>r_2\), and also \(\gamma_*>2/7\) and \(\gamma_*>r_D\). The complement reduction then proves the unrestricted maximum. Equality in every reduction forces \(m=3\), the arithmetic-progression orbit, and step \(d\equiv\pm1\), which is precisely the seven sets \(\{b,b+1,b+2\}\).

## Verification
`artifacts/verify.py` exhausts all \(127\) nonzero subsets of \(\mathbb Z_7\), verifies that the only maximizers are the seven consecutive triples, checks the exact \(21+14\) affine-orbit decomposition of three-subsets, verifies the minimal polynomials and rational isolating inequalities used in the proof, and checks the difference-set Fourier identity. It uses the dependency versions listed in `artifacts/requirements.txt`.

A replay gives

`VERIFY_OK subsets=127 maximizers=7 three_orbits=21+14`

and

`gamma= 0.44024969186969749395910358854099048612028672420029`.

The exhaustive calculation is a finite cross-check; the reductions and exact inequalities above prove the claim.

## Relationship to prior work
Bonami and Révész formulate finite cyclic idempotent concentration, define the finite quantities \(\gamma_p^{\sharp}(q)\), and state that the best constants are not known for \(p\ne2\). Their work supplies the natural invariant evaluated here but does not give the exact \(q=7\), \(p=1\) value or its maximizers.

A published exact two-frequency result determines the cardinality-two slice for every cyclic group and explicitly leaves the unrestricted finite concentration constant open. The published exact projection norm for three consecutive characters determines the denominator \(D_3/7\) at \(N=7\), but it neither optimizes the point-concentration numerator over supports nor compares against all other spectral cardinalities. A separate seven-sample Fano-triple result optimizes a fixed-unimodular peak norm, a different objective. Graham records that three-subsets of \(\mathbb Z_7\) have two affine-equivalence classes and studies their Sidon constants; that does not determine the \(L^1\) point-concentration ratio.

## Limitations
The theorem is an exact small-modulus evaluation. It does not provide a formula for arbitrary prime modulus or improve the known asymptotic nonconcentration theorem. The proof exploits the complete subset geometry of \(\mathbb Z_7\), which does not scale directly to large primes. A residual originality risk remains that the same \(q=7\) finite constant may have appeared as an unindexed numerical or tabular calculation in older Littlewood or finite-idempotent literature, although the inspected primary and closely related sources did not state it.

## References
1. A. Bonami and Sz. Gy. Révész, *Integral Concentration of idempotent trigonometric polynomials with gaps*, arXiv:0707.3023v1, first public 2007-07-20. Primary MSC 42A05.
2. A. Bonami and Sz. Gy. Révész, *Concentration of the integral norm of idempotents*, arXiv:0811.4576v1, first public 2008-11-27.
3. published-finding corpus finding `aabfaa5078e3`, *Exact two-frequency \(L^1\) concentration on every cyclic group*.
4. published-finding corpus finding `b176a6018242`, *Exact three-frequency Fourier projection norm on every cyclic group*.
5. published-finding corpus finding `d1f94e9a8add`, *Exact seven-sample phase minimax for the Fano frequency triple*.
6. C. C. Graham, *A beastiary of sets having extremal Sidon constant, or, there must be more than one theorem somewhere here*, arXiv:1910.00924v1.

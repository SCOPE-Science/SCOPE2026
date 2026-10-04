# Sharp hyperbolic displacement for radial quasiconformal twists
## Finding
For \(0<r\le 1\), let
\[
T_\phi(re^{i\theta})=re^{i(\theta+\phi(r))},\qquad T_\phi(0)=0,
\]
where \(\phi:(0,1]\to\mathbb R\) is locally absolutely continuous, \(\phi(1)=0\), and
\[
S:=\operatorname*{ess\,sup}_{0<r<1} r|\phi'(r)|<\infty.
\]
Then \(T_\phi\) extends continuously to the closed disk, fixes the unit circle pointwise, and is quasiconformal with exact maximal dilatation
\[
K(T_\phi)=\left(\frac{\sqrt{S^2+4}+S}{2}\right)^2.
\]
With the Poincare metric normalized by \(d_{\mathbb D}(z,w)=2\operatorname{artanh}\rho(z,w)\), its maximal displacement satisfies the sharp inequality
\[
\sup_{z\in\mathbb D}d_{\mathbb D}(z,T_\phi z)\le \log K(T_\phi).
\]
For every \(c\ge0\), the logarithmic twist \(\phi_c(r)=c\log r\) attains equality in the supremum: \(\sup d_{\mathbb D}=\log K\).

## Assumptions and scope
The statement concerns radial angular shears only. The angular lift \(\phi\) is real-valued and locally absolutely continuous on \((0,1]\), with trace \(\phi(1)=0\). No boundedness of \(\phi\) near the origin is required because \(|T_\phi(z)|=|z|\), so continuity at \(0\) is automatic. The quantity \(S\) is an essential supremum. The result does not claim the same \(\log K\) displacement bound for arbitrary boundary-fixing quasiconformal self-maps of the disk.

## Proof
For \(r>0\), use the orthonormal polar frame \((e_r,e_\theta)\). After removing the harmless target rotation, the differential of \(T_\phi\) is the shear
\[
A(r)=\begin{pmatrix}1&0\\ r\phi'(r)&1\end{pmatrix}
\]
for almost every \(r\). Put \(s=r\phi'(r)\). Since \(\det A=1\), the product of the singular values is one. Direct diagonalization of \(A^*A\) gives the larger singular value
\[
\sigma_+(s)=\frac{\sqrt{s^2+4}+|s|}{2},
\]
so the pointwise linear dilatation is \(\sigma_+(s)^2\). This is increasing in \(|s|\), hence
\[
K(T_\phi)=\left(\frac{\sqrt{S^2+4}+S}{2}\right)^2.
\]
The inverse is obtained by replacing \(\phi\) by \(-\phi\), so the map is a homeomorphism; the finite essential bound above gives quasiconformality.

For two points on the same circle separated by angle \(\phi(r)\), the hyperbolic distance identity is
\[
\sinh\!\left(\frac{d_{\mathbb D}(re^{i\theta},T_\phi(re^{i\theta}))}{2}\right)
=\frac{2r|\sin(\phi(r)/2)|}{1-r^2}.
\]
Because \(\phi(1)=0\) and \(|\phi'(t)|\le S/t\) almost everywhere,
\[
|\phi(r)|\le S\log(1/r).
\]
Using \(|\sin u|\le |u|\) and the elementary inequality
\[
2r\log(1/r)\le 1-r^2\qquad(0<r<1),
\]
we obtain
\[
\sinh\!\left(\frac{d_{\mathbb D}(z,T_\phi z)}{2}\right)\le\frac S2.
\]
Thus
\[
d_{\mathbb D}(z,T_\phi z)\le2\operatorname{arsinh}(S/2)=\log K(T_\phi).
\]
The elementary inequality follows by differentiating \(1-r^2+2r\log r\), which is nonnegative on \((0,1]\).

For \(\phi_c(r)=c\log r\), one has \(r|\phi_c'(r)|=c\) almost everywhere. The preceding upper bound applies, while
\[
\frac{2r|\sin(c\log r/2)|}{1-r^2}\longrightarrow\frac c2
\qquad(r\uparrow1).
\]
Hence the displacement supremum equals \(2\operatorname{arsinh}(c/2)=\log K\), proving sharpness.

## Verification
The proof is analytic and covers every admissible \(\phi\); finite computation is not used to infer the theorem. The accompanying standard-library checker verifies the algebraic identity \(\log K=2\operatorname{arsinh}(S/2)\), samples the elementary envelope \(2r\log(1/r)\le1-r^2\), and numerically confirms approach to equality for five logarithmic twists. Its expected output is `VERIFY_OK identity_cases=7 envelope_points=9999 equality_families=5`.

## Relationship to prior work
Wu, arXiv:2609.32891v1 (2026), characterizes continuous preservers of Carleson interpolating sequences. In particular, Theorem 3.3 identifies the identity-boundary kernel with suitable pseudohyperbolically uniform disk homeomorphisms, and Theorem 3.18 notes that every quasiconformal disk homeomorphism with identity boundary values lies in that kernel. The paper also gives an exact dilatation formula for radial extensions of boundary circle maps, a different family from the radial angular shears treated here.

The older identity-boundary distortion literature studies Teichmuller's displacement problem for general quasiconformal self-maps. Vuorinen and Zhang, arXiv:1203.0427v3 and J. London Math. Soc. 90 (2014), survey the sharp planar disk problem and give general unit-ball estimates. Their displayed disk bounds are not the radial-twist identity above. The constant-slope logarithmic spiral mapping and its dilatation formula are classical; the equality witness is therefore not claimed as a new map. The contribution here is the exact variable-twist formula together with the sharp \(\sup d_{\mathbb D}\le\log K\) optimization for the whole radial-twist class and its placement inside the recent Carleson-preserver kernel.

## Limitations
The theorem is restricted to radius-preserving angular shears. It does not improve the sharp Krzyz bound for arbitrary boundary-fixing quasiconformal maps. The literature search did not locate an earlier statement of the exact variable-twist displacement inequality; because radial and spiral quasiconformal mappings are classical objects, an older equivalent formulation remains a residual originality risk. Independent audit has not been performed.

## References
1. J. Wu, *Characterizations and boundary regularity of continuous preservers of Carleson interpolating sequences*, arXiv:2609.32891v1, 26 Sep 2026.
2. M. Vuorinen and X. Zhang, *Distortion of quasiconformal mappings with identity boundary values*, arXiv:1203.0427v3; J. London Math. Soc. 90 (2014), 637--653, DOI 10.1112/jlms/jdu043.

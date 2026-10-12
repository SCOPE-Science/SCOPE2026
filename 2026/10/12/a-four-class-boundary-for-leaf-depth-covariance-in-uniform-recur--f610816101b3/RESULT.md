# A four-class boundary for leaf–depth covariance in uniform recursive trees

## Finding

Let \(T_n\) be the uniform random recursive tree on \(\{1,\ldots,n\}\), with vertex \(1\) its root and each vertex \(j\ge2\) independently attaching to a uniform parent in \(\{1,\ldots,j-1\}\). Write \(L_n\) for the number of vertices with no children, \(d(v)\) for root distance, and
\[
F_n(z)=\sum_{v=1}^{n}z^{d(v)},\qquad
N_{n,r}^{(q)}=\#\{v:d(v)\equiv r\pmod q\}.
\]
For every integer \(n\ge3\) and complex \(z\), the exact polynomial identity is
\[
\boxed{\operatorname{Cov}(L_n,F_n(z))=
\frac{(n-2)z(1-z)}4\prod_{j=3}^{n-1}\frac{j-1+z}{j}.}\tag{1}
\]
An empty product is \(1\). The identity also gives zero at \(n=2\).

For \(q=2\) the covariance is exactly
\[
\operatorname{Cov}(L_n,N_{n,0}^{(2)})=-\frac1{2(n-1)},\quad
\operatorname{Cov}(L_n,N_{n,1}^{(2)})=\frac1{2(n-1)}\qquad(n\ge3).
\tag{2}
\]
For any fixed integer \(q\ge3\), define \(\omega=e^{2\pi i/q}\), \(\alpha=\cos(2\pi/q)\), \(\beta=\sin(2\pi/q)>0\), and the nonzero constant
\[
A_q=\frac{\omega(1-\omega)}{2\Gamma(2+\omega)}.
\]
Uniformly over the finitely many residues \(r=0,\ldots,q-1\),
\[
\boxed{\operatorname{Cov}(L_n,N_{n,r}^{(q)})=
\frac{2}{q}n^{\alpha}\operatorname{Re}\!\left(A_q
 e^{i(\beta\log n-2\pi r/q)}\right)+o(n^{\alpha}).}\tag{3}
\]
Every residue covariance changes sign infinitely often. Its oscillation envelope tends to zero for \(q=3\), remains nonzero and bounded for \(q=4\), and grows without bound along subsequences for \(q\ge5\). Thus the **cross-covariance boundary occurs at modulus four**, unlike the modulus-six variance boundary for the unmarked depth profile.

## Assumptions and scope

The random attachment choices are independent and uniform. The root has depth zero. A leaf is a vertex with zero children (so the root is a leaf only at \(n=1\), which is not needed). The modulus \(q\) remains fixed while \(n\to\infty\). Complex covariance means \(\mathbb E[(L_n-\mathbb EL_n)(F_n(z)-\mathbb EF_n(z))]\), with no complex conjugate; the residue covariances are real. Formula (1) is a finite polynomial identity and remains meaningful at every complex \(z\). No growth-uniform assertion when \(q\) varies with \(n\) is made.

## Proof

**First moments.** Conditional on \(T_n\), the generating polynomial of all vertex depths obeys
\[
\mathbb E[F_{n+1}(z)\mid T_n]=(1+z/n)F_n(z).
\]
Writing \(a_n(z)=\mathbb EF_n(z)\), with \(a_1(z)=1\), gives
\[
a_n(z)=\prod_{j=1}^{n-1}(1+z/j).
\tag{4}
\]
Define the leaf-depth polynomial \(G_n(z)=\sum_{v\text{ leaf}}z^{d(v)}\) and \(b_n(z)=\mathbb EG_n(z)\). The new vertex is a leaf, and its chosen parent ceases to be a leaf if previously leaf; hence
\[
\mathbb E[G_{n+1}(z)\mid T_n]=(1-1/n)G_n(z)+(z/n)F_n(z).
\]
For \(n\ge2\), this recurrence, \(b_2(z)=z\), and (4) yield the polynomial identity
\[
(1+z)b_n(z)=za_n(z).
\tag{5}
\]
At \(z=1\), \(\mathbb EL_n=b_n(1)=n/2\), for \(n\ge2\).

**Mixed recurrence.** Write \(C_n(z)=\operatorname{Cov}(L_n,F_n(z))\). At step \(n+1\), choose parent \(V\) uniformly. Let \(I_V\) indicate that \(V\) was a leaf. Then
\[
L_{n+1}=L_n+1-I_V,\qquad F_{n+1}(z)=F_n(z)+z^{d(V)+1}.
\]
The conditional covariance of the increments is
\[
\operatorname{Cov}(1-I_V,z^{d(V)+1}\mid T_n)
=-\frac z nG_n(z)+\frac{z}{n^2}L_nF_n(z).
\]
Apply the law of total covariance, use the two conditional means above, (5), and \(\mathbb EL_n=n/2\). For \(n\ge2\),
\[
C_{n+1}(z)=\left(1+\frac{z-1}{n}\right)C_n(z)
+\frac{z(1-z)}{2n(1+z)}a_n(z),\qquad C_2(z)=0.
\tag{6}
\]
The apparent pole at \(z=-1\) is removable by (4)–(5). Let \(h_2(z)=1\) and \(h_n(z)=\prod_{j=2}^{n-1}(1+(z-1)/j)\). Then \(a_n(z)=(n+z-1)h_n(z)\) and \(h_{n+1}(z)=(n+z-1)h_n(z)/n\). Dividing (6) by \(h_{n+1}(z)\) yields the constant increment \(z(1-z)/(2(1+z))\). Therefore
\[
C_n(z)=\frac{(n-2)z(1-z)}{2(1+z)}h_n(z)
=\frac{(n-2)z(1-z)}4\prod_{j=3}^{n-1}\frac{j-1+z}{j},
\]
proving (1) first away from \(z=-1\), hence everywhere by polynomial identity.

**Residues and phase boundary.** Fourier inversion on \(\mathbb Z/q\mathbb Z\) gives
\[
N_{n,r}^{(q)}=\frac1q\sum_{\ell=0}^{q-1}\omega^{-r\ell}F_n(\omega^\ell).
\tag{7}
\]
Since \(C_n(1)=0\), the zeroth Fourier mode contributes nothing. At \(z=-1\), (1) telescopes to \(C_n(-1)=-1/(n-1)\); (2) follows.

For each fixed root of unity \(z\neq1\), (1) has the exact Gamma representation
\[
C_n(z)=\frac{(n-2)z(1-z)}{2\Gamma(2+z)}
\frac{\Gamma(n-1+z)}{\Gamma(n)},
\]
so the standard fixed-argument Gamma-ratio asymptotic gives
\[
C_n(z)=\frac{z(1-z)}{2\Gamma(2+z)}n^z(1+O(n^{-1})).
\tag{8}
\]
For \(q\ge3\), the only nonzero Fourier roots with maximum real part are \(\omega\) and \(\bar\omega\). They contribute the conjugate pair in (3); every other mode is \(o(n^\alpha)\). The constant \(A_q\) is nonzero because \(\omega\notin\{0,1\}\) and the Gamma function is finite and nonzero at \(2+\omega\). Since \(\beta>0\), for any desired phase \(\theta\) one may choose integers asymptotic to \(\exp((2\pi k+\theta)/\beta)\); then \(\beta\log n\to\theta\pmod{2\pi}\). Choosing opposite phases proves infinitely many positive and negative values for every residue. Finally, \(\alpha=-1/2\) when \(q=3\), \(\alpha=0\) when \(q=4\), and \(\alpha>0\) when \(q\ge5\). This proves the three magnitude regimes.

## Verification

`CHECK.py` independently enumerates all \((n-1)!\) parent-choice sequences through \(n=9\), computes the exact rational covariance coefficients, compares them to (1), checks the parity identity and the first derivative at \(z=1\), and verifies Fourier inversion for moduli \(2\) through \(9\). Run `python3 CHECK.py` in the directory containing this document and the checker. The checker uses only the Python standard library and reports 58 exact coefficient/identity checks and 352 finite Fourier checks. Finite enumeration is not a proof of the infinite asymptotics; those follow from (6)–(8).

## Relationship to prior work

Janson's 2005 paper (arXiv:math/0509471, first posted September 21, 2005) studies depth congruence classes of uniform recursive trees using a cyclic generalized urn. It establishes a variance/distribution boundary at modulus six, but its depth-profile result does not include the *mixed* covariance with the number of leaves. Van der Hofstad, Hooghiemstra, and Van Mieghem (2002) obtain exact covariances among depth-level sizes, not the mixed leaf/level statistic. Janson's 2004 work studies the outdegree-count profile, which includes the marginal number of leaves but not the depth-level mixed covariance. Marginal degree and depth formulas do not determine their joint covariance. A path-length covariance is obtained by differentiating (1) at \(z=1\); that scalar specialization is not presented as the novelty. The principal claim here is the fixed-modulus leaf/depth cross-covariance trichotomy and its sharp four-class boundary.

## Limitations

The theorem assumes uniform recursive attachment and fixed \(q\). It concerns covariance rather than distributional joint limits or causal relations. The oscillation is in \(\log n\), so finite samples can show long stretches of one sign. Historical coverage is not exhaustive: the full version of the 2002 level-covariance paper and the 2004 degree-profile paper were not available for complete comparison during this review, so implicit deductions in their general formulas remain a residual priority risk. In particular, neither a failed search nor the current self-review constitutes independent historical certification.

## References

- Svante Janson, *Congruence Properties of Depths in Some Random Trees*, arXiv:math/0509471v1, posted 2005-09-21, https://arxiv.org/abs/math/0509471 . Primary MSC 60C05.
- Remco van der Hofstad, Gerard Hooghiemstra, Piet Van Mieghem, *On the Covariance of the Level Sizes in Random Recursive Trees*, Random Structures & Algorithms 20 (2002), 519–539, https://doi.org/10.1002/rsa.10030 .
- Svante Janson, *Asymptotic Degree Distribution in Random Recursive Trees*, Random Structures & Algorithms 26 (2005), 69–83, first published 2004-11-16, https://doi.org/10.1002/rsa.20046 .
- Serdar Altok and Ümit Işlak, *On Leaf Related Statistics in Recursive Tree Models*, Statistics & Probability Letters 121 (2017), 61–69, https://doi.org/10.1016/j.spl.2016.10.007 .

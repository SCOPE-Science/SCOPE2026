# Residue-class theta asymptotics for commuting finite-field involutions

## Finding
Fix an odd prime-power \(q\). Among matrices \(U\in\mathrm{GL}_n(\mathbb F_q)\) with \(U^2=I\), include the identity. If \(U,V\) are independent uniform samples from this set, their commuting probability has a sharp four-residue asymptotic, with a quantitative multiplicative remainder:
\[
\Pr(UV=VU)=q^{-n^2/4}\frac{\Psi_\rho(q)}{\Phi_\infty(q)\Theta_\epsilon(q)^2}\left(1+O_q(q^{-n/8})\right),\quad\rho=n\bmod4,\quad\epsilon=n\bmod2.
\]
All limiting constants are positive, and the constants indexed by residues one and three are equal. The numerator is a theta series of the rank-three root lattice \(A_3\) shifted by a residue-dependent coset. The exact finite count is an already-known representation-orbit formula; the new assertion here is its fixed-field, growing-dimension asymptotic with residue-dependent leading constants and an error bound.

## Assumptions and scope
Throughout \(q\) is a fixed odd prime power, \(n\ge1\), and \(G_j=|\mathrm{GL}_j(\mathbb F_q)|\), with \(G_0=1\). Write \(\Phi_j=\prod_{h=1}^{j}(1-q^{-h})\), \(\Phi_\infty=\prod_{h\ge1}(1-q^{-h})>0\); then \(G_j=q^{j^2}\Phi_j\). Define absolutely convergent series
\[
\Theta_\epsilon=\sum_{t\in\mathbb Z+\epsilon/2}q^{-2t^2},\qquad
\Psi_\rho=\sum_{\substack{k_1,k_2,k_3,k_4\in\mathbb Z\\k_1+k_2+k_3+k_4=\rho}}q^{-\sum_{i=1}^4(k_i-\rho/4)^2},
\]
for \(\epsilon\in\{0,1\}\) and \(\rho\in\{0,1,2,3\}\). Here \(O_q\) means that a multiplicative constant may depend on \(q\) but not \(n\). These are *involutory elements*, not solely elements of group order exactly two.

## Proof
Since the characteristic is odd, every solution of \(U^2=I\) is semisimple with eigenvalues in \(\{1,-1\}\). For each ordered direct-sum decomposition \(\mathbb F_q^n=E_+\oplus E_-\), exactly one such \(U\) acts by the respective signs, and the number of decompositions of dimensions \(a,b\) is \(G_n/(G_aG_b)\). Consequently
\[
I_n=G_n\sum_{a+b=n}\frac1{G_aG_b}.
\]
For commuting \(U,V\), the four pairwise orthogonal idempotents \((I\pm U)(I\pm V)/4\) (with the signs independently chosen) produce the unique simultaneous eigenspace decomposition into four labeled blocks. Conversely every such decomposition determines precisely one commuting pair. Thus
\[
C_n=G_n\sum_{a+b+c+d=n}\frac1{G_aG_bG_cG_d}.
\]
This finite orbit calculation is standard for representations of the Klein four-group and is credited below.

For the involution sum, write \(a=n/2+t\), \(b=n/2-t\), where \(t\in\mathbb Z+\epsilon/2\) with the sign convention immaterial, and \(|t|\le n/2\). The identity \(a^2+b^2=n^2/2+2t^2\) yields
\[
\frac{I_n}{G_n}=q^{-n^2/2}\Phi_\infty^{-2}\bigl(\Theta_\epsilon+O_q(q^{-n/8})\bigr).
\]
Indeed \(\Phi_m/\Phi_\infty=1+O_q(q^{-m-1})\), obtained by bounding the tail of the convergent product. For summands where both \(a,b\ge n/4\), replacing the two \(\Phi\)-factors introduces relative error \(O_q(q^{-n/4})\). The omitted tails have \(|t|\ge n/4\), and their total Gaussian weight is \(O_q(q^{-n^2/8})\). Enlarging the implicit constant handles all finite \(n\).

Write \(n=4m+\rho\), \(0\le\rho<4\), and \((a,b,c,d)=(m+k_1,m+k_2,m+k_3,m+k_4)\), where \(\sum k_i=\rho\). Completing squares gives
\[
\sum_{i=1}^{4}(m+k_i)^2=\frac{n^2}{4}+\sum_{i=1}^{4}(k_i-\rho/4)^2.
\]
Thus
\[
\frac{C_n}{G_n}=q^{-n^2/4}\Phi_\infty^{-4}\bigl(\Psi_\rho+O_q(q^{-n/8})\bigr).
\]
To justify the stated uniform error, separate tuples with each of the four dimensions at least \(n/8\) from the remaining tuples. In the first region, replacing finite Euler factors by \(\Phi_\infty\) incurs \(O_q(q^{-n/8})\). If a dimension is smaller than \(n/8\), its deviation from \(n/4\) is at least \(n/8\); the Gaussian theta tail of squared deviation at least \(n^2/64\) is \(O_q(q^{-n^2/64})\), and is in particular \(O_q(q^{-n/8})\) as \(n\to\infty\). The four-dimensional hyperplane sum is absolutely convergent, permitting uniform comparison. The limiting theta sums have a strictly positive term and so additive errors are multiplicative ones.

The sought probability is \(C_n/I_n^2\). Insert the two formulas, cancel \(G_n=q^{n^2}\Phi_n\), and use \(\Phi_n=\Phi_\infty(1+O_q(q^{-n}))\). The remaining power is \(q^{-n^2/4}\), and the Euler factor is \(\Phi_\infty^{-1}\), proving the theorem. Replacing every integer \(k_i\) by \(1-k_i\) identifies \(\Psi_1\) with \(\Psi_3\); the corresponding one-dimensional theta series is the same because both residues are odd.

## Verification
Run `python verify_commuting_involutions.py` with Python 3. The checker constructs all involutory matrices and tests commutation directly for prime-field sizes \((q,n)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\); it compares them with the orbit sums and checks finite exact counts for dimensions through sixteen and the asymptotic constants on four residue sequences. The full input/output is embedded separately. Numerical convergence confirms, but does not prove, the asymptotic statement; the proof is the Gaussian-tail and Euler-product argument above.

## Relationship to prior work
Bate and Gullon (2017) give the representation-theoretic orbit count for arbitrary finite-group homomorphisms into general linear groups, so the finite four-block identity is not new. Their principal asymptotic identifies the leading polynomial degree and coefficient *as the field size varies*; it does not give the fixed-field, growing-dimension theta constant. Fulman, Guralnick, and Stanton (2016) analyze single involution counts and parity asymptotics, providing the natural one-variable antecedent. Baek and Han (2016) analyze commuting involution graph diameters and certain small-dimensional neighborhoods, rather than the global growing-dimension probability. Burness, Guralnick, Moretó, and Navarro (2021) give group-uniform bounds and qualitative convergence for commuting prime-power elements; they do not provide the residue-dependent sharp constant for this restricted probability.

## Limitations
The field characteristic must be odd. The result is for two independent uniformly sampled solutions of \(U^2=I\), including identity, and the limit sends dimension to infinity while fixing field size. The finite orbit formula is acknowledged as previously known. The asymptotic leading constant might admit a reformulation via earlier general homomorphism enumeration or modular theta-function literature; full bibliographic priority is not guaranteed. No assertion about characteristic two or independent validation is made.

## References
1. S. Baek and C. Han, *Commuting involution graphs of linear groups*, arXiv:1610.07938v1 (25 October 2016).
2. M. Bate and A. Gullon, *Asymptotic Bounds for the Size of Hom(A,GL_n(q))*, Glasgow Mathematical Journal, DOI:10.1017/S0017089516000562 (online 14 March 2017); freely accessible accepted manuscript at eprints.whiterose.ac.uk/id/eprint/113941/.
3. J. Fulman, R. Guralnick, D. Stanton, *Asymptotics of the number of involutions in finite classical groups*, arXiv:1602.03611v1 (11 February 2016).
4. T. C. Burness, R. M. Guralnick, A. Moretó, G. Navarro, *On the commuting probability of p-elements in a finite group*, arXiv:2112.08681v1 (16 December 2021).

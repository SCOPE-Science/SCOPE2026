# Bockstein equidistribution and image-shape counts for square-zero endomorphisms over length-two chain rings

## Finding
Let \(R\) be a finite commutative chain ring of length exactly two, with maximal ideal \((\pi)\), \(\pi^2=0\), and residue field \(k=R/(\pi)\) having \(q\) elements. Fix an integer \(n\ge1\). For each \(X\in M_n(R)\) with \(X^2=0\), let \(A=X\bmod\pi\), let \(r=\operatorname{rank}_k A\), and put \(s=n-2r\). Define \(H(A)=\ker A/\operatorname{im}A\), of dimension \(s\). There is an induced endomorphism \(\beta_X\in\operatorname{End}_kH(A)\), defined below relative to the fixed uniformizer. **For every fixed square-zero \(A\) of rank \(r\), each endomorphism of \(H(A)\) is induced by precisely \(q^{2r(n-r)}\) square-zero lifts.** Hence the induced map is uniformly distributed over the entire full matrix algebra, without any further nilpotence restriction. If \(t=\operatorname{rank}_k\beta_X\), then
\[
\operatorname{im}_R X\cong R^r\oplus k^t.
\]
Write \({a\brack b}_q=\prod_{i=0}^{b-1}(q^{a}-q^i)/(q^b-q^i)\) and \(|\mathrm{GL}_r(k)|=\prod_{i=0}^{r-1}(q^r-q^i)\), with empty products equal to one. For every \(0\le r\le\lfloor n/2\rfloor\) and \(0\le t\le n-2r\), the number of such \(X\) with reduction rank \(r\) and image module type \(R^r\oplus k^t\) is
\[
N_{n,q}(r,t)={n\brack r}_q{n-r\brack r}_q\left(\prod_{i=0}^{r-1}(q^r-q^i)\right)q^{2r(n-r)}{n-2r\brack t}_q\prod_{i=0}^{t-1}(q^{n-2r}-q^i).
\]
No other pairs occur. The full conditional similarity-invariant distribution of \(\beta_X\), not only its rank, is likewise that of a uniformly sampled \(s\)-by-\(s\) matrix over \(k\).

## Assumptions and scope
The ring \(R\) is unital, finite, commutative, and principal local with the strict ideal chain \(R\supsetneq\pi R\supsetneq0\). Thus \(\operatorname{ann}_R(\pi)=\pi R\), and multiplication by \(\pi\) identifies \(k\) with \(\pi R\) as a \(k\)-vector space. No ring characteristic, splitting, or coefficient-field hypothesis is needed. Elements of \(k\) act on \(\pi R\) independently of their chosen representatives. The image module is considered as an \(R\)-module, and \(k^t\) denotes \(t\) copies of \(R/\pi R\). All matrices are labeled; no simultaneous-similarity orbit counts are asserted.

Given \(v\in\ker A\), select any lift \(\widetilde v\in R^n\) of \(v\). Since \(A v=0\), there is a unique \(z\in k^n\) with \(X\widetilde v=\pi\widetilde z\), where \(\pi\widetilde z\) is independent of the lift of \(z\). As \(X^2=0\), reduction of \(X(\pi\widetilde z)=0\) implies \(Az=0\). Set \(\beta_X([v])=[z]\) in \(H(A)\). Replacing \(\widetilde v\) by \(\widetilde v+\pi\widetilde w\) changes \(z\) by \(Aw\), and replacing \(v\) by \(v+Au\) can be implemented by replacing \(\widetilde v\) by \(\widetilde v+X\widetilde u\), whose image changes by \(X^2\widetilde u=0\). This proves \(\beta_X\) is a well-defined \(k\)-linear map. Changing \(\pi\) to a unit multiple scales it by a nonzero residue scalar, preserving its rank and uniformity.

## Proof
**1. Reduction and counting its square-zero forms.** Since \(A^2=0\), its image \(U\) is contained in its kernel \(K\). Fix \(r=\dim_kU\). Choose \(U\) in \({n\brack r}_q\) ways, choose the \((n-r)\)-dimensional subspace \(K\supset U\) in \({n-r\brack r}_q\) ways, and then choose the induced isomorphism \(k^n/K\to U\) in \(|\mathrm{GL}_r(k)|\) ways. Therefore the number of rank-\(r\) square-zero \(A\) is
\[
T_{n,q}(r)={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(k)|.
\]

**2. Lifting equations and free secondary data.** A change of basis over \(k\) conjugates \(A\) to a direct sum of \(r\) nilpotent two-blocks and \(s=n-2r\) zero one-blocks. Lift the basis change to \(\mathrm{GL}_n(R)\), and use a decomposition \(R^n=E\oplus F\oplus G\) with respective dimensions \(r,r,s\). Let \(N:F\to E\) be the identity and let \(N\) vanish on \(E\oplus G\); it is a fixed square-zero lift of \(A\). Any other lift has a unique form \(X=N+\pi Y\), with \(Y\in M_n(k)\) (here \(\pi Y\) is independent of representative choices). Multiplying gives \(X^2=\pi(NY+YN)\), so the square-zero equation imposes exactly
\[
Y_{FE}=Y_{FG}=Y_{GE}=0,\qquad Y_{FF}=-Y_{EE}.
\]
These equations hold in every residue characteristic. The free blocks are \(Y_{EE},Y_{EF},Y_{EG},Y_{GF},Y_{GG}\). Their total number of scalar entries is \(2r^2+2rs+s^2=2r(n-r)+s^2\). Since \(H(A)\) identifies with the residual block \(G/\pi G\), the induced endomorphism \(\beta_X\) is exactly \(Y_{GG}\). Hence a *prescribed arbitrary* \(s\)-by-\(s\) matrix \(\beta_X\) has exactly \(q^{2r(n-r)}\) lifts. This also includes \(r=0\) and \(s=0\).

**3. Image shape.** Select the \(r\) unit pivots of the block \(X_{EF}=I_r+\pi Y_{EF}\); its \(R\)-module image contributes \(R^r\). Invertible elementary row and column operations remove the remaining entries in the corresponding rows and columns. The residual lower-right block is \(\pi Y_{GG}\), because all other nonzero terms are divisible by \(\pi\) and every product of two such terms vanishes. Its image is \(k^t\) where \(t=\operatorname{rank}_kY_{GG}\). This yields the asserted module decomposition.

**4. Finite-field rank spectrum.** The number of \(s\)-by-\(s\) matrices over \(k\) of rank exactly \(t\) is \({s\brack t}_q\prod_{i=0}^{t-1}(q^s-q^i)\): choose the image subspace and then a surjective linear map onto it. Multiply this by the number of choices of \(A\) in Step 1 and by the constant fiber size in Step 2 to obtain the formula. The argument treats all pairs of integers in the stated ranges and proves no others are possible.

## Verification
The companion standalone Python program `verify.py` constructs finite rings with actual arithmetic, enumerates actual square-zero matrices, computes image cardinalities through their action on all module vectors, and compares the joint counts with the formula. Test cases include \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/9\mathbb Z\), \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\), \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\), and \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\), for the declared small matrix dimensions. Run `python3 verify.py`; it prints `VERIFY_OK_SQUARE_ZERO_CHAIN2_SHAPE` upon success. The universal result rests on the proof, not on extrapolation from enumerations.

## Relationship to prior work
Hua (1999) treats polynomial equations over finite fields, including square-zero matrices over fields. Honold--Landjev (1999) and Feng--Nóbrega--Kschischang--Silva (2013/2014) establish general matrix and module-shape theory over finite chain rings. Bleher--Chinburg--Huisgen-Zimmermann (2014) study representation varieties for square-zero-radical algebras over fields. Existing square-zero-lift enumerations already determine the aggregate count indexed by \(r\) for equal-characteristic dual numbers; **this aggregate is not claimed new**. The contribution isolated here is the intrinsic secondary-endomorphism uniformity at *each fixed reduction*, its complete image-module-shape refinement, and the equal-/mixed-characteristic ring-independence. A possible equivalent argument within older matrix-equation literature has not been ruled out.

## Limitations
The chain-ring length must be exactly two; arbitrary longer length, non-chain local rings, and conjugacy orbits are not covered. The secondary map depends on a chosen uniformizer up to scalar. The result concerns labeled matrices, not inequivalent \(R[x]/(x^2)\)-module structures. Full historical priority remains uncertain because relevant older papers could be checked only at abstract level. Independent validation has not been performed.

## References
1. J. Hua, *Polynomial equations for matrices over finite fields*, Bull. Austral. Math. Soc. 59 (1999), available at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/68B94681BE3A9AE1AB2584266673AAA9/S0004972700032603a.pdf/polynomial-equations-for-matrices-over-finite-fields.pdf.
2. T. Honold and I. Landjev, *Linear Codes over Finite Chain Rings*, Electronic Journal of Combinatorics, publication page dated 1999-12-18, https://doi.org/10.37236/1489.
3. C. Feng, R. W. Nóbrega, F. R. Kschischang, D. Silva, *Communication over Finite-Chain-Ring Matrix Channels*, arXiv:1304.2523, https://arxiv.org/abs/1304.2523.
4. F. M. Bleher, T. Chinburg and B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045, https://arxiv.org/abs/1407.3045.
5. J. Cheong, J. Liang and M. Strand, *Polynomial equations for matrices over integers modulo a prime power and the cokernel of a random matrix*, arXiv:2209.03626, https://arxiv.org/abs/2209.03626 (square-free reduction hypothesis excludes the quadratic polynomial here).
6. D. Brawley, *Counting Matrices by Drazin Index*, SIAM J. Algebraic Discrete Methods (1982), https://doi.org/10.1137/0603003 (abstract only inspected).
7. D. Dafni and L. N. Vaserstein, *Matrix zeros of quadratic equations*, J. Algebra (1988), https://doi.org/10.1016/0022-314X(88)90024-8 (abstract only inspected).

# Exact nonzero Jordan structure and resonance for multivariable Rhaly operators

## Finding

Let \(d\ge 1\), choose a coordinate \(j\in\{1,\ldots,d\}\), and let \(a=(a_N)_{N\ge0}\subset\mathbb C\) satisfy
\[
 \sum_{N=0}^{\infty}(N+1)^d|a_N|<\infty.
\]
On the Drury–Arveson space \(H_d^2\), define the homogeneous Rhaly operator
\[
 R_{j,a}f=\sum_{N\ge0}a_N\sum_{m=0}^Nz_j^{N-m}f_m,
 \qquad f=\sum_{m\ge0}f_m,
\]
where \(f_m\) is homogeneous of total degree \(m\). Write
\[
 D_d(N)=\binom{N+d-1}{d-1}.
\]
Then \(R_{j,a}\) is trace class, its nonzero spectrum is exactly the set of nonzero \(a_N\), and
\[
 \det(I-zR_{j,a})=\prod_{N=0}^{\infty}(1-za_N)^{D_d(N)},
 \qquad \operatorname{Tr}(R_{j,a}^{k})=\sum_{N\ge0}D_d(N)a_N^k\quad(k\ge1).
\]

More precisely, fix a nonzero eigenvalue \(\lambda\), list the *finitely many* indices where it occurs as \(n_1<\cdots<n_s\), and set \(M=n_s\). For a multi-index \(\beta\in\mathbb N_0^{d-1}\) of degree \(r=|\beta|\le M\), put
\[
 b_\beta(\lambda)=\#\{i: n_i\ge r\}.
\]
The complete Jordan decomposition of the finite-dimensional generalized \(\lambda\)-eigenspace consists of **one Jordan block of length \(b_\beta(\lambda)\)** for every such \(\beta\); there are no other blocks. In particular,
\[
 \operatorname{mult}_{\mathrm{alg}}(\lambda)=\sum_{i=1}^sD_d(n_i),\qquad
 \operatorname{mult}_{\mathrm{geom}}(\lambda)=D_d(M),\qquad
 \operatorname{ord}_{\lambda}(\text{resolvent pole})=s.
\]
The last equality uses the \(\beta=0\) block, which has length \(s\).

For the natural polynomial-geometric sequence \(a_N=(N+1)q^N\), \(0<q<1\), nonzero eigenvalues collide only in pairs. A collision at two indices \(0\le n<m\) occurs exactly at
\[
 q=q_{n,m}=\left(\frac{n+1}{m+1}\right)^{1/(m-n)}.
\]
At this parameter, the common eigenvalue \(\lambda=(n+1)q^n\) has exactly \(D_d(n)\) Jordan blocks of length two and \(D_d(m)-D_d(n)\) blocks of length one; its geometric and algebraic multiplicities are \(D_d(m)\) and \(D_d(n)+D_d(m)\), respectively. Away from the countable resonance set \(\{q_{n,m}:0\le n<m\}\), every nonzero eigenvalue is semisimple. These statements concern individual isolated eigenvalues; global similarity to a diagonal operator is not asserted.

## Assumptions and scope

The Drury–Arveson kernel is \(K(z,w)=(1-\langle z,w\rangle)^{-1}\) on the unit ball of \(\mathbb C^d\). Monomials are orthogonal with \(\|z^\alpha\|^2=\alpha!/|\alpha|!\), where \(|\alpha|\) denotes total degree. The multiplier \(M_{z_j}\) is a contraction. The hypothesis \(\sum (N+1)^d|a_N|<\infty\) is a simple sufficient condition ensuring trace-class convergence; it is not claimed necessary. The case \(d=1\) is included using the unique empty transverse multi-index. No classification of the spectral point zero or of the singular-value sequence is claimed.

## Proof

**1. Trace-class construction.** Let \(P_m\) be the homogeneous degree-\(m\) orthogonal projection. The \(N\)-th output-row operator is
\[
 U_N=a_N\sum_{m=0}^N M_{z_j}^{N-m}P_m.
\]
It maps into the degree-\(N\) space of dimension \(D_d(N)\). Since \(\|M_{z_j}\|\le1\), Cauchy–Schwarz gives
\[
 \|U_N\|\le |a_N|\sqrt{N+1},\qquad
 \|U_N\|_{\mathcal S_1}\le D_d(N)|a_N|\sqrt{N+1}.
\]
As \(D_d(N)=O_d((N+1)^{d-1})\), the assumed series makes \(\sum U_N\) converge in trace norm. The finite partial sums \(\sum_{N=0}^LU_N\) equal \(P_{\le L}R_{j,a}P_{\le L}\), and each is lower triangular by total degree, with diagonal entry \(a_N\) repeated \(D_d(N)\) times. Trace-norm convergence of Fredholm determinants and traces proves the displayed product and power-trace identities. Every nonzero spectral point of a compact operator is an eigenvalue. Conversely, if \(R_{j,a}f=\lambda f\ne0\) and \(f_k\) is the lowest nonzero homogeneous term, comparison of degree \(k\) yields \(a_k=\lambda\). Thus the nonzero spectrum is contained in the nonzero coefficients. The determinant product, or the finite-head/tail argument below, proves each nonzero coefficient actually occurs.

**2. Transverse line reduction.** Remove coordinate \(j\) from each monomial exponent and call the remaining multi-index \(\beta\), with \(r=|\beta|\). The orthogonal spaces
\[
 X_\beta=\overline{\operatorname{span}}\{z_j^k z'^{\beta}:k\ge0\}
\]
reduce the operator: \(R_{j,a}\) preserves the transverse exponent, as does its adjoint. On a polynomial \(\sum_{k\ge0}c_kz_j^kz'^{\beta}\), the coefficient of \(z_j^iz'^{\beta}\) after applying \(R_{j,a}\) is
\[
 a_{i+r}\sum_{k=0}^ic_k.
\]
This formula is in *unnormalized* orthogonal monomials. Each finite truncation is conjugate through a nonsingular diagonal normalization matrix to the ordinary finite terraced matrix with row \(i\) equal to \(a_{i+r}\) up to column \(i\). Hence normalization cannot alter finite Jordan blocks.

**3. Exact finite Jordan blocks.** Fix \(\lambda\ne0\) and a transverse \(\beta\) with \(r\le M\). Restrict to total degrees at most \(M\), so the line indices are \(0\le i\le M-r\). The diagonal entries equal to \(\lambda\) occur precisely when \(r+i\in\{n_1,\dots,n_s\}\). Their count is \(b_\beta(\lambda)\), the algebraic multiplicity on this line. To compute geometric multiplicity, the eigenvalue equation for coefficient \(c_i\), with cumulative sums \(S_i=\sum_{k=0}^ic_k\) and \(S_{-1}=0\), becomes
\[
 (\lambda-a_{i+r})S_i=\lambda S_{i-1}.
\]
Whenever \(a_{i+r}\ne\lambda\), the factor \(\lambda/(\lambda-a_{i+r})\) is nonzero. At each occurrence of \(a_{i+r}=\lambda\), the equation forces \(S_{i-1}=0\) but leaves \(S_i\) free. Every free choice at an occurrence before the *last* one is forced to zero at the next occurrence. The last occurrence supplies exactly one freely chosen coordinate, proving the eigenvalue has geometric multiplicity one on the line. A finite-dimensional matrix with algebraic multiplicity \(b_\beta\) and geometric multiplicity one has precisely one Jordan block of that length.

**4. Passage to the full space.** Split \(H_d^2\) into total degrees \(\le M\) and \(>M\). The operator has block-lower-triangular form \(\begin{psmallmatrix}A&0\\B&C\end{psmallmatrix}\). Its tail \(C\) is compact and has no eigenvalue \(\lambda\): a nonzero tail eigenfunction would have a lowest homogeneous degree \(k>M\) with \(a_k=\lambda\), contradicting maximality of \(M\). Therefore \(C-\lambda I\) is invertible. The projection from the full generalized \(\lambda\)-root space onto the finite head intertwines the restricted operators and is an isomorphism: solve its tail components successively using \((C-\lambda I)^{-1}\). For clarity, on a finite-head root space where \(A_\lambda=A-\lambda I\) satisfies \(A_\lambda^s=0\), the corresponding invariant graph operator is explicitly \(X=-\sum_{h=0}^{s-1}(C-\lambda I)^{-(h+1)}BA_\lambda^h\). Indeed, \((C-\lambda I)X-XA_\lambda=-B\), proving the intertwining directly. The finite-head Jordan classification thus gives the exact full-space classification. As the number of transverse multi-indices of degree at most \(n\) equals \(D_d(n)\), summing their contributions gives the two multiplicity formulas and maximal block length \(s\).

**5. Resonance family.** For \(a_N=(N+1)q^N\), consecutive ratios are
\[
 \frac{a_{N+1}}{a_N}=q\frac{N+2}{N+1},
\]
strictly decreasing in \(N\). The coefficient sequence is unimodal, with at most a two-term plateau, so any given value is attained at no more than two indices. Solving \(a_n=a_m\) for \(n<m\) yields the stated unique \(q_{n,m}\). For a pair \(n<m\), each transverse \(\beta\) of degree \(\le n\) gives a length-two Jordan block, and each transverse \(\beta\) with \(n<|\beta|\le m\) a length-one block. Counting these proves the sharp dimensional multiplicities. If no collision occurs, all nonzero Jordan blocks have length one.

## Verification

The standalone `checker.py` constructs exact rational finite-dimensional monomial matrices from the homogeneous formula and compares the nullities of the first and second powers of \(R-\lambda I\) against the predicted geometric and algebraic multiplicities. It tests the resonances \(q=1/2\), \(2/3\), \(3/4\) in dimensions \(2\) and \(3\), and a separate complex-coefficient-independent triple occurrence (using rational real coefficients) whose predicted Jordan block sizes are \(3,2,2,1,1\). The checker reports 16 exact symbolic assertions passed. All infinite-dimensional, all-parameter claims follow from the preceding proof rather than finite tests.

## Relationship to prior work

Michael R. Pilla introduced these multivariable homogeneous Rhaly operators in 2026. The definition and the transverse-line decomposition for the associated Cesàro operators appear there; Section 4.4 established only an inclusion for point spectra and a compact spectral inclusion, not the nonzero algebraic/geometric multiplicities or the Jordan diagrams. The 2019 work of Mursaleen, Yildirim and Durna treats spectra of certain one-variable generalized Rhaly matrices; the 2025/2026 work of Galanopoulos and Girela focuses on boundedness and compactness on one-variable analytic spaces. Bellavita, Dellepiane and Stylogiannis analyze one-variable weighted-Hardy Rhaly ideal properties. The present classification combines multivariable monomial multiplicities with a nontrivial Jordan-block count at repeated diagonal levels. It does not assert that the elementary one-dimensional finite-matrix recursion is new.

## Limitations

The weighted coefficient decay condition is sufficient but not sharp. The generalized eigenspace at \(0\), singular values, global completeness or Riesz-basis properties, and perturbative eigenprojection norms are not classified. The originality assessment is limited by incomplete access to some older full texts on factorable triangular matrices, and a more general historical Jordan-classification theorem could imply the one-dimensional ingredient. No independent mathematical review has been performed.

## References

1. M. R. Pilla, *Rhaly-Type Operators in Several Complex Variables*, arXiv:2606.25885 (first posted 2026-06-24), especially Sections 2.2, 4.1 and 4.4. https://arxiv.org/abs/2606.25885
2. P. Galanopoulos and D. Girela, *Rhaly Operators Acting on Hardy, Bergman, and Dirichlet Spaces*, arXiv:2511.09201; Journal of Geometric Analysis **36** (2026), article 115. https://doi.org/10.1007/s12220-026-02361-9
3. M. Mursaleen, M. Yildirim and N. Durna, *On the spectrum and Hilbert Schimidt properties of generalized Rhaly matrices*, Communications Faculty of Sciences University of Ankara Series A1 **68** (2019), 712–723. https://doi.org/10.31801/cfsuasmas.464177
4. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875 (2026). https://arxiv.org/abs/2606.15875

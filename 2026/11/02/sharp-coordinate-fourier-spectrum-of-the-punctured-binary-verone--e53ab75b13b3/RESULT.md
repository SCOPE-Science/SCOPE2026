# Sharp coordinate-Fourier spectrum of the punctured binary Veronese cone

## Finding
For every integer \(d\ge3\), let \(X_d=\{vv^{\mathsf T}:0\ne v\in\mathbb F_2^d\}\) in the additive group of symmetric binary matrices. This set has cardinality \(Q-1\), with \(Q=2^d\). On \(X_d\), sample the constant and **every distinct diagonal or strictly upper-triangular coordinate additive character**:
\[
1,\qquad a_i(v)=(-1)^{v_i}\ (1\le i\le d),\qquad
b_{ij}(v)=(-1)^{v_iv_j}\ (1\le i<j\le d).
\]
The Gram matrix \(G_d\) is defined by uniform probability averaging over \(X_d\), not by unnormalized counting. Put \(m=\binom d2\), \(k=1+d+m\) and
\[
 H_d^{(0)}=\begin{pmatrix}
 1&0&\sqrt m/2\\
 0&1&\sqrt{(d-1)/2}\\
 \sqrt m/2&\sqrt{(d-1)/2}&(m+2d-1)/4
 \end{pmatrix},\quad
 w_d=(1,\sqrt d,\sqrt m)^{\mathsf T},\quad
 H_d=\frac{QH_d^{(0)}-w_dw_d^{\mathsf T}}{Q-1}.
\]
The entire Gram spectrum, with multiplicities, is
\[
\begin{array}{c|c}
 \text{eigenvalues}&\text{multiplicity}\\\hline
 \text{the three eigenvalues of }H_d&1\text{ each, algebraically counted}\\
 \displaystyle\frac{Q}{Q-1}\frac{d+3+\sqrt{(d+3)^2-16}}8&d-1\\
 \displaystyle\frac{Q}{Q-1}\frac{d+3-\sqrt{(d+3)^2-16}}8&d-1\\
 \displaystyle\frac{Q}{4(Q-1)}&m-d
\end{array}
\]
(the last multiplicity is zero when \(d=3\)). Every eigenvalue is positive. **Both sharp extremal eigenvalues belong to the same three-dimensional symmetric sector**:
\[
 \lambda_{\max}(G_d)=\lambda_{\max}(H_d),\qquad
 \lambda_{\min}(G_d)=\lambda_{\min}(H_d),\qquad
 \kappa_d^2=\frac{\lambda_{\max}(H_d)}{\lambda_{\min}(H_d)}
 \sim\frac{d^4}{16}\quad(d\to\infty).
\]
Here \(\kappa_d\) is the singular-value condition number of the restriction/evaluation operator, with probability-normalized rows. In addition, the exact Gram determinant is
\[
 \boxed{\det G_d=\frac{Q^{k-1}(Q-k)}{4^m(Q-1)^k}.}
\]
As a point of comparison, the *intrinsic* degree-at-most-two Walsh characters in the parameter vector \(v\), evaluated on the same punctured cube, have only the two Gram eigenvalues \(Q/(Q-1)\) (multiplicity \(k-1\)) and \((Q-k)/(Q-1)\) (multiplicity one). Their squared condition number tends to one; the quartic penalty arises from choosing coordinate characters of the ambient symmetric-matrix embedding instead.

## Assumptions and scope
The field is exactly \(\mathbb F_2\), the dimension satisfies \(d\ge3\), and the matrix cone excludes zero. A symmetric binary matrix has one independent coordinate for each diagonal entry and each strictly upper-triangular entry; no character is duplicated by including both symmetric off-diagonal positions. The ambient-coordinate family has size \(k\), smaller than \(|X_d|=Q-1\) for all \(d\ge3\). The stated condition number is for the chosen coefficient-coordinate system; it is not invariant under a nonorthogonal change of basis. The result does not assert a basis of all \(L^2(X_d)\) for \(d\ge4\).

## Proof
**1. Identification and independent intrinsic basis.** Over \(\mathbb F_2\), the diagonal of \(vv^{\mathsf T}\) equals \(v\), so the map \(v\mapsto vv^{\mathsf T}\) is injective. Write \(\chi_i(v)=(-1)^{v_i}\) and \(\chi_{ij}(v)=\chi_i(v)\chi_j(v)\). The relation
\[
 b_{ij}=\tfrac12(1+\chi_i+\chi_j-\chi_{ij})
\]
shows that the ambient-coordinate family is related to the intrinsically orthonormal full-cube Walsh band \(\{1,\chi_i,\chi_{ij}\}\) by an invertible triangular coefficient transform of determinant modulus \(2^{-m}\). On the full Boolean cube the intrinsic Gram is \(I_k\). Removing the zero vector, where every intrinsic character equals \(1\), gives its normalized Gram
\[
 W_d=\frac{Q I_k-\mathbf1_k\mathbf1_k^{\mathsf T}}{Q-1}.
\]
Because \(2^d>1+d+\binom d2=k\) for \(d\ge3\), its eigenvalues are \(Q/(Q-1)\) with multiplicity \(k-1\), and \((Q-k)/(Q-1)>0\) once. This proves independence and, by the coefficient transform, yields the determinant formula for \(G_d\).

**2. Exact ambient-coordinate moments.** Let \(G_d^{(0)}\) denote the probability Gram on *all* \(Q\) parameter vectors. Let \(B\) be the unsigned \(d\times m\) incidence matrix of the complete graph, let \(J_m\) be the all-one matrix and let \(\mathbf1\) be the all-one vector of the relevant length. Directly using independent unbiased bits gives
\[
G_d^{(0)}=
\begin{pmatrix}
1&0&\frac12\mathbf1_m^{\mathsf T}\\
0&I_d&\frac12 B\\
\frac12\mathbf1_m&\frac12 B^{\mathsf T}&\frac14(I_m+B^{\mathsf T}B+J_m)
\end{pmatrix}.
\]
For example, two distinct edge characters have mean product \(1/2\) if their edges meet and \(1/4\) if disjoint; a vertex and an edge character have mean product \(1/2\) exactly for incidence. Every character takes value \(1\) at \(v=0\), so the sought punctured Gram is
\[
 G_d=\frac{QG_d^{(0)}-zz^{\mathsf T}}{Q-1},\qquad
 z=(1,\mathbf1_d^{\mathsf T},\mathbf1_m^{\mathsf T})^{\mathsf T}.
\]

**3. Complete orthogonal decomposition.** The incidence matrix obeys \(BB^{\mathsf T}=(d-2)I_d+J_d\) and has full row rank for \(d\ge3\). Decompose the edge coefficient space into its constant line, the standard component \(B^{\mathsf T}(\mathbf1_d^\perp)\), and \(\ker B\), of respective dimensions \(1,d-1,m-d\). The vertex coefficient space is its constant line plus \(\mathbf1_d^\perp\). The matrix \(zz^{\mathsf T}\) acts only on the three constant coefficient lines. On \(\ker B\) the eigenvalue is \(Q/[4(Q-1)]\). For every unit \(u\perp\mathbf1_d\), the orthonormal coefficient pair consisting of the vertex vector \(u\) and the edge vector \(B^{\mathsf T}u/\sqrt{d-2}\) has invariant matrix
\[
\frac Q{Q-1}\begin{pmatrix}
1&\sqrt{d-2}/2\\
\sqrt{d-2}/2&(d-1)/4
\end{pmatrix}.
\]
Its determinant before the leading normalization is \(1/4\) and its trace is \((d+3)/4\), producing the two displayed standard eigenvalues, each repeated \(d-1\) times. On the orthonormal span of the constant, normalized vertex sum, and normalized edge sum, the full-cube matrix is \(H_d^{(0)}\), and removal of the zero vector changes it to precisely \(H_d\). The dimensions add to \(m+d+1=k\), establishing the full spectrum without omissions.

**4. Extremal-mode rigidity.** Let \(\lambda_{+,d}^{\mathrm{std}}\) and \(\lambda_{-,d}^{\mathrm{std}}\) be the larger and smaller eigenvalues of the standard block. Their trace gives
\[
\lambda_{+,d}^{\mathrm{std}}<\frac Q{Q-1}\frac{d+3}{4}.
\]
By the Rayleigh principle, \(\lambda_{\max}(H_d)\) is at least its bottom-right diagonal entry \([Q(m+2d-1)-4m]/[4(Q-1)]\), strictly exceeding the preceding trace bound because \(Q(m+d-4)>4m\) for every integer \(d\ge3\). The edge-kernel eigenvalue is smaller as well. Thus the top eigenvalue always lies in \(H_d\).

For the minimum, consider \(x=(-\sqrt m/2,-\sqrt{(d-1)/2},1)^{\mathsf T}\). It satisfies \(x^{\mathsf T}H_d^{(0)}x=1/4\), \((w_d^{\mathsf T}x)^2=m/4\) and \(\|x\|^2=(d^2+3d+4)/8\). Hence
\[
\lambda_{\min}(H_d)\le
\frac{x^{\mathsf T}H_dx}{\|x\|^2}
=\frac{2(Q-m)}{(Q-1)(d^2+3d+4)}.
\]
The standard small eigenvalue equals \(\frac Q{Q-1}\frac2{d+3+\sqrt{(d+3)^2-16}}\). As \(d^2+3d+4>2(d+3)\), the displayed Rayleigh bound lies strictly below it. It also lies below \(Q/[4(Q-1)]\), since \(d^2+3d+4>8\). Therefore \(\lambda_{\min}(G_d)=\lambda_{\min}(H_d)\) for every \(d\ge3\); there is no hidden lower-mode transition.

**5. Sharp asymptotic.** Since \(\|w_dw_d^{\mathsf T}\|=1+d+m=O(d^2)\), one has \(H_d=H_d^{(0)}+O(d^2/2^d)\) in operator norm. The full-cube matrix \(H_d^{(0)}\) has one eigenvalue exactly \(1\); its other two are the roots of
\[
 \lambda^2-T_d\lambda+\tfrac14=0,\qquad
 T_d=\frac{m+2d+3}{4}.
\]
Consequently, its largest eigenvalue is asymptotic to \(d^2/8\), and its smallest to \(2/d^2\). The exponentially small perturbation is negligible relative even to the smallest eigenvalue, so the ratio for \(H_d\), and hence for \(G_d\), is asymptotic to \(d^4/16\).

## Verification
The standalone script `check.py` enumerates all nonzero binary vectors in dimensions three through eight. Using exact rational arithmetic, it reconstructs every Gram entry from the character definitions, verifies the full-cube moment formula, checks full column rank, confirms the complete Gram determinant formula, tests the trivial-sector bilinear form, and verifies representative standard and edge-kernel invariant identities. The output is `VERIFY_OK`. Finite checks corroborate rather than establish the universal theorem; the preceding algebraic decomposition and inequalities cover every \(d\ge3\).

## Relationship to prior work
Schmidt's work on symmetric bilinear forms in even characteristic (2010) studies rank-distance codes and association-scheme structure, not the coordinate-selected Walsh Gram spectrum. His 2014 manuscript on odd-field symmetric forms provides the broader coding-theoretic setting, while the 2018 extension includes characteristic-two association-scheme eigenvalues and supplies possible general character-sum machinery. These general tables can be used to reconstruct relevant averages, but the stated three-sector coordinate-frame diagonalization, extremal-mode comparison, exact determinant, and quartic conditioning law are not the statements of those inspected works. A published harmonic-frame result for *odd-order* rank-one symmetric cones uses only off-diagonal frequencies and has a different lower-mode transition and cubic asymptotic; a separate result for arbitrary rectangular rank-one matrices has a different sample space. The present result specifically treats characteristic two, all independent symmetric-matrix coordinates including the diagonal, and omission of the zero matrix.

## Limitations
The full Gram spectrum concerns one specified coordinate Fourier band, not arbitrary choices of characters or arbitrary symmetric-matrix rank shells. The probability measure on the nonzero rank-one cone is uniform. The asymptotic constant depends on this nonorthonormal ambient-coordinate basis; an intrinsic degree-two Walsh basis is much better conditioned. Exact finite checks are not infinite proofs. The Fourier and association-scheme literature is extensive, and an older equivalent spectral specialization remains a historical-priority risk; the general association-scheme formulas are not claimed as new.

## References
1. K.-U. Schmidt, *Symmetric bilinear forms over finite fields of even characteristic*, Journal of Combinatorial Theory, Series A **117** (2010), 1011–1026, DOI: 10.1016/j.jcta.2010.05.006; author manuscript at https://math.uni-paderborn.de/fileadmin/mathematik/AG-Diskrete_Mathematik/Publications-schmidt/bilinear.pdf.
2. K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, arXiv:1410.7184, first posted 2014-10-27; https://arxiv.org/abs/1410.7184.
3. K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, arXiv:1803.04274, first posted 2018-03-12; https://arxiv.org/abs/1803.04274.
4. *Sharp Fourier Riesz spectrum and a dimension transition on the finite-field Veronese cone*, published 2026-10-11 in the public published-finding corpus research collection; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-fourier-riesz-spectrum-and-a-dimension-transition-on-the-f--7e4eb0365b75.
5. *Complete first-coordinate Fourier spectrum on finite-field rank-one matrices*, published 2026-10-11 in the public published-finding corpus research collection; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-first-coordinate-fourier-spectrum-on-finite-field-rank--3ad73e3126a7.

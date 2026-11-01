# An exact Haar-regression criterion for numerical information of normal matrices

## Finding
Let \(n\ge2\), let \(A\in M_n(\mathbb C)\) be normal, and let \(\sigma\) be normalized unitary-invariant probability measure on the unit sphere of \(\mathbb C^n\). Put \(\phi_T(x)=\langle Tx,x\rangle\), \(\mu_A=(\phi_A)_\#\sigma\), and \(V_A=\operatorname{span}_{\mathbb C}\{I,A,A^*\}\). For every \(B\in M_n(\mathbb C)\), define the optimal nonlinear numerical-information error
\[
\mathcal E_A(B)=\inf_{F\in L^2(\mu_A)}\int |\phi_B(x)-F(\phi_A(x))|^2\,d\sigma(x).
\]
Then, for **every** \(B\),
\[
\mathcal E_A(B)\le\frac{\operatorname{dist}_{\mathrm{HS}}(B,V_A)^2}{n(n+1)}.
\]
**Equality for all \(B\)** holds if and only if the *distinct* eigenvalues of \(A\), viewed in \(\mathbb R^2\), are affinely independent. Equivalently, \(A\) has at most two distinct eigenvalues or has exactly three distinct noncollinear eigenvalues. In these cases the unique best predictor (up to \(\mu_A\)-almost-everywhere equality) is an affine function \(F(z)=a+bz+c\overline z\), and the displayed right-hand side is the exact squared optimal error. If the distinct spectrum is affinely dependent, some spectral projection \(B\) has **strict** inequality.

The first minimal-dimensional failure is explicit. For \(A=\operatorname{diag}(-1,0,1)\) and \(B=\operatorname{diag}(0,1,0)\), the exact best nonlinear predictor is \(F(t)=(1-|t|)/2\) on \([-1,1]\), and
\[
\mathcal E_A(B)=\frac1{24},\qquad
\frac{\operatorname{dist}_{\mathrm{HS}}(B,V_A)^2}{3\cdot4}=\frac1{18}.
\]
Thus nonlinearity reduces the squared prediction error by exactly one quarter in this canonical three-level example.

## Assumptions and scope
The field is \(\mathbb C\), the Haar law is normalized, the random vector is a single uniform unit vector, and the loss is squared absolute complex modulus. All operators here are finite \(n\times n\) matrices, and the classification assumes that the input \(A\) is normal. The regression class is all \(\mu_A\)-square-integrable Borel functions, without regularity restrictions. The *distinct* spectral values are counted without multiplicity; eigenvalue multiplicities can be arbitrary positive integers.

## Proof
**1. Haar quadratic-form identity.** For every \(R\in M_n(\mathbb C)\), invariance of the uniform unit vector and the complex spherical fourth moments give
\[
\int |\phi_R(x)|^2\,d\sigma(x)=\frac{\operatorname{tr}(RR^*)+|\operatorname{tr}R|^2}{n(n+1)}. \tag{1}
\]
Indeed \(\mathbb E[x_i\overline{x_j}\overline{x_k}x_l]=(\delta_{ij}\delta_{lk}+\delta_{ik}\delta_{lj})/[n(n+1)]\), obtainable by writing \(x\) as a normalized standard complex Gaussian vector; its squared coordinate moduli are Dirichlet with unit parameters. As \(I\in V_A\), the Hilbert–Schmidt residual \(R=B-P_{V_A}B\) of orthogonal projection onto \(V_A\) has trace zero. Consequently (1) gives the exact optimal **affine** loss
\[
\inf_{a,b,c\in\mathbb C}\int|\phi_B(x)-(a+b\phi_A(x)+c\overline{\phi_A(x)})|^2\,d\sigma(x)
=\frac{\operatorname{dist}_{\mathrm{HS}}(B,V_A)^2}{n(n+1)}. \tag{2}
\]
To check optimality in (2), decompose any candidate residual into the Hilbert–Schmidt orthogonal sum of \(R\) and an element of \(V_A\); (1) makes the squared loss at least that of \(R\), with no cross term. Nonlinear predictors include affine predictors, proving the universal inequality.

**2. Conditional expectation.** Write \(A=\sum_{j=1}^q\lambda_jP_j\), with distinct eigenvalues and spectral ranks \(d_j=\operatorname{rank}P_j\). Put \(T_j(x)=\|P_jx\|^2\). Given \((T_1,\ldots,T_q)\), the directions within nonzero blocks are independent Haar vectors, and blockwise rotations kill the off-diagonal terms. It follows that
\[
\mathbb E[\phi_B\mid T_1,\ldots,T_q]
=\sum_{j=1}^q T_j\frac{\operatorname{tr}(BP_j)}{d_j}. \tag{3}
\]
Furthermore \(Z=\phi_A=\sum_j\lambda_jT_j\), with \(\sum_jT_j=1\). If the \(\lambda_j\) are affinely independent in \(\mathbb R^2\), the vector \((T_j)\) is uniquely determined by \(Z\), through affine barycentric coordinates. The conditional mean \(\mathbb E[\phi_B\mid Z]\) is therefore given by (3), an affine function of \(Z\) and \(\bar Z\). The matrix \(C=\sum_j[\operatorname{tr}(BP_j)/d_j]P_j\) is exactly \(P_{V_A}B\), since \(V_A\) is the entire space of block-scalar spectral matrices when the distinct eigenvalues are affinely independent. The conditional-expectation projection theorem, together with (1), proves equality in the finding.

**3. Necessity of spectral affine independence.** Suppose that \(\mathbb E[\phi_B\mid Z]\) is affine in \(Z\) for **every** \(B\). In particular, for each \(B=P_j\), the conditional mean \(f_j(Z)=\mathbb E[T_j\mid Z]\) agrees almost everywhere on the spectral convex hull with an affine function of the real and imaginary parts of \(Z\). The law of \(Z\) has the entire spectral convex hull as support, because the block masses have a strictly positive Dirichlet density in the simplex interior. At each extreme spectral vertex \(\lambda_k\), the relation \(Z=\sum_j\lambda_jT_j\) forces \(T_k\to1\) as \(Z\to\lambda_k\), uniformly over the feasible block-mass vectors. Thus continuity of an affine \(f_j\) implies \(f_j(\lambda_k)=\delta_{jk}\) at every extreme vertex.

If the convex hull is a segment and there are at least three distinct eigenvalues, select an eigenvalue in the relative interior: its \(f_j\) would vanish at both segment endpoints, hence on the whole segment, contradicting \(\mathbb E[T_j]=d_j/n>0\). If the convex hull has at least three noncollinear vertices but includes a nonextreme eigenvalue, choose its \(P_j\): the affine \(f_j\) vanishes at three noncollinear vertices, so vanishes identically, again impossible. If all eigenvalues are extreme vertices and there are at least four, select any one of them; its \(f_j\) vanishes at three other noncollinear extreme vertices, another contradiction. These cases exhaust affine dependence in the plane. Therefore for an affinely dependent spectrum some \(\mathbb E[\phi_{P_j}\mid Z]\) cannot be affine. Since the conditional expectation uniquely minimizes squared error over all \(F(Z)\), and finite-dimensional affine predictors form a closed proper subspace of \(L^2(\mu_A)\), the inequality is then strict for that \(P_j\).

**4. Exact three-level boundary.** For \(A=\operatorname{diag}(-1,0,1)\), put \(X=-|x_1|^2+|x_3|^2\) and \(Y=|x_2|^2\). The three squared moduli are uniformly Dirichlet \((1,1,1)\). The joint \((X,Y)\) density is exactly \(1\) on \(\{-1\le X\le1,\ 0\le Y\le1-|X|\}\), hence \(Y\mid X=t\) is uniform on \([0,1-|t|]\). The conditional mean is \((1-|t|)/2\), and the expected conditional variance equals
\[
\frac1{12}\int_{-1}^1(1-|t|)^3\,dt=\frac1{24}.
\]
The Hilbert–Schmidt projection of \(B\) onto \(V_A=\operatorname{span}\{I,A\}\) is \(I/3\). Its squared residual norm is \(2/3\), and (2) gives \((2/3)/12=1/18\). All stated identities follow.

## Verification
The proof uses only finite-dimensional Haar fourth moments, block-unitary invariance, uniqueness of barycentric coordinates, conditional expectation as an \(L^2\) projection, and the geometry of a planar convex polygon. A standalone exact-arithmetic checker, `verify.py`, tests the core fourth-moment identity against Dirichlet moments, the three-level conditional integrals, and several finite matrix projections. Its finite tests do not establish the universal quantifiers; the proof above does.

## Relationship to prior work
D. M. Johnson, *Numerical Information of Hilbert Space Operators* (first public 21 October 2026, arXiv:2610.29826v1), characterizes **zero-error pointwise** dependence \(\phi_B=F\circ\phi_A\): it occurs precisely for the affine operator pencil. Here the question is different: whether a **best nonlinear mean-square predictor** can beat its best affine counterpart, and the answer is classified completely for normal finite-dimensional \(A\). The equality criterion and strict three-level example do not follow from the pointwise inclusion theorem alone.

Classical spherical moment identities and Dirichlet coordinate laws are used as established inputs. L. Zhang, *Exact probability laws of random inner products: Dirichlet splines, overlaps, uncertainty, and Bargmann invariants* (arXiv:2610.25196, first submitted 18 October 2026), studies related marginal distributions; distributional laws are not themselves conditional-regression projection identities. The numerical-shadow framework traces to Dunkl et al., *Numerical shadow and geometry of quantum states* (arXiv:1104.2760).

## Limitations
This is a finite-dimensional classification restricted to **normal** \(A\); no corresponding necessity theorem is claimed for all nonnormal matrices or infinite-dimensional operators. The explicit numerical gain \(1/24\) versus \(1/18\) is for the specified symmetric three-level example, not a universal sharp gain across all non-simplex spectra. Self-review has passed; independent mathematical validation and publication-priority certification have not been performed. Older unindexed results on conditional means of Dirichlet barycentric projections remain a possible novelty risk.

## References
- D. M. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826v1, 21 October 2026. https://arxiv.org/html/2610.29826v1
- L. Zhang, *Exact probability laws of random inner products: Dirichlet splines, overlaps, uncertainty, and Bargmann invariants*, arXiv:2610.25196v1, 18 October 2026. https://arxiv.org/abs/2610.25196
- C. F. Dunkl, P. Gawron, J. A. Holbrook, J. A. Miszczak, Z. Puchała, K. Życzkowski, *Numerical shadow and geometry of quantum states*, arXiv:1104.2760. https://arxiv.org/abs/1104.2760

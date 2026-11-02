# A sharp dimension threshold for centering in periodic weighted-shift numerical-radius norms

## Finding

For every integer \(n\ge2\), let \(T_a\) be the unilateral weighted shift on complex \(\ell^2(\mathbb N_0)\) whose weights repeat the vector \(a=(a_0,\ldots,a_{n-1})\in\mathbb C^n\). Equip \(\mathbb C^n\) with the numerical-radius norm \(\|a\|_{\mathrm{nr},n}=w(T_a)\). Let \(E_n a=(n^{-1}\sum_{j=0}^{n-1}a_j)\mathbf1\), and let \(P_n=I-E_n\).

**Theorem.** The mean-zero projection \(P_n\) is contractive in \(\|\cdot\|_{\mathrm{nr},n}\) if and only if \(n=2\). Its norm at \(n=2\) equals one. At the first noncontractive dimension, the following sharp **two-coordinate restriction** holds:
\[
\sup_{0\ne a\in\mathbb C^3,\,|\operatorname{supp}a|\le2}
\frac{\|P_3a\|_{\mathrm{nr},3}}{\|a\|_{\mathrm{nr},3}}
=\frac4{\sqrt{15}}.
\]
An attaining vector is \(a=(3-i\sqrt{111},0,3+i\sqrt{111})\). Thus \(\|P_3\|\ge4/\sqrt{15}>1\); the **unrestricted** operator norm is not asserted to equal this value.

For each \(n\ge4\), the explicit two-coordinate family \(a^{(\varepsilon)}=(1,0,-e^{i\varepsilon},0,\ldots,0)\) obeys, as nonzero real \(\varepsilon\to0\),
\[
\frac{\|P_na^{(\varepsilon)}\|_{\mathrm{nr},n}}
{\|a^{(\varepsilon)}\|_{\mathrm{nr},n}}
=\begin{cases}
1+|\varepsilon|/n+O(\varepsilon^2),&n=4,\\
1+|\varepsilon|/(2n)+O_n(\varepsilon^2),&n\ge5.
\end{cases}
\]
In each case the error is for fixed \(n\), and its sign is not assumed. Both positive linear coefficients are exact, not merely lower estimates.

## Assumptions and scope

All scalars are complex. The numerical radius is \(w(T)=\sup_{\|u\|_2=1}|\langle Tu,u\rangle|\). The shift is unilateral but the weights are periodically repeated indefinitely. The average \(E_n\) is the coordinate arithmetic mean, and the projection acts on periodic weight vectors, not on \(\ell^2\) itself. Every \(n\ge2\) is covered; no assertion about arbitrary, nonperiodic weights is made.

For \(n\ge3\), the classical periodic-weight variational formula gives
\[
\|a\|_{\mathrm{nr},n}
=\lambda_{\max} B_n(|a|),\qquad
B_n(|a|)_{j,j+1}=B_n(|a|)_{j+1,j}=\frac{|a_j|}{2},
\]
with indices modulo \(n\); all unspecified entries are zero. For \(n=2\) the two cyclic contributions occupy the same matrix entry and are added. This convention avoids incorrectly treating the length-two cycle as an ordinary simple graph.

## Proof

**The two-periodic exception.** Directly, \(\|(z_0,z_1)\|_{\mathrm{nr},2}=(|z_0|+|z_1|)/2\). Therefore
\[
\|P_2(z_0,z_1)\|_{\mathrm{nr},2}
=\frac{|z_0-z_1|}{2}
\le\frac{|z_0|+|z_1|}{2}.
\]
Equality holds for opposite nonzero entries, proving norm one.

**The exact three-periodic sparse constant.** By coordinate permutation symmetry of the triangular variational problem, any vector with at most two nonzero entries may be written \(a=(z,0,t)\). Since the two nonzero cycle edges form a path,
\[
\|(z,0,t)\|_{\mathrm{nr},3}=\frac12\sqrt{|z|^2+|t|^2}.
\]
Writing \(P_3(z,0,t)=((2z-t)/3,-(z+t)/3,(2t-z)/3)\), the variational characterization of the positive three-edge matrix gives
\[
\|P_3(z,0,t)\|_{\mathrm{nr},3}
=\frac13\max_{q_j\ge0,\,\sum q_j^2=1}
\bigl(q_0q_1|2z-t|+q_1q_2|z+t|+q_2q_0|2t-z|\bigr).
\]
The maximum ratio over \(|z|^2+|t|^2=1\) can be computed by introducing phases \(u,v,w\) with \(|u|=q_0q_1\), \(|v|=q_1q_2\), \(|w|=q_2q_0\). Moving the maximum over the phases outside the linear maximization over \(z,t\) and applying Cauchy–Schwarz gives
\[
\sup_{(z,t)\ne0}\frac{\|P_3(z,0,t)\|_{\mathrm{nr},3}}{\|(z,0,t)\|_{\mathrm{nr},3}}
=\frac23\max_{q,u,v,w}\sqrt{F},\quad
F=|2u-v-w|^2+|-u-v+2w|^2.
\]
For fixed moduli let \(s=|u+w|\). The phase of \(v\) can be optimized, and direct expansion yields
\[
F\le9(|u|^2+|w|^2)+2|v|^2-4s^2+2|v|s
\le9(|u|^2+|w|^2)+\frac94|v|^2.
\]
Both inequalities admit simultaneous equality for suitable phases. Put \(x=q_0^2\). Then
\[
|u|^2+|w|^2=x(1-x),\qquad |v|^2=q_1^2q_2^2\le\frac{(1-x)^2}{4},
\]
and therefore
\[
F\le9\left(x(1-x)+\frac{(1-x)^2}{16}\right)
=\frac{12}{5}-\frac{135}{16}\left(x-\frac7{15}\right)^2
\le\frac{12}{5}.
\]
This gives the sharp upper bound \((2/3)\sqrt{12/5}=4/\sqrt{15}\). To verify attainment without any phase-selection ambiguity, take
\(a=(3-i\sqrt{111},0,3+i\sqrt{111})\). Its input norm is \(2\sqrt{15}\). Its centered vector is \((1-i\sqrt{111},-2,1+i\sqrt{111})\), whose edge moduli are \((4\sqrt7,2,4\sqrt7)\). The positive triangular matrix has Perron eigenvalue exactly \(8\): its characteristic equation is \(4\lambda^3-\lambda(112+4+112)-224=0\), with unique positive root \(\lambda=8\). The quotient is therefore exactly \(4/\sqrt{15}\).

**Every higher period.** Let \(n\ge4\) and \(a^{(\varepsilon)}\) be as in the theorem. Its only two nonzero weighted edges are disjoint, so \(\|a^{(\varepsilon)}\|_{\mathrm{nr},n}=1/2\). With \(\mu=(1-e^{i\varepsilon})/n\), the weight moduli of \(P_na^{(\varepsilon)}\) are \(1+O(\varepsilon^2)\) on edges \(0\) and \(2\), and \(|\varepsilon|/n+O(|\varepsilon|^3)\) on every other edge.

At \(\varepsilon=0\), the positive edge matrix consists of two disjoint single-edge blocks (plus isolated vertices). Its top eigenvalue \(1/2\) has exactly two orthonormal eigenvectors \(r=(e_0+e_1)/\sqrt2\) and \(s=(e_2+e_3)/\sqrt2\), separated from the rest of the spectrum by a positive gap. In the span of \(r,s\), the first-order perturbation has diagonal zero and off-diagonal \(1/(4n)\) for \(n\ge5\): precisely one newly activated edge connects the two blocks. When \(n=4\), the closing edge supplies a second identical coupling and the off-diagonal is \(1/(2n)\). A standard finite-dimensional symmetric block reduction (or Schur complement and the spectral gap) therefore yields
\[
\|P_na^{(\varepsilon)}\|_{\mathrm{nr},n}
=\begin{cases}
1/2+|\varepsilon|/(2n)+O(\varepsilon^2),&n=4,\\
1/2+|\varepsilon|/(4n)+O_n(\varepsilon^2),&n\ge5.
\end{cases}
\]
Dividing by the exact input norm \(1/2\) gives the claimed ratio expansions, strictly greater than one for sufficiently small nonzero \(\varepsilon\). The classification follows.

## Verification

The standalone script `CHECKER.py` verifies the exact quadratic completion-of-squares identity, the algebraic three-cycle witness and its norms, triangle-inequality contractivity at period two, and the perturbative coefficients in ten finite periods. It is supplementary: the dimension-uniform classification and the sharp three-periodic bound follow from the preceding analytical proof, not from finite tests.

## Relationship to prior work

Sharif (2023) introduces the periodic numerical-radius norm on coefficient vectors and establishes norm-one results for coordinate multipliers and shifts; these do not imply contractivity of the *complement* of the cyclic averaging projection. Ridge's periodic-weight variational principle supplies the finite Perron reduction, not the projection classification. Published work on numerical-radius smoothness and Green-kernel perturbations concerns different operators or strictly positive backgrounds; the present perturbation splits two degenerate top eigenvectors at a sparse background. The exact sparse amplification constant at period three is not a general numerical-radius inequality obtained by merely renaming parameters.

## Limitations

The unrestricted value of \(\|P_3\|_{\mathrm{nr},3}\) and the unrestricted exact values for periods \(n\ge4\) are **not** proved. The formula \(4/\sqrt{15}\) is sharp only for inputs with at most two nonzero coefficients. The expansions for higher periods have dimension-dependent remainders and are not uniform in \(n\). Published-source comparison reduces but cannot eliminate the possibility of an equivalent earlier theorem stated in different terminology. No independent validation has been performed.

## References

1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876, first submitted 2023-03-02. https://arxiv.org/abs/2303.00876
2. W. J. Ridge, *Numerical range of a weighted shift with periodic weights*, Pacific J. Math. 62 (1976), 105–110. DOI:10.2307/2041852 (cited for the classical periodic variational formula; original full text not independently accessed).
3. A. Wang and P. Y. Wu, *Numerical ranges of weighted shifts*, J. Math. Anal. Appl. 381 (2011), cited in Sharif's literature review for periodic-weight numerical-radius comparisons.

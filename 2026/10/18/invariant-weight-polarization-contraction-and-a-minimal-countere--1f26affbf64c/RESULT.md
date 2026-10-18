# Invariant-weight polarization contraction and a minimal counterexample in predictive opinion loops

## Finding

Consider the perfect-prediction Friedkin--Johnsen opinion loop on any finite connected undirected network with positive reciprocal edge weights, arbitrary heterogeneous peer susceptibilities strictly between zero and one, a common platform susceptibility, and infinitely many peer-interaction steps between prediction updates. There is an explicit, susceptibility-adjusted stationary weight for which equilibrium disagreement decreases **strictly** as platform susceptibility increases, with a **sharp spectral contraction factor**. Ordinary equally weighted disagreement has no such monotonicity even for a three-person unweighted path, and three is the smallest possible population size for this failure.

Precisely, for a symmetric nonnegative weighted adjacency matrix \(A\), positive weighted degrees \(d_i=\sum_j A_{ij}\), row-stochastic \(W_{ij}=A_{ij}/d_i\), and \(0<\alpha_i<1\), define
\[
P=(I-\Lambda W)^{-1}(I-\Lambda),\qquad
\nu_i=\frac{d_i(1-\alpha_i)/\alpha_i}{\sum_j d_j(1-\alpha_j)/\alpha_j},\qquad
\Lambda=\operatorname{diag}(\alpha_1,\ldots,\alpha_n).
\]
For any innate opinion \(x^*\in[0,1]^n\) and common platform susceptibility \(0\le\beta<1\), the unique equilibrium is
\[
x_\beta=(1-\beta)(I-\beta P)^{-1}P x^*.
\]
The vector \(\nu\) is positive and stationary for \(P\), and \(P\) is self-adjoint and strictly positive definite in \(\ell^2(\nu)\). Write its eigenvalues in descending order as \(1=\lambda_1>\lambda_2\ge\cdots\ge\lambda_n>0\). Then, setting \(\bar x_\nu=\sum_i\nu_i x_i^*\),
\[
\sum_i\nu_i(x_{\beta,i}-\bar x_\nu)^2
\le
\left(\frac{(1-\beta)\lambda_2}{1-\beta\lambda_2}\right)^2
\sum_i\nu_i(x_i^*-\bar x_\nu)^2.
\]
The factor is **sharp** over all nonconstant bounded innate-opinion vectors, and the left side is strictly decreasing with \(\beta\) for every nonconstant \(x^*\). The \(\nu\)-weighted mean stays exactly \(\bar x_\nu\) for all \(\beta\), and \(x_\beta\to\bar x_\nu\mathbf1\) as \(\beta\uparrow1\).

In contrast, for the simple path with edges \(1\)--\(2\) and \(1\)--\(3\),
\[
\alpha=(1/10,1/100,19/20),\qquad x^*=(0,1/4,1),
\]
ordinary population variance satisfies
\[
\operatorname{Var}_{\mathrm{unif}}(x_0)=\frac{8163}{819200}
<\frac{4179945336867}{419399996328968}
=\operatorname{Var}_{\mathrm{unif}}(x_{1/20}).
\]
Its derivative at \(\beta=0\) equals \(36441/458752000>0\). For a connected graph with only two vertices, ordinary variance never increases (and decreases strictly for nonconstant innate opinions), regardless of the two admissible susceptibilities. Thus the three-person example is a smallest-order obstruction.

## Assumptions and scope

The network has \(n\ge2\) vertices and \(A=A^{\mathsf T}\ge0\), with \(A_{ii}=0\), positive weights on its edges, connected support and \(d_i>0\). An individual with opinion \(y_i\) starts each period with the blended opinion \((1-\beta)x_i^*+\beta f_i\), where \(f\) is the preceding period's vector of expressed opinions. During that period, infinitely many Friedkin--Johnsen peer updates are taken, with update \(y\mapsto(I-\Lambda)y_{\mathrm{initial}}+\Lambda W y\). The predictor then repeats the resulting expressed-opinion vector exactly. The common \(\beta\in[0,1)\) is a susceptibility, not a time step. For \(\beta=1\), only the limit of fixed points as \(\beta\uparrow1\) is asserted.

For a positive probability vector \(\nu\), define \(\operatorname{Var}_\nu(z)=\sum_i\nu_i(z_i-\sum_j\nu_j z_j)^2\). Ordinary variance is \(\operatorname{Var}_{\mathrm{unif}}\) with weights \(1/n\). The convention is row-stochastic, receiving-neighbor averaging.

## Proof

**1. The exact response matrix.** Put \(Q=\Lambda W\), \(B=I-\Lambda\), and \(R=(I-Q)^{-1}\). Because each row sum of \(Q\) equals \(\alpha_i<1\), \(\rho(Q)\le\max_i\alpha_i<1\). Hence \(R=\sum_{k\ge0}Q^k\), and the Friedkin--Johnsen equilibrium from a given initial opinion \(z\) is \(R Bz=Pz\). Since \((I-Q)\mathbf1=B\mathbf1\), \(P\mathbf1=\mathbf1\). Connectedness, \(\alpha_i>0\), and the strictly positive diagonal of \(B\) imply every entry of \(P\) is strictly positive.

The outer prediction recursion is \(f^{t+1}=P((1-\beta)x^*+\beta f^t)\). For \(0\le\beta<1\), the matrix \(\beta P\) has spectral radius less than one; the unique fixed point is exactly the displayed \(x_\beta\).

**2. Detailed balance and positivity.** Let \(\mu_i=d_i/\alpha_i\). For each \(i,j\),
\[
\mu_i Q_{ij}=A_{ij}=\mu_jQ_{ji}.
\]
Thus \(Q\) is self-adjoint in \(\ell^2(\mu)\), as are all its powers and \(R\). The spectrum of \(Q\) lies in \((-1,1)\), so \(R=(I-Q)^{-1}\) is strictly positive definite in that inner product. The identities \(P=RB\) and \(\nu_i\propto\mu_iB_{ii}\) give, for every \(i,j\),
\[
\nu_iP_{ij}=\frac{\mu_iB_{ii}R_{ij}B_{jj}}{\sum_k\mu_kB_{kk}}
=\nu_jP_{ji}.
\]
The corresponding quadratic form is
\[
\langle z,Pz\rangle_\nu
=\frac{\langle Bz,RBz\rangle_\mu}{\sum_k\mu_k B_{kk}}>0
\]
for \(z\ne0\). Hence \(P\) is self-adjoint positive definite in \(\ell^2(\nu)\). Since \(P\) is entrywise positive and stochastic, Perron--Frobenius theory gives a simple eigenvalue one and all other eigenvalues of modulus below one; positivity of the quadratic form makes them all strictly positive. Detailed balance and row stochasticity yield \(\nu^{\mathsf T}P=\nu^{\mathsf T}\).

**3. Sharp disagreement law.** Choose an orthonormal eigenbasis \(v_1=\mathbf1,v_2,\dots,v_n\) in \(\ell^2(\nu)\); \(\|\mathbf1\|_\nu=1\). Write \(x^*=\bar x_\nu\mathbf1+\sum_{j\ge2}c_jv_j\). Functional calculus in the fixed-point formula yields
\[
x_\beta=\bar x_\nu\mathbf1+
\sum_{j\ge2}c_j f_\beta(\lambda_j)v_j,
\qquad f_\beta(s)=\frac{(1-\beta)s}{1-\beta s}.
\]
This proves mean invariance and the **exact** variance identity
\[
\operatorname{Var}_\nu(x_\beta)=
\sum_{j=2}^{n}c_j^2f_\beta(\lambda_j)^2.
\]
For \(0<s<1\), \(f_\beta(s)>0\), \(\partial_\beta f_\beta(s)=s(s-1)/(1-\beta s)^2<0\), and \(\partial_s f_\beta(s)=(1-\beta)/(1-\beta s)^2>0\). Every nonconstant \(x^*\) has some nonzero \(c_j\) with \(j\ge2\), proving strict decrease, the sharp \(\lambda_2\) bound, and convergence to consensus. Equality in the bound is attained whenever the nonconstant part of \(x^*\) belongs to the \(\lambda_2\)-eigenspace; a constant shift and sufficiently small nonzero scale put such a vector in \([0,1]^n\).

**4. Why three individuals are necessary for ordinary-variance failure.** For \(n=2\), the quotient of \(\mathbb R^2\) by constant vectors has dimension one. Accordingly,
\[
x_{\beta,1}-x_{\beta,2}=
 f_\beta(\lambda_2)(x_1^*-x_2^*).
\]
Ordinary variance is one quarter of the squared difference, so it is decreasing for nonconstant innate opinions regardless of the two susceptibilities.

For the stated three-person path, direct inversion gives
\[
P=\begin{pmatrix}
225/238&99/1904&5/1904\\
9/952&37719/38080&1/38080\\
855/952&1881/38080&1999/38080
\end{pmatrix},\qquad
\nu=(342,1881,1)/2224.
\]
The equilibrium at \(\beta=0\) is \(x_0=(1/64,317/1280,83/1280)\). Substitution of \(\beta=1/20\) in the resolvent yields the two exact variances in the finding; their difference is
\[
\frac{81131241010077}{42946559624086323200}>0.
\]
An independent derivative calculation gives
\[
\left.\frac{d}{d\beta}\operatorname{Var}_{\mathrm{unif}}(x_\beta)\right|_{\beta=0}
=\frac{36441}{458752000}>0.
\]
All parameters lie strictly inside the admissible susceptibility range. The example is unweighted and connected, and the same system obeys the strict \(\nu\)-weighted contraction proved above.

## Verification

Run `python3 verify.py` using Python 3.9 or later. The program uses only standard-library exact fractions and Gaussian elimination. It independently constructs \(P\), verifies row stochasticity, positive entries, detailed balance against \(\nu\), the explicit three-vertex matrix and its exact increasing ordinary variance, and the positive ordinary-variance derivative. It also checks 96 equilibrium/mean/variance identities on connected weighted path, star and complete graphs with two through five vertices, plus 64 two-vertex spectral-difference identities. These are finite cross-checks, not a replacement for Steps 1--4 of the proof.

## Relationship to prior work

Wu, Abebe and Mendler--Dünner introduce the coupled perfect-prediction loop and its general equilibrium resolvent, prove regular-graph homogeneous-susceptibility variance decrease, and prove a high-platform-susceptibility consensus limit under heterogeneous susceptibilities [1, Sections 4.1--4.3 and Appendix A.5--A.6]. Those established results are used, not claimed here as original. The present claim identifies an **explicit invariant measure** on arbitrary connected reciprocal weighted networks with heterogeneous peer susceptibilities, proves a sharp monotone **measure-specific** polarization law, and exhibits the minimal exact obstruction to replacing that measure by equal weights.

Boudourides analyzes susceptibility-dependent Friedkin--Johnsen response matrices and degree-weighted spectral formulas in an undirected **homogeneous-susceptibility**, fixed-boundary setting [2, Sections 2.2--2.6]. This supplies nearby Green-operator background but not the repeated predictive-feedback equilibrium or the heterogeneous stationary measure and the counterexample here. Ordinary reversibility and spectral calculus are classical [3]; their use is explicit in the proof rather than counted as new mathematics.

## Limitations

The spectral monotonicity requires reciprocal network weights, strictly interior peer susceptibilities, a single common platform susceptibility, infinite peer-relaxation intervals, and perfect feedback of all expressed opinions. It does not claim ordinary variance decreases on irregular/heterogeneous networks; in fact the displayed example refutes that extrapolation. No conclusion is asserted for directed nonreversible networks, finite peer-relaxation lengths, heterogeneous platform susceptibilities, learning error, or empirical social behavior. Historical priority outside the materially compared literature is not fully excluded.

## References

1. J. Wu, R. Abebe, C. Mendler--Dünner, *Opinion Dynamics in Learning Systems* (also displayed as *Reaching a Consensus in Predictive Loops*), arXiv:2603.12137v1, publicly posted 2026-03-12. https://arxiv.org/abs/2603.12137
2. M. Boudourides, *Boundary-Value Friedkin--Johnsen Dynamics and Influence-Based Centralities on Networks*, arXiv:2602.08704, 2026. https://arxiv.org/pdf/2602.08704
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, online monograph, Chapter 3, https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch3.S1.html

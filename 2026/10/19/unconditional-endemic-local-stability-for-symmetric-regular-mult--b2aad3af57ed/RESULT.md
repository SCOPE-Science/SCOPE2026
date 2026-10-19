# Unconditional endemic local stability for symmetric regular multigroup SAIRS networks

## Finding
For every connected undirected regular weighted contact network, the homogeneous endemic equilibrium of the SAIRS epidemic model is locally exponentially asymptotically stable whenever its reproduction number exceeds one, for arbitrary nonnegative vaccination and waning rates and arbitrary positive, potentially unequal, asymptomatic and symptomatic transmission and recovery rates. In particular, vaccination may exceed both stage-specific recovery rates. Stability holds against every network-heterogeneous infinitesimal perturbation, not merely perturbations constant over communities.

## Assumptions and scope
Fix an integer \(n\ge2\). Let \(W=(w_{ij})\) be a real symmetric nonnegative irreducible row-stochastic matrix, so \(W\mathbf1=\mathbf1\) and all its real eigenvalues satisfy \(-1\le q\le1\). Let \(\mu,\alpha,\delta_A,\delta_I,\beta_A,\beta_I>0\), \(\nu,\gamma\ge0\). For community \(i\), nonnegative fractions \(S_i,A_i,I_i,R_i\) sum to one. Write \(\phi_i=\sum_j w_{ij}(\beta_A A_j+\beta_I I_j)\). The equations, with rates per unit time, are
\[
\begin{aligned}
\dot S_i&=\mu-\phi_iS_i-(\mu+\nu)S_i+\gamma R_i,\\
\dot A_i&=\phi_iS_i-(\alpha+\delta_A+\mu)A_i,\\
\dot I_i&=\alpha A_i-(\delta_I+\mu)I_i,\\
\dot R_i&=\delta_A A_i+\delta_I I_i+\nu S_i-(\gamma+\mu)R_i.
\end{aligned}
\]
Set \(u=\alpha+\delta_A+\mu\), \(v=\delta_I+\mu\), \(d=\mu+\nu+\gamma\), \(B=\beta_A+\alpha\beta_I/v\), and \(\mathcal R_0=(\mu+\gamma)B/(du)\). Assume \(\mathcal R_0>1\). The theorem concerns the unique homogeneous endemic equilibrium and its full-space local linearized stability; it does not assert uniqueness of all spatially nonhomogeneous endemic equilibria or global convergence.

## Proof
**Equilibrium.** Write \(s=u/B\). Because \(\mathcal R_0>1\), \(s<(\mu+\gamma)/d\). Define
\[
a=\frac{\mu+\gamma-ds}{u+\gamma(1+\alpha/v)}>0,\qquad i=\frac{\alpha a}{v},\qquad r=\frac{\delta_Aa+\delta_Ii+\nu s}{\gamma+\mu}>0.
\]
The four equilibrium equations hold identically at \((s,a,i,r)\), and their sum implies \(s+a+i+r=1\). This is the unique equilibrium in the homogeneous strictly positive branch: the positive \(A\)-equation forces \(sB=u\), and the remaining equations determine \(a,i,r\).

**Jacobian reduction.** Put \(\lambda=Ba>0\), \(g=s\beta_A>0\), \(h=s\beta_I\alpha/v>0\), so \(g+h=u\). Eliminating \(R_i\) using \(R_i=1-S_i-A_i-I_i\), the derivative in a real \(W\)-eigenmode with eigenvalue \(q\) is
\[
J(q)=\begin{pmatrix}
-(d+\lambda)&-(\gamma+gq)&-(\gamma+(hv/\alpha)q)\\
\lambda&gq-u&(hv/\alpha)q\\
0&\alpha&-v
\end{pmatrix}.
\]
Symmetry gives an orthonormal eigenbasis, so these \(3\times3\) blocks account for every admissible perturbation in the simplex. The full \(4n\)-variable dynamics has in addition the independent total-population eigenvalues \(-\mu\), because \(\dot N_i=\mu(1-N_i)\).

**Uniform Routh–Hurwitz inequalities.** Write \(t=1-q\ge0\). Direct determinant expansion yields \(\det(zI-J(q))=z^3+c_1(t)z^2+c_2(t)z+c_3(t)\), with
\[
\begin{aligned}
c_1(t)&=d+\lambda+h+v+gt,\\
c_2(t)&=d(h+v)+\lambda(u+v+\gamma)+(dg+vu)t,\\
c_3(t)&=\lambda[vu+\gamma(\alpha+v)]+dvu\,t.
\end{aligned}
\]
Every coefficient is strictly positive for \(t\ge0\). Let \(H(t)=c_1(t)c_2(t)-c_3(t)\). At \(t=0\), since \(c_2(0)>\lambda(u+v+\gamma)>\lambda(u+\gamma)\), it suffices to check
\[
\begin{aligned}
c_1(0)(u+\gamma)-[vu+\gamma(\alpha+v)]
&=(d+\lambda+h)(u+\gamma)-\gamma\alpha>0.
\end{aligned}
\]
Indeed \(d=\mu+\nu+\gamma\ge\gamma\) and \(u=\alpha+\delta_A+\mu>\alpha\), while \(\lambda,h>0\); thus \(H(0)>0\). Furthermore
\[
H'(t)=dg\,c_1(0)+g\,c_2(0)+vu[c_1(0)-d]+2g(dg+vu)t>0.
\]
Hence \(H(t)>0\) for every \(t\ge0\). The cubic Routh–Hurwitz criterion implies all eigenvalues of every \(J(q)\) have strictly negative real parts. The remaining eigenvalues \(-\mu\) are negative. Therefore the equilibrium is locally exponentially asymptotically stable for every stated set of parameters and every stated network.

## Verification
The standalone `VERIFY.py` bundled with this result reconstructs the characteristic polynomial using exact symbolic algebra, verifies all three coefficient formulas identically, and computes full-network Jacobian eigenvalues for three independent admissible parameter examples. These computational checks supplement the symbolic inequalities above; the proof applies to all admissible parameters without relying on finite numerical sampling.

## Relationship to prior work
Ottaviano, Sensi and Sottile (arXiv:2202.02993, earliest public version 2022-02-07; subsequently published as a 2023 paper) establish endemic local stability for general multi-group SAIRS models under additional inequalities, including recovery rates exceeding vaccination; their theorem does not yield the present high-vaccination stability assertion. Their 2021 single-population analysis (arXiv:2109.05122) already treats the one-community unconditional case. Here the additional assertion is that **all spatially nonuniform eigenmodes** remain stable for any connected symmetric row-stochastic contact network, even when asymptomatic and symptomatic rates differ. The spectral decomposition and cubic Hurwitz calculation supply the relevant proof beyond the one-community result. The argument does not assert that diagonalization or Routh–Hurwitz is a new technique.

## Limitations
The conclusion is local and is limited to homogeneous rates with proportional, symmetric, row-stochastic contact matrices in both infection stages. It does not apply to arbitrary heterogeneous or directed contact matrices, different asymptomatic/symptomatic network eigenvectors, or networks with unequal row sums. No claims of global stability, epidemiological intervention optimality, or independent validation are made.

## References
1. C. Ottaviano, M. Sensi and S. Sottile, *Global stability of multi-group SAIRS epidemic models*, arXiv:2202.02993 (first public version 2022-02-07); Mathematical Methods in the Applied Sciences, DOI:10.1002/mma.9303.
2. C. Ottaviano, M. Sensi and S. Sottile, *Global stability of SAIRS epidemic models*, arXiv:2109.05122 (2021), for the previously known single-population case.

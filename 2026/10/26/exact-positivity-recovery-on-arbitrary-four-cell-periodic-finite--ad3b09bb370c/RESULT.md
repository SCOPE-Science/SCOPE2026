# Exact positivity recovery on arbitrary four-cell periodic finite-element meshes

## Finding
Let \(a,b,c,d>0\) be the lengths, in cyclic order, of four intervals in a periodic one-dimensional mesh, and let \(M\) and \(K\) be the consistent piecewise-linear finite-element mass and unit-diffusivity stiffness matrices. For \(t\ge0\), set \(P(t)=(M+tK)^{-1}M\). Then every diagonal entry of \(P(t)\) is positive, and for every \(t>0\) every entry between adjacent nodes is strictly positive. Each of its four ordered opposite-node entries has precisely one positive zero \(\rho_{ij}\), is negative for \(0<t<\rho_{ij}\), and positive for \(t>\rho_{ij}\). Consequently, with \(\rho=\max\{\rho_{02},\rho_{20},\rho_{13},\rho_{31}\}\),
\[
P(t)\ge0\quad\Longleftrightarrow\quad t=0\quad\text{or}\quad t\ge\rho.
\]
The four thresholds are **explicitly computable quadratic radicals**, with no mesh-ratio restrictions. Define \(Q(t)=M+tK\), and, for opposite ordered indices \((i,j)\), define the quadratic polynomial
\[
F_{ij}(t)=\frac{432abcd}{t}\bigl(\operatorname{adj}(Q(t))M\bigr)_{ij}=A_{ij}t^2+B_{ij}t+C_{ij}.
\]
The polynomial division is exact; \(A_{ij}>0\) and \(C_{ij}<0\). Thus
\[
\rho_{ij}=\frac{-B_{ij}+\sqrt{B_{ij}^{2}-4A_{ij}C_{ij}}}{2A_{ij}}.
\]
Although \(M\) and \(K\) are symmetric, \(P(t)\) generally is not: the four directional thresholds can differ.

## Assumptions and scope
Nodes \(0,1,2,3\) are numbered cyclically, with the element from node \(i\) to \(i+1\pmod4\) having length \(h_i\), where \((h_0,h_1,h_2,h_3)=(a,b,c,d)\). On every element of length \(h\), add \(\frac h6\begin{pmatrix}2&1\\1&2\end{pmatrix}\) to the two associated mass degrees of freedom and \(\frac1h\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\) to stiffness. The temporal integrator is a completed backward-Euler step; there are no boundary degrees of freedom or imposed Dirichlet data. Statements are for all positive real \(a,b,c,d\) and all real \(t\ge0\), including threshold equalities.

## Proof
The mass matrix is symmetric positive definite by its finite-element integral, and stiffness is positive semidefinite with \(K\mathbf1=0\). Hence \(Q(t)\) is positive definite and \(\det Q(t)>0\) for all \(t\ge0\). Also \(P(0)=I\), and \(P(t)\mathbf1=\mathbf1\).

All numerators can be checked by **one exact polynomial identity calculation**. Put \(G(t)=432abcd\,\operatorname{adj}(Q(t))M\). The included `verify.py` constructs the matrices symbolically, multiplies out the adjugate, and checks coefficient signs as polynomials in the *four independent* positive indeterminates \(a,b,c,d\). It establishes:

1. For each diagonal \((i,i)\), all four coefficients \([t^k]G_{ii}(t)\), \(k=0,1,2,3\), are nonzero polynomials with exclusively positive monomial coefficients.
2. For each adjacent ordered pair, \([t^0]G_{ij}=0\), while \([t^k]G_{ij}\), \(k=1,2,3\), have exclusively positive monomial coefficients.
3. For each opposite ordered pair, \([t^0]G_{ij}=0\), \([t^1]G_{ij}\) has exclusively negative monomial coefficients, and \([t^3]G_{ij}\) exclusively positive monomial coefficients. The sign of \([t^2]G_{ij}\) is unrestricted.

This is a finite check of symbolic identities and coefficient signs, rather than numerical sampling: positivity of \(a,b,c,d\) makes each monomial-sign conclusion uniform over the entire stated domain. Thus the sign of an opposite entry of \(P(t)\) for \(t>0\) is the sign of a quadratic \(A_{ij}t^2+B_{ij}t+C_{ij}\) with \(A_{ij}>0\), \(C_{ij}<0\). Its two roots have negative product, hence exactly one is positive, and the displayed radical is that root. This proves the asserted signs and the maximum-of-four exact threshold. At \(t=0\), \(P=I\).

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The checker proves the complete monomial-sign table exactly, verifies the alternating-mesh specialization, and terminates with the message `all symbolic coefficient tests, special-case recovery and matrix identities passed`. For \((a,b,c,d)=(1,2,3,4)\) and \(t=1\), exact matrix calculation gives \(P_{31}=-153/4025\) but \(P_{13}=63/1150\); at \(t=5/2\), every entry is positive, the smallest being \(207/15832\). The elementary sufficient \(M+tK\) Stieltjes condition would instead require \(t\ge8/3\). These examples check, but do not replace, the all-positive-parameter symbolic proof.

## Relationship to prior work
Li and Huang (2012) prove general sufficient conditions for discrete maximum principles of time-dependent finite-element diffusion, based on a Stieltjes-matrix test. Jin, Lazarov, Thomée, and Zhou (2015) discuss positivity thresholds and eventual positivity for finite-element diffusion/subdiffusion schemes, without this four-periodic-nonuniform exact classification. The new conclusion gives necessity, sufficiency, strict sign mechanisms and ordered-pair quadratic radicals for arbitrary four independent element lengths. The alternating subfamily \((a,b,a,b)\) has a previously known single threshold; the checker verifies exact specialization to \((\sqrt{a^2b^2+2ab(a+b)^2}-ab)/12\). In the unrestricted case there can instead be four different ordered threshold values.

## Limitations
This is a classification for four periodic \(P_1\) elements only, with constant unit diffusivity, consistent mass, and backward Euler. It does not establish a corresponding all-mesh criterion for five or more periodic elements, for variable diffusivity, or for different time integrators. The symbolic sign proof depends on exactly reproducible rational-polynomial expansions supplied in the checker; no external independent validation is claimed. Specialized finite-element literature not located by the stated searches could contain equivalent results.

## References
- X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657 (first public version September 25, 2012), especially Section 3, Theorem 3.1. https://arxiv.org/abs/1209.5657
- B. Jin, R. Lazarov, V. Thomée, and Z. Zhou, *On nonnegativity preservation in finite element methods for subdiffusion equations*, arXiv:1510.02825 (October 9, 2015), especially Section 4, Theorems 4.1–4.3. https://arxiv.org/abs/1510.02825
- V. Thomée and L. B. Wahlbin, *On the existence of maximum principles in parabolic finite element equations*, Mathematics of Computation **77** (2008), 11–19, doi:10.1090/S0025-5718-07-02021-2 (background; full text not inspected).

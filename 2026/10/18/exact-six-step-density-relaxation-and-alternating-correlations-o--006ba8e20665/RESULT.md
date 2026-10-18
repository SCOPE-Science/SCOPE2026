# Exact six-step density relaxation and alternating correlations of the golden-mean tent map

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(I=[(\varphi-1)/2,\varphi/2]\), and \(T(x)=\varphi\min\{x,1-x\}\). Write \(P\) for its Perron--Frobenius operator on densities with respect to Lebesgue measure on \(I\). Let \(V\) be the four-dimensional real space of functions which are affine separately on \(I_-=[(\varphi-1)/2,1/2]\) and \(I_+=[1/2,\varphi/2]\), with equality at the join not required. Define
\[
\rho(x)=\begin{cases}\frac{2}{3-\varphi},&x\in I_-,\\[2pt]\frac{2\varphi}{3-\varphi},&x\in I_+.\end{cases}
\]
For every \(q\in V\) and every integer \(k\ge0\), with \(m_q=\int_I q(x)\,dx\),
\[
\boxed{P^{6k}q=m_q\rho+\varphi^{-12k}(q-m_q\rho).}
\]
In particular, for any probability density \(q\in V\), the six-step subsequence is an **exact convex interpolation** to the invariant density; the total-variation distance satisfies
\[
\boxed{\|P^{6k}q-\rho\|_{\mathrm{TV}}=\varphi^{-12k}\|q-\rho\|_{\mathrm{TV}}.}
\]
Here total variation denotes the distance between absolutely continuous probability measures, or half the \(L^1\) norm of their density difference.

Set \(\mu=\int_I x\rho(x)\,dx=\frac14+\frac{3\sqrt5}{20}\), and define the **stationary coordinate covariance** \(C_n=\int_I(x-\mu)(T^n(x)-\mu)\rho(x)\,dx\). For all integers \(n\ge0\),
\[
\boxed{C_n=\varphi^{-2n}c_{n\bmod6}},\qquad
(c_0,c_1,c_2,c_3,c_4,c_5)=\left(\frac{3-\sqrt5}{40},-\frac1{30},\frac1{30},-\frac{3-\sqrt5}{40},\frac{7-3\sqrt5}{60},-\frac{7-3\sqrt5}{60}\right).
\]
Consequently \(C_{2j}>0\) and \(C_{2j+1}<0\) for all \(j\ge0\); the signed covariance has six distinct phase amplitudes and obeys \(C_{n+6}=\varphi^{-12}C_n\) exactly.

## Assumptions and scope

The map is considered only on its invariant interval \(I\), and end points of the two affine pieces are assigned arbitrarily (changing them does not affect densities). The exact density relaxation is for probability densities **piecewise affine on these two cells**, not for arbitrary absolutely continuous initial measures. The correlation claim uses the explicit invariant density \(\rho\) and the coordinate observable \(x\), not other observables or the Taylor--Couette Navier--Stokes system. Nonnegative normalized \(q\in V\) need not be continuous across the midpoint.

## Proof

Put \(\ell=(\varphi-1)/2\), \(u=\varphi/2\), and \(h=1/2\). Each \(x\in(\ell,h)\) has only the decreasing-branch preimage \(1-x/\varphi\). Each \(x\in(h,u)\) has two preimages \(x/\varphi\) and \(1-x/\varphi\). Thus, writing \(q(x)=A_-+B_-x\) for \(x\in I_-\) and \(q(x)=A_++B_+x\) for \(x\in I_+\), the transfer operator has the **exact matrix**
\[
\mathsf P=\begin{pmatrix}
0&\varphi^{-1}&0&\varphi^{-1}\\
\varphi^{-1}&\varphi^{-1}&0&\varphi^{-1}\\
0&0&0&-\varphi^{-2}\\
0&0&\varphi^{-2}&-\varphi^{-2}
\end{pmatrix}
\]
on column vectors \((A_-,A_+,B_-,B_+)^T\). Its characteristic polynomial factors over the real algebraic field as
\[
\det(tI-\mathsf P)=(t-1)(t+\varphi^{-2})(t^2+\varphi^{-2}t+\varphi^{-4}).
\]
The normalized density \(\rho\) corresponds to the vector \(r=(2/(3-\varphi),2\varphi/(3-\varphi),0,0)^T\) and satisfies \(\mathsf P r=r\). The mass functional \(J(v)=\int_I q\,dx\) satisfies \(J\mathsf P=J\) and \(Jr=1\). Therefore \(V=\operatorname{span}\{r\}\oplus\ker J\) is \(\mathsf P\)-invariant. The three characteristic roots on \(\ker J\) are distinct, namely \(-\varphi^{-2}\) and \(\varphi^{-2}e^{\pm2\pi i/3}\). Their sixth powers all equal \(\varphi^{-12}\). Diagonalizability of this three-dimensional restriction proves \(\mathsf P^6v=J(v)r+\varphi^{-12}(v-J(v)r)\), hence the announced identity for all \(k\ge0\). The exact total-variation equality follows from homogeneity of \(L^1\).

To compute covariance, let \(g(x)=(x-\mu)\rho(x)\). This belongs to \(V\), with \(J(g)=0\). By change of variables in the transfer formula, \(C_n=\int_I(x-\mu)(P^n g)(x)\,dx\). The mean \(\mu\) follows by integrating \(x\rho(x)\) over the two cells. Multiplying the displayed four-by-four matrix on the vector of \(g\) and integrating the resulting affine expressions produces for \(n=0,1,2,3,4,5\) the six coefficients \(C_n=\varphi^{-2n}c_n\) printed above. Since \(g\in\ker J\), the six-step operator identity gives \(P^{n+6}g=\varphi^{-12}P^ng\). This extends the six evaluations to **every** nonnegative integer \(n\). Finally \(3-\sqrt5>0\) and \(7-3\sqrt5>0\), proving strict sign alternation.

## Verification

The accompanying `verify.py` independently reconstructs the transfer matrix, the invariant density and mass functional, checks the exact polynomial and sixth-power matrix identities over \(\mathbb Q(\sqrt5)\), and compares 18 independent covariance coefficients against the six-phase formula in exact arithmetic. Running `python verify.py` with SymPy reports `PASS`. These symbolic identities are finite algebraic verifications supporting the infinite proof; they do not constitute an exhaustive numerical orbit simulation.

## Relationship to prior work

Wang et al. specify this exact golden-mean tent map and its two-cell invariant density as a statistical model for a spline return map; their manuscript evaluates a **one-time probability density** and does not give the claimed six-step relaxation or all-lag coordinate-covariance constants [1]. The classical ChaosBook exercise/solution already establishes the **full Perron--Frobenius spectral determinant** for this golden-mean pruned map [2]. In particular, the four eigenvalues used here are not claimed as a newly discovered spectrum. The present result concerns the exact projection of the degree-one, piecewise-affine density space and the amplitude/sign-resolved coordinate correlations; the previously known eigenvalue locations alone do not determine their coefficients, although they are essential prior groundwork. Related stationary autocorrelation computations for other interval maps do not imply this precise model's formula.

## Limitations

This theorem is an exact calculation for the canonical tent map, not a proof of the same time-correlations for its nonlinearly conjugate spline map or physical fluid. A topological conjugacy need not preserve coordinate covariance. The restriction of initial densities to \(V\) is essential for the exact six-step equality. Further historical literature could contain an equivalent observable-level correlation calculation; no independent mathematical or priority audit has been performed.

## References

1. Wang, Ayats, Deguchi, Meseguer and Mellibovsky, arXiv:2409.09234v1 (2024-09-13), https://arxiv.org/html/2409.09234v1.
2. Cvitanović et al., Chaos: Classical and Quantum (ChaosBook), version 11.2.2 (2005), Exercise 13.8 and Solution 13.8 (p. 797), https://www.chaosbook.org/version11/chapters/ChaosBook11_2_2.pdf.

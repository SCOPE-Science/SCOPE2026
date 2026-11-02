# A sharp universal competition cutoff for attracting exchange two-cycles in a symmetric Ricker map

## Finding

Consider the two-species Ricker competition map
\[
F_{\rho,\gamma}(x,y)=\bigl(\rho x e^{-x-\gamma y},\ \rho y e^{-y-\gamma x}\bigr),
\qquad \rho>0,\quad\gamma>0,
\]
on the strictly positive quadrant. An **exchange two-cycle** means a least-period-two orbit of the form \((u,v)\longleftrightarrow(v,u)\), with \(u>v>0\); the order \(u>v\) merely fixes its representative.

**Theorem.** A positive exchange two-cycle exists if and only if
\[
0<\gamma<1,\qquad
\log\rho>\frac{2(1+\gamma)}{1-\gamma}.
\]
When it exists it is unique up to interchange of its two points. Put
\[
A(z)=\frac{\operatorname{artanh}z}{z},\qquad
q(z)=(1-z^2)A(z),\qquad 0<z<1.
\]
Its unique parameter is determined by
\[
\log\rho=\frac{2(1+\gamma)}{1-\gamma}A(z),\qquad
u=\frac{2A(z)(1+z)}{1-\gamma},\quad
v=\frac{2A(z)(1-z)}{1-\gamma}.
\]
For each \(0<\gamma<1\), define \(z_{-}(\gamma)\) and \(z_{+}(\gamma)\) as the unique roots in \((0,1)\) of, respectively,
\[
q(z_{-})=\frac{1-\gamma}{1+\gamma},
\qquad
(1+\gamma)q(z_{+})+\frac{1-\gamma}{2A(z_{+})}=1.
\]
Then the exchange two-cycle is **locally exponentially attracting if and only if**
\[
\boxed{z_{-}(\gamma)<z<z_{+}(\gamma).}
\]
There is a nonempty attracting interval in the growth parameter \(\rho\) if and only if \(0<\gamma<\gamma_*\), where the **universal sharp competition cutoff** is
\[
\boxed{\gamma_*=
\frac{1}{1+2A(z_*)}=0.277839040264087\ldots},
\]
and \(z_*=0.75175950359911\ldots\) is the unique solution in \((0,1)\) of
\[
\boxed{(1-z_*^2)\operatorname{artanh}z_*=z_*^3.}
\]
For \(\gamma\ge\gamma_*\), no positive exchange two-cycle is locally exponentially attracting, regardless of \(\rho\). At \(\gamma=\gamma_*\) the two stability boundaries coalesce and the two eigenvalues of the symmetry-reduced one-step matrix are both \(-1\); the corresponding two-step multipliers are both \(+1\). These equalities assert nonhyperbolicity, not nonlinear attraction or a particular bifurcation type.

For \(0<\gamma<\gamma_*\), the unique attracting window is exactly
\[
\exp\!\left(\frac{2(1+\gamma)}{1-\gamma}A(z_{-}(\gamma))\right)
<\rho<
\exp\!\left(\frac{2(1+\gamma)}{1-\gamma}A(z_{+}(\gamma))\right).
\]

## Assumptions and scope

All statements concern the explicitly displayed symmetric two-dimensional difference map, strictly positive initial states, and positive parameters \(\rho\) and \(\gamma\). The competition coefficient is the same in both cross terms, and both species have the same intrinsic growth factor. An exchange cycle is strictly different from a synchronous two-cycle on the diagonal \(x=y\). Local exponential attraction means that both eigenvalues of the derivative of the second iterate at either cycle point have modulus strictly less than one. At a boundary eigenvalue of modulus one, this theorem does not classify nonlinear stability.

## Proof

**1. Unique exact exchange orbit.** Suppose \(F(u,v)=(v,u)\) with \(u>v>0\). Dividing the two update equations by the original populations, taking logarithms and subtracting gives
\[
(1-\gamma)(u-v)=2\log(u/v)>0.
\]
Hence \(\gamma<1\). Adding the equations gives \(2\log\rho=(1+\gamma)(u+v)\). Let \(S=u+v\) and \(z=(u-v)/S\), so \(z\in(0,1)\). Since \(\log(u/v)=2\operatorname{artanh}z\), the preceding identities become
\[
S=\frac{4A(z)}{1-\gamma},\qquad
\log\rho=\frac{2(1+\gamma)}{1-\gamma}A(z).
\]
Consequently \(u=S(1+z)/2\) and \(v=S(1-z)/2\), giving the formula in the theorem. Conversely these expressions satisfy both original exchange equations: the logarithmic sum and difference determine them uniquely. The function \(A(z)\) increases strictly from \(1\) to \(+\infty\). Indeed,
\[
A'(z)=\frac{z/(1-z^2)-\operatorname{artanh}z}{z^2}>0,
\]
because the numerator vanishes at zero and has positive derivative \(2z^2/(1-z^2)^2\). Thus the parameter equation has exactly one solution \(z\in(0,1)\) precisely when the stated strict growth inequality holds.

**2. Exact two-step spectrum.** Let \(P\) exchange the two coordinates, and define \(B=P\,DF(u,v)\). Since \(F\) commutes with \(P\), the two-step Jacobian at \((u,v)\) equals \(B^2\). Using \(F(u,v)=(v,u)\), direct differentiation yields
\[
B=
\begin{pmatrix}
-\gamma u & (u/v)(1-v)\\
(v/u)(1-u)&-\gamma v
\end{pmatrix}.
\]
Its trace and determinant, with \(q(z)=(1-z^2)A(z)\), are
\[
T=-\gamma S,\qquad
D=(\gamma^2-1)uv+S-1
=S\bigl[1-(1+\gamma)q(z)\bigr]-1.
\]
The two-step Floquet multipliers are the squares of the two roots of \(\lambda^2-T\lambda+D=0\). Therefore the exchange orbit attracts exponentially exactly when the real matrix \(B\) is Schur stable. The strict degree-two Schur conditions are
\[
1+T+D>0,\qquad 1-T+D>0,\qquad1-D>0.
\]
Substitution gives the **exact** identities
\[
\begin{aligned}
1+T+D&=4A(z)\left[1-\frac{1+\gamma}{1-\gamma}q(z)\right],\\
1-T+D&=(1+\gamma)S\,[1-q(z)],\\
1-D&=S\left[(1+\gamma)q(z)-1+\frac{1-\gamma}{2A(z)}\right].
\end{aligned}
\]
To analyze their signs, note \(q\) decreases strictly from \(1\) to \(0\), because
\[
q'(z)=\frac{z-(1+z^2)\operatorname{artanh}z}{z^2}<0:
\]
the numerator is zero at zero and has derivative \(-2z\operatorname{artanh}z-2z^2/(1-z^2)<0\). Thus \(1-q(z)>0\) throughout \((0,1)\). The first Schur condition holds exactly when \(z>z_{-}\); the third holds exactly when \(z<z_{+}\). The root \(z_{+}\) exists uniquely since its defining left side decreases strictly from \((3+\gamma)/2>1\) to \(0\). This proves the sharp open stability interval.

**3. The universal coupling cutoff.** At \(z=z_{-}(\gamma)\), the first Schur inequality becomes equality. There \(D=\gamma S-1\). Because the third Schur expression decreases strictly in \(z\), we have
\[
z_{-}<z_{+}\ \Longleftrightarrow\ 1-D\big|_{z=z_-}>0
\ \Longleftrightarrow\ \gamma S(z_{-})<2.
\]
As \(\gamma\) increases from zero to one, \(z_{-}\) increases strictly from zero to one; hence \(A(z_{-})\) increases from one to infinity. Therefore
\[
\gamma S(z_{-})=\frac{4\gamma A(z_{-})}{1-\gamma}
\]
increases strictly and continuously from zero to infinity. Exactly one crossover exists. At that crossover, \(\gamma S=2\) implies \(\gamma=1/(1+2A)\); combining this with \(q=(1-\gamma)/(1+\gamma)\) gives \(q=z^2\), or
\[
(1-z^2)\operatorname{artanh}z=z^3.
\]
The latter equation has exactly one interior root because \(q(z)\) is strictly decreasing from one to zero whereas \(z^2\) is strictly increasing from zero to one. Thus its root gives precisely \(\gamma_*\), and the claimed strict coupling classification follows. At the crossover, \(T=-\gamma S=-2\) and \(D=1\), so the two roots of the characteristic polynomial are both \(-1\).

**4. Exact stable witness.** With \(\gamma=1/10\) and \(z=3/5\), the formulas yield
\[
\rho=2^{110/27},\qquad
u=\frac{160\log2}{27},\qquad
v=\frac{40\log2}{27}.
\]
The map exchanges \((u,v)\) and \((v,u)\). The matrix \(B\) has
\[
T=-\frac{20\log2}{27},\qquad
D=\frac{200\log2}{27}-1-\frac{704(\log2)^2}{81}.
\]
Its eigenvalues are approximately \(0.0708018922372\) and \(-0.584244248208\), so both two-step multipliers are strictly inside the unit disk. The reproducible script checks the exact identities and reports the strict inequalities; numerical approximations are illustrative rather than a substitute for the analytical threshold proof.

## Verification

The standalone standard-library script `verification/check_ricker_swap.py` recomputes the two scalar boundary equations by bisection, differentiates the two-step map, confirms that its monodromy equals \(B^2\), verifies the exact logarithmic witness, and checks the Schur identities over 300 additional seeded parameter samples. Its output includes \(z_*=0.75175950359911\) and \(\gamma_*=0.27783904026409\). All reported checks executed successfully. The proof above, including uniqueness and the universal parameter quantifiers, is analytical; the finite checks do not establish those general statements on their own.

## Relationship to prior work

The two-dimensional Ricker competition model, including symmetric coupling and observed out-of-phase period-two oscillations, is established in previous literature. Kulakov, Neverova, and Frisman (2022), especially §4.1, treat the symmetric case and study the appearance and stability loss of antiphase cycles numerically through dynamic-mode diagrams and iterated-map nullclines. Their §4 explains that finding these periodic points numerically is difficult. Goldar and collaborators (2026), §§2 and 5, study this model in a general asymmetric parameter regime and give implicit conditions and generic Jacobian-based stability criteria for period-two solutions. The present finding does **not** claim the existence of out-of-phase oscillations or the generic Schur test as new. It gives the exact closed one-dimensional parametrization of the exchange branch, a necessary-and-sufficient open growth interval for local exponential attraction, and the analytically sharp *parameter-independent* competition cutoff \(\gamma_*\).

A published spectral-reduction result for **synchronous** cycles of row-regular multispecies Ricker systems does not imply the criterion here: the present orbit is off the synchronization diagonal and swaps species each step. Known low-growth global convergence results also do not cover the high-growth attracting exchange window. The inspected sources did not exhibit the same complete closed criterion; this is evidence of a gap, not proof of worldwide historical priority.

## Limitations

The result applies only to positive **exchange** two-cycles in an exchange-symmetric two-species map. It does not classify asymmetric period-two orbits, synchronous two-cycles, higher-period dynamics, chaotic attractors, or global basins. At an equality boundary, the linearized two-step dynamics is nonhyperbolic, so nonlinear stability and any associated flip/Neimark–Sacker bifurcation require further analysis. The conclusions are independent of whether other attractors coexist. The closest earlier 2022 paper already recognizes antiphase cycles numerically, and some older related full texts were not available; independent historical-priority assessment remains necessary.

## References

1. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen, and M. Izadi, “Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth,” *Discrete Dynamics in Nature and Society* (first published 16 September 2026). DOI: https://doi.org/10.1155/ddns/7255117. Open full text: https://onlinelibrary.wiley.com/doi/10.1155/ddns/7255117.
2. M. Kulakov, G. Neverova, and E. Frisman, “The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability,” *Mathematics* **10** (2022), 1076, §4.1. DOI: https://doi.org/10.3390/math10071076. Accessible full text: https://www.researchgate.net/publication/359552540_The_Ricker_Competition_Model_of_Two_Species_Dynamic_Modes_and_Phase_Multistability.
3. S. Baigent et al., “A global picture for the planar Ricker map,” *Journal of Difference Equations and Applications* (2023). DOI: https://doi.org/10.1080/10236198.2023.2222855 (only summary/introduction available in this review).
4. R. Luis, S. Elaydi, and H. Oliveira, 2011 stability and bifurcation study of a planar Ricker competition map. DOI: https://doi.org/10.1080/17513758.2011.581764 (abstract available; full text not inspected).

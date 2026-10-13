# Rectangular detectors on weighted rook quantum networks: exact resonance and capture laws

## Finding

**Theorem (rectangular absorption, including a rank-one resonance).** Let integers \(m,n\geq2\), positive hopping strengths \(a,b>0\), and nonempty subsets \(R\subseteq\{0,\ldots,m-1\}\), \(T\subseteq\{0,\ldots,n-1\}\) of sizes \(r,s\) be given. On the vertex space of \(K_m\square K_n\), use
\[
H=a A(K_m)\otimes I_n+bI_m\otimes A(K_n),\qquad H_{\rm eff}=H-i\sum_{(i,j)\in R\times T}\gamma_{ij}|i,j\rangle\langle i,j|,
\]
where all \(\gamma_{ij}>0\). Write \(\alpha=\min(r,m-1)\), \(\beta=\min(s,n-1)\), and \(\epsilon=\mathbf1_{\{am=bn,\ r<m,\ s<n\}}\). The dimension of the subspace eventually absorbed (the orthogonal complement of the loss-free subspace) is exactly
\[
\boxed{\dim\mathcal B=(1+\alpha)(1+\beta)-\epsilon.}
\]

For a unit initial state at \((x,y)\), eventual absorption \(C(x,y)=1-\lim_{t\to\infty}\|e^{-iH_{\rm eff}t}|x,y\rangle\|^2\) obeys the following closed formula. Set
\[
c_R(x)=\begin{cases}1&x\in R,\\ 1/(m-r)&x\notin R,\end{cases}\qquad
c_T(y)=\begin{cases}1&y\in T,\\ 1/(n-s)&y\notin T.\end{cases}
\]
(The second branch of either definition is unused when that subset is the entire factor.) Away from the resonance \(am=bn\), or when \(r=m\) or \(s=n\),
\[
\boxed{C(x,y)=c_R(x)c_T(y).}
\]
At the resonance, if both subsets are proper, additionally set
\[
h_R(x)=\begin{cases}1&x\in R,\\-r/(m-r)&x\notin R,\end{cases}\quad
h_T(y)=\begin{cases}1&y\in T,\\-s/(n-s)&y\notin T.\end{cases}
\]
Then
\[
\boxed{C(x,y)=c_R(x)c_T(y)-\frac{\bigl(h_R(x)-h_T(y)\bigr)^2}{mn\bigl(r/(m-r)+s/(n-s)\bigr)}.}
\]
The correction is nonnegative and arises from **exactly one additional normalized dark vector** at resonance. Every formula is independent of the individual positive absorbing rates. More generally, for any initial density operator \(\rho\), eventual absorption is \(\operatorname{Tr}(P_{\mathcal B}\rho)\), with \(P_{\mathcal B}\) constructed in the proof.

A rectangular detector set achieves complete eventual absorption of **every** initial state away from resonance exactly when \(r\ge m-1\) and \(s\ge n-1\). At resonance complete absorption holds exactly when these inequalities hold *and* either \(r=m\) or \(s=n\). Consequently, the smallest sizes of completely absorbing rectangular sets are \((m-1)(n-1)\) off resonance and \(mn-\max(m,n)\) on resonance. The equal-weight square \(m=n,\ a=b\) is a special case.

## Assumptions and scope

The graph has vertices \((x,y)\in\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\). Vertices in the same row or in the same column are joined, with real hopping amplitudes \(a\) and \(b\) in the respective Cartesian factors. There are no additional onsite potentials, dephasing, interactions, or unmonitored losses. Precisely the rectangle \(R\times T\) is absorbing, with arbitrary rate \(\gamma_{ij}>0\) at each detector. The asymptotic claim is about infinite time. All quantifiers apply to every integer \(m,n\ge2\), every nonempty rectangle, every \(a,b>0\), every strictly positive rate assignment, and every localized initial vertex; the density-operator extension holds by linearity. Only equality of the two spectral gaps, not rationality of their ratio, is relevant.

## Proof

**1. Asymptotic capture equals spectral visibility.** Let \(\Gamma=\sum_{R\times T}\gamma_{ij}|i,j\rangle\langle i,j|\). For a solution \(\psi(t)=e^{-i(H-i\Gamma)t}\psi(0)\),
\[
\frac{d}{dt}\|\psi(t)\|^2=-2\langle\psi(t),\Gamma\psi(t)\rangle\le0.
\]
If \((H-i\Gamma)v=zv\), then \(\operatorname{Im}z=-\langle v,\Gamma v\rangle/\|v\|^2\le0\); equality requires \(\Gamma v=0\) and hence \(Hv=zv\). A Jordan block on the real axis would cause polynomial growth in the contractive propagator and is impossible. All other generalized eigenspaces decay exponentially. Thus the asymptotic norm is exactly the squared norm of the initial projection onto the maximal \(H\)-invariant subspace in \(\ker\Gamma\). If \(P_\lambda\) denotes the **orthogonal** spectral projector of \(H\) at eigenvalue \(\lambda\), its orthogonal complement is
\[
\mathcal B=\operatorname{span}\{P_\lambda|i,j\rangle:\lambda\in\operatorname{spec}(H),\ (i,j)\in R\times T\}.
\]
This argument also proves the asserted independence of all positive detector rates.

**2. The four tensor eigenspaces and the unique collision.** Let \(u_m=m^{-1/2}\mathbf1_m\), \(E_m=u_mu_m^*\), \(F_m=I_m-E_m\), with analogous definitions for \(n\). Because \(A(K_m)=mE_m-I_m\), the four mutually orthogonal spectral projections are
\[
E_m\otimes E_n,\quad F_m\otimes E_n,\quad E_m\otimes F_n,\quad F_m\otimes F_n,
\]
with respective eigenvalues \(a(m-1)+b(n-1)\), \(a(m-1)-b\), \(-a+b(n-1)\), \(-a-b\). Since \(a,b>0\), the only possible collision is between the two middle eigenvalues, precisely when \(am=bn\).

**3. Distinct gaps.** Define \(U_R=\operatorname{span}\{F_me_i:i\in R\}\), and \(U_T=\operatorname{span}\{F_ne_j:j\in T\}\). Their dimensions are \(\alpha,\beta\), respectively: for a proper subset, its projected coordinate vectors are linearly independent; for the full set, their sole dependence is their sum. Distinct spectral values let the four detector-projected blocks be separated. Thus
\[
\mathcal B=(\operatorname{span}\{u_m\}\oplus U_R)\otimes(\operatorname{span}\{u_n\}\oplus U_T),
\]
and \(\dim\mathcal B=(1+\alpha)(1+\beta)\). For proper \(R\), the first factor is exactly the span of the individual coordinate vectors in \(R\) and the uniform vector on its complement, because it contains \(u_m\) and \(F_me_i\) for all \(i\in R\). The diagonal of its orthogonal projector is \(c_R(x)\); the other factor analogously has diagonal \(c_T(y)\). This gives the first sitewise formula.

**4. Coincident gaps.** The first and fourth spectral blocks retain ranks \(1\) and \(\alpha\beta\). In the middle direct sum \((U_R\otimes\operatorname{span}\{u_n\})\oplus(\operatorname{span}\{u_m\}\otimes U_T)\), a detector projection is the sum of its two components, rather than two separately accessible vectors. For proper \(R,T\), write the coefficient array as an \(r\times s\) matrix \(X\): its first component depends injectively on its row sums and its second injectively on its column sums. These sums satisfy one and only one relation, equality of their grand totals; therefore the middle rank is \(r+s-1\), one below \(r+s\). If \(R\) or \(T\) is full, its centered coordinate vectors have a constant-vector kernel; this removes that one relation, and the middle rank is \(\alpha+\beta\). This proves the dimension formula in all boundary cases.

When both subsets are proper, define \(h_R\in\mathbb R^m\) by its displayed components, and \(h_T\in\mathbb R^n\) similarly. Both have coordinate sum zero, belong respectively to \(U_R,U_T\), and take the constant value \(1\) on their detector subsets. Hence
\[
D=h_R\otimes\mathbf1_n-\mathbf1_m\otimes h_T
\]
lies in the degenerate middle eigenspace and vanishes at **every** detector. Its two tensor terms are orthogonal (both centered vectors have zero sum), and direct summation gives
\[
\|D\|^2=mn\left(\frac r{m-r}+\frac s{n-s}\right).
\]
The preceding rank computation shows that the resonant bright space is *exactly* the nonresonant tensor-product visibility space minus \(\operatorname{span}\{D\}\). Subtracting \(|D\rangle\langle D|/\|D\|^2\) from its projector yields the second sitewise formula. No other dark direction is created by resonance.

**5. Full capture and minimum rectangle size.** Each factor visibility space equals the whole coordinate factor exactly when \(r\ge m-1\), respectively \(s\ge n-1\). Their tensor product is full precisely when both conditions hold. At resonance an additional dimension is lost exactly if both detector subsets are proper. Therefore complete capture needs one entire factor selected as well as the other factor minus at most one point. Minimizing \(rs\) over admissible rectangles gives the asserted minima.

## Verification

Run \(python3\ \texttt{verify.py}\) with NumPy and SciPy installed (see \(\texttt{requirements.txt}\)). This independently diagonalizes the original Hamiltonian, groups equal eigenvalues, projects arbitrary rectangular detectors into *numerically calculated* eigenspaces, and compares the resulting spectral-visible projector diagonals and rank with the theorem. It checks every \(m,n\in\{2,3,4,5,6\}\), every allowed \(r,s\), and both a resonant and a nonresonant positive hopping pair: 800 rank-and-sitewise comparisons. Twelve additional calculations propagate states with varied positive detector rates under the non-Hermitian Hamiltonian and compare late-time norm loss. The checked package run returned

```text
VERIFY_OK spectral_rank_and_sitewise_cases=800 direct_loss_cases=12
```

The eigenspace-projection tests and time evolution corroborate but do not prove the all-size theorem; analytic steps 1–5 supply that proof. Exact equality of spectral gaps is checked symbolically in the derivation and implemented by construction in test cases; floating-point eigensolver tolerance is not used to infer a general collision classification.

## Relationship to prior work

Ge, Greenberg, Perez and Tamon (arXiv:1009.1340, initially public 2010-09-07) discuss Cartesian-product continuous-time walks and their tensor adjacency rule in the context of perfect state transfer, not absorption. Razzoli, Paris and Bordone (arXiv:2011.13794, 2020) establish spectral/Krylov transport efficiency and explicitly evaluate *single-site* trapping on several graph families, including strongly regular graphs. **Their strongly-regular one-sink result already covers the equal-weight square rook graph with one detector**; this known subcase is not an originality claim. Cavazzoni et al. (arXiv:2205.09408) analyze perturbations of complete, complete-bipartite, and star graphs with a single trap. The result here is the multi-detector rectangular and two-independent-hopping classification, its rank-one resonance and closed sitewise laws. The general spectral projector principle is also not claimed as new.

## Limitations

The theorem does not address arbitrary non-rectangular detector patterns, spatial disorder, complex hopping phases, dephasing, nonlinear or interacting dynamics, or nonpositive detector rates. At a resonance, an arbitrarily small detuning changes the infinite-time answer but not the finite-time continuity of the propagator. No uniform relaxation-time estimate as the resonance is approached is claimed. The finite verifier does not establish originality or infinite-size correctness; separate literature comparison remains subject to an unlocated equivalent specialized result.

## References

1. Y. Ge, B. Greenberg, O. Perez, C. Tamon, *Perfect state transfer, graph products and equitable partitions*, arXiv:1009.1340 (initial submission 2010-09-07), especially Section 2 and its Cartesian adjacency identity.
2. L. Razzoli, M. G. A. Paris, P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (initial submission 2020-11-27), especially Sections 3–4, strongly regular graph capture Eq. (25), and Appendix A.
3. S. Cavazzoni, L. Razzoli, P. Bordone, M. G. A. Paris, *Perturbed graphs achieve unit transport efficiency without environmental noise*, arXiv:2205.09408 (2022), especially Sections II, IV–VI and its single-trap model.

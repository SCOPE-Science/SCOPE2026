# Uniqueness and minimal product length of the closest separable state on the one-zero Dicke edge
## Finding
For every integer \(n\ge 2\) and every \(0<s<1\), let
\[
\rho_{n,s}=s\lvert1\rangle^{\otimes n}\!\langle1\rvert^{\otimes n}+(1-s)\lvert D_{n,1}\rangle\!\langle D_{n,1}\rvert,
\]
where \(\lvert D_{n,1}\rangle\) is the normalized symmetric Dicke state with exactly one \(0\) and \(n-1\) entries equal to \(1\). Put
\[
p=\frac{1-s}{n},\qquad q=\frac{n-1+s}{n},
\]
and
\[
\lvert\phi_\varphi\rangle=\sqrt p\,e^{i\varphi}\lvert0\rangle+\sqrt q\,\lvert1\rangle.
\]
The separable state
\[
\sigma_{n,s}=\int_0^{2\pi}\frac{d\varphi}{2\pi}\,
\lvert\phi_\varphi\rangle^{\otimes n}\!\langle\phi_\varphi\rvert^{\otimes n}
\]
is the unique closest fully separable state to \(\rho_{n,s}\) in relative entropy. Moreover its minimum number of pure product terms in any convex decomposition is exactly \(n+1\), and the minimum is attained by the finite roots-of-unity ensemble
\[
\sigma_{n,s}=\frac1{n+1}\sum_{j=0}^{n}
\lvert\phi_{2\pi j/(n+1)}\rangle^{\otimes n}
\!\langle\phi_{2\pi j/(n+1)}\rvert^{\otimes n}.
\]
Thus an optimizer that was previously supplied as a continuous phase average is rigid in the interior of this edge: the closest separable density operator is unique, while an optimal finite product ensemble needs and suffices to have \(n+1\) terms.

## Assumptions and scope
The relative entropy of entanglement is minimized over the full set of fully separable \(n\)-qubit density operators. The parameter interval is strictly interior, \(0<s<1\). Both endpoint cases are excluded because the rank and equality structure change there. Logarithms in the relative entropy may be taken in any fixed base; base two is used below to match the cited formulas.

The Dicke convention is the one used in the cited symmetric-state literature: \(\lvert D_{n,k}\rangle\) has exactly \(k\) zeros. With
\[
B_k=\binom nk p^kq^{n-k},
\]
the phase average is diagonal in the Dicke basis with eigenvalues \(B_0,\ldots,B_n\). Since \(p,q>0\), all \(B_k\) are positive.

## Proof
Let
\[
P_0=\lvert D_{n,0}\rangle\!\langle D_{n,0}\rvert,
\qquad
P_1=\lvert D_{n,1}\rangle\!\langle D_{n,1}\rvert,
\]
and define the positive operator
\[
A=\frac{s}{q^n}P_0+\frac1{q^{n-1}}P_1.
\]
We first characterize exactly the product vectors saturating the support inequality \(\langle A\rangle\le1\).

Write a normalized product vector, away from harmless coordinate-boundary cases handled by continuity, as
\[
\lvert\Psi\rangle=\bigotimes_{j=1}^n
\frac{x_j\lvert0\rangle+\lvert1\rangle}{\sqrt{1+\lvert x_j\rvert^2}}.
\]
Set
\[
t=\frac pq=\frac{1-s}{n-1+s},
\qquad
Q=\frac1{n^2}\left\lvert\sum_{j=1}^n x_j\right\rvert^2.
\]
A direct overlap calculation gives
\[
\langle\Psi\rvert A\lvert\Psi\rangle
=
\frac{(1+t)^{n-1}\bigl(1-(n-1)t+nQ\bigr)}
{\prod_{j=1}^n(1+\lvert x_j\rvert^2)}.
\]
Arithmetic-geometric mean followed by Cauchy gives
\[
\prod_{j=1}^n(1+\lvert x_j\rvert^2)
\ge
\left(1+\frac1n\sum_{j=1}^n\lvert x_j\rvert^2\right)^n
\ge(1+Q)^n.
\]
Since \(u\mapsto(1+u)^n\) is strictly convex for \(n\ge2\), its tangent at \(u=t\) yields
\[
(1+Q)^n\ge
(1+t)^{n-1}\bigl(1-(n-1)t+nQ\bigr).
\]
Hence \(\langle A\rangle\le1\) on every product state and therefore \(\operatorname{Tr}(A\tau)\le1\) on every fully separable state \(\tau\).

All three inequalities are equalities simultaneously exactly when
\[
x_1=\cdots=x_n=\sqrt t\,e^{i\varphi}
\]
for some phase \(\varphi\). Consequently the pure product states saturating \(\langle A\rangle=1\) are precisely
\[
\lvert\phi_\varphi\rangle^{\otimes n}.
\]

Now let \(\tau\) be any fully separable state for which the relative entropy \(D(\rho_{n,s}\Vert\tau)\) is finite, and set
\[
r_j=\operatorname{Tr}(P_j\tau),\qquad j\in\{0,1\}.
\]
Vector-state Jensen for the concave logarithm gives
\[
\operatorname{Tr}(\rho_{n,s}\log\tau)
\le s\log r_0+(1-s)\log r_1.
\]
Because \(B_0=q^n\) and \(B_1=(1-s)q^{n-1}\), weighted arithmetic-geometric mean and the support inequality give
\[
\left(\frac{r_0}{B_0}\right)^s
\left(\frac{r_1}{B_1}\right)^{1-s}
\le
s\frac{r_0}{B_0}+(1-s)\frac{r_1}{B_1}
=
\operatorname{Tr}(A\tau)
\le1.
\]
Combining these inequalities yields
\[
D(\rho_{n,s}\Vert\tau)\ge D(\rho_{n,s}\Vert\sigma_{n,s}).
\]
This reproduces, by a self-contained supporting-hyperplane argument, the already known optimal value and the fact that \(\sigma_{n,s}\) is a closest separable state.

It remains to prove uniqueness. If \(\tau\) is any closest separable state, equality must hold throughout the chain above. In particular \(\operatorname{Tr}(A\tau)=1\). Decompose \(\tau\) into pure product states. Each component has expectation at most one against \(A\), so every component of positive weight must itself saturate the bound. The equality classification therefore forces
\[
\tau=\int
\lvert\phi_\varphi\rangle^{\otimes n}\!\langle\phi_\varphi\rvert^{\otimes n}
\,d\mu(\varphi)
\]
for some probability measure \(\mu\) on the circle.

Equality in vector-state Jensen for the \(P_0\) term, whose coefficient \(s\) is positive, implies that \(\lvert D_{n,0}\rangle\) is an eigenvector of \(\tau\). In the Dicke basis the orbit mixture has entries
\[
\langle D_{n,k}\rvert\tau\lvert D_{n,\ell}\rangle
=
\sqrt{B_kB_\ell}\int e^{i(k-\ell)\varphi}\,d\mu(\varphi).
\]
Because all \(B_k>0\), the eigenvector condition at \(k=0\) forces
\[
\int e^{im\varphi}\,d\mu(\varphi)=0,
\qquad m=1,\ldots,n.
\]
Every nonzero difference \(k-\ell\) lies between \(-n\) and \(n\), so all off-diagonal Dicke entries vanish. The diagonal entries are already fixed at \(B_k\). Hence \(\tau=\sigma_{n,s}\), proving uniqueness.

Finally, \(\sigma_{n,s}\) has rank \(n+1\), since all \(B_k\) are positive. Any pure-state convex decomposition, and therefore any pure-product decomposition, needs at least \(n+1\) terms. The uniform \((n+1)\)-st roots of unity obey
\[
\frac1{n+1}\sum_{j=0}^{n}e^{2\pi i jm/(n+1)}=0,
\qquad m=1,\ldots,n,
\]
so the displayed roots-of-unity ensemble reproduces exactly the same Dicke-diagonal state. Thus the lower bound is attained, and the minimum product length is \(n+1\).

## Verification
The accompanying `verify.py` checks the coefficient identities entering the witness, exact binomial normalization for several rational interior parameters, the convex tangent inequality on rational test grids, and the vanishing of the first \(n\) Fourier moments for the \((n+1)\)-st roots of unity. It prints `VERIFY_OK` on success.

Those computations are supplementary. The theorem for all integers \(n\ge2\) and all real \(0<s<1\) follows from the analytic inequalities and equality conditions above, not from finite enumeration.

## Relationship to prior work
Wei, Ericsson, Goldbart, and Munro introduced this permutation-invariant Dicke-mixture family and in 2004 gave a phase-averaged separable candidate together with a conjectural relative-entropy formula supported numerically. Wei's 2008 theorem subsequently proved the relative-entropy formula for the broader symmetric family and constructed a closest separable state by the same phase-twirling mechanism. Those results establish the optimum value and existence of an optimizer; they do not supply the uniqueness statement or the minimum finite product length proved here.

A broader uniqueness theorem of Friedland and Gour proves uniqueness of the closest separable state when the entangled density operator is full rank. That hypothesis does not apply here: \(\rho_{n,s}\) has rank two while the ambient Hilbert space has dimension \(2^n\). Their treatment also notes that uniqueness can fail for semipositive states, so the rank-deficient case requires additional structure rather than following from the full-rank theorem.

The new ingredient is the equality classification for the supporting operator \(A\). It confines every closest separable decomposition to one common-modulus phase orbit. Equality in logarithmic Jensen then annihilates the first \(n\) Fourier moments, which simultaneously proves uniqueness of the density operator and identifies an optimal \((n+1)\)-point quadrature.

## Limitations
The theorem concerns only the interior one-zero Dicke edge \(0<s<1\). It does not claim uniqueness at either endpoint, nor does it classify closest separable states for arbitrary mixtures involving more than the two Dicke levels \(k=0\) and \(k=1\).

The roots-of-unity construction proves the minimum number of pure product states needed to decompose this particular closest separable state. It does not assert uniqueness of the minimizing ensemble itself; many probability measures or finite phase sets can share the required first \(n\) vanishing Fourier moments.

## References
1. T.-C. Wei, M. Ericsson, P. M. Goldbart, W. J. Munro, “Connections between relative entropy of entanglement and geometric measure of entanglement,” *Quantum Information and Computation* 4 (2004), arXiv:quant-ph/0405002v1, DOI: 10.26421/QIC4.4-2.
2. T.-C. Wei, “Relative entropy of entanglement for multipartite mixed states: Permutation-invariant states and Dür states,” *Physical Review A* 78 (2008), 012327, arXiv:0805.1090v1, DOI: 10.1103/PhysRevA.78.012327.
3. S. Friedland, G. Gour, “Closed formula for the relative entropy of entanglement in all dimensions,” *Physical Review Letters* 106 (2011), 130401, arXiv:1007.4544v1.

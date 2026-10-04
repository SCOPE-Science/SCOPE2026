# Explicit Moreau–Yosida exactness interval for every pure two-qubit state

## Finding
For every pure two-qubit state \(\rho=|\psi\rangle\langle\psi|\), Shirokov's trace-norm Moreau–Yosida approximation \(E_F^\lambda\) equals \(E_F\) on an explicit nonzero interval. For concurrence \(c\in(0,1]\), define
\[
f(c)=h\!\left(\frac{1+\sqrt{1-c^2}}2\right),\qquad
\lambda_*(c)=\frac1{2f'(c)},
\]
where \(h(x)=-x\log x-(1-x)\log(1-x)\) uses natural logarithms. Then
\[
E_F^\lambda(\rho)=E_F(\rho)\quad\text{for }0<\lambda\le\lambda_*(c).
\]
For \(0<c<1\),
\[
\lambda_*(c)=\frac{\sqrt{1-c^2}}{c\log\!\left(\frac{1+\sqrt{1-c^2}}{1-\sqrt{1-c^2}}\right)},
\]
and \(\lambda_*(1)=1/2\). Product pure states are exact for every \(\lambda>0\).

## Assumptions and scope
The Hilbert space is \(\mathbb C^2\otimes\mathbb C^2\), and entropy is measured with natural logarithms as in arXiv:2609.30246v2. Standard negativity is \(N(\sigma)=(\|\sigma^{T_B}\|_1-1)/2\). The interval is sufficient; maximality is not claimed.

## Proof
By local unitaries write \(|\psi\rangle=a|00\rangle+b|11\rangle\), with \(a,b>0\), \(a^2+b^2=1\), and \(c=2ab\). Let \(F\) be the swap and \(W=|\Phi^+\rangle\langle\Phi^+|-I/2\). The eigenvalues of \(\rho^{T_B}\) are \(a^2,b^2,ab,-ab\), so \(\operatorname{sign}(\rho^{T_B})=F\). The trace-norm supporting inequality at \(\rho^{T_B}\), together with \(F^{T_B}=2|\Phi^+\rangle\langle\Phi^+|\), gives
\[
N(\sigma)\ge\operatorname{Tr}(W\sigma)
\]
for every two-qubit state \(\sigma\), with equality \(N(\rho)=\operatorname{Tr}(W\rho)=c/2\).

For pure two-qubit states \(2N=C\). Since negativity is convex and concurrence is the convex roof of pure-state concurrence,
\[
2N(\sigma)\le C(\sigma)
\]
for every mixed two-qubit state. Wootters' formula in natural-log normalization is \(E_F(\sigma)=f(C(\sigma))\).

The function \(f\) is increasing and convex. With \(r=\sqrt{1-c^2}\),
\[
f'(c)=\frac{c}{2r}\log\!\left(\frac{1+r}{1-r}\right),\qquad
f''(c)=\frac{\log((1+r)/(1-r))-2r}{2r^3}>0,
\]
because \(\operatorname{artanh}(r)>r\); also \(f'(1)=1\). Therefore
\[
\begin{aligned}
E_F(\sigma)&=f(C(\sigma))\ge f(2N(\sigma))\\
&\ge f(c)+f'(c)(2N(\sigma)-c)\\
&\ge f(c)+2f'(c)\left(\operatorname{Tr}(W\sigma)-\frac c2\right)
=\operatorname{Tr}(\Lambda\sigma),
\end{aligned}
\]
where
\[
\Lambda=2f'(c)W+(f(c)-cf'(c))I.
\]
Equality holds at \(\rho\). Undoing the Schmidt local unitaries gives \(\Lambda_\psi\).

The spectrum of \(W_\psi\) is \(\{1/2,-1/2,-1/2,-1/2\}\), so \(D(\Lambda_\psi)=2f'(c)\). Shirokov's variational characterization of \(E_F^\lambda\) permits global supporting operators with spectral diameter at most \(1/\lambda\). Thus \(\Lambda_\psi\) certifies equality whenever \(2f'(c)\le1/\lambda\), proving the interval. For \(c=0\), separability gives \(E_F^\lambda=E_F=0\) for every \(\lambda>0\).

## Verification
The proof is analytic. Critical checks were independently reconstructed: the partial-transpose spectrum and sign, the trace-norm subgradient, \(2N\le C\) from convexity/convex roof, the derivatives of \(f\), and the exact spectral diameter. Supplementary random-state tests at reference concurrences \(0.05,0.2,0.5,0.8,0.99,1\) found no violation of either \(2N\le C\) or the displayed supporting inequality; these computations are not used as proof.

## Relationship to prior work
arXiv:2609.30246v2 defines \(E_F^\lambda\), proves its spectral-diameter variational characterization and exactness criterion, and treats maximally entangled pure states, giving the two-qubit endpoint \(\lambda\le1/2\). The current paper states that a positive exactness interval had not been established there for all pure two-qubit states.

arXiv:2609.31097v1 gives a complete qualitative criterion for existence of global supporting affine functionals for two-qubit \(E_F\). Its theorem implies existence for every entangled rank-one state, but full-text inspection found neither the explicit negativity-based support above nor a closed-form Moreau–Yosida interval. The present result is therefore a quantitative strengthening rather than a new qualitative existence theorem.

Wootters supplies the exact two-qubit formula \(E_F=f(C)\). The known negativity-versus-concurrence comparison is consistent with the inequality used here; the proof above derives the required normalization directly.

## Limitations
The result is restricted to pure two-qubit reference states and the trace-norm Moreau–Yosida approximation of arXiv:2609.30246v2. The threshold is certified sufficient and may be nonoptimal. No selective-LOCC claim is made.

## References
1. M. E. Shirokov, *The Moreau-Yosida approximation of the Entanglement of Formation: basic properties and accuracy estimates*, arXiv:2609.30246v2 (earliest public posting 2026-09-24).
2. Wei Song and Xiao-Lan Zong, *Supporting functionals and singular boundary geometry of two-qubit entanglement of formation*, arXiv:2609.31097v1.
3. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, arXiv:quant-ph/9709029.
4. F. Verstraete, K. Audenaert, J. Dehaene, and B. De Moor, *A comparison of the entanglement measures negativity and concurrence*, arXiv:quant-ph/0108021.

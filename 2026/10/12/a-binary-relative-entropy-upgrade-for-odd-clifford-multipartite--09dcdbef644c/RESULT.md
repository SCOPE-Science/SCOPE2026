# A binary-relative-entropy upgrade for odd Clifford multipartite witnesses
## Finding
Let \(n\ge3\) be odd and \(m\ge2\). At each site \(r\), let
\[
\Gamma^{(r)}_1,\ldots,\Gamma^{(r)}_m
\]
be pairwise anticommuting Hermitian unitaries, and define
\[
B=\sum_{i=1}^m\Gamma^{(1)}_i\otimes\cdots\otimes\Gamma^{(n)}_i.
\]
Then
\[
B^2=mI,\qquad \|B\|=\sqrt m,
\]
and the exact product-state threshold is
\[
\sup_{\sigma\ {\rm product}}|\operatorname{Tr}(\sigma B)|=1.
\]

For any state \(\rho\), put
\[
b=\operatorname{Tr}(\rho B).
\]
If \(b>1\), its total correlation
\[
I_{\mathrm{tot}}(\rho)=D\!\left(\rho\middle\|\rho_1\otimes\cdots\otimes\rho_n\right)
\]
obeys
\[
I_{\mathrm{tot}}(\rho)\ge
d_{\mathrm{bin}}\!\left(
\frac{1+b/\sqrt m}{2}
\middle\|
\frac{1+1/\sqrt m}{2}
\right),
\]
where
\[
d_{\mathrm{bin}}(p\|q)=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
\]
This is strictly larger than
\[
\frac{(b-1)^2}{2m}
\]
for \(b>1\), so it strictly improves the quadratic Pinsker specialization of the source's total-correlation witness bound.

For
\[
B=X^{\otimes n}+Y^{\otimes n}+Z^{\otimes n},
\qquad n\ge3\ {\rm odd},
\]
the largest possible witness value is \(b=\sqrt3\). At that endpoint the new certificate is
\[
I_{\mathrm{tot}}(\rho)\ge
\log\frac{2\sqrt3}{\sqrt3+1}
=
0.237400786151619\ldots,
\]
whereas the source's quadratic odd-party bound gives
\[
\frac{(\sqrt3-1)^2}{6}
=
0.089316397477041\ldots.
\]

## Assumptions and scope
All systems are finite dimensional and logarithms are natural. The local observables are Hermitian unitaries that pairwise anticommute at each site, and the party number is odd. Different sites need not use identical representations.

The result is a lower bound on total correlation from one witness expectation. It is not claimed to be the exact minimum total correlation at fixed \(b\), and no equality classification is asserted. Even party number is outside the claim because the corresponding global tensor terms commute rather than anticommute.

## Proof
Fix a site and a state \(\sigma\), and write
\[
x_i=\operatorname{Tr}(\sigma\Gamma_i).
\]
Anticommutation and \(\Gamma_i^2=I\) imply
\[
\left(\sum_i x_i\Gamma_i\right)^2
=
\left(\sum_i x_i^2\right)I.
\]
Hence the operator norm of the sum is \(\|x\|_2\). Its expectation in \(\sigma\) is \(\|x\|_2^2\), so
\[
\|x\|_2^2\le\|x\|_2
\]
and therefore \(\|x\|_2\le1\).

For a product state, generalized Hölder gives
\[
\left|\sum_i\prod_{r=1}^n x_i^{(r)}\right|
\le
\prod_{r=1}^n\|x^{(r)}\|_n
\le
\prod_{r=1}^n\|x^{(r)}\|_2
\le1.
\]
Thus the product threshold is at most \(1\). It is attained by choosing, at every site, a \(+1\) eigenstate of \(\Gamma^{(r)}_1\). Anticommutation makes the expectation of every other generator vanish in that state, so the product expectation of \(B\) equals \(1\).

Now set
\[
U_i=\Gamma^{(1)}_i\otimes\cdots\otimes\Gamma^{(n)}_i.
\]
For \(i\ne j\), moving \(U_i\) past \(U_j\) contributes one minus sign per site. Since \(n\) is odd,
\[
U_iU_j=-U_jU_i.
\]
Also \(U_i^2=I\). Therefore
\[
B^2=\sum_iU_i^2+\sum_{i<j}(U_iU_j+U_jU_i)=mI.
\]
Consequently
\[
W=\frac{B}{\sqrt m}
\]
is a Hermitian unitary. Its spectral measurement has projectors
\[
P_\pm=\frac{I\pm W}{2}.
\]

Let
\[
\sigma_*=\rho_1\otimes\cdots\otimes\rho_n.
\]
On \(\rho\), the positive-outcome probability is
\[
p=\frac{1+b/\sqrt m}{2}.
\]
On \(\sigma_*\), it is
\[
q=\frac{1+\operatorname{Tr}(\sigma_*B)/\sqrt m}{2}
\le
q_0:=\frac{1+1/\sqrt m}{2},
\]
because \(\sigma_*\) is a product state. Since \(b>1\), one has \(p>q_0\ge q\).

Data processing under this binary measurement gives
\[
I_{\mathrm{tot}}(\rho)
=
D(\rho\|\sigma_*)
\ge d_{\mathrm{bin}}(p\|q).
\]
For fixed \(p\),
\[
\frac{\partial}{\partial q}d_{\mathrm{bin}}(p\|q)
=
\frac{q-p}{q(1-q)}.
\]
Thus the binary divergence decreases as \(q\) increases throughout \(q<p\), and hence
\[
d_{\mathrm{bin}}(p\|q)\ge d_{\mathrm{bin}}(p\|q_0).
\]
This proves the displayed bound.

Finally,
\[
p-q_0=\frac{b-1}{2\sqrt m}.
\]
Binary Pinsker yields
\[
d_{\mathrm{bin}}(p\|q_0)\ge2(p-q_0)^2
=
\frac{(b-1)^2}{2m},
\]
with strict inequality for the distinct interior Bernoulli laws occurring when \(b>1\).

## Verification
The argument is analytic for every admissible finite dimension, every odd \(n\ge3\), every \(m\ge2\), and every state with \(b>1\). No finite experiment establishes any universal quantifier.

The bundled checker verifies the scalar comparison, the \(m=3\) endpoint values, and \(B^2=3I\) for the three-qubit Pauli instance. Those checks are corroborative only.

## Relationship to prior work
Tian's *Multipartite parity bounds and total correlation* proves a general parity-defect estimate and then uses quantum Pinsker to obtain a quadratic total-correlation lower bound. Its Pauli example gives, for odd party number,
\[
I_{\mathrm{tot}}(\rho)\ge
\frac16\left(\operatorname{Tr}(\rho B)-1\right)_+^2
\]
for
\[
B=X^{\otimes n}+Y^{\otimes n}+Z^{\otimes n}.
\]
The same paper identifies Clifford-type local geometry as a natural direction for sharper intrinsic local constants.

Wehner and Winter established the local Bloch-ball geometry of mutually anticommuting Clifford observables, including the squared-expectation constraint used above. Their result does not state the multipartite product threshold, the odd-tensor binary spectral collapse, or a total-correlation lower bound.

A previously published source-specific result for the same anchor optimized only the trace-norm/Pinsker mechanism over real weights in the three-Pauli family, obtaining a Euclidean-distance-to-\(\ell_1\)-ball certificate. That statement neither uses binary relative entropy nor treats arbitrary \(m\) anticommuting generators. The present theorem is therefore not a restatement of that earlier optimization.

## Limitations
The theorem is restricted to odd numbers of sites and pairwise anticommuting Hermitian unitaries. It is a lower bound rather than an exact fixed-expectation total-correlation optimum. The even-party case requires a different spectral analysis. No claim is made about entanglement, nonlocality, or device-independent certification.

## References
1. J. Tian, *Multipartite parity bounds and total correlation*, arXiv:2603.01105v1 (first public 2026-03-01), primary MSC 81P40.
2. S. Wehner and A. Winter, *Higher entropic uncertainty relations for anti-commuting observables*, Journal of Mathematical Physics 49, 062105 (2008), DOI 10.1063/1.2943685; arXiv:0710.1185.

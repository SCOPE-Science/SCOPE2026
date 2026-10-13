# Joint-fault distance of implicit \(\operatorname{collapse}(n)\) checks
## Finding
Consider one \(n\)-qubit repetition-code patch in the implicit-check version of \(\operatorname{collapse}(n)\). Let
\[
L=X_1X_2\cdots X_n,
\qquad
S_j=Z_jZ_{j+1}
\quad(1\le j<n).
\]
The source construction measures \(L\) on the root and \(LS_j\) on the \(j\)-th check output. In the ideal stabilizer sector \(S_j=+1\), all \(n\) ideal measurement signs therefore agree.

Let
\[
x=(x_1,\ldots,x_n)\in\mathbb F_2^n
\]
describe Pauli-\(X\) faults present on the patch immediately before the implicit-check measurement gadget, and let
\[
e=(e_0,e_1,\ldots,e_{n-1})\in\mathbb F_2^n
\]
describe classical sign flips of the root and check readouts. Then implicit postselection accepts exactly when
\[
\boxed{
e_j\oplus e_0=x_j\oplus x_{j+1}
\quad(1\le j<n).
}
\]

This single equation gives three distinct distances.

First, with \(x=0\), the only accepted readout patterns are
\[
e=0^n
\quad\text{and}\quad
e=1^n.
\]
Thus every nonzero pure readout pattern of weight below \(n\) is detected. This supplies a general-\(n\) proof of the source's statement that implicit checks eliminate collapse readout errors through order \(n-1\).

Second, with \(e=0\), the only accepted Pauli-\(X\) patterns are
\[
x=0^n
\quad\text{and}\quad
x=1^n.
\]
Thus pure patch bit-flip faults also have detection distance \(n\).

Third, when the two fault types are allowed simultaneously, the accepted-fault code has minimum nonzero total Hamming weight
\[
\boxed{2}.
\]
For example, an \(X\) fault on the first patch qubit produces only the first stabilizer-domain wall, and one flipped first-check readout masks that domain wall.

The more operational quantity is the minimum accepted fault weight that flips the inferred root sign. Such an error has \(e_0=1\). Its exact minimum is
\[
\boxed{
d_{\mathrm{sign}}(n)=\left\lfloor\frac n2\right\rfloor+1.
}
\]
An alternating patch fault pattern attains the bound together with one root-readout flip. Thus pure readout noise has order-\(n\) suppression, but joint patch-\(X\) and readout noise can produce an accepted wrong inferred sign at order only \(\lfloor n/2\rfloor+1\).

There is also an exact stochastic law. Suppose the \(x_i\) are independent Bernoulli-\(q\) faults and all readout flips are independent Bernoulli-\(p\). Define
\[
G_n(r;q)
=
(1-q,q)
\begin{pmatrix}
1-q & qr\\
(1-q)r & q
\end{pmatrix}^{n-1}
\binom11.
\]
For \(0<p<1\), the accepted probabilities with unflipped and flipped inferred root sign are
\[
\boxed{
A_0=(1-p)^n
G_n\!\left(\frac p{1-p};q\right),
}
\]
and
\[
\boxed{
A_1=p^n
G_n\!\left(\frac{1-p}{p};q\right).
}
\]
Hence
\[
A_{\mathrm{acc}}=A_0+A_1,
\qquad
P_{\mathrm{sign}\mid\mathrm{acc}}
=
\frac{A_1}{A_0+A_1}.
\]
The endpoint cases \(p=0\) and \(p=1\) are obtained directly from the finite sums.

For readout noise alone, \(q=0\), these formulas reduce to
\[
A_{\mathrm{acc}}=(1-p)^n+p^n,
\qquad
P_{\mathrm{sign}\mid\mathrm{acc}}
=
\frac{p^n}{(1-p)^n+p^n}.
\]
For equal small fault rates \(p=q=\eta\),
\[
P_{\mathrm{sign}\mid\mathrm{acc}}
=
\Theta\!\left(
\eta^{\lfloor n/2\rfloor+1}
\right).
\]
Thus simultaneous state and readout faults change the leading accepted-sign exponent even though each fault family separately has distance \(n\).

If \(M\) independent patches are postselected and the final correction uses the parity of their root signs, then
\[
P_{\mathrm{all\,acc}}=A_{\mathrm{acc}}^M
\]
and, conditioned on acceptance,
\[
P_{\mathrm{parity}}
=
\frac{1-(1-2P_{\mathrm{sign}\mid\mathrm{acc}})^M}{2}.
\]

## Assumptions and scope
The deterministic classification assumes the ideal pre-fault patch lies in the repetition-code stabilizer sector
\[
S_j=+1.
\]
The only quantum faults modeled are Pauli-\(X\) errors present immediately before the source's implicit-check measurement gadget. Readout faults are modeled as classical flips of the reported eigenvalue signs. The exact distance statements do not require probabilistic independence.

The probability formulas additionally assume independent and identically distributed patch-\(X\) faults with probability \(q\) and independent and identically distributed readout flips with probability \(p\). The multi-patch parity formula assumes independent patches.

This is a syndrome-detection and inferred-sign theorem. It does not model dephasing, leakage, coherent faults, correlated hardware noise, faults occurring inside the implementation of the check gadget, or target-register damage caused by earlier distributed-control faults. An accepted patch-\(X\) pattern need not by itself imply a final computational error; the theorem identifies when the postselection information can or cannot distinguish the modeled faults and when the inferred logical-\(X\) sign is wrong.

## Proof
Let the ideal root outcome be the sign
\[
\ell\in\{+1,-1\}.
\]
Because the ideal state satisfies \(S_j=+1\), the ideal \(LS_j\) check outcome is also \(\ell\).

Now apply the Pauli-\(X\) pattern \(x\). The logical operator \(L\) commutes with every physical \(X_i\), so its ideal measurement sign remains \(\ell\). The stabilizer \(S_j=Z_jZ_{j+1}\) anticommutes with exactly one of \(X_j,X_{j+1}\) when
\[
x_j\oplus x_{j+1}=1.
\]
Thus the true \(j\)-th check sign becomes
\[
\ell\,(-1)^{x_j\oplus x_{j+1}}.
\]

A readout flip \(e_0\) changes the reported root sign to
\[
\ell\,(-1)^{e_0},
\]
while \(e_j\) changes the reported \(j\)-th check sign to
\[
\ell\,(-1)^{x_j\oplus x_{j+1}\oplus e_j}.
\]
Implicit postselection accepts exactly when every reported check agrees with the reported root. Cancelling \(\ell\) gives
\[
e_j\oplus e_0=x_j\oplus x_{j+1}
\]
for every \(j\).

The pure-noise statements follow immediately. If \(x=0\), then every \(e_j=e_0\), so \(e\) is either \(0^n\) or \(1^n\). If \(e=0\), then
\[
x_j=x_{j+1}
\]
for all \(j\), so \(x\) is either \(0^n\) or \(1^n\).

For the joint detector distance, take
\[
x=(1,0,\ldots,0),
\qquad
e=(0,1,0,\ldots,0).
\]
This nonzero accepted pair has total weight \(2\), while no total-weight-one pair can satisfy all acceptance equations. Hence the joint distance is exactly \(2\).

For an accepted wrong inferred root sign, one has \(e_0=1\). Let
\[
k=|x|,
\qquad
t=\left|\{j:x_j\ne x_{j+1}\}\right|.
\]
The acceptance equations force exactly \(n-1-t\) of the check-readout bits to equal \(1\), so the total fault weight is
\[
w=k+n-t.
\]
Every \(1\) in the binary string \(x\) is incident to at most two transitions, hence
\[
t\le2k.
\]
Also \(t\le n-1\). Therefore
\[
t-k
\le
\min\{k,n-1-k\}
\le
\left\lfloor\frac{n-1}{2}\right\rfloor,
\]
and so
\[
w
=
n-(t-k)
\ge
n-\left\lfloor\frac{n-1}{2}\right\rfloor
=
\left\lfloor\frac n2\right\rfloor+1.
\]
Equality is attained by the alternating string
\[
x=0101\cdots
\]
together with \(e_0=1\) and the check-readout bits fixed by the acceptance equations. This proves the exact sign distance.

For the stochastic law, let
\[
T(x)=\left|\{j:x_j\ne x_{j+1}\}\right|.
\]
Conditional on \(x\), acceptance with \(e_0=0\) requires \(T(x)\) flipped check readouts, while acceptance with \(e_0=1\) requires \(n-1-T(x)\) flipped check readouts. Therefore
\[
A_0
=
(1-p)^n
\mathbb E_q
\left[
\left(\frac p{1-p}\right)^{T(x)}
\right]
\]
and
\[
A_1
=
p^n
\mathbb E_q
\left[
\left(\frac{1-p}{p}\right)^{T(x)}
\right].
\]

The transition-count generating function is computed by a two-state transfer matrix. If the previous bit is \(a\) and the next bit is \(b\), the factor is
\[
\Pr(x_{j+1}=b)\,r^{a\oplus b}.
\]
Hence
\[
\mathbb E_q[r^{T(x)}]
=
(1-q,q)
\begin{pmatrix}
1-q & qr\\
(1-q)r & q
\end{pmatrix}^{n-1}
\binom11
=
G_n(r;q),
\]
which proves the displayed formulas.

Finally, when \(p=q=\eta\), every accepted wrong-sign event has total fault weight at least
\[
\left\lfloor\frac n2\right\rfloor+1,
\]
and an event of exactly that weight exists. All event probabilities are nonnegative, so the conditional error has precisely the stated leading-order exponent as \(\eta\to0\).

## Verification
The proof is exact and finite-dimensional. No exhaustive finite enumeration is used to establish the all-\(n\) claims.

The bundled checker independently enumerates all patch and readout patterns for
\[
2\le n\le10
\]
and confirms the acceptance equations, the pure-fault distance \(n\), the joint detector distance \(2\), and the wrong-sign distance
\[
\left\lfloor\frac n2\right\rfloor+1.
\]
It also compares the transfer-matrix probabilities with direct exact rational enumeration for several \(n,p,q\), and verifies the multi-patch parity formula. These computations are corroborative only.

## Relationship to prior work
Smith, Pokharel, Maurya, and Takita introduce the \(\operatorname{distribute}\)--\(\operatorname{collapse}(n)\) framework and explain that an \(n\)-qubit patch can be viewed as a repetition code with logical
\[
L=X_1\cdots X_n
\]
and stabilizers
\[
S_j=Z_jZ_{j+1}.
\]
Their implicit-check gadget measures \(L\) on the root and products \(LS_j\) on the check outputs. They explicitly state that implicit checks detect collapse readout errors through order \(n-1\), but illustrate the readout mechanism with \(n=2\). The deterministic pure-readout portion of the present theorem supplies the general proof of that statement.

The new part is the joint-fault boundary. The source discusses gate-induced bit flips and readout errors as two detectable fault mechanisms, but does not classify their simultaneous masking patterns, give the exact accepted-fault kernel, identify the distance-two mixed detector, derive the exact wrong-sign distance
\[
\left\lfloor\frac n2\right\rfloor+1,
\]
or give the transfer-matrix acceptance and conditional-error laws.

General single-shot error-correction literature explains why simultaneous data and syndrome-measurement faults require special redundancy or repeated information. Bombín's single-shot framework and later data-syndrome-code work provide that broader context. They do not analyze the particular implicit logical-\(X\) measurements of \(\operatorname{collapse}(n)\) or imply the source-specific distances and stochastic formulas above without reconstructing this measurement map.

A public technical review of arXiv:2609.08925 independently notes that the source illustrates the general-\(n\) readout claim with a two-qubit example rather than a full proof. That review does not contain the mixed-fault classification or the formulas proved here.

## Limitations
The joint-fault distance is a property of the stated effective premeasurement \(X\)-fault plus classical-readout model. It is not a circuit-level fault distance for every physical implementation of \(V_n\). Fault propagation through the controlled operation, coherent errors, leakage, dephasing, and correlated readout can change the operational failure law.

The exact transfer formula assumes independent faults. The deterministic kernel equation remains valid without that independence assumption, but a correlated noise law must be evaluated directly on the kernel.

The theorem concerns error detection and the inferred logical-\(X\) sign. It does not assert that every accepted nonzero \(x\) causes a logical error on the target computation.

## References
1. K. C. Smith, B. Pokharel, S. Maurya, and M. Takita, *Resilience Beyond the Light Cone: Error-Detected Primitives for Practical Dynamic Circuits*, arXiv:2609.08925v1 (first public 2026-09-08).
2. H. Bombín, *Single-Shot Fault-Tolerant Quantum Error Correction*, Physical Review X 5, 031043 (2015), DOI 10.1103/PhysRevX.5.031043.
3. K.-Y. Kuo and C.-Y. Lai, *Generalized quantum data-syndrome codes and belief propagation decoding for phenomenological noise*, arXiv:2310.12682.

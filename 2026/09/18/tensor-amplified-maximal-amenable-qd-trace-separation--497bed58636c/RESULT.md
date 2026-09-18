# Tensor amplification yields maximal amenable–quasidiagonal trace separation

## Result

Let \(A\) be a unital \(C^*\)-algebra and let \(e_0,e_1\in A\) be complementary projections. Assume

1. every quasidiagonal tracial state \(\rho\in T_{\mathrm{qd}}(A)\) satisfies
   \[
   \rho(e_0)=\rho(e_1)=\frac12;
   \]
2. there are tracial states \(\mu_0,\mu_1\in T(A)\) with
   \[
   \mu_i(e_j)=\delta_{ij},
   \qquad
   \lambda:=\frac12(\mu_0+\mu_1)\in T_{\mathrm{qd}}(A).
   \]

For \(r\ge 1\), put \(A_r=A^{\otimes_{\min} r}\). For
\(\omega=(\omega_1,\ldots,\omega_r)\in\{0,1\}^r\), define
\[
E_\omega=e_{\omega_1}\otimes\cdots\otimes e_{\omega_r},
\qquad
\mu_\omega=\mu_{\omega_1}\otimes\cdots\otimes\mu_{\omega_r}.
\]
Then:

\[
\boxed{\rho(E_\omega)=2^{-r}\quad
       \text{for every }\rho\in T_{\mathrm{qd}}(A_r)}
\]
and
\[
\boxed{
\operatorname{dist}_{A_r^*}\!\bigl(\mu_\omega,T_{\mathrm{qd}}(A_r)\bigr)
=2(1-2^{-r}).
}
\]

Each \(\mu_\omega\) is amenable. Thus a two-sector obstruction to quasidiagonality tensor-amplifies to traces whose norm distance from the quasidiagonal trace set approaches the maximal possible value \(2\).

There is also an exact infinite-tensor conclusion. Let
\[
A_\infty=\varinjlim\bigl(A_r,\ x\mapsto x\otimes1\bigr)
\]
be the spatial infinite tensor power and let
\(\mu_0^{\otimes\infty}\) be the product trace. Then
\[
\boxed{
\operatorname{dist}_{A_\infty^*}
\!\bigl(\mu_0^{\otimes\infty},T_{\mathrm{qd}}(A_\infty)\bigr)=2.
}
\]
Moreover \(\mu_0^{\otimes\infty}\) is amenable, while
\(\lambda^{\otimes\infty}\) is quasidiagonal, so the quasidiagonal trace set of
\(A_\infty\) is nonempty.

## Key permanence lemma

The mechanism is a compression fact for tensor-factor projections.

**Lemma.** Let \(B,C\) be unital \(C^*\)-algebras, let
\(\tau\in T_{\mathrm{qd}}(B\otimes_{\min}C)\), and let \(q\in C\) be a projection
with \(\tau(1\otimes q)>0\). Then
\[
\tau_q(b)=\frac{\tau(b\otimes q)}{\tau(1\otimes q)}
\]
is a quasidiagonal tracial state on \(B\).

**Proof.**
Choose u.c.p. maps
\(\phi_n:B\otimes_{\min}C\to M_{k(n)}\) witnessing quasidiagonality of \(\tau\).
Set
\[
h_n=\phi_n(1\otimes q).
\]
Since \(q^2=q\),
\[
\|h_n^2-h_n\|\longrightarrow0.
\]
For large \(n\), put
\[
Q_n=\mathbf1_{[1/2,1]}(h_n).
\]
The approximate-projection relation gives
\[
\|Q_n-h_n\|\longrightarrow0.
\]
For fixed \(b\in B\), write \(x_n(b)=\phi_n(b\otimes1)\). Because
\(b\otimes1\) commutes with \(1\otimes q\) and \(\phi_n\) is asymptotically
multiplicative,
\[
\|[x_n(b),h_n]\|\longrightarrow0,
\]
hence also
\[
\|[x_n(b),Q_n]\|\longrightarrow0.
\]
Let \(r_n=\operatorname{rank}Q_n\). Since
\[
\frac{r_n}{k(n)}\longrightarrow\tau(1\otimes q)>0,
\]
the maps
\[
\psi_n(b)=Q_nx_n(b)Q_n\in Q_nM_{k(n)}Q_n\cong M_{r_n}
\]
are eventually well-defined unital completely positive maps. Their
multiplicativity defects tend to zero because
\[
\psi_n(bc)-\psi_n(b)\psi_n(c)
\]
is the sum of a compressed multiplicativity defect of \(\phi_n\) and an
off-diagonal term controlled by \([Q_n,x_n(b)]\).

For the traces,
\[
\frac1{k(n)}\operatorname{Tr}(Q_nx_n(b))
   \longrightarrow \tau(b\otimes q),
\qquad
\frac{r_n}{k(n)}\longrightarrow\tau(1\otimes q).
\]
Dividing the two limits gives
\[
\operatorname{tr}_{r_n}(\psi_n(b))\longrightarrow\tau_q(b).
\]
Thus \(\tau_q\) is quasidiagonal. \(\square\)

## Uniform sector masses in tensor powers

Fix \(\rho\in T_{\mathrm{qd}}(A_r)\). Hold all tensor coordinates except one
fixed and compress by the corresponding word projection in the other
coordinates. If that projection has positive \(\rho\)-mass, the lemma produces a
quasidiagonal trace on the remaining copy of \(A\); the hypothesis on \(A\)
forces the two conditional sector masses to be equal. If the conditioning
projection has zero mass, both refinements have zero mass.

Consequently two words differing in one bit have equal \(\rho\)-mass. The
hypercube \(\{0,1\}^r\) is connected, while the \(E_\omega\) are mutually
orthogonal and sum to \(1\). Hence
\[
\rho(E_\omega)=2^{-r}.
\]

## Exact norm distance

Tensor products of quasidiagonal approximations show that
\[
\lambda_r:=\lambda^{\otimes r}\in T_{\mathrm{qd}}(A_r).
\]
Expanding the tensor product,
\[
\lambda_r=2^{-r}\sum_{\eta\in\{0,1\}^r}\mu_\eta.
\]
For any quasidiagonal \(\rho\), the self-adjoint unitary
\[
u_\omega=2E_\omega-1
\]
gives
\[
\|\mu_\omega-\rho\|
\ge
|(\mu_\omega-\rho)(u_\omega)|
=
2(1-2^{-r}).
\]
This proves the lower bound.

For the reverse inequality, write
\[
\lambda_r
=
2^{-r}\mu_\omega+(1-2^{-r})\theta_\omega,
\]
where \(\theta_\omega\) is the normalized convex combination of the other
\(\mu_\eta\). The states \(\mu_\omega\) and \(\theta_\omega\) are supported on
the complementary projections \(E_\omega\) and \(1-E_\omega\), so
\[
\|\mu_\omega-\theta_\omega\|=2.
\]
Therefore
\[
\|\mu_\omega-\lambda_r\|
=
2(1-2^{-r}),
\]
and \(\lambda_r\) is quasidiagonal. This proves the exact distance formula.

Because quasidiagonal traces are amenable and amenable traces form a face,
the finite convex decomposition of \(\lambda_r\) also shows that every
\(\mu_\omega\) is amenable.

## Infinite tensor power

Amenable traces and quasidiagonal traces are stable under finite tensor products.
For the infinite product state, use the canonical product-state slice map onto a
finite tensor stage. On a prescribed finite set of \(A_\infty\), first approximate
inside \(A_r\), then compose a finite-stage amenable or quasidiagonal approximation
with this slice map. Hence
\[
\mu_0^{\otimes\infty}\in T_{\mathrm{am}}(A_\infty),
\qquad
\lambda^{\otimes\infty}\in T_{\mathrm{qd}}(A_\infty).
\]

Now let \(\rho\in T_{\mathrm{qd}}(A_\infty)\). Its restriction to every unital
finite tensor stage is quasidiagonal. Therefore, for
\[
E_r=e_0^{\otimes r}\otimes1\otimes1\otimes\cdots,
\]
the finite-stage result gives
\[
\rho(E_r)=2^{-r},
\qquad
\mu_0^{\otimes\infty}(E_r)=1.
\]
Testing on \(2E_r-1\) yields
\[
\|\mu_0^{\otimes\infty}-\rho\|
\ge 2(1-2^{-r})
\]
for every \(r\). Letting \(r\to\infty\) gives the lower bound \(2\), and \(2\)
is also the universal upper bound for the distance between states.

## Application to Moradi's 2026 construction

Moradi constructs a separable unital residually finite-dimensional
\(C^*\)-algebra \(A\) with complementary sector projections \(e^0,e^1\).
His Theorem 4.1 proves that every quasidiagonal trace on \(A\) has
\[
\rho(e^0)=\rho(e^1)=\frac12.
\]
His Lemma 3.2 constructs tracial states \(\mu_0,\mu_1\) satisfying
\[
\mu_i(e^j)=\delta_{ij},
\qquad
\tau_\infty=\frac12(\mu_0+\mu_1).
\]
The trace \(\tau_\infty\) is a weak-star limit of normalized traces of
finite-dimensional coordinate representations; quasidiagonal traces are
weak-star closed, so \(\tau_\infty\) is quasidiagonal.

Hence Moradi's algebra satisfies the hypotheses above. For every \(r\),
\[
\operatorname{dist}
\bigl(\mu_0^{\otimes r},T_{\mathrm{qd}}(A^{\otimes_{\min}r})\bigr)
=
2(1-2^{-r}).
\]
Finite minimal tensor powers of an RFD algebra are RFD: tensor a separating
family of finite-dimensional representations and take their direct sum.
Thus the finite-stage examples remain separable, unital and RFD.

In particular, for every \(\varepsilon>0\) there is a separable unital RFD
\(C^*\)-algebra carrying an amenable trace whose norm distance from every
quasidiagonal trace is greater than \(2-\varepsilon\). The infinite tensor
power reaches distance exactly \(2\).

This is stronger than merely exhibiting a non-quasidiagonal component of a
quasidiagonal trace: the defect can be amplified until the bad amenable trace
is asymptotically, and in the infinite tensor power exactly, maximally separated
from the entire quasidiagonal trace set in dual norm.

## Limitations

- The infinite tensor power is not claimed to remain RFD.
- No exactness, nuclearity, UCT, simplicity, or classification property is asserted.
- The compression lemma is a permanence device and is not claimed to be new by itself.
- Originality is claimed only for the tensor-amplified sector theorem and its exact
  norm-distance consequences, to the best of our knowledge.
- The result uses the specific sector-balance theorem available in Moradi's
  construction; it does not say that arbitrary failures of faciality admit the same
  amplification.

## References

1. M. Moradi, *Quasidiagonal traces need not form a face*, arXiv:2609.18793 (2026).
   https://arxiv.org/abs/2609.18793
2. N. P. Brown, *Invariant means and finite representation theory of \(C^*\)-algebras*,
   Memoirs of the AMS 184 (2006), no. 865; arXiv:math/0304009.
   https://arxiv.org/abs/math/0304009

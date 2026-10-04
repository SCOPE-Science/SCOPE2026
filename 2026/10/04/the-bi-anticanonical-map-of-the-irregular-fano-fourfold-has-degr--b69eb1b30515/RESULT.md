# The bi-anticanonical map of the irregular Fano fourfold has degree \(8\)
## Finding
Let \(k=\overline{\mathbf F}_2\), and let \(X\) be the smooth Fano fourfold constructed by Waldron--Witaszek. Their construction starts from the normal integral complete intersection
\[
H=V(Q,C)\subset\mathbf P^6_k
\]
and a finite flat universal homeomorphism
\[
\pi:H\longrightarrow X
\]
of degree \(2\). Let \(A\) denote the ample line bundle called \(K\) in their paper, so that
\[
\pi^*A\simeq\mathcal O_H(1).
\]

Then
\[
A^{\otimes2}\simeq\omega_X^{-2},
\qquad
h^0(X,\omega_X^{-2})=7.
\]
The complete bi-anticanonical system is basepoint-free. Under the above identification, a basis of its pullback to \(H\) is
\[
x_0^2,\ldots,x_5^2,t^2.
\]
Hence the complete bi-anticanonical morphism
\[
\Phi_{|-2K_X|}:X\longrightarrow\mathbf P^6
\]
is finite and purely inseparable of degree \(8\), with image the Frobenius twist
\[
H^{(2)}\subset\mathbf P^6
\]
of the \((2,3)\) complete intersection \(H\).

Waldron--Witaszek also construct an injection
\[
A^{\otimes2}\hookrightarrow\Omega_X^1.
\]
With the identification above this is an injection
\[
\omega_X^{-2}\hookrightarrow\Omega_X^1,
\]
so
\[
h^0(X,\Omega_X^1)\ge7.
\]

## Assumptions and scope
The notation is that of arXiv:2609.29924v1, except that \(A\) is used here for the paper's ample line bundle \(K\), in order not to confuse it with the canonical divisor. The ground field is \(k=\overline{\mathbf F}_2\).

The image \(H^{(2)}\) means the Frobenius twist embedded by the squared homogeneous coordinates. Over the perfect field \(k\) it is abstractly isomorphic to a Frobenius twist of \(H\), but the statement keeps the twist notation because the coefficients of the defining quadric are Frobenius-conjugated.

No claim is made here about the full Hodge diamond, the Picard group, or whether \(h^0(X,\Omega_X^1)=7\) is an equality.

## Proof
Waldron--Witaszek prove
\[
\pi^*\omega_X^{-1}\simeq\mathcal O_H(1)
\qquad\text{and}\qquad
\pi^*A\simeq\mathcal O_H(1).
\]
Therefore the line bundle
\[
L:=A\otimes\omega_X
\]
has trivial pullback to \(H\). Since \(\pi\) is finite flat of degree \(2\), applying the norm gives
\[
L^{\otimes2}\simeq\operatorname{Nm}_{H/X}(\pi^*L)\simeq\mathcal O_X.
\]
Thus
\[
A^{\otimes2}\simeq\omega_X^{-2}.
\]

It remains to compute the complete space of sections. Put
\[
S=k[x_0,\ldots,x_5,t],\qquad R=S/(Q,C),
\]
and let
\[
D=\sum_{i=0}^5x_i^2\frac{\partial}{\partial x_i}.
\]
The source proves
\[
D(Q)=C,\qquad D(C)=0,
\]
and that \(\mathcal O_X\) is the sheaf of \(D\)-invariant functions on \(H\).

Locally on \(X\), Proposition 4.5 identifies a generator of \(\pi^*A\) with \(x_i c\), where \(c\) is a unit. Hence a generator of \(\pi^*A^{\otimes2}\) is \(x_i^2c^2\), which is killed by \(D\) in characteristic \(2\). Conversely, if a local section of \(\mathcal O_H(2)\) is killed by \(D\), dividing by the nowhere-vanishing section \(x_i^2c^2\) gives a degree-zero function killed by the local foliation derivation, hence a function pulled back from \(X\). Therefore
\[
A^{\otimes2}
=
\ker\!\left(
D:\pi_*\mathcal O_H(2)\longrightarrow\pi_*\mathcal O_H(3)
\right).
\]
Taking global sections and using projective normality of the complete intersection gives
\[
H^0(X,A^{\otimes2})
=
\ker(D:R_2\to R_3).
\]

We now compute this kernel exactly. Write
\[
Q=B+\sum_{i=0}^5\theta^{i+1}x_i^2+t^2,
\qquad
B=x_0x_1+x_2x_3+x_4x_5,
\]
so that
\[
C=D(B).
\]
If \(q\in S_2\) represents a class in the kernel, then in \(S_3\)
\[
D(q)=\ell Q+\mu C
\]
for some \(\ell\in S_1\) and \(\mu\in k\). The polynomial \(D(q)\) has no \(t^3\) term and no \(x_it^2\) term. The coefficient of \(t^3\) in \(\ell Q\) is the \(t\)-coefficient of \(\ell\), while the coefficient of \(x_it^2\) is the \(x_i\)-coefficient. Hence \(\ell=0\). It follows that
\[
D(q)=\mu C=D(\mu B),
\]
so
\[
D(q+\mu B)=0
\]
in the polynomial ring \(S\).

The degree-two kernel of \(D:S_2\to S_3\) is exactly
\[
\operatorname{span}_k\{x_0^2,\ldots,x_5^2,t^2\}.
\]
Indeed, every square is killed in characteristic \(2\); each mixed monomial \(x_ix_j\) contributes the unique pair
\[
x_i^2x_j+x_ix_j^2,
\]
and each \(tx_i\) contributes the unique monomial \(tx_i^2\), so no nonzero linear combination of mixed monomials lies in the kernel.

Modulo \(Q\), the element \(B\) is itself a linear combination of the seven squares. Therefore every class in \(\ker(D:R_2\to R_3)\) is represented by a linear combination of
\[
x_0^2,\ldots,x_5^2,t^2.
\]
These seven classes are linearly independent in \(R_2\): a relation among them equal to a scalar multiple of \(Q\) would force that scalar to vanish by comparing the cross terms in \(B\). Thus
\[
h^0(X,A^{\otimes2})=7.
\]

The seven descended sections have no common zero because their pullbacks are the seven coordinate squares on the projective variety \(H\). Hence \(|A^{\otimes2}|=|-2K_X|\) is basepoint-free. Let
\[
g:X\longrightarrow\mathbf P^6
\]
be the resulting morphism. After pullback along \(\pi\), it is
\[
g\circ\pi:
[x_0:\cdots:x_5:t]
\longmapsto
[x_0^2:\cdots:x_5^2:t^2].
\]
This is the relative Frobenius morphism of the embedded fourfold \(H\), whose image is \(H^{(2)}\). Since \(H\) is integral of dimension \(4\), that Frobenius has function-field degree
\[
2^4=16.
\]
The extension \(k(H)/k(X)\) has degree \(2\). Therefore
\[
[k(X):k(H^{(2)})]=\frac{16}{2}=8.
\]
The extension is purely inseparable. Since \(A^{\otimes2}\) is ample and basepoint-free, \(g\) is finite onto its image. Hence \(g\) is a finite purely inseparable morphism of degree \(8\) onto \(H^{(2)}\).

Finally, Proposition 5.1 of the source gives an injective sheaf map
\[
A^{\otimes2}\hookrightarrow\Omega_X^1.
\]
Using \(A^{\otimes2}\simeq\omega_X^{-2}\) and the seven independent global sections just computed gives
\[
h^0(X,\Omega_X^1)\ge7.
\]

## Verification
The accompanying `verify.py` checks the coefficient-independent characteristic-two algebra used in the kernel computation. It enumerates all degree-two monomials in seven variables, constructs the matrix of
\[
D=\sum_{i=0}^5x_i^2\partial_{x_i}
\]
over \(\mathbf F_2\), and verifies that its kernel has dimension \(7\), generated by the seven squares. It also verifies \(D(B)=C\), the \(t^3\) and \(x_it^2\) coefficient test forcing \(\ell=0\), and the degree arithmetic \(2^4/2=8\). The replay output ends in `VERIFY_OK`.

The verifier is only a finite consistency check. The sheaf-kernel identification, norm argument, and function-field degree argument are mathematical proofs and do not depend on extrapolating from a finite computation.

## Relationship to prior work
Waldron--Witaszek construct \(X\), \(H\), \(\pi\), and the ample line bundle \(A\); prove
\[
\pi^*\omega_X^{-1}\simeq\mathcal O_H(1),
\qquad
\pi^*A\simeq\mathcal O_H(1);
\]
compute the degree-one invariant kernel; and construct
\[
A^{\otimes2}\hookrightarrow\Omega_X^1.
\]
The inspected full text does not identify \(A^{\otimes2}\) with \(\omega_X^{-2}\), compute \(h^0(X,A^{\otimes2})\), describe the complete bi-anticanonical map, or state its degree.

A contemporaneous note by Pieter Belmans observes from the same injection that
\[
h^0(X,\Omega_X^1)\ge6
\]
and studies an exceptional rank-two bundle. It does not state the seven-dimensional bi-anticanonical calculation or the degree-\(8\) Frobenius model.

## Limitations
The result gives an exact bi-anticanonical model and a seven-dimensional subspace of global one-forms, but it does not determine whether additional global one-forms exist. It also does not determine the Picard group; in particular the argument only needs
\[
(A\otimes\omega_X)^{\otimes2}\simeq\mathcal O_X
\]
and does not assert \(A\simeq\omega_X^{-1}\).

No exhaustive claim about all unpublished or unindexed discussions of this very recent example is made.

## References
1. J. Waldron and J. Witaszek, *An irregular smooth Fano fourfold in positive characteristic*, arXiv:2609.29924v1, submitted 24 September 2026.
2. P. Belmans, *An exceptional object for the irregular Waldron--Witaszek Fano fourfold*, 25 September 2026.

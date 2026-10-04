# Exact compactness threshold for intermediate Morrey derivatives on compact-resolvent Hilbert scales
## Finding
Let \(H\) be an infinite-dimensional complex Hilbert space, and let \(B\ge I\) be a positive self-adjoint operator with compact resolvent. Fix \(T>0\), \(m\ge2\), \(0<j<m\), \(1<p<\infty\), and \(0\le\lambda<1\). Define
\[
\mathbb D_M^{m,p,\lambda}(0,T;D(B),H)
=
\{u\in\mathcal M^{p,\lambda}(0,T;D(B)):D_t^m u\in\mathcal M^{p,\lambda}(0,T;H)\}.
\]
For every \(0\le\alpha\le1\), the map
\[
D_t^j:\mathbb D_M^{m,p,\lambda}(0,T;D(B),H)
\longrightarrow
\mathcal M^{p,\lambda}(0,T;D(B^\alpha))
\]
has the exact trichotomy
\[
\begin{cases}
\text{compact},&0\le\alpha<1-j/m,\\
\text{bounded but noncompact},&\alpha=1-j/m,\\
\text{unbounded},&1-j/m<\alpha\le1.
\end{cases}
\]
Thus the fractional-domain exponent \(1-j/m\) is not only the sharp boundedness exponent: for every infinite-dimensional compact-resolvent Hilbert scale it is also the exact boundary between same-Morrey compactness and noncompactness.

## Assumptions and scope
For a Banach space \(X\), the time-Morrey norm is
\[
\|f\|_{\mathcal M^{p,\lambda}(0,T;X)}
=
\sup_{J\subset(0,T)} |J|^{-\lambda/p}
\left(\int_J\|f(t)\|_X^p\,dt\right)^{1/p},
\]
where the supremum is over nonempty intervals. The fractional-domain norm is \(\|x\|_{D(B^\alpha)}=\|B^\alpha x\|_H\), as in the focal Hilbert-scale formulation. The finite interval and the compact-resolvent hypothesis are essential to the compactness assertion. The statement concerns the same Morrey exponent and the same Morrey parameter in source and target.

## Proof
Put \(s_*=1-j/m\).

First suppose \(0\le\alpha<s_*\). Choose \(\alpha_0\) such that
\[
\max\{\alpha,1-(j+1)/m\}<\alpha_0<s_*.
\]
Then \(\sigma_0=1-\alpha_0\) satisfies
\[
j/m<\sigma_0<(j+1)/m.
\]
Compact resolvent of \(B\) implies that \(D(B)\) embeds compactly into \(H\). The compact derivative theorem of Shahmurov--Shahmurov, applied with \(E_0=D(B)\), \(E=H\), \(q=2\), and interpolation coordinate \(\sigma_0\), therefore gives compactness of \(D_t^j\) into
\[
(D(B),H)_{\sigma_0,2}=D(B^{\alpha_0}).
\]
Since \(\alpha_0>\alpha\) and \(B\ge I\), the inclusion \(D(B^{\alpha_0})\hookrightarrow D(B^\alpha)\) is continuous. Composition proves compactness into \(D(B^\alpha)\).

At \(\alpha=s_*\), boundedness is exactly the finite-interval Hilbert-scale estimate of Shahmurov--Shahmurov:
\[
\|B^{s_*}D_t^j u\|_{\mathcal M^{p,\lambda}(H)}
\le C\left(
\|Bu\|_{\mathcal M^{p,\lambda}(H)}+
\|D_t^m u\|_{\mathcal M^{p,\lambda}(H)}
\right).
\]

It remains to prove critical noncompactness and supercritical unboundedness for each fixed \(B\). By the spectral theorem for a positive self-adjoint operator with compact resolvent, there are orthonormal eigenvectors \((e_n)\) and eigenvalues \(\beta_n\to\infty\) with \(Be_n=\beta_n e_n\). Set
\[
\omega_n=\beta_n^{1/m},
\qquad
u_n(t)=\beta_n^{-1}e^{i\omega_n t}e_n.
\]
Let
\[
c_{T,p,\lambda}=T^{(1-\lambda)/p}.
\]
Since \(\|Be^{i\omega_n t}\beta_n^{-1}e_n\|_H=1\) and \(\|D_t^m\nu_n(t)\|_H=1\),
\[
\|B\nu_n\|_{\mathcal M^{p,\lambda}(H)}
=
\|D_t^m\nu_n\|_{\mathcal M^{p,\lambda}(H)}
=
c_{T,p,\lambda}.
\]
Hence \((\nu_n)\) is bounded in the graph space. For every \(0\le\alpha\le1\),
\[
B^\alpha D_t^j\nu_n(t)
=i^j\beta_n^{\alpha-s_*}e^{i\omega_n t}e_n,
\]
so
\[
\|D_t^j\nu_n\|_{\mathcal M^{p,\lambda}(D(B^\alpha))}
=
c_{T,p,\lambda}\beta_n^{\alpha-s_*}.
\]
If \(\alpha>s_*\), these norms diverge, proving unboundedness. If \(\alpha=s_*\), then for \(n\ne k\), orthogonality gives at every \(t\)
\[
\|B^{s_*}(D_t^j\nu_n-D_t^j\nu_k)(t)\|_H=\sqrt2.
\]
Therefore
\[
\|D_t^j\nu_n-D_t^j\nu_k\|_{\mathcal M^{p,\lambda}(D(B^{s_*}))}
=
\sqrt2\,c_{T,p,\lambda}.
\]
The critical image contains a uniformly separated sequence, so the bounded critical map is not compact. This proves all three regimes.

## Verification
The proof uses no finite experiment or numerical approximation. The subcritical step was checked against the exact interpolation identity
\[
D(B^s)=(D(B),H)_{1-s,2}
\]
and the strict compactness range in the focal paper. The endpoint estimate was checked against its Hilbert-scale theorem. The obstruction sequence is internal to an arbitrary fixed compact-resolvent operator: its source graph norm is constant, its critical target distances are constant and positive, and its supercritical target norm diverges. The argument includes the boundary \(\lambda=0\) and every \(0\le\alpha\le1\).

## Relationship to prior work
Shahmurov--Shahmurov prove same-Morrey compactness for intermediate derivatives after a strict loss of interpolation smoothness, state that the same-Morrey compactness condition is strict, prove the Hilbert endpoint bound in \(D(B^{1-j/m})\), and give one model showing that a larger fractional-domain exponent cannot hold uniformly. Those results supply the subcritical and critical boundedness sides used here, but they do not state the fixed-operator compact/bounded-noncompact/unbounded trichotomy for every positive self-adjoint compact-resolvent \(B\).

Their companion paper on compact embeddings treats first-order Morrey evolution spaces, exact trace compactness, and a Hilbert-triple threshold for time-continuous compactness. Its Hilbert threshold concerns \(C([0,T];H)\), not the same-Morrey intermediate-derivative map into the fractional-domain scale above.

Ragusa--Shakhmurov prove subcritical compact embeddings for operator-valued Sobolev--Morrey spaces under an older multiplier framework. Their strict subcritical result is compatible with the first regime here, but the inspected statements do not give critical noncompactness for every fixed compact-resolvent Hilbert scale or the exact three-regime classification.

## Limitations
The result is restricted to positive self-adjoint compact-resolvent operators on infinite-dimensional complex Hilbert spaces, finite time intervals, and \(0\le\alpha\le1\). It does not assert compactness in a pointwise-in-time topology, does not address non-self-adjoint sectorial scales, and does not classify targets outside the fractional-domain scale. An equivalent endpoint-obstruction theorem may exist in older Sobolev--Lions terminology; this is the principal residual literature risk.

## References
1. R. Shahmurov and V. Shahmurov, *Derivative Embeddings in Vector-Valued Morrey Spaces*, arXiv:2610.00292v1, 2026.
2. R. Shahmurov and V. Shahmurov, *Compact Embeddings of Vector-Valued Morrey Spaces*, arXiv:2609.29152v1, 2026.
3. M. A. Ragusa and V. Shakhmurov, *Embedding of vector-valued Morrey spaces and separable differential operators*, Bulletin of Mathematical Sciences 9 (2019), 1950005, DOI:10.1007/s13373-018-0129-x.

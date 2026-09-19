# Depth-one local Clifford ensembles are non-plussed distinct

## Statement

Let \(\mathcal E\) be an ensemble of unitaries on \(\mathbb C^N\). For \(t\) query registers, let \(\Pi_{\mathrm{Dist}}\) be the projector onto computational-basis strings with pairwise distinct labels, let
\[
\Pi_{\mathrm{NoPlus}}=(I-|+\rangle\!\langle+|)^{\otimes t},
\]
and let \(\Pi_{\mathrm{DNP}}\) project onto
\(\mathrm{Dist}_{N,t}\cap\mathrm{NoPlus}_{N,t}\), the distinct nonplussed subspace of Foxman--Lombardi--Ma--Nehoran--Wright.

Define the worst-case ordinary distinctness failure
\[
\delta_t(\mathcal E)
:=\sup_\rho\Bigl(1-\mathbb E_{U\sim\mathcal E}
\operatorname{Tr}[\Pi_{\mathrm{Dist}}U^{\otimes t}\rho U^{\dagger\otimes t}]\Bigr)
\]
and the one-copy plus-state flatness parameter
\[
\mu_+(\mathcal E)
:=\left\|\mathbb E_{U\sim\mathcal E}
U^\dagger|+\rangle\!\langle+|U\right\|_\infty.
\]
For \(2\le t\le N/2\),
\[
\boxed{
\sup_\rho\Bigl(1-\mathbb E_U
\operatorname{Tr}[\Pi_{\mathrm{DNP}}U^{\otimes t}\rho U^{\dagger\otimes t}]\Bigr)
\le
4\delta_t(\mathcal E)+4t\mu_+(\mathcal E)
+\frac{t(t-1)}{N-t+1}.
}
\tag{1}
\]
In particular, if \(\mathcal E\) is an exact unitary 1-design, then \(\mu_+(\mathcal E)=1/N\), so
\[
\boxed{
\varepsilon_{\mathrm{DNP}}^{(t)}(\mathcal E)
\le
4\delta_t(\mathcal E)+\frac{4t}{N}
+\frac{t(t-1)}{N-t+1}.
}
\tag{2}
\]

Now let \(U=V_1\otimes\cdots\otimes V_n\), where the \(V_i\) are independent draws from an exact unitary 2-design on \(\mathbb C^d\), and put \(N=d^n\). Then
\[
\delta_t(\mathcal E)
\le \binom t2\left(\frac{2}{d+1}\right)^n,
\]
and hence
\[
\boxed{
\varepsilon_{\mathrm{DNP}}^{(t)}(\mathcal E)
\le
4\binom t2\left(\frac{2}{d+1}\right)^n
+\frac{4t}{d^n}
+\frac{t(t-1)}{d^n-t+1}.
}
\tag{3}
\]
For qubits, independent uniformly random single-qubit Clifford gates therefore satisfy
\[
\boxed{
\varepsilon_{\mathrm{DNP}}^{(t)}
\le
2t(t-1)\left(\frac23\right)^n
+\frac{4t}{2^n}
+\frac{t(t-1)}{2^n-t+1}.
}
\tag{4}
\]
For every polynomially bounded \(t=t(n)\), the right-hand side is negligible in \(n\). Thus the depth-one ensemble of independent single-qubit Clifford gates is non-plussed distinct, answering the explicit distinctness question posed by Raza--Eisert--Fefferman.

## Proof

Write \(P=\Pi_{\mathrm{Dist}}\), \(Q=\Pi_{\mathrm{NoPlus}}\), and \(R=\Pi_{\mathrm{DNP}}\). Foxman--Lombardi--Ma--Nehoran--Wright prove two geometric facts used in their unitary-2-design analysis. First, the quantum union bound gives, for every density operator \(\sigma\),
\[
\operatorname{Tr}(PQ\sigma QP)
\ge 1-4\operatorname{Tr}[(I-P)\sigma]
       -4\operatorname{Tr}[(I-Q)\sigma].
\tag{5}
\]
Second, their Friedrichs-angle estimate implies
\[
\operatorname{Tr}(R\sigma)
\ge \operatorname{Tr}(PQ\sigma QP)
-\frac{t(t-1)}{N-t+1}
\tag{6}
\]
in the regime considered here. Combining (5) and (6) reduces non-plussed distinctness to separate control of ordinary collisions and plus-state support.

For the second term, let \(Q_j=|+\rangle\!\langle+|\) on register \(j\). Since the \(Q_j\) act on distinct registers,
\[
I-Q=I-\prod_{j=1}^t(I-Q_j)\preceq\sum_{j=1}^t Q_j.
\]
Moreover,
\[
U^{\dagger\otimes t}Q_jU^{\otimes t}
=(U^\dagger|+\rangle\!\langle+|U)_j,
\]
with identity on all other registers. Therefore, for every \(\rho\),
\[
\mathbb E_U\operatorname{Tr}[(I-Q)U^{\otimes t}\rho U^{\dagger\otimes t}]
\le t\mu_+(\mathcal E).
\tag{7}
\]
A unitary 1-design has
\(\mathbb E_U U^\dagger|+\rangle\!\langle+|U=I/N\), giving \(t/N\). Equations (5)--(7), together with the definition of \(\delta_t\), prove (1) and (2).

It remains to establish the local-design bound in (3). On two local \(d\)-dimensional registers define
\[
\pi_{\mathrm{eq}}=\sum_{a=1}^d |aa\rangle\!\langle aa|.
\]
For an exact unitary 2-design,
\[
\mathbb E_V V^{\dagger\otimes2}\pi_{\mathrm{eq}}V^{\otimes2}
=\frac{2}{d+1}\Pi_{\mathrm{sym}}.
\tag{8}
\]
Indeed, \(\pi_{\mathrm{eq}}\) lies in the symmetric subspace and has trace \(d\), while \(\dim\mathrm{Sym}^2(\mathbb C^d)=d(d+1)/2\). Hence the operator norm in (8) is \(2/(d+1)\).

For \(U=\bigotimes_{b=1}^nV_b\), the global equality projector factors over sites, and independence gives
\[
\left\|\mathbb E_U U^{\dagger\otimes2}\Pi_{\mathrm{eq}}U^{\otimes2}\right\|_\infty
=\left(\frac{2}{d+1}\right)^n.
\tag{9}
\]
Thus every fixed pair of query registers collides with probability at most the right-hand side of (9), for every possibly entangled input state. Since the complement of the distinct subspace is the union of pair-collision events,
\[
I-P\preceq\sum_{1\le i<j\le t}\Pi_{\mathrm{eq}}^{(i,j)},
\]
which gives
\[
\delta_t(\mathcal E)
\le \binom t2\left(\frac{2}{d+1}\right)^n.
\tag{10}
\]
Finally, a tensor product of independent local 1-designs is itself a global 1-design: successively twirling each tensor factor sends any operator \(X\) to \(\operatorname{Tr}(X)I/d^n\). Applying (2) and (10) proves (3). For \(d=2\), the single-qubit Clifford group is an exact 2-design and (4) follows.

## Relation to prior work

Raza, Eisert and Fefferman prove that a depth-one layer of independent single-qubit Clifford gates is \((2/3)^n\)-entangled-anticoncentrated and hence negligibly distinct for polynomially many queries. In their discussion they explicitly ask whether this ensemble is also non-plussed distinct. Foxman, Lombardi, Ma, Nehoran and Wright introduced the distinct nonplussed subspace and proved that a global unitary 2-design has \(O(t^2/N)\) mass outside it; their proof separates the ordinary-distinct and NoPlus estimates and controls their noncommuting intersection using the Friedrichs angle.

Equation (1) isolates the general lifting principle implicit in that geometry: a global 2-design is not required. Ordinary distinctness plus one-copy plus-state flatness suffices. Product local 2-designs meet both conditions even though they are not global 2-designs, which yields the stated open-question corollary and the fixed-local-dimension qudit extension.

## Limitations

The result establishes concentration on the distinct nonplussed subspace for parallel forward-query states. It does **not** by itself prove that \(P\bigotimes_i C_i\) is a pseudorandom unitary after removing the binary phase layer: the corresponding security reduction may require additional structure beyond DNP concentration. It also does not address inverse, transpose, controlled, conjugate, or adaptive oracle access. The explicit bound is stated for \(t\le N/2\), which covers polynomially many queries when \(N=d^n\) with fixed \(d\ge2\). No claim of optimal constants is made.

## References

1. A. Raza, J. Eisert, B. Fefferman, *Distinctness threshold for pseudorandom unitaries*, arXiv:2609.03065v1 (2026). https://arxiv.org/abs/2609.03065
2. B. Foxman, A. Lombardi, F. Ma, B. Nehoran, J. Wright, *Quantum Lazy Sampling and Path Recording for Any Group*, arXiv:2606.30281v1 (2026). https://arxiv.org/abs/2606.30281

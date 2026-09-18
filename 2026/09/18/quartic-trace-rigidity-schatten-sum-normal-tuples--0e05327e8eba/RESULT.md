# A quartic trace identity rigidifies Schatten sum-normal tuples

## Result

Let \(H\) be a complex Hilbert space and let \({\bf T}=(T_1,\dots,T_d)\) be a commuting \(d\)-tuple with \(T_j\in \mathcal S_4(H)\). Put
\[
D=\sum_{j=1}^d[T_j^*,T_j],\qquad C_{jk}=[T_j^*,T_k].
\]
Then \(D,C_{jk}\in\mathcal S_2(H)\) and
\[
\boxed{\ \|D\|_2^2=\sum_{j,k=1}^d\|C_{jk}\|_2^2.\ }
\]
Consequently, a commuting Schatten-4 tuple is sum-normal, \(D=0\), if and only if it is doubly commuting; in particular every coordinate is normal. The same conclusion therefore holds for commuting tuples in \(\mathcal S_p\) for every \(0<p\le4\).

If instead \(T_j\in\mathcal S_2(H)\) and the tuple is sum-hyponormal, \(D\ge0\), then \(D\in\mathcal S_1\) and
\[
\operatorname{Tr}D=\sum_j\big(\|T_j\|_2^2-\|T_j^*\|_2^2\big)=0.
\]
Thus \(D=0\), and the quartic identity implies \(C_{jk}=0\) for every \(j,k\). Hence every commuting sum-hyponormal Schatten-2 tuple is normal and doubly commuting. This also holds for \(\mathcal S_p\), \(0<p\le2\).

There is an analogous finite-tracial-algebra statement. If \((M,\tau)\) is a finite von Neumann algebra with a faithful normal finite trace and \(T_1,\dots,T_d\in M\) commute, then
\[
\left\|\sum_j[T_j^*,T_j]\right\|_{2,\tau}^2
=
\sum_{j,k}\|[T_j^*,T_k]\|_{2,\tau}^2.
\]
Therefore every commuting sum-normal tuple in \(M\) is doubly commuting, and every commuting sum-hyponormal tuple in \(M\) is normal: positivity gives \(\tau(D)=0\), hence \(D=0\) by faithfulness, and then the identity annihilates all mixed commutators.

## Proof of the identity

Schatten Hölder gives \(T_j^*T_k,T_kT_j^*\in\mathcal S_2\), so all traces below are legitimate. Since \(D=D^*\),
\[
\|D\|_2^2=\operatorname{Tr}(D^2).
\]
Also \(C_{jk}^*=C_{kj}\), hence
\[
\sum_{j,k}\|C_{jk}\|_2^2
=
\sum_{j,k}\operatorname{Tr}\!\left((T_k^*T_j-T_jT_k^*)(T_j^*T_k-T_kT_j^*)\right).
\]
Expand the right-hand side. Its four sums are
\[
\begin{aligned}
A&=\sum_{j,k}\operatorname{Tr}(T_k^*T_jT_j^*T_k),\\
B&=\sum_{j,k}\operatorname{Tr}(T_k^*T_jT_kT_j^*),\\
C&=\sum_{j,k}\operatorname{Tr}(T_jT_k^*T_j^*T_k),\\
E&=\sum_{j,k}\operatorname{Tr}(T_jT_k^*T_kT_j^*).
\end{aligned}
\]
Using cyclicity of the trace, \(T_jT_k=T_kT_j\), and therefore \(T_j^*T_k^*=T_k^*T_j^*\), these become
\[
\begin{aligned}
A&=\sum_{j,k}\operatorname{Tr}(T_jT_j^*T_kT_k^*),\\
B&=\sum_{j,k}\operatorname{Tr}(T_j^*T_jT_kT_k^*),\\
C&=\sum_{j,k}\operatorname{Tr}(T_jT_j^*T_k^*T_k),\\
E&=\sum_{j,k}\operatorname{Tr}(T_j^*T_jT_k^*T_k).
\end{aligned}
\]
Thus the expanded sum is \(A-B-C+E\), exactly
\[
\operatorname{Tr}\!\left(\left(\sum_j(T_j^*T_j-T_jT_j^*)\right)^2\right)=\operatorname{Tr}(D^2).
\]
The proof in a finite tracial von Neumann algebra is identical with \(\operatorname{Tr}\) replaced by \(\tau\).

## Quantitative consequence

The identity is a no-cancellation law at quartic trace level:
\[
\|[T_j^*,T_k]\|_2\le \left\|\sum_\ell[T_\ell^*,T_\ell]\right\|_2
\quad(1\le j,k\le d).
\]
Thus, inside \(\mathcal S_4\), a small sum-normality defect controls every mixed adjoint commutator in Hilbert--Schmidt norm with constant one.

## Relation to recent work

Chavan, Reza and Sequeira, *Sum of self-commutators of commuting operators* (arXiv:2609.19287, September 2026), introduce sum-normal and sum-hyponormal commuting tuples and explicitly ask whether every sum-normal tuple must be normal. They prove several affirmative cases and a decomposition for compact sum-hyponormal tuples, but the general sum-normal question remains open. The theorem above gives an affirmative answer for the Schatten-4 ideal and a stronger doubly-commuting conclusion. It also upgrades the trace obstruction for sufficiently summable sum-hyponormal tuples: Schatten-2 membership forces normality.

Misra, Pramanick and Sinha, *A trace inequality for commuting tuple of operators* (arXiv:2012.11115), study the full matrix \(([T_j^*,T_k])_{j,k}\), its symmetrized determinant and associated trace inequalities. This is close structural prior art for mixed commutators. The present result concerns instead the exact Hilbert--Schmidt energy identity above. Searches for the displayed identity, its Schatten-4 rigidity consequence, and its finite-tracial formulation did not locate a prior statement; originality is therefore asserted only to the best of our knowledge.

## Limitations

The Schatten-4 hypothesis is a sufficient summability condition that makes the quartic trace calculation legitimate; no sharpness of the exponent \(4\) is claimed. In particular, the result does not settle whether an arbitrary compact sum-normal commuting tuple must be normal. The commuting hypothesis is essential: for a nonnormal finite-rank operator \(A\), the noncommuting pair \((A,A^*)\) has cancelling self-commutators, \([A^*,A]+[A,A^*]=0\), without normality. The finite-von-Neumann-algebra consequence uses a faithful finite trace.

## Sources

- Sameer Chavan, Md. Ramiz Reza, Shanola S. Sequeira, *Sum of self-commutators of commuting operators*, arXiv:2609.19287. https://arxiv.org/abs/2609.19287
- Gadadhar Misra, Paramita Pramanick, Kalyan B. Sinha, *A trace inequality for commuting tuple of operators*, arXiv:2012.11115. https://arxiv.org/abs/2012.11115

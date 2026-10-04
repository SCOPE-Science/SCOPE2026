# A dense arithmetic spectrum of perfect-transfer energy shifts on complete spin networks

## Finding

Fix an integer \(n\ge4\). Consider the single-excitation XY Hamiltonian used by Casaccino, Lloyd, Mancini, and Severini on the complete graph \(K_n\): every off-diagonal coupling has weight \(2\), and the two designated input/output vertices receive the same positive diagonal energy shift \(\Delta>0\). Define
\[
\alpha(\Delta)=\sqrt{4n^2-4(n-4)\Delta+\Delta^2},
\qquad
\beta(\Delta)=\frac{\Delta-2n}{\alpha(\Delta)}.
\]
Then perfect state transfer between the two shifted vertices occurs if and only if
\[
\beta(\Delta)=\frac pq
\]
in lowest terms with integers \(q>0\), \(|p|<q\), and \(p,q\) of opposite parity.

When this holds, the complete set of positive perfect-transfer times is
\[
t=\frac{2\pi q}{\alpha(\Delta)}(2s+1),
\qquad s=0,1,2,\ldots,
\]
so the minimum positive transfer time is
\[
t_{\min}=\frac{2\pi q}{\alpha(\Delta)}.
\]

The condition can be written directly as a parametrization of all positive shifts:
\[
\Delta_{p,q}
=
\frac{\left(2p+\sqrt{2nq^2-2(n-2)p^2}\right)^2}{q^2-p^2},
\]
where \(q>0\), \(|p|<q\), \(\gcd(p,q)=1\), and \(p,q\) have opposite parity. In particular,
\[
(p,q)=(0,1)
\quad\Longrightarrow\quad
\Delta=2n,
\]
which is the tuning displayed in the source paper.

There are infinitely many other exact tunings. In fact, the perfect-transfer shifts form a countable dense subset of \((0,\infty)\). Thus the source value \(\Delta=2n\) is a particularly simple exact point, rather than the unique positive energy shift supporting perfect transfer.

## Assumptions and scope

The Hamiltonian normalization is exactly that of the source: in the single-excitation basis, every edge of \(K_n\) contributes an off-diagonal matrix entry \(2\). Only the two input/output vertices receive the common shift \(\Delta\), and \(\Delta\) is restricted to be positive. The graph order satisfies \(n\ge4\), matching the complete-graph theorem in the source.

The result classifies exact perfect transfer for this fixed-coupling one-parameter family. It does not classify unequal shifts on the two marked vertices, changes to the edge weights, missing-edge graphs, noisy Hamiltonians, or pretty-good transfer at shifts outside the exact arithmetic set.

## Proof

Let the two shifted vertices be \(1\) and \(2\). Introduce
\[
a=\frac{e_1-e_2}{\sqrt2},
\qquad
s=\frac{e_1+e_2}{\sqrt2},
\qquad
r=\frac1{\sqrt{n-2}}\sum_{j=3}^n e_j.
\]
The antisymmetric vector is an eigenvector with eigenvalue
\[
\lambda_a=\Delta-2.
\]
The only part of the symmetric sector reached from \(s\) is \(\operatorname{span}\{s,r\}\), on which the Hamiltonian is
\[
B=
\begin{pmatrix}
\Delta+2 & 2\sqrt{2(n-2)}\\
2\sqrt{2(n-2)} & 2(n-3)
\end{pmatrix}.
\]
Its mean eigenvalue and spectral gap are
\[
\tau=\frac{\Delta+2n-4}{2},
\qquad
\alpha=\sqrt{4n^2-4(n-4)\Delta+\Delta^2}.
\]

Since
\[
e_1=\frac{s+a}{\sqrt2},
\qquad
e_2=\frac{s-a}{\sqrt2},
\]
perfect transfer from \(e_1\) to \(e_2\) first requires zero amplitude in the \(r\)-direction. The off-diagonal entry of \(e^{-itB}\) is a nonzero constant times \(\sin(\alpha t/2)\), so this happens exactly when
\[
t=\frac{2\pi k}{\alpha},
\qquad k\in\mathbb Z_{>0}.
\]
At such a time, the symmetric state has phase
\[
e^{-itB}s=(-1)^k e^{-i\tau t}s.
\]
Perfect transfer further requires the symmetric and antisymmetric phases to be opposite:
\[
(-1)^k e^{-i\tau t}=-e^{-i\lambda_a t}.
\]
Since
\[
\lambda_a-\tau=\frac{\Delta-2n}{2},
\]
this condition is equivalent to
\[
e^{-i\pi k\beta}=(-1)^{k+1},
\qquad
\beta=\frac{\Delta-2n}{\alpha}.
\]

If transfer occurs, then \(k\beta\) is an integer, so \(\beta\) is rational. Write \(\beta=p/q\) in lowest terms with \(q>0\). Then \(q\mid k\); writing \(k=qs\), the parity condition becomes
\[
sp\equiv qs+1\pmod2,
\]
or
\[
s(p-q)\equiv1\pmod2.
\]
This has a solution exactly when \(p-q\) is odd, that is, exactly when \(p\) and \(q\) have opposite parity. In that case the solutions are precisely the odd integers \(s\), proving the complete time formula.

For \(\Delta>0\),
\[
\alpha^2=(\Delta-2n)^2+16\Delta,
\]
so \(|\beta|<1\). Moreover,
\[
\beta'(\Delta)
=
\frac{8\Delta+16n}{\alpha(\Delta)^3}>0,
\]
and
\[
\lim_{\Delta\downarrow0}\beta(\Delta)=-1,
\qquad
\lim_{\Delta\to\infty}\beta(\Delta)=1.
\]
Thus \(\beta\) is a continuous increasing bijection from \((0,\infty)\) onto \((-1,1)\).

To invert it, set \(\beta=p/q\) and \(y=\sqrt\Delta\). From
\[
\frac{\beta}{\sqrt{1-\beta^2}}
=
\frac{\Delta-2n}{4\sqrt\Delta}
\]
one obtains
\[
y
=
\frac{2p+\sqrt{2nq^2-2(n-2)p^2}}{\sqrt{q^2-p^2}},
\]
which gives the displayed \(\Delta_{p,q}\).

Finally, reduced dyadic fractions with odd numerator,
\[
\frac{2j+1}{2^m},
\]
are dense in \((-1,1)\) and always have opposite-parity numerator and denominator. Their inverse images under the continuous bijection \(\beta^{-1}\) are therefore dense in \((0,\infty)\). This proves the density statement.

## Verification

`verify_complete_graph_shifts.py` checks the arithmetic parametrization and the exact reduced dynamics. For several graph orders and many reduced pairs \((p,q)\) of opposite parity, it reconstructs \(\Delta_{p,q}\), verifies \(\beta(\Delta_{p,q})=p/q\), evolves the exact antisymmetric-plus-two-dimensional reduction at the predicted minimum time, and checks unit transfer with zero leakage. It also checks same-parity reduced pairs such as \((1,3)\), for which every leakage-free time fails the phase condition.

The checker additionally confirms that \((p,q)=(0,1)\) gives \(\Delta=2n\) and reproduces the source transfer time. These finite checks are supplementary; the all-parameter classification is proved algebraically above.

## Relationship to prior work

Casaccino, Lloyd, Mancini, and Severini derive the complete-graph spectrum and exact transition amplitudes for this Hamiltonian. Their Theorem 1 exhibits the choice \(\Delta=2n\) and the corresponding perfect-transfer times, and the text calls this the optimal energy shift. The inspected paper does not classify all positive shifts that give exact transfer.

Angeles-Canul, Norton, Opperman, Paribello, Russell, and Tamon subsequently developed a more general weighted-join framework. Their double-cone corollary gives sufficient rational/parity constructions when both self-loop and edge weights may be chosen. It explicitly describes itself as generalizing the Casaccino observation. That result does not state the fixed-edge-weight necessary-and-sufficient classification above; here every off-diagonal coupling remains fixed at the source value \(2\), and only the common diagonal shift varies.

Kempton, Lippner, and Yau later proved broad existence results for perfect state transfer after adding graph potentials. Their theorem is nonconstructive in a substantially more general potential space and does not provide this one-parameter arithmetic spectrum.

Targeted searches for the complete graph with two equal potentials, the Casaccino tuning, rational eigenvalue-gap conditions, and weighted self-loops did not locate the displayed iff classification, its exact minimum-time formula, or the density conclusion.

## Limitations

The novelty claim is deliberately narrow. The spectral reduction and the explicit point \(\Delta=2n\) are prior work; the contribution assessed here is the complete fixed-coupling classification of all positive equal shifts and its dense arithmetic parametrization.

Density is an exact mathematical statement, not a robustness statement: nearby perfect-transfer shifts can have very different minimum transfer times, and generic nearby shifts need not give exact transfer. Noise sensitivity remains outside the theorem.

An equivalent specialization may be derivable from later general potential or weighted-join criteria using different notation. The inspected high-relevance sources did not state this fixed-coupling classification explicitly.

## References

1. A. Casaccino, S. Lloyd, S. Mancini, and S. Severini, “Quantum state transfer through a qubit network with energy shifts and fluctuations,” arXiv:0904.4510; *International Journal of Quantum Information* 7 (2009), 1417–1427, DOI: 10.1142/S0219749909006085.
2. R. J. Angeles-Canul, R. M. Norton, M. C. Opperman, C. C. Paribello, M. C. Russell, and C. Tamon, “On quantum perfect state transfer in weighted join graphs,” arXiv:0909.0431 (2009).
3. M. Kempton, G. Lippner, and S.-T. Yau, “Perfect state transfer on graphs with a potential,” *Quantum Information and Computation* 17 (2017), 303–327, arXiv:1611.02093, DOI: 10.26421/QIC17.3-4-7.

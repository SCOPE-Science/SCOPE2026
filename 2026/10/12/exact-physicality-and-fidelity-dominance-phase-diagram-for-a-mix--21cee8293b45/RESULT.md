# Exact physicality and fidelity-dominance phase diagram for a mixed non-orthogonal teleportation family
## Finding
For the mixed non-orthogonal two-qubit family introduced in arXiv:1002.2047v1,
\[
\rho_N(r,\epsilon)=g\,|\psi_r\rangle\langle\psi_r|+\frac{1-g}{4}I_4,
\qquad
g=\frac{1+r^2}{3-r^2}+\epsilon,
\]
with \(0\le r<1\) and \(\epsilon>0\), the source's epsilon-only statement is not sufficient for \(\rho_N\) to be a density operator. The exact physical entangled domain is
\[
0<\epsilon\le \epsilon_{\max}(r):=\frac{2(1-r^2)}{3-r^2}.
\]
Equivalently, for \(0<\epsilon<2/3\), physicality is exactly
\[
0\le r\le \sqrt{\frac{2-3\epsilon}{2-\epsilon}}.
\]
At \(\epsilon=2/3\), only \(r=0\) remains physical, and for \(\epsilon>2/3\) there is no physical member of this parametrized entangled family. Within the physical domain, the source's average fidelity
\[
F_N(r,\epsilon)=\frac23+\frac{(3-r^2)\epsilon}{6(1+r^2)}
\]
has an exact comparison with its reference mixed state \(\rho_{\rm new}(p)\), whose useful range is \(0\le p<1/4\) and fidelity is \(F_{\rm new}(p)=(7-4p)/9\):
\[
F_N>F_{\rm new}\quad\Longleftrightarrow\quad
p>p_*(r,\epsilon):=\frac14-\frac{3\epsilon(3-r^2)}{8(1+r^2)},
\]
with equality exactly at \(p=p_*\). Uniform strict dominance over every useful \(p\in[0,1/4)\) occurs exactly when \(r<1/\sqrt2\) and
\[
\frac{2(1+r^2)}{3(3-r^2)}<\epsilon\le\frac{2(1-r^2)}{3-r^2}.
\]
At \(r=1/\sqrt2\) and \(\epsilon=2/5\), the two families tie at \(p=0\) and \(\rho_N\) is strictly better for every \(p>0\). Thus the physicality constraint and the relative-fidelity comparison together have a sharp \(r=1/\sqrt2\) transition that is absent from the source's verbal parameter-range statements.

## Assumptions and scope
The family is exactly the two-qubit state of Eq. (22) in Adhikari--Majumdar--Home--Pan--Joshi, with the entangled parametrization of Eq. (25). The non-orthogonality parameter satisfies \(0\le r<1\), and \(\epsilon>0\). The comparison state \(\rho_{\rm new}(p)\) is used only on the source's useful-teleportation interval \(0\le p<1/4\). No assertion is made about other non-orthogonal state families or other teleportation protocols.

## Proof
Because \(|\psi_r\rangle\) is normalized, the eigenvalues of
\[
\rho_N=g|\psi_r\rangle\langle\psi_r|+\frac{1-g}{4}I_4
\]
are \((1+3g)/4\) once and \((1-g)/4\) with multiplicity three. In the entangled parametrization \(g=(1+r^2)/(3-r^2)+\epsilon\), positivity from below is automatic, so \(\rho_N\ge0\) is equivalent to \(g\le1\). Solving that inequality gives
\[
0<\epsilon\le\frac{2(1-r^2)}{3-r^2}.
\]
For \(0<\epsilon<2/3\), solving the same inequality for \(r^2\) gives
\[
r^2\le\frac{2-3\epsilon}{2-\epsilon}.
\]
The endpoint statements follow directly.

For the fidelity comparison, subtract the two published formulas:
\[
F_N-F_{\rm new}
=\frac{4p-1}{9}+\frac{\epsilon(3-r^2)}{6(1+r^2)}.
\]
This is positive exactly when
\[
p>\frac14-\frac{3\epsilon(3-r^2)}{8(1+r^2)}=:p_*(r,\epsilon).
\]
Strict dominance for every \(p\in[0,1/4)\) is equivalent to \(p_*<0\), hence
\[
\epsilon>\epsilon_{\rm all}(r):=\frac{2(1+r^2)}{3(3-r^2)}.
\]
Such an \(\epsilon\) can also obey the physicality upper bound precisely when
\[
\epsilon_{\rm all}(r)<\epsilon_{\max}(r)
\quad\Longleftrightarrow\quad r^2<\frac12.
\]
At \(r^2=1/2\), both bounds equal \(2/5\), yielding equality at \(p=0\) and strict superiority for \(p>0\).

## Verification
The included `verify.py` uses exact rational arithmetic to replay the physicality boundary, the fixed-\(\epsilon\) inversion, the source-figure cutoffs \(r^2=7/9\) for \(\epsilon=1/5\) and \(r^2=1/2\) for \(\epsilon=2/5\), the fidelity threshold \(p_*\), and the critical value \(r^2=1/2\). Its finite grid is supplementary; the proof above establishes the quantified statements for the full continuous parameter domain.

## Relationship to prior work
Adhikari et al. define \(\rho_N\) with \(0\le g\le1\), introduce \(g=(1+r^2)/(3-r^2)+\epsilon\), and state that \(\rho_N\) can always be used as a teleportation channel for \(0<\epsilon<2/3\). Their Eqs. (28) and (30) also give the two fidelity formulas compared here, while the text reports only that the non-orthogonal mixed channel can be better for a range of parameters. The present result resolves the internal parameter-domain mismatch and gives the exact joint comparison partition. The later comparative study arXiv:1610.02514v1 treats quasi-Bell states and explicit noise models; its inspected scope does not supply this mixed-state physicality or dominance diagram.

## Limitations
The result starts from the published state and fidelity formulas and does not independently rederive the full teleportation protocol. The exact physicality boundary is elementary once the source parametrization is written down; its value is that it is necessary to correct the source's parameter-wide operational statement and to delimit the fidelity comparison. No claim is made that the underlying teleportation criterion or the reference state's fidelity formula is new. A residual literature risk remains that an unindexed erratum or later note may have stated the same corrected phase diagram.

## References
1. S. Adhikari, A. S. Majumdar, D. Home, A. K. Pan, and P. Joshi, “Quantum teleportation using non-orthogonal entangled channels,” arXiv:1002.2047v1 (2010); later Physica Scripta 85, 045001 (2012), DOI:10.1088/0031-8949/85/04/045001.
2. M. Sisodia, V. Verma, K. Thapliyal, and A. Pathak, “Teleportation of a qubit using entangled non-orthogonal states: A comparative study,” arXiv:1610.02514v1 (2016).

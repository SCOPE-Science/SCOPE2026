# Six arithmetic phase symmetries of the square-spectrum fourth-moment majorant

## Finding
For every integer \(N\ge 11\), let \(w_1,\ldots,w_N>0\), let \(\theta_1,\ldots,\theta_N\in\mathbb R\), and define
\[
P_{\theta}(t)=\sum_{k=1}^{N} w_k e^{i\theta_k}e^{ik^2t},\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
With normalized Haar measure \(dt/(2\pi)\),
\[
\|P_{\theta}\|_4^4\le\|P_0\|_4^4.
\]
The complete equality family is **independent of the strictly positive weights**. Equality holds if and only if there exist six real parameters \(\alpha,\beta,\gamma,\delta,\epsilon,\zeta\) such that, for every \(1\le k\le N\),
\[
\theta_k\equiv \alpha+\beta k^2+\gamma\,\mathbf1_{4\mid k}
+\delta\,\mathbf1_{k\equiv2\pmod4}
+\epsilon\,\mathbf1_{3\nmid k}+\zeta\,\chi_5(k)\pmod{2\pi},
\]
where \(\chi_5(k)=0\) for \(5\mid k\), \(\chi_5(k)=1\) for \(k\equiv\pm1\pmod5\), and \(\chi_5(k)=-1\) for \(k\equiv\pm2\pmod5\).

The equality set is a connected six-dimensional torus in the \(N\)-dimensional coefficient-phase torus, with coordinates freely prescribed at indices \(1,\ldots,6\). The displayed six-parameter map onto it is exactly \(120\)-to-one on parameter tori. At \(N=10\) the equality set has dimension \(7\); thus \(11\) is the sharp threshold after which the six-dimensional classification persists for **every** larger truncation. In particular, besides constant phase and spatial translation, there are four genuine arithmetic phase symmetries of the maximal fourth moment.

## Assumptions and scope
The spectrum consists of positive integer squares \(\{k^2:1\le k\le N\}\). The weights are arbitrary positive real numbers, not necessarily decreasing or equal. The phases are considered modulo \(2\pi\). The theorem concerns the phase maximizers of the fourth moment for fixed coefficient magnitudes; it does not determine the optimal magnitudes under an \(\ell^2\) constraint, nor higher even moments, nor other polynomial spectra.

## Proof
**1. The equality equations.** Parseval and convolution give the exact identity
\[
\|P_\theta\|_4^4
=\sum_{s=2}^{2N^2}\left|\sum_{a^2+b^2=s}w_aw_b e^{i(\theta_a+\theta_b)}\right|^2,
\]
where inner sums use ordered pairs \(1\le a,b\le N\). Triangle inequalities prove the stated upper bound. Because every \(w_k\) is positive, equality occurs exactly when
\[
\theta_a+\theta_b\equiv\theta_c+\theta_d\pmod{2\pi}
\quad\text{whenever}\quad a^2+b^2=c^2+d^2.
\tag{1}
\]
Repeated indices are allowed. This proves necessity and sufficiency without estimates or limiting arguments.

**2. Six exact solutions of (1).** The constant phase and square-frequency phase satisfy (1) immediately. The two residue-class functions \(\mathbf1_{4\mid k}\) and \(\mathbf1_{k\equiv2\pmod4}\) do as well: the six possible unordered pairs of classes (divisible by \(4\), congruent to \(2\) modulo \(4\), odd) have disjoint squared-sum residue sets modulo \(16\), namely \(\{0\}\), \(\{4\}\), \(\{8\}\), \(\{1,9\}\), \(\{5,13\}\), \(\{2,10\}\). Thus an equal sum of squares preserves the number of entries in each even class. Next, squares modulo \(3\) are \(0\) or \(1\), so the sum modulo \(3\) fixes the number of indices not divisible by \(3\). Finally, squares modulo \(5\) lie in \(\{0,1,4\}\). Two-element multisets of these residues have different sums modulo \(5\), except \(\{0,0\}\) and \(\{1,4\}\), both summing to \(0\). Their sums of \(\chi_5\)-values are both zero; all other cases force the same \(\chi_5\)-sum. Therefore each of the six displayed functions obeys every relation (1).

**3. Six freely chosen initial phases.** Form the \(6\times6\) matrix of these functions, in displayed order, evaluated at \(k=1,\ldots,6\):
\[
B=\begin{pmatrix}
1&1&0&0&1&1\\
1&4&0&1&1&-1\\
1&9&0&0&0&-1\\
1&16&1&0&1&1\\
1&25&0&0&1&0\\
1&36&0&1&0&1
\end{pmatrix},\qquad \det B=120.
\]
As a full-rank integer matrix, \(B\) induces a surjective torus endomorphism \((\mathbb R/2\pi\mathbb Z)^6\to(\mathbb R/2\pi\mathbb Z)^6\), with finite kernel of order \(120\). Therefore every six-tuple of initial phases is obtained from the displayed family, with precisely \(120\) parameter choices modulo \(2\pi\).

**4. Five small equal-square relations determine indices \(7\) through \(11\).** The following integer identities are exact:
\[
\begin{aligned}
7^2+1^2&=5^2+5^2,\\
8^2+1^2&=7^2+4^2,\\
9^2+2^2&=7^2+6^2,\\
11^2+3^2&=9^2+7^2,\\
10^2+5^2&=11^2+2^2.
\end{aligned}
\]
Equation (1) accordingly determines, in the order \(7,8,9,11,10\), all five remaining phases from the first six. Since one of our six-parameter phase sequences matches any prescribed first six, every equality sequence through index \(11\) coincides with one of them.

**5. A uniform infinite descent from a three-four-five rotation.** Fix an integer \(k\ge12\). There is a unique \(a\in\{1,2,3,4,5\}\) satisfying \(a\equiv 3k\pmod5\). Put
\[
b=\frac{3k+4a}{5},\qquad c=\frac{4k-3a}{5}.
\]
Both are positive integers, and \(a,b,c<k\) because \(a\le5<k/2\), \(b<k\iff a<k/2\), and \(c<k\) automatically. Direct expansion gives
\[
k^2+a^2=b^2+c^2.
\]
Hence every equality sequence must satisfy \(\theta_k\equiv\theta_b+\theta_c-\theta_a\pmod{2\pi}\). Strong induction shows that agreement on the first eleven indices forces agreement on every subsequent index. Since our six-feature sequences satisfy every relation (1), the equality classification is both necessary and sufficient for all \(N\ge11\).

**6. Sharp stable onset and topology.** For \(N=10\), the only unordered equal-two-square collisions are \(50=1^2+7^2=5^2+5^2\), \(65=1^2+8^2=4^2+7^2\), and \(85=2^2+9^2=6^2+7^2\). They independently determine the phases at \(7,8,9\), while index \(10\) remains free. Thus the equality torus has dimension \(7\) at \(N=10\). The two new collisions at \(N=11\) determine both \(10\) and \(11\) and lower its dimension to \(6\); the descent prevents further reductions. As arbitrary first-six phases parametrize the equality set bijectively, its dimension is exactly six and it is connected, not a union of torsion translates.

## Verification
The standalone `verify.py` requires only Python's standard library. It checks the integer determinant \(120\); exact relation ranks \(3,5,6,12\) at \(N=10,11,12,18\); all six modular invariants for every two-square collision through \(N=100\); the descent identities for each integer from \(12\) through \(2499\); and direct complex fourth-moment identities at two truncation sizes. Run `python verify.py`. These finite checks independently detect coding and algebraic mistakes, but the universal result rests on the modular proof and algebraic descent, not finite enumeration.

## Relationship to prior work
Ioann Vasilyev, *Norm bounds on Fourier series with polynomial spectra and constrained coefficients* (arXiv:2608.19132, public August 19, 2026), studies fourth moments on polynomial spectra, including the squares, with coefficient-size hypotheses. Its square-spectrum estimates motivate studying equality under independent variation of coefficient phases. Those estimates do not determine this six-parameter equality family, its extra arithmetic symmetries, or the cutoff at \(N=11\). General fourth-moment formulae and results on phase rigidity for other finite Fourier supports are relevant background but do not imply the square-spectrum two-sum relation classification. The usual majorant triangle inequality is classical; the claim here is the exhaustive arithmetic description of **all** its equality cases for arbitrary positive weights.

## Limitations
The classification requires strictly positive weights; if any coefficient vanishes, equality may have additional phase freedoms. It only concerns the fourth moment and the positive-square spectrum. The cutoff is stabilization after \(N=11\), not a claim that smaller truncations never have six-dimensional equality sets. The 120-to-one count describes the specific integer-parameter representation, not the number of distinct coefficient-phase maximizers, which is uncountable. Historical-priority checks do not exclude unindexed equivalent work. No independent validation has been performed.

## References
- I. Vasilyev, *Norm bounds on Fourier series with polynomial spectra and constrained coefficients*, arXiv:2608.19132 (first submitted August 19, 2026), https://arxiv.org/abs/2608.19132.
- Classical Parseval identity, Fourier-convolution fourth-moment formula, and equal-sums-of-two-squares identities (standard background).

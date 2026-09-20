# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the level of constants and normalizations.

The starting expansion
\[
f_n(x)=n!\sum_{j\ge0}e^{-jx}L_n(jx)
\]
follows directly from termwise differentiation of the geometric series for \((1-e^{-x})^{-1}\), as recorded in Castillo's article.

The 2025 correction gives
\[
\frac{e^{y^2}}{\sqrt\pi}\int_{\mathbb R}e^{-t^2}H_n(t)^2\cos(2yt)\,dt
=2^n n!L_n(2y^2).
\]
With \(y^2=jx/2\), its exponential factor is \(e^{-jx/2}\). Multiplication by the original \(e^{-jx}\) therefore leaves the kernel coefficient \(q^j=e^{-jx/2}\), not \(e^{-jx}\). This scaling is essential; direct substitution confirms it.

For each squarefree \(d\), the block
\[
\sum_{m\ge1}(q^d)^{m^2}\cos(m\sqrt d\,u)
\]
is one half of \(\theta_3(\sqrt d\,u/2,q^d)-1\). The DLMF product for \(\theta_3\) implies its minimum is bounded below by the corresponding \(\theta_4(0,q^d)\) value, because
\[
1+2a\cos(2z)+a^2\ge(1-a)^2.
\]
The recombination is exact: in the unique representation \(j=dm^2\) with \(d\) squarefree, \(m\) is even if and only if \(4\mid j\). Hence the lower bound becomes
\[
1-\frac q{1-q}+\frac{2q^4}{1-q^4}
=\frac{1-q-q^2-q^3}{1-q^4}.
\]
All rearrangements are justified by domination by \(\sum_{j\ge0}q^j\).

At the equality threshold the kernel lower bound is only zero. Strict positivity of \(f_n\) nevertheless follows because \(K_q(0)=1/(1-q)>0\), continuity gives a neighborhood where the kernel is positive, and a nonzero Hermite polynomial cannot vanish on an interval.

No hidden convexity, asymptotic, or numerical assumption is used.

## Originality

The literature check began from the older Clark–Ismail line and then followed later status updates.

- Clark–Ismail (2003) formulates the derivative-positivity/complete-monotonicity program.
- Alzer–Berg–Koumandos (2005) disproves the global all-order complete-monotonicity conjecture and is cited by later work for the remaining uniform-threshold problem.
- Castillo (2024) explicitly states that determining the smallest positive uniform threshold remains open and records the earlier \(2\log2\) theorem.
- Castillo's 2025 correction retracts the claimed \(\log2\) improvement, supplies the corrected Hermite–Laguerre identity, and restores the theorem \(x>2\log2\). It says that alternative Laguerre integral representations could slightly refine that interval, but gives no concrete replacement threshold.

Searches for the exact derivative expression together with theta functions, squarefree decomposition, the cubic \(q+q^2+q^3=1\), the decimal threshold \(1.218755\ldots\), and combinations of Hermite/Laguerre/theta terminology did not locate this theorem or proof. Current searches around the 2025 correction also did not reveal a later published explicit improvement.

The full Al-Musallam–Bustoz (2006) article was not separately inspected. Its \(2\log2\) result is explicitly stated in Castillo's primary literature, including the 2025 correction. Because the 2025 correction itself notes unspecified possible refinements, an unpublished or differently indexed stronger estimate remains a concrete originality risk. No available source found during this check supplied the squarefree-theta argument or the stated cubic threshold.

## Value

The contribution is more than a numerical perturbation of \(2\log2\): it exposes a structural lower-bound mechanism for the nonharmonic kernel
\[
\sum_{j\ge0}q^j\cos(\sqrt j\,u)
\]
by decomposing frequencies according to squarefree kernel. The resulting theta blocks admit exact global lower bounds, and their recombination collapses to an elementary rational function. The method is potentially reusable for other kernels whose frequencies are indexed by square parts.

Quantitatively, the sufficient threshold decreases from \(2\log2=1.386294\ldots\) to
\[
-2\log\rho=1.218755726872012\ldots.
\]

## Limitations

The theorem gives an upper bound for the optimal uniform threshold, not its exact value. It does not classify failures below the bound or determine a minimal failing derivative order. The unspecified refinements mentioned in the 2025 correction were not available for comparison. A differently phrased, unpublished, or poorly indexed stronger result may exist.

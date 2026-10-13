# Polylogarithmic universal overhead gives near-linear-dimension single-shot QLDPC families
## Finding
Let \(\mathcal C_n=[[n,k_n]]\) be any CSS quantum low-density parity-check family with uniformly bounded check weight and qubit degree and with \(k_n/n\to R>0\). Fix a joint local-stochastic physical-and-measurement noise rate \(0<p<p_{\rm RG}\). Let \(\alpha>0\) be the overhead exponent appearing in the universal single-shot conversion of Yuan.

For every fixed \(s,r\ge0\), there is a constant \(K>0\) such that the choice
\[
m_n=\left\lceil K(\log n)^{1/\alpha}\right\rceil
\]
produces output CSS QLDPC codes
\[
\widetilde{\mathcal C}_n=[[N_n,k_n]],\qquad N_n=nm_n,
\]
for which the published single-shot decoder obeys
\[
P_{\rm fail}(T_n)\le n^{-r}
\]
for every \(T_n\le n^s\) and all sufficiently large \(n\). In terms of the total output length,
\[
k_n=\Theta\!\left(\frac{N_n}{(\log N_n)^{1/\alpha}}\right),
\qquad
\frac{k_n}{N_n}=\Theta\!\left((\log N_n)^{-1/\alpha}\right),
\]
and the local decoder has parallel running time \(O(\log\log N_n)\).

Thus Yuan's transformation, applied to an arbitrary positive-rate bounded-degree seed family, has an explicit family-level operating regime with polynomially many noisy correction rounds, polynomially small logical failure, and only polylogarithmic spatial-rate loss.

## Assumptions and scope
The seed family is CSS QLDPC with check weights and qubit degrees bounded uniformly in \(n\), so the constants in the source theorem can be chosen uniformly along the family. The noise rate \(p\) is fixed strictly below the source threshold \(p_{\rm RG}\). The constants \(s\) and \(r\) are fixed and nonnegative. The logarithm base is immaterial because it changes only the constant \(K\).

The claim uses the universal conversion in arXiv:2610.02137v1, which maps an \([[n,k]]\) CSS QLDPC code to an \([[nm,k]]\) CSS QLDPC code, preserves bounded check weight and qubit degree up to absolute constants, and gives a local decoder with parallel time \(O(\log m)\).

## Proof
For fixed \(p<p_{\rm RG}\), the source bound
\[
P_{\rm fail}(T)\le O(Tn)\left(\frac{p}{p_{\rm RG}}\right)^{\Omega(m^\alpha)}
\]
can be written, for positive constants \(C,c\) independent of \(n,m,T\), as
\[
P_{\rm fail}(T)\le CTn\exp(-cm^\alpha).
\]
Choose \(K\) so that
\[
cK^\alpha>s+r+1.
\]
For \(T_n\le n^s\) and \(m_n=\lceil K(\log n)^{1/\alpha}\rceil\), one has \(m_n^\alpha\ge K^\alpha\log n\), hence
\[
P_{\rm fail}(T_n)
\le Cn^{s+1-cK^\alpha}.
\]
The exponent is strictly smaller than \(-r\), so the fixed prefactor \(C\) is absorbed for all sufficiently large \(n\), proving \(P_{\rm fail}(T_n)\le n^{-r}\).

Because \(k_n/n\to R>0\), one has \(k_n=\Theta(n)\). Also
\[
m_n=\Theta((\log n)^{1/\alpha}),
\qquad
N_n=nm_n.
\]
Therefore
\[
\log N_n=\log n+O(\log\log n),
\]
so \(\log N_n/\log n\to1\), and consequently
\[
m_n=\Theta((\log N_n)^{1/\alpha}).
\]
Substitution into \(k_n=\Theta(N_n/m_n)\) gives the stated logical-dimension and rate laws. Finally, the source decoder time \(O(\log m_n)\) becomes \(O(\log\log N_n)\).

## Verification
The proof is symbolic and does not depend on finite enumeration or numerical fitting. The only asymptotic conversion is \(\log N_n=\log n+O(\log\log n)\), which follows directly from the chosen polylogarithmic \(m_n\). The failure estimate retains an explicit strict exponent margin before absorbing the constant prefactor.

The primary source was inspected at its main result and literature-comparison sections. Its stated output parameters, stochastic failure bound, bounded-degree preservation, and decoder-time bound are exactly the premises used here.

## Relationship to prior work
Yuan proves the universal \([[n,k]]\) to \([[nm,k]]\) CSS QLDPC transformation and its finite-parameter stochastic failure estimate. The paper emphasizes that constant-rate seed QLDPC families exist and that its construction preserves the number of logical qubits, but it does not state the family-level specialization above: a polylogarithmic overhead choice giving \(k_n=\Theta(N_n/(\log N_n)^{1/\alpha})\), polynomial reliability over polynomially many rounds, and \(O(\log\log N_n)\) decoder time.

Campbell's earlier universal single-shot result allows arbitrary codes but can require nonlocal, high-weight measurement checks and is formulated for adversarial-noise soundness rather than the stochastic-threshold guarantee used here. Yuan explicitly identifies this distinction. The recent passive self-correcting construction of Balasubramanian, Davydova, and Lin is an important precursor to Yuan's recursive mechanism, but it addresses a passive three-dimensional memory rather than this family-level active single-shot rate-reliability specialization.

## Limitations
The result is a sufficient corollary of the published upper bound on failure probability. It does not prove that \(m_n=\Theta((\log n)^{1/\alpha})\) is necessary, that the resulting rate is optimal, or that the source exponent \(\alpha\) is sharp. It does not claim a distance law for the transformed codes. If the seed already has a stronger single-shot decoder, Yuan's enhancement theorem can yield stronger suppression than the bare universal guarantee analyzed here.

## References
Andrew C. Yuan, "One-Shot any Code," arXiv:2610.02137v1, 2026.

Earl T. Campbell, "A theory of single-shot error correction for adversarial noise," arXiv:1805.09271v6, 2019.

Shankar Balasubramanian, Margarita Davydova, and Ting-Chun Lin, "A passive self-correcting quantum memory in three dimensions," arXiv:2605.10943v1, 2026.

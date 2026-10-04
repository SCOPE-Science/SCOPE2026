# Exact nonvanishing phase-retrieval fibers for an even two-point cyclic STFT window
## Finding
Let \(N\ge 4\), let \(a\in\mathbb Z_N\setminus\{0\}\), put \(d=\gcd(a,N)\) and \(L=N/d\), and assume that \(L\ge 4\) is even. For the two-point window \(g_a=\delta_0+\delta_a\), consider the full set of cyclic STFT magnitudes \(|V_{g_a}f(x,\ell)|\).

Partition \(\mathbb Z_N\) into the \(d\) cycles of the permutation \(x\mapsto x+a\). Each cycle has even length \(L\), hence a canonical bipartition after a starting point is chosen. For every signal \(f\in\mathbb C^N\) with \(f_x\ne0\) for all \(x\), the complete measurement fiber is as follows. On each step cycle, one may always multiply by an arbitrary unimodular scalar. In addition, if and only if the magnitudes of \(f\) are constant values \(A\) and \(B\) on the two parity classes of that cycle, one may swap the two levels by multiplying the first class by \(B/A\) and the second by \(A/B\). If \(A=B\), this is the identity; if \(A\ne B\), it is the unique nontrivial extra ambiguity on that cycle. There are no other signals with the same STFT magnitude.

Consequently, a full-support signal is phase retrievable up to a single global phase precisely when \(d=1\) and its magnitudes do not alternate between two distinct constants around the step-\(a\) cycle.
## Assumptions and scope
The cyclic STFT convention is
\[
V_gf(x,\ell)=\sum_{j\in\mathbb Z_N}f_j\overline{g_{j-x}}e^{-2\pi i j\ell/N}.
\]
The theorem concerns full-support signals and the fixed window \(g_a=\delta_0+\delta_a\). The step order \(L=N/\gcd(a,N)\) is assumed even and at least \(4\). The order-two case is excluded because the two nonzero Fourier coefficients used below coalesce when \(a\equiv-a\pmod N\). Signals containing zeros are not classified here.
## Proof
For \(g_a=\delta_0+\delta_a\), a time slice has exactly two terms:
\[
V_{g_a}f(x,\ell)=e^{-2\pi i x\ell/N}\left(f_x+f_{x+a}e^{-2\pi i a\ell/N}\right).
\]
Therefore
\[
|V_{g_a}f(x,\ell)|^2=|f_x|^2+|f_{x+a}|^2+f_x\overline{f_{x+a}}e^{2\pi i a\ell/N}+\overline{f_x}f_{x+a}e^{-2\pi i a\ell/N}.
\]
Because \(L\ge4\), the characters indexed by \(a\) and \(-a\) are distinct. Taking the discrete Fourier transform in \(\ell\) therefore recovers, for every \(x\), both
\[
s_x=|f_x|^2+|f_{x+a}|^2
\quad\text{and}\quad
c_x=f_x\overline{f_{x+a}}.
\]

Let \(\widetilde f\) have the same STFT magnitude. Since \(c_x\ne0\), it is also full-support. Put \(q_x=\widetilde f_x/f_x\). Equality of the recovered products gives
\[
q_x\overline{q_{x+a}}=1,
\]
so along each step cycle all \(q_x\) have one common argument and their moduli alternate between some \(r>0\) and \(r^-1\). Thus the only possible non-global freedom on a cycle is an alternating positive rescaling.

Equality of the recovered sums gives, on an edge whose first endpoint carries modulus multiplier \(r\),
\[
r^2|f_x|^2+r^{-2}|f_{x+a}|^2=|f_x|^2+|f_{x+a}|^2.
\]
After multiplication by \(r^2\), this is
\[
(r^2-1)\left(r^2|f_x|^2-|f_{x+a}|^2\right)=0.
\]
If \(r=1\), the competitor differs only by the cycle phase. If \(r\ne1\), then every edge from the first parity class to the second satisfies \(|f_{x+a}|^2=r^2|f_x|^2\), while every following edge forces the next first-class magnitude to equal the preceding first-class magnitude. Going around the cycle shows that all first-class magnitudes equal one value \(A\) and all second-class magnitudes equal one value \(B=rA\). The competitor then multiplies the first class by \(B/A\) and the second by \(A/B\), which swaps those magnitudes.

Conversely, when a cycle has alternating constant magnitudes \(A,B\), this swap preserves every product \(c_x\) and every sum \(s_x\), hence preserves every STFT intensity slice by the displayed Fourier expansion. The classification is independent across the \(d\) disjoint step cycles. A single global phase is therefore the entire fiber exactly when there is only one step cycle and its two parity classes do not carry distinct constant magnitudes.
## Verification
The proof is algebraic and does not depend on finite experimentation. The bundled script `verify_two_point_phase_fibers.py` provides an exact rational-arithmetic cross-check. For every \(4\le N\le120\) and every nonzero step \(a\) whose order is even and at least \(4\), it checks that the intensity of each two-term slice has exactly the three expected character coefficients, constructs alternating two-level signals on every step cycle, verifies the level-swap invariance coefficient-by-coefficient, and checks that perturbing one same-parity magnitude removes the nontrivial alternating modulus solution. The replay performs \(400616\) exact checks across \(5856\) swap cycles and ends with `VERIFY_OK`.
## Relationship to prior work
Bojarovska and Flinth proved general Gabor phase-retrieval criteria and, for nonvanishing signals, a weaker sufficient ambiguity-function condition. Their nonvanishing criterion requires the relevant ambiguity samples at shifts \(0\) and \(1\) to be nonzero. For the equal two-point window at even step order, the zero-shift ambiguity contains a factor of the form \(1+e^{-2\pi i a\ell/N}\) and therefore vanishes at a half-cycle character, so that criterion does not decide the present case.

Jaganathan, Eldar, and Hassibi proved almost-sure uniqueness for nonvanishing signals under overlapping short-time windows. The alternating two-level family above is an explicit description of the exceptional measure-zero fiber geometry for the equal two-point cyclic window, rather than another generic uniqueness statement.

Bartusel later gave broad injectivity criteria for STFT phase retrieval on cyclic groups and emphasized cases where the window ambiguity function has zeros. The complete finite-dimensional short-window results in that work concern separated signal classes; the paper also records the prior almost-all result for nonvanishing signals. The present theorem instead classifies every full-support signal for this degenerate equal two-point window at even step order and identifies the exact exceptional set and its complete fiber.
## Limitations
The order-two step case \(L=2\) is excluded because the \(a\) and \(-a\) character coefficients coincide, so the edge product is not individually recoverable by this argument. Signals with zeros can have additional support-induced ambiguities and are outside the claim. The literature search found no equivalent exact exceptional-set classification, but an unindexed or differently phrased prior derivation remains possible.
## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first posted 19 March 2015; Journal of Fourier Analysis and Applications 22 (2016), DOI 10.1007/s00041-015-9431-0.
2. K. Jaganathan, Y. C. Eldar, and B. Hassibi, *STFT Phase Retrieval: Uniqueness Guarantees and Recovery Algorithms*, arXiv:1508.02820v1, first posted 12 August 2015; IEEE Journal of Selected Topics in Signal Processing 10 (2016), DOI 10.1109/JSTSP.2016.2549507.
3. D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on Z, Z_d and R^d*, Journal of Fourier Analysis and Applications 29 (2023), article 53, DOI 10.1007/s00041-023-10026-2.

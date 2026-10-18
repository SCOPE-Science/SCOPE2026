# The sign-character phase transition in packet-reversal overhand shuffles

## Finding

Fix an integer \(n\ge2\) and a cut probability \(0<p<1\), and write \(q=1-p\). Independently cut each of the \(n-1\) gaps of a deck with probability \(p\), and reverse every resulting contiguous packet in place. Let \(R\) be the resulting random permutation, and write \(\varepsilon_n(p)=\mathbb E[\operatorname{sgn}(R)]\). For convenience extend this notation by \(\varepsilon_0(p)=\varepsilon_1(p)=1\).

**Theorem.** For every \(0<p<1\), the complete sign-character eigenvalue sequence has generating function and recursion
\[
\sum_{n\ge0}\varepsilon_n(p)z^n
=\frac{1+qz}{1-pz+qz^2},\qquad
\varepsilon_n(p)=p\varepsilon_{n-1}(p)-q\varepsilon_{n-2}(p)\quad(n\ge2).
\]
There is a sharp parameter threshold
\[
p_*=2(\sqrt2-1).
\]
If \(p\ge p_*\), then \(\varepsilon_n(p)>0\) for **every** \(n\ge2\). At equality the exact formula is
\[
\varepsilon_n(p_*)=(\sqrt2-1)^n(1+\sqrt2\,n).
\]
If \(0<p<p_*\), the sequence \(\varepsilon_n(p)\) takes strictly positive and strictly negative values **infinitely often** as \(n\) grows. Thus the direction of the single-pass even-versus-odd bias oscillates with deck size exactly below this threshold.

For the Markov chain on permutations obtained by independent passes, the sign character \(\chi(\sigma)=\operatorname{sgn}(\sigma)\) is an exact eigenfunction with eigenvalue \(\varepsilon_n(p)\). Starting from an even deck, after each integer \(t\ge0\) passes,
\[
\Pr\{\text{even parity after }t\text{ passes}\}
=\tfrac12\bigl(1+\varepsilon_n(p)^t\bigr).
\]
Consequently the projected parity law has total-variation distance exactly \(\lvert\varepsilon_n(p)\rvert^t/2\) from the parity of a uniform permutation; the full-deck total-variation distance is **at least**, not necessarily equal to, this quantity. The conventional physical packet-order reversal differs by a whole-deck reversal, so its parity eigenvalue is \((-1)^{n(n-1)/2}\varepsilon_n(p)\).

## Assumptions and scope

A cut after each of the \(n-1\) gaps is an independent Bernoulli event with success probability \(p\), all independent between passes. Packet-reversal keeps packet positions and reverses card order inside each packet. The random walk acts on the full symmetric group by multiplying by this independent random permutation. The parameter \(p\) is fixed for each assertion about varying deck size; formulas for finite \(n\) do not require any asymptotic regime. The zero-card coefficient is an auxiliary generating-function convention, not an assertion about a shuffle with no cards.

## Proof

**1. Packet sign and first-packet decomposition.** Reversing a packet of length \(\ell\) makes \(\ell(\ell-1)/2\) inversions. Its sign is
\[
s_\ell=(-1)^{\ell(\ell-1)/2}=(-1)^{\lfloor\ell/2\rfloor}.
\]
Disjoint packet reversals multiply their signs. The weight of a first packet of length \(\ell\), with no cut inside it, is \(q^{\ell-1}\). Introduce the formal power series
\[
A(z)=\sum_{\ell\ge1}s_\ell q^{\ell-1}z^\ell
=\frac{z(1-qz)}{1+q^2z^2},
\]
where the equality follows by grouping the repeating sign pattern \((+,-,-,+)\) in blocks of four. For a nonempty deck, either there is no cut (contribution \(A(z)\)) or the first packet ends with a cut and is followed by a nonempty residual deck (contribution \(pA(z)(F(z)-1)\)), where \(F(z)=\sum_{n\ge0}\varepsilon_n(p)z^n\). Including the empty auxiliary deck,
\[
F(z)=1+A(z)+pA(z)(F(z)-1)
=\frac{1+qA(z)}{1-pA(z)}.
\]
Substitution and \(p+q=1\) give \(F(z)=(1+qz)/(1-pz+qz^2)\). Coefficient comparison gives both starting values and the exact recursion.

**2. Real-root regime.** The characteristic equation is \(r^2-pr+q=0\), with discriminant \(\Delta=p^2-4q\). The unique zero of \(\Delta\) inside \((0,1)\) is \(p_*\). If \(p>p_*\), put \(r_\pm=(p\pm\sqrt\Delta)/2\). Then \(0<r_-<r_+<1\) and
\[
\varepsilon_n(p)=
\frac{(1-r_-)r_+^n-(1-r_+)r_-^n}{r_+-r_-}>0
\quad(n\ge0),
\]
since both factors in the first positive product are strictly greater than their counterparts in the second. At \(p=p_*\), the repeated root is \(r=\sqrt2-1\) and the starting values give \(\varepsilon_n=r^n(1+n(1/r-1))=r^n(1+\sqrt2 n)>0\).

**3. Complex-root regime.** If \(0<p<p_*\), write the characteristic roots as \(\sqrt q\,e^{\pm i\theta}\), with \(0<\theta<\pi/2\) determined by \(\cos\theta=p/(2\sqrt q)\). The two starting values yield
\[
\varepsilon_n(p)=q^{n/2}\left[\cos(n\theta)+c\sin(n\theta)\right],\qquad
c=\frac{1/\sqrt q-\cos\theta}{\sin\theta}>0.
\]
The bracket is a nonzero scalar multiple of \(\cos(n\theta-\phi)\). If \(\theta/(2\pi)\) is irrational, the orbit of angles is dense in the circle and visits open arcs where this cosine is strictly positive and strictly negative infinitely often. If it is rational, the bracket sequence is periodic and its sum over a full period is zero, because \(e^{i\theta}\ne1\); its value at index zero is \(1\), so a strictly negative term must occur in the period. Repeating the period supplies infinitely many positive and negative terms. This proves the sharp dichotomy, including rational resonances.

**4. Character dynamics and physical convention.** Since the sign is multiplicative, for every state \(\sigma\),
\[
\mathbb E[\chi(\sigma R)\mid\sigma]
=\chi(\sigma)\varepsilon_n(p).
\]
For independent passes starting at an even state, their signs multiply and have mean \(\varepsilon_n(p)^t\); for a random variable taking values \(\pm1\), the probability of \(+1\) is half of one plus its mean. The uniform law on the symmetric group assigns parity probability \(1/2\) for \(n\ge2\), and data processing under the parity map proves the full-deck total-variation lower bound. In the physical convention, the packet-reversal permutation is followed by deterministic full-deck reversal \(J\), whose sign is \((-1)^{n(n-1)/2}\), producing the claimed correction.

**5. Scale separation.** For each fixed \(0<p<1\), both characteristic roots have modulus strictly less than one: in the complex regime their modulus is \(\sqrt q\), and in the real regime the dominant root is \(r_+<1\). The repeated-root expression also tends to zero exponentially up to the explicit linear prefactor. Hence \(\lvert\varepsilon_n(p)\rvert\to0\) exponentially fast in \(n\) (with a linear prefactor at \(p=p_*\)). In particular, parity is asymptotically fair after one pass, despite the established \(n^2\log n\) scale for full-deck mixing.

## Verification

The accompanying standalone `check.py` enumerates every cut configuration for all deck sizes \(1\le n\le12\) at each of four rational probabilities \(p\in\{1/4,1/2,3/4,9/10\}\), constructs the resulting permutation explicitly, calculates its inversion parity, and compares the exact rational weighted sum to the recurrence. **All 48 full-enumeration identities passed.** Further exact checks examine sign reversal at \(p=3/4\), sustained positivity at \(p=9/10\), eigenvalue bounds and finite-pass parity formulas. These are finite consistency tests; the theorem for all deck sizes and all cut probabilities follows from the preceding proof, not extrapolation from the tests.

## Relationship to prior work

Yunjiang Jiang, *Cutoff for the Overhand Shuffle* (first posted September 10, 2026, arXiv:2610.00137v1), studies precisely the independent-gap packet-reversal model, obtains total-variation cutoff and an exact **one-card** cosine spectrum. Neither its full-deck cutoff nor its one-card eigenvalues identify the distinct sign-character eigenvalue, exact parity law, or its sharp oscillatory threshold. Johan Jonasson, *The overhand shuffle mixes in \(\Theta(n^2\log n)\) steps* (2006; arXiv:math/0501401), treats the same packet convention and proves a mixing-time order result, not the stated sign-eigenvalue classification. The universal representation-theoretic observation that sign is an eigenfunction of a convolution chain does not, without evaluating its expectation, yield this model-specific generating function or phase boundary.

## Limitations

This is an exact statement about the **parity projection**, not an upper bound on full-deck mixing or a determination of the entire spectrum. The phase dichotomy for the sign of parity bias applies directly to the in-place packet-reversal convention; physical packet-order reversal adds an explicit deck-size-dependent sign factor. The assertions on infinitely many sign changes take \(p\) fixed while deck size tends to infinity. The result does not treat correlated cuts, nonidentically distributed gaps, or other packet operations. A broader historical character-spectrum identity might encompass this calculation; independent priority review has not been performed.

## References

1. Yunjiang Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1 (initial public submission September 10, 2026), https://arxiv.org/html/2610.00137v1.
2. Johan Jonasson, *The overhand shuffle mixes in \(\Theta(n^2\log n)\) steps*, Annals of Applied Probability 16 (2006), 241–243; arXiv:math/0501401, https://arxiv.org/abs/math/0501401.
3. Robin Pemantle, *Randomization time for the overhand shuffle*, Journal of Theoretical Probability 2 (1989), 37–49 (historical model and mixing bounds; full text not inspected).

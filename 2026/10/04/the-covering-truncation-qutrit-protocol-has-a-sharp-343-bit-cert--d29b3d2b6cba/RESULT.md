# The covering–truncation qutrit protocol has a sharp 343-bit certified bound

## Finding
For the exact qutrit-simulation construction introduced by de Gois, Santos, and Vieira, allow the covering radius and fallback interval to vary as in their optimization remark. Retaining their universal covering estimate and their fallback architecture, the sharp whole-bit bound certified by this parameterized proof family is 343 bits.

An explicit attaining choice is
\[
r^2=\frac{7}{120},\qquad L=\frac{32}{45},\qquad U=\frac{23}{30},\qquad N=107,\qquad n=27.
\]
For this choice the qutrit protocol is exact for arbitrary finite-outcome POVMs and has message dimension at most
\[
4702\,4809^{27}<2^{343}.
\]
The same message bound therefore applies, through the communication-to-Bell reduction in the source, to arbitrary finite-outcome bipartite correlations whenever the receiving subsystem is a qutrit.

No admissible parameter choice in this same proof family, when the only covering input is \(K_{\mathrm{cover}}\le(2/r)^4\), can certify a 342-bit bound.

## Assumptions and scope
The claim concerns the parameterized version of the source construction, not the unknown optimal classical simulation cost of a qutrit. Let \(s=r^2\), take a covering radius \(0<r<1/\sqrt{8}\), and a fallback interval \([L,U]\) satisfying \(2/3<L<U\le1-4r^2\). The lower restriction \(L>2/3\) ensures a strictly positive uniform lower bound on the fallback POVM weight. The only covering-number input used is the source lemma \(K_{\mathrm{cover}}\le(2/r)^4\).

For these parameters, the fallback weight is
\[
\eta=12r^4(U-L),
\]
and the binary truncation length \(N\) must satisfy
\[
\left(1-\frac{1-\eta}{18}\right)^N<\eta.
\]
For the multi-outcome protocol, if \(\varepsilon=(3/4)^n\), the source positivity argument carries through whenever
\[
\varepsilon<\eta\left(3-\frac{2}{L}\right)
\quad\text{and}\quad
\varepsilon<\frac14.
\]
These are sufficient conditions for the same exactness proof; no claim is made that every possible modification of the protocol must satisfy them.

## Proof
First consider the displayed attaining parameters. Since \(U=1-4r^2\), two rays in one covering ball have squared overlap strictly larger than \(U\), so the fallback set remains inside the original acceptance set exactly as required in the source construction. The universal covering estimate gives
\[
K_{\mathrm{cover}}\le\left(\frac2r\right)^4
=\frac{230400}{49}<4703.
\]
Because the covering number is an integer, \(K_{\mathrm{cover}}\le4702\).

The generalized fallback weight is
\[
\eta=12\left(\frac7{120}\right)^2
\left(\frac{23}{30}-\frac{32}{45}\right)
=\frac{49}{21600}.
\]
The probability that one coordinate is not eligible for the truncated branch is therefore \(1-(1-\eta)/18\). Exact integer arithmetic gives
\[
\left(1-\frac{1-\eta}{18}\right)^{107}
<\eta,
\]
so \(N=107\) makes the source correction probability valid.

For the multi-outcome fallback, put \(\beta=1-\alpha\). The source identity
\[
1\le W+\beta(3-W)
\]
implies
\[
W\ge\frac{1-3\beta}{1-\beta}.
\]
Since \(\alpha\ge L=32/45\), one has \(\beta\le13/45\), and hence
\[
W\ge3-\frac2L=\frac3{16}.
\]
With \(n=27\),
\[
\varepsilon=\left(\frac34\right)^{27}
<\eta\frac3{16}=\frac{49}{115200},
\]
and also \(\varepsilon<1/4\). Thus the corrected weights in the multi-outcome decoder stay nonnegative and their total mass is below four, so the source validity and exactness calculation applies unchanged. The message alphabet obeys
\[
d_C\le4702(107+4702)^{27}=4702\,4809^{27}<2^{343},
\]
which proves the 343-bit upper bound.

It remains to show that 342 bits cannot be certified anywhere in this parameterized family from the same covering estimate. Increasing \(U\) can only increase \(\eta\), so for lower-bound purposes set \(U=1-4s\). For fixed \(s\), maximizing \(\eta(3-2/L)\) over \(L\) gives
\[
T(s)=12s^2\left(3A+2-2\sqrt{6A}\right),\qquad A=1-4s.
\]
A convenient reparametrization is \(y=\sqrt{6A}\), for which
\[
T(s)=\frac{((6-y^2)(y-2))^2}{96}.
\]
For \(s\ge6/125\), one has \(y<221/100\) and \(-3y^2+4y+6>0\); hence \(T(s)\) is decreasing on that range.

Two global lower bounds are also useful. First,
\[
\eta\le4s^2(1-12s)\le\frac1{243},
\]
and the binary truncation inequality cannot hold with \(N\le96\); therefore every admissible member has \(N\ge97\). Second, writing \(x=L-2/3\) and \(d=1/3-4s\),
\[
\eta\left(3-\frac2L\right)
\le54s^2x(d-x)
\le\frac{27}2s^2d^2
\le\frac1{1536}
<\left(\frac34\right)^{25},
\]
so every admissible multi-outcome construction has \(n\ge26\).

The remaining possibilities are separated by four exact threshold checks. Monotonicity of \(T\) and exact algebraic comparison give
\[
\begin{aligned}
T(6/125)&< (3/4)^{26},\\
T(293/5000)&< (3/4)^{27},\\
T(8/125)&< (3/4)^{28},\\
T(27/400)&< (3/4)^{29}.
\end{aligned}
\]
Consequently, if \(n=26,27,28,29\), respectively, then \(s\) is below the corresponding threshold, forcing the covering bounds \(K\ge6944,4659,3906,3511\). Together with \(N\ge97\), exact integer comparisons give
\[
\begin{aligned}
6944(6944+97)^{26}&>2^{342},\\
4659(4659+97)^{27}&>2^{342},\\
3906(3906+97)^{28}&>2^{342},\\
3511(3511+97)^{29}&>2^{342}.
\end{aligned}
\]
If \(n\ge30\), then \(s<1/12\) implies \(K\ge2304\), and already \(2304(2304+97)^{30}>2^{342}\). Hence no admissible member of the stated parameterized proof family certifies 342 bits.

## Verification
The accompanying `verify.py` uses exact rational and integer arithmetic. It checks the attaining parameters, the binary and multi-outcome inequalities, the 343-bit alphabet bound, the global bounds \(N\ge97\) and \(n\ge26\), the four algebraic threshold comparisons after sign-controlled squaring, and all five integer lower bounds that exclude 342 bits. Running it prints `VERIFY_OK`.

## Relationship to prior work
De Gois, Santos, and Vieira prove finite exact qutrit simulation and give the explicit 357-bit bound. Their Remark D.5 introduces variable covering radius \(r\) and fallback interval \([L,U]\), derives \(\eta=12r^4(U-L)\), and states that improving the communication bound requires balancing the covering size against truncation length, but they do not carry out the optimization. Their multi-outcome section fixes the original parameters and uses 26 copies.

Earlier 2026 work by Schlösser and Kleinmann still treated finiteness of the qutrit cost as unknown and supplied lower bounds for restricted qutrit scenarios. Zartab, Gasbarri, Sentís, and Muñoz-Tapia developed approximate higher-dimensional simulations rather than an exact finite qutrit protocol. The present result is therefore a quantitative refinement of the September 2026 exact construction, together with an optimality statement restricted to its stated covering/truncation proof family and universal cover estimate.

## Limitations
The 343-bit number is not claimed to be the true classical simulation cost \(C_{\mathrm{cl}}(3)\). A better covering of \(\mathbb{CP}^2\), a different fallback architecture, a different binarization, variable-length coding, or an unrelated protocol could improve it. The lower-bound part proves only that 342 bits cannot be certified inside the explicitly stated parameterized family when the covering cardinality is controlled solely by \(K_{\mathrm{cover}}\le(2/r)^4\). The primary September 2026 source is a preprint.

## References
1. C. de Gois, T. S. R. Santos, and C. Vieira, “Quantum communication and Bell nonlocality require infinite classical communication to simulate,” arXiv:2609.04182v1 (2026).
2. S. Schlösser and M. Kleinmann, “Bounding the classical cost of simulating quantum behaviors in the prepare-and-measure scenario,” arXiv:2603.01255 (2026).
3. M. Zartab, G. Gasbarri, G. Sentís, and R. Muñoz-Tapia, “Prepare-and-measure and entanglement simulation beyond qubits,” Scientific Reports 16, 21297 (2026); arXiv:2508.02377.

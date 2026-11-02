# Sharp affine-codebook random access and rigidity of bent worst-case inputs

## Finding

For every even integer \(m\ge 2\), write \(N=2^m\). Consider binary random access from an arbitrary \(N\)-bit truth table \(B=(B_x)_{x\in\mathbb F_2^m}\) into a randomized \((m+1)\)-bit message \((a,b)\in\mathbb F_2^m\times\mathbb F_2\), with the **fixed affine decoder** \(D_x(a,b)=a\cdot x+b\pmod 2\). The encoder may choose any input-dependent probability distribution on the messages, without shared randomness.

The exact maximum worst-case coordinate recovery probability is
\[
\boxed{\sup_{\pi}\inf_{B,x}\Pr_{(a,b)\sim\pi_B}[D_x(a,b)=B_x]=\frac12+\frac{1}{2\sqrt N}.}
\]
Here \(\pi\) ranges over all randomized encoders, and each \(\pi_B\) is a distribution on the entire affine-message alphabet.

For any input \(B\), the optimal encoder's worst-coordinate recovery probability equals this global minimum **if and only if** \(B\) is a bent Boolean function (equivalently, every Walsh coefficient of its sign table has magnitude \(\sqrt N\)). At each such worst-case input, the optimal distribution over the \(2N\) affine messages is **unique**: it assigns probability \(1/N\) to each of the \(N\) affine words positively correlated with \(B\), and zero to every other affine word. These statements concern the fixed decoder and do not assert optimality among arbitrary decoders.

## Assumptions and scope

All inner products and affine evaluations are over \(\mathbb F_2\). The bit positions are indexed by the entire cube \(\mathbb F_2^m\), including the zero position; the message alphabet consists of all affine functions, with no puncturing. No shared randomness, noiseless communication, and independent fresh encoder randomness per use are assumed. The decoder does not depend on \(B\) and is not optimized.

Define \(s_x=(-1)^{B_x}\) and \(\chi_a(x)=(-1)^{a\cdot x}\). Let
\[
W_a=\sum_{x\in\mathbb F_2^m}s_x\chi_a(x),\qquad S=\sum_{a\in\mathbb F_2^m}|W_a|.
\]
The Walsh matrix \(H=(\chi_a(x))_{x,a}\) satisfies \(H^TH=NI\), so \(\sum_aW_a^2=N^2\) and \(N\le S\le N\sqrt N\).

## Proof

**Construction and universal lower bound.** Since \(S>0\), for any \(B\) select \(a\) with probability \(|W_a|/S\), and choose \(b\) so that \((-1)^b=\operatorname{sgn}(W_a)\). Coefficients equal to zero receive zero probability and can use either sign. The expectation of the decoded sign at any \(x\) is
\[
\mathbb E[(-1)^{D_x(a,b)}]=\frac1S\sum_aW_a\chi_a(x)=\frac NSs_x,
\]
by inverse Walsh orthogonality. Thus **every coordinate** succeeds with probability \((1+N/S)/2\). By Cauchy–Schwarz and Parseval, \(S\le N\sqrt N\), proving universal success at least \(\frac12+\frac1{2\sqrt N}\). If \(B\) is not bent, equality in Cauchy–Schwarz fails, so this explicit encoder gives a strictly larger probability at every coordinate.

**Bent upper bound.** For even \(m\), the Boolean quadratic
\[
Q(x)=\sum_{j=1}^{m/2}x_{2j-1}x_{2j}\pmod 2
\]
is bent. Indeed, the Walsh sum factors into \(m/2\) two-bit factors, each equal to \(\pm 2\), so \(|W_a|=2^{m/2}=\sqrt N\) for every \(a\). The argument below applies to every bent \(B\).

Let an arbitrary encoder assign probabilities \(p_{a,b}\), and put \(t_a=p_{a,0}-p_{a,1}\). Then \(\sum_a|t_a|\le1\), and its decoded sign expectations are \(y_x=\sum_at_a\chi_a(x)\). For a bent input,
\[
\frac1N\sum_xs_xy_x=\frac1N\sum_aW_at_a\le\frac1{\sqrt N}\sum_a|t_a|\le\frac1{\sqrt N}.
\]
Consequently, at least one coordinate has signed correlation \(s_xy_x\le1/\sqrt N\), so its success probability is at most \(\frac12+\frac1{2\sqrt N}\). This matches the construction. Since nonbent inputs achieve strictly better, the globally hardest tables are precisely the bent functions.

**Unique encoder on every hardest input.** At a bent input, an optimal encoder must have signed correlation at least \(1/\sqrt N\) at *every* coordinate. The displayed average bound forces \(s_xy_x=1/\sqrt N\) for all \(x\). Inverting the Walsh transform gives
\[
t_a=\frac{W_a}{N\sqrt N}=\frac{\operatorname{sgn}(W_a)}N\qquad\text{for all }a.
\]
All \(N\) absolute differences \(|t_a|\) equal \(1/N\), so their sum is one. But \(\sum_{a,b}p_{a,b}=1\), and \(|p_{a,0}-p_{a,1}|\le p_{a,0}+p_{a,1}\). Hence equality holds termwise: for each \(a\), the unique permitted \(b\) is the one whose sign matches \(W_a\), and its probability is exactly \(1/N\). No other optimal distribution is possible.

## Verification

The included standalone \(\texttt{verify.py}\) uses only exact Python integer arithmetic. It computes the fast Walsh transform, checks Parseval and inverse-transform identities, and verifies the quadratic bent spectrum for \(m=2,4,6,8\). It exhaustively checks all \(2^{2^m}\) truth tables for \(m=2\) and \(m=4\), finding exactly \(8\) and \(896\) maximizers of Walsh \(\ell_1\) norm, respectively, as expected for bent functions. The recorded execution ends with \(\texttt{AFFINE_RAC_VERIFY_OK}\). These finite checks are corroboration, not a substitute for the all-\(m\) algebraic proof.

To reproduce, use a standard Python 3 interpreter: `python verify.py`. No external dependencies are required. The randomized encoder itself is constructed using a fast Walsh–Hadamard transform in \(O(N\log N)\) arithmetic operations followed by weighted sampling.

## Relationship to prior work

Kondo, Sato, Yano, Maeda, Ito and Yamamoto (arXiv:2604.21274, first public April 23, 2026) formulate classical worst-case random-access optimization geometrically and solve the **punctured simplex** decoder case with \(2^k-1\) inputs and \(k\)-bit messages. Their Theorem 17 uses Walsh orthogonality but not the full affine Reed–Muller codebook of length \(2^m\) with \(m+1\) message bits, nor the bent-input and unique-mixture theorem here. The geometric framework is a starting point, not claimed as new.

The Walsh spectrum and covering-radius extremality of bent functions, and their role as worst-case received words for first-order Reed–Muller list decoding, were known long before this result. In particular, Dumer and collaborators' 2007 work studies list sizes in Hamming balls. The novelty claimed here is restricted to the exact fixed-decoder random-access minimax objective, its full extremal-input characterization and unique optimal stochastic affine encoder; **not** to the classical existence or spectrum of bent functions.

Kondo and Maeda (arXiv:2610.38429, dated October 28, 2026) subsequently describe a generic orthogonal-array random-access encoder; that construction does not determine this affine-codebook minimax value or encoder rigidity.

## Limitations

The decoder's affine truth table is fixed. The result makes no assertion that the probability above is optimal for unrestricted \((N,m+1)\) random access codes with other deterministic or randomized decoders. The full set of optimal encoders for *nonbent* inputs is not characterized. Bent existence and the numerical Walsh \(\ell_1\) extremum are classical; publication-priority risk remains for the random-access reformulation and uniqueness statement. No independent mathematical audit has been performed.

## References

- R. Kondo, Y. Sato, H. Yano, Y. Maeda, K. Ito, and N. Yamamoto, *Random Access Codes: Explicit Constructions, Optimality, and Classical-Quantum Gaps*, arXiv:2604.21274 (first public April 23, 2026), especially geometric optimization and Theorem 17. https://arxiv.org/abs/2604.21274
- I. Dumer et al., *List decoding of the first-order binary Reed–Muller codes*, *Problems of Information Transmission* **43** (2007), Section 4 on maximal lists and bent functions.
- The established Walsh-flatness characterization of bent functions, e.g. the reference compilation at https://boolean.wiki.uib.no/Bent_Boolean_Functions (background, not new).

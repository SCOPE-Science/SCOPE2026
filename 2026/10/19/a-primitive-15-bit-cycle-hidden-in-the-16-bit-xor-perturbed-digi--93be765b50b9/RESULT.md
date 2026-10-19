# A primitive 15-bit cycle hidden in the 16-bit XOR-perturbed digital tent map

## Finding

The bit-level perturbation proposed by Nardo, Nepomuceno, Muñoz, Butusov and Arias-Garcia for the digital tent map is a linear map over \(\mathbb F_2\), despite its presentation as a branch-dependent chaotic map. For any word length \(k\ge3\), every state becomes periodic in **at most one iteration**: the periodic states are exactly the codimension-one parity hyperplane of states whose last three bits sum to zero in \(\mathbb F_2\). Each periodic state has precisely one additional, nonperiodic predecessor.

For the published \(k=16\) realization, there are exactly **two periodic cycles**: a single fixed point, consisting of the all-zero word, and one primitive cycle containing every other periodic state, of length \(32767\). The other \(32768\) states are strictly preperiodic with transient length one. The two basins have sizes \(2\) and \(65534\), respectively. All outputs after one step obey an exact three-bit parity identity, so at least half the full-resolution words are impossible outputs, even though coarse numerical histograms can appear approximately uniform.

## Assumptions and scope

Let \(k\ge3\), and denote a digital state by its ordered fractional bits \(b=(b_1,\ldots,b_k)\in\mathbb F_2^k\), with the most significant bit first. Define the deterministic gate-level update \(T_k\) by conditionally applying the bitwise one's complement when \(b_1=1\), shifting left by one place (discarding the leading bit), and setting the new final bit to \(b_{k-1}\oplus b_k\). Equivalently, the resulting bits \(c=T_k(b)\) are

\[
c_i=b_1\oplus b_{i+1}\quad(1\le i\le k-1),\qquad
c_k=b_{k-1}\oplus b_k.
\]

This is the exact ideal synchronous transition of the XOR-gate realization specified by the source paper's Equations (6)–(8) and Figure 2, without stochastic reseeding, postprocessing, analog faults, or intermediate gates outside that diagram. The one-step selector for an initial seed is not treated as part of the autonomous orbit. No claim is made about any altered implementation or arbitrary continuous real tent map.

Put

\[
H_k=\{c\in\mathbb F_2^k:c_{k-2}\oplus c_{k-1}\oplus c_k=0\}.
\]

For \(k=16\), define the degree-\(15\) binary polynomial

\[
Q(t)=t^{15}+\sum_{j=0}^{13}t^j.
\]

## Proof

**1. Linearity, image, and one-step stabilization.** Every output coordinate is the sum modulo two of two input coordinates, so \(T_k\) is \(\mathbb F_2\)-linear. Its last three coordinates satisfy

\[
c_{k-2}\oplus c_{k-1}\oplus c_k
=(b_1\oplus b_{k-1})\oplus(b_1\oplus b_k)
\oplus(b_{k-1}\oplus b_k)=0.
\]

The first \(k-1\) output coordinates vanish precisely when \(b_2=\cdots=b_k=b_1\). The last output then vanishes, too; hence \(\ker T_k\) consists of zero and the all-one vector. Rank-nullity gives \(\dim(\operatorname{im}T_k)=k-1\), so \(\operatorname{im}T_k=H_k\). The all-one vector does **not** belong to \(H_k\), because three ones have odd parity. Thus \(\ker T_k\cap H_k=\{0\}\), and the restriction \(T_k|_{H_k}\) is a bijection of \(H_k\). Every point of \(H_k\) is consequently periodic; every point outside it maps into \(H_k\) in one step and is not periodic. Moreover, each \(h\in H_k\) has two preimages differing by the all-one vector, and exactly one lies outside \(H_k\).

**2. Characteristic polynomial.** Let \(M_k\) be the matrix of \(T_k\). In the characteristic equation over \(\mathbb F_2[t]\), the first \(k-1\) rows of \((tI-M_k)b=0\) yield \(b_{j+1}=t b_j+b_1\). Eliminating \(b_2,\ldots,b_k\) and using the final row \((t+1)b_k+b_{k-1}=0\) gives, by monic polynomial row elimination,

\[
\chi_{M_k}(t)=t\left(t^{k-1}+\sum_{j=0}^{k-3}t^j\right).
\]

For clarity, put \(P_j(t)=t^{j-1}+\sum_{r=0}^{j-2}t^r\) for \(j\ge2\), with \(P_1(t)=1\). The eliminated final row is \((t+1)P_k(t)+P_{k-1}(t)=t^k+\sum_{j=1}^{k-2}t^j\), precisely the displayed characteristic polynomial. Because \(H_k\) is invariant and the quotient of \(\mathbb F_2^k\) by \(H_k\) has zero induced map, the characteristic polynomial on \(H_k\) is the degree-\((k-1)\) factor.

**3. Exact primitive-polynomial certificate at sixteen bits.** With coefficients encoded as bits of an integer, \(Q\) has mask `0xBFFF`. Exact polynomial arithmetic modulo \(Q\) yields

\[
t^{2^{15}}\equiv t\pmod Q,
\qquad \gcd(Q,t^{2^5}-t)=\gcd(Q,t^{2^3}-t)=1.
\]

The Rabin irreducibility criterion (degree \(15\), distinct prime divisors \(3\) and \(5\)) proves \(Q\) irreducible. Further, because \(2^{15}-1=32767=7\cdot31\cdot151\), modular exponentiation gives the following nonunit residues:

\[
\begin{aligned}
t^{4681}&\equiv\texttt{0x021F}\pmod Q,\\
t^{1057}&\equiv\texttt{0x5193}\pmod Q,\\
t^{217}&\equiv\texttt{0x355C}\pmod Q.
\end{aligned}
\]

These residues are all unequal to one. Hence the residue class of \(t\) in \(\mathbb F_2[t]/(Q)\) has multiplicative order \(32767\), so \(Q\) is primitive. The restriction \(T_{16}|_{H_{16}}\) has irreducible characteristic polynomial \(Q\), hence is linearly conjugate to multiplication by that primitive element on \(\mathbb F_{2^{15}}\). It follows that zero is its only fixed point and that its \(32767\) nonzero states constitute one cycle. Part 1 supplies the exact one-step transients, basin counts, and parity obstruction.

## Verification

Run the standalone Python 3 program `verify_tent.py` with no dependencies. It computes the gate-level update and an independently expressed linear update on all \(65536\) words, checks image rank and the parity condition, performs exact binary-polynomial irreducibility and primitive-order calculations, then exhaustively traverses the entire nonzero periodic cycle. It reports `VERIFICATION_OK` after confirming every stated finite-state count. The infinite-word-length assertions and completeness of the classification follow from the algebraic argument, not from extrapolating the computation.

## Relationship to prior work

The original Nardo–Nepomuceno–Muñoz–Butusov–Arias-Garcia paper [1] supplies the gate layout, conditional complement rule, and XOR perturbation and evaluates hardware usage, pseudorandom test statistics, and finite sampled traces. It does not state the characteristic polynomial, the invariant output parity hyperplane, or an exhaustive cycle and transient census. The complete circuit-to-linear-map reduction is not a general consequence of the continuum tent-map formulation: it uses the specific one's-complement and XOR implementation.

Classical maximum-length linear-feedback shift-register theory [2] already proves the period of a linear register **once** its primitive connection polynomial is known. That theory is used, not claimed as new. The contribution here is the exact identification of this particular published circuit with an effectively \(15\)-dimensional linear system and its exact characteristic/primitivity and orbit structure. The originating author's later thesis [3] reproduces this circuit and its empirical tests; its available chapter excerpts were considered, but a complete independent reading of that thesis chapter was unavailable.

## Limitations

The statement is about deterministic bit-level states and transition logic, not analog perturbations, reset circuitry, changed output formatting, or attacks on a particular application. It does not prove a cryptographic attack, statistical failure for the tests applied in [1], or an absence of useful practical sample sequences. A sampled histogram with bins coarser than the binary grid can coexist with the exact parity restriction. Priority remains subject to specialist scrutiny of less accessible literature and of the complete thesis chapter cited above.

## References

[1] L. Nardo, E. Nepomuceno, D. Muñoz, D. Butusov, and J. Arias-Garcia, *A Hardware-Efficient Perturbation Method to the Digital Tent Map*, Electronics **12** (2023), article 1953. DOI: https://doi.org/10.3390/electronics12081953 ; lawful open PDF: https://mural.maynoothuniversity.ie/id/eprint/18534/1/electronics-12-01953.pdf (first public release: 2023-04-21).

[2] N. P. Smart, *Cryptography: An Introduction*, treatment of linear-feedback shift registers and primitive connection polynomials, https://nigelsmart.github.io/Crypto_Book/book.pdf ; see also *The Cycle Structure of LFSR with Arbitrary Characteristic Polynomial over Finite Fields*, arXiv:1612.07928.

[3] L. G. Nardo, *Exploiting the Chaotic Dynamics: Novel Approaches for Cryptosystems, Digital Systems, and Lyapunov Exponent Estimation*, PhD thesis (2024), https://repositorio.ufmg.br/handle/1843/75848 .

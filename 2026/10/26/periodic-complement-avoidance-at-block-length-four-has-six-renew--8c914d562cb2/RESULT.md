# Periodic complement avoidance at block length four has six renewal families

## Finding

For every integer \(n\ge1\), a **labeled circular word** is a binary vector \(w=(w_0,\ldots,w_{n-1})\) with its positions distinguished. Define its set of cyclic length-four factors by
\[\mathcal F_4(w)=\{(w_i,w_{i+1},w_{i+2},w_{i+3}):i\in\mathbb Z/n\mathbb Z\},\]
where all indices are taken modulo \(n\). Complementation flips every bit. Call \(w\) admissible when there is no \(u\in\mathcal F_4(w)\) for which the bitwise complement \(\bar u\) also lies in \(\mathcal F_4(w)\). This is equivalent to avoidance in the bi-infinite periodic extension, including when \(n<4\).

**Theorem.** Let \(c_n\) count admissible labeled circular words. For every \(m\ge2\), let \(p_m(n)\) count labeled binary circular words whose ones are separated by at least \(m-1\) zeros in the periodically repeated word (the all-zero word is counted). For all \(n\ge1\),
\[
\boxed{c_n=2p_3(n)+4p_7(n)-4},\qquad
p_m(n)=1+\sum_{j=1}^{\lfloor n/m\rfloor}\frac{n}{j}\binom{n-(m-1)j-1}{j-1}.
\]
Consequently the exact dynamical generating function is
\[
\boxed{\exp\!\left(\sum_{n\ge1}\frac{c_nz^n}{n}\right)=
\frac{(1-z)^4}{(1-z-z^3)^2(1-z-z^7)^4}}.
\]
The number \(N_n\) of admissible necklaces (rotation classes) and the number \(P_n\) of admissible labeled primitive-period words are, respectively,
\[
N_n=\frac1n\sum_{d\mid n}\varphi(d)c_{n/d},\qquad
P_n=\sum_{d\mid n}\mu(d)c_{n/d}.
\]
For \(n=1,\ldots,20\) the labeled counts are
\[
(2,2,8,10,12,20,58,74,98,132,178,244,340,506,738,1066,1532,2198,3156,4540).
\]
In particular, the dominant exponential growth constant is the unique positive real root \(\lambda\in(1,2)\) of \(\lambda^3-\lambda^2-1=0\), and \(c_n\sim2\lambda^n\).

## Assumptions and scope

All words are over the ordered alphabet \(\{0,1\}\). Distinct coordinate positions are distinguished in \(c_n\), even if the word is periodic. A factor always wraps around the circle and may revisit coordinates when \(n<4\). The complement is **bitwise**, not reversal or reverse complement. The constraint concerns pairs of *distinct* length-four factors; it does not count how many times a factor occurs. The result holds for every positive circumference with no aperiodicity, balance, or prescribed-content assumption.

## Proof

**1. The eight-vertex edge graph.** Identify the binary four-bit word whose integer value is \(e\in\{0,\ldots,15\}\) with the directed edge
\[e:\quad \lfloor e/2\rfloor\longrightarrow e\bmod8\]
in the binary order-three de Bruijn graph. Its complementary edge is \(15-e\). Exactly eight unordered complementary pairs \(\{e,15-e\}\) occur. Any cyclic word gives a closed directed walk of length \(n\), and its *set* of edges is a strongly connected directed support with at most one edge in each complementary pair. Conversely, a closed walk of length \(n\) on such edges determines a unique admissible labeled circular word. The graph convention is valid even for \(n=1,2,3\).

**2. Finite support-classification lemma.** There are exactly \(3^8=6561\) subsets of edges containing at most one member of each complementary pair: for each pair choose neither, the lower-numbered member, or the higher-numbered member. Test strong connectivity on the active vertices via directed reachability in both directions. The nonempty strongly connected supports consist of precisely \(20\) distinct sets. Their inclusion-maximal members are exactly the following six sets; each string lists the edge integers in hexadecimal notation:

| Family | Edges, hexadecimal | Number of members | \(\det(I-zA)\) |
| --- | --- | ---: | --- |
| A | `012568bc` | 8 | \(1-z-z^7\) |
| B | `013468ad` | 8 | \(1-z-z^7\) |
| C | `2579bcef` | 8 | \(1-z-z^7\) |
| D | `3479adef` | 8 | \(1-z-z^7\) |
| E | `012489` | 6 | \(1-z-z^3\) |
| F | `67bdef` | 6 | \(1-z-z^3\) |

Here \(A\) is the \(8\times8\) adjacency matrix of the edges in that row, with zero entries at inactive vertices. The full list of the \(20\) connected supports in hexadecimal is

`012568bc, 013468ad, 2579bcef, 3479adef, 12568bc, 13468ad, 2579bce, 3479ade, 012489, 67bdef, 01248, 12489, 67bde, 7bdef, 1248, 7bde, 249, 6bd, 0, f`.

Each of the \(18\) nonconstant supports is contained in **exactly one** of the six maximal members. The singleton loop `0` is contained in A, B and E; the singleton loop `f` is contained in C, D and F. This is a finite exhaustive lemma, with the full \(6561\)-case algorithm supplied in `verify.py`, including assertions of the exact full table and maximal family membership. Thus all nonconstant labeled periodic words occur in exactly one template, whereas each constant word occurs in exactly three templates. This yields a correction of subtracting \(4\) from the sum of the six template counts, for every \(n\ge1\).

**3. Exact template traces.** For a finite adjacency matrix \(A\), the number of length-\(n\) closed walks with a specified initial vertex is \(\operatorname{tr}(A^n)\). The six small determinants stated in the table are exact integer polynomial identities. They follow either from direct expansion or from the recurrence for coefficients \(q_k\) of \(\det(I-zA)\):
\[q_0=1,\qquad kq_k=-\sum_{i=1}^kq_{k-i}\operatorname{tr}(A^i),\quad1\le k\le8.\]
The accompanying checker computes all six \(8\times8\) matrices, their traces, and these coefficients independently from the stated determinant factors.

For each \(m\in\{3,7\}\), the standard \(m\)-state spacing automaton for zeros separated by at least \(m\) between successive ones has generating determinant \(1-z-z^m\): it has a zero-letter self-loop at its ready state and an \(m\)-step return cycle enforcing the minimum separation. Consequently
\[\sum_{n\ge1}\frac{p_m(n)}n z^n=-\log(1-z-z^m),\]
and \(p_m(n)\) equals the trace sequence of each corresponding template. There are four \(m=7\) templates and two \(m=3\) templates. The support classification therefore gives \(c_n=2p_3(n)+4p_7(n)-4\) for **all** \(n\).

**4. Explicit coefficients, necklaces and growth.** If there are exactly \(j\ge1\) ones on a labeled circle, all \(j\) successive cyclic gaps have at least \(m-1\) zeros. Cyclic gap compositions and division by the choice of distinguished one give
\[\frac nj\binom{n-(m-1)j-1}{j-1}\]
words, with \(j\le\lfloor n/m\rfloor\); add one all-zero word. This proves the binomial formula. Exponentiating the trace identity and the constant-word correction gives the stated rational dynamical generating function. Fixed points of a rotation through \(k\) places correspond to length-\(\gcd(n,k)\) periodic admissible words; Burnside's lemma proves the necklace formula, while Möbius inversion proves the primitive-period formula.

Finally, \(p_3(n)\) is the sum of \(n\)-th powers of the three roots of \(x^3-x^2-1\); its unique positive root \(\lambda>1\) is strictly larger in modulus than the other two by primitivity of the spacing graph. The corresponding seven-state graph has smaller spectral radius, because it permits a proper subset of the periodic spacing-three language; more explicitly its Perron root \(\rho\) satisfies \(\rho^7-\rho^6-1=0\) and \(1<\rho<\lambda\). Hence \(c_n\sim2\lambda^n\).

## Verification

Run `python3 verify.py` using only the Python standard library. The checker enumerates all \(6561\) complement-compatible edge subsets, tests directed strong connectivity and the complete \(20\)-support list, identifies the six maximal templates, reconstructs exact determinant coefficients via Newton identities, and compares their traces with the independent circular-gap formula through length \(36\). It also enumerates all \(2^n\) labeled binary words separately for each \(1\le n\le16\) and tests the factor-complement condition directly, including short-period wraparound. Successful output begins `COMPLEMENT4_CYCLIC_PASS`.

## Relationship to prior work

Currie, Dvořáková, Ochem, Opočenská, Rampersad and Shallit introduced and analyzed the length-threshold complementary-factor avoidance class \(\mathrm{CAL}_{\ell}\). Their preprint appeared publicly on September 20, 2022 (arXiv:2209.09598), and the later journal article studies repetition and factor-complexity thresholds, including a length-four restriction combined with power-freeness. The present theorem instead counts **all** periodic points of the unrestricted length-four avoidance class at **every** length, with a six-template classification and exact necklace/zeta formulas. Their results do not state or directly imply the periodic-point census under the same unrestricted hypotheses. Sawada, Stevens and Williams construct complement-free de Bruijn sequences by selecting representatives of complementary factor pairs at odd orders, rather than enumerating all binary periodic words avoiding complementary length-four factors. Neither source is claimed to establish this new enumeration. Further prior coverage is possible in an unindexed cyclic-symbolic-dynamics treatment; originality is assessed only against the sources actually checked.

## Limitations

The classification is specific to binary complementation and factors of length four; it does not give a formula for higher factor length, other alphabets, arbitrary morphic constraints, or joint repetition thresholds. The finite support lemma is reproducibly verified by a complete \(6561\)-case exact computation, not expanded here into \(6561\) handwritten cases. The direct word check only reaches length \(16\); the all-length result follows from the finite graph classification and transfer-matrix identities, not finite extrapolation. No independent mathematical audit has been conducted.

## References

1. J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598 (first public posting 2022-09-20); *Electronic Journal of Combinatorics* 32(4) (2025), P4.24, doi:10.37236/11555. https://arxiv.org/abs/2209.09598
2. J. Sawada, B. Stevens, A. Williams, *De Bruijn Sequences for the Binary Strings with Maximum Density*, WALCOM 2011, LNCS 6552, 182–190, doi:10.1007/978-3-642-19094-0_19. https://doi.org/10.1007/978-3-642-19094-0_19
3. Standard formal determinant/trace identity \(\det(I-zA)=\exp(-\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n)\) and Burnside's lemma, with explicit specializations proved above.

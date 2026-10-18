# Exact mod-four edge-count laws conditional on all degree parities in a uniform random graph

## Finding

Let \(n\geq3\), let \(G\sim G(n,1/2)\) be a labeled simple graph with independent fair edges, and write \(E=|E(G)|\). Fix a binary vector \(d=(d_1,\ldots,d_n)\) of even weight \(w=\sum_{j=1}^n d_j\). Let \(D_j=\deg_G(j)\bmod 2\), \(M=\binom n2\), and \(Z_{n,w}=\mathbb E[i^E\mid D=d]\), where \(i^2=-1\). The conditional expectation depends on \(d\) only through \(w\), and is given by the following *exact* formulas:

\[
Z_{n,w}=\begin{cases}
0,&n\text{ even and }0<w<n,\\[2pt]
2^{n-M-2}(1+i)^M\bigl(1+i(-1)^{n/2}\bigr),&n\text{ even and }w=0,\\[2pt]
2^{n-M-2}(1+i)^M\bigl(1-i(-1)^{n/2}\bigr),&n\text{ even and }w=n,\\[2pt]
(-1)^{w/2+(n^2-1)/8}\,2^{-(M-n+1)/2}\exp(i\pi M/4),&n\text{ odd}.
\end{cases}
\]

In every case, for each integer \(a\in\{0,1,2,3\}\),
\[
\Pr(E\equiv a\pmod4\mid D=d)
=\tfrac14\left(1+2\operatorname{Re}(i^{-a}Z_{n,w})\right).
\]
In particular, the four conditional residue probabilities are all exactly \(1/4\) **if and only if** \(n\) is even and \(0<w<n\). Thus for even order, every fixed feasible nonconstant degree-parity vector makes the entire edge count *exactly* uniform modulo four. The two constant parity vectors are the only exceptions; in odd order no feasible vector gives exact uniformity. The nonzero complex biases have exact magnitudes \(2^{-(M-n+1)/2}\) for odd \(n\) and \(2^{n-M/2-3/2}\) for the two even-order exceptions.

## Assumptions and scope

The probability space consists of all \(2^M\) simple labeled graphs on vertex set \(\{1,\ldots,n\}\), equally weighted. The statement holds for every integer \(n\geq3\) and every \(d\in\{0,1\}^n\) of even Hamming weight; odd-weight vectors have zero probability by the handshaking lemma and are not conditioned upon. There are exactly \(2^{M-n+1}\) graphs with each feasible vector \(d\); thus all conditional probabilities are defined. Here \(i\) is the imaginary unit and complex powers are integer powers except for the real powers of two and the ordinary exponential \(\exp(i\pi M/4)\). All equalities are finite-sample identities, not asymptotic approximations.

## Proof

**1. The degree-syndrome fibers are uniform.** Encode the \(M\) edges by \(x\in\mathbb F_2^M\). The incidence matrix \(B\) of the complete graph, with both endpoints marked by \(1\), satisfies \(D=Bx\). Its image is precisely the even-weight vectors and its rank is \(n-1\), since a connected graph has an incidence matrix of that rank over \(\mathbb F_2\). Thus every feasible fiber \(Bx=d\) has \(2^{M-n+1}\) members, and \(\Pr(D=d)=2^{-(n-1)}\).

**2. A syndrome Fourier transform.** For \(y\in\mathbb F_2^n\), write \(y\cdot d\) for the binary scalar product, and let \(K_k(w;n)\) be the coefficient of \(t^k\) in \((1-t)^w(1+t)^{n-w}\). Expanding the indicator \(\mathbf1_{Bx=d}=2^{-n}\sum_y(-1)^{y\cdot(Bx-d)}\) and averaging independent edge variables yields
\[
Z_{n,w}=\frac{(1+i)^M}{2^{M+1}}
\sum_{k=0}^n K_k(w;n)(-i)^{k(n-k)}.\tag{1}
\]
Indeed, for a test vector \(y\) with \(k\) ones, exactly \(k(n-k)\) edges join opposite \(y\)-classes. Each such edge contributes \((1-i)/2\), rather than \((1+i)/2\); their ratio is \(-i\). Summing \((-1)^{y\cdot d}\) over test vectors of weight \(k\) gives \(K_k(w;n)\).

**3. Even order.** When \(n\) is even, \((-i)^{k(n-k)}=1\) for even \(k\) and \(i(-1)^{n/2}\) for odd \(k\). Put \(F(t)=(1-t)^w(1+t)^{n-w}\). The even and odd coefficient sums are \((F(1)+F(-1))/2\) and \((F(1)-F(-1))/2\), respectively. For \(0<w<n\), both \(F(1)\) and \(F(-1)\) vanish. For \(w=0\), the pair is \((2^n,0)\); for \(w=n\), it is \((0,2^n)\). Substitution into (1) gives all three even-order cases.

**4. Odd order.** Put \(\varepsilon=(-1)^{(n-1)/2}\). Then \((-i)^{k(n-k)}=\cos(\pi k/2)+\varepsilon\sin(\pi k/2)\). Therefore the coefficient sum in (1) is
\[
\operatorname{Re}\left[(1-i\varepsilon)(1-i)^w(1+i)^{n-w}\right]
=(-1)^{w/2+(n^2-1)/8}2^{(n+1)/2}.
\]
Here the last identity follows by writing \(1\pm i=\sqrt2\exp(\pm i\pi/4)\), and uses that \(w\) is even. Combining with \((1+i)^M=2^{M/2}\exp(i\pi M/4)\) yields the odd-order case of the claimed formula.

**5. Recovering all four probabilities.** Fix any triangle on the vertex set. Symmetric difference of an edge set with this triangle preserves each degree parity and flips the parity of the number of edges. It is a fixed-point-free involution on each feasible syndrome fiber; hence \(\mathbb E[(-1)^E\mid D=d]=0\). Four-point Fourier inversion, using \(\mathbb E[i^E\mid D=d]=Z_{n,w}\) and its complex conjugate, gives the displayed probability formula. This inversion also shows that the four probabilities are uniform exactly when \(Z_{n,w}=0\). The explicit cases above have no other zeros. Their magnitudes follow from \(|1+i|=\sqrt2\).

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and integer arithmetic. It computes the Gaussian-integer Fourier sum (1) from exact Krawtchouk coefficients and compares it with an independent evaluation of the closed forms for every feasible weight through \(n=12\), totaling 45 exact formula comparisons. Separately it enumerates **every** graph on \(n=3,4,5,6\) labeled vertices (33,864 graphs in total) and confirms all four counts for every possible degree-parity vector (60 conditional fiber configurations). The reported 105 checks are finite corroboration; Steps 1–5 are the proof for every admissible \(n\).

Run `python3 verify.py`; the expected output is `OK: 105 independent exact analytic/finite-graph instances; n=3..12 analytic, n=3..6 exhaustive.`

## Relationship to prior work

The degree-congruence questions and discrete Fourier setup are motivated by Ferber, Hardiman and Krivelevich, who study induced subgraphs with prescribed degree residues and develop asymptotic degree-congruence estimates. Balister, Powierski, Scott and Tan count partitions into induced subgraphs with prescribed degree residues. These results address degree conditions for induced subgraphs or vertex partitions, not the conditional distribution of a whole graph's edge total modulo four. The work of Lengler and collaborators examines global edge-count congruence as a source of dependencies in random graph models, but develops connectivity thresholds rather than this joint conditional law. The general relationship between binary-code weight enumerators and graph cycle spaces, including MacWilliams/Greene methods, is classical. Equation (1) is a specialization of general character-enumeration methods; the asserted result is the evaluated, parity-sensitive classification of every labeled syndrome fiber, not a claim to invent the transform itself.

## Limitations

The graph must have independent fair edges, and the conditioning concerns the entire **parity** vector, not full integer degree values. No claim is made for \(n=1,2\), unequal edge probabilities, or other edge-count moduli. The result proves exact finite-order probabilities, but not any broader universality under dependence. Historical priority remains potentially sensitive to older cycle-code coset enumerators and Ising-type partition-function identities: an equivalent formulation under those names may exist beyond the inspected sources. No independent scientific audit has been performed.

## References

1. A. Ferber, L. Hardiman, and M. Krivelevich, *On subgraphs with degrees of prescribed residues in the random graph*, arXiv:2107.06977, initially public 2021-07-14. Relevant portions: Theorems 1.1–1.3 and Section 2, especially Lemma 2.5 and its Fourier proof.
2. P. Balister, E. Powierski, A. Scott, and J. Tan, *Counting partitions of \(G_{n,1/2}\) with degree congruence conditions*, arXiv:2105.12612, initially public 2021-05-26. Relevant portions: introduction, Theorems 4–7 and the partition-count proofs.
3. J. Lengler and collaborators, *On Connectivity in Random Graph Models with Limited Dependencies*, arXiv:2305.02974, initially public 2023-05-04; APPROX/RANDOM 2023, DOI: 10.4230/LIPIcs.APPROX/RANDOM.2023.30. Relevant portion: Section 1.1 examples of global edge-count congruence, and the main connectivity thresholds.
4. P. J. Cameron, *Cycle Index, Weight Enumerator, and Tutte Polynomial*, Electronic Journal of Combinatorics 9 (2002), N2. Relevant portion: Sections 2 and 4 on weight enumerators and Greene's theorem.

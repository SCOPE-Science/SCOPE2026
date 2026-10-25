# Sharp mod-four stabilization and zero-mode rank dichotomy for permuted Rule 90 rings

## Finding

For every even ring length \(N\ge4\), and **every** permutation of the \(N\) sites applied after the synchronous Rule 90 update, there is an exact dichotomy between one-step stabilization and unavoidable further collapse. Let \(T=PR\) on \(V=\mathbb F_2^N\), where \((Rx)_i=x_{i-1}+x_{i+1}\) with subscripts modulo \(N\) and \(P\) is any coordinate-permutation matrix. Set \(E=\{0,2,\ldots,N-2\}\), let \(\pi\) be defined by \((Py)_i=y_{\pi(i)}\), and define \(q=|\{i\in E:\pi(i)\in E\}|\pmod2\).

Then \(\operatorname{rank}T=N-2\), and
\[
\operatorname{rank}T^2=\begin{cases}
N-2,&N\equiv2\pmod4,\\
N-3,&N\equiv0\pmod4\ \text{and}\ q=1,\\
N-4,&N\equiv0\pmod4\ \text{and}\ q=0.
\end{cases}
\]

When \(N\equiv2\pmod4\), **all** \(2^{N-2}\) configurations in \(\operatorname{im}T\) are periodic, every other one of the \(3\cdot2^{N-2}\) configurations has exact preperiod one, and each periodic configuration has exactly four one-step predecessors, of which precisely three are nonperiodic. These statements hold for every permutation; no orbit-length assertion beyond eventual periodicity is made.

When \(4\mid N\), no site permutation makes the first image entirely periodic: \(\operatorname{rank}T^2<\operatorname{rank}T\) always. The zero eigenvalue of \(T\) has exactly \(2-q\) Jordan blocks of length **at least two**, so either one or two independent nilpotent chains are unavoidable. Both alternatives occur for every such \(N\). For the partial prefix rotations \(\pi_r\) from the motivating family, \(q=1\) precisely for \(r\equiv2,3\pmod4\), and \(q=0\) precisely for \(r\equiv0,1\pmod4\) (when \(4\mid N\)). Therefore, the second image has exactly \(2^{N-3}\) or \(2^{N-4}\) states, respectively.

## Assumptions and scope

All vector spaces, ranks, orthogonality, and Jordan forms are over \(\mathbb F_2\). The ring size is even and at least four; the permutation is entirely arbitrary and need not respect geometric adjacency. The dynamics consists of a parallel neighborhood XOR followed by a fixed site permutation, with the same permutation at each step. A state is periodic if some positive iterate fixes it, and its preperiod is the least nonnegative number of steps until it reaches a periodic state. A first or second image denotes the set \(T(V)\) or \(T^2(V)\), not the exact eventual periodic core when \(4\mid N\).

For clarity, the prefix-rotation permutation \(\pi_r\), \(1\le r\le N\), is defined by \(\pi_r(0)=r-1\), \(\pi_r(i)=i-1\) for \(1\le i<r\), and \(\pi_r(i)=i\) for \(r\le i<N\). This is the zero-based indexing of the motivating source's partial-shift connection.

## Proof

**1. The Rule 90 kernel and image.** For \(N\) even, the equation \(Rx=0\) says \(x_{i-1}=x_{i+1}\) for every \(i\); hence the coordinates of \(x\) are constant separately on the even and odd sites. Write \(e_E\) and \(e_O\) for their indicator vectors, with \(O=\{1,3,\ldots,N-1\}\). Consequently \(K=\ker R=\operatorname{span}\{e_E,e_O\}\) has dimension two. Since \(R\) is symmetric, \(\operatorname{im}R=K^\perp\), where the dot product is the standard nondegenerate binary pairing. Thus \(\operatorname{rank}T=N-2\), \(\ker T=K\), and \(\operatorname{im}T=P K^\perp\).

**2. The two-dimensional obstruction.** Restrict the pairing \((v,w)\mapsto\langle v,Pw\rangle\) to \(K\times K\). Since \(E\) and \(O\) each contain \(m=N/2\) sites, its matrix in the basis \((e_E,e_O)\), over \(\mathbb F_2\), is
\[
B=\begin{pmatrix}q&q+\overline m\\q+\overline m&q\end{pmatrix},\qquad \overline m=m\pmod2.
\]
Indeed, the even-to-even incidence has cardinality parity \(q\); the two mixed incidences have parity \(m-q\), and the odd-to-odd incidence also has parity \(q\). For \(v\in K\), the condition \(v\in\operatorname{im}T=P K^\perp\) is equivalent to \(\langle v,Pw\rangle=0\) for every \(w\in K\). Therefore
\[
\dim(\ker T\cap\operatorname{im}T)=2-\operatorname{rank}B.
\]
The restriction \(T:\operatorname{im}T\to\operatorname{im}T^2\) has kernel precisely this intersection, so
\[
\operatorname{rank}T^2=(N-2)-(2-\operatorname{rank}B)=N-4+\operatorname{rank}B.
\]

**3. The sharp modulo-four split.** If \(N\equiv2\pmod4\), then \(m\) is odd. In characteristic two \(\det B=q^2+(q+1)^2=1\), independently of \(q\). Thus \(\operatorname{rank}B=2\), giving \(\operatorname{rank}T^2=N-2\). If \(4\mid N\), then \(m\) is even and \(B\) is the all-\(q\) matrix. Its rank is one for \(q=1\), zero for \(q=0\). This proves all three rank formulas. Both latter ranks really occur: the identity permutation has \(q=m\equiv0\pmod2\), while swapping a single even and a single odd index changes \(q\) to one.

**4. The complete one-step basin law when \(N\equiv2\pmod4\).** Equality of the first and second image dimensions, with \(\operatorname{im}T^2\subseteq\operatorname{im}T\), gives equality of those spaces. Therefore the restriction of \(T\) to \(\operatorname{im}T\) is an injective self-map of a finite set, hence a permutation; all its states are periodic. A state outside the image cannot be periodic, and its first image is already periodic. The image has \(2^{N-2}\) states, leaving \(2^N-2^{N-2}=3\cdot2^{N-2}\) of exact preperiod one. As \(\dim\ker T=2\), every state in the image has exactly four predecessors in the full space. Exactly one of those predecessors lies in the image, since the restriction is bijective; the other three are nonperiodic.

**5. Nilpotent Jordan chains and partial rotations.** For any linear map over a finite field, each Jordan block at eigenvalue zero of length at least two contributes one dimension to \(\ker T\cap\operatorname{im}T\), whereas blocks of length one and nonzero-eigenvalue blocks contribute zero. By Step 2 this number is \(2-\operatorname{rank}B=2-q\) when \(4\mid N\). This counts only blocks of length at least two; it does not assert the lengths of longer chains or the eventual core dimension. Under the prefix rotation \(\pi_r\), direct counting gives
\[
q\equiv \mathbf1_{\{r\text{ odd}\}}+\left\lceil\frac r2\right\rceil\pmod2
\qquad(4\mid N),
\]
which is one for \(r\equiv2,3\pmod4\), and zero for \(r\equiv0,1\pmod4\). The image cardinalities follow from the ranks. This completes the proof.

## Verification

The included standalone Python 3 standard-library checker computes exact binary matrix ranks directly from the update rule, not from the theorem's pairing matrix. It exhausts all \(\sum_{N=3}^{8}N!=46{,}230\) permutations at small dimensions and tests additional reproducible random and prefix-rotation permutations through dimension 36, a total of 49,660 matrix-permutation cases. The successful output is `VERIFY_OK matrix_permutation_cases= 49660`. The program checks the odd-dimensional control case as well as all three even-dimensional branches. This finite evidence checks implementation and boundaries; the universal assertion is proved in Steps 1–5.

## Relationship to prior work

Suzuki, Okuyama, Takahashi, and Saito (2026, arXiv:2609.34542) explicitly introduce the same composition \(T=P_r R\), prove that the first image is a periodic core in odd dimensions, and state in §3.2, Remark 1, that their analysis is restricted to odd ring lengths because their odd-dimensional argument does not extend to even lengths. Their main results characterize certain long periodic orbits for partial prefix rotations; neither their proofs nor their characteristic-polynomial tables classify the first two image ranks for even rings under arbitrary site permutations. The even-dimensional theorem above supplies this omitted boundary and covers all \(N!\) wiring permutations, not just the \(N\) prefix rotations.

Earlier studies by Onuki, Suzuki, and Saito (2025) and Onuki and Saito (2025) concern directly stable periodic orbits of related permutation automata. Their full texts could not be lawfully accessed in this investigation; metadata and the 2026 paper's comparisons were examined. Classical Rule 90 and linear algebra cover the general tools used here, not by themselves the parity-incidence classification for every wiring permutation. Searches of closely matching dynamical statements and published mathematics research records found no equivalent result; absence of a match is not proof of priority.

## Limitations

The theorem determines the full periodic-state census only when \(N\equiv2\pmod4\). For dimensions divisible by four it determines the exact first two image sizes and number of zero-Jordan blocks of length at least two, **not** the higher images, exact periods, whole transient-depth distribution, or complete Jordan form. It does not claim that the odd-dimensional one-step result is new. There has been no independent audit; a matching older result under another description or in the inaccessible 2025 works remains a priority risk.

## References

1. Y. Suzuki, N. Okuyama, H. Takahashi, and T. Saito, *Permutation XOR cellular automata: partial-shift connections and half-primitive polynomials*, arXiv:2609.34542, first public version September 28, 2026. https://arxiv.org/abs/2609.34542 .
2. M. Onuki, Y. Suzuki, and T. Saito, *Permutation XOR cellular automata and direct stable periodic orbits*, Neurocomputing 656 (2025), 131510, DOI:10.1016/j.neucom.2025.131510 (full text not inspected).
3. M. Onuki and T. Saito, *Analysis of Direct Stable Binary Periodic Orbits in Permutation Elementary Cellular Automata*, Communications in Computer and Information Science 2282 (2025), 380–392, DOI:10.1007/978-981-96-6948-6_27 (full text not inspected).

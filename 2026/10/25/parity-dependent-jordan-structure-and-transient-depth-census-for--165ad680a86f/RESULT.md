# Parity-dependent Jordan structure and transient-depth census for Kautz XOR dynamics

## Finding

For every alphabet size \(q\ge 2\) and word length \(m\ge 1\), let \(K(q,m)\) be the directed Kautz shift graph of all length-\(m\) words with unequal consecutive letters, with the shift-and-append arrows. Let \(F\) be the synchronous binary update that replaces each vertex value by the XOR of its outgoing-neighbour values. Write \(N=q(q-1)^{m-1}\).

The **complete power-rank law over \(\mathbb F_2\)** is
\[
\operatorname{rank}(F^t)=
\begin{cases}
q(q-1)^{m-1-t},&0\le t\le m-1,\\
q,& t\ge m,\ q\text{ even},\\
q-1,& t\ge m,\ q\text{ odd}.
\end{cases}
\]
For even \(q\), every recurrent state is fixed or in a primitive two-cycle; there are \(2^{q-1}\) fixed states and \(2^{q-2}\) primitive two-cycles. For odd \(q\), all recurrent states are fixed and there are \(2^{q-1}\) of them.

The **sharp maximum number of updates to enter the recurrent set** is
\[
K=\begin{cases}
0,&q=2,\\
m-1,&q\ge4\text{ even},\\
m,&q\text{ odd}.
\end{cases}
\]
For each integer \(0\le t\le K\), the exact number of initial states whose first periodic time is at most \(t\) is
\[
C_{\le t}=2^{N-r_t+r_K},\qquad r_t=\operatorname{rank}(F^t).
\]
Thus the exact-time population is \(C_{\le0}\) at zero and \(C_{\le t}-C_{\le t-1}\) for \(1\le t\le K\). If \(q\) is odd, exactly one half of all states require the maximum \(m\) updates. If \(q\ge4\) is even and \(m\ge2\), the fraction requiring the maximum \(m-1\) updates is \(1-2^{-q(q-2)}\).

**Complete Jordan classification.** When \(m\ge2\), for each \(1\le j\le m-2\) the multiplicity of the nilpotent zero-eigenvalue block of length \(j\) is \(q(q-2)^2(q-1)^{m-j-2}\). The remaining zero blocks are as follows:

- For odd \(q\), there are \(q^2-2q-1\) zero blocks of length \(m-1\), and one of length \(m\). The nonzero part consists of \(q-1\) one-dimensional eigenvalue-one blocks.
- For even \(q\), there are \(q(q-2)\) zero blocks of length \(m-1\), with no length-\(m\) zero block. The nonzero part consists of one size-two eigenvalue-one block and \(q-2\) size-one eigenvalue-one blocks.

For \(m=1\) and odd \(q\), there is one zero block of length one and \(q-1\) one-dimensional eigenvalue-one blocks. For \(m=1\) and even \(q\), there are no zero blocks and the eigenvalue-one part has one size-two block and \(q-2\) size-one blocks. In particular, \(q=2\) gives a two-state swap at every \(m\), so the latter description applies without zero blocks.

## Assumptions and scope

Fix integers \(q\ge2\) and \(m\ge1\), and an alphabet \(A\) with \(|A|=q\). A vertex is a word \(w=(w_1,\ldots,w_m)\in A^m\) satisfying \(w_i\ne w_{i+1}\) for \(1\le i<m\). It has an arrow to \((w_2,\ldots,w_m,a)\) whenever \(a\ne w_m\); for \(m=1\), this reads as an arrow from \((w_1)\) to \((a)\) whenever \(a\ne w_1\). The configuration space is \(V=\mathbb F_2^{K(q,m)}\), and
\[
(Fx)(w)=\sum_{a\in A\setminus\{w_m\}}x(w_2,\ldots,w_m,a)
\]
with sums taken in \(\mathbb F_2\). "Time to enter the recurrent set" means the least \(t\ge0\) for which \(F^t x\) is periodic. Fixed states have period one; a primitive two-cycle comprises two distinct periodic configurations. Every formula counts labelled vertices/configurations, not symmetry classes. The Jordan statements concern \(F\) over \(\mathbb F_2\), so eigenvalue one has characteristic-two Jordan blocks.

## Proof

**Power rank through the shift structure.** For \(0\le t\le m-1\), all length-\(t\) walks leaving \(w\) are uniquely specified by their appended sequence. Therefore \((F^t x)(w)\) is the sum of the input coordinates indexed by the length-\(m\) admissible words beginning with the suffix \((w_{t+1},\ldots,w_m)\) of length \(m-t\). These sets of input coordinates partition the vertex set as the suffix varies. Each set is nonempty and all such suffixes occur at some vertex \(w\). Consequently, the distinct row functionals of \(F^t\) have nonempty pairwise disjoint support, hence are linearly independent over \(\mathbb F_2\). Their number is \(q(q-1)^{m-t-1}\). In particular \(\operatorname{im}F^{m-1}\) is precisely the \(q\)-dimensional subspace \(W\) of configurations depending only on the final letter.

**The last-letter operator.** On \(W\), represent a configuration as \(x(w)=g(w_m)\) for \(g:A\to\mathbb F_2\). Then
\[
(Fg)(b)=\sum_{a\ne b}g(a)=(I+J)g(b),
\]
where \(J\) is the all-ones \(q\times q\) matrix. Since \(J^2=qJ\), its behaviour splits according to the parity of \(q\). If \(q\) is even, \((I+J)^2=I\), so \(F\) is an involution on \(W\) and all of \(W\) is periodic. If \(q\) is odd, \((I+J)^2=I+J\), and its image is exactly the codimension-one even-parity subspace, on which it acts as the identity. Thus the recurrent subspace is \(W\) for even \(q\) (dimension \(q\)), or \(FW\) for odd \(q\) (dimension \(q-1\)). The rank formula for all higher powers follows at once.

The fixed vectors on \(W\) satisfy \(Jg=0\), meaning \(\sum_{a\in A}g(a)=0\), independently of the parity of \(q\). Hence exactly \(2^{q-1}\) fixed configurations exist. For even \(q\), \(2^q-2^{q-1}=2^{q-1}\) remaining recurrent configurations pair into \(2^{q-2}\) distinct two-cycles. For odd \(q\), every recurrent state is fixed.

**Depth census and sharpness.** Let \(K\) be the index at which the power ranks stabilize. Since \(F\) is bijective on the stabilized image \(U=\operatorname{im}F^K\), an input becomes periodic by time \(t\le K\) exactly when \(F^t x\in U\). The image \(F^t V\) contains \(U\), and the restriction of \(F^t\) onto its image is surjective; therefore the full inverse image of \(U\) has dimension \(N-r_t+\dim U=N-r_t+r_K\). This proves the population formula. For odd \(q\), the ranks decrease from \(r_{m-1}=q\) to \(r_m=q-1\), giving \(K=m\). For even \(q\ge4\), \(r_{m-2}=q(q-1)>q=r_{m-1}\), giving \(K=m-1\); when \(m=1\) no transient exists. For \(q=2\), \(N=2\) for all \(m\), and the update swaps the two vertices, giving \(K=0\). Each asserted maximum is attained because the corresponding rank strictly falls on that final step. Taking ratios of the cumulative counts yields the last-step fractions.

**Jordan multiplicities.** Split the finite-dimensional space into the nilpotent zero-primary space and the invertible recurrent space. For a nilpotent Jordan block of size \(j\), the rank drop \(r_{t-1}-r_t\) counts blocks with length at least \(t\). Hence the multiplicity of length \(j\) is \(r_{j-1}-2r_j+r_{j+1}\), with ranks extended constantly after stabilization. Inserting the displayed rank sequence gives exactly the zero-block multiplicities stated above. On the recurrent space, odd \(q\) gives the identity; even \(q\) gives \(I+J\) with \((J)^2=0\) and \(\operatorname{rank}J=1\), so precisely one size-two Jordan block at eigenvalue one and \(q-2\) one-dimensional blocks. The length-one boundaries follow by applying the same \(I+J\) calculation directly. This determines the full Jordan form and completes the proof.

## Verification

The accompanying standalone `kautz_parity_verify.py` constructs directed adjacency lists from admissible words independently of the symbolic argument, computes powers over \(\mathbb F_2\) using bitset elimination, and compares exact ranks. It also exhaustively iterates the state dynamics whenever the vertex count is at most twelve and compares exact transient-depth populations, fixed states and primitive two-cycles. The included `verification_output.txt` records the executed results: 26 graph instances, 149 power-rank identities, and 8,788 fully simulated configurations. The code is finite evidence for checked instances; the argument above is the proof for all parameters.

## Relationship to prior work

Rosenfeld's 2002 Kautz-sequence article treats Kautz digraphs as iterated line digraphs and gives a characteristic-polynomial formula. Its algebraic spectrum already constrains the eigenvalues, and no novelty is asserted for that spectral identity. The result here determines the **characteristic-two power-rank filtration, exact zero-primary Jordan lengths, and all labelled transient-depth and periodic populations**, which are not fixed by the characteristic polynomial alone. Dalfó and Fiol (2016) investigate enumerative properties of iterated line digraphs and cyclic Kautz variants; their inspected line-digraph results do not state this exact binary state-transition census. Sutner (1988) discusses additive automata on general graphs, and Giang (2010) discusses linear periodic sequences over finite fields; their general framework does not provide the parameterized Kautz-specific rank/Jordan profiles. A related 2008 paper by Ganguly and collaborators studies cycles of additive cellular automata, but only its abstract was accessible here and its full text could not be compared.

## Limitations

The rule is explicitly **directed outgoing-neighbour XOR** and uses the full Kautz shift graph; conclusions need not hold for the underlying undirected graph, a cyclic Kautz subgraph, other update rules, or other fields. Numerical checks do not certify the infinite family. Historical novelty is qualified by incomplete access to the 2008 related paper, and an unindexed prior equivalent may exist. The result is a proved theoretical classification, not an independently audited external certification.

## References

- V. R. Rosenfeld, *Enumerating Kautz Sequences*, Kragujevac Journal of Mathematics **24** (2002), 19–41. https://imi.pmf.kg.ac.rs/kjm/pub/12617301003674_3.pdf
- K. Sutner, *Additive Automata on Graphs*, Complex Systems **2** (1988), 649–661. https://content.wolfram.com/uploads/sites/13/2018/02/02-6-3.pdf
- D. V. Giang, *Linear difference equations and periodic sequences over finite fields*, arXiv:1003.5028 (first posted 2010-03-26). https://arxiv.org/abs/1003.5028
- C. Dalfó and M. A. Fiol, *A note on the order of iterated line digraphs*, arXiv:1607.08832 (first posted 2016-07-29). https://arxiv.org/abs/1607.08832
- N. Ganguly et al., *Exploring Cycle Structures of Additive Cellular Automata*, Fundamenta Informaticae **87** (2008), 137–154. https://doi.org/10.3233/FUN-2008-87202 (abstract-level comparison only).
- J. M. Brunat, *Explicit Cayley Covers of Kautz Digraphs*, Electron. J. Combin. **18** (2011), P105. https://doi.org/10.37236/592

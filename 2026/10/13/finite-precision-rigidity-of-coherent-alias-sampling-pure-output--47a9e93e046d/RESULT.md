# Finite-precision rigidity of coherent alias sampling: pure-output and uniform-output classifications
## Finding
Consider the coherent alias-sampling circuit of Liu et al., in which a uniform address is used to load an alias and an integer keep threshold, a uniform random register is compared with that threshold, and the address is exchanged with the alias on the selected branch. The source's implementation retains the companion address, keep threshold, random register, and comparison flag.

For \(L=2^n\ge2\) and \(B=2^b\ge2\), let the alias table be arbitrary except for the actual bit-width convention
\[
a_j\in\{0,\ldots,L-1\},\qquad 0\le t_j<B\quad(0\le j<L).
\]
Write
\[
d_j=B-t_j\ge1,
\qquad
v_{a,t}=\sum_{j:\,a_j=a,\,t_j=t}|j\rangle,
\]
where empty sums vanish. After the compare-and-swap and without uncomputing the retained registers, the reduced state of the output address is exactly
\[
\boxed{\rho_{\mathrm{addr}}=
\frac1{LB}\left(\sum_{j=0}^{L-1}d_j|a_j\rangle\langle a_j|
+\sum_{a,t}t|v_{a,t}\rangle\langle v_{a,t}|\right).}
\]
Its diagonal agrees with the sampled probabilities in the source:
\[
p_i=\langle i|\rho_{\mathrm{addr}}|i\rangle
=\frac{t_i+\sum_{j:\,a_j=i}d_j}{LB}.
\]

**Pure-output classification.** The state \(\rho_{\mathrm{addr}}\) has rank one if and only if there exists an address \(c\) such that
\[
a_j=c\quad\text{for all }j,
\qquad
t_j=0\quad\text{for all }j\ne c.
\]
In that case \(\rho_{\mathrm{addr}}=|c\rangle\langle c|\). In particular no table obeying the source's strict \(b\)-bit storage convention produces any nonbasis pure address state without ancilla cleanup.

**Uniform-output classification.** The computational-basis distribution is exactly uniform, \(p_i=1/L\) for all \(i\), if and only if the alias map \(j\mapsto a_j\) is a permutation and the keep integers are constant along its cycles:
\[
t_{a_j}=t_j\quad\text{for every }j.
\]
Every such table has the identical reduced quantum state
\[
\boxed{\rho_{\mathrm{addr}}=I/L.}
\]
For the positive-amplitude uniform target
\[
|+_L\rangle=L^{-1/2}\sum_{j=0}^{L-1}|j\rangle,
\]
this yields the **exact** fidelity, trace distance, and address--retained-register entanglement entropy
\[
\boxed{\langle+_L|\rho_{\mathrm{addr}}|+_L\rangle=L^{-1},\quad
\tfrac12\|\rho_{\mathrm{addr}}-|+_L\rangle\langle+_L|\|_1=1-L^{-1},\quad
S(\rho_{\mathrm{addr}})=\log_2L=n.}
\]
Thus classical sampling fidelity equal to one is compatible with exponentially small *pure-state* fidelity, independently of how the finite-precision uniform alias table is chosen. No **unitary on the address alone** can restore purity while keeping this output, since unitaries preserve the spectrum of \(I/L\). Any subsequent purification, postselection, joint ancilla cleanup, or state re-preparation is an additional physical procedure and must be analyzed separately.

The formula also computes fidelity to any positive-amplitude target \(|\psi_p\rangle=\sum_i\sqrt{p_i}|i\rangle\) formed from the realized address probabilities:
\[
\langle\psi_p|\rho_{\mathrm{addr}}|\psi_p\rangle
=\frac1{LB}\left[
\sum_jd_jp_{a_j}+\sum_{a,t}t
\left(\sum_{j:\,a_j=a,\,t_j=t}\sqrt{p_j}\right)^2\right].
\]

## Assumptions and scope
The source's compare-and-swap circuit is interpreted literally: a uniform superposition of \(L\) input addresses and \(B\) random integers, lookup of the alias and keep registers, a comparator flag \(\sigma\ge t_j\), and a coherent exchange of address and alias when the flag is set. The **entire** companion index, keep integer, random integer, and flag remain as auxiliary registers, consistent with the source's explicit implementation convention. Additional temporary lookup-work registers are assumed returned to their specified outputs, and not used to erase the listed retained data.

All amplitudes before the Boolean reversible circuit are positive and uniform, as in the source. The theorem is for arbitrary tables satisfying the integer range, whether or not the table was obtained from a particular classical alias-construction algorithm. The threshold restriction \(t_j<B\) is essential: a \(b\)-bit stored integer cannot equal \(B=2^b\), and the source explicitly uses \(\{0,\ldots,B-1\}\). If a different implementation represents a full-keep threshold \(t_j=B\), the classifications can change.

The theorem addresses the **reduced output address** of this retained-garbage circuit, not the quality of a subsequent block-encoding or qubitization oracle in which the full preparation circuit and its inverse act coherently. It is not a no-go theorem for clean alias-preparation schemes that actively uncompute their auxiliary registers.

## Proof
After the initial uniform superposition and the table lookup, the state (suppressing fixed ancillas) is
\[
\frac1{\sqrt{LB}}
\sum_{j=0}^{L-1}\sum_{\sigma=0}^{B-1}
|j\rangle_{A}|a_j\rangle_C|t_j\rangle_T|\sigma\rangle_R|0\rangle_F.
\]
The comparator sets \(f_j(\sigma)=\mathbf1_{\sigma\ge t_j}\). The controlled exchange gives the following explicit state:
\[
|\Omega\rangle=\frac1{\sqrt{LB}}
\sum_{j,\sigma}
\begin{cases}
|j\rangle_A|a_j,t_j,\sigma,0\rangle_G,&\sigma<t_j,\\
|a_j\rangle_A|j,t_j,\sigma,1\rangle_G,&\sigma\ge t_j.
\end{cases}
\]
This is a single sum with the displayed case-dependent summand. In the exchanged branch, the retained tuple \((j,t_j,\sigma,1)\) identifies the original address \(j\), so all exchanged contributions are mutually orthogonal after tracing out \(G\). There are \(d_j\) such terms for each \(j\), yielding the first, diagonal, sum in the claimed density matrix.

In the unexchanged branch, the retained tuple is \((a_j,t_j,\sigma,0)\). Two original inputs \(j,k\) contribute coherently precisely when \(a_j=a_k\) and \(t_j=t_k\), with the same \(\sigma\). For each common pair \((a,t)\), there are \(t\) admissible random strings \(\sigma<t\). Their contribution is exactly \(t|v_{a,t}\rangle\langle v_{a,t}|\). The branches with distinct flags are orthogonal. This proves the full formula. Its trace is one, since \(\sum_j(d_j+t_j)=LB\), and its diagonal is the stated classical alias distribution.

For purity, observe that every \(d_j>0\) and every term of the density formula is positive semidefinite. If the total matrix has rank one, all the nonzero vectors \(|a_j\rangle\) in its positive decomposition must span one line. Consequently all aliases are equal to one label \(c\), and the support of the rank-one state is \(\mathbb C|c\rangle\). If some \(j\ne c\) had \(t_j>0\), then the positive term \(t_j|v_{c,t_j}\rangle\langle v_{c,t_j}|\) would have positive diagonal at \(j\), outside this support, contradiction. Thus all \(j\ne c\) have \(t_j=0\). Conversely, this condition makes every summand supported on \(|c\rangle\), and the trace-one state is \(|c\rangle\langle c|\).

For uniformity, the diagonal formula gives the equations
\[
\sum_{j:\,a_j=i}d_j=d_i
\quad\text{for each }i,
\]
because \(t_i=B-d_i\). As \(d_i\ge1\), every index \(i\) must have at least one alias preimage. A surjective endomap of a finite \(L\)-element set is a permutation. Each \(i\) therefore has exactly one preimage \(a^{-1}(i)\), so the equations reduce to \(d_{a^{-1}(i)}=d_i\), equivalently \(t_{a_j}=t_j\) along every alias cycle. This also proves the converse.

When the aliases form a permutation, every fiber \(\{j:a_j=a,t_j=t\}\) has at most one element, so every \(v_{a,t}\) is a basis vector or zero. Thus the reduced matrix is diagonal. Uniformity makes each diagonal entry exactly \(1/L\), proving \(\rho=I/L\).

The fidelity to \(|+_L\rangle\) is the expectation of \(I/L\), namely \(1/L\). The difference \(I/L-|+_L\rangle\langle+_L|\) has eigenvalues \(-(L-1)/L\) once and \(1/L\) with multiplicity \(L-1\), giving trace distance \(1-1/L\). Since \(|\Omega\rangle\) is pure, the entropy of entanglement across address versus retained registers equals \(S(\rho)=\log_2L\). The general positive-target fidelity formula follows by direct substitution of the density-matrix decomposition.

## Verification
The theorem is proved for every \(L=2^n\ge2\), \(B=2^b\ge2\), and every allowed alias and threshold table. No finite enumeration establishes an infinite claim.

The standalone checker independently constructs the circuit output by enumerating all input address/random pairs, groups equal retained tuples, and traces out those tuples. It compares the resulting integer Gram matrix with the formula for all tables in several small dimensions, checks the purity criterion and the complete uniformity/permutation classification, verifies the uniform-state fidelity and trace distance, and confirms a boundary counterexample when full-keep values \(t_j=B\) are allowed. The exact proof above, not these finite checks, establishes the universal result.

## Relationship to prior work
Babbush et al., *Encoding Electronic Spectra in Quantum Circuits with Linear T Complexity* (2018), introduce the relevant coherent alias sampling circuit. Their Fig. 11 and Eq. (38) explicitly retain and describe the temporary garbage state. That state description is foundational prior information and already permits the reduced state to be computed; the novel claim here is **not** that alias sampling has garbage, nor the full-state equation. The all-table finite-bit purity and uniform-marginal classifications above add the strict positive-deficit analysis of the source's stored threshold range; the original full-state formula remains the prior starting point.

Liu et al., *Logical Resource Estimation for Quantum State Preparation with compilation* (2026), specify the implemented \(b\)-bit threshold range, retain the auxiliary registers, and give the exact output-basis probabilities. They explicitly distinguish distribution reproduction from pure-state preparation. They do not characterize which legal tables can nevertheless give pure outputs or show that **every** exactly uniform table forces the address to be maximally mixed.

The later paper *Exponentially Compressed and Garbage-Free Alias Sampling for Polynomial State Preparation* (2026) builds a distinct construction using a separate output register, coherent source-pair fibers, fiber ranking, and uncomputation. It explicitly identifies orthogonal output-fiber garbage prior to cleanup. That construction has different retained-register geometry from the earlier compare-and-swap register exchange; its general qualitative observation about garbage does not state the strict finite-bit permutation rigidity theorem for the earlier circuit. It illustrates why the results here do not prohibit alternative clean preparations.

## Limitations
The theorem is conditional on keeping the specific auxiliary registers after the compare-and-swap and on the strict \(b\)-bit convention \(t_j<B\). It does not classify circuits that erase the comparator, uncompute all garbage, use a different output register, or represent full-keep thresholds separately. It does not assert that distributing probabilities correctly is inadequate for all applications; in PREPARE/SELECT constructions, a complete coherent oracle followed by its inverse may use retained garbage safely.

The classification is an exact mathematical consequence of the specified circuit; it does not establish a lower bound on gate counts or prove that garbage uncomputation is computationally hard. Generic entanglement from retained data is well known, and the claim of novelty is restricted to the two complete finite-precision table classifications and their exact quantitative consequences.

## References
1. D. Liu et al., *Logical Resource Estimation for Quantum State Preparation with compilation*, arXiv:2605.18877v1, first public 2026-05-15, primary MSC 81P68, Sections 2.1 and 2.3.
2. R. Babbush et al., *Encoding Electronic Spectra in Quantum Circuits with Linear T Complexity*, Physical Review X 8, 041015 (2018), DOI 10.1103/PhysRevX.8.041015, Section III.D, Fig. 11, Eqs. (37)–(39).
3. D. Liu et al., *Exponentially Compressed and Garbage-Free Alias Sampling for Polynomial State Preparation*, arXiv:2610.03800v1, first public 2026-10-01, Section V.

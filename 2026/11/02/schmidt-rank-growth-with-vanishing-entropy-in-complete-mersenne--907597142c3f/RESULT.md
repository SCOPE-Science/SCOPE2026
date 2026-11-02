# Schmidt-rank growth with vanishing entropy in complete Mersenne-uniform hypergraph states

## Finding

Let \(j\ge3\) be an integer, \(q=2^j\), and \(k=q-1\). Prepare the pure \(n\)-qubit hypergraph state associated with **all** \(k\)-element hyperedges on \(n=m+b\) labeled qubits, and partition the qubits into subsystems of sizes \(m,b\ge q-1\). Define, for \(0\le r<q\),

\[
 p_m(r)=2^{-m}\sum_{\substack{0\le t\le m\\t\equiv r\pmod q}}\binom mt,
 \qquad
 p_b(r)=2^{-b}\sum_{\substack{0\le t\le b\\t\equiv r\pmod q}}\binom bt.
\]

Form the real \(q\times q\) matrix

\[
 T_{r,s}=\sqrt{p_m(r)p_b(s)}\left(1-2\mathbf 1_{\{r+s\equiv q-1\pmod q\}}\right),
 \qquad 0\le r,s<q.
\]

**Exact finite-system statement.** The reduced density matrix of either subsystem has precisely \(q\) positive eigenvalues, counted with multiplicity, and they are the eigenvalues of \(TT^{\mathsf T}\). All other eigenvalues vanish. In particular, the Schmidt rank is **exactly \(q\)** for every qualifying \(m,b\); the positive eigenvalues are not generally equal.

**Sequential large-block limit.** With \(q\) fixed and both \(m,b\to\infty\), the entire positive spectrum converges, as a multiset, to

\[
 \left\{\left(1-\frac2q\right)^2\right\}
 \cup \left\{\frac4{q^2}\right\}^{\!q-1}.
\]

The limiting purity and base-two entropy are therefore

\[
 P_q=\left(1-\frac2q\right)^4+\frac{16(q-1)}{q^4},
\]
\[
 S_q=-\left(1-\frac2q\right)^2\log_2\left(1-\frac2q\right)^2
 -\frac{4(q-1)}{q^2}\log_2\left(\frac4{q^2}\right).
\]

In a **second** limit, \(q=2^j\to\infty\) after the two block sizes have grown, \(S_q=O((\log q)/q)\to0\), while the exact finite-size Schmidt rank \(q\to\infty\). Thus this family simultaneously exhibits increasing Schmidt rank and asymptotically vanishing von Neumann entanglement entropy. No joint-limit claim is made.

## Assumptions and scope

There is exactly one pure qubit for each hypergraph vertex. For every distinct \(k\)-subset of vertices, apply a \(k\)-controlled phase gate that changes the sign of the all-one string on that subset, starting from \(|+\rangle^{\otimes n}\). There are no other hyperedges, weights, gates, noise, or measurements. The integer \(j\ge3\) and block sizes \(m,b\ge q-1\) are arbitrary, and the partition itself can be any set of \(m\) vertices because the state is permutation symmetric. For the limit, \(q\) is held fixed while \(m,b\to\infty\) independently, followed by \(q\to\infty\) through powers of two.

## Proof

**1. Phase depends on a residue.** For a computational basis string of Hamming weight \(w\), exactly \(\binom wk\) of the applied controlled-phase gates act with sign \(-1\). Hence the normalized coefficient is \(2^{-n/2}(-1)^{\binom wk}\). Lucas' congruence modulo two, applied to \(k=2^j-1\) (all lowest \(j\) binary digits equal one), gives

\[
 \binom wk\equiv\mathbf 1_{\{w\equiv q-1\pmod q\}}\pmod2.
\]

Consequently the matrix of state amplitudes across the bipartition has entries

\[
 C_{x,y}=2^{-n/2}\bigl(1-2\mathbf1_{\{|x|+|y|\equiv q-1\pmod q\}}\bigr),
 \quad x\in\{0,1\}^m,\ y\in\{0,1\}^b.
\]

**2. Exact compression.** For each residue \(r\), let \(E_r\) be the normalized uniform superposition of the computational basis strings in the first subsystem with weight congruent to \(r\), and define \(F_s\) analogously for the second. Since \(m,b\ge q-1\), every residue class occurs on both sides. The vectors \(E_r\) and \(F_s\) are orthonormal within their respective systems. All rows of \(C\) in a given residue class coincide, and likewise for columns. In the above orthonormal bases, \(C\) is exactly \(T\) and vanishes on their orthogonal complements. Thus the nonzero spectrum of \(CC^{\mathsf T}\) equals that of \(TT^{\mathsf T}\).

**3. Full rank.** Write \(D_m=\operatorname{diag}(\sqrt{p_m(r)})\), \(D_b=\operatorname{diag}(\sqrt{p_b(s)})\), and \(F=\boldsymbol1\boldsymbol1^{\mathsf T}-2R\), where \(R\) is the permutation matrix \(R_{r,s}=\mathbf1_{\{r+s\equiv q-1\pmod q\}}\). Then \(T=D_mFD_b\) and both diagonal factors are invertible. Since \(R^{\mathsf T}=R\), \(R^2=I\), and \(R\boldsymbol1=\boldsymbol1\),

\[
 FF^{\mathsf T}=4I+(q-4)\boldsymbol1\boldsymbol1^{\mathsf T}.
\]

This matrix has eigenvalue \((q-2)^2\) once and eigenvalue \(4\) with multiplicity \(q-1\); all are strictly positive for \(q\ge8\). Therefore \(T\) has rank \(q\), proving the exact Schmidt-rank claim and the complete finite spectrum description.

**4. Large-block spectrum.** A root-of-unity filter gives, with \(\omega=e^{2\pi i/q}\),

\[
 p_m(r)=\frac1q\sum_{\ell=0}^{q-1}\omega^{-r\ell}
 \left(\frac{1+\omega^\ell}{2}\right)^m.
\]

For every nonzero \(\ell\pmod q\), the modulus of the base in parentheses is at most \(\cos(\pi/q)<1\). Hence \(p_m(r)\to1/q\) and \(p_b(s)\to1/q\), uniformly over residues, as both block sizes grow. In operator norm, \(T\to F/q\). Continuity of singular values, together with the two eigenvalues of \(FF^{\mathsf T}\) above, proves the stated complete limiting spectrum. Normalization follows from \((q-2)^2+4(q-1)=q^2\). Substitution gives exact \(P_q\) and \(S_q\).

**5. Entropy collapse in the iterated limit.** The limiting spectrum comprises one weight \((1-2/q)^2=1-O(1/q)\) and \(q-1\) weights \(4/q^2\), whose total mass is \(O(1/q)\). Directly bounding the two entropy contributions gives \(S_q=O((\log q)/q)\). Thus \(S_q\to0\), although the exact Schmidt rank equals \(q\) for every qualifying finite system. This completes the proof.

## Verification

The included standalone file `verify_mersenne.py` independently calculates residue probabilities by a cyclic Bernoulli update, constructs \(T\), computes singular values, compares small-system spectra to the full computational-basis amplitude matrix with the binomial phase, and checks the limiting eigenvalues and purity. It tests \(q\in\{4,8,16\}\), including the \(q=4\) boundary as a diagnostic outside the stated \(j\ge3\) theorem. The recorded test passed 21 spectral, rank, and normalization comparisons. The proof above, not these finite tests, establishes the theorem for all indicated parameters.

## Relationship to prior work

Rossi, Huber, Bruß and Macchiavello introduced the general hypergraph-state construction and the corresponding equal-amplitude Boolean phase representation; that formalism is used here. Nöller, Gühne and Gachechiladze investigate **geometric entanglement** and local symmetries for symmetric complete hypergraph states, not the finite-system Schmidt eigenvalue formula or the two-stage Mersenne-arity entropy collapse established here. Fajardo and Paraschiv give a general cross-cut sign-matrix formalism and useful Schmidt-rank lower-bound certificates; the present proof instead evaluates all nonzero Schmidt eigenvalues exactly for a specific infinite family. Previously available power-of-two-arity spectrum identities concern \(k=2^j\), not the distinct all-ones binary arities \(k=2^j-1\). The finite compression step uses standard symmetric-state and singular-value methods; these general techniques are not claimed as new.

## Limitations

No spectral statement is asserted for arbitrary hyperedge sizes, incomplete hypergraphs, general weighted controlled phases, noisy states, or cuts in which one side has fewer than \(q-1\) qubits (although residue compression itself is still available). Entropy convergence is sequential, not uniform in growing \(q\) and block size. The exact historical novelty of the specific cyclic sign-matrix spectral identity is subject to specialized prior-literature coverage; the statement is independently reproducible, not independently audited.

## References

1. M. Rossi, M. Huber, D. Bruß, C. Macchiavello, *Quantum Hypergraph States*, arXiv:1211.5554, first posted 2012-11-23, https://arxiv.org/abs/1211.5554 .
2. J. Nöller, O. Gühne, M. Gachechiladze, *Symmetric hypergraph states: Entanglement quantification and robust Bell nonlocality*, arXiv:2302.01695, https://arxiv.org/abs/2302.01695 .
3. C. Fajardo, M. Paraschiv, *Restriction-Based Certificate of Bipartite Schmidt Rank in Hypergraph States*, arXiv:2602.21016, https://arxiv.org/abs/2602.21016 .

# Golden-ratio entropy and exact periodic-orbit law for the binary \((1,3,4)\)-pseudoperiod shift

## Finding
Let \(X\subseteq\{0,1\}^{\mathbb Z}\) consist of all bi-infinite binary sequences \(x\) satisfying
\[
\forall i\in\mathbb Z,\qquad x_i\in\{x_{i+1},x_{i+3},x_{i+4}\}.
\]
This is the binary shift with the distinguished three-pseudoperiod \((1,3,4)\), known to hold for every paperfolding sequence. Let \(P_n=|\{x\in X:\sigma^n x=x\}|\) for \(n\ge1\). Its Artin--Mazur zeta function is exactly
\[
\boxed{\zeta_X(z)=\exp\!\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right)=
\frac{1}{(1-z)^3(1+z)(1-z-z^2)(1+z+z^2)(1+z^2-z^4)}.}
\]
The shift has exactly four strongly connected components in its canonical four-block presentation: two fixed-point components, one alternating two-cycle, and one primitive twelve-state component. Consequently,
\[
\boxed{h_{\mathrm{top}}(X)=\log\!\left(\frac{1+\sqrt5}{2}\right).}
\]
There is exactly one measure of maximal entropy; it assigns probability \(1/2\) to each letter. Thus the complete periodic-point spectrum and the entropy are explicit although the source motivating this pseudoperiod is aperiodic.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), indexing is two-sided, equality is literal equality rather than abelian equivalence, and every displayed assertion includes all integer coordinates. The periodic-point count \(P_n\) counts sequences fixed by the \(n\)-fold shift (not primitive orbits). The number of primitive shift-orbits of length exactly \(n\) is therefore
\[
\frac1n\sum_{d\mid n}\mu(d)P_{n/d}.
\]
The entropy uses natural logarithms. This theorem does not characterize all three-pseudoperiodic words with arbitrary offsets, and it does not assert that all sequences in \(X\) are paperfolding sequences.

## Proof
**Step 1 (exact forbidden language).** The condition fails at coordinate \(i\) precisely if the four visible symbols \(x_i,x_{i+1},x_{i+3},x_{i+4}\) are such that the last three equal \(1-x_i\). The intervening symbol \(x_{i+2}\) is free. Consequently the complete forbidden five-block list is
`01011`, `01111`, `10000`, `10100`.
There are no additional local constraints.

**Step 2 (finite matrix, with explicit indexing).** Index a sixteen-state matrix \(M\) by the binary integers \(0,\ldots,15\). State \(s\) represents its length-four binary expansion. For each \(b\in\{0,1\}\), place an edge from \(s\) to \(t=(2s+b)\bmod16\) unless the concatenation of the four digits of \(s\) with \(b\) belongs to the four-element forbidden set above. Let \(M_{s,t}\) be the number of these edges; it is either zero or one. This completely defines the integer matrix without an external data dependency. A bi-infinite admissible sequence determines exactly one bi-infinite state walk, namely its moving four-symbol windows, and vice versa. In particular, \(P_n=\operatorname{tr}(M^n)\) for every \(n\ge1\), including \(n<4\).

**Step 3 (exact characteristic polynomial).** Direct rational-integer arithmetic gives
\[
\det(\lambda I-M)=\lambda^4(\lambda-1)^3(\lambda+1)
(\lambda^2-\lambda-1)(\lambda^2+\lambda+1)
(\lambda^4+\lambda^2-1).
\]
This identity is reproducible without symbolic-algebra software: the attached script builds every matrix entry from Step 2, computes the traces \(\operatorname{tr}(M^j)\) for \(1\le j\le16\), and reconstructs the coefficients by the exact Newton identities. The sixteen coefficients are tested against the product displayed here. The determinant identity is therefore a finite, explicitly specified calculation. Since \(\exp(\sum_{n\ge1}\operatorname{tr}(M^n)z^n/n)=\det(I-zM)^{-1}\), substitution yields the stated zeta function as a formal power series.

**Step 4 (entropy and components).** Direct reachability in the directed graph gives the four mutually reachable state sets
\[
\{0\},\qquad\{15\},\qquad\{5,10\},\qquad
\{1,2,3,4,6,7,8,9,11,12,13,14\}.
\]
The first three have spectral radius one. The last one is primitive: its twelfth-order adjacency matrix has an eighth power with *every entry strictly positive*, as checked by exact integer multiplication. From the polynomial of Step 3, the unique largest modulus among all eigenvalues is \(\varphi=(1+\sqrt5)/2\); indeed the roots of \(\lambda^4+\lambda^2-1\) have moduli \(\varphi^{-1/2}\) or \(\varphi^{1/2}\), the cubic factor has roots of modulus one, and the remaining non-Perron quadratic root has modulus \(\varphi^{-1}\). The standard Perron--Frobenius growth theorem for finite directed graphs therefore gives \(h_{\mathrm{top}}(X)=\log\varphi\). The unique primitive positive-entropy component supplies the unique maximizing stationary Markov measure, and every invariant measure supported on the other components has strictly smaller entropy. Finally, bit-complementation preserves the entire forbidden set and therefore takes the unique maximal-entropy measure to itself; it must consequently give mass \(1/2\) to each bit.

## Verification
Run `python3 verify_pseudo134.py` with Python 3 and no nonstandard packages. The script verifies the exact forbidden set, the sixteen-state matrix with 28 directed edges, the complete strongly connected partition, positive entries in the eighth power of the twelve-state core, and the entire degree-sixteen characteristic polynomial by integer Newton identities. It independently enumerates every cyclic binary word of length \(1\le n\le12\) and every finite binary word of length \(4\le n\le14\), comparing those counts with matrix calculations. Initial cyclic counts are \(P_1,\ldots,P_6=2,4,8,16,12,16\). The exhaustive checks are finite certificates for the finite-state reductions; the matrix representation and algebra prove the claims at every length.

## Relationship to prior work
Meleshko, Ochem, Shallit and Shan (arXiv:2207.10171, first public version July 20, 2022) introduce pseudoperiodicity and prove that \((1,3,4)\) works simultaneously for all paperfolding sequences (Section 4.6). They also analyze two-shift pseudoperiods and repetition thresholds. That membership theorem does not give the topological entropy of **all binary sequences admitting this fixed triple**, the four-component decomposition, the maximal-entropy measure, or their periodic-point zeta function. The construction here concerns a different global object (the entire finite-type shift), not an additional pseudoperiod of a single automatic word. Standard finite-type-shift transfer-matrix tools are acknowledged as existing methods; the explicit polynomial, orbit census, component structure and golden-ratio entropy are the evaluated statements.

## Limitations
The polynomial calculation can be reproduced exactly with the included verifier, but there is no independent mathematical audit. Other descriptions of the same finite-type shift, perhaps under the four forbidden blocks rather than the pseudoperiod terminology, could duplicate this explicit result. General transfer-matrix methods apply to any fixed set of offsets, but this calculation does not determine their entropy in closed form. No claim of a complete classification of arbitrary pseudoperiods is made.

## References
Meleshko, J.; Ochem, P.; Shallit, J.; Shan, S. L., *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171 (initial public version 2022-07-20), especially Definition 1 and Section 4.6. https://arxiv.org/abs/2207.10171

Lind, D.; Marcus, B., *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 1995. Standard Perron--Frobenius, finite-type entropy and dynamical-zeta framework (background reference, not an independent verification of this particular shift).

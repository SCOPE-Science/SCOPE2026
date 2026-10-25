# Path-reversal orientation of all higher-independence spheres

## Finding
Let \(P_n\) be the simple path on the ordered vertices \(1,\ldots,n\), with \(n\ge1\). For \(r\ge1\), let \(X_n=\operatorname{Ind}_r(P_n)\) consist of vertex subsets whose induced path components have at most \(r\) vertices; equivalently, its binary membership word contains no \(r+1\) consecutive ones. The involution \(s(i)=n+1-i\) preserves the complex. Put \(d=r+2\).

For \(k\ge1\) and \(n\in\{dk-1,dk\}\), the only nonzero reduced integral homology of \(X_n\) is \(\widetilde H_{rk-1}(X_n;\mathbb Z)\cong\mathbb Z\), and reversal acts on it by the following complete sign formula:
\[
\epsilon_r(n)=\begin{cases}
(-1)^{rk/2},& k\text{ even, for either }n,\\
(-1)^{r(k-1)/2+\lceil r/2\rceil},&k\text{ odd and }n=dk-1,\\
(-1)^{r(k-1)/2+\lfloor r/2\rfloor},&k\text{ odd and }n=dk.
\end{cases}
\]
For all other \(n\), the complex is contractible. In particular, the reduced rational homology of the geometric orbit space \(|X_n|/\langle s\rangle\) has dimension one in degree \(rk-1\) precisely when the displayed sign is positive; otherwise the orbit space is reduced rationally acyclic. No assertion of contractibility of a rationally acyclic quotient is made.

## Assumptions and scope
The path is unweighted and simple, the parameter \(r\) is a positive integer, and the reversal is the indicated path automorphism. Integral homology is reduced and the degree-one character is a sign of an integral rank-one representation. The homotopy-concentration assertion is the known path theorem of Paolini--Salvetti as quoted and proved with a perfect matching in Deshpande--Singh, Proposition 4.3. This theorem provides the rank-one homology and contractibility but not the reversal action.

## Proof
**1. Concentration input and Lefschetz normalization.** Deshpande--Singh, Proposition 4.3 and Theorem 4.2, imply \(X_n\simeq S^{rk-1}\) for \(n=(r+2)k-1\) or \(n=(r+2)k\), and \(X_n\) is contractible otherwise. In the sphere cases write \(q=rk-1\). An invariant face of a simplicial involution is a union of vertex orbits. If \(j\) such orbits are chosen, its contribution to the *reduced* simplicial Lefschetz number is \(-(-1)^j\), including the empty face. Consequently
\[
\epsilon_r(n)=(-1)^{q+1}F_r(n),\qquad
F_r(n)=\sum_{\substack{S\subseteq V(P_n),\ sS=S\\ S\in X_n}}(-1)^{\#(S/\langle s\rangle)}.
\]
The orbit count, rather than the number of selected vertices, is essential because the orientation sign on a setwise-fixed simplex is the sign of the restricted permutation.

**2. Exact half-word automaton.** Define the \((r+1)\times(r+1)\) integer matrix \(T_r\), with states \(0,\ldots,r\), by \((T_r)_{i0}=1\) for every \(i\), \((T_r)_{i,i+1}=-1\) for \(0\le i<r\), and all other entries zero. A state records the number of consecutive selected positions at the end of a word. The first transition appends an unselected position; the second appends a selected position with weight \(-1\), and forbids a run of \(r+1\) ones. Let
\[
a_j=e_0^{\mathsf T}T_r^j\mathbf1\quad(j\ge0),\]
where \(e_0\) is the first coordinate vector and \(\mathbf1\) is the all-ones vector. Then \(a_0=1\), \(a_j=0\) for \(1\le j\le r\), and \(a_{r+1}=(-1)^r\), by cancelling all binary words except the forbidden all-ones word.

For even \(n=2m\), a reversal-invariant membership word has two equal mirrored halves. Its initial central run of \(\ell\) selected *orbits* contributes a full run of \(2\ell\) selected vertices, so \(\ell\le\lfloor r/2\rfloor\). The next orbit is unselected, after which the ordinary automaton applies. Therefore, whenever \(n\ge r+1\),
\[
F_r(2m)=\sum_{\ell=0}^{\lfloor r/2\rfloor}(-1)^\ell a_{m-\ell-1}.
\]
For odd \(n=2m+1\), when the central fixed vertex is absent there are \(a_m\) weighted possibilities. When it is present, a surrounding run of \(\ell\) selected pairs has \(2\ell+1\) vertices, hence \(\ell\le\lfloor(r-1)/2\rfloor\). Thus
\[
F_r(2m+1)=a_m+\sum_{\ell=0}^{\lfloor(r-1)/2\rfloor}(-1)^{\ell+1}a_{m-\ell-1}.
\]
The formulas count each admissible invariant face exactly once; all exponents of \(a\) that appear are nonnegative in the stated range.

**3. Transfer periodicity and base values.** The characteristic polynomial is
\[
\det(xI-T_r)=x^{r+1}-x^r+\cdots+(-1)^{r+1}=\frac{x^{r+2}-(-1)^r}{x+1}.
\]
By Cayley--Hamilton, \(T_r^{r+2}=(-1)^r I\), and therefore \(a_{j+r+2}=(-1)^r a_j\). In both half-word sums, increasing the path length by \(2(r+2)\) increases \(m\) by \(r+2\) without changing parity. Thus \(F_r(n+2d)=(-1)^rF_r(n)\). In the spherical cases this increases \(k\) by two and the dimension \(q\) by \(2r\), so
\[
\epsilon_r(d(k+2)-t)=(-1)^r\epsilon_r(dk-t)\quad(t=0,1).
\]
It remains only to evaluate the four base cases. At \(n=d-1=r+1\), the complex is the boundary of an \(r\)-simplex, and path reversal permutes its \(r+1\) vertices with sign \((-1)^{\lceil r/2\rceil}\). At \(n=d=r+2\), the two formulas in Step 2, using \(a_0=1\) and \(a_j=0\) for \(1\le j\le r\), give \(\epsilon_r(d)=(-1)^{\lfloor r/2\rfloor}\). At \(n=2d-1\) and \(n=2d\), the same formulas, using \(a_{r+1}=(-1)^r\), give \(\epsilon_r(2d-1)=\epsilon_r(2d)=(-1)^r\). Applying the recurrence yields the displayed formula for every \(k\).

**4. Quotients.** Over \(\mathbb Q\), homology of a quotient of a finite simplicial complex by a finite simplicial group action agrees with invariant rational homology. Thus the sign determines the entire reduced rational homology of the reversal quotient as stated.

## Verification
Run `python3 verification.py` using Python's standard library. It verifies exact matrix periodicity and the closed formula in 234 parameter cases, reconstructs reversal-invariant faces directly for small cases, and computes exact mod-two chain homology for 34 additional path complexes. This finite verification is corroborative: the proof above covers all positive integer parameters.

## Relationship to prior work
Deshpande and Singh, *Higher Independence Complexes of graphs and their homotopy types* (arXiv:2001.05448, first public January 15, 2020), Section 4, gives the nonequivariant path sphere/contraction theorem and its perfect-matching proof. The present statement classifies the otherwise unspecified reversal sign on its integral top homology. Results about the full strong discrete-Morse complex of paths concern a different complex; existing dihedral homology calculations for cycle matching complexes and bounded-independence complexes likewise do not imply the path reversal formula. The 2014 theorem on nerve complexes of evenly spaced circular arcs computes dihedral representations for cyclic interval nerves; its cycle-action statements do not determine the indicated path involutions.

## Limitations
No explicit canonical integral generator is chosen, and no equivariant homotopy equivalence or integral orbit-space homology is asserted. The homotopy concentration is a cited theorem; the symmetry character is proved here by exact weighted Lefschetz counting. Unindexed equivalent computations remain possible.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first posted 2020-01-15; Section 4, Theorem 4.2 and Proposition 4.3. https://arxiv.org/pdf/2001.05448
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson, C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336, 2014; discussion of different dihedral nerve actions. https://arxiv.org/pdf/1410.4336

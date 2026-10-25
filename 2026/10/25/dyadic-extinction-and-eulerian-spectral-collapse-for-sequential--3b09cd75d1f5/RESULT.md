# Dyadic extinction and Eulerian spectral collapse for sequential Rule 90

## Finding

Let \(n\ge3\), and let \(\pi\) be any permutation of the sites \(\mathbb Z/n\mathbb Z\). A complete sweep updates each site once, in order \(\pi\), by the binary Rule-90 operation \(x_i\gets x_{i-1}+x_{i+1}\pmod 2\), using the current values of its neighbors. Denote the resulting linear map by \(F_\pi\). Write \(p_i\) for the position of site \(i\) in \(\pi\), and let
\[
 a(\pi)=\#\{i\in\mathbb Z/n\mathbb Z:p_i<p_{i+1}\}.
\]
Define the binary cycle matching polynomial
\[
 H_n(z)=\sum_{M\text{ a matching of }C_n}z^{n-|M|}\in\mathbb F_2[z].
\]
Then the following statements hold simultaneously for every \(n\ge3\) and every update order:
\[
 \det(zI-F_\pi)=H_n(z)+z^{a(\pi)}+z^{n-a(\pi)}. \tag{1}
\]
Exactly \(\lfloor n/2\rfloor\) distinct characteristic polynomials occur as \(\pi\) varies. For each \(1\le a\le n-1\), precisely \(n\big\langle\!\!\big\langle n-1,a-1\big\rangle\!\!\big\rangle\) orders have \(a(\pi)=a\), where the bracket denotes the Eulerian number counting permutations of \(n-1\) entries with \(a-1\) ascents.

More sharply, **every initial configuration reaches zero** under iteration of the same complete sweep if and only if
\[
 n=2^s\text{ for an integer }s\ge2,\qquad a(\pi)=n/2. \tag{2}
\]
Every such state is zero after at most \(n\) complete sweeps. Hence the number of zero-extinguishing schedules is exactly
\[
 n\big\langle\!\!\big\langle n-1,n/2-1\big\rangle\!\!\big\rangle
\]
when \(n\) is a power of two at least four, and is zero otherwise. At \(n=4\) there are \(16\) such orders among \(24\); at \(n=8\) there are \(19{,}328\) among \(40{,}320\).

## Assumptions and scope

All linear algebra and determinants are over \(\mathbb F_2\). The spatial boundary is periodic, and each ring site is updated **exactly once per sweep**. The permutation is fixed and repeated across sweeps; synchronous Rule 90 and changing/random schedules are different systems. For \(n\ge3\), each vertex has two distinct neighboring sites. Nilpotent means \(F_\pi^k=0\) for some positive integer \(k\), equivalently all configurations eventually reaching the all-zero configuration.

## Proof

**1. One-sweep implicit system.** Let \(x\) be the old state and \(y=F_\pi x\) the final state. When site \(i\) is visited, an already-updated neighbor \(j\) has value \(y_j\), whereas a neighbor still waiting has value \(x_j\). Define binary \(n\)-by-\(n\) matrices \(L,U\), with \(L_{ij}=1\) if \(j=i\pm1\) was updated *before* \(i\), and \(U_{ij}=1\) if it is updated *after* \(i\). Then
\[
 (I-L)y=Ux,\qquad F_\pi=(I-L)^{-1}U.
\]
In update-order coordinates \(L\) is strictly lower triangular, so \(\det(I-L)=1\). Consequently,
\[
 \det(zI-F_\pi)=\det\bigl(z(I-L)-U\bigr). \tag{3}
\]
In characteristic two the diagonal weights in this determinant are \(z\); a directed neighbor entry has weight \(z\) if that neighbor was updated earlier, and \(1\) otherwise.

**2. Permutation expansion.** A determinant term chooses one outgoing entry at each vertex. For a cycle graph with \(n\ge3\), any contributing permutation consists of fixed vertices and disjoint swaps along cycle edges, or is one of the two cyclic orientations around the entire ring. A fixed vertex contributes \(z\). Each swapped neighboring pair contributes \(z\), since exactly one of its two opposing directed entries has weight \(z\). Thus terms of the first kind contribute \(z^{n-|M|}\) for a matching \(M\). The two full cyclic orientations contribute \(z^{a(\pi)}\) and \(z^{n-a(\pi)}\), respectively, because each oriented cycle uses an earlier-neighbor edge once for each ascent in the site-position sequence (or its complement). Signs disappear modulo two. This proves (1), including possible cancellation of the two full-cycle terms when \(a=n/2\).

**3. The matching polynomial is monomial precisely at dyadic sizes.** Counting cyclic matchings gives \(H_1(z)=z\), \(H_2(z)=z^2\) (formal initial values) and, for \(n\ge3\),
\[
 H_n(z)=z\bigl(H_{n-1}(z)+H_{n-2}(z)\bigr).
\]
Equivalently, with \(B(z)=\left(\begin{smallmatrix}z&z\\1&0\end{smallmatrix}\right)\), the trace \(\operatorname{tr}(B(z)^n)\) satisfies the same recurrence and initial values, so equals \(H_n(z)\). In characteristic two \(\operatorname{tr}(B^{2^s})=\operatorname{tr}(B)^{2^s}\) and therefore \(H_{2^sm}=H_m^{2^s}\). If \(m=1\), then \(H_{2^s}=z^{2^s}\). If \(m>1\) is odd, the coefficient of \(z^{m-1}\) in \(H_m\) is \(m\equiv1\pmod2\), counting the \(m\) one-edge matchings; hence \(H_m\ne z^m\) and \(H_{2^sm}\ne z^{2^sm}\). Thus
\[
 H_n(z)=z^n\quad\Longleftrightarrow\quad n\text{ is a power of two}. \tag{4}
\]

**4. Sharp nilpotence equivalence.** Every monomial of \(H_n\) has exponent at least \(\lceil n/2\rceil\), since a matching has at most \(\lfloor n/2\rfloor\) edges. If \(a\ne n/2\), the smaller of \(a,n-a\) is strictly below \(n/2\); that low-degree term in (1) cannot cancel with any term of \(H_n\) or with the other oriented-cycle term. Hence \(\det(zI-F_\pi)\ne z^n\). If \(a=n/2\), necessarily \(n\) is even and the two oriented-cycle terms cancel, leaving \(H_n\). By (4) the characteristic polynomial is \(z^n\) exactly in (2). A finite-dimensional linear map is nilpotent if and only if its characteristic polynomial is \(z^n\): one implication is immediate from Jordan form, and the other follows from Cayley–Hamilton. In that case \(F_\pi^n=0\). Conversely, when the polynomial is not \(z^n\), the map is not nilpotent, so some initial state never reaches zero.

**5. Spectrum classes and schedule census.** The integer \(a(\pi)\) lies in \(\{1,\ldots,n-1\}\), because positions around a cycle cannot increase or decrease strictly at every step. Two polynomials in (1) coincide precisely when \(\{a,n-a\}\) agree as multisets: their oriented-cycle monomial pairs are otherwise different, and they share the same \(H_n\). There are \(\lfloor n/2\rfloor\) such pairs. To count orders, choose which site has earliest update position (\(n\) choices). Read the remaining \(n-1\) positions cyclically starting immediately after that site. The first cyclic comparison is an ascent and the last a descent, so the remaining comparisons contain exactly \(a-1\) ascents among \(n-1\) entries. Thus precisely \(n\langle\!\langle n-1,a-1\rangle\!\rangle\) orders have the stated cyclic ascent number. All Eulerian numbers in this range are positive, proving realizability and the claimed counts.

## Verification

Run the standalone Python 3 standard-library program `verify.py`. It independently builds the sequential state map from site-by-site row operations, computes its characteristic polynomial by a subset dynamic-programming expansion of \(\det(zI-F_\pi)\) in \(\mathbb F_2[z]\), compares it to (1), checks Eulerian frequencies and the sharp nilpotence condition, and tests additional deterministic random orders at larger sizes. It exhaustively tests all \(5{,}910\) orders for \(3\le n\le7\), including nilpotency, plus \(399\) larger-order samples. A separate all-order ascent census at \(n=8\) gives \(19{,}328\) dyadically balanced schedules. Finite tests corroborate but do not prove the all-\(n\) statement.

For a directly auditable example, at \(n=4\), take update order \((0,2,1,3)\). Starting from the four-bit word `0011` (site \(0\) is the rightmost bit), successive complete sweeps produce `0101` and then `0000`. Theorem (2) establishes extinction of **every** four-bit input for this order. At \(n=8\), updating all even sites before all odd sites provides an explicit qualifying order.

## Relationship to prior work

Macauley and Mortveit (arXiv:0802.4412) study cycle equivalence and update-order orientations for general sequential graph dynamical systems, rather than this Rule-90 characteristic polynomial and extinction census. Vielhaber (arXiv:1208.2762) studies asynchronous ECA computational expressivity, including Rule 90 in a reachability table, without the stated fixed-schedule spectral classification. Defant (arXiv:1511.06966) studies invertible Rule-150 and Rule-105 systems, not noninvertible Rule 90. Balbi and collaborators (arXiv:2004.07128) classify sensitivity for a specified set of rules not including Rule 90.

Donoso-Leiva, Goles, Ríos-Wilson and Sené (arXiv:2509.07797v2, Theorem 7 and Corollary 1) make an opposite assertion that Rule-90 initial configurations containing a pair of adjacent ones cannot reach a fixed point under any sequential order. The explicit four-site trajectory above disproves that assertion under its stated general quantifiers. Their work does not supply, and is not used as a premise for, the spectral formula or classification here. The mathematical discrepancy makes independent comparison important; this note is not an independent assessment of that paper as a whole.

## Limitations

The characteristic polynomial is not a complete invariant of a noninvertible linear map: orders with the same cyclic ascent statistic can have different ranks, Jordan structures, transient depths and nonzero periodic orbit counts. This finding makes **no** claim to classify those finer invariants or the sharp extinction index of each nilpotent order. It concerns permutation sweeps, not block-parallel or time-varying updates. Historical priority has not been independently certified; possible unlocated equivalent results remain a residual literature risk.

## References

- M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412 (first posted 2008-02-29).
- M. Vielhaber, *Computing by Temporal Order: Asynchronous Cellular Automata*, arXiv:1208.2762 (first posted 2012-08-14), DOI 10.4204/EPTCS.90.14.
- C. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966 (first posted 2015-11-22).
- P. P. Balbi et al., *Non-maximal sensitivity to synchronism in periodic elementary cellular automata: exact asymptotic measures*, arXiv:2004.07128 (2020).
- I. Donoso-Leiva et al., *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797v2 (2026 revision of 2025 preprint), Section 3.1.2.

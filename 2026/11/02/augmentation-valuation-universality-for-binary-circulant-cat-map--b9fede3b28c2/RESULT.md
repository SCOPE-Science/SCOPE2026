# Augmentation-valuation universality for binary circulant cat-map orbit spectra

## Finding
Let \(n=2^k\) with \(k\ge2\). Consider **any** symmetric binary circulant \(n\)-by-\(n\) matrix \(C\), allowing or excluding self-loops, and the binary coupled cat map
\[
M_C=\begin{pmatrix}I&C\\C&I+C^2\end{pmatrix}
\quad\text{on }\mathbb F_2^{2n}.
\]
Write its circulant polynomial as \(c(X)\) in \(\mathbb F_2[X]/(X^n-1)\), and let \(\varepsilon=c(1)\in\mathbb F_2\). Put \(g(X)=c(X)\) when \(\varepsilon=0\), and \(g(X)=c(X)+1\) when \(\varepsilon=1\). Let \(v\) be the largest integer at most \(n\) such that \((X+1)^v\) divides \(g(X)\) in the local quotient, with \(v=n\) when \(g=0\). Set
\[
(b,w)=\begin{cases}(1,v),&\varepsilon=0,\\(3,2v),&\varepsilon=1,\end{cases}\qquad
Q_j=2^{2\min(n,w2^j)},\qquad
J=\min\{j\ge0:w2^j\ge n\}.
\]
Here all exponents and divisibility statements refer to **binary** (two-level) phase coordinates, not reduction modulo higher powers of two.

**Complete fixed-space and exact-order theorem.** For every integer \(j\ge0\), precisely \(Q_j\) configurations satisfy \(M_C^{b2^j}x=x\). The exact order of \(M_C\) as a permutation of the binary phase space is \(b2^J\). When \(\varepsilon=0\), the numbers of primitive cycles are
\[
\boxed{a_1=Q_0,\qquad a_{2^j}=\frac{Q_j-Q_{j-1}}{2^j}\ (1\le j\le J),}
\]
and every other cycle length is absent. When \(\varepsilon=1\), the zero configuration is the sole fixed point, and the primitive-cycle counts are
\[
\boxed{a_1=1,\quad a_3=\frac{Q_0-1}{3},\quad
 a_{3\cdot2^j}=\frac{Q_j-Q_{j-1}}{3\cdot2^j}\ (1\le j\le J),}
\]
with no other cycle lengths. If two symmetric circulant graphs have equal \((\varepsilon,v)\), they have **identical complete binary temporal orbit spectra** despite possibly having different degrees and connectivity. All matrices \(M_C\) here are invertible; there are no preperiodic tails.

As a concrete comparison at \(n=16\), the degree-two coupling \(C_2=S+S^{-1}\) and the degree-four coupling \(C_4=S+S^{-1}+S^2+S^{-2}\) have identical orbit spectra: both have \((\varepsilon,v)=(0,2)\), sixteen fixed configurations, exact global period eight, 120 primitive two-cycles and 16,320 primitive four-cycles. In contrast, adding a self-loop to either coupling changes the parity class and introduces a factor-three primitive-period family. This invariance across different connectivity sizes is not implied by a characteristic-polynomial comparison over characteristic zero.

## Assumptions and scope
The cyclic shift \(S\) acts on site indices modulo \(n\); \(C=c(S)\) is any binary symmetric circulant, i.e. \(C^\top=C\). In particular, graph degree, number of connected components and the presence of loops are unrestricted. Matrix products and updates are over \(\mathbb F_2\). The zero polynomial has valuation \(n\). The polynomial ring \(R=\mathbb F_2[X]/((X+1)^n)\) is local because \(n\) is a power of two; therefore a polynomial is a unit precisely when its value at \(X=1\) is one. Valuation is defined in this ring and may be computed by repeated exact division by \(X+1\).

## Proof
**1. Scalar local-ring reduction and invertibility.** Since \(X^n-1=(X+1)^n\) over \(\mathbb F_2\), the cyclic-coordinate space is the free rank-one \(R\)-module. The full phase space is \(R^2\). The block matrix \(M_C\) is the \(R\)-linear matrix
\[
M=\begin{pmatrix}1&c\\c&1+c^2\end{pmatrix}.
\]
Its determinant is \((1+c^2)+c^2=1\) and its trace is \(c^2\), so it is invertible and satisfies
\[
M^2+c^2M+I=0.
\]
The symmetry condition on \(C\) additionally makes the integer model symplectic and does not enter the finite-field rank calculation.

**2. Even augmentation.** If \(\varepsilon=c(1)=0\), then \(c=(X+1)^vu\) with \(u\) a unit when \(c\ne0\). Factor
\[
M-I=cD,\qquad D=\begin{pmatrix}0&1\\1&c\end{pmatrix},
\]
where \(D\) has determinant one. In characteristic two, for every \(j\ge0\),
\[
M^{2^j}-I=(M-I)^{2^j}=c^{2^j}D^{2^j}.
\]
Consequently its kernel is that of scalar multiplication by \((X+1)^{v2^j}\) on \(R^2\). Multiplication by \((X+1)^h\) on \(R\) has an \(\mathbb F_2\)-kernel of dimension \(\min(n,h)\). Thus \(\#\operatorname{Fix}(M^{2^j})=2^{2\min(n,v2^j)}=Q_j\). Since this map is unipotent, all primitive periods are powers of two; the smallest \(2^j\) giving the identity occurs at \(j=J\). This also covers \(c=0\), where \(v=n\), \(M=I\), and \(J=0\).

**3. Odd augmentation.** If \(\varepsilon=1\), the reduction of \(M\) modulo the maximal ideal \((X+1)\) is
\[
M_0=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]
which has order three; \(M_0-I\) and \(M_0+I\) are both invertible. As a result, \(M+I\) is invertible over \(R\), and any positive iterate whose exponent is not divisible by three has only the zero fixed vector. Using the characteristic polynomial identity,
\[
M^2+M+I=(c^2+1)M=(c+1)^2M.
\]
Therefore
\[
M^3-I=(M+I)(M^2+M+I)=(c+1)^2M(M+I).
\]
Both matrices multiplying \((c+1)^2\) are invertible. Raising to \(2^j\) in characteristic two gives
\[
M^{3\cdot2^j}-I=(c+1)^{2^{j+1}}[M(M+I)]^{2^j},
\]
so its kernel dimension is \(2\min(n,2v2^j)\) and its number of fixed points is \(Q_j\). The exact order is \(3\cdot2^J\). This includes \(c=1\), where \(v=n\) and \(M\) has order three.

**4. Exhaustive orbit lengths and counts.** In both cases the relevant first return operator \(M^b\) is a unipotent element whose order is a power of two. For an odd integer \(r\), \((I+H)^r-I=H U(H)\) with \(U(0)=1\), hence \(U(H)\) invertible for nilpotent \(H\). Thus odd extra factors in a return time cannot enlarge a fixed space. In the odd-augmentation case, a nontrivial return time must also be divisible by three, by reduction modulo \((X+1)\). The only possible lengths are exactly those listed. Subtracting the numbers of fixed points at successive return times gives the number of points of each primitive length; division by its length gives the claimed cycle census. All coefficients are integers because they count actual cycles.

**5. Structural consequence.** The rank and orbit census depend only on whether \(c(1)=0\) and the vanishing order of \(c+\varepsilon\) at \(X=1\). For the illustrated degree-two and degree-four couplings, \(S^a+S^{-a}=S^{-a}(S^a+1)^2\) and \(S^2+S^{-2}\) has valuation four, whereas the \(a=1\) component has valuation two. Their sum retains valuation two, proving identical complete temporal spectra even though their graph degrees differ.

## Verification
Run `python3 verify.py` with standard Python. The program independently builds the binary matrices from symmetric circulant row masks, computes exact matrix powers, Gaussian-elimination ranks and polynomial \((X+1)\)-valuations, and tests the predicted kernel dimensions and exact orders. It checks all symmetric circulant matrices for \(n=4,8,16\) (\(8+32+512=552\) choices), 128 reproducible pseudorandom examples at \(n=32\), and all binary configurations for all eight \(n=4\) couplings. In total 680 coupling matrices are checked, with all assertions passing. The proof is algebraic for arbitrary powers of two; enumeration is a finite consistency check, not an infinite certificate.

## Relationship to prior work
Manolas and Floratos (2026) introduce this symmetric circulant coupled-cat-map construction and calculate general matrix recurrences and selected numerical modular period spectra. Their formulae do not classify **every** binary symmetric circulant coupling using one augmentation valuation, nor do they give the complete all-state primitive cycle counts. The previously investigated nearest-neighbor loopless family, the all-to-all family, and the self-loop variants are individual specializations of the present theorem, not separate claims of novelty here. The new result is the universality across all symmetric circulant connection graphs, including different degrees with indistinguishable binary temporal spectra. The finite local-ring argument is elementary in its ingredients, but the all-graph orbit-spectrum classification is a structural synthesis beyond numerical period tables.

## Limitations
The theorem requires site count a power of two and **binary** phase coordinates; no claim is made for odd site counts, generic phase-grid moduli or the full real chaotic dynamics. The word 'universal' refers to all symmetric binary circulant couplings subject to these hypotheses. Over unindexed earlier literature a general group-ring formulation might already imply the result; this remains a historical-priority risk. The finite verifier does not replace the proof.

## References
- Kimon Manolas and Emmanuel Floratos, *Coupled Arnol'd cat maps on circulant graphs*, arXiv:2605.00965v1, first publicly available May 1, 2026, especially the general model and Section 4.1 on period spectra.
- Minos Axenides, Emmanuel Floratos and Stam Nicolis, *Arnol'd cat map lattices*, arXiv:2208.03267 (2022), for earlier general coupled-map constructions and numerical period studies.

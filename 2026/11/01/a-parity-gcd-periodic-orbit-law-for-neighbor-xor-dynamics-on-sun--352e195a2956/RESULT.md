# A parity–gcd periodic-orbit law for neighbor-XOR dynamics on sunlet graphs

## Finding
For every integer \(n\ge3\), form the labelled sunlet graph \(S_n=C_n\circ K_1\): one pendant leaf is attached to each of the \(n\) vertices of a simple cycle. On the binary state space \(\mathbb F_2^{2n}\), consider the synchronous neighbor-XOR update \(F_n\) sending every vertex state to the sum (modulo two) of all its neighbors' current states. For **every integer \(t\ge1\)** the exact number of configurations returning in \(t\) steps is
\[
\#\operatorname{Fix}(F_n^t)
=2^{\,2\gcd(n,t)-\mathbf 1_{\{n\ \mathrm{odd},\ t\ \mathrm{odd}\}}}.
\]
In particular, no configuration has a transient: the global update is a permutation. Its **exact order**, and hence the largest attainable primitive period, is
\[
L_n=\begin{cases}n,&n\ \mathrm{even},\\2n,&n\ \mathrm{odd}.\end{cases}
\]
For each positive divisor \(d\mid L_n\), the number of distinct primitive cycles of length \(d\), with vertices labelled and states identified only along their time orbit, is
\[
C_n(d)=\frac1d\sum_{e\mid d}\mu(d/e)
2^{\,2\gcd(n,e)-\mathbf 1_{\{n\ \mathrm{odd},\ e\ \mathrm{odd}\}}}.
\]
All other primitive-period counts vanish. For instance, the length-\(3\) sunlet has \(2,1,10,5\) primitive orbits of lengths \(1,2,3,6\), respectively; the length-\(4\) sunlet has \(4,6,60\) of lengths \(1,2,4\). The odd-cycle correction is exactly **one binary dimension** at odd return times; it disappears at all even return times.

## Assumptions and scope
All graph edges are undirected, with no loops or multiple edges; \(n\ge3\) ensures that the rim is a simple cycle. Each rim vertex is indexed by \(i\in\mathbb Z/n\mathbb Z\), and its unique leaf shares index \(i\). There are exactly two binary field values, and updates are simultaneous. Identify the rim and leaf vectors with \(R=\mathbb F_2[x,x^{-1}]/(x^n-1)\), with \(x\) representing a cyclic shift. The update matrix over \(R\) is
\[
A=\begin{pmatrix}s&1\\1&0\end{pmatrix},\qquad s=x+x^{-1}.
\]
The finite ring \(R\) has \(\mathbb F_2\)-dimension \(n\). The notation \(\#\operatorname{Fix}\) counts labelled binary configurations, including the all-zero configuration. No quotient by spatial rotations or reflections is taken.

## Proof
**Step 1: Reversibility and local reduction.** Since \(\det A=1\) in characteristic two, \(A\) is invertible with inverse \(\left(\begin{smallmatrix}0&1\\1&s\end{smallmatrix}\right)\). Every state therefore lies on a periodic orbit. Write \(n=2^a m\) with \(m\) odd and \(a\ge0\), and \(e=2^a\). Since \(x^n-1=(x^m-1)^e\) and \(x^m-1\) is square-free, the Chinese remainder theorem decomposes \(R\) into the primary local factors of the irreducible divisors of \(x^m-1\). The total \(\mathbb F_2\)-dimension of a kernel is the sum of its local contributions.

**Step 2: Every primary factor away from \(x+1\).** The element \(s=(x+1)^2/x\) is a unit on each primary factor belonging to an irreducible polynomial other than \(x+1\). By direct multiplication the vectors \((x,1)^\top\) and \((x^{-1},1)^\top\) are eigenvectors of \(A\) with eigenvalues \(x\) and \(x^{-1}\). Their determinant is \(x+x^{-1}=s\), a local unit. Hence \(A\) is conjugate over each such factor to \(\operatorname{diag}(x,x^{-1})\). The dimensions of the two local fixed kernels for \(A^t\) are both exactly the corresponding local degree of \(\gcd(x^n-1,x^t-1)\). This follows directly from multiplication by \(x^t-1\) on a quotient of \(\mathbb F_2[x]\); multiplying by \(x^{-t}\) changes no kernel.

**Step 3: The exceptional primary factor \(x+1\).** Here \(R_0=\mathbb F_2[y]/(y^e)\) for \(y=x+1\), and \(s=y^2/x\), where \(x=1+y\) is a unit. Put \(B=A+I\). Its matrix has a unit off-diagonal entry, and \(\det B=s\); consequently, elementary invertible row and column operations reduce \(B\) to the diagonal matrix \(\operatorname{diag}(1,s)\). Thus
\[
\dim_{\mathbb F_2}\ker B=\min(e,2).
\]
If \(t\) is odd, write \(A^t+I=(A+I)Q_t(A)\), with \(Q_t(z)=1+z+\cdots+z^{t-1}\). The matrix \(A\bmod y\) has characteristic polynomial \((z+1)^2\) and is unipotent. Since \(Q_t(1)=1\) for odd \(t\), \(Q_t(A)\bmod y\) is invertible; invertibility lifts to the local ring \(R_0\). Therefore \(\dim\ker(A^t+I)=\min(e,2)\) on this exceptional factor when \(t\) is odd.

If \(t=2^c u\) with \(c\ge1\) and odd \(u\), the same invertibility gives
\[
A^t+I=(A^u+I)^{2^c}=B^{2^c}Q_u(A)^{2^c}.
\]
The characteristic identity \(A^2+sA+I=0\) implies \(B^2=sA\), and therefore \(B^{2^c}=s^{2^{c-1}}A^{2^{c-1}}\). Since \(A\) is a unit and \(s\) is a unit times \(y^2\), multiplication by \(B^{2^c}\) has kernel dimension \(2\min(e,2^c)\). This is exactly twice the \(x+1\)-primary degree in \(\gcd(x^n-1,x^t-1)\), because \(x^t-1\) vanishes to multiplicity \(2^c\) at \(x=1\).

**Step 4: Summation.** Over \(\mathbb F_2\), the polynomial identity
\[
\gcd(x^n-1,x^t-1)=x^{\gcd(n,t)}-1
\]
gives total gcd degree \(\gcd(n,t)\). When \(t\) is even, Step 3 supplies twice the exceptional degree, so every factor together gives \(\dim\ker(A^t+I)=2\gcd(n,t)\). When \(t\) is odd, the exceptional gcd degree is one and its fixed-kernel contribution is \(\min(e,2)\). This equals one if \(n\) is odd and two if \(n\) is even. The total fixed-kernel dimension is therefore \(2\gcd(n,t)-1\) exactly when \(n,t\) are both odd, and \(2\gcd(n,t)\) otherwise. Taking the power of two proves the fixed-state formula.

**Step 5: Exact order and cycle counts.** For even \(n\), the fixed space at \(t=n\) has dimension \(2n\), so \(A^n=I\); no smaller positive exponent has full fixed dimension, since that would require \(n\mid t\). For odd \(n\), the fixed space at \(t=n\) has dimension \(2n-1\), whereas \(t=2n\) has dimension \(2n\). No smaller positive exponent can be the identity because the full dimension requires both \(t\) even and \(n\mid t\). Thus the order is \(L_n\) as claimed. For an invertible linear transformation over a finite field, rational canonical form has invariant factors ordered by divisibility; the last companion block has the full matrix order because every other block order divides it. A cyclic generator of this block therefore has primitive period exactly \(L_n\). Finally, Möbius inversion of \(\#\operatorname{Fix}(A^t)=\sum_{d\mid t}d C_n(d)\) yields the displayed exact primitive-orbit formula.

## Verification
The companion standalone Python 3 script `verify.py` calculates GF(2) powers and ranks of the actual \(2n\)-vertex adjacency matrices without using the polynomial proof. It compares the predicted fixed dimensions against **1,200 matrix-rank cases**, comprising every \(3\le n\le32\) and every \(1\le t\le2n+5\). It also checks the exact matrix orders for these sizes, exhaustively enumerates all **21,824** binary configurations for sizes \(3\le n\le7\), and compares **19** directly enumerated primitive-cycle counts with Möbius inversion. All checks passed. Run `python3 verify.py` with no dependencies outside the Python standard library; the exact replay output is embedded as `verification_output.txt`. Finite checks are corroboration, not a proof for all \(n,t\).

## Relationship to prior work
The reversible two-step formulation \(u_{j+1}=u_{j-1}+u_{i-1}+u_{i+1}\) is a known second-order Rule 90 cellular-automaton construction; reversible second-order and matrix formulations appear in Macfarlane (2004). The novelty assessed here is **not** the reversible construction, but the complete all-length, all-time formula for labelled fixed states and primitive cycles under periodic boundary conditions, with a sharp odd/odd exception and exact maximum period. Boulet (2009) studies sun-graph spectral characterizations, not these binary temporal return counts. Aledo, Martínez and Valverde (2015) survey finite graph update dynamics without deriving these sunlet-specific formulas. Kari and Taati (2013) provide broader reversible/surjective cellular-automaton theory rather than this finite-ring orbit census. Closely related earlier classifications of sunlet dynamics under different, nonlinear majority updates do not imply this result. The power-of-two rim case can also be obtained from the known doubled nilpotent Jordan chains for leaf coronas; the new part includes every non-power-of-two length and an all-return-time formula. The directly related 2004 paper could not be checked in full, so stronger historical overlap remains possible.

## Limitations
The theorem applies to the binary field, synchronous neighbor-XOR updates and precisely one pendant leaf at each rim vertex. It says nothing about asynchronous scans, other moduli, incomplete leaf coronas, or nonlinear diffusion and majority rules. It counts labelled states, not graph-automorphism orbits. The full text of Macfarlane (2004), a directly relevant predecessor on reversible second-order cellular automata, was unavailable during this comparison; its accessible abstract states its focus on single-seed weight sequences rather than all periodic-boundary configurations, but no assertion of noncoverage rests on the abstract alone. Exact originality in older, inaccessible or differently formulated literature is not certified, and no independent audit was performed.

## References
1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A: Mathematical and General 37 (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006. First online 28 October 2004.
2. R. Boulet, *Spectral characterizations of sun graphs and broken sun graphs*, Discrete Mathematics & Theoretical Computer Science 11 (2009). DOI: 10.46298/dmtcs.456. Full open-access PDF inspected.
3. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, arXiv:1311.2319 (first posted 10 November 2013), open-access text inspected.
4. J. A. Aledo, S. Martínez, and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Advances in Mathematical Physics (2015), Article ID 594294. DOI: 10.1155/2015/594294. Full HTML inspected.

# Complete cycle census of the three-step Fibonacci recurrence modulo powers of three

## Finding
For every integer \(k\ge1\), the map \(T(a,b,c)=(b,c,a+b+c)\) on \((\mathbb Z/3^k\mathbb Z)^3\) has exactly one fixed point, the zero vector. For each \(1\le t\le k\) it has exactly \(2\cdot9^{t-1}\) distinct cycles of least length \(13\cdot3^{t-1}\), and no other cycles. Hence its total number of cycles is exactly \((9^k+3)/4\). More precisely, the least period of every nonzero vector divisible by \(3^{k-t}\) but not by \(3^{k-t+1}\) is \(13\cdot3^{t-1}\).

This proves the power-of-three specialization that OEIS A106285 identifies as an apparent match with A054879, and gives the complete period spectrum rather than only the total.

## Assumptions and scope
Let \(k\) be any positive integer and work over \(R_k=\mathbb Z/3^k\mathbb Z\). The state space consists of all ordered triples, not merely the standard Tribonacci seed. Let \(T(a,b,c)=(b,c,a+b+c)\). A cycle is an orbit under this permutation; its least period is its cardinality. For nonzero \(v\in R_k^3\), define \(s=\min_{1\le i\le3}\min(k,\nu_3(v_i))\) using integer representatives, and \(t=k-s\).

## Proof
In the coordinate convention \(v=(a,b,c)^T\), the companion matrix is
\[A=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix}.\]
Direct integer multiplication gives
\[A^{13}=\begin{pmatrix}274&423&504\\504&778&927\\927&1431&1705\end{pmatrix},\quad
Q=\frac{A^{13}-I}{3}=\begin{pmatrix}91&141&168\\168&259&309\\309&477&568\end{pmatrix},\quad\det Q=106.\]
Thus \(A^{13}\equiv I\pmod3\), \(A\not\equiv I\pmod3\), and \(Q\) is invertible modulo three. As 13 is prime, the order of \(A\bmod3\) is exactly 13. Its characteristic polynomial is \(x^3-x^2-x-1\), which has no root in \(\mathbf F_3\), hence is irreducible. Consequently every nonzero vector modulo three has least period 13 (if \(A^jv=v\) for \(0<j<13\), primality of 13 forces \(Av=v\), impossible by irreducibility).

For every integer \(r\ge0\), write
\[A^{13\cdot3^r}=I+3^{r+1}Q_r,\quad Q_r\equiv Q\pmod3.\]
The base case is above; the induction follows by expanding \((I+3^{r+1}Q_r)^3\), where after division by \(3^{r+2}\) all terms except \(Q_r\) are divisible by three. In particular all \(Q_r\) are invertible modulo three and over \(\mathbb Z/3^t\mathbb Z\).

A primitive vector \(w\) modulo \(3^t\) has reduction nonzero mod three, hence its period is divisible by 13. Since \(A^{13}\equiv I\pmod3\), its remaining period is a power of three. For \(r\ge0\),
\[(A^{13\cdot3^r}-I)w=3^{r+1}Q_rw\equiv0\pmod{3^t}\quad\Longleftrightarrow\quad r+1\ge t,\]
because \(Q_rw\) is primitive. Therefore its least period is precisely \(13\cdot3^{t-1}\). Every nonzero state of exact coordinate valuation \(s=k-t\) corresponds bijectively to a primitive vector modulo \(3^t\), so the same period formula holds at precision \(k\).

There are \(3^{3t}-3^{3(t-1)}=26\cdot3^{3t-3}\) vectors with exact coordinate valuation \(k-t\). Dividing by the common period gives \(2\cdot3^{2t-2}=2\cdot9^{t-1}\) cycles. The zero vector is fixed and no other periods occur. Summation yields \[1+2\sum_{t=1}^k9^{t-1}=\frac{9^k+3}{4}.\]

## Verification
Execute the standalone `verify.py` with Python 3. It checks the displayed integer matrix certificate and independently traces all states for precisions \(1\le k\le3\), comparing exact length spectra with the theorem. Finite checks support but do not replace the universal argument.

## Relationship to prior work
OEIS A106285, created May 2, 2005, explicitly records that the number of three-step Fibonacci cycles at prime powers of three *appears* to agree with A054879, whose closed formula is \((9^k+3)/4\). This theorem supplies a proof, as well as the missing exact cycle-length multiplicities. OEIS A106288 lists the number of distinct possible periods, not their full multiplicities. Robinson's 1963 work discusses companion-matrix periodicity for ordinary two-step Fibonacci sequences and a general matrix method; that general method motivates rather than literally states the above 3-step 3-adic classification. This conclusion assumes no later or unlocated equivalent theorem.

## Limitations
The theorem is for the all-ones three-step recurrence and moduli \(3^k\). It does not enumerate cycles for other moduli or higher-step recurrences. The result uses standard lifting arguments; broad existing companion-matrix results may implicitly contain this specialization. Literature coverage is limited to the cited inspected material, not the total literature. Independent validation has not been conducted.

## References
- T. D. Noe, OEIS A106285, *Number of orbits of the 3-step recursion mod n*, May 2, 2005, https://oeis.org/A106285.
- P. Dominici, OEIS A054879, *Closed walks of length 2n along the edges of a cube based at a vertex*, May 23, 2000, https://oeis.org/A054879.
- T. D. Noe, OEIS A106288, *Number of different orbit lengths of the 3-step recursion mod n*, May 2, 2005, https://oeis.org/A106288.
- D. W. Robinson, *The Fibonacci Matrix Modulo m*, Fibonacci Quarterly 1 (1963), 29–36, https://www.fq.math.ca/Scanned/1-2/robinson.pdf.

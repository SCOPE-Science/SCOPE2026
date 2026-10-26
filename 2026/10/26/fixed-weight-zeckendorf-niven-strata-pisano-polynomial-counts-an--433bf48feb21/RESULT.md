# Fixed-weight Zeckendorf–Niven strata: Pisano-polynomial counts and an adjacency correction

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For every fixed integer \(s\ge 2\), put
\[
C_s(L)=\#\{1\le n<F_{L+2}:\text{the Zeckendorf expansion of }n\text{ has exactly }s\text{ summands, and }s\mid n\}.
\]
Write \(h=\pi(s)\) for the Pisano period of Fibonacci numbers modulo \(s\), and work in the cyclic group ring \(R_s=\mathbb Z[X]/(X^s-1)\). Define
\[
A_s(X)=\sum_{j=0}^{h-1}X^{F_j},\qquad B_s(X)=\sum_{j=0}^{h-1}X^{2F_j},\qquad
T_{s,r}=[X^0]A_s(X)^r,\qquad U_s=[X^0]B_s(X)A_s(X)^{s-2},
\]
where \([X^0]\) means the coefficient of the identity element after reduction modulo \(X^s-1\). Then the following constitute one counting theorem.

For every residue \(0\le r<h\), the function \(q\mapsto C_s(qh+r)\) agrees, for all sufficiently large integers \(q\), with a rational-coefficient polynomial of degree at most \(s\). On the full-period subsequence it satisfies the explicit two-term formula
\[
\boxed{C_s(qh)=\frac{T_{s,s}}{s!}q^s-\frac{U_s/2+T_{s,s-1}}{(s-2)!}q^{s-1}+O_s(q^{s-2}).}
\]
Here \(q\) ranges over positive integers tending to infinity, with \(s\) held fixed; the implicit constant may depend on \(s\). In particular, among Zeckendorf expansions supported at indices \(2,\ldots,L+1\) and having exactly \(s\) summands, the fraction satisfying the Niven divisibility condition tends to the explicitly computable rational number
\[
\boxed{\rho_s=\frac{T_{s,s}}{h^s}.}
\]
The first values are
\[
\rho_2=\frac59,\qquad \rho_3=\frac{85}{256},\qquad
\rho_4=\frac7{27},\qquad \rho_5=\frac15.
\]
Thus the conditional divisibility fraction is not generally the naive value \(1/s\); its bias can have either sign.

In the first four nontrivial strata, the eventual quasi-polynomial on full Pisano blocks is in fact an exact polynomial for **every** integer \(q\ge1\):
\[
\begin{aligned}
C_2(3q)&=(5q^2-5q+2)/2,\\
C_3(8q)&=(85q^3-99q^2+35q-6)/3,\\
C_4(6q)&=(28q^4-84q^3+91q^2-45q+10)/2,\\
C_5(20q)&=16000q^5/3-8000q^4+14200q^3/3-1380q^2+559q/3-14.
\end{aligned}
\]

## Assumptions and scope
All counts are of **positive** integers, not word representations with leading zero as separate multiplicities. Zeckendorf uniqueness identifies them bijectively with subsets of \(\{2,\ldots,L+1\}\) having no two adjacent indices. The total number of expansions with exactly \(s\) summands is \(\binom{L-s+1}{s}\) for \(L\ge2s-1\). The theorem concerns fixed weight \(s\) as the largest available Fibonacci index grows, not a variable summand count of order \(L\). The Pisano period is a valid quasi-polynomial period, not necessarily the least one.

## Proof
**1. Periodic transfer and eventual polynomiality.** Introduce variables \(y\) for the number of selected indices and \(X\) for their Fibonacci-value residue modulo \(s\). If the last index is respectively unselected or selected, the two generating components evolve under
\[
M_i(y,X)=\begin{pmatrix}1&1\\yX^{F_i}&0\end{pmatrix}
\quad(i\ge2).
\]
Starting from \(v=(1,0)^\mathsf T\), the coefficient \([y^sX^0]\) of \((1,1)M_{L+1}\cdots M_2v\) is exactly \(C_s(L)\). Set \(P=M_{h+1}\cdots M_2\), and \(R_r=M_{r+1}\cdots M_2\) (the empty product is the identity). Fibonacci periodicity gives
\[
C_s(qh+r)=[y^sX^0](1,1)R_rP^qv.
\]
All calculations may be performed in \(R_s[y]/(y^{s+1})\). At \(y=0\), each \(M_i\) is the rank-one idempotent matrix with rows \((1,1)\) and \((0,0)\); hence \(\det(I-tP)|_{y=0}=1-t\). The matrix generating function
\[
\sum_{q\ge0}t^qR_rP^q=R_r(I-tP)^{-1}
\]
has, on extracting the coefficient of \(y^s\), denominator dividing \((1-t)^{s+1}\): expand the inverse determinant as a finite series in its positive-\(y\)-degree part. Thus each scalar coefficient series has no poles except at \(t=1\), with pole order at most \(s+1\). Its coefficients are eventually polynomial in \(q\) of degree at most \(s\).

**2. Two leading coefficients before the adjacency restriction.** Consider arbitrary \(s\)-element subsets of the same \(qh\) indices, temporarily allowing adjacent choices. The generating product is exactly
\[
\prod_{i=2}^{qh+1}(1+yX^{F_i})
=\left(\prod_{j=0}^{h-1}(1+yX^{F_j})\right)^q.
\]
In the ring with rational coefficients, the logarithm of the inner product is \(yA_s-y^2B_s/2+O(y^3)\). Extracting \([y^sX^0]\) from its \(q\)th power gives
\[
\frac{T_{s,s}}{s!}q^s-\frac{U_s}{2(s-2)!}q^{s-1}+O_s(q^{s-2}).
\]

**3. Adjacent-pair correction.** An excluded adjacent pair occupying indices \(i,i+1\) contributes \(X^{F_i+F_{i+1}}=X^{F_{i+2}}\). Summing over the \(qh-1\) allowable edges gives \(qA_s+O_s(1)\) in \(R_s\), because one edge of a complete periodic block is omitted. Having marked one such edge, the other \(s-2\) choices contribute at leading order \(q^{s-2}A_s^{s-2}/(s-2)!\). Configurations with two marked adjacency events, a triple of consecutive selected indices, or an incidental index collision number only \(O_s(q^{s-2})\): each imposes at least two independent restrictions on the \(s\) positions. Therefore the one-edge correction is
\[
\frac{T_{s,s-1}}{(s-2)!}q^{s-1}+O_s(q^{s-2}).
\]
Subtracting this from the unrestricted count proves the two-term formula. In particular, the Fibonacci addition law collapses the entire edge-residue correction to the lower convolution coefficient \(T_{s,s-1}\).

**4. Density.** The number of legal \(s\)-element index sets is \(\binom{qh-s+1}{s}=(qh)^s/s!+O_s(q^{s-1})\). Division yields \(T_{s,s}/h^s+O_s(q^{-1})\) on full blocks. For an arbitrary \(L=qh+r\), \(0\le r<h\), appending at most \(h-1\) positions changes the count by \(O_s(L^{s-1})\), and does the same to the unrestricted denominator; hence the same limiting fraction holds without restricting \(L\) to full periods.

**5. Exact small-weight polynomials.** For \(s=2,3,4,5\), respectively, the Pisano periods are \(3,8,6,20\), all strictly larger than \(s\). In the degree-\(s\) truncation of the cyclic group ring, \(\det P=(-y)^hX^{\sum_{j=0}^{h-1}F_j}\) vanishes. Because the two eigenvalues of \(P\) have distinct constant terms \(1\) and \(0\), they split as formal power series; the small eigenvalue has \(y\)-order at least \(h\), so its \(q\)th power vanishes after truncation for every \(q\ge1\). The remaining eigenvalue equals \(1+O(y)\), and its \(q\)th power is a degree-at-most-\(s\) polynomial in \(q\) after extraction of \(y^s\). Thus \(C_s(qh)\) is polynomial in \(q\) for **all** \(q\ge1\), not just eventually. Exact transfer evaluation at \(q=1,\ldots,s+1\) gives the following integer data, uniquely determining the printed formulas:

| \(s\) | \(h\) | Values at \(q=1,\ldots,s+1\) |
|---|---:|---|
| 2 | 3 | 1, 6, 16 |
| 3 | 8 | 5, 116, 501, 1330 |
| 4 | 6 | 0, 30, 347, 1539, 4530 |
| 5 | 20 | 859, 75372, 763925, 3694918, 12224751, 32077824 |

These values are independently reproducible with the bundled exact-integer checker; the preceding transfer argument, not interpolation alone, proves that the formulas hold for every \(q\ge1\).

## Verification
Run `python3 verify_fixed_layers.py` using a Python 3 standard library. The checker enumerates legal index subsets independently for small lengths and compares against the residue transfer dynamic program; verifies the full polynomial identities for \(1\le q\le16\); and independently computes \(T_{s,s}\), \(U_s\), and the resulting rational limiting probabilities for \(s=2,3,4,5\). Successful output begins with `VERIFY_OK`. The code is a finite consistency test; the proof above covers all fixed weights and all admissible lengths.

## Relationship to prior work
Lao, Miller, Rosa, Shiliaev, Tresch, Wong and Zhang (arXiv:2606.24006, first submitted June 22, 2026) proved infinitely many Zeckendorf–Niven integers in each arithmetic progression and studied consecutive runs. Their Sections 2–5 do not state a polynomial fixed-weight stratum count, a Pisano-convolution limiting proportion, or the second-order adjacency term. Ray and Cooper proved that the unrestricted set of Zeckendorf–Niven integers has natural density zero; this does not determine the conditional fraction among integers having exactly a fixed number of Zeckendorf summands. Koloğlu, Kopp, Miller and Wang studied the Gaussian distribution of the number of summands without the simultaneous Niven congruence. Generic finite-state rational generating-function methods explain eventual quasi-polynomiality in principle; the arithmetic formulas, Fibonacci-specific second term, and exact low-weight polynomials are the present distinction.

## Limitations
The index cutoffs are Fibonacci cutoffs, and \(s\) is held fixed. No unconditional density for Zeckendorf–Niven integers as a whole, no least quasipolynomial period, and no uniform asymptotic for growing \(s\) is claimed. The older Ray–Cooper full article was not materially available during comparison; its abstract supports only the density-zero result. The chance of an equivalent general fixed-weight residue-count theorem in unindexed literature remains a priority risk.

## References
1. K. Lao, S. J. Miller, N. Rosa, M. Shiliaev, G. Tresch, T. W. H. Wong and H. Zhang, *On Zeckendorf-Niven numbers and arithmetic progressions*, arXiv:2606.24006v1 (June 22, 2026), https://arxiv.org/abs/2606.24006 ; accessible public full text: https://www.researchgate.net/publication/407644844_On_Zeckendorf-Niven_numbers_and_arithmetic_progressions .
2. A. Ray and C. Cooper, *On the natural density of the k-Zeckendorf Niven numbers*, J. Inst. Math. Comput. Sci. Math. Ser. 19 (2006), 83–98, https://www.researchgate.net/publication/265778462_On_the_natural_density_of_the_k-Zeckendorf_Niven_numbers .
3. M. Koloğlu, G. Kopp, S. J. Miller and Y. Wang, *On the number of summands in Zeckendorf decompositions*, Fibonacci Quarterly 49 (2011), 116–130, https://www.maths.ox.ac.uk/node/36538 .
4. D. D. Wall, *Fibonacci series modulo m*, American Mathematical Monthly 67 (1960), 525–532.

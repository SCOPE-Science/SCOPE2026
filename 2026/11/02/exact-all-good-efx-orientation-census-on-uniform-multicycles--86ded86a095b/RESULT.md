# Exact all-good EFX orientation census on uniform multicycles

## Finding

For integers \(n\ge 3\) and \(q\ge 1\), let \(C_n^{(q)}\) have \(n\) labeled agents on a simple cycle and \(q\) individually distinguishable parallel goods on each consecutive pair. Each good has additive value one to each endpoint and zero to other agents. An orientation allocates every good to one endpoint. Impose **all-good EFX**: for all distinct agents \(i,j\) and every good \(g\) allocated to \(j\), \(v_i(X_i)\ge v_i(X_j\setminus\{g\})\), including goods of value zero to \(i\).

Let \(N_{n,q}\) count such orientations, with different allocations of distinguishable parallel goods counted separately. Put \(\mathcal S_q=\{0,\dots,q\}^2\) and define the integer \((q+1)^2\)-square matrix \(T_q\) by
\[
(T_q)_{(a,b),(b',c)}=\begin{cases}
\binom qc,&b'=b,\quad c\le 2b+\mathbf1_{a=0},\quad 2b\le a+q+\mathbf1_{c=q},\\
0,&\text{otherwise}.
\end{cases}
\]
Then, for every \(n\ge3\) and \(q\ge1\),
\[
\boxed{N_{n,q}=\operatorname{tr}(T_q^n).}
\]
The first two genuine parallel-edge cases admit unexpectedly small, exact characteristic factors:
\[
\det(\lambda I-T_2)=\lambda^4(\lambda^2+1)(\lambda^3-4\lambda^2+4\lambda-2),
\]
\[
\det(\lambda I-T_3)=\lambda^{12}(\lambda-1)(\lambda^3-7\lambda^2+6\lambda-6).
\]
In particular, if \(U_0=3,U_1=4,U_2=8\) and \(U_{r+3}=4U_{r+2}-4U_{r+1}+2U_r\), and if \(V_0=3,V_1=7,V_2=37\) and \(V_{r+3}=7V_{r+2}-6V_{r+1}+6V_r\), then
\[
\boxed{N_{n,2}=U_n+2\cos(n\pi/2),\qquad N_{n,3}=V_n+1.}
\]
For \(n=3,4,5,6,7,8\), respectively, the double-edge counts are \(22,66,184,522,1488,4226\), and the triple-edge counts are \(236,1466,9068,56090,347012,2146946\).

If every good is oriented independently and fairly, the sharp exponential decay bases of the probability of all-good EFX are \(\rho_2/4\) and \(\rho_3/8\), respectively, where \(\rho_2=2.839286755\ldots\) is the unique real root of \(t^3-4t^2+4t-2\), and \(\rho_3=6.186964983\ldots\) is the unique real root of \(t^3-7t^2+6t-6\). Numerically these bases are \(0.709821688\ldots\) and \(0.773370623\ldots\). In particular, the normalized EFX survival base is strictly larger with three goods per adjacency than with two: \[\rho_2/4<3/4<\rho_3/8.\]

## Assumptions and scope

Cycles have at least three *distinct* agents and no loops. Each edge class contains exactly \(q\) distinguishable goods, each valued one by its two endpoints and zero elsewhere; valuations are additive and identical on incident goods. No goods may be discarded or allocated to a non-endpoint. The EFX quantifier ranges over **every** good in the other bundle, even one of zero value to the envier (sometimes distinguished from the weaker \(\mathrm{EFX}_0\) convention). The formula is not an enumeration of unrestricted nonorientation EFX allocations, nor does it cover arbitrary weights or nonuniform multiplicities.

## Proof

Number agents and edge classes by \(i\in\mathbb Z/n\mathbb Z\), with class \(i\) joining \(i\) to \(i+1\). Define \(x_i\in\{0,\dots,q\}\) as the number of goods of class \(i\) going to agent \(i+1\). Thus agent \(i\)'s own total is \(L_i=x_{i-1}+q-x_i\). Her valuation for her left neighbor's bundle is \(q-x_{i-1}\); her valuation for her right neighbor's bundle is \(x_i\); nonneighbors' bundles have zero value.

For left-neighbor comparison, the latter also holds \(x_{i-2}\) goods of the previous class, all of zero value to \(i\). If \(x_{i-2}>0\), all-good EFX demands \(L_i\ge q-x_{i-1}\), since deleting one such zero-valued good leaves this valuation unchanged. If \(x_{i-2}=0\), the left neighbor holds only \(q-x_{i-1}\) shared goods, so the sharp inequality is \(L_i\ge q-x_{i-1}-1\); this is automatically valid when that bundle is empty. Together these are precisely
\[
 x_i\le 2x_{i-1}+\mathbf 1_{x_{i-2}=0}.
\]
Similarly, her right neighbor holds \(q-x_{i+1}\) goods not valued by \(i\), and all-good EFX toward the right requires
\[
 2x_i\le x_{i-1}+q+\mathbf 1_{x_{i+1}=q}.
\]
The two displayed conditions for all agents are thus equivalent to the length-three-window conditions, for every cyclic index \(i\),
\[
 x_i\le 2x_{i-1}+\mathbf1_{x_{i-2}=0},\qquad
 2x_{i-1}\le x_{i-2}+q+\mathbf1_{x_i=q}.
\]
The transfer matrix \(T_q\) records exactly these two conditions on the triple \((a,b,c)=(x_{i-2},x_{i-1},x_i)\), progressing between overlapping two-coordinate states. Each cyclic closed walk of length \(n\) corresponds bijectively to a cyclic profile \((x_i)_{i\in\mathbb Z/n\mathbb Z}\). For a fixed profile, the goods of class \(i\) have \(\binom q{x_i}\) distinct assignments realizing that count. The product of these multiplicities is exactly the product of transfer weights around the walk. Taking the trace proves the general formula.

For the two small multiplicities, order states \((a,b)\) lexicographically. Form the matrix entrywise above. Exact determinant expansion gives the displayed two characteristic polynomials. This finite identity can also be reconstructed using only integer traces and Newton's identities: write \(D(z)=\det(I-zT_q)=\sum_{k=0}^{(q+1)^2}d_k z^k\), let \(d_0=1\), \(s_j=\operatorname{tr}(T_q^j)\), and compute
\[
 k d_k=-\sum_{j=1}^k d_{k-j}s_j.
\]
For \(q=2\), this gives \(D(z)=(1+z^2)(1-4z+4z^2-2z^3)\). For \(q=3\), it gives \(D(z)=(1-z)(1-7z+6z^2-6z^3)\), with all higher \(d_k\) zero. These equalities can be checked exactly by the included dependency-free verifier; they are finite determinant certificates, not conjectures inferred from numerical samples.

Each power trace is the sum of \(n\)-th powers of eigenvalues, with algebraic multiplicities. The cubic factors give the stated recurrences by Newton's identities, the quadratic factor \(\lambda^2+1\) contributes \(2\cos(n\pi/2)\), and the linear factor \(\lambda-1\) contributes one.

Finally, each cubic has exactly one real zero beyond two, respectively six, as is seen by its critical-point signs. Its remaining conjugate roots have moduli \(\sqrt{2/\rho_2}<1\) and \(\sqrt{6/\rho_3}<1\) by the product of roots. All extra roots have absolute value at most one, so \(N_{n,2}\sim\rho_2^n\) and \(N_{n,3}\sim\rho_3^n\). There are \(2^{qn}\) equally likely labeled orientations, proving the two probability bases. Also, the cubic for \(\rho_2\) is negative at two and positive at three, whereas the cubic for \(\rho_3\) is negative at six and positive at seven; uniqueness of the real roots gives \(\rho_2<3<\rho_3/2\), which proves the strict comparison of survival bases.

## Verification

The included \(verify.py\) is a standalone Python 3 script using only the standard library. Run `python3 verify.py` from the directory containing the file. It independently constructs each individual labeled-good orientation and tests every ordered pair of agents and **every good** in the other bundle, including zero-valued goods. It compares this direct enumerator to the weighted transfer-matrix trace for \(21\) parameter pairs: \(q=1\), \(3\le n\le10\); \(q=2\), \(3\le n\le8\); \(q=3\), \(3\le n\le6\); \(q=4\), \(3\le n\le4\); \(q=5,n=3\). This examines \(491320\) labeled orientations. It independently computes the characteristic polynomials from traces using integer Newton identities for \(q=1,2,3\). The analytical argument, not finite sampling, handles all \(n,q\) in scope.

## Relationship to prior work

Afshinmehr, Ashuri, Mahmoudkhan, Mehlhorn, and Shahrezaei (2026) establish the existence and computability of EFX **allocations** for general multigraphs under cancelable valuations, with a full definition of all-good EFX; existence does not determine counts of **orientations**. Afshinmehr, Danaei, Kazemi, Mehlhorn, and Rathi (initial 2024 preprint, later updated) study existence of EFX allocations on multicycles and orientability boundaries for bipartite multigraphs, not an exact enumerator for homogeneous parallel-edge cycles. Kanellopoulos et al. (2025) study decision complexity and minimum charity for EF(X) orientations, not counts. Earlier exact enumeration for simple, one-good-per-class cycles does not imply the present double/triple-edge spectra; enumeration of multistars does not imply cycle counts. Thus the contribution is the all-multiplicity transfer law and explicit smallest genuinely parallel-edge characteristic factors and rarity rates, rather than EFX existence itself.

## Limitations

These counts are for homogeneous, incident-unit additive valuations and orientation-only allocations. The exact small characteristic factors are proved for \(q=2,3\), not claimed for every multiplicity. The general transfer formula gives an exact finite computation but is not a uniform closed radical formula for arbitrary \(q\). The verification checks finitely many parameter values; the infinite statement rests on the local-constraint bijection. As with any literature comparison, unindexed equivalent enumeration results may exist; this is not an independent audit or certification.

## References

- M. Afshinmehr, A. Ashuri, P. Mahmoudkhan, K. Mehlhorn, and A. M. Shahrezaei, *EFX Allocations Exist on Multi-Graphs* (first public June 17, 2026), https://arxiv.org/abs/2606.18665.
- M. Afshinmehr, A. Danaei, M. Kazemi, K. Mehlhorn, and N. Rathi, *EFX Allocations and Orientations on Bipartite Multi-graphs: A Complete Picture* (first public October 22, 2024), https://arxiv.org/abs/2410.17002.
- S. Kanellopoulos, E. Nemery, C. Pergaminelis, M. M. Sotiriou, and M. Vasilakis, *EF(X) Orientations: A Parameterized Complexity Perspective* (first public December 31, 2025), https://arxiv.org/abs/2512.25033.
- K. Hsu, *EFX Orientations of Multigraphs* (2025 conference paper), https://doi.org/10.3233/FAIA251259.

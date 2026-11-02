# The exact trace spectrum in the first centered box of integral symplectic four-matrices

## Finding

Consider the standard integral symplectic group of rank two, with form
\[\Omega=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix},\qquad \operatorname{Sp}_2(\mathbb Z)=\{M\in M_4(\mathbb Z):M^{\mathsf T}\Omega M=\Omega\}.\]
The first nonempty centered sup-norm box is
\[\mathcal B_1=\{M\in\operatorname{Sp}_2(\mathbb Z):\max_{1\le i,j\le4}|M_{ij}|\le1\}.\]
Its exact trace enumerator is
\[\boxed{\sum_{M\in\mathcal B_1}z^{\operatorname{tr}M+4}=561(1+z^8)+1000(z+z^7)+1900(z^2+z^6)+2840(z^3+z^5)+4710z^4.}\]
Thus \(|\mathcal B_1|=17{,}312\), and the trace multiplicities at \(-4,-3,-2,-1,0,1,2,3,4\) are respectively \(561,1000,1900,2840,4710,2840,1900,1000,561\). The sequence is symmetric and strictly increases toward trace zero.

## Assumptions and scope

Entries are integers in \(\{-1,0,1\}\), the symplectic form is the explicitly displayed standard \(4\)-dimensional form, and the box is centered at the zero matrix with *inclusive* radius one. The count is by actual integer matrices, without conjugation or reduction modulo an integer. The trace is the ordinary integer trace. No sampling or asymptotic approximation enters the assertion. This is the first higher-rank case after \(\operatorname{Sp}_1(\mathbb Z)=\operatorname{SL}_2(\mathbb Z)\).

## Proof

Write \(M=(v_1\ v_2\ w_1\ w_2)\) in columns, with each vector in \(V=\{-1,0,1\}^4\). Define the integral alternating form
\[J(x,y)=x_1y_3+x_2y_4-x_3y_1-x_4y_2.\]
Expanding \(M^{\mathsf T}\Omega M=\Omega\) shows it is equivalent to the six scalar equations
\[J(v_1,v_2)=J(w_1,w_2)=0,\qquad J(v_i,w_j)=\delta_{ij}\quad(1\le i,j\le2).\]
The remaining pairings are automatic by alternating symmetry. In particular \(v_1,v_2\) cannot be zero. For each of the \(80^2\) ordered nonzero pairs \((v_1,v_2)\), discard the pair unless \(J(v_1,v_2)=0\), and form the *explicit finite sets*
\[W_1(v_1,v_2)=\{w\in V:J(v_1,w)=1,\ J(v_2,w)=0\},\]
\[W_2(v_1,v_2)=\{w\in V:J(v_1,w)=0,\ J(v_2,w)=1\}.\]
Every admissible matrix is obtained **exactly once** by selecting \(w_1\in W_1\), \(w_2\in W_2\), and retaining the pair exactly when \(J(w_1,w_2)=0\). Conversely all such selections satisfy the full matrix identity, so the procedure is both sound and exhaustive. Its trace is \((v_1)_1+(v_2)_2+(w_1)_3+(w_2)_4\).

The complete exact evaluation of these bounded integer loops is certified by the accompanying executable `verify_sp4.py`. The number of ordered first-column pairs yielding exactly \(c\) admissible completions is:

| \(c\) | \(8\) | \(9\) | \(12\) | \(14\) | \(18\) | \(21\) | \(27\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| pairs | 512 | 128 | 416 | 128 | 96 | 128 | 32 |

All other pairs have zero completions. These seven figures total \(1{,}440\) contributing ordered pairs, and their weighted sum is
\[8\cdot512+9\cdot128+12\cdot416+14\cdot128+18\cdot96+21\cdot128+27\cdot32=17312.\]
Accumulating the explicitly specified trace alongside each completed column quadruple gives the nine coefficients stated in the theorem. They can be checked without the pairing enumeration by a second exhaustive algebraic method. Indeed, for \(M=\begin{pmatrix}A&B\\C&D\end{pmatrix}\) with ternary \(2\times2\) integer blocks, the same symplectic identity is equivalent to the conditions
\[A^{\mathsf T}C=(A^{\mathsf T}C)^{\mathsf T},\quad B^{\mathsf T}D=(B^{\mathsf T}D)^{\mathsf T},\quad A^{\mathsf T}D-C^{\mathsf T}B=I_2.\]
The second algorithm traverses all \(81^4\) ordered block quadruples with safe algebraic pruning and accumulates \(\operatorname{tr}A+\operatorname{tr}D\). It returns the same exact nine coefficients independently, completing the finite exhaustive proof.

Finally, \(M\mapsto-M\) is a bijection on the box and changes the sign of the trace; this also proves the palindromic symmetry without computation. Strict growth of the coefficients toward zero follows from their exact values.

## Verification

Run `python3 verify_sp4.py` using only the Python standard library. It performs two complete counts: the first uses six symplectic pairings among ternary columns, while the second uses three \(2\times2\) block matrix identities. Both must match the same nine-term distribution, and the column method must additionally match the seven-level completion histogram. The expected terminal marker is `VERIFY_OK`; an assertion failure stops execution otherwise. The evaluation is finite and exhaustive over fully specified domains, rather than an empirical extrapolation.

## Relationship to prior work

Lena Wurzinger, *Integer symplectic matrices in expanding boxes*, arXiv:2610.29794v1 (first public 21 October 2026), defines these boxes in all symplectic ranks, proves a uniform bound for arbitrary box centers (Theorem 1.1), and derives a centered-box asymptotic (Theorem 1.2). Its introduction records an earlier exact rank-one formula for larger shells. Its inspected introduction, symplectic-counting arguments, and final asymptotic section do not present the first centered rank-two integer count or its trace spectrum. An asymptotic estimate, even with known leading constant, does not determine a fixed-radius spectrum. OEIS A364771 instead counts matrices over the finite residue rings \(\mathbb Z/n\mathbb Z\); this does not determine which integer lifts lie in a specified centered box, nor their integer traces.

## Limitations

The result concerns only centered radius one and rank two; it does not supply a formula for arbitrary box sizes or arbitrary center, nor a higher-rank trace distribution. The proof is a fully specified exact finite enumeration with source code and an independently formulated check, not a closed-form symbolic evaluation of all trace coefficients. The publication-priority search was bounded; a previous unindexed exact census could exist. No independent audit has been performed.

## References

1. L. Wurzinger, *Integer symplectic matrices in expanding boxes*, arXiv:2610.29794v1, 21 October 2026. https://arxiv.org/abs/2610.29794 and https://arxiv.org/pdf/2610.29794.
2. OEIS Foundation, A364771, *Order of the symplectic group of 4 X 4 matrices over Z_n*. https://oeis.org/A364771 (finite-ring count, distinct from a bounded integral count).

# Sharp fourth moments for the first two nontrivial symmetric-group characters

## Finding
Let \(S_n\) be the symmetric group with probability-normalized counting measure, where \(n\ge4\). Write \(\chi_{1,n}=\chi^{(n-1,1)}\) and \(\chi_{2,n}=\chi^{(n-2,2)}\) for its first two nontrivial real irreducible characters. For \(a,b\in\mathbb C\), define \(F_{a,b}=a\chi_{1,n}+b\chi_{2,n}\). Then
\[
\int_{S_n}|F_{a,b}|^4\,d\mu_n\le \mathcal K_n(|a|^2+|b|^2)^2,
\]
where the following algebraic sharp constants are exact. For each listed row, \(t_n\) is the **unique positive root** of \(H_n(t)=0\), and \(\mathcal K_n=P_n(t_n)/(1+t_n^2)^2\).

| Degree | \(P_n(t)\) | \(H_n(t)\) | \(\mathcal K_n\), approximately |
| --- | --- | --- | --- |
| \(n=4\) | \(4t^4+8t^3+12t^2+3\) | \(2t^3+2t^2-6t-3\) | \(7.317018044684\) |
| \(n=5\) | \(4t^4+12t^3+24t^2+16t+6\) | \(3t^2+2t-4\) | \(15.641081748080\) |
| \(n=6\) | \(4t^4+12t^3+30t^2+24t+13\) | \(3t^4+11t^3+9t^2-2t-6\) | \(22.379326363869\) |
| \(n=7\) | \(4t^4+12t^3+30t^2+28t+15\) | \(3t^4+11t^3+12t^2-7\) | \(24.713866882268\) |
| \(n\ge8\) | \(4t^4+12t^3+30t^2+28t+16\) | \(3t^4+11t^3+12t^2+t-7\) | \(25.267327761537\) |

For every \(n\ge4\), **all** nonzero equality cases are
\[
(a,b)=\lambda(t_n,1),\qquad \lambda\in\mathbb C\setminus\{0\}.
\]
In particular, the normalized sharp fourth moment grows strictly at each of the degrees \(4,5,6,7,8\) and is **exactly constant for every degree \(n\ge8\)**. For \(n\ge8\), the two-character optimal fourth-power amplification \(25.2673277\ldots\) exceeds the pure \(\chi_{2,n}\) fourth moment \(16\).

## Assumptions and scope
The probability measure is \(\mu_n(\{\sigma\})=1/n!\). The standard character is \(\chi_{1,n}(\sigma)=X(\sigma)-1\), where \(X(\sigma)\) is the number of fixed points. Let \(Y(\sigma)\) be the number of disjoint two-cycles of \(\sigma\); then the second character is
\[
\chi_{2,n}(\sigma)=\binom{X(\sigma)}2+Y(\sigma)-X(\sigma).
\]
The latter follows by subtracting the trivial and standard summands from the permutation representation on unordered pairs. Both are orthonormal irreducible characters, so \(\|F_{a,b}\|_2^2=|a|^2+|b|^2\). The theorem concerns precisely this **two-dimensional central character subspace**, not the full matrix-coefficient isotypic Fourier blocks or an operator projection norm.

## Proof
**1. Exact low-cycle factorial moments.** For integers \(i,j\ge0\), count ordered choices of \(i\) distinct fixed points and \(j\) distinct two-cycles in a uniformly random permutation. If \(i+2j\le n\), there are \(n!/(2^j(n-i-2j)!)\) ways to select these marked structures, and each is preserved by \((n-i-2j)!\) permutations of the remaining letters. Hence
\[
\mathbb E[(X)_i(Y)_j]=2^{-j}\quad\text{for }i+2j\le n,
\qquad
\mathbb E[(X)_i(Y)_j]=0\quad\text{otherwise},
\]
where \((x)_k=x(x-1)\cdots(x-k+1)\), with \((x)_0=1\). This is an exact finite-group identity, not a Poisson-limit approximation.

**2. Fourth-moment table and stabilization.** Substitute \(A=X-1\) and \(B=X(X-3)/2+Y\). Expand their mixed fourth moments in the falling-factorial basis and apply step 1. The resulting five moments, displayed in order \(\big(\mathbb EA^4,\mathbb EA^3B,\mathbb EA^2B^2,\mathbb EAB^3,\mathbb EB^4\big)\), are
\[
\begin{array}{c|ccccc}
 n & \mathbb EA^4 & \mathbb EA^3B & \mathbb EA^2B^2 & \mathbb EAB^3 & \mathbb EB^4\\\hline
 4&4&2&2&0&3\\
 5&4&3&4&4&6\\
 6&4&3&5&6&13\\
 7&4&3&5&7&15\\
 n\ge8&4&3&5&7&16
\end{array}.
\]
Each monomial in this expansion uses total **cycle weight** at most eight (weight one for \(X\), two for \(Y\)), since \(A\) has weight one and \(B\) weight two. Therefore the table is identical for every \(n\ge8\) by the factorial-moment identity. Exact finite values follow by the same expansion with the above cutoff; no extrapolation from numerical samples is required.

**3. Complex phases are rigid.** Let \(u=|a|\), \(v=|b|\), and, when \(uv>0\), set \(c=\cos(\arg a-\arg b)\). Since \(A,B\) are real,
\[
\mathbb E|aA+bB|^4
=u^4M_{40}+v^4M_{04}+(2+4c^2)u^2v^2M_{22}
+4c\left(u^3vM_{31}+uv^3M_{13}\right),
\]
where \(M_{ij}=\mathbb E(A^iB^j)\). In every row of the table, \(M_{22}>0\), \(M_{31}>0\), and \(M_{13}\ge0\). For \(u,v>0\), this expression is a strictly convex quadratic in \(c\in[-1,1]\); its greater endpoint is uniquely \(c=1\), because \(M_{31}>0\). Thus any mixed maximizer has equal coefficient phases, and after division by a common nonzero scalar the coefficients are \((t,1)\) with \(t>0\).

**4. One positive optimizer per degree.** The table now gives the scalar quotient \(f_n(t)=P_n(t)/(1+t^2)^2\) displayed in the Finding. Direct differentiation yields
\[
 f'_n(t)=-\frac{4tH_n(t)}{(1+t^2)^3}\quad(n=4),\qquad
 f'_n(t)=-\frac{4(t+1)^2H_n(t)}{(1+t^2)^3}\quad(n=5),
\]
and
\[
 f'_n(t)=-\frac{4H_n(t)}{(1+t^2)^3}\quad(n\ge6).
\]
For \(n=4,5\), the displayed \(H_n\) are respectively the cubic and quadratic in the table; for \(n\ge6\), they are the quartics there. Every \(H_n\) has a negative constant term, positive leading coefficient, and exactly one sign change in descending coefficient order. Descartes' rule and the intermediate value theorem imply **exactly one positive zero** \(t_n\). The derivative is positive before that zero and negative after it, proving strict global maximality in the open range \(t>0\). Both boundary values \(t=0\) and \(t=\infty\) are strictly smaller. This proves the sharp constants and every equality case, including exclusions of single-character extremizers.

**5. Strict finite-rank transitions.** For fixed \(t>0\), the successive numerator differences are
\[
P_5-P_4=4t^3+12t^2+16t+3,\quad
P_6-P_5=6t^2+8t+7,\quad
P_7-P_6=4t+2,\quad P_8-P_7=1.
\]
All are positive. Maximizing the successive quotients gives \(\mathcal K_4<\mathcal K_5<\mathcal K_6<\mathcal K_7<\mathcal K_8\). Moment stabilization in step 2 gives \(\mathcal K_n=\mathcal K_8\) for every \(n\ge8\). This completes the proof.

## Verification
The accompanying standalone standard-library program `verify.py` independently computes exact fourth-moment averages over permutation conjugacy classes for \(4\le n\le14\), using \(1/\prod_j j^{c_j}c_j!\) for the class probability. It separately enumerates every permutation at \(4\le n\le7\) and reproduces the full moment table, orthonormality and phase-optimized algebraic constants. It returns `VERIFY_OK` with 84 deterministic assertions. Separately, exact symbolic differentiation and polynomial factorization were compared with the displayed derivative formulas. These finite/symbolic checks corroborate the proof; the all-degree result follows from steps 1–5.

## Relationship to prior work
Sawatzky (arXiv:2210.16262v1, primary MSC 43A30) studies central Fourier algebras and amenability constants of finite groups, but his stated objectives and examined character formulas do not give sharp \(L^2\)-to-\(L^4\) synthesis norms for this two-irrep subspace. Hamaker and Rhoades (arXiv:2206.06567) supply the general character-polynomial framework underlying the two explicit characters, and Ford (arXiv:2104.12019) supplies the exact permutation-cycle moment mechanism. These ingredients and orthogonality are known and **are not claimed as discoveries**. The result here is their sharp mixed-character fourth-moment optimization, equality rigidity, four strict finite-rank jumps and exact stabilization at rank eight.

A published result titled *Exact endpoint norms for the \(n-2,2\) Fourier block of symmetric groups* gives \(\ell^1/\ell^\infty\) norms of the **complete regular-representation isotypic projection**, a different operator and exponent, and does not imply the present two-character \(L^2\)-to-\(L^4\) theorem. Results on abelian sparse characters, group sampling and SU(2)/SU(3) character packets concern different groups or subspaces and do not cover this claim. Mathematical statements rather than title similarity were compared.

## Limitations
The sharp classification is restricted to the central span of exactly the two specified irreducible characters. It does not determine the full low-degree Fourier subspace, arbitrary pairs of Specht characters, or intermediate exponents. Some ingredients are established classical character and cycle-statistic formulas; a previously published presentation of this particular mixed-norm optimization could exist under equivalent representation-theoretic terminology. No independent audit has been performed. Numerical constants are approximations to the exact algebraic definitions, and checker enumeration alone is not an all-degree proof.

## References
1. J. Sawatzky, *Amenability constants of central Fourier algebras of finite groups*, arXiv:2210.16262v1, first public 2022-10-28; primary MSC2020 43A30. https://arxiv.org/abs/2210.16262
2. Z. Hamaker and B. Rhoades, *Characters of Local and Regular Permutation Statistics*, arXiv:2206.06567v1, first public 2022-06-14, especially character polynomials and local functions. https://arxiv.org/abs/2206.06567
3. K. Ford, *Cycle Type of Random Permutations: A Toolkit*, arXiv:2104.12019v1, first public 2021-04-24, Theorems 1.2–1.3. https://arxiv.org/abs/2104.12019
4. *Exact endpoint norms for the \(n-2,2\) Fourier block of symmetric groups*, published public research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-endpoint-norms-for-the-n-2-2-fourier-block-of-symmetric-gr--2557238644ab

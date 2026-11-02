# Two cyclotomic resonance clocks in neighbor-parity dynamics on generalized Petersen graphs

## Finding

For every integer \(n\ge5\), let \(GP(n,2)\) be the simple, labelled generalized Petersen graph with vertices \(u_i,v_i\), indexed modulo \(n\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Over \(\mathbb F_2\), let \(F_n\) simultaneously replace the bit at each vertex by the sum of the bits at its three neighbors. Put \(e=2^{\nu_2(n)}\), \(\alpha=\mathbf 1_{3\mid n}\), and \(\beta=\mathbf 1_{5\mid n}\). Define, for integers \(t\ge0\),

\[
 d_n=4e(\alpha+\beta),\qquad h_n(t)=2\alpha\min(t,2e)+4\beta\min(t,e).
\]

**Theorem.** The periodic-state set of \(F_n\) has exactly \(2^{2n-d_n}\) elements. The set of configurations that have entered this periodic-state set by time \(t\) has exactly

\[
 C_n(t)=2^{2n-d_n+h_n(t)}
\]

members. Thus precisely \(C_n(0)\) configurations first enter at time zero, and precisely \(C_n(t)-C_n(t-1)\) first enter at time \(t\ge1\). The maximum first-entry time is

\[
 T_n=\begin{cases}2e,&3\mid n,\\ e,&3\nmid n,\ 5\mid n,\\0,&\gcd(n,15)=1.\end{cases}
\]

In particular, **the update is bijective exactly when \(\gcd(n,15)=1\)**. Over an algebraic closure of \(\mathbb F_2\), its zero-primary Jordan form has exactly two blocks of size \(2e\) if \(3\mid n\), exactly four blocks of size \(e\) if \(5\mid n\), and no other zero-primary blocks. Contributions from the two divisibility conditions are additive.

The exact number of fixed configurations is

\[
 \#\operatorname{Fix}(F_n)=2^{\min(2,e)+4\beta}.
\]

Finally, every temporal returning-point population admits a finite polynomial-gcd formula, given below; it determines all primitive orbit numbers by ordinary Möbius inversion. The theorem concerns synchronous, loopless, *open-neighborhood* parity, not a sequential update or a self-inclusive rule.

**Examples.** On the Petersen graph \(GP(5,2)\), the recurrent set contains \(2^6=64\) of the \(2^{10}\) states: \(32\) fixed points and \(16\) primitive two-cycles; all other states enter recurrence in one step. On \(GP(6,2)\), exactly \(16\) of \(2^{12}\) states are periodic, with four fixed states and six primitive two-cycles; its maximum transient length is four. These orbit counts follow from the return-time formula, not from an assumption of period at most two for all \(n\).

## Assumptions and scope

All vector spaces and matrix operations are over \(\mathbb F_2\), unless a scalar extension is explicitly stated. No self-loop is present; \(n\ge5\) ensures each vertex has three distinct neighbors. A configuration is periodic if \(F_n^r(x)=x\) for some positive integer \(r\). Its first-periodic-entry time is the least nonnegative \(t\) for which \(F_n^t(x)\) is periodic. These are finite-dimensional linear dynamics, so the Fitting decomposition separates a nilpotent summand from an invertible summand. The periodic configurations are exactly the invertible summand, and their preimages through time \(t\) include the \(t\)-th kernel of the nilpotent summand.

## Proof

**1. Cyclic matrix symbol.** Let \(z\) denote cyclic shift and set \(R_n=\mathbb F_2[z,z^{-1}]/(z^n-1)\). Ordering outer and inner vertex coordinates identifies the update operator with multiplication on \(R_n^2\) by

\[
 B(z)=\begin{pmatrix}y&1\\1&y^2\end{pmatrix},\qquad y=z+z^{-1}.
\]

The use of \(y^2=z^2+z^{-2}\) is a characteristic-two identity. Its trace and determinant are

\[
 \tau=y+y^2=y(y+1),\qquad \delta=y^3+1=(y+1)(y^2+y+1),
\]

and the exact cyclotomic factorization is

\[
 \delta=z^{-3}(z^2+z+1)(z^4+z^3+z^2+z+1).
\]

Write \(\Phi_3=z^2+z+1\) and \(\Phi_5=z^4+z^3+z^2+z+1\). These are distinct irreducible polynomials over \(\mathbb F_2\), of degrees two and four. The polynomial \(z^n-1\) has \(\Phi_j\) as a factor exactly when \(j\mid n\), and then with multiplicity \(e=2^{\nu_2(n)}\). Every other local factor makes \(\delta\) a unit, so \(B\) is invertible there.

**2. The three-resonance local block.** On the \(\Phi_3\)-primary factor, \(y\equiv1\), \(y+1=z^{-1}\Phi_3\), and \(B\) modulo \(\Phi_3\) is the rank-one square-zero matrix with all four entries equal to one. Cayley–Hamilton in characteristic two yields the exact identity

\[
 B^2=\tau B+\delta I=(y+1)\bigl(y B+(y^2+y+1)I\bigr).
\]

The factor in parentheses reduces modulo \(\Phi_3\) to \(B+I=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), which is a unit matrix. Consequently \(B^{2e}=0\) on the two-dimensional module over \(\mathbb F_2[z]/(\Phi_3^e)\). Its determinant has valuation one and it has a unit off-diagonal entry, so elementary row-column operations give the local Smith form \(\operatorname{diag}(1,\Phi_3)\); hence its kernel has dimension one over the residue field \(\mathbb F_4\). Because the entire local space has dimension \(2e\) over \(\mathbb F_4\) and is nilpotent, one kernel dimension implies exactly one Jordan block of size \(2e\) for each of the two roots of \(\Phi_3\). Thus this resonance contributes \(2\min(t,2e)\) to \(\dim_{\mathbb F_2}\ker(F_n^t)\) and contributes total nilpotent dimension \(4e\).

**3. The five-resonance local block.** On the \(\Phi_5\)-primary factor, \(y^2+y+1\equiv0\), so \(\tau\equiv1\) and \(\delta\) has valuation exactly one. The reduction of the characteristic polynomial of \(B\) is \(\lambda(\lambda+1)\), which has coprime roots over \(\mathbb F_{16}\). The two factors lift uniquely to comaximal factors over the local Artin ring (or its complete DVR before truncation). Thus the two-dimensional module splits into one invertible rank-one summand and one rank-one summand on which the eigenvalue is \(\Phi_5\) times a unit. The latter is one nilpotent Jordan block of size \(e\) for each of the four roots of \(\Phi_5\). Hence this resonance contributes \(4\min(t,e)\) to the kernel dimension and has total nilpotent dimension \(4e\). It is independent of the \(\Phi_3\) contribution by the Chinese remainder theorem.

**4. Entry-time law.** The Chinese remainder decomposition separates the two nilpotent families from all invertible local factors, proving that the nilpotent dimension is \(d_n\). Their joint \(t\)-th kernel has dimension \(h_n(t)\). Periodic states form a linear subspace of dimension \(2n-d_n\); configurations entering that subspace by time \(t\) number \(2^{2n-d_n+h_n(t)}\). Both possible longest blocks are present whenever their divisibility conditions hold, so the asserted maximum first-entry time is attained. The determinant factorization proves bijectivity exactly for \(\gcd(n,15)=1\).

**5. Fixed points.** The off-diagonal entries of \(B+I\) are units, so its global Laurent-polynomial Smith invariants are \(1\) and \(\det(B+I)\). Directly,

\[
 \det(B+I)=y(y^2+y+1)=z^{-3}(z+1)^2\Phi_5(z).
\]

A scalar multiplication by a Laurent polynomial \(p\) on \(\mathbb F_2[z]/(z^n-1)\) has kernel dimension \(\deg\gcd(p,z^n-1)\). The multiplicity of \(z+1\) in \(z^n-1\) is \(e\), while that of \(\Phi_5\) is \(e\) when \(5\mid n\). Hence \(\dim\ker(B+I)=\min(2,e)+4\beta\), giving the fixed-point formula.

**6. All return times.** For \(t\ge1\), form the polynomial matrix

\[
 H_t(z)=\left(z^2 B(z)\right)^t+z^{2t}I\in\operatorname{Mat}_2(\mathbb F_2[z]).
\]

Let \(s_1\) be the monic gcd of its four entries, and \(s_2=\det(H_t)/s_1\). These are the two Smith invariant factors of \(H_t\) over \(\mathbb F_2[z]\). The determinant is nonzero as a polynomial, because no eigenvalue of the generic matrix \(B(z)\) is a constant root of unity: its characteristic polynomial \(\lambda^2+(y+y^2)\lambda+(y^3+1)\) has a nonzero cubic coefficient in the indeterminate \(y\), for every constant \(\lambda\). Since \(z^{2t}\) is a unit in \(R_n\), the return-time equation is \(H_t x=0\). Thus, with \(P_n=z^n-1\),

\[
 \boxed{\#\operatorname{Fix}(F_n^t)=2^{\deg\gcd(P_n,s_1)+\deg\gcd(P_n,s_2)}.}
\]

For each \(r\ge1\), the number of primitive \(r\)-cycles is exactly \(\frac1r\sum_{d\mid r}\mu(r/d)\#\operatorname{Fix}(F_n^d)\). This formula is an exact algorithm for all \(n,r\), not a closed classification of which larger primitive periods occur. No claim of a uniform period-two bound is made. This completes the proof.

## Verification

Both supplied Python files use only the standard library. Running `python artifacts/verify.py` performs exact binary matrix-kernel comparisons for all \(5\le n\le100\) through their relevant transient ranges, including the stabilized thresholds, and exhaustive state-by-state entry-time classification for \(5\le n\le8\). Running `python artifacts/verify_fixed.py` independently compares exact polynomial Smith-gcd return-time exponents against direct binary-matrix ranks for all \(5\le n\le30\) and \(1\le t\le32\). The scripts were replayed from their supplied paths and their results are recorded verbatim in `artifacts/verification_output.txt`.

The calculations establish finite checks only; the local-primary arguments above establish the infinite family. An additional exact polynomial-gcd check of the fixed-point exponent was performed for \(5\le n\le400\); the code for that short independent loop appears in `artifacts/verify_fixed_points.py`.

## Relationship to prior work

Gera and Stănică (2011) explicitly derive the two-circulant adjacency block of every generalized Petersen graph and its complex spectral quadratic; their Theorem 2.4 is a source for the matrix symbol. The present zero-primary classification operates instead in characteristic two, including repeated cyclotomic factors when \(n\) is even. The complex spectrum alone does not give these mod-two Jordan block lengths, transient shells, or the fixed-time gcd census.

Zaidenberg (2006) gives the harmonic/convolution approach to finite-field cellular automata and their periodic harmonic functions. His 2009 matrix-valued Floquet–Bloch work supplies a broader conceptual spectral framework (notably its Section 4), but the finite-characteristic, even-period repeated-root phenomenon and the stated \(GP(n,2)\) laws are not explicit there. General spectral methods are acknowledged rather than claimed as new. The arithmetic thresholds and nilpotent partitions above require additional local factorization; the result is a graph-family specialization, not a claim to a new general theory of additive cellular automata.

## Limitations

The statement applies only to the ordinary \(GP(n,2)\) graph with \(n\ge5\), synchronous open-neighborhood parity over \(\mathbb F_2\), and labelled configurations. It does not classify nonlinear rules, self-inclusive parity, asynchronous scans, other skips, or arbitrary finite fields. The all-return-time formula is exact but uses polynomial gcds rather than a uniform elementary expression for the largest primitive period. Published generic spectral descriptions may permit the displayed formulas to be derived independently; the literature review did not identify their explicit characteristic-two transient statements. No independent mathematical audit has been performed.

## References

1. R. Gera and P. Stănică, *The spectrum of generalized Petersen graphs*, Australasian Journal of Combinatorics **49** (2011), 39–45. https://ajc.maths.uq.edu.au/pdf/49/ajc_v49_p039.pdf . Theorem 2.4 and Section 3 explicitly treat the block representation and \(GP(n,2)\).
2. M. Zaidenberg, *Convolution equations on lattices: periodic solutions with values in a prime characteristic field*, arXiv:math-ph/0606070, first posted 2006-06-29. https://arxiv.org/abs/math-ph/0606070 .
3. M. Zaidenberg, *Discrete convolution operators in positive characteristic: a variation on the Floquet–Bloch theory*, arXiv:0910.3351, first posted 2009-10-18. https://arxiv.org/abs/0910.3351 .

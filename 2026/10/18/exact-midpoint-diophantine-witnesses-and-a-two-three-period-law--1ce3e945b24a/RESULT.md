# Exact midpoint Diophantine witnesses and a two/three-period law for subtractive recurrences

## Finding

Fix an integer \(k\ge2\) and positive integers \(1\le A<B\). Generate \(u_1=A\), \(u_2=B\), and \(u_{n+2}=ku_{n+1}-u_n\) for \(n\ge1\). Let \(d=\gcd(A,B)\), \(a_n=u_n/d\), and \(b_n=u_{n+1}/d\). For every \(n\ge1\), exactly one of
\[
a_nx+b_ny=\frac{(a_n-1)(b_n-1)}2,\qquad
a_nx+b_ny+1=\frac{(a_n-1)(b_n-1)}2
\]
has a nonnegative integer solution, and that solution is unique. Define \(\delta_n\in\{0,1\}\) as the constant added on the left in the solvable equation. The least period of \((\delta_n)_{n\ge1}\) is **exactly two if \(k\) is even, and exactly three if \(k\) is odd**, for every admissible initial pair. The sequence alternates when \(k\) is even. If \(k\) is odd, a complete period contains either one or two occurrences of \(\delta=1\), with the choice fixed explicitly by the initial parity state below.

The result also constructs the unique solution pair at every index. Let \(\alpha_n\) be the least positive inverse of \(a_n\) modulo \(b_n\), and put
\[
\beta_n=\frac{a_nb_n+1-a_n\alpha_n}{b_n}.
\]
Then \(1\le\alpha_n<b_n\), \(1\le\beta_n\le a_n\), and
\[
\boxed{(a_{n+1},b_{n+1},\alpha_{n+1},\beta_{n+1})
=(b_n,kb_n-a_n,k\alpha_n+\beta_n-a_n,b_n-\alpha_n).}
\]
If \(\alpha_n,\beta_n\) are both odd, then \(\delta_n=0\) and
\[
(x_n,y_n)=\left(\frac{\alpha_n-1}{2},\frac{\beta_n-1}{2}\right).
\]
Otherwise \(\delta_n=1\) and
\[
(x_n,y_n)=\left(\frac{b_n-\alpha_n-1}{2},\frac{a_n-\beta_n-1}{2}\right).
\]
These formulas apply to normalized noncoprime initial pairs as well as coprime pairs.

## Assumptions and scope

All variables and indices are integers. The hypotheses \(k\ge2\) and \(1\le A<B\) guarantee positive, strictly increasing recurrence terms. The common divisor \(d\) is fixed, since \(\gcd(u_{n+1},ku_{n+1}-u_n)=\gcd(u_n,u_{n+1})\). Accordingly \(1\le a_n<b_n\), \(\gcd(a_n,b_n)=1\), and \(b_n\ge2\) for every \(n\ge1\). The ordinary least positive modular inverse \(\alpha_n\) is therefore well-defined. The claimed least period concerns the *solvable-equation indicator*, not the (unbounded) solution-coordinate sequences.

## Proof

**1. Complementary Bézout witnesses.** Fix coprime \(1\le a<b\), write \(a\alpha+b\beta=ab+1\) with \(1\le\alpha<b\). Then the integer \(\beta\) necessarily satisfies \(1\le\beta\le a\). Set \(M=(a-1)(b-1)/2\). If \(\alpha\) and \(\beta\) are odd, direct substitution gives
\[
a\frac{\alpha-1}{2}+b\frac{\beta-1}{2}=M.
\]
Otherwise the parity identity \(a\alpha+b\beta\equiv ab+1\pmod2\) implies that both \(b-\alpha\) and \(a-\beta\) are odd. In this case,
\[
a\frac{b-\alpha-1}{2}+b\frac{a-\beta-1}{2}=M-1.
\]
The displayed coordinates are nonnegative. For uniqueness and exclusion, note that any nonnegative representation \(ax+by=N<ab\) has \(0\le x<b\) and \(0\le y<a\), and \(x\) is uniquely determined modulo \(b\); therefore such a representation is unique. When \(a=1\), \(M=0\), so only the first equation has a solution. When \(a\ge2\), let \(F=ab-a-b=2M-1\). For every \(0\le N\le F\), choose the unique \(x_0\in\{0,\ldots,b-1\}\) with \(ax_0\equiv N\pmod b\), and let \(y_0=(N-ax_0)/b\). The integer \(N\) is representable if and only if \(y_0\ge0\). The complementary value \(F-N\) has the corresponding unique residue representative \(b-1-x_0\) and quotient \(-1-y_0\), so it is representable if and only if \(y_0\le-1\). Thus exactly one of the complementary values \(M\) and \(M-1\) is representable. The parity constructions above select that value and supply its unique witness.

**2. Unimodular inverse transport.** Write \((a',b')=(b,kb-a)\). Given \((\alpha,\beta)\), define \(\alpha'=k\alpha+\beta-a\), \(\beta'=b-\alpha\). A direct calculation gives \(b\alpha'+(kb-a)\beta'=b(kb-a)+1\). Further \(1\le\beta'<b\); the displayed Bézout identity with \(1\le\beta'<b\) forces \(1\le\alpha'<kb-a\). Hence these are precisely the prescribed new inverse witnesses. This holds at every index, including \(a=1\).

**3. Six-state reduction.** Reduce \((a,b,\alpha,\beta)\) modulo two. The Bézout identity restricts it to the six states
\[
(0,1,0,1),\ (0,1,1,1),\ (1,0,1,0),\ (1,0,1,1),\ (1,1,0,0),\ (1,1,1,1).
\]
For \(\kappa=k\bmod2\) the transition is
\[
T_\kappa(a,b,\alpha,\beta)
=(b,\kappa b+a,\kappa\alpha+\beta+a,b+\alpha)\pmod2.
\]
Its cycles on the admissible states are exhaustive. For \(\kappa=0\), the three two-cycles are
\[
\begin{gathered}
(0,1,0,1)\leftrightarrow(1,0,1,1),\\
(0,1,1,1)\leftrightarrow(1,0,1,0),\\
(1,1,0,0)\leftrightarrow(1,1,1,1).
\end{gathered}
\]
The \(\delta\) values alternate on each cycle. For \(\kappa=1\), the two three-cycles are
\[
\begin{gathered}
(0,1,0,1)\to(1,1,1,1)\to(1,0,1,0)\to(0,1,0,1),\\
(0,1,1,1)\to(1,1,0,0)\to(1,0,1,1)\to(0,1,1,1).
\end{gathered}
\]
Their respective \(\delta\) strings are \((1,0,1)\) and \((0,1,0)\). The first case has one zero and two ones in each period; the second has two zeros and one one. None of these cyclic binary strings has smaller positive period; this proves the exact least-period and frequency assertions.

## Verification

For illustration, starting at \((A,B)=(1,2)\) gives \((\delta_1,\delta_2,\ldots)=(0,1,0,1,\ldots)\) when \(k=2\), and \((0,0,1,0,0,1,\ldots)\) when \(k=3\).

Run `python3 verify.py` with Python 3.8 or later. The standalone checker independently recomputes modular inverses at 68,094 recurrence states, validates the transported witnesses, verifies 58,782 parity-period comparisons, brute-enumerates all small nonnegative solutions for 9,269 cases, and checks gcd normalization at 2,640 indices arising from noncoprime initial seeds. It also validates the recurrence identities and parity claims. These finite checks are supplementary: all infinite quantified statements follow from the algebraic proof.

## Relationship to prior work

Davala's 2023 paper establishes explicit solutions for several prescribed balancing and Lucas-balancing pairs, notably sequences with recurrence coefficient six. The present result includes the adjacent balancing subcase but does not claim it as new. Arachchi and collaborators' 2023 paper proves a general modular-inverse equation-selection criterion and establishes parity patterns for **additive** recurrences \(u_{n+2}=ku_{n+1}+u_n\); that result neither asserts nor implies the subtractive-recurrence period law without a new argument. Chu, Miller and Tresch's 2025 problems paper motivates determining solvable equations and solutions for other recurrences. The 2025 survey on the same pair gives detailed arbitrary-seed formulas for the Fibonacci (additive) recurrence; a September 2026 generalization studies complementary targets and special Fibonacci cases, rather than this uniform negative-sign law. The contribution here is the subtractive, arbitrary-seed inverse-witness transport and universal sharp two/three-period dichotomy, not existence or uniqueness for a single pair. None of the examined statements gives this full theorem.

## Limitations

The theorem requires \(k\ge2\) and positive strictly ordered initial terms \(A<B\); it makes no statement for arbitrary signed or nonmonotone recurrences. The recurrence of integer solution coordinates is explicit but their growth rates are not analyzed. A literature search cannot exclude every unpublished or unindexed equivalent result, and no independent mathematical audit has been performed.

## References

1. R. K. Davala, *Solution to a pair of linear, two-variable, Diophantine equations with coprime coefficients from balancing and Lucas-balancing numbers*, Notes on Number Theory and Discrete Mathematics **29** (2023), 495–502, online first 15 July 2023, DOI: 10.7546/nntdm.2023.29.3.495-502.
2. S. U. K. Arachchi, H. V. Chu, J. Liu, Q. Luan, R. Marasinghe and S. J. Miller, *On a Pair of Diophantine Equations*, arXiv:2309.04488, initial submission 1 September 2023.
3. H. V. Chu, S. J. Miller and M. Tresch, *Problems Regarding a Pair of Diophantine Equations*, arXiv:2512.12681, December 2025.
4. H. V. Chu, R. Gulecha, S. Guo, N. Johnson, S. J. Miller and Y. Shin, *A Survey on a Pair of Diophantine Equations*, arXiv:2509.01781, September 2025.
5. H. V. Chu, D. Kim, T. Koch, S. J. Miller and A. V. Nguyen, *Generalizing a Pair of Diophantine Equations*, arXiv:2609.08728, September 2026.

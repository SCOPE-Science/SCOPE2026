# A sharp heterogeneous orientation phase for three-point concentration

## Finding

For an integer-valued random variable \(Z\), define its point concentration by \(Q(Z)=\sup_{k\in\mathbb Z}\Pr(Z=k)\). Let \(1/3\le a\le b\le c\le1/2\). For \(t\in\{a,b,c\}\), independently let \(Y_t\) be supported at \(0,1,2\), with respective masses \(t,t,1-2t\). Let
\[
T(a,b,c)=\max_{(s_1,s_2,s_3)\in\{-1,1\}^3}
Q(s_1Y_a+s_2Y_b+s_3Y_c).
\]
Then the **exact maximum**, attained for every admissible triple, is
\[
\boxed{T(a,b,c)=\max\{A(a,b,c),B(a,b,c)\}},
\]
where
\[
A=ab+ac+bc-3abc,\qquad
B=7abc-4ab-ac-bc+a+b.
\]
When \(A\) is the larger branch, the all-positive (equivalently, all-negative) orientation attains the optimum. When \(B\) is the larger branch, the \((+,+,-)\) orientation, in which the variable with the largest mass parameter \(c\) is reversed, attains the optimum. Their difference is
\[
\boxed{A-B=(1-2c)(5ab-a-b).}
\]
Consequently, when \(1/3<a<b<c<1/2\), the **unique maximizing sign pattern up to global reversal** is all-aligned when \(5ab>a+b\), and it reverses just the variable with parameter \(c\) when \(5ab<a+b\). At \(5ab=a+b\) both patterns tie. Thus the orientation phase boundary depends only on the *two smaller* parameters: it is independent of the largest parameter throughout the strict interior.

For equal parameters \(a=b=c=t\), the phase changes at \(t=2/5\); the value there is \(36/125\). The heterogeneous result is stronger than simply applying the equal-cap value at the largest parameter, because it determines the exact signed candidate at every ordered triple.

## Assumptions and scope

The three variables are independent; each has the exact three-point probability vector specified above. At the endpoints \(t=1/3\) and \(t=1/2\), one obtains respectively the uniform three-point and two-point laws. The full formula holds with these endpoints, but strict uniqueness is stated only for \(1/3<a<b<c<1/2\). Translation and simultaneous reflection of a sum preserve its maximum point probability, so among eight sign patterns it suffices to examine four representatives: \((+,+,+)\), \((+,+,-)\), \((+,-,+)\), and \((-,+,+)\). In particular this is the standard-extremal sign-selection functional, **not** the unrestricted supremum over all integer distributions with individual point-mass bounds.

## Proof

**1. Four probability generating functions.** Write \(p_t(z)=t+tz+(1-2t)z^2\) and \(r_t(z)=(1-2t)+tz+tz^2\). Reversal of a three-point law changes its polynomial from \(p_t\) to \(r_t\), up to a monomial. Thus the largest coefficient in the four polynomials
\[
P=p_a p_b p_c,\quad H=p_a p_b r_c,\quad
J=p_a r_b p_c,\quad K=r_a p_b p_c
\]
exhausts the signed concentration problem. Let \(P_j,H_j,J_j,K_j\) denote coefficients of \(z^j\).

**2. Locate possible maxima, with an exact positivity certificate.** Every coefficient sequence of \(p_t\) and \(r_t\) is log-concave: \(t^2\ge t(1-2t)\) holds precisely for \(t\ge1/3\). Convolution preserves log-concavity for nonnegative sequences supported on an integer interval: indeed the Toeplitz matrix of a log-concave sequence has nonnegative minors of order two, and the product of two such Toeplitz matrices has the same property by the Cauchy–Binet identity. Therefore every one of \(P,H,J,K\) has a log-concave coefficient sequence.

The following *eight exact coefficient inequalities* hold for every ordered triple in the stated closed parameter simplex:
\[
\begin{gathered}
P_2\ge P_1,\quad P_3\ge P_4,\\
H_3\ge H_2,\quad H_3\ge H_4,\\
J_3\ge J_2,\quad J_3\ge J_4,\\
K_2\ge K_1,\quad K_3\ge K_4.
\end{gathered}
\]
For completeness these are algebraic identities with a nonnegative-coefficient certificate, not numerical guesses. Put
\[
t_0=6a-2,\quad t_1=6(b-a),\quad t_2=6(c-b),\quad t_3=3-6c.
\]
These four quantities are nonnegative and sum to one. Temporarily let \(S=t_0+t_1+t_2+t_3\), \(A_0=2S+t_0\), \(B_0=A_0+t_1\), and \(C_0=B_0+t_2\). In the polynomials above, replace \(p_t\) by \(u+uz+(6S-2u)z^2\) and \(r_t\) by \((6S-2u)+uz+uz^2\) with \(u\) one of \(A_0,B_0,C_0\). Each comparison is then a homogeneous cubic in \(t_0,t_1,t_2,t_3\). **Every one of its 20 monomial coefficients is a nonnegative integer**. The full eight-row exact coefficient table is in `COEFFICIENTS.tsv`; `check.py` independently reconstructs all eight polynomials using integer polynomial arithmetic and checks the complete certificate. Since \(t_i\ge0\), the displayed inequalities follow for the entire continuum of parameters.

Log-concavity and these local coefficient comparisons imply
\[
Q(Y_a+Y_b+Y_c)=\max\{P_2,P_3\},\quad
Q(Y_a+Y_b-Y_c)=H_3,
\]
\[
Q(Y_a-Y_b+Y_c)=J_3,\quad
Q(-Y_a+Y_b+Y_c)=\max\{K_2,K_3\}.
\]

**3. Compare all candidates.** Direct multiplication and collection of coefficients give
\[
P_2=ab+ac+bc-3abc=A,
\quad H_3=7abc-4ab-ac-bc+a+b=B,
\]
and the exact differences
\[
\begin{aligned}
H_3-P_3&=(3c-1)(6ab-a-b),\\
H_3-J_3&=(3a-1)(c-b),\\
H_3-K_3&=(c-a)(3b-1),\\
H_3-K_2&=(1-2b)(a+ac-c).
\end{aligned}
\]
All four are nonnegative on the ordered parameter simplex. For the first, \(6ab-a-b\ge0\) whenever \(a,b\ge1/3\), since it vanishes at \((1/3,1/3)\) and increases in each variable. For the fourth, \(a+ac-c=a-(1-a)c\ge(3a-1)/2\ge0\). The middle two follow directly from ordering. Hence every candidate other than \(P_2\) is at most \(H_3\); and \(P_2-H_3=(1-2c)(5ab-a-b)\). This proves the exact two-branch maximum.

For strict \(1/3<a<b<c<1/2\), every displayed domination over a genuinely different remaining sign choice is strict. The phase-gap factor is nonzero away from \(5ab=a+b\), establishing the stated uniqueness up to a common sign reversal; at equality both types are optimal. Endpoints follow directly from the non-strict inequalities and continuity. \(\square\)

## Verification

Run `python3 check.py` with `COEFFICIENTS.tsv` in the same directory. The checker has no third-party dependencies. It recomputes all 160 exact homogeneous polynomial coefficients, checks nonnegativity of each and equality to the supplied table, verifies five symbolic factorization identities, and separately enumerates all 120 ordered triples from an eight-point rational parameter grid (including endpoints). The analytic positivity proof, not this finite grid, supplies the universal quantifier over real \(a,b,c\). Both exact algebraic routes passed when tested with the embedded file pair.

## Relationship to prior work

Kurauskas (2026), arXiv:2603.11043v1, formulates an exact conjecture using signed sums of minimum-variance distributions \(\nu_\alpha\) and proves an asymptotic analogue. Its definition of standard extremal laws directly motivates the signed-selection optimization treated here. That paper discusses the nontrivial role of signs, particularly for odd numbers of summands, but does not state or imply the ordered *heterogeneous* three-variable phase \(5ab=a+b\).

Madiman, Wang and Woo (2019), arXiv:1712.00913, prove majorization for convolutions after gap-closing rearrangement under a log-concavity condition. This does not optimize sign reversals of the already gap-free three-point laws at fixed \((a,b,c)\), which is the subject here. Singhal (2022), arXiv:1912.02886, studies signs for Bernoulli laws, not the three-site laws in the present theorem. The equal-parameter specialization is not claimed as an independently new case. The heterogeneous optimization does not imply the full point-concentration conjecture for arbitrary discrete distributions.

## Limitations

No assertion is made about nonsigned coefficients, arbitrary supports, unrestricted point-mass-capped distributions, four or more summands, or parameters outside \([1/3,1/2]\). The strict phase uniqueness requires strict ordering and interior parameters; ties may proliferate on the boundary. This analysis does not establish priority against all unindexed literature, nor does it constitute an independent external audit.

## References

1. V. Kurauskas, *An asymptotically optimal bound for the concentration function of a sum of independent integer random variables*, arXiv:2603.11043v1 (first publicly available 11 March 2026), especially Introduction, Conjecture 1.3 and standard-extremal definitions.
2. M. Madiman, L. Wang, J. O. Woo, *Majorization and Rényi Entropy Inequalities via Sperner Theory*, *Discrete Mathematics* 342 (2019), 2911–2923, arXiv:1712.00913, especially Theorem 1.4.
3. M. Singhal, *Erdős–Littlewood–Offord problem with arbitrary probabilities*, *Discrete Mathematics* 345 (2022), 113005, arXiv:1912.02886.

# Alternating endpoint identity at the singular weight \(x=-1\)
## Finding
Let \(c\ne0\), let \(r\ge1\) be an integer, and let
\[
P(n)=a_3n^3+a_2n^2+a_1n+a_0.
\]
Suppose \((u_n)_{n\ge0}\) satisfies
\[
(n+1)^r u_{n+1}=P(n)u_n-cn^r u_{n-1}\qquad(n\ge0),
\]
where the equation at \(n=0\) is interpreted as \(u_1=P(0)u_0\). Define
\[
s_n=\frac{a_3}{2}n^4+\left(\frac{2a_2}{3}-a_3\right)n^3+\left(a_1-a_2+\frac{a_3}{2}\right)n^2+\left(2a_0-a_1+\frac{a_2}{3}\right)n
\]
and
\[
W_n=-c(n+1)^{2r}+cn^{2r}-P(n)^2-s_nP(n).
\]
Then for every integer \(N\ge1\),
\[
\sum_{n=0}^{N-1}W_n\frac{u_n^2}{(-c)^n}
=
\frac{N^{2r}u_N^2-cN^{2r}u_{N-1}^2-N^rs_Nu_Nu_{N-1}}{(-c)^{N-1}}.
\]
This supplies the alternating weight \(x=-1\), which is excluded from Theorem 2.1 of arXiv:2609.29910v1. For the second-kind Apéry-like recurrence with \(P(n)=an(n+1)+b\), the auxiliary polynomial simplifies to
\[
s_n=\frac{2a}{3}n^3+\left(2b-\frac{2a}{3}\right)n.
\]

## Assumptions and scope
The statement is an algebraic identity over characteristic zero; it is presented over the reals to match the motivating recurrence. No positivity, integrality, or asymptotic hypothesis is needed. The restriction \(r\ge1\) removes the extra initial datum \(u_{-1}\) that appears in the \(r=0\) boundary term of the source theorem. The polynomial \(P\) may have degree below three by allowing leading coefficients to vanish.

## Proof
A direct finite-difference calculation gives
\[
s_{n+1}-s_n=2P(n)\qquad(n\ge0).
\]
For \(n\ge1\), define
\[
H_n=\frac{n^{2r}u_n^2-cn^{2r}u_{n-1}^2-n^rs_nu_nu_{n-1}}{(-c)^{n-1}},
\]
and put \(H_0=0\). Using
\[
(n+1)^ru_{n+1}=P(n)u_n-cn^ru_{n-1},
\]
expand \(H_{n+1}\) and subtract \(H_n\) after putting both terms over the denominator \((-c)^n\). The coefficient of \(u_nu_{n-1}\) is
\[
cn^r\bigl(-2P(n)+s_{n+1}-s_n\bigr)=0.
\]
The remaining coefficient of \(u_n^2\) is
\[
P(n)^2-s_{n+1}P(n)-c(n+1)^{2r}+cn^{2r}
=-P(n)^2-s_nP(n)-c(n+1)^{2r}+cn^{2r}=W_n.
\]
Hence
\[
H_{n+1}-H_n=W_n\frac{u_n^2}{(-c)^n}.
\]
At \(n=0\), the recurrence gives \(u_1=P(0)u_0\), while \(s_0=0\) and \(s_1=2P(0)\). Therefore the same increment identity holds for \(H_1-H_0\). Summing from \(n=0\) to \(N-1\) proves the formula.

## Verification
The proof above is symbolic and covers every allowed \(N\), so finite computation is not used as an infinite proof. The accompanying `verify.py` independently checks the finite-difference equation and the telescoping identity with exact rational arithmetic for six coefficient families, exponents \(r=1,2,3,4\), and every \(N\) from \(1\) through \(12\). Its recorded output is in `verification_output.txt`.

## Relationship to prior work
Theorem 2.1 of Zhi-Hong Sun, arXiv:2609.29910v1, assumes \(cx(x+1)\ne0\), defines an auxiliary polynomial \(s_n(x)\) whose displayed coefficients contain powers of \((x+1)^{-1}\), and uses the relation \(s_{n+1}(x)+xs_n(x)=2P(n)\). Thus \(x=-1\) is not a legal specialization of that statement. At the excluded value the auxiliary relation changes naturally to the finite-difference equation \(s_{n+1}-s_n=2P(n)\), whose polynomial solution above yields a finite endpoint identity without singular coefficients.

Searches for the same alternating square-sum statement, including the related Christoffel-Darboux paper arXiv:2608.13192v1 and classical Christoffel-Darboux references, did not locate this endpoint formula. The available abstract of arXiv:2608.13192v1 was inspected, but its full text was not available through the checked lawful routes, so possible hidden overlap there remains a residual literature risk.

## Limitations
The result does not treat the \(r=0\) boundary case, does not assert new congruences, and does not classify every singular limit of the source's parameterized identities. The exact-rational replay samples finitely many recurrences and serves only as a reproducibility check; the universal content rests on the telescoping proof. Literature searches cannot establish absolute novelty, and the inaccessible full text of arXiv:2608.13192v1 is the main remaining overlap risk.

## References
1. Zhi-Hong Sun, *Identities and congruences involving orthogonal polynomials and Apéry-like numbers*, arXiv:2609.29910v1, 24 September 2026, especially Theorem 2.1 and its proof.
2. Zhi-Hong Sun, *Generalizations of the Christoffel-Darboux formula and congruences involving Apéry-like numbers*, arXiv:2608.13192v1, 13 August 2026.
3. NIST Digital Library of Mathematical Functions, §18.2(v), Christoffel-Darboux formulas.

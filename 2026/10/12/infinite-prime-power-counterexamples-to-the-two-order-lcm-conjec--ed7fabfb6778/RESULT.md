# Infinite prime-power counterexamples to the two-order lcm conjecture for reciprocal Lucas recurrences

## Finding
For every integer \(a\ge4\) with \(a\equiv4\pmod6\) and every integer \(j\ge1\), put \(e=\nu_2(a)\), \(m=2^{e+1}\), and \(n=3^j\). For the recurrence
\[
U_0=0,\qquad U_1=1,\qquad U_{r+2}=aU_{r+1}-U_r,
\]
let \(\alpha_a(t)\) be the first positive zero index modulo \(t\), \(\pi_a(t)\) the least period, and \(\omega_a(t)=\pi_a(t)/\alpha_a(t)\). Then
\[
\omega_a(m)=1,\qquad \omega_a(n)=2,\qquad
\omega_a(\operatorname{lcm}(m,n))=1.
\]
In particular, the mixed \((1,2)\) entry of Conjecture 5.2 in Benfield--Lippard is false for infinitely many recurrence parameters and, for each such parameter, infinitely many pairs of moduli.

## Assumptions and scope
All recurrence terms are integers, and zero indices and periods are computed modulo positive integers \(t\ge2\). The parameter \(a\) is an integer congruent to \(4\) modulo \(6\), hence even, positive and at least \(4\); \(j\) is any positive integer. The notation \(\nu_2(a)\) is the exponent of \(2\) in the integer \(a\). The particular moduli \(2^{e+1}\) and \(3^j\) are coprime, so their least common multiple equals their product. The claim concerns the recurrence coefficient of the second preceding term equal to \(-1\); it does not assert anything for arbitrary second coefficients.

## Proof
**Zero indices, matrix periods, and the lcm law.** Define the integral matrix
\[
T=\begin{pmatrix}a&-1\\1&0\end{pmatrix},\qquad \det T=1.
\]
A direct induction gives
\[
T^r=\begin{pmatrix}U_{r+1}&-U_r\\U_r&-U_{r-1}\end{pmatrix}
\quad(r\ge1).
\]
If \(U_r\equiv0\pmod t\), the recurrence gives \(U_{r+1}\equiv-U_{r-1}\pmod t\), so \(T^r\) is a scalar matrix. Conversely, scalarity of \(T^r\) implies \(U_r\equiv0\pmod t\). The scalar powers of the invertible matrix \(T\) form a subgroup of the integers under exponentiation; thus the positive zero indices are precisely the positive multiples of their least member \(\alpha_a(t)\). The least period is precisely the order \(\pi_a(t)\) of \(T\) modulo \(t\), because \((U_r,U_{r+1})\) is a complete recurrence state.

At exponent \(\alpha_a(t)\), the matrix equals \(cI\) for a unit \(c\) modulo \(t\). Taking determinants shows \(c^2\equiv1\pmod t\), so the period is either \(\alpha_a(t)\) or \(2\alpha_a(t)\). In particular \(\omega_a(t)\in\{1,2\}\). For any \(s,t\ge2\), the zero and period conditions modulo \(\operatorname{lcm}(s,t)\) hold if and only if they hold modulo both \(s\) and \(t\). Hence
\[
\alpha_a(\operatorname{lcm}(s,t))=\operatorname{lcm}(\alpha_a(s),\alpha_a(t)),\quad
\pi_a(\operatorname{lcm}(s,t))=\operatorname{lcm}(\pi_a(s),\pi_a(t)).
\]
These general matrix and least-common-multiple facts are classical; see Renault [2].

**The two-power modulus.** Since \(a\) is even, let \(e=\nu_2(a)\ge1\) and \(m=2^{e+1}\). The first terms are
\[
U_2=a,\quad U_3=a^2-1,\quad U_4=a(a^2-2),\quad U_5=a^4-3a^2+1.
\]
Here \(U_1\not\equiv0\pmod m\), \(U_2\not\equiv0\pmod m\), and \(U_3\) is odd. Since \(a^2-2\equiv2\pmod4\), the fourth term has valuation \(e+1\) at \(2\). Thus \(\alpha_a(m)=4\). Also \(2e\ge e+1\), so \(U_5\equiv1\pmod m\), and the recurrence state at index \(4\) is \((U_4,U_5)\equiv(0,1)\pmod m\). Thus \(\pi_a(m)=4\) and \(\omega_a(m)=1\).

**The odd rank and doubled period for every power of three.** Since \(a\equiv1\pmod3\), the recurrence modulo \(3\) begins \(0,1,1,0,-1,-1,0,1\), so \(\alpha_a(3)=3\) and \(\pi_a(3)=6\).

For any positive integer \(r\), put \(V_r=U_{r+1}-U_{r-1}\). The standard companion identities, obtained by multiplying the roots of \(X^2-aX+1\) or by induction, are
\[
V_r^2-4=(a^2-4)U_r^2,\qquad
U_{3r}=U_r(V_r^2-1)
       =U_r\bigl(3+(a^2-4)U_r^2\bigr).
\]
The identities remain valid at the double-root parameter, although here \(a\ge4\). Whenever \(3\mid U_r\), the last parenthesis is divisible by \(3\). Starting with \(3\mid U_3\), repeated tripling yields \(3^j\mid U_{3^j}\) for every \(j\ge1\). Therefore the least zero index \(R=\alpha_a(3^j)\) divides the odd number \(3^j\); in particular \(R\) is odd. Because the period modulo \(3^j\) is a multiple of its reduction's period \(\pi_a(3)=6\), it is even. Since \(\omega_a(3^j)\in\{1,2\}\) and \(R\) is odd, necessarily
\[
\pi_a(3^j)=2R,\qquad \omega_a(3^j)=2.
\]

**Combination.** The moduli \(m=2^{e+1}\) and \(n=3^j\) are coprime. With \(R\) odd, the lcm identities give
\[
\alpha_a(mn)=\operatorname{lcm}(4,R)=4R,
\quad
\pi_a(mn)=\operatorname{lcm}(4,2R)=4R.
\]
Thus \(\omega_a(mn)=1\) although the constituent orders are \(1\) and \(2\), proving the theorem for every stated parameter.

## Verification
The smallest example is \(a=4\), \(m=8\), \(n=3\): the ranks and periods are respectively \((4,4)\), \((3,6)\) and \((12,12)\) modulo \(8\), \(3\) and \(24\). The standalone integer-arithmetic verifier `verify.py` checks \(17\) admissible coefficients \(4\le a\le100\), four powers \(3^j\) per coefficient, and the two polynomial identities at \(153\) integer inputs. It is a finite consistency check, **not** a proof of the infinitely quantified theorem. The proof above supplies that quantification.

## Relationship to prior work
Benfield and Lippard [1, Section 5, Conjecture 5.2 and Table 8] conjecture that the order modulo a least common multiple is \(2\) when one constituent has order \(1\) and the other order \(2\), for all recurrences with second coefficient \(-1\). Their v1 (July 2024) and v2 (January 2025) both state this. The displayed family contradicts this exact mixed entry, not merely an analogous conjecture. Renault [2, Theorem 1] proves the rank and period lcm formulas and [2, final section] treats the general range of orders. Those classical formulas are explicitly used rather than claimed as new; the new assertion is the infinite concrete simultaneous realization with order changing from \(2\) to \(1\). The known period-equality question for companion Lucas sequences concerns a different invariant and does not imply these examples.

## Limitations
The argument refutes only the mixed \((1,2)\) entry of the proposed table. It does not classify every pair of moduli or every recurrence coefficient, nor does it assert which other entries remain valid. Although no equivalent infinite counterexample family was located in the inspected sources, previously unindexed work remains possible. The result has not received independent external mathematical audit.

## References
[1] B. Benfield and O. Lippard, *Connecting Zeros in Pisano Periods to Prime Factors of K-Fibonacci Numbers*, arXiv:2407.20048v1 (first public release 2024-07-29), Conjecture 5.2 and Table 8; see also arXiv:2407.20048v2 (2025-01-30). https://arxiv.org/html/2407.20048v2

[2] M. Renault, *The Period, Rank, and Order of the (a,b)-Fibonacci Sequence Mod m*, Mathematics Magazine **86** (2013), 372--380, DOI:10.4169/math.mag.86.5.372, especially Theorem 1 and the section on order.

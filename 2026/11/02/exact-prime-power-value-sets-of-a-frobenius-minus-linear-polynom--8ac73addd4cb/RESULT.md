# Exact prime-power value sets of a Frobenius-minus-linear polynomial

## Finding
For an odd prime \(p\), let \(f_p(X)=X^p-pX\) and let \(V_{p,k}=\{f_p(x)\bmod p^k:x\in\mathbb Z\}\), with \(R_{p,k}=|V_{p,k}|\). The image is classified for every \(k\ge1\), and a uniform all-prime density follows.

For \(p\ge5\), write \(S_p(0)=1\) and, for integers \(m\ge1\), define the number of square residues modulo \(p^m\) by
\[
S_p(m)=1+\frac{p-1}{2}\sum_{j=0}^{\lfloor(m-1)/2\rfloor}p^{m-2j-1}.
\]
Then the exact image cardinality is
\[
R_{p,1}=R_{p,2}=p,\qquad R_{p,k}=p^{k-2}+(p-1)S_p(k-3)\quad(k\ge3).
\]
The normalized image density tends to
\[
\lim_{k\to\infty}\frac{R_{p,k}}{p^k}=\frac{3p+1}{2p^2(p+1)}\quad(p\ge5).
\]
The exceptional ternary branch has the simple stabilized description
\[
V_{3,k}=\{y\bmod3^k:y\bmod81\in T\}\quad(k\ge4),
\]
where \(T=\{0,2,9,18,27,29,36,45,52,54,63,72,79\}\). Thus
\[
R_{3,1}=3,\quad R_{3,2}=3,\quad R_{3,3}=5,\quad R_{3,k}=13\cdot3^{k-4}\;(k\ge4),
\qquad\lim_{k\to\infty}R_{3,k}/3^k=13/81.
\]
Beyond cardinalities, when \(p\ge5\) the full \(p\)-adic image is a disjoint union of one linear cylinder and \(p-1\) translated/scaled square sets, specified below.

## Assumptions and scope
All residue rings are \(\mathbb Z/p^k\mathbb Z\); \(p\) runs over **all odd rational primes**. The notation \(\mathbb Z_p\) means the ring of \(p\)-adic integers. A value set counts distinct outputs, not multiplicities. Let \(\mu_{p-1}\subset\mathbb Z_p^\times\) be its \(p-1\) Teichmüller roots, uniquely lifting all nonzero residues modulo \(p\); write \(\mathbb Z_p^2=\{z^2:z\in\mathbb Z_p\}\). A square residue modulo the trivial ring \(p^0=1\) is counted once.

## Proof
**Step 1: The zero residue input ball.** Write \(x=pt\), with \(t\in\mathbb Z_p\). Then
\[
f_p(pt)=p^2\bigl(-t+p^{p-2}t^p\bigr).
\]
The polynomial \(h(t)=-t+p^{p-2}t^p\) reduces to \(-t\) modulo \(p\), while its derivative \(h'(t)=-1+p^{p-1}t^{p-1}\) is a unit everywhere. By the simple-root version of Hensel's lemma, each \(b\in\mathbb Z_p\) has exactly one preimage \(t\) in \(\mathbb Z_p\). Hence the zero input ball has image exactly \(p^2\mathbb Z_p\), containing \(p^{k-2}\) residues at level \(k\ge2\) (one at \(k=1\)).

**Step 2: Unit input balls for \(p\ge5\).** Every unit has a unique representation \(x=\zeta+pt\), with \(\zeta\in\mu_{p-1}\) and \(t\in\mathbb Z_p\). Since \(\zeta^p=\zeta\) and \(f_p'(\zeta)=0\), the binomial expansion gives
\[
f_p(\zeta+pt)=(1-p)\zeta+p^3u_\zeta t^2 U_\zeta(t),\qquad
u_\zeta=\frac{p-1}{2}\zeta^{p-2}\in\mathbb Z_p^\times,
\]
with \(U_\zeta(t)\in1+p\mathbb Z_p[t]\). Indeed, the quadratic coefficient is \(\binom p2p^2\zeta^{p-2}=p^3u_\zeta\), and all higher terms have at least one extra factor of \(p\) for \(p\ge5\). The convergent binomial square root \(W_\zeta(t)=\sqrt{U_\zeta(t)}\) belongs to \(1+p\mathbb Z_p\langle t\rangle\). The map \(t\mapsto H_\zeta(t)=tW_\zeta(t)\) satisfies \(H_\zeta(t)\equiv t\pmod p\) and \(H_\zeta'(t)\equiv1\pmod p\). Solving \(H_\zeta(t)=b\) by Hensel's lemma shows \(H_\zeta\) is a bijection of \(\mathbb Z_p\). Consequently,
\[
f_p(\zeta+p\mathbb Z_p)=(1-p)\zeta+p^3u_\zeta\mathbb Z_p^2.
\]
The pieces for different \(\zeta\) are pairwise disjoint because their outputs reduce to different nonzero residues modulo \(p\). They are disjoint from the zero branch as well. Thus this equality, together with \(p^2\mathbb Z_p\), is an exact **description of the entire image**. For \(k\le2\), each input residue ball maps to a single residue at level \(k\); for \(k\ge3\), each nonzero input residue class contributes exactly \(S_p(k-3)\) outputs, since multiplication by \(u_\zeta\) and translation preserve cardinality. This proves the first cardinality formula.

**Step 3: Counting squares.** A nonzero square modulo \(p^m\) has an even valuation \(2j<m\). There are \((p-1)p^{m-2j-1}/2\) units that are quadratic residues modulo \(p^{m-2j}\), and zero contributes one more value. Summing gives \(S_p(m)\). Dividing by \(p^m\), the geometric series yields \(\lim_{m\to\infty}S_p(m)/p^m=p/(2(p+1))\). Substituting in the cardinality formula yields \((3p+1)/(2p^2(p+1))\).

**Step 4: The special prime \(p=3\).** On the nonzero input balls the cubic term is not an extra factor of three relative to the quadratic term. Direct expansion gives
\[
f_3(1+3t)=-2+27t^2(t+1),\qquad
f_3(-1+3t)=2+27t^2(t-1).
\]
For \(g_+(t)=t^2(t+1)\), its values modulo three on the classes \(t=0,1,-1\) are respectively \(0,2,0\). The derivatives are units on \(1+3\mathbb Z_3\) and \(-1+3\mathbb Z_3\). By Hensel's lemma those two balls map bijectively onto \(2+3\mathbb Z_3\) and \(3\mathbb Z_3\), respectively. The remaining input ball maps into \(3\mathbb Z_3\), so \(g_+(\mathbb Z_3)=(2+3\mathbb Z_3)\cup3\mathbb Z_3\). Similarly, \(g_-(t)=t^2(t-1)\) maps the input balls \(1+3\mathbb Z_3\) and \(-1+3\mathbb Z_3\) bijectively onto \(3\mathbb Z_3\) and \(1+3\mathbb Z_3\), and its remaining ball introduces no additional values. Thus \(g_-(\mathbb Z_3)=3\mathbb Z_3\cup(1+3\mathbb Z_3)\).

Combining these images with the zero branch \(9\mathbb Z_3\) yields exactly the thirteen residue classes \(T\bmod81\) displayed in the theorem, each a complete \(81\mathbb Z_3\)-coset. Reduction modulo \(3,9,27\) gives image cardinalities \(3,3,5\); for \(k\ge4\), each class modulo 81 has \(3^{k-4}\) lifts. The stabilized ternary formula and its density follow.

## Verification
Run the standalone `verify.py` with Python 3. It enumerates every input at the specified small prime powers, compares the unique-output count with the claimed exact formulas, and independently checks the proposed 13 residue classes modulo 81, including their lift stability through modulus \(3^9\). The experiment does not establish the infinite family: Steps 1–4 do so via \(p\)-adic Hensel arguments.

## Relationship to prior work
Classical finite-field value-set studies include Chou–Gomez-Calderon–Mullen (1988) and Mullen–Muratović-Ribić–Wang (2015). The latter characterizes finite-field image size through a polynomial coefficient matrix, but is restricted to finite fields and does not give the level-by-level image of \(X^p-pX\) over \(\mathbb Z/p^k\mathbb Z\). Bremser–Gomez-Calderon (1991) specifically studies Dickson polynomials over Galois rings; our \(p=3\) member agrees with the Dickson cubic \(X^3-3X\), which makes that source a meaningful priority risk for the ternary branch. For \(p\ge5\), \(X^p-pX\) is not the degree-\(p\) Dickson polynomial, and the proof relies instead on the explicitly exhibited critical square-map normal forms. Shang (2023) proves extremal **upper bounds** on value-set cardinalities for arbitrary nonpermutation polynomials over residue rings, rather than this specified family's exact images. No claim is made that Hensel's lemma, Teichmüller representatives, or local Morse reductions are new.

## Limitations
Historical priority for the ternary specialization is uncertain because the complete 1991 Galois-ring paper was not available for inspection. The broader prime-uniform formulas are not inferred from searches alone; an equivalent treatment in unlocated literature remains possible. The result concerns only odd primes, this specified Frobenius-minus-linear family, and distinct values, not their full fiber distribution. It has not received independent mathematical audit.

## References
1. G. L. Mullen, A. Muratović-Ribić, and Q. Wang, *On coefficients of powers of polynomials and their compositions over finite fields*, arXiv:1503.07487v1, submitted 2015-03-25, MSC 11T06.
2. P. S. Bremser and J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250, DOI:10.1016/0022-314X(91)90087-R.
3. W. S. Chou, J. Gomez-Calderon, and G. L. Mullen, *Value sets of Dickson polynomials over finite fields*, Journal of Number Theory 30 (1988), 334–344, DOI:10.1016/0022-314X(88)90006-6.
4. W. J. Ralph, *The value set of polynomials over \(\mathbb Z_m\) and the combinatorics of sequences*, Mathematika 42 (1995), 190–198, DOI:10.1112/S0025579300011487.
5. S. Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226v1 (2023).

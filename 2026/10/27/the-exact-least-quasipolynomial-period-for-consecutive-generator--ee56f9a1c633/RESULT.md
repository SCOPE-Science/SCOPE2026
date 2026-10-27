# The exact least quasipolynomial period for consecutive-generator Frobenius quotients

## Finding
For each fixed integer \(p\ge 2\) and every integer \(a>p\), let
\[
 S_a=\langle a,a+1\rangle=\{ua+v(a+1):u,v\in\mathbb Z_{\ge0}\},\qquad
 G_p(a)=\max\{n\in\mathbb Z_{\ge0}:pn\notin S_a\}.
\]
The least positive quasipolynomial period of the function \(a\mapsto G_p(a)\) is **exactly \(p\)**. This sharpens the previously established bound that the period divides \(p\), including all **composite** moduli. More explicitly, for every proper positive divisor \(d\mid p\), set \(k=p/d\). The branch on multiples of \(p\) is
\[
 G_p(a)=\frac{a^2}{p}-a-1\qquad (a>p,\ a\equiv0\pmod p),
\]
whereas for all \(a>p\) with \(a\equiv d\pmod p\),
\[
 G_p(a)\ge \frac{a^2}{p}-a-1+
 \frac{(d-1)(k-1)a+p-d}{p} > \frac{a^2}{p}-a-1.
\]
The term displayed after the plus sign is strictly positive, even when \(d=1\). These two branches, although congruent modulo \(d\), therefore cannot come from one polynomial branch of period \(d\).

## Assumptions and scope
A *quasipolynomial period* \(q\ge1\) means that polynomials \(P_0,\ldots,P_{q-1}\in\mathbb C[X]\) exist with \(G_p(a)=P_r(a)\) whenever \(a>p\) is an integer satisfying \(a\equiv r\pmod q\). A least period is the least positive such \(q\). The parameter \(p\) is an arbitrary fixed integer, **not necessarily prime**; the variable \(a\) ranges through **all** integers \(a>p\), without a primality or coprimality restriction on \(a,p\). Throughout, \(\mathbb Z_{\ge0}\) includes zero.

## Proof
**Gap parametrization.** Write a nonnegative integer uniquely as \(x=ua+v\) with \(0\le v<a\). Then \(x\in S_a\) if and only if \(v\le u\): in this case \(x=(u-v)a+v(a+1)\), and in the reverse direction every expression in the generators yields a quotient at least its remainder. Consequently the positive gaps are exactly
\[
 F_a-ia-j,\quad F_a=a^2-a-1,\quad 0\le j\le i\le a-2. \tag{1}
\]
Indeed \(F_a-ia-j=(a-2-i)a+(a-1-j)\), whose remainder exceeds its quotient, and the reverse substitution \(i=a-2-u\), \(j=a-1-v\) covers every gap.

**Upper period \(p\).** The greatest gap of \(S_a/p\) is the largest gap in (1) divisible by \(p\), divided by \(p\). Therefore
\[
 G_p(a)=\frac{F_a-\min\{ia+j:0\le j\le i\le a-2,\quad ia+j\equiv F_a\pmod p\}}p. \tag{2}
\]
For each fixed residue \(r=a\bmod p\), an admissible pair exists with \(i=p-1\): choose \(j\) to be the least residue of \(r^2-1\) modulo \(p\). Since \(a>p\), every admissible pair with \(i\ge p\) has cost at least \(pa>(p-1)a+p-1\) and hence cannot minimize (2). Among pairs \(i<p\), the congruence determines the unique \(j\in\{0,\ldots,p-1\}\) (if any), and \(0\le j\le i\). Increasing \(i\) by at least one increases \(ia+j\) by at least \(a-(p-1)>0\). Thus the minimizing integers \(I_p(r),J_p(r)\) depend only on \(r\), not on \(a\), and
\[
 G_p(a)=\frac{a^2-(I_p(r)+1)a-(J_p(r)+1)}p,\qquad a\equiv r\pmod p. \tag{3}
\]
This gives the quadratic quasipolynomial of period \(p\), consistent with Liu's published exact residue formula [1].

**A rigid branch.** If \(a\equiv0\pmod p\), then \(F_a\equiv-1\pmod p\), so every admissible \(j\) equals \(p-1\) modulo \(p\). The least possible cost has \(i=j=p-1\), and (2) yields the exact formula
\[
 G_p(a)=\frac{a^2}{p}-a-1. \tag{4}
\]

**A separating branch for each proper divisor.** Let \(d\mid p\) with \(1\le d<p\); set \(k=p/d\ge2\). On the entire residue class \(a\equiv d\pmod p\), take
\[
 i=d+k-2,\qquad j=d-1.
\]
Then \(0\le j\le i\le p-1\le a-2\), because \(p-1-i=(d-1)(k-1)\ge0\). Moreover,
\[
 ia+j\equiv (d+k-2)d+d-1=d^2+dk-d-1
 \equiv d^2-d-1\equiv F_a\pmod p.
\]
Thus (1) yields an actual gap divisible by \(p\), and (2) gives
\[
 G_p(a)\ge\frac{F_a-ia-j}p
 =\left(\frac{a^2}{p}-a-1\right)
 +\frac{(d-1)(k-1)a+(p-d)}p.
 \tag{5}
\]
The correction is positive because \(p-d>0\). If \(d\) were a quasipolynomial period, the infinitely many inputs \(a\equiv0\pmod p\) and \(a\equiv d\pmod p\) would share the same residue class modulo \(d\). A single polynomial cannot agree with (4) on the first infinite progression and be strictly larger on the second. Therefore **no proper divisor of \(p\)** is a period.

**Excluding nondivisor periods.** Suppose a function on all sufficiently large integers has quasipolynomial periods \(p\) and \(q\). Put \(d=\gcd(p,q)\). Let two residues \(r,r'\pmod p\) satisfy \(r\equiv r'\pmod d\), and select a residue \(s\pmod q\) with \(s\equiv r\pmod d\). By the generalized Chinese remainder theorem, each pair of conditions \((a\equiv r\pmod p,\ a\equiv s\pmod q)\) and \((a\equiv r'\pmod p,\ a\equiv s\pmod q)\) holds on an infinite progression. Therefore the polynomial branch for \(r\pmod p\) agrees at infinitely many points with that for \(s\pmod q\), as does the branch for \(r'\pmod p\); all three polynomials are identical. Hence the \(p\)-branches are constant on residue classes modulo \(d\), and \(d\) is itself a quasipolynomial period. Since no proper divisor of \(p\) is a period, \(d=p\), so \(p\mid q\). Thus the least period is exactly \(p\). \(\square\)

## Verification
The independent arithmetic script `VERIFY.py` uses exact integers only. It compares the direct membership/gap definition with the residue-minimization formula for **3,234** combinations \(2\le p\le50\), \(p<a<3p+15\). It also checks the divisor-separation witnesses, their congruences and strict inequalities, and the residue-zero branch at several values of \(a\). These computations were executed and returned `VERIFY_OK`. No finite test is used to infer minimality for infinitely many moduli; that assertion follows from the preceding proof.

Run with `python3 VERIFY.py` from the extracted package directory. No external Python packages or network access are required.

## Relationship to prior work
Feihu Liu [1, Theorem 1.4 and Corollary 5.5] determines every residue-class polynomial of \(G_p\) and proves that \(p\) is a quasipolynomial period, explicitly observing in Definition 5.4 that such a displayed period need not be least. Liu [1, Proposition 5.9] also bounds the number of distinct branches for **prime** \(p\), making the prime-modulus least-period conclusion an implicit special consequence. The new contribution here is a direct **all-moduli sharpness proof**, in particular for every composite \(p\), requiring just one explicit separating witness for each proper divisor.

Strazzanti [2, Section 4] gives quotient Frobenius formulas, notably for moduli \(2\) and \(5\). Cabanillas [3, Section 5] gives a continued-fraction description of general two-generator quotients; it does not state this least-period classification. Liu's preceding paper [4] handles a different family of quotients under a divisibility restriction on the generators. General parametric numerical-semigroup quasipolynomial results [5] concern existence of some eventual period, not this fixed exact minimum. The special prime cases are not claimed as independent novelties.

## Limitations
The theorem concerns exactly the consecutive generators \(a,a+1\), the quotient parameter fixed in advance and \(a>p\). It does not determine the number of distinct polynomial branches, which can be less than \(p\), nor least periods for \(\langle a,b\rangle/p\) with general \(b\), nor effective results for varying \(p\). The claimed originality of the uniform composite-modulus sharpness is based on inspected literature and similarity comparisons, not an exhaustive proof of priority; a previously unnoticed equivalent consequence of a broader semigroup theorem remains a bibliographic risk.

## References
[1] Feihu Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076, first posted July 25, 2026, Sections 2 and 5. https://arxiv.org/abs/2607.23076

[2] Francesco Strazzanti, *Minimal genus of a multiple and Frobenius number of a quotient of a numerical semigroup*, arXiv:1512.00638, Section 4. https://arxiv.org/abs/1512.00638

[3] Emmanuel Cabanillas, *Quotients of numerical semigroups generated by two numbers*, arXiv:1904.08240, Section 5. https://arxiv.org/abs/1904.08240

[4] Feihu Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415, Sections 2–4. https://arxiv.org/abs/2604.26415

[5] Tristram Bogart, John Goodrick and Kevin Woods, *Periodic behavior in families of numerical and affine semigroups via parametric Presburger arithmetic*, arXiv:1911.09136. https://arxiv.org/abs/1911.09136

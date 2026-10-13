# Exceptional \(j=1728\) locus for split-cubic \(D(n)\)-triples
## Finding
Let \(1\le a<b<c\) be positive integers and let \(n\ne0\) be an integer for which \(ab+n\), \(ac+n\), and \(bc+n\) are integer squares. For the split cubic
\[
E_{a,b,c}^{(n)}:y^2=(ax+n)(bx+n)(cx+n),
\]
use the rational Legendre parameter
\[
\lambda=\frac{b(c-a)}{c(b-a)}.
\]
Then
\[
j(E_{a,b,c}^{(n)})=1728
\quad\Longleftrightarrow\quad
\frac2b=\frac1a+\frac1c.
\]
Equivalently, if \(r^2=ab+n\), \(s^2=ac+n\), and \(t^2=bc+n\), then the exceptional condition is
\[
r^2+t^2=2s^2.
\]
Thus the three defining squares form an arithmetic progression. No member of this rational split-cubic family has \(j=0\) over \(\mathbb Q\).

The exceptional locus is genuinely populated. For every integer \(s\ge1\),
\[
\{6s,8s,12s\}
\]
is a \(D(-47s^2)\)-triple, since the three shifted products are \(s^2\), \(25s^2\), and \(49s^2\). Its Legendre parameter is \(2\), so its \(j\)-invariant is \(1728\).

There is also an exact finite-field consequence resolving the exceptional-twist ambiguity in this case. At every good prime \(p\ge5\), a nonsquare quadratic twist of the \(\lambda=2\) Legendre reduction is \(\mathbb F_p\)-isomorphic to the original if and only if \(p\equiv3\pmod4\). For the displayed family, every prime \(p\ge5\) with \(p\nmid 3\cdot47\cdot s\) is good. If in addition \(p\equiv3\pmod4\), then
\[
\#E(\mathbb F_p)=p+1.
\]
For \(p\ge7\) in this congruence class, the cofactor relative to the largest prime divisor of the group order is \(4\) exactly when \((p+1)/4\) is prime.

## Assumptions and scope
The ordering \(1\le a<b<c\), integrality, and \(n\ne0\) are part of the claim. The \(j\)-statements are over \(\mathbb Q\); they do not assert that a nonzero rational \(j\)-invariant cannot reduce to \(0\) at a special prime. The finite-field statement is only for the \(j=1728\) locus, and the explicit point-count formula is asserted only at good primes with \(p\equiv3\pmod4\).

For the explicit scaled family, the bad-prime support is contained in the primes dividing \(2\cdot3\cdot47\cdot s\). Thus the stated condition \(p\ge5\) and \(p\nmid3\cdot47\cdot s\) is sufficient for good reduction.

## Proof
For a Legendre curve the standard formula is
\[
j(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.
\]
Direct subtraction gives the exact factorization
\[
256(1-\lambda+\lambda^2)^3-1728\lambda^2(1-\lambda)^2
=64(\lambda+1)^2(\lambda-2)^2(2\lambda-1)^2.
\]
Because \(a<b<c\),
\[
\lambda-1=\frac{a(c-b)}{c(b-a)}>0,
\]
so \(\lambda>1\). Among the three rational solutions \(-1,1/2,2\) of \(j(\lambda)=1728\), only \(\lambda=2\) is therefore possible. The equation \(\lambda=2\) is equivalent to
\[
b(c-a)=2c(b-a)
\quad\Longleftrightarrow\quad
b(a+c)=2ac
\quad\Longleftrightarrow\quad
\frac2b=\frac1a+\frac1c.
\]
Writing \(r^2=ab+n\), \(s^2=ac+n\), and \(t^2=bc+n\), the middle equality is \(ab+bc=2ac\); after adding \(2n\), this is exactly \(r^2+t^2=2s^2\). Finally, \(j(\lambda)=0\) would require \(\lambda^2-\lambda+1=0\), which has no rational root.

For the scaled family, direct calculation gives
\[
(6s)(8s)-47s^2=s^2,\qquad
(6s)(12s)-47s^2=25s^2,\qquad
(8s)(12s)-47s^2=49s^2,
\]
and
\[
\lambda=\frac{8s(12s-6s)}{12s(8s-6s)}=2.
\]
This proves existence at every scale.

Translate the Legendre curve at \(\lambda=2\) by \(u=x+1\). Its equation becomes
\[
y^2=x^3-x.
\]
A nonsquare quadratic twist by \(d\in\mathbb F_p^\times\) has the short Weierstrass form \(y^2=x^3-d^2x\). It is \(\mathbb F_p\)-isomorphic to \(y^2=x^3-x\) exactly when \(d^2\) is a fourth power. If \(d\) is nonsquare, this happens exactly when \(p\equiv3\pmod4\): for \(p\equiv3\pmod4\), fourth powers and squares coincide, whereas for \(p\equiv1\pmod4\), the square \(d^2\) lies in the non-fourth-power square coset.

When \(p\equiv3\pmod4\), the trace of \(y^2=x^3-x\) is zero. Indeed, pairing \(x\) with \(-x\) in the quadratic-character sum works because \(\chi_p(-1)=-1\). Hence the group order is \(p+1\), and every quadratic twist also has trace zero. The split-cubic reduction is one of these twists under the stated normalization, so its order is also \(p+1\). Since \(4\mid p+1\), writing \(p+1=4m\) shows that the cofactor with respect to the largest prime divisor is \(4\) exactly when \(m\) itself is prime.

## Verification
The companion script `verify_exceptional_j.py` uses only exact integer arithmetic. It verifies the polynomial factorization coefficient-by-coefficient, checks the \(D(-47s^2)\) identities and \(\lambda=2\) for several scales, and exhaustively counts points on \(y^2=x^3-x\) for all sampled primes below \(200\), confirming order \(p+1\) whenever \(p\equiv3\pmod4\). The packaged replay returned `VERIFY_OK family_scales=6 primes_below_200=44 trace_zero_cases=23`. These finite checks support the algebra but are not used as a substitute for the general proof.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa, and Sukhonwimolmal give the split-cubic normalization, the parameter \(\lambda=b(c-a)/(c(b-a))\), the twist relation, and a bounded finite-field census. Their discussion explicitly notes that exceptional \(j\)-invariants can make a nonsquare twist isomorphic to the original, while their census is descriptive and does not classify this exceptional locus. The present result identifies the full rational \(j=1728\) locus in their ordered positive family, proves that it occurs in an infinite scaled family of integral \(D(n)\)-triples, and resolves the nonsquare-twist isomorphism question for that locus.

Earlier work of Dujella associates full-rational-\(2\)-torsion elliptic curves to Diophantine triples and studies rank and torsion; it does not give the harmonic-mean criterion above. Kazalicki and Naskręcki study different elliptic/K3 structures attached to Diophantine triples, including CM phenomena in other fibrations, but this does not imply the parameter-level classification for the split cubic used here.

## Limitations
The result does not classify all integral solutions of \(2/b=1/a+1/c\) that are \(D(n)\)-triples, nor does it give density statements for good primes or cofactor-four primes. The explicit family has varying \(n=-47s^2\), so it is not a fixed-\(n\) infinitude result. At primes \(p\equiv1\pmod4\), the nonsquare twist is proved non-isomorphic to the original, but no general closed point-count formula is asserted here.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa, and T. Sukhonwimolmal, *Split-Cubic Curves from \(D(n)\)-Triples: A Bounded Finite-Field Census*, arXiv:2610.03121v1 (2026).
2. A. Dujella, *Diophantine triples and construction of high-rank elliptic curves over \(\mathbb Q\) with three non-trivial \(2\)-torsion points*, Rocky Mountain J. Math. 30 (2000), 157--164, DOI 10.1216/rmjm/1022008982.
3. M. Kazalicki and B. Naskręcki, *Diophantine triples and K3 surfaces*, J. Number Theory 236 (2022), 41--70, DOI 10.1016/j.jnt.2021.07.009.

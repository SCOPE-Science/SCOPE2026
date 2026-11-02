# Exact residue fibers of tetrahedral numbers at every modulus

## Finding

Put \(B(n)=\binom n3=n(n-1)(n-2)/6\) for integers \(n\ge0\), with \(B(0)=B(1)=B(2)=0\). This is the tetrahedral sequence after an index shift. For every integer \(m\ge2\), its **least** index period modulo \(m\) is
\[
L(m)=m\gcd(m,6).
\]
For each residue \(y\pmod m\), let
\[
F_m(y)=\#\{0\le n<L(m):B(n)\equiv y\pmod m\}.
\]
The following rules specify \(F_m(y)\) exactly, with no restrictions on \(m\), and therefore classify every missing residue and every multiplicity.

**Dyadic prime powers.** For \(k\ge1\),
\[
F_2(0)=3,\qquad F_2(1)=1,
\]
where \(F_2\) abbreviates \(F_{2^1}\). For all \(k\ge2\),
\[
F_{2^k}(y)=\begin{cases}5,&y\equiv0\pmod4,\\1,&y\not\equiv0\pmod4.\end{cases}
\]
**Ternary prime powers.** For every \(k\ge1\) and every \(y\pmod{3^k}\),
\[
F_{3^k}(y)=3.
\]
**Odd primes \(p\ge5\).** Let \(k\ge1\), \(q=p^k\), and
\[
f(X)=\frac{(X-1)^3-(X-1)}6,\qquad f'(X)=\frac{3(X-1)^2-1}{6}.
\]
For \(t\in\mathbb F_p\), define the nonsingular multiplicity
\[
r_p(t)=\#\{x\in\mathbb F_p:f(x)=t,\ f'(x)\ne0\}.
\]
The set \(C_p=\{\alpha\in\mathbb Z_p:3\alpha^2=1\}\) has either zero or two elements. For each \(\alpha\in C_p\), put \(v_\alpha=-\alpha/9\), \(c_\alpha=\alpha/2\), interpreted modulo \(p^k\). Define the square-root count
\[
R_{p,h}(u)=\#\{z\pmod{p^h}:z^2\equiv u\pmod{p^h}\},\quad R_{p,0}=1.
\]
For \(y\pmod q\), the critical contribution associated with \(\alpha\) is
\[
H_{p,k,\alpha}(y)=
\begin{cases}
1,&k=1,\ y\equiv v_\alpha\pmod p,\\
pR_{p,k-2}\big(c_\alpha^{-1}(y-v_\alpha)/p^2\big),&k\ge2,\ y\equiv v_\alpha\pmod{p^2},\\
0,&\text{otherwise}.
\end{cases}
\]
In the middle line the quotient is taken modulo \(p^{k-2}\), which is well-defined under the displayed congruence; at \(k=2\) it is the unique element modulo one. The all-level fiber formula is
\[
\boxed{F_{p^k}(y)=r_p(y\bmod p)+\sum_{\alpha\in C_p}H_{p,k,\alpha}(y).}
\]
The square-root term is elementary: for \(h\ge1\), it is \(p^{\lfloor h/2\rfloor}\) when \(u\equiv0\pmod{p^h}\); otherwise if \(e=\nu_p(u)<h\), it is \(2p^{e/2}\) when \(e\) is even and \(p^{-e}u\) is a quadratic residue modulo \(p\), and zero in every other case.

**All moduli.** Write \(m=\prod_{p^k\parallel m}p^k\). Then
\[
\boxed{F_m(y)=\prod_{p^k\parallel m}F_{p^k}(y\bmod{p^k}).}
\]
In particular, using the Legendre symbol \(\chi_p(-3)\), the exact number of distinct tetrahedral residues modulo \(m\) is
\[
\boxed{\#\{B(n)\bmod m:n\ge0\}
=m\prod_{\substack{p\mid m\\p\ge5}}\frac{2p+\chi_p(-3)}{3p}.}
\]
The empty product is one. Thus every residue modulo a number of the form \(2^a3^b\) occurs, whereas the obstruction at other primes is decided entirely modulo the prime, never by higher prime-power digits.

## Assumptions and scope

The integer \(m\) is at least two; the parameter \(k\) is any positive integer; the prime \(p\) is rational. All counts are of **index classes in one least period**, not distinct integer values. For the odd-prime formula, \(\mathbb Z_p\) is the ring of \(p\)-adic integers, and all denominators \(2,6,9\) are units for \(p\ge5\). The polynomial \(f\) is evaluated modulo \(p^k\) using these units. Two critical points exist exactly when \(3\) is a square modulo \(p\), and their critical values are distinct modulo \(p\). The shift between \(B(n)\) and the usual tetrahedral number \(\binom{n+2}{3}\) does not alter full-period frequencies.

## Proof

**1. Powers of two.** Split the input into four classes \(n=4t+r\), \(0\le r<4\). Direct expansion gives
\[
\begin{aligned}
B(4t)&=4h_0(t),&h_0(t)&=\frac{t(8t^2-6t+1)}3,\\
B(4t+1)&=2h_1(t),&h_1(t)&=\frac{t(16t^2-1)}3,\\
B(4t+2)&=4h_2(t),&h_2(t)&=\frac{t(2t+1)(4t+1)}3,\\
B(4t+3)&=1+2h_3(t),&h_3(t)&=\frac{t(16t^2+24t+11)}3.
\end{aligned}
\]
Every \(h_r\) is a polynomial over \(\mathbb Z_2\) and its divided difference \((h_r(s)-h_r(t))/(s-t)\) is odd for distinct \(s,t\in\mathbb Z_2\). Thus each \(h_r\) induces a bijection modulo every \(2^j\): it is an isometry on \(\mathbb Z_2\). In a period of length \(2^{k+1}\), each branch contains \(2^{k-1}\) inputs. The branches \(r=1\) and \(r=3\) contribute one preimage to every even and every odd target, respectively. For \(k\ge2\), each of \(r=0,2\) contributes two further preimages exactly to targets divisible by four, proving the \(5/1\) rule. For \(k=1\), the four inputs give multiplicities \(3,1\). This also proves period divisibility; the shift \(2^k\) is not a period (use \(n=1\) and the \(h_1\) isometry when \(k\ge2\); inspect \(k=1\) directly). Hence the least period is \(2^{k+1}\).

**2. Powers of three.** For \(r\in\{0,1,2\}\), the polynomial \(g_r(t)=B(3t+r)\) has coefficients in \(\mathbb Z_3\) and satisfies
\[
g_r(s)-g_r(t)=(s-t)U_r(s,t),\qquad U_r(s,t)\equiv1\pmod3.
\]
Indeed \(g_r(t)\equiv t\pmod3\) and all its nonlinear coefficients are divisible by three. Thus each \(g_r\) is an isometry on \(\mathbb Z_3\), hence a permutation modulo each \(3^k\). The three branches in \(0\le n<3^{k+1}\) give exactly three preimages to every target. The shift \(3^k\) is not a period because the \(g_0\) branch is an isometry, so the least period is \(3^{k+1}\).

**3. Regular roots at \(p\ge5\).** Since \(6\) is invertible, \(B(n)=f(n)\) is a polynomial on \(\mathbb Z/p^k\mathbb Z\). Its least period is \(p^k\): the top-digit translation by \(p^{k-1}\) changes its value for any \(n\) with \(f'(n)\not\equiv0\pmod p\), and such \(n\) exists. Every nonsingular root modulo \(p\) has precisely one lift to a root modulo \(p^k\) for each fixed target of the same residue class, by Hensel's lemma. This contributes \(r_p(y\bmod p)\).

**4. Singular roots at \(p\ge5\).** Write \(X-1=\alpha+t\), where \(3\alpha^2=1\) and \(t\in p\mathbb Z_p\). Exact expansion gives
\[
f(1+\alpha+t)=-\frac\alpha9+\frac\alpha2t^2+\frac16t^3
=v_\alpha+c_\alpha t^2\left(1+\frac{t}{3\alpha}\right).
\]
The analytic change \(u=t\sqrt{1+t/(3\alpha)}\) is a bijective isometry of \(p\mathbb Z_p\). Indeed the square root with residue one exists by Hensel's lemma; the convergent expansion gives \(u(t)=t+O(t^2)\), where on \(p\mathbb Z_p\) the correction has Lipschitz constant at most \(p^{-1}\). Thus differences preserve valuation, and for any prescribed output, solving \(t=u-(u(t)-t)\) by contraction gives a unique input. Thus the critical branch is exactly the quadratic congruence \(c_\alpha u^2\equiv y-v_\alpha\pmod{p^k}\) with \(u\equiv0\pmod p\). For \(k=1\) it contributes one when its critical residue is hit. For \(k\ge2\), set \(u=pz\); solutions can exist only when \(y\equiv v_\alpha\pmod{p^2}\), and each root of \(z^2\) modulo \(p^{k-2}\) has \(p\) lifts to \(z\pmod{p^{k-1}}\), giving exactly \(H_{p,k,\alpha}(y)\). The elementary square-root count follows by comparing valuations and applying Hensel's lemma to the two unit roots when they exist. No other singular roots exist, proving the full fiber formula.

**5. The number of attained prime-field values.** In \(\mathbb F_p\), a target with two roots arises precisely from a critical point of \(f\); for every such critical value there is also a distinct simple root, because
\[
f(1+\alpha)-f(1+u)=-\frac{(\alpha-u)^2(2\alpha+u)}6
\]
when \(3\alpha^2=1\). Thus **every attained residue has a nonsingular preimage**, which proves that each attained class modulo \(p\) has all \(p^{k-1}\) lifts among the values modulo \(p^k\). To count the missing classes modulo \(p\), use the collision identity
\[
f(x)=f(y),\ x\ne y\quad\Longleftrightarrow\quad
(x-1)^2+(x-1)(y-1)+(y-1)^2=1.
\]
Let \(\chi=\chi_p(-3)\) and \(C=1+\chi_p(3)\). The right-hand conic has \(p-\chi\) ordered points (the split/nonsplit binary quadratic norm count); precisely \(C\) lie on its diagonal. The cubic has \(C\) values with two roots; writing \(N_3\) for the number with three roots, distinct ordered collisions count in two ways to yield \(p-\chi-C=2C+6N_3\). Thus \(N_3=(p-\chi-3C)/6\). Since the missing-value count is \(C+2N_3\), it equals \((p-\chi)/3\). The attained-value count is therefore \((2p+\chi)/3\).

**6. Composite moduli.** The prime-power periods are powers of distinct primes, hence pairwise coprime. The Chinese remainder theorem makes a complete index period modulo \(m\) the direct product of prime-power index periods, giving the stated factorization of \(F_m\). The prime-power least periods also force the product to be the least period; this is \(m\gcd(m,6)\). Multiplying the local image counts proves the displayed product formula.

## Verification

The supplied standalone `verify.py` constructs every residue fiber directly over periods of \(2^{k+1}\), \(3^{k+1}\), and \(p^k\), and independently computes the predicted fibers by the prime-wise formulas, including critical-point Hensel lifts and quadratic-root counts. It compares every fiber for \(55\) prime-power levels with \(p^k\le35000\), totaling \(205113\) target fibers, and confirms \(27\) composite-modulus Chinese-remainder examples. The verification is finite; the six proof steps above establish the unrestricted statements.

## Relationship to prior work

The first-prime-level cubic congruences are classical; the finite-field value-set count for the cubic is a special case of the known Dickson-polynomial value-set theory. The period formula for tetrahedral numbers for arbitrary moduli also appears in Ahmed's 2019 work. The new assertion assessed here is the **combined all-modulus value-fiber classification**, including the all-level ternary equidistribution, the dyadic fivefold exceptional fibers, and the precise singular-lift corrections at odd primes. The 2011 modular-class study of tetrahedral numbers treats the first modular layers, not this full all-prime-power fiber formula.

## Limitations

The results concern one specific integer-valued cubic and cannot be inferred for arbitrary figurate polynomials. The odd-prime formulas are algorithmically explicit, using small-field root checks and Hensel lifts rather than a uniform target-by-target closed elementary expression free of root testing. The 1991 article of Bremser and Gomez-Calderon on Dickson polynomials over Galois rings describes some preimage counts; its full text was not accessible for a complete priority comparison. This is a genuine residual literature risk particularly for the odd-prime subformula. The result has only been reviewed within the present mathematical analysis; no independent validation is claimed.

## References

1. J. V. Leyendekkers and A. G. Shannon, *The structure of geometric number sequences*, Notes on Number Theory and Discrete Mathematics **17**(3) (2011), 31–37, https://nntdm.net/papers/nntdm-17/NNTDM-17-3-31-37.pdf (tetrahedral modular classes).
2. Z.-H. Sun, *Cubic congruences and sums involving* \(\binom{3k}{k}\), arXiv:1310.6721, first posted 2013-10-24, https://arxiv.org/abs/1310.6721 (general cubic-congruence root criteria).
3. W. S. Chou, J. Gomez-Calderon, and G. L. Mullen, *Value sets of Dickson polynomials over finite fields*, J. Number Theory **30** (1988), 334–344, DOI:10.1016/0022-314X(88)90006-6.
4. P. S. Bremser and J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, J. Number Theory **38** (1991), 240–250, DOI:10.1016/0022-314X(91)90087-R (abstract accessible; full text not inspected).
5. M. M. Ahmed, *A Platonic basis of integers*, arXiv:1904.02787v1 (2019), https://arxiv.org/abs/1904.02787, Proposition 3.1 (periodicity, not target-frequency formulas).

# Exact GCDs of even-length Fibonacci and Lucas cubic windows

## Finding

Let \(F_0=0,F_1=1\) and \(L_0=2,L_1=1\), with both sequences satisfying \(X_{n+2}=X_{n+1}+X_n\). For a positive integer \(k\), write
\[
D_F(k)=\gcd_{n\ge0}\sum_{j=1}^{k}F_{n+j}^{3},\qquad
D_L(k)=\gcd_{n\ge0}\sum_{j=1}^{k}L_{n+j}^{3}.
\]
Here each gcd is the positive gcd of the indicated infinite family. Define \(\varepsilon_3(m)=1\) if \(3\mid m\) and zero otherwise; define \(\varepsilon_4(m)=1\) if \(4\mid m\) and zero otherwise. **For every integer \(m\ge1\)**,
\[
\boxed{D_F(2m)=\begin{cases}
 L_m/2^{\varepsilon_3(m)},&m\text{ odd},\\
 3^{\varepsilon_4(m)}F_m/2^{\varepsilon_3(m)},&m\text{ even},
\end{cases}}
\]
and
\[
\boxed{D_L(2m)=\begin{cases}
 L_m/2^{\varepsilon_3(m)},&m\text{ odd},\\
 5\cdot3^{\varepsilon_4(m)}F_m/2^{\varepsilon_3(m)},&m\text{ even}.
\end{cases}}
\]
All displayed quantities are positive integers. In particular, at window length six both gcds are \(2\). The Fibonacci cubic formula proposed in Mbirika--Spilker, Question 6.1, predicts \(4\) at that length and hence does not hold as printed.

## Assumptions and scope

There are no unproved hypotheses. The result is for the standard Fibonacci and Lucas initial conditions and every **even** positive window length, with cubes of individual terms taken **before** summing. It does not assert a formula for odd window lengths or for arbitrary generalized Fibonacci initial values. For identity manipulations we extend both sequences to every integer index by the same recurrence: \(F_{-r}=(-1)^{r+1}F_r\), \(L_{-r}=(-1)^rL_r\) for positive \(r\).

## Proof

**1. Two basic cubic-window identities.** The standard cubic identities, obtained by expanding the Binet expressions, are
\[
5F_r^3=F_{3r}-3(-1)^rF_r,\qquad
L_r^3=L_{3r}+3(-1)^rL_r.
\]
For either \(X=F\) or \(X=L\), the recurrence gives
\[
X_{3r+2}-X_{3r-1}=2X_{3r},\qquad
\sum_{j=1}^{k}(-1)^{n+j}X_{n+j}
=(-1)^{n+k}X_{n+k-1}-(-1)^nX_{n-1}.
\]
Thus, when \(k=2m\), putting \(S^X_n=\sum_{j=1}^{2m}X_{n+j}^3\),
\[
10S^F_n=F_{3(n+2m)+2}-F_{3n+2}-6(-1)^n(F_{n+2m-1}-F_{n-1}),\tag{1}
\]
\[
2S^L_n=L_{3(n+2m)+2}-L_{3n+2}+6(-1)^n(L_{n+2m-1}-L_{n-1}).\tag{2}
\]

**2. Pairing the endpoints at the half-length.** Standard addition identities, or the Binet formulas, give for every integer \(r\):
\[
\begin{array}{c|cc}
& m\text{ odd}&m\text{ even}\\\hline
F_{r+2m}-F_r&L_mF_{r+m}&F_mL_{r+m}\\
L_{r+2m}-L_r&L_mL_{r+m}&5F_mF_{r+m}
\end{array}
\]
and the triple-index identities yield
\[
L_{3m}=L_m(L_m^2+3)\quad(m\text{ odd}),\qquad
F_{3m}=F_m(L_m^2-1)\quad(m\text{ even}).
\]
Put \(s=L_m\), \(t=n+m\), and define the integer sequences
\[
T_a(t)=aF_{3t+2}+6(-1)^tF_{t-1},\qquad
U_a(t)=aL_{3t+2}-6(-1)^tL_{t-1}.
\]
Substitution into (1)--(2), noting \((-1)^n=(-1)^{t-m}\), gives the **exact four-way reduction**
\[
\begin{array}{c|cc}
 &m\text{ odd}&m\text{ even}\\\hline
10S^F_n&s\,T_{s^2+3}(t)&F_m\,U_{s^2-1}(t)\\
2S^L_n&s\,U_{s^2+3}(t)&5F_m\,T_{s^2-1}(t).
\end{array}\tag{3}
\]

**3. Two exact integer-sequence gcd lemmas.** Both \(T_a(t)\) and \(U_a(t)\), for any integer \(a\), satisfy the integral reversible recurrence with characteristic polynomial
\[
(z^2-4z-1)(z^2+z-1)=z^4-3z^3-6z^2+3z+1.
\]
Indeed, their exponential roots are the two roots of the cubic-index Fibonacci/Lucas recurrence, together with the negatives of the two roots of the ordinary recurrence. The leading and constant coefficients are both \(1\), so any four consecutive integer values generate, by integral forward and backward recurrence, precisely the same gcd as all values at \(t\ge m\), for every fixed integer \(m\).

The first four values are
\[
\begin{split}
(T_a(0),T_a(1),T_a(2),T_a(3))
 &=(a+6,5a,21a+6,89a-6),\\
(U_a(0),U_a(1),U_a(2),U_a(3))
 &=(3a+6,11a+12,47a-6,199a+18).
\end{split}
\]
Here \(T_a(2)=T_a(0)+4T_a(1)\), \(T_a(3)=-T_a(0)+18T_a(1)\), \(U_a(2)=-21U_a(0)+10U_a(1)\), and \(U_a(3)=-73U_a(0)+38U_a(1)\). Hence the gcds of all terms (and of every positive tail) are exactly
\[
\gcd_tT_a(t)=\gcd(a+6,5a)=\gcd(a+6,30),\tag{4}
\]
\[
\gcd_tU_a(t)=\gcd(3a+6,11a+12).\tag{5}
\]
In (5), the gcd divides \(30\), since \(11(3a+6)-3(11a+12)=30\).

**4. The final three local divisibility tests.** Use
\[
L_m^2-5F_m^2=4(-1)^m,\quad
2\mid L_m\iff3\mid m,\quad
3\mid L_m\iff m\equiv2\pmod4.
\]
The last two are immediate from the Lucas recurrence modulo \(2\) and modulo \(3\); the second applies to every integer \(m\), and the third to every nonnegative index. In particular, \(3\nmid L_m\) when \(m\) is odd.

For odd \(m\), (4) and \(L_m^2\equiv1\pmod5\) give
\[
\gcd(L_m^2+9,30)=\begin{cases}5,&3\mid m,\\10,&3\nmid m.\end{cases}
\]
For odd \(m\), applying (5) with \(a=L_m^2+3\), the two arguments are \(3L_m^2+15\) and \(11L_m^2+45\). Their gcd is \(1\) when \(3\mid m\), and \(2\) otherwise (no factor \(3\) or \(5\) is possible). Substituting into (3) gives the first branches of both formulas.

For even \(m\), write \(a=L_m^2-1\). The two arguments in (5) become \(3L_m^2+3\) and \(11L_m^2+1\). Their gcd, a divisor of \(30\), has factor \(5\) always; factor \(2\) exactly when \(3\nmid m\); and factor \(3\) exactly when \(4\mid m\). Thus
\[
\gcd(3L_m^2+3,11L_m^2+1)=
5\cdot2^{1-\varepsilon_3(m)}3^{\varepsilon_4(m)}.
\]
Similarly (4) yields
\[
\gcd(L_m^2+5,30)=2^{1-\varepsilon_3(m)}3^{\varepsilon_4(m)}.
\]
Inserting these last two equalities into (3) and dividing by the respective factors \(10\) and \(2\) proves the remaining branches. Multiplication by the nonnegative constants in (3) commutes with taking positive integer gcds; all denominators cancel as specified. This completes the proof.

## Verification

The standalone `verify_cubic_windows.py` checks the exact cubic-sum identities, half-length reductions, and stated GCD formula for every \(1\le m\le160\), using twelve independent sliding windows for each of the two sequences. It also checks the two-parameter four-term identities and characteristic recurrence for all \(-500\le a\le500\), and the contrasting window-six values. Execute from this directory using `python3 verify_cubic_windows.py`; no nonstandard packages are needed. The program prints a line beginning `VERIFY_OK` on success. These tests are independent finite consistency checks; the preceding algebraic argument proves the infinite claim.

For a small explicit witness, at \(k=6\) the Fibonacci windows beginning at \(F_1\) and \(F_2\) sum to \(674\) and \(2870\), whose gcd is \(2\). The theorem also proves every longer window sum is divisible by \(2\); the proposed formula in Question 6.1 instead gives \(\gcd(F_7^3-1,F_8^3-1)=4\).

## Relationship to prior work

Mbirika and Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers* (first posted 2022-04-26), prove the corresponding square-window formulas and in §6.1 explicitly pose the cubic extension and conjectural even-window expressions. Their printed Fibonacci expression fails already at \(k=6\); the present theorem supplies exact expressions for **both** Fibonacci and Lucas cubic windows for every even length. The printed Lucas candidate also contains a second subtraction of \(9\) despite the indicated cubic power, so it should not be silently identified with subtraction of \(L_2^3=27\). Our result is based directly on the infinite-window gcd definition, not that displayed candidate.

Guyer and Mbirika (2021) compute first-power GCDs. Mbirika, Schrader and Spilker (2023) treat six Pell-type first-power sequences and some square-window instances. Their stated results do not imply the third-power Fibonacci/Lucas formulas here. Targeted indexed-record and literature searches yielded no identified stronger third-power result, but such searches cannot establish exhaustive publication priority.

## Limitations

The theorem covers even lengths only, standard Fibonacci/Lucas initial values, and cubes only. No statement about odd lengths, all Gibonacci initial conditions, or higher powers is claimed. The checker is finite and not an independent certification of the proof. The 2022 preprint's conjectural status is reported accurately; correcting a conjecture does not establish absolute priority over unindexed later publications.

## References

1. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626, first public version 2022-04-26, especially §6.1 and Theorems 5.2--5.4. https://arxiv.org/abs/2204.12626
2. Dan Guyer and aBa Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262, first public version 2021-04-25. https://arxiv.org/abs/2104.12262
3. aBa Mbirika, Janee Schrader and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, arXiv:2301.05758, first public version 2023-01-13. https://arxiv.org/abs/2301.05758

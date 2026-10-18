# Exact two-nonzero-digit Niven counts and a 48-phase decimal law

## Finding

A base-\(b\) Niven (Harshad) integer is divisible by its sum of base-\(b\) digits. For \(b\ge2\) and integer \(L\ge1\), let \(H_b(L)\) count integers \(0<n<b^L\) with exactly two nonzero base-\(b\) digits that are Niven.

**Gap classification.** Write any such two-nonzero-digit integer uniquely as \(n=a b^i+c b^j\), with \(1\le a,c<b\) and \(0\le i<j<L\). Put \(m=a+c\), let \(q\) denote the largest divisor of \(m\) coprime to \(b\), and set
\[
 h=\frac{q}{\gcd(q,c)},\qquad
 \lambda_{a,c}=\operatorname{ord}_{h}(b),
\]
where \(\operatorname{ord}_1(b)=1\). With \(v_p\) the usual prime valuation, set
\[
 I_{a,c}=\max_{p\mid b}\max\left\{0,\left\lceil\frac{v_p(a+c)-v_p(a)}{v_p(b)}\right\rceil\right\}.
\]
Then the **necessary and sufficient** condition is
\[
 \boxed{m\mid n\quad\Longleftrightarrow\quad i\ge I_{a,c}\ \text{and}\ \lambda_{a,c}\mid(j-i).}
\]

Define for positive integer \(t\) and integer \(N\)
\[
 F_t(N)=\sum_{k\ge1}\max(N-tk,0),\qquad
 Q_t(N)=\max\left(0,\left\lfloor\frac{N-1}{t}\right\rfloor\right).
\]
The sum is finite and has the exact form
\[
 F_t(N)=Q_t(N)N-\frac{t}{2}Q_t(N)(Q_t(N)+1).
\]
For **every** \(L\ge1\), not merely asymptotically,
\[
 \boxed{H_b(L)=\sum_{a=1}^{b-1}\sum_{c=1}^{b-1}F_{\lambda_{a,c}}(L-I_{a,c}).}
\]

For fixed \(b\), let
\[
 \gamma_b=\frac12\sum_{a,c}\frac1{\lambda_{a,c}},\qquad
 \delta_b=\sum_{a,c}\left(\frac{I_{a,c}}{\lambda_{a,c}}+\frac12\right).
\]
When \(L\ge\max_{a,c}I_{a,c}\), there is an *exact* representation
\[
 H_b(L)=\gamma_bL^2-\delta_bL+\Theta_b(L),
\]
where \(\Theta_b\) is nonnegative, bounded, and periodic with period dividing \(\operatorname{lcm}_{a,c}\lambda_{a,c}\). This implies a rational limiting proportion \(2\gamma_b/(b-1)^2\) among integers with exactly two nonzero base-\(b\) digits below \(b^L\).

**Decimal specialization.** In base \(10\), the complete ordered-digit-pair census \((I,\lambda):\text{multiplicity}\) is
\[
 (0,1):14,\quad(0,2):8,\quad(0,6):14,\quad(0,16):2,
\]
\[
 (1,1):27,\quad(1,6):2,\quad(2,1):8,\quad(3,1):4,\quad(4,1):2.
\]
Writing \(F_t(N)=0\) for \(N\le t\), this gives the *exact all-length formula*
\[
 \begin{aligned}
 H_{10}(L)={}&14F_1(L)+8F_2(L)+14F_6(L)+2F_{16}(L)\\
 &+27F_1(L-1)+2F_6(L-1)\\
 &+8F_1(L-2)+4F_1(L-3)+2F_1(L-4).
 \end{aligned}
\]
Consequently
\[
 \boxed{H_{10}(L)=\frac{1483}{48}L^2-\frac{623}{6}L+\Theta_{10}(L)\quad (L\ge4),}
\]
where \(\Theta_{10}\) has **least positive period \(48\)**. The limiting decimal fraction is
\[
 \boxed{\lim_{L\to\infty}\frac{H_{10}(L)}{81\binom L2}=\frac{1483}{1944}.}
\]

## Assumptions and scope

The base \(b\) is any fixed integer at least two. Digits are conventional, with unique positional expansions; exactly two digit positions contain nonzero digits. The lower exponent \(i\) and upper exponent \(j\) are ordered, and \(a\) is the lower-position digit. The count is over integers below the *exclusive* bound \(b^L\). The empty product and the multiplicative order modulo one are interpreted as one. For a prime \(p\mid b\), \(v_p(a)\) and \(v_p(c)\) are finite because digits are positive.

## Proof

Let \(p\mid b\), write \(e=v_p(a+c)\), \(r=v_p(a)\), \(s=v_p(c)\), and \(w=v_p(b)>0\). If \(r\ne s\), then \(e=\min(r,s)\), so both summands \(a b^i\) and \(c b^j\) are divisible by \(p^e\) for every \(0\le i<j\); the \(p\)-condition is automatic and the corresponding ceiling bound in \(I_{a,c}\) is zero. If \(r=s\), then \(e\ge r\). Because \(j>i\), the valuations \(r+iw\) and \(s+jw\) differ strictly, so
\[
 v_p(a b^i+c b^j)=r+iw.
\]
It follows that \(p^e\) divides \(n\) precisely when \(i\ge\max(0,\lceil(e-r)/w\rceil)\). Combining primes dividing \(b\) yields \(i\ge I_{a,c}\).

For the remaining prime-power factors, \(q\) is coprime to \(b\). Division by the invertible residue \(b^i\) gives
\[
 n\equiv0\pmod q\iff a+c b^{j-i}\equiv0\pmod q
 \iff c(b^{j-i}-1)\equiv0\pmod q,
\]
since \(q\mid a+c\). Dividing by \(\gcd(q,c)\) gives \(b^{j-i}\equiv1\pmod h\), equivalent to \(\lambda_{a,c}\mid(j-i)\). Coprimality of the prime-power parts completes the gap classification.

Fix \((a,c)\) and an admissible gap \(j-i=t k\), \(k\ge1\), with \(t=\lambda_{a,c}\). The inequalities \(I_{a,c}\le i<j<L\) leave exactly \(\max(L-I_{a,c}-tk,0)\) choices for \(i\). Summing gaps and then digit pairs proves the all-length formula. Evaluating the finite arithmetic progression yields the stated floor expression.

For any integer \(N\ge0\), put \(r=N\bmod t\), \(0\le r<t\). Direct evaluation of the same progression gives
\[
 F_t(N)=\frac{N^2}{2t}-\frac N2+\frac{r(t-r)}{2t}.
\]
Substitute \(N=L-I_{a,c}\) and sum. The coefficients of \(L^2\) and \(L\) are exactly \(\gamma_b\) and \(-\delta_b\). The remaining expression is
\[
 \Theta_b(L)=\sum_{a,c}\left(\frac{I_{a,c}^2}{2\lambda_{a,c}}+\frac{I_{a,c}}2+
 \frac{r_{a,c}(\lambda_{a,c}-r_{a,c})}{2\lambda_{a,c}}\right),
 \quad r_{a,c}=(L-I_{a,c})\bmod\lambda_{a,c}.
\]
It is a bounded, periodic nonnegative rational function, proving the fixed-base result and proportion because there are exactly \((b-1)^2\binom L2\) two-nonzero-digit integers below \(b^L\).

For \(b=10\), factor \(a+c\) for each of the 81 ordered digit pairs and calculate the two invariants \(I\) and \(\lambda\). The nine frequencies displayed above sum to 81. Substituting the frequencies into the exact formula gives \(\gamma_{10}=1483/48\) and \(\delta_{10}=623/6\), with \(\max I=4\) and period dividing \(\operatorname{lcm}(1,2,6,16)=48\). To show that the *least* period is 48 rather than a proper divisor, evaluate the 48 rational values \(H_{10}(L)-(1483/48)L^2+(623/6)L\) for \(L=4,\ldots,51\). None of the proper divisors \(1,2,3,4,6,8,12,16,24\) is a period of these 48 values, as the standalone exact-arithmetic verifier checks. Since period 48 has already been proved for all \(L\ge4\), this finite residue check certifies minimality for the infinite tail.

## Verification

The included `verify_niven.py` reconstructs \(I\) and \(\lambda\) from factorizations; checks the decimal frequency table, exact two coefficients, and least period by rational arithmetic; compares two independent population enumerations against the floor formula for several bases and lengths; and reports a deterministic success marker. Example decimal counts are \(H_{10}(2)=14\), \(H_{10}(5)=362\), \(H_{10}(20)=10391\), and \(H_{10}(100)=298685\). The proof is symbolic; regressions are corroboration, not substitutes for infinite arguments.

## Relationship to prior work

Cooper and Kennedy (1985) derive asymptotics for Niven integers of *fixed digit sum* and discuss polynomial residue-class counting; their 1988 follow-up elaborates digit-sum counting constants. These broad digit-sum results overlap with the use of modular periods and mean that generic eventual polynomiality, by itself, is not claimed as new. Neither inspected statement supplies the all-base ordered-two-digit gap criterion, the exact unrestricted-support-two floor formula, or the explicit decimal density and least-period data. Fredricksen, Ionascu, Luca, and Stanica (2008) study the **minimum Niven integer for a specified digit sum**, not counts restricted to exactly two occupied positions. De Koninck, Doyon, and Kátai (2003) prove an unrestricted base-\(b\) Niven counting asymptotic of order \(x/\log x\) (Theorem 1), which does not determine this polylogarithmically sparse support-two component. These distinctions identify the claimed contribution without asserting global uniqueness.

## Limitations

The formula concerns exactly two nonzero digits and cutoffs at exact base powers. It does not give corresponding population laws for arbitrary real cutoffs or for three or more nonzero digits. The 1985 text is accessible through a facsimile OCR whose displayed mathematical formulas are imperfect; a previously unnoticed stronger multiset-counting implication is a residual originality risk. The unrestricted 2003 counting theorem is compatible with, but does not imply, the much smaller support-two law. No independent audit has been performed.

## References

- C. N. Cooper and R. E. Kennedy, "On an Asymptotic Formula for the Niven Numbers," *International Journal of Mathematics and Mathematical Sciences* 8 (1985), 537–543, doi:10.1155/S0161171285000576.
- C. N. Cooper and R. E. Kennedy, "A Partial Asymptotic Formula for the Niven Numbers," *Fibonacci Quarterly* 26 (1988), 163–168, doi:10.1080/00150517.1988.12429647.
- J.-M. De Koninck, N. Doyon, and I. Kátai, "On the counting function for the Niven numbers," *Acta Arithmetica* 106 (2003), 265–275, doi:10.4064/aa106-3-5.
- H. Fredricksen, E. J. Ionascu, F. Luca, and P. Stănică, "Minimal Niven numbers," arXiv:0803.0477v1, first public version 2008-03-04, https://arxiv.org/html/0803.0477v1.

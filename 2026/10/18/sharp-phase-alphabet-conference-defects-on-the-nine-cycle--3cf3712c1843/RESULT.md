# Sharp phase-alphabet conference defects on the nine-cycle

## Finding

Let \(q\in\{2,4,6,8\}\), let \(\zeta_q=e^{2\pi i/q}\), and let \(f:\mathbb Z/9\mathbb Z\to\mathbb C\) satisfy \(f(0)=0\), \(f(j)\in\{\zeta_q^r:0\le r<q\}\) for \(1\le j\le8\), and \(\sum_j f(j)=0\). Define the periodic autocorrelation and its conference defect by
\[
 C_f(h)=\sum_{j\in\mathbb Z/9\mathbb Z}f(j+h)\overline{f(j)},\qquad
 \mathcal E_q(f)=\sum_{h=1}^{8}|C_f(h)+1|^2.
\]
For each of the four phase alphabets the feasible set is nonempty. Its **exact minimum**, together with the number of minimizers normalized by \(f(1)=1\), is
\[
\begin{array}{c|c|c|c}
q&\min\mathcal E_q&\text{normalized feasible sequences}&\text{normalized minimizers}\\\hline
2&16&35&12\\
4&16&1225&84\\
6&4&9135&6\\
8&24-16\sqrt2&23765&6
\end{array}.
\]
In particular, no conference signal on the nine-cycle can use solely eighth roots of unity under these constraints, and the optimal positive defect is exactly \(24-16\sqrt2\). The next strictly greater defect among admissible eighth-root sequences is \(40-24\sqrt2\).

The six normalized eighth-root optimizers are **exactly** the exponent lists \((r_1,\ldots,r_8)\) below, with \(f(j)=\zeta_8^{r_j}\):
\[
\begin{gathered}
(0,1,3,7,3,7,5,4),\\
(0,2,2,5,1,6,6,4),\\
(0,3,4,2,6,0,7,4),\\
(0,5,4,6,2,0,1,4),\\
(0,6,6,3,7,2,2,4),\\
(0,7,5,1,5,1,3,4).
\end{gathered}
\]
They form one orbit under multiplication by an eighth root of unity, cyclic-group index dilations by units modulo \(9\), and complex conjugation. There are exactly \(48\) unnormalized eighth-root optimizers.

## Assumptions and scope

The time domain is the additive group \(\mathbb Z/9\mathbb Z\); no restriction to odd signals is imposed. The Fourier transform is **unnormalized**:
\[
\widehat f(k)=\sum_{j=0}^{8}f(j)e^{-2\pi i jk/9}.
\]
The condition \(\widehat f(0)=0\) is imposed, rather than optimized. All minimization is over *precisely* the indicated roots-of-unity alphabet, not arbitrary unimodular phases. A conference signal would have \(C_f(h)=-1\) at all nonzero lags and \(|\widehat f(k)|^2=9\) for every nonzero frequency. Since \(C_f(0)=8\), Fourier inversion and Parseval give the exact alternate description
\[
\mathcal E_q(f)=\frac19\sum_{k=1}^{8}\bigl(|\widehat f(k)|^2-9\bigr)^2.
\]
Thus the invariant is spectral variance around the optimal flat spectrum, equivalently the squared Frobenius correlation error of the corresponding punctured circulant design.

## Proof

**1. Exhaustive normalization.** Multiplying the entire sequence by a common member of the phase alphabet preserves all constraints and the defect, so every orbit has exactly one representative with \(f(1)=1\). The remaining seven exponents independently range over \(\{0,\ldots,q-1\}\). Consequently an exhaustive proof requires at most \(q^7\) representatives, with no untested sequences.

**2. Exact zero-mean test.** In the integer basis \(1,\zeta_q,\ldots,\zeta_q^{\varphi(q)-1}\) of the cyclotomic field, represent each \(\zeta_q^r\) by the residue of \(X^r\) modulo the monic cyclotomic polynomial. For the four cases these are
\[
\Phi_2(X)=X+1,\quad \Phi_4(X)=X^2+1,\quad
\Phi_6(X)=X^2-X+1,\quad \Phi_8(X)=X^4+1.
\]
Because these are the minimal polynomials, an eight-term phase sum is zero if and only if each integer coordinate vanishes. This tests the mean condition without floating-point tolerance.

**3. Exact energy.** For nonzero \(h\), write \(W_h=1+C_f(h)\). Each \(W_h\) is a sum of cyclotomic integer basis vectors and \(W_{9-h}=\overline{W_h}\). Hence
\[
\mathcal E_q(f)=2\sum_{h=1}^{4}|W_h|^2.
\]
The norm squares of vectors with integer coordinates are exact integers for \(q=2,4,6\). Specifically, for \(q=6\), if \(W_h=a+b\zeta_6\), then \(|W_h|^2=a^2+ab+b^2\). For \(q=8\), write \(W_h=a+b\zeta_8+c\zeta_8^2+d\zeta_8^3\); then
\[
|W_h|^2=(a^2+b^2+c^2+d^2)
 +[a(b-d)+c(b+d)]\sqrt2.
\]
Thus every tested defect is represented *exactly* as an integer pair \((A,B)\), meaning \(A+B\sqrt2\) (and \(B=0\) in the first three cases). Two such pairs are strictly ordered using integer-square comparisons and the irrationality of \(\sqrt2\); no rounding is used in the certificate.

**4. Complete finite certificate.** The complete executable enumerator `verify_phase_energy.py` iterates over all \(q^7\) normalized exponents for each alphabet, discards only candidates that fail the exact coordinate-wise zero-mean test, computes all four autocorrelation terms by modular-index arithmetic in the same exact cyclotomic basis, and compares the resulting energy pairs exactly. The four exhaustive candidate counts, minima, and minimizer counts are precisely those stated in the table. For the eighth-root case it independently checks the explicit set of six exponent lists and that the second-smallest distinct pair is \((40,-24)\). This is an exhaustive **finite** proof, not an extrapolation from sampling or an optimization heuristic. The script has no nonstandard dependencies.

**5. Orbit and positivity.** Acting by index dilation \(j\mapsto uj\) for \(u\in(\mathbb Z/9\mathbb Z)^\times\), conjugating all phases, and then renormalizing \(f(1)\) sends the displayed first optimizer through exactly the six listed normalized exponent tuples (direct modular exponent calculation). Allowing eight independent choices of common phase gives \(6\cdot8=48\) unnormalized optimizers. Finally, \(24-16\sqrt2>0\), since \(24^2>2\cdot16^2\). Thus exact eighth-root flatness is impossible within the prescribed class.

## Verification

Run `python3 verify_phase_energy.py` using ordinary Python 3. It reproduces, using integral arithmetic, the entire table and six eighth-root minimizers; also checks the second distinct octary defect and independently evaluates the autocorrelation defect of an extremizer using complex trigonometric functions to verify normalization. On the checked system the script exited successfully and printed `Exact cyclotomic checks: PASS`. The exact finite exhaustive computation, rather than the numerical comparison, establishes the theorem.

## Relationship to prior work

Fallon and Iverson's 2026 paper introduces and studies conference signals and provides energy minimization over **unrestricted unimodular phases** (Section 3), including numerical examples at cyclic order nine. Their Theorem 2.1 supplies the exact zero-autocorrelation equivalence used here. Their continuous-phase constructions have zero conference defect but do not determine the **positive optimal defects** under the four specified quantized alphabets, nor the finite octary optimizer orbit. Chee, Tan, and Zhou study **perfect and nearly-perfect** almost prime-ary sequences and existence obstructions, rather than exact squared correlation-loss minima for binary, quadriphase, six-phase, and eight-phase nine-cycle designs. Hence neither cited work directly determines the present four sharp finite-alphabet values. Earlier or unindexed equivalent exact enumerations remain a priority risk.

## Limitations

The theorem is specific to length nine, the mandatory zero and zero-mean conditions, and phase alphabets \(\mu_2,\mu_4,\mu_6,\mu_8\). It does not state an optimal bound for arbitrary phases or other cyclic orders. The computations enumerate finitely many exact algebraic candidates; they do not imply any broader classification of conference signals. The result has not undergone independent audit, and historical priority is not conclusively established.

## References

1. K. Fallon and J. W. Iverson, *Conference signals: Applications, existence, and constructions*, arXiv:2610.09169v1, first posted 6 October 2026; particularly Theorem 2.1 and Section 3. https://arxiv.org/abs/2610.09169
2. Y. M. Chee, Y. Tan, and Y. Zhou, *Almost p-Ary Perfect Sequences*, Sequences and Their Applications—SETA 2010, Lecture Notes in Computer Science 6338, pp. 399–415, 2010. https://doi.org/10.1007/978-3-642-15874-2_34

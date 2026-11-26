# Sharp digit envelopes and oscillation constants for positive Galileo sequences

## Finding
Fix an integer \(k\ge2\). A normalized positive integer Galileo sequence is a sequence \((a_n)_{n\ge1}\) of positive integers with \(a_1=1\), whose partial sums \(S_0=0\), \(S_n=\sum_{j=1}^{n}a_j\) obey \(S_{2n}=kS_n\) for every \(n\ge1\). Define
\[
L_k(0)=0,\qquad L_k(n)=\sum_{j\ge0}\varepsilon_j k^j
\quad\text{if}\quad n=\sum_{j\ge0}\varepsilon_j2^j,\ \varepsilon_j\in\{0,1\}.
\]
For \(n\ge1\) set \(r(n)=\lceil\log_2n\rceil\) and \(U_k(n)=k^{r(n)}-L_k(2^{r(n)}-n)\). These definitions include powers of two and \(n=1\).

**Sharp simultaneous envelopes.** Every sequence in this class satisfies \(L_k(n)\le S_n\le U_k(n)\) for all \(n\ge1\). There is a single sequence realizing the lower envelope at all indices and a single sequence realizing the upper envelope at all indices.

**Sharp growth constants.** With \(\alpha=\log_2k\), every sequence in this class satisfies
\[
\frac{n^{\alpha}}{k-1}\le S_n\le \left(k-\frac1{k-1}\right)n^{\alpha}.
\]
Neither coefficient can be improved uniformly over the class and all positive indices. For the extremal sequences,
\[
\liminf_{n\to\infty}\frac{L_k(n)}{n^\alpha}=\frac1{k-1},\qquad
\limsup_{n\to\infty}\frac{L_k(n)}{n^\alpha}=1,
\]
\[
\liminf_{n\to\infty}\frac{U_k(n)}{n^\alpha}=1,\qquad
\limsup_{n\to\infty}\frac{U_k(n)}{n^\alpha}=k-\frac1{k-1}.
\]
At \(k=2\), both envelopes equal \(n\) and both coefficients equal one.

## Assumptions and scope
The terms are positive integers, \(S_1=1\), and \(k\ge2\) is an integer. The terms need not be monotone. All asymptotic assertions refer to infinite sequences. No scaled bounds for the unrestricted class with \(S_1>1\) are asserted: scaling the constructions does not exhaust that class.

## Proof
**Pointwise comparison.** Positivity and integrality imply, for \(m\ge1\),
\[
S_{2m}=kS_m,\qquad kS_m+1\le S_{2m+1}\le kS_{m+1}-1.
\]
Since \(L_k(2m)=kL_k(m)\) and \(L_k(2m+1)=kL_k(m)+1\), strong induction starting at \(S_1=1\) proves the lower comparison. For the upper comparison, define \(V(1)=1\) and \(V(2m)=kV(m)\), \(V(2m+1)=kV(m+1)-1\) for \(m\ge1\). These recurrences involve smaller indices and give \(S_n\le V(n)\) by strong induction. The formula for \(U_k\) satisfies the same recurrences. For even \(n=2m\), the exponent \(r(n)\) is \(r(m)+1\) and the reflected argument of \(L_k\) is doubled. For odd \(n=2m+1\ge3\), \(r(n)=r(m+1)+1\). With \(h=2^{r(n)-1}-(m+1)\), the reflected argument is \(2h+1\), and \(L_k(2h+1)=kL_k(h)+1\). Thus \(U_k=V\).

**Simultaneous realization.** Incrementing a binary numeral changes a block of \(t\) trailing ones to zeros and adds a one in position \(t\). The digit map increases by \(k^t-\sum_{j=0}^{t-1}k^j\ge1\). The positive integral differences of \(L_k\) therefore realize the lower envelope and satisfy the dilation identity. To realize the upper envelope, set \(a_1=1\), \(a_2=k-1\), and recursively set \((a_{2m-1},a_{2m})=(ka_m-1,1)\) for \(m\ge2\). Each pair, including the initial pair, sums to \(ka_m\); this gives \(S_{2n}=kS_n\) by summation. All terms are positive integers, and \(S_{2m+1}=kS_{m+1}-1\) for \(m\ge1\). The upper recurrence identifies the partial sums as \(U_k\).

**Growth of \(L_k\).** Superadditivity of \(x\mapsto x^\alpha\) for \(\alpha\ge1\) gives \(L_k(n)\le n^\alpha\). For the converse bound, write \(n=2^j+t\), \(0\le t<2^j\). Since \((2^j+t)^\alpha-t^\alpha\) is nondecreasing in \(t\),
\[
n^\alpha-t^\alpha\le(2^{j+1})^\alpha-(2^j)^\alpha=(k-1)k^j.
\]
Induction from zero then gives \(n^\alpha\le(k-1)(k^j+L_k(t))=(k-1)L_k(n)\). Powers \(n=2^j\) give ratio one, and \(L_k(2^j-1)=(k^j-1)/(k-1)\) makes the ratio tend to \(1/(k-1)\).

**Growth of \(U_k\).** The upper recurrence gives \(U_k(n)\ge n^\alpha\) by induction, using for odd indices \((2m+2)^\alpha-1\ge(2m+1)^\alpha\). Let \(r=r(n)\) and \(x=(2^r-n)/2^r\in[0,1/2)\). The lower bound for \(L_k\) gives
\[
\frac{U_k(n)}{n^\alpha}\le F(x)=\frac{1-x^\alpha/(k-1)}{(1-x)^\alpha}.
\]
For \(0<x<1/2\), \(F'(x)=\alpha(1-x^{\alpha-1}/(k-1))/(1-x)^{\alpha+1}\ge0\); the limiting value is \(F(1/2)=k-1/(k-1)\). Powers of two again give ratio one. For \(j\ge1\), \(U_k(2^j+1)=k^{j+1}-(k^j-1)/(k-1)\), so the normalized ratio tends to the limiting upper coefficient. These subsequences and the simultaneous realizations prove sharpness.

## Verification
The accompanying standard-library `verify.py` compares the integer splitting constructions with their digit formulas for \(2\le k\le17\), \(1\le n\le2000\), and enumerates all positive splits for three small horizons to test the pointwise bounds. The recorded run (`python3 verify.py`) reports 32,000 deterministic index checks and 54,300 finite-prefix comparisons. Those are finite checks; the proof above covers every parameter and index in the stated class.

## Relationship to prior work
Cheah and Treeby [1, Theorem 5] give the binary-tree parameterization of positive Galileo sequences. Their Theorem 12 establishes power bounds for nondecreasing integer terms, without the sharp coefficients stated here for arbitrary positive integer terms. The splitting framework and the binary-to-base-\(k\) digit map itself are not new. The contribution is the exact simultaneous optimization of the normalized sequences, including the reflected upper envelope, and evaluation of the sharp family-wide coefficients. Earlier papers [2–4] concern Galileo recurrences, families or iterates. Limits of access to those older papers prevent an exhaustive priority assertion.

## Limitations
This does not classify the attainable values strictly between the two envelopes at a fixed index. It does not extend the estimates to unnormalized, noninteger or nonpositive terms.

## References
1. W. Cheah and D. Treeby, *Structure and Growth of Galileo Sequences*, [arXiv:2604.20889](https://arxiv.org/abs/2604.20889), 2026.
2. K. O. May, *Galileo sequences, a good dangling problem*, American Mathematical Monthly 79 (1972), 67–69, DOI: 10.2307/2978135.
3. D. Zeitlin, *A family of Galileo sequences*, American Mathematical Monthly 82 (1975), 819–822, DOI: 10.2307/2319798.
4. Ö. Eğecioğlu, *A note on iterated Galileo sequences*, Discrete Mathematics, Algorithms and Applications 9 (2017), 1750015, DOI: 10.1142/S179383091750015X.

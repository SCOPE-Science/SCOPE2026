# Exact periodic image law for elementary cellular automaton Rule 30

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous Rule 30 update on an **indexed cyclic ring** with \(n\ge1\), and write \(a_n=|\operatorname{Im}(F_n)|\) and \(b_n=2^n-a_n\). Define integers \(s_0=3\), \(s_1=s_2=1\), and \(s_n=s_{n-1}+2s_{n-3}\) for \(n\ge3\). Then for every integer \(n\ge1\),

\[
\boxed{a_n=2^n-\frac{s_n+1-2\mathbf{1}_{3\mid n}}2,\qquad b_n=\frac{s_n+1-2\mathbf{1}_{3\mid n}}2.}
\]

With the formal generating-function convention \(a_0=1\), the complete all-length image series is

\[
\boxed{\sum_{n\ge0}a_nz^n=\frac{1-2z+2z^2-5z^3+6z^4-z^5+2z^6-4z^7}{(1-z)(1-2z)(1+z+z^2)(1-z-2z^3)}.}
\]

Let \(\rho\approx1.695620769559862\) be the positive root of \(t^3-t^2-2\) and let \(\sigma=\sqrt{2/\rho}<\rho\). The inaccessible-output count and its proportion obey

\[
b_n=\frac12\rho^n+O(\sigma^n),\qquad \frac{b_n}{2^n}=\frac12(\rho/2)^n+O((\sigma/2)^n).
\]

The first values of \(a_n\), for \(1\le n\le17\), are \(1,3,5,11,26,52,106,223,455,923,1882,3816,7710,15571,31395,63199,127110\). For example, the unreachable output counts at lengths \(8,12,16\) are respectively \(33,280,2337\).

## Assumptions and scope

Indices are taken modulo \(n\) and the local rule is exactly

\[
F_n(x)_i=x_{i-1}\oplus(x_i\lor x_{i+1}),
\]

where \(\oplus\) and \(\lor\) are Boolean exclusive-or and inclusive-or. Repeated neighbors on rings of size one or two are evaluated as the same indexed bits. Outputs are distinct **indexed** configurations, not rotation or reflection classes. A predecessor is required to have the **same cyclic period \(n\)**; finite-window preimages on a line or antecedents of longer period are a different question. The length-zero term of the generating function is a counting convention only, not a zero-cell cellular automaton.

## Proof

**1. From backward pair propagation to finite transformations.** For a prescribed output bit \(b\in\{0,1\}\), knowledge of the adjacent input pair \((u,v)=(x_i,x_{i+1})\) determines the preceding pair uniquely:

\[
T_b(u,v)=(b\oplus(u\lor v),u).
\]

Encode \((u,v)\) as \(2u+v\in\{0,1,2,3\}\). The complete truth tables for \(T_0\) and \(T_1\), written as images of inputs \(0,1,2,3\), are respectively

\[
T_0=(0,2,3,3),\qquad T_1=(2,0,1,1).
\]

For any prescribed cyclic output \(y=(y_0,\ldots,y_{n-1})\), iterating the backward maps around the ring closes to an input cycle exactly when the composition \(T_{y_0}\circ\cdots\circ T_{y_{n-1}}\) has a fixed pair-state. Indeed, a fixed pair determines all neighboring pairs by the local inverse rule and the fixed-point condition closes the cycle. Conversely, every same-length predecessor yields such a fixed point. This proves the exact equivalence for all \(n\ge1\), including repeated-neighbor boundary cases.

Begin at the identity transformation on four pair-states and append either transformation by right composition. The generated finite transformation monoid has **exactly 41 distinct transformations**; exactly **30** of these transformations have a fixed point. Both numbers are established by the finite exhaustive generation in `verify.py` and its complete saved transition list `certificate.json`; every new state is produced by a generator and all successors remain in that list. Define a \(41\)-by-\(41\) nonnegative integer matrix \(M\), where \(M_{ij}\) is the number of generator labels taking transformation state \(i\) to state \(j\). Let \(e\) be the row vector selecting the identity and let \(f\) be the column indicator of fixed-point transformations. The fixed-point equivalence gives, for every \(n\ge0\),

\[
a_n=eM^nf,
\]

with \(a_0=1\), since the identity has a fixed point.

**2. Finite exact identity, and why it proves infinitely many lengths.** Set

\[
P(z)=1-2z+2z^2-5z^3+6z^4-z^5+2z^6-4z^7,
\]

\[
Q(z)=(1-z)(1-2z)(1+z+z^2)(1-z-2z^3).
\]

By the adjugate formula,

\[
\sum_{n\ge0}eM^nf\,z^n=e(I-zM)^{-1}f=H(z)/D(z),
\]

where \(D(z)=\det(I-zM)\), \(D(0)=1\), \(\deg D\le41\), and \(\deg H\le40\). The numerator \(QH-PD\) has degree at most \(48\). The independent recurrences in `verify.py`, applied to the exact complete monoid transitions in `certificate.json`, compute and compare **all 49 integer coefficients**, from degree \(0\) through degree \(48\), of \(e(I-zM)^{-1}f\) and \(P/Q\). They agree exactly. Since both denominators have constant term one, the first 49 zero coefficients of their difference imply the numerator \(QH-PD\), whose degree is at most 48, is the zero polynomial. Therefore \(H/D=P/Q\) as formal rational power series, with no untested higher-length inference.

The public certificate stores all 41 transformations, every two-letter transition, all acceptance bits, both candidate polynomials, and all 49 checked coefficients; the verifier re-derives each entry, rather than trusting the stored numbers.

**3. Closed formula.** Let \(s_n\) be the power sums of the three roots (with multiplicity) of \(t^3-t^2-2\). Newton's identities give \(s_0=3\), \(s_1=s_2=1\), and \(s_n=s_{n-1}+2s_{n-3}\), so

\[
\sum_{n\ge0}s_nz^n=\frac{3-2z}{1-z-2z^3}.
\]

Algebraic combination with the proved expression \(P/Q\) gives the exact formal identity

\[
2\left(\frac1{1-2z}-\frac{P(z)}{Q(z)}\right)
=\frac{3-2z}{1-z-2z^3}-3+\frac{z}{1-z}-\frac{2z^3}{1-z^3}.
\]

For each positive degree \(n\), the left coefficient is \(2(2^n-a_n)=2b_n\), while the right coefficient is \(s_n+1-2\mathbf{1}_{3\mid n}\). This proves both exact counts. The constant-degree coefficient is zero, consistent with the formal \(a_0\) convention.

**4. Asymptotics.** The real cubic has one positive root \(\rho\); its other two roots form a conjugate pair. Vieta's product formula makes their common modulus \(\sigma=\sqrt{2/\rho}\). Consequently the power sum satisfies \(s_n=\rho^n+O(\sigma^n)\). Because \(\sigma>1\), the bounded correction \(1-2\mathbf{1}_{3\mid n}\) is absorbed in the error term. Dividing by \(2^n\) gives the asserted vanishing fraction of missing configurations.

## Verification

Place `RESULT.md`, `verify.py`, and `certificate.json` in one directory and run:

```bash
python3 verify.py
```

The script uses only Python's standard library. A successful replay prints `VERIFY_OK` after rebuilding the 41-state closure from the two local inverse maps; comparing the certificate's complete tables and 49 exact coefficient values; checking the rational identity by coefficient recursion; and independently enumerating **all binary input rings of every length from 1 through 17**, computing distinct direct Rule 30 images. The exhaustive finite rings are an independent cross-check; the infinite theorem rests on the exact rational-series degree argument above. The three finite reference counts of unreachable outputs, \(33,280,2337\), agree with the Elementary CA Zoo. More extensively, every inaccessible-state count for ring lengths \(1\) through \(27\) agrees with the independently published 2016 finite state-diagram census by Faulkenberry (Appendix A, Table 6); the verifier derives those lengths from the exact proved recurrence, not from a second enumeration of all inputs through length 27.

## Relationship to prior work

Jen's 1989 *Enumeration of Preimages in Cellular Automata* derives complete finite-block preimage formulas, including Rule 30's four preimages of any given finite window when suitable boundary input bits are allowed. That statement does **not** imply same-period cyclic reachability or count the distinct cyclic outputs for arbitrary \(n\). The difference matters: linear Rule 30 is left-permutive, yet an indexed periodic ring has unreachable finite-period outputs. Wolfram's 1983 statistical-mechanical analysis and his 2019 Rule 30 discussion address fundamental dynamics and finite-ring state transition graphs, not this demonstrated exact image-count sequence. Faulkenberry’s 2016 complete state-diagram table gives the precise Rule 30 unreachable-output counts for each length from \(1\) through \(27\). Those independently tabulated coefficients agree exactly with the present all-length formula, but the inspected thesis sections on state-diagram construction, observed Garden-of-Eden trends, and its Appendix A do not assert a recurrence or rational closed form valid for every ring length. The Elementary CA Zoo also supplies finite examples, but neither finite census alone implies the all-length formula or the exact asymptotic loss exponent.

The local inverse maps, subset automata, and generating-function techniques are classical. The contribution claimed here is solely the explicit, proved all-length **cyclic image counting formula and resulting finite-period orphan law**, not the general methodology, left permutivity, or the existence of finite-ring orphan states.

## Limitations

The result concerns **one synchronous update**, uniform binary alphabet, periodic length-\(n\) inputs and outputs, and indexed states; it does not enumerate all predecessor multiplicities, classify multistep reachable states, or solve any Rule 30 computational universality or long-term unpredictability problem. The derivation is independently replayable but is **not** an independent external mathematical audit. Literature comparison establishes no priority beyond inspected materials; an unindexed exact formula or an inaccessible earlier complete study could cover the same statement. The full 1983 manuscript was not materially inspected in this analysis, although its dated bibliographic record and associated Rule 30 historical context were checked.

## References

1. S. Wolfram, “Statistical Mechanics of Cellular Automata,” *Reviews of Modern Physics* **55**, 601–644 (published 1 July 1983), https://doi.org/10.1103/RevModPhys.55.601 .
2. E. Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* **3** (1989), 421–456. Primary full text: https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
3. S. Wolfram, “Announcing the Rule 30 Prizes” (1 October 2019), https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/ .
4. “Gardens of Eden,” Elementary CA Zoo, https://cellular.solves.ca/gardens-of-eden (finite census data; accessed October 2026).
5. S. J. Faulkenberry, *Cellular Automata: Optimal Analysis, Coding, and Testing for Encryption*, M.S. thesis, Middle Tennessee State University (May 2016), Appendix A, Table 6 and Section 6.6. https://jewlscholar.mtsu.edu/server/api/core/bitstreams/46cbf4ee-2dd2-4358-b114-d7844e6cd8f5/content .
6. E. Jen, “Scaling of Preimages,” *Complex Systems* **1** (1987), https://www.complex-systems.com/abstracts/v01_i06_a02/ (abstract-level contextual comparison).

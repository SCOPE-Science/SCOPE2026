# Singleton-prime windows and bounded clustering in reciprocal LCM endpoints

## Finding

Fix a real parameter \(\kappa>5\), and define the normalized reciprocal LCM-power function
\[
Q_\kappa(n)=\left(\frac{n}{\kappa^{\omega(n)}}\sum_{d\mid n}\mu(d)\sigma_{-1}(n/d)^\kappa\right)^{1/(\kappa-1)},\qquad
\sigma_{-1}(m)=\sum_{e\mid m}\frac1e.
\]
Let \(N_\kappa(\varepsilon)\) be the **largest** positive integer maximizing \(Q_\kappa(n)/n^\varepsilon\) over \(n\ge1\), where \(\varepsilon>0\). For sufficiently large primes \(p\), put
\[
t_{p,\kappa}=\frac{\log Q_\kappa(p)}{\log p},\qquad
s_{p,\kappa}=\frac{\log Q_\kappa(p^2)-\log Q_\kappa(p)}{\log p}.
\]
Then the following statements hold.

**Exact singleton window.** For every sufficiently large prime \(p\) (depending on \(\kappa\)),
\[
v_p(N_\kappa(\varepsilon))=1
\quad\Longleftrightarrow\quad
s_{p,\kappa}<\varepsilon\le t_{p,\kappa}.
\]
The window is nonempty, and its width satisfies
\[
t_{p,\kappa}-s_{p,\kappa}
=\frac{\kappa-5}{12p^2\log p}
+O_\kappa\!\left(\frac1{p^3\log p}\right).
\]

**Simultaneous-singleton localization.** Let \(p<q\) be distinct primes both occurring to exponent exactly one in the *same* \(N_\kappa(\varepsilon)\). Then, uniformly over all such pairs as \(\varepsilon\to0^+\),
\[
q-p\le \frac{\kappa-5}{6}+o_\kappa(1).
\]
Consequently, the number of exponent-one primes in \(N_\kappa(\varepsilon)\) is bounded by a constant depending only on \(\kappa\), uniformly for \(\varepsilon>0\). If \(5<\kappa<17\), then every sufficiently late endpoint contains **at most one** exponent-one prime. For every fixed \(\kappa>5\), infinitely many distinct endpoints contain an exponent-one prime; when \(5<\kappa<17\), infinitely many contain **exactly one**.

## Assumptions and scope

All logarithms are natural; \(\mu\) is the Möbius function and \(\omega\) counts distinct prime divisors. Prime-power local factors for \(a\ge1\) are
\[
Q_\kappa(p^a)^{\kappa-1}
=\frac{p^a}{\kappa}\left[\sigma_{-1}(p^a)^\kappa-\sigma_{-1}(p^{a-1})^\kappa\right],
\qquad Q_\kappa(1)=1.
\]
Existence, finiteness, primewise maximization, and tie-breaking for \(N_\kappa(\varepsilon)\) are those of Molnar's Definition 4.1 and Lemma 4.2. In each local tie, the *largest* exponent is used. The asymptotic statements fix \(\kappa\) before taking \(p\to\infty\) or \(\varepsilon\to0^+\); no uniformity for growing \(\kappa\) is asserted.

## Proof

**1. Analytic local expansions.** Write \(x=1/p\), \(r=\kappa-1\), and \(L_a(x)=\log Q_\kappa(p^a)\), interpreted through the exact prime-power formulas as real-analytic functions near \(x=0\). Explicitly,
\[
Q_\kappa(p)^r=\frac{(1+x)^\kappa-1}{\kappa x},\qquad
Q_\kappa(p^2)^r=\frac{(1+x+x^2)^\kappa-(1+x)^\kappa}{\kappa x^2}.
\]
Taylor expansion (with removable singularities at \(x=0\)) yields
\[
L_1(x)=\tfrac12x+\tfrac{\kappa-5}{24}x^2+O_\kappa(x^3),
\qquad L_2(x)=x+O_\kappa(x^3),
\]
and hence
\[
2L_1(x)-L_2(x)=\tfrac{\kappa-5}{12}x^2+O_\kappa(x^3).
\]
The claimed window width follows directly. For sufficiently large \(p\), \(0<s_{p,\kappa}<t_{p,\kappa}\), with
\[
s_{p,\kappa}\sim t_{p,\kappa}\sim\frac1{2p\log p}.
\]

**2. No competing exponents.** At fixed \(p\), write
\[
H_{p,\varepsilon}(a)=\log Q_\kappa(p^a)-a\varepsilon\log p
\quad(a\ge0).
\]
The comparisons \(H(1)\ge H(0)\) and \(H(1)>H(2)\), including the largest-exponent tie convention, are equivalent to \(\varepsilon\le t_{p,\kappa}\) and \(\varepsilon>s_{p,\kappa}\), respectively. They are necessary for selecting exponent one. Conversely, Molnar's strict local estimate gives \(Q_\kappa(p^a)<p/(p-1)\) for every \(a\ge1\). Let
\[
b_{p,\kappa}=\frac{\log(p/(p-1))-\log Q_\kappa(p)}{2\log p}
\sim\frac1{4p\log p}.
\]
For sufficiently large \(p\), \(s_{p,\kappa}>b_{p,\kappa}\). Whenever \(\varepsilon>s_{p,\kappa}\) and \(a\ge3\),
\[
H_{p,\varepsilon}(a)-H_{p,\varepsilon}(1)
<\log\frac p{p-1}-\log Q_\kappa(p)-(a-1)\varepsilon\log p<0.
\]
Thus no \(a\ge3\) can compete. Conversely, if \(a=1\) is selected, comparison against both \(0\) and \(2\) forces the stated half-open window. The window is nonempty by Step 1.

**3. Prime-window diameter.** Extend \(t_{p,\kappa}\) to the smooth real-variable function
\[
T_\kappa(u)=\frac{L_1(1/u)}{\log u}\quad(u>1).
\]
The convergent local Taylor series also differentiates, giving
\[
T_\kappa(u)=\frac1{2u\log u}+O_\kappa\!\left(\frac1{u^2\log u}\right),\qquad
T'_\kappa(u)=-\frac1{2u^2\log u}(1+o_\kappa(1)).
\]
For sufficiently large \(p\), \(T_\kappa\) is strictly decreasing. If \(p<q\) both have exponent one at parameter \(\varepsilon\), then
\[
0<T_\kappa(p)-T_\kappa(q)
< t_{p,\kappa}-s_{p,\kappa}
=\frac{\kappa-5}{12p^2\log p}(1+o_\kappa(1)).
\]
If \(q/p\) failed to tend to \(1\), the left-hand difference would be of order \(1/(p\log p)\), contradicting the right-hand order \(1/(p^2\log p)\). Therefore \(q/p\to1\). The mean-value theorem, uniformly on the interval \([p,q]\), now gives
\[
T_\kappa(p)-T_\kappa(q)
=\frac{q-p}{2p^2\log p}(1+o_\kappa(1)),
\]
proving \(q-p\le(\kappa-5)/6+o_\kappa(1)\).

**4. Uniformity and the sharp low-parameter consequence.** For every fixed prime \(p\), the local power-mean representation puts \(Q_\kappa(p^2)>Q_\kappa(p)\), so \(s_{p,\kappa}>0\). Thus as \(\varepsilon\to0^+\), all primes selected at exponent one necessarily tend to infinity. The diameter estimate in Step 3 is consequently uniform among any such primes. A bounded-diameter interval contains a bounded number of integers, proving bounded singleton support as \(\varepsilon\to0^+\). For parameters bounded away from zero, local optimality against exponent zero and \(Q_\kappa(p^a)<p/(p-1)\) leave only finitely many possible primes, giving the global bound. If \(5<\kappa<17\), the asymptotic diameter is strictly below \(2\), but sufficiently large distinct primes differ by at least \(2\); hence at most one singleton occurs at small \(\varepsilon\).

Finally, for every sufficiently large prime \(p\), take \(\varepsilon=(s_{p,\kappa}+t_{p,\kappa})/2\). The local exponent-one conclusion follows from Step 2, and \(\varepsilon\to0^+\) as \(p\to\infty\). The canonical endpoints are unbounded along these choices (each includes its selected prime), so infinitely many distinct ones exist. In \(5<\kappa<17\), the at-most-one conclusion makes their singleton count exactly one. \(\square\)

## Verification

The accompanying standard-library Python script `verify_singleton_windows.py` evaluates the two exact rational prime-power factors at high decimal precision for several integer parameters and primes. It tests the half-open window at its midpoint against local exponents \(0\) through \(13\), and bounds all larger exponents by \(Q_\kappa(p^a)<p/(p-1)\). It also illustrates the normalized width convergence and checks the negative-width comparison at lower integer parameters over a finite prime range. These numerical tests are ancillary: the infinite theorem follows from the analytic estimates and primewise optimization above.

## Relationship to prior work

Molnar, *Reciprocal LCM powers and Robin's criterion*, arXiv:2610.12816v1 (8 October 2026), defines and factorizes these normalized endpoints (Definition 4.1, Lemma 4.2), proves the needed strict local upper bound (Lemma 3.1), and observes the critical \(\kappa=5\) sign change in \(Q_\kappa(p^2)/Q_\kappa(p)^2\) (Remark after Corollary 4.8). Its Lemma 4.5 instead bounds repeated prime support over a wide fractional range below the largest prime. The explicit singleton window, its simultaneous-prime diameter bound, the globally bounded singleton count, and the at-most-one law for \(5<\kappa<17\) are not stated in that source. They require comparing both local transition thresholds across distinct primes, not only the sign of their difference. Fan–Kobayashi–Molnar, *A family of analogues to the Robin criterion*, arXiv:2511.02106, concerns the earlier **nonreciprocal** LCM-power function and does not directly optimize these normalized reciprocal endpoint exponents.

## Limitations

The constants and the onset of the assertions depend on fixed \(\kappa\); no effective uniform prime threshold in \(\kappa\) or exact finite list of exceptional small primes is claimed. The result does not classify how many singleton primes are achieved for large \(\kappa\), quantify the number of singleton-containing endpoints of bounded size, or establish the Robin inequality itself. No conclusion about the unnormalized endpoint family is intended. Previously unindexed equivalent results remain a possible originality risk; independent mathematical audit has not been performed.

## References

1. G. Molnar, *Reciprocal LCM powers and Robin's criterion*, arXiv:2610.12816v1, 8 October 2026, https://arxiv.org/html/2610.12816v1 .
2. S. Fan, M. Kobayashi, and G. Molnar, *A family of analogues to the Robin criterion*, arXiv:2511.02106v1, 3 November 2025, https://arxiv.org/abs/2511.02106 .

# Phase-rigid sharp fourth moments for characteristic-two APN graph extension

## Finding

For every power \(q=2^n\) with \(n\ge1\), let \(F:\mathbb F_q\to\mathbb F_q\) be any map, and let \(\psi:\mathbb F_q\to\mathbb C\) be a nontrivial additive character. Set
\[
\mathcal E_F f(X,Y)=\frac1q\sum_{t\in\mathbb F_q} f(t)\psi(Xt+YF(t)),\qquad
\mathcal C(F)=\sup_{f\ne0}\frac{\sum_{X,Y\in\mathbb F_q}|\mathcal E_Ff(X,Y)|^4}{(q^{-1}\sum_t|f(t)|^2)^2}.
\]
Then \(\mathcal C(F)\ge 3-2/q\), with equality **if and only if** \(F\) is almost perfect nonlinear (APN). In fact, for non-APN maps,
\[
\mathcal C(F)\ge3-\frac2q+\frac8{q^2}.
\]
If \(F\) is APN, write \(S=\sum_t|f(t)|^2\), \(Q=\sum_t|f(t)|^4\), and \(T=\sum_t f(t)^2\). For every complex-valued \(f\), the exact fourth moment is
\[
q^2\sum_{X,Y}|\mathcal E_Ff(X,Y)|^4=|T|^2+2(S^2-Q).
\]
Its **sharp global deficit** is the explicit sum of squares
\[
\begin{aligned}
&\left(3-\frac2q\right)\left(\frac Sq\right)^2-
 \sum_{X,Y}|\mathcal E_Ff(X,Y)|^4\\
&=\frac1{q^2}\sum_{t<u}\left[
 |f(t)\overline{f(u)}-\overline{f(t)}f(u)|^2
 +\frac2q\bigl(|f(t)|^2-|f(u)|^2\bigr)^2
 \right].
\end{aligned}
\]
Here the order \(t<u\) is *any* fixed total ordering of the field elements, used once per unordered pair. Every nonzero equality case is exactly
\[
f(t)=\lambda\varepsilon_t,\qquad
\lambda\in\mathbb C\setminus\{0\},\quad
\varepsilon_t\in\{+1,-1\}\ \text{for all }t.
\]
Thus there are precisely \(2^{q-1}\) equality classes modulo nonzero complex scaling.

## Assumptions and scope

The ambient additive group is \((\mathbb F_q^2,+)\), which has exponent two. The additive character may be any nontrivial one; all conclusions are character-independent. A map \(F\) is APN when, for every \(s\ne0\) and every \(w\in\mathbb F_q\), the equation \(F(t+s)+F(t)=w\) has at most two solutions. Since solutions occur in pairs \(t,t+s\), this condition says that unordered pairs of *distinct* graph points have different sums. All assertions quantify over every \(n\ge1\), every such map and all complex inputs; in particular no primality of \(q\) is assumed.

## Proof

**Fourier normalization.** Place \(f(t)\) at the graph point \((t,F(t))\) in the additive group \(\mathbb F_q^2\), extending it by zero elsewhere; call the resulting function \(g\). Let \(c=g*g\) denote unnormalized convolution. Character orthogonality and Fourier Plancherel give exactly
\[
\sum_{X,Y}|\mathcal E_Ff(X,Y)|^4=\frac1{q^2}\sum_{s,w}|c(s,w)|^2.
\]
There is no approximation or asymptotic normalization in this equality.

**APN collision fibers.** In characteristic two, \((t,F(t))+(t,F(t))=(0,0)\) for every \(t\). Hence \(c(0,0)=\sum_t f(t)^2=T\). If \(s\ne0\), the first coordinate of \((t,F(t))+(u,F(u))\) is \(s=t+u\); an APN map permits at most one unordered pair \(\{t,u\}\) for each pair \((s,w)\). Thus nonzero graph sums each contribute either zero or \(c(s,w)=2f(t)f(u)\). Running once through all unordered distinct pairs gives
\[
\sum_{s,w}|c(s,w)|^2=|T|^2+4\sum_{t<u}|f(t)|^2|f(u)|^2
 =|T|^2+2(S^2-Q).
\]

**Sharp bound and exact remainder.** Expand the difference between the proposed sharp fourth moment and the preceding identity:
\[
q^2\left[\left(3-\frac2q\right)(S/q)^2-\sum_{X,Y}|\mathcal E_Ff|^4\right]
=(S^2-|T|^2)+2\left(Q-\frac{S^2}{q}\right).
\]
Two elementary pair identities, valid for arbitrary complex inputs, are
\[
S^2-|T|^2=\sum_{t<u}|f(t)\overline{f(u)}-\overline{f(t)}f(u)|^2,
\]
\[
Q-\frac{S^2}{q}=\frac1q\sum_{t<u}(|f(t)|^2-|f(u)|^2)^2.
\]
They prove the nonnegative sum-of-squares formula and the universal bound \(\mathcal C(F)\le3-2/q\) for APN maps.

**Every optimizer.** Equality forces equal values of \(|f(t)|\) for every \(t\), and the first sum forces \(f(t)^2\) to have one common complex argument. Unless \(f=0\), all coordinates have a common nonzero modulus, so \(f(t)=\lambda\varepsilon_t\) for arbitrary signs. Conversely those functions make both pair sums vanish. Quotienting the \(2^q\) sign patterns by their simultaneous negation gives \(2^{q-1}\) distinct complex projective classes. In particular constant coefficients attain the bound, proving its sharpness.

**Necessity of APN and quantitative separation.** For arbitrary \(F\), let \(m_{s,w}\) count unordered distinct pairs \(\{t,u\}\) with \(t+u=s\) and \(F(t)+F(u)=w\); necessarily \(s\ne0\). Every such pair contributes both orderings to a graph-sum fiber, giving the exact constant-input energy
\[
\sum_{X,Y}|\mathcal E_F1(X,Y)|^4
=3-\frac2q+\frac4{q^2}\sum_{s\ne0,w}m_{s,w}(m_{s,w}-1).
\]
Indeed the zero fiber contributes \(q^2\), while the other fibers contribute \(4\sum m_{s,w}^2\), and \(\sum_{s\ne0,w}m_{s,w}=q(q-1)/2\). If APN fails, some \(m_{s,w}\ge2\), adding at least \(8/q^2\) to the displayed moment. Since \(q^{-1}\sum_t|1|^2=1\), this is a lower bound for \(\mathcal C(F)\); it rules out equality at \(3-2/q\). Conversely, the APN case was proved sharp above.

**Nonvacuity.** The monomial \(F(t)=t^3\) is APN for every \(q=2^n\). For \(s\ne0\), the derivative is \(F(t+s)+F(t)=s^3[(t/s)^2+(t/s)+1]\). The additive polynomial \(u\mapsto u^2+u\) has kernel precisely \(\{0,1\}\), hence every derivative fiber has at most two points.

## Verification

The accompanying standard-library Python program `verify_apn.py` constructs \(\mathbb F_{2^n}\) for \(1\le n\le5\), including nonprime fields, and checks the APN derivative condition and the exact integer-valued additive-energy identity. It exhausts **all maps** on the fields of orders two and four and checks further deterministic pseudorandom maps over orders eight, sixteen, and thirty-two. For each field it verifies ten deterministic complex-coefficient vectors by both convolution and direct two-dimensional Walsh transform, including both expressions for the deficit, and tests three sign-pattern equality cases. Its numerical tolerance is used only for floating-point complex arithmetic; the all-fields theorem is proved algebraically above. Reproduce with `python3 verify_apn.py`.

## Relationship to prior work

The equivalence between APN derivatives and the Sidon property of the graph **is known** (Carlet and Picek, 2021); the older Chabaud–Vaudenay Walsh fourth-moment characterization, reviewed and extended by Carlet (2017), **already detects APN from the unweighted Walsh fourth moment**. Neither fact is presented here as new. Standard Sidon fourth-moment identities in torsion-free settings also establish the usefulness of additive-collision counting, but the exponent-two common diagonal fiber changes the complex phase structure. The object here is the *complete complex-input sharp Fourier extension problem*, including an equality classification, a global sharp deficit certificate and explicit spectral separation for non-APN graphs. The sharp finite-field extension work of González-Riquelme and Oliveira e Silva addresses odd-characteristic quadratic surfaces rather than characteristic-two APN graphs; Fraser and Rakhmonov give nonsharp \(L^2\)-restriction estimates for large Sidon sets at a different exponent. Exact novelty beyond these specific inspected statements remains subject to unindexed or earlier equivalent formulations.

## Limitations

This work does not compute \(\mathcal C(F)\) for a general non-APN map; the non-APN estimate is only a certified lower bound, not claimed optimal. It does not address extension exponents other than four, nonbinary characteristic, or quantitative distances between maps \(F\) and the APN class. The proof is self-contained; the finite checker is corroboration, not certification for arbitrarily large fields. Earlier APN moment characterizations and the APN/Sidon bridge are credited as existing work. No independent mathematical audit has been performed.

## References

1. Claude Carlet, *Characterizations of the differential uniformity of vectorial functions by the Walsh transform*, Cryptology ePrint Archive 2017/516 (2017), https://eprint.iacr.org/2017/516.
2. Claude Carlet and Stjepan Picek, *On the exponents of APN power functions and Sidon sets, sum-free sets, and Dickson polynomials*, *Advances in Mathematics of Communications*, DOI:10.3934/amc.2021064, https://doi.org/10.3934/amc.2021064.
3. Cristian González-Riquelme and Diogo Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (2024), https://arxiv.org/abs/2405.16647.
4. Jonathan M. Fraser and Firdavs Rakhmonov, *An improved \(L^2\) restriction theorem in finite fields*, arXiv:2505.09293 (2025), https://arxiv.org/abs/2505.09293.

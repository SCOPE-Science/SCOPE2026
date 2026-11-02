# A finite-to-asymptotic Jensen–Shannon reversal under experiment homogenization

## Finding
Fix \(0<t<1\) and the three-symbol alphabet \(\{A,B,C\}\). Under two alternative hypotheses define two coordinate experiments by
\[
P_1=\delta_C,\quad Q_1=(1-t)\delta_B+t\delta_C,\qquad P_2=t\delta_A+(1-t)\delta_C,\quad Q_2=\delta_A.
\]
Let \(\bar P=(P_1+P_2)/2\), \(\bar Q=(Q_1+Q_2)/2\), and, for every integer \(m\ge1\), compare the original \(2m\)-observation experiment
\[
\mathsf P_m=(P_1\otimes P_2)^{\otimes m},\quad\mathsf Q_m=(Q_1\otimes Q_2)^{\otimes m}
\]
against the homogenized experiment
\[
\overline{\mathsf P}_m=\bar P^{\otimes 2m},\quad \overline{\mathsf Q}_m=\bar Q^{\otimes 2m}.
\]
For natural-log Jensen–Shannon divergence, define \(\Delta_m(t)=\operatorname{JS}(\overline{\mathsf P}_m,\overline{\mathsf Q}_m)-\operatorname{JS}(\mathsf P_m,\mathsf Q_m)\). The exact original divergence is \((1-t^m)\log2\). At a single block,
\[
\Delta_1(t)=\frac34\log(4/3)\,t+O\!\left(t^2\log(1/t)\right)>0
\]
for all sufficiently small positive \(t\). Nevertheless, for **every** fixed \(t\in(0,1)\), \(\Delta_m(t)<0\) for every sufficiently large integer \(m\). Thus homogenization initially increases Jensen–Shannon information for suitable elementary experiments but eventually *decreases* it under repeated blocks. For the explicit choice \(t=1/10\), signs at block counts \(m=1,2,3,4\) are respectively positive, positive, negative, negative, certified by exact rational arithmetic.

## Assumptions and scope
The alphabet contains three distinguishable outcomes and the alternatives are two probability measures (a binary hypothesis). Experiments are independent across coordinates and across repeated blocks, and their coordinate labels are known in the original experiment and hidden after homogenization. Only \(t\in(0,1)\) and integer \(m\ge1\) are assumed; no common-support or positivity assumption is imposed. All logarithms are natural, \(0\log0:=0\), and
\[
\operatorname{JS}(U,V)=\tfrac12 D_{\mathrm{KL}}(U\|(U+V)/2)+\tfrac12 D_{\mathrm{KL}}(V\|(U+V)/2).
\]
The reversal concerns Jensen–Shannon divergence of full product *distributions*, not the average marginal divergence.

## Proof
**1. Exact disjoint-support overlap of the original.** Under \(\mathsf P_m\), every first-coordinate occurrence is \(C\), and each second coordinate is in \(\{A,C\}\). Under \(\mathsf Q_m\), every second-coordinate occurrence is \(A\), and each first coordinate is in \(\{B,C\}\). Exactly one full string belongs to both supports: \((C,A)\) repeated \(m\) times. Both laws assign it mass \(t^m\). On their remaining supports the laws are mutually singular. Since Jensen–Shannon information is \(\log 2\) for disjoint equal-prior observations and zero for a common equal-mass atom, direct summation gives
\[
\operatorname{JS}(\mathsf P_m,\mathsf Q_m)=(1-t^m)\log2. \tag{1}
\]

**2. Entropy defect of the homogenized experiment.** Put \(h(a,b)=(a+b)\log(a+b)-a\log a-b\log b\) for \(a,b\ge0\). For all finite distributions, \(\operatorname{JS}(U,V)=\log2-\tfrac12\sum_x h(U(x),V(x))\). The homogeneous marginals have coordinates \(\bar P=(t/2,0,1-t/2)\), \(\bar Q=(1/2,(1-t)/2,t/2)\), ordered by \((A,B,C)\). Since a word containing \(B\) has zero probability under \(\bar P\), only binary \(A/C\) words contribute to the entropy defect. Set \(n=2m\) and
\[
a_{m,k}=\binom nk(t/2)^k(1-t/2)^{n-k},\qquad b_{m,k}=\binom nk(1/2)^k(t/2)^{n-k}.
\]
For words containing exactly \(k\) letters \(A\), homogeneity of \(h\) gives the **exact finite formula**
\[
H_m(t):=\tfrac12\sum_x h(\overline{\mathsf P}_m(x),\overline{\mathsf Q}_m(x))=\tfrac12\sum_{k=0}^{2m}h(a_{m,k},b_{m,k}).\tag{2}
\]
Combining (1) and (2) yields \(\Delta_m(t)=t^m\log2-H_m(t)\).

**3. Strict short-block gain.** With \(m=1\), equation (2) reduces exactly to
\[
H_1(t)=\frac18\big[h(t^2,1)+2h(t(2-t),t)+h((2-t)^2,t^2)\big].\tag{3}
\]
The first and third summands in brackets are \(O(t^2\log(1/t))\). By homogeneity and continuity of \(h\), \(h(t(2-t),t)=t\,h(2-t,1)=t(3\log3-2\log2)+O(t^2)\). Consequently
\[
\Delta_1(t)=\left[\log2-\frac14(3\log3-2\log2)\right]t+O(t^2\log(1/t))
=\frac34\log(4/3)t+O(t^2\log(1/t)),
\]
with a strictly positive linear coefficient.

**4. Strict long-block loss.** Fix \(t\in(0,1)\). For sufficiently small fixed \(c>0\), let \(\ell_m=\lfloor cm\rfloor\), and consider the disjoint collection \(E_m\) of all homogenized words containing exactly \(m+\ell_m\) letters \(A\), exactly \(m-\ell_m\) letters \(C\), and no \(B\). Under the two homogenized alternatives, the event masses are
\[
U_m(E_m)=\binom{2m}{m+\ell_m}\frac{t^{m+\ell_m}(2-t)^{m-\ell_m}}{4^m},\qquad
V_m(E_m)=\binom{2m}{m+\ell_m}\frac{t^{m-\ell_m}}{4^m}.\tag{4}
\]
Define \(I(c)=(1+c)\log(1+c)+(1-c)\log(1-c)\). Stirling's formula gives
\[
\lim_{m\to\infty}\frac1m\log\frac{U_m(E_m)}{t^m}=-I(c)+(1-c)\log(2-t)+c\log t,\tag{5}
\]
\[
\lim_{m\to\infty}\frac1m\log\frac{V_m(E_m)}{t^m}=-I(c)-c\log t.\tag{6}
\]
At \(c=0\), the right-hand side of (5) is \(\log(2-t)>0\). The expression in (6) vanishes at zero but has derivative \(-\log t>0\), because \(I'(0)=0\). Thus a sufficiently small fixed \(c>0\) makes **both** displayed limits strictly positive, implying
\[
\min\{U_m(E_m),V_m(E_m)\}>t^m\qquad\text{for all sufficiently large }m.\tag{7}
\]
For \(a,b\ge0\), concavity of binary entropy gives \(h(a,b)\ge 2\log2\min(a,b)\). Each word in \(E_m\) has the same ratio of alternative probabilities; thus \(\sum_{x\in E_m}h(U_m(x),V_m(x))=h(U_m(E_m),V_m(E_m))\). Hence
\[
H_m(t)\ge\frac12h(U_m(E_m),V_m(E_m))\ge\log2\min\{U_m(E_m),V_m(E_m)\}>t^m\log2,
\]
and therefore \(\Delta_m(t)<0\) eventually for every fixed \(t\in(0,1)\). This completes the proof.

## Verification
The standard-library program `verify_js.py` evaluates each \(\Delta_m(1/10)\) for \(m=1,2,3,4\) using exact fractions and rigorous lower/upper bounds for logarithms. It obtains the sign sequence \((+,+,-,-)\) and numerically displays \(\Delta_1\approx0.006985730061085755\), \(\Delta_2\approx0.000216649008191337\), \(\Delta_3\approx-0.000069269281975063\), and \(\Delta_4\approx-0.000020071749851047\). The infinite-
block theorem follows analytically from (5)–(7), not from these finite computations. Run `python3 verify_js.py` using Python's standard library; recorded output is in `verification_output.txt`.

## Relationship to prior work
Kontorovich, *A local-to-global principle for f-divergence homogenization*, arXiv:2610.31164v1 (first publicly posted 2026-10-22), formulates the same averaging-versus-product operation and proves a finite-constant criterion. Its Sections 1–3 and 7 establish unit constant for relative entropy and squared Hellinger, and discuss total variation and the power-divergence family. Neither that general criterion nor its unit-constant power-divergence cases state this ternary Jensen–Shannon sign reversal or its change under fixed-block repetition. We do not claim the comparison framework or the Jensen–Shannon formula as new; the new contribution assessed here is the explicit sharp-direction witness and its rigorous eventual reverse sign. The possibility that earlier information-theory comparisons implicitly entail this behavior remains a historical-priority qualification.

## Limitations
The theorem treats this one-parameter ternary family and a fixed two-coordinate repeating block. It does not determine an optimal universal Jensen–Shannon homogenization constant, minimal alphabet, all sign-change indices, or the behavior for arbitrary experiments. The exact-rational computations certify only the listed four finite cases; they are not a substitute for the separate asymptotic argument. Independent mathematical review and historical-priority verification have not been performed.

## References
Kontorovich, Aryeh. *A local-to-global principle for f-divergence homogenization*. arXiv:2610.31164v1, 22 October 2026. https://arxiv.org/abs/2610.31164

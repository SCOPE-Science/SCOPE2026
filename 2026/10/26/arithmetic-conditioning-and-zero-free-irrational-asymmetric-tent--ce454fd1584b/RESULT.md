# Arithmetic conditioning and zero-free irrational asymmetric tent transforms

## Finding
For a triangular probability density with an interior apex at \(c\in(0,1)\), Fourier nonvanishing is equivalent to irrationality of \(c\), but near-zero Fourier conditioning records the *entire irrationality exponent* of \(c\). Write \(\widehat f_c(t)=\int_{\mathbb R}f_c(x)e^{-itx}\,dx\), and let \(\|x\|=\min_{j\in\mathbb Z}|x-j|\). Define \(E_c(t)=e^{-ict}-(1-c)-ce^{-it}\). For every integer \(k\) and every \(c\in(0,1)\), the complete Fourier frequency cell \(I_k=[2\pi k-\pi,2\pi k+\pi]\) satisfies the *parameter-uniform* bounds
\[
\frac{|1-e^{-2\pi i kc}|}{1+\pi^2/4}\le \min_{t\in I_k}|E_c(t)|\le |1-e^{-2\pi i kc}|.
\]
Consequently, for irrational \(c\), letting \(\mu(c)\in[2,\infty]\) denote its irrationality exponent,
\[
\limsup_{|t|\to\infty}\frac{-\log|\widehat f_c(t)|}{\log|t|}=\mu(c)+1.
\]
Moreover, with \(c\in(0,1)\) arbitrary,
\[
\inf_{t\in\mathbb R}(1+|t|)^3|\widehat f_c(t)|>0
\quad\Longleftrightarrow\quad c\text{ is badly approximable}.
\]
For irrational \(c\), \(\widehat f_c\) is zero-free on the whole real axis, so the translates of \(f_c\) span a dense subspace of \(L^1(\mathbb R)\). In contrast, for rational \(c=p/q\) in lowest terms, its nonzero real Fourier zeros are exactly \(t=2\pi q\ell\) with nonzero integers \(\ell\), and all have multiplicity two. This is a statement about real-frequency Fourier conditioning, not an assertion of invertibility by a bounded reciprocal Fourier multiplier.

## Assumptions and scope
Fix \(0<c<1\). The nonnegative, unit-mass, continuous compactly supported density is
\[
f_c(x)=\begin{cases}2x/c,&0\le x\le c,\\2(1-x)/(1-c),&c<x\le1,\\0,&\text{otherwise}.\end{cases}
\]
The irrationality exponent is \(\mu(c)=\sup\{\alpha\ge0: |c-p/q|<q^{-\alpha}\text{ for infinitely many }(p,q)\in\mathbb Z\times\mathbb N\}\). A real number is badly approximable exactly when \(\inf_{q\ge1}q\|qc\|>0\). The cell inequality also holds for rational \(c\) and \(k=0\), where its lower bound can equal zero. The logarithmic formula is asserted only for irrational \(c\), because rational parameters have exact real zeros.

## Proof
**1. Exact transform and zeros.** In the distributional sense,
\[
f_c''=\frac2c\delta_0-\frac2{c(1-c)}\delta_c+\frac2{1-c}\delta_1.
\]
Integrating by parts twice gives, for \(t\ne0\),
\[
\widehat f_c(t)=\frac{2}{c(1-c)t^2}\bigl(e^{-ict}-(1-c)-ce^{-it}\bigr)=\frac{2E_c(t)}{c(1-c)t^2},
\]
with removable value \(\widehat f_c(0)=1\). If \(E_c(t)=0\), then \(|(1-c)+ce^{-it}|=1\). Strict convexity of the unit disk gives \(e^{-it}=1\), hence \(t=2\pi k\); the remaining equation forces \(kc\in\mathbb Z\). This proves the exact nonzero real zero set. At such a zero, direct differentiation gives \(E'_c(t)=0\) and \(E''_c(t)=c(1-c)\ne0\); thus the Fourier zero is exactly double.

**2. The universal full-cell inequality.** Fix \(k\in\mathbb Z\), write \(t=2\pi k+u\) with \(|u|\le\pi\), and put \(r=|E_c(t)|\) and \(P=(1-c)+ce^{-iu}\). We have \(1-|P|\le r\), and therefore
\[
4c(1-c)\sin^2(u/2)=1-|P|^2\le 2r.
\]
Since \(2|\sin(u/2)|\ge 2|u|/\pi\) in this interval,
\[
c(1-c)u^2\le\frac{\pi^2}{2}r.
\]
The centered expression \(e^{icu}P=(1-c)e^{icu}+ce^{-i(1-c)u}\) has no linear term. The elementary integral Taylor remainder \(|e^{iv}-1-iv|\le v^2/2\) for real \(v\) yields
\[
|e^{icu}P-1|\le \frac{c(1-c)}2u^2\le\frac{\pi^2}{4}r.
\]
But \(r=|e^{-2\pi i kc}-e^{icu}P|\). By the triangle inequality,
\[
|1-e^{-2\pi i kc}|\le(1+\pi^2/4)r.
\]
Taking the minimum in the cell proves the lower bound. Setting \(u=0\) proves the upper bound, with no asymptotic or irrationality assumption. Both ends of every cell have been included.

**3. Diophantine exponent and weighted lower bound.** For any \(k\),
\[
4\|kc\|\le |1-e^{-2\pi i kc}|\le2\pi\|kc\|.
\]
For \(|k|\ge1\), uniformly over \(t\in I_k\), \(|t|\) is comparable with \(|k|\) as \(|k|\to\infty\). Hence the cell estimate identifies the minimum of \(|t|^2|\widehat f_c(t)|\) with \(\|kc\|\), up to constants depending only on \(c\). For irrational \(c\), the elementary identity
\[
\mu(c)=1+\limsup_{k\to\infty}\frac{-\log\|kc\|}{\log k}
\]
now proves the claimed logarithmic limsup, including the case \(\mu(c)=\infty\). Indeed, the lower cell bound controls all frequencies and cell centers attain the reverse exponent inequality. Equivalently, the weighted infimum outside a compact set is positive exactly when \(\inf_{k\ge1}k\|kc\|>0\). On a compact frequency set, \(\widehat f_c\) has a positive modulus minimum for irrational \(c\). Rational \(c\) has exact zeros and cannot meet the weighted condition. These observations prove the stated equivalence.

**4. Translation cyclicity.** Wiener's classical \(L^1\) Tauberian theorem characterizes density of complex linear combinations of translates by absence of real Fourier zeros. Apply the zero classification in Step 1. This does not imply uniform lower bounds on arbitrary irrational parameters; Steps 2–3 quantify exactly why.

## Verification
The standalone `checks/check.py` recomputes the Fourier integral symbolically and compares direct numerical quadratures against the closed formula at 15 parameter-frequency pairs. It tests the full-cell inequality for 45 parameter-cell pairs and the rational double-zero Taylor coefficient at nine sampled sites. Its recorded successful execution is in `checks/check-output.txt`. These finite checks are regression tests; they do not replace the global proofs, the irrationality-exponent identity, or Wiener's theorem.

## Relationship to prior work
Dimitrov and Xu discuss Wiener's translation theorem and the familiar *symmetric* tent kernel with the squared-sinc Fourier transform, which has many real zeros. Their Proposition 2.15 and Section 4 concern that symmetric tent and associated Wronskians, not the arithmetic conditioning of the asymmetric triangular family. The published CharFun implementation explicitly gives the triangular distribution's three-exponential characteristic function (equivalent to Step 1, subject to its sign convention); its formula is **prior art**, not a novel ingredient. Neither source establishes the parameter-uniform full-cell estimate or the consequent exact Diophantine conditioning exponent and badly-approximable criterion. The real-zero classification is an easy geometric consequence of the known transform formula, and is included for completeness, not independently claimed as significant novelty.

## Limitations
The universal constant \(1+\pi^2/4\) is a proved, not claimed optimal, comparison constant. The theorem controls the real axis and polynomial near-zero rates; it does not classify non-real zeros or give stable deconvolution by a bounded Fourier multiplier. The Diophantine exponent statement is a limiting order, not a finite-frequency uniform bound for general irrational \(c\). Unindexed older work on asymmetric hat splines or Diophantine small divisors may contain equivalent inequalities; no independent audit of novelty has been performed.

## References
1. D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace Transforms*, arXiv:1606.05011v1, first public 16 June 2016. Especially Proposition 2.15 and Section 4. https://arxiv.org/pdf/1606.05011
2. *CharFun*, `cfX_Triangular.R`, triangular distribution characteristic-function source code, documentation built 2 May 2019. https://rdrr.io/cran/CharFun/src/R/cfX_Triangular.R
3. N. Wiener, *Tauberian Theorems*, Annals of Mathematics 33 (1932), 1–100; cited and used in Reference 1. The classical theorem is invoked, not re-proved.

# Singular-drift height and sharp quasi-mixing scale for a translated Boole map

## Finding
For the parabolic rational inner map \(T_\beta(z)=z+\beta-1/z\) on the upper half-plane, let \(b_\infty(\beta)=\lim_{n\to\infty}\operatorname{Im}T_\beta^n(i)\), for \(0<\beta\le1/4\). Then the singular, drift-to-zero height satisfies the **explicit uniform bound**
\[
\left|\beta b_\infty(\beta)-\pi\right|\le \frac{\beta^3}{3}+2\beta^2\log\frac{4\pi}{\beta}.
\]
In particular \(\lim_{\beta\downarrow0}\beta b_\infty(\beta)=\pi\). For the transfer-operator normalizer \(u_n(\beta)=\operatorname{Im}T_\beta^n(i)/(\pi|T_\beta^n(i)|^2)\),
\[
\lim_{n\to\infty}n^2\beta^3u_n(\beta)=\frac{\beta b_\infty(\beta)}\pi,
\qquad
\lim_{\beta\downarrow0}\lim_{n\to\infty}n^2\beta^3u_n(\beta)=1.
\]
Thus the fixed-positive-drift inverse-square quasi-mixing normalizer has the exact singular prefactor \(1/(\beta^3 n^2)\) as the drift vanishes. The unshifted map instead has the inverse-square-root mixing normalizer \(1/(\pi\sqrt{2n})\), so this is a nonuniform transition in both exponent and amplitude.

## Assumptions and scope
The complex upper half-plane is \(\mathbb H=\{z:\operatorname{Im}z>0\}\). Fix real \(0<\beta\le1/4\); all iterates start from \(i\), with the iteration count tending to infinity *before* \(\beta\downarrow0\). The map \(T_\beta\) preserves \(\mathbb H\). The normalizer is based on the Poisson kernel evaluated at zero, as defined above. No claim is made about uniformity as iteration count and drift tend to their limits simultaneously.

## Proof
Put \(h=\beta^2\), \(w_n=\beta T_\beta^n(i)=x_n+i y_n\), and \(t_n=h/|w_n|^2\). Direct substitution gives
\[
 w_{n+1}=w_n+h-\frac{h}{w_n},\qquad
 x_{n+1}=(1-t_n)x_n+h,\qquad y_{n+1}=(1+t_n)y_n.
\]
Since \(x_0=0\) and \(y_0=\beta\), induction shows \(y_n\ge\beta\), \(0<t_n\le1\), and \(x_n\ge0\). On \(\mathbb H\) use the principal logarithm and define \(F(w)=w+\log(w-1)\). Because
\[
 w_{n+1}-1=(w_n-1)(1+h/w_n)
\]
and \(|h/w_n|\le\beta\le1/4\), the principal arguments change without a branch crossing, so exactly
\[
 F(w_{n+1})-F(w_n)=h+E_n,\qquad
 E_n=\log(1+h/w_n)-h/w_n.
\]
The standard power-series remainder bound for \(|a|\le1/4\) gives \(|\log(1+a)-a|\le |a|^2\). Hence
\[
 \left|\sum_{k=0}^{n-1}\operatorname{Im}E_k\right|
 \le h\sum_{k=0}^{n-1}t_k
 \le2h\sum_{k=0}^{n-1}\log(1+t_k)
 =2h\log\frac{y_n}{\beta},
\]
where \(t\le2\log(1+t)\) for \(0\le t\le1\). Moreover \(\operatorname{Im}F(w_0)=\pi+\beta-\arctan\beta\), and \(0\le\beta-\arctan\beta\le\beta^3/3\). Since \(0<\arg(w_n-1)<\pi\), it follows for every \(n\) that
\[
 y_n\le\pi+\frac{\beta^3}{3}+2\beta^2\log\frac{y_n}{\beta}.
\]
The bound \(y_n\le4\pi\) follows inductively. It holds at \(n=0\). If it holds at \(n\), then \(y_{n+1}\le2y_n\le8\pi\), so the last displayed inequality yields \(y_{n+1}\le\pi+\beta^3/3+2\beta^2\log(8\pi/\beta)<4\pi\) for \(0<\beta\le1/4\). Thus \(y_n\uparrow y_\infty\le4\pi\).

In fact \(x_n\to+\infty\). Otherwise some finite \(M\) would bound \(x_n\) for infinitely many \(n\); on those indices \(y_{n+1}-y_n=y_n h/(x_n^2+y_n^2)\ge\beta h/(M^2+16\pi^2)>0\), contrary to convergence of \(y_n\). Consequently \(\arg(w_n-1)\to0\) and \(\operatorname{Im}F(w_n)\to y_\infty\). Passing to the limit in the preceding telescoping estimate proves
\[
 |y_\infty-\pi|\le\beta^3/3+2\beta^2\log(4\pi/\beta).
\]
By definition \(y_\infty=\beta b_\infty(\beta)\). Also \(x_{n+1}-x_n=h-hx_n/(x_n^2+y_n^2)\to h\), so Cesàro averaging gives \(x_n/n\to h\). Substitution in the exact Poisson normalizer yields \(n^2\beta^3u_n(\beta)\to y_\infty/\pi\), proving the stated limits.

## Verification
The proof gives a rigorous all-iterate height bound and an explicit error estimate; no infinite conclusion is inferred from finite simulation. The independent stand-alone `verify.py` supplied with this result checks the algebraic one-step identity, the logarithm telescoping formula, monotone heights and several finite-drift numerical enclosures. It is a diagnostic, not a substitute for the proof. Execute `python3 verify.py` in the directory containing that file.

## Relationship to prior work
Aaronson, *Dual mixing and quasi-mixing of inner function restrictions*, Proposition 3.1, supplies for **fixed** nonzero drift the existence of \(b_\infty\) and the inverse-square singular dual quasi-mixing normalization, and for zero drift the inverse-square-root mixing normalization. Those facts are prior work. The additional statement here is the explicit singular parameter asymptotic \(\beta b_\infty(\beta)\to\pi\), its quantitative all-small-drift bound, and the resulting exact \(\beta^{-3}\) prefactor in the iterated normalization limit. The source proposition alone, with an unspecified drift-dependent \(b_\infty\), does not determine this constant. Related work of Arizmendi, Salazar and Wang concerns parabolic central-limit/return sequences, while Ivrii treats simply parabolic inner-function dynamics; neither accessible comparison explicitly supplies this vanishing-drift height law. The complete Ivrii article was not available for direct comparison, leaving a priority uncertainty.

## Limitations
The order of limits is essential; no joint scaling theorem is asserted. The bound \(O(\beta^2\log(1/\beta))\) is sufficient for the sharp leading constant and is not claimed to be an optimal error rate. The finding concerns the single-pole translated Boole family, not every finite-measure parabolic inner map. An equivalent parameter limit in older parabolic-iteration literature cannot be ruled out without further priority review. No independent audit has been performed.

## References
1. J. Aaronson, *Dual mixing and quasi-mixing of inner function restrictions*, arXiv:2609.00217, first posted 2026-08-31, Proposition 3.1 and Section 1.
2. O. Ivrii, *Dynamics of simply parabolic inner functions*, arXiv:2606.19260 (2026); abstract accessible, complete text not inspected.
3. O. Arizmendi, M. Salazar and J.-C. Wang, *Berry–Esseen type estimate and return sequence for parabolic iteration in the upper half-plane*, arXiv:1811.12545; IMRN 2021.
4. Ch. Pommerenke, *On the iteration of analytic functions in a halfplane*, J. London Math. Soc. (1979), as cited in Aaronson.

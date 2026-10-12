# Order-six reversal of the generalized-key two-periodic bifurcation
## Finding
For the four-state hard-core model with the fertile graph of generalized-key type on a Cayley tree of integer order \(k\ge 4\), consider the invariant two-periodic branch \(I_2\) studied by Khakimov and Tozhiboev. Every non-translation-invariant positive solution on this branch is parameterized, up to swapping the two parity classes, by a unique \(s>0\). Define
\[
a_k(s)=\frac{\sinh((k-1)s)}{\sinh s},\qquad
b_k(s)=\frac{\sinh(ks)}{\sinh s},\qquad
c_k(s)=\frac{\sinh((k+1)s)}{\sinh s},
\]
and
\[
g_k(s)=b_k(s)a_k(s)^{1/k}-c_k(s).
\]
There is a unique \(s_k>0\) with \(g_k(s)>0\) exactly for \(0<s<s_k\). On this interval the activity is
\[
\Lambda_k(s)=\frac{a_k(s)^k}{b_k(s)^k g_k(s)}.
\]
The branch meets the translation-invariant locus at
\[
\lambda_c(k)=\frac{(k-1)^k}{k^k\bigl(k(k-1)^{1/k}-(k+1)\bigr)}.
\]
Its local orientation is
\[
\log\frac{\Lambda_k(s)}{\lambda_c(k)}=B_k s^2+O(s^4),
\quad
B_k=\frac{k(k+1)\bigl(3k+1-3(k-1)^{1+1/k}\bigr)}{6\bigl(k(k-1)^{1/k}-(k+1)\bigr)}.
\]
Here \(B_4>0\) and \(B_5>0\), whereas \(B_k<0\) for every \(k\ge6\). Therefore the generalized-key branch changes from the source's supercritical orientation at \(k=4\) to a subcritical orientation beginning sharply at \(k=6\). For every \(k\ge6\), defining \(\lambda_{\min}(k)=\min_{0\le s<s_k}\Lambda_k(s)\) using the continuous value at \(s=0\), one has \(\lambda_{\min}(k)<\lambda_c(k)\), and every \(\lambda\in(\lambda_{\min}(k),\lambda_c(k))\) yields at least four distinct non-translation-invariant positive \(I_2\) boundary laws and hence at least four non-translation-invariant two-periodic splitting Gibbs measures.

## Assumptions and scope
The spin set is \(\{0,1,2,3}\), all occupied activities are the common value \(\lambda>0\), and the compatibility graph is the source's generalized-key fertile graph. The Cayley tree has order \(k\ge4\), meaning degree \(k+1\). Only the invariant set \(I_2\) of the source's two-periodic equations is classified here. The phrase “at least four” is intentional: other invariant sets or additional solutions at the same activity are not excluded.

## Proof
The source's equations on \(I_2\) are
\[
z_0=\lambda\left(\frac{z_0+z_2}{z_2}\right)^k,\quad
z_1=\lambda\left(\frac{z_1+z_2}{z_2}\right)^k,\quad
z_2=\lambda\left(\frac{z_0+z_1+z_2+1}{z_2}\right)^k.
\]
For a non-translation-invariant positive solution let \(t=(z_0/z_1)^{1/k}\ne1\). Taking the positive \(k\)-th root of the quotient of the first two equations gives
\[
t(z_1+z_2)=z_0+z_2.
\]
With
\[
A(t)=\sum_{j=1}^{k-1}t^j,\quad B(t)=\sum_{j=0}^{k-1}t^j,\quad C(t)=\sum_{j=0}^k t^j,
\]
one obtains
\[
z_0=\frac{t^k}{G(t)},\qquad z_1=\frac{1}{G(t)},\qquad z_2=\frac{A(t)}{G(t)},
\]
where
\[
G(t)=B(t)A(t)^{1/k}-C(t),\qquad
\lambda(t)=\frac{A(t)^k}{B(t)^kG(t)}.
\]
Conversely, direct substitution shows that these formulas solve all three equations whenever \(G(t)>0\), so the parameterization is exhaustive on \(I_2\). Also \(G(1/t)=t^{-k}G(t)\), so replacing \(t\) by \(1/t\) swaps \(z_0,z_1\), leaves \(z_2\) fixed, and preserves \(\lambda\).

Put \(t=e^{2s}\) with \(s>0\). Factoring the geometric sums gives \(G(t)=e^{ks}g_k(s)\), and positivity is equivalent to
\[
\Phi_k(s)=\log a_k(s)-k\log\frac{c_k(s)}{b_k(s)}>0.
\]
At the origin,
\[
\Phi_k(0)=\log(k-1)-k\log\frac{k+1}k>0
\]
for \(k\ge4\), because \((1+1/k)^k<e<3\le k-1\). As \(s\to\infty\), \(\Phi_k(s)=-2s+O(1)\), so \(\Phi_k(s)\to-\infty\).

For fixed \(s>0\), set \(H_s(u)=u\coth(us)\). Then
\[
H_s''(u)=2s\,\operatorname{csch}^2(us)\bigl(us\coth(us)-1\bigr)>0.
\]
Thus the forward differences of \(H_s\) are strictly increasing, and
\[
\Phi_k'(s)=H_s(k-1)-H_s(1)-k\bigl(H_s(k+1)-H_s(k)\bigr)<0.
\]
Hence \(\Phi_k\) has exactly one positive zero \(s_k\), proving the precise positivity interval. Since \(g_k(s)\downarrow0\) at \(s_k\), while \(a_k,b_k\) remain positive and finite, \(\Lambda_k(s)\to+\infty\) as \(s\uparrow s_k\).

Expanding \(\sinh(ns)/\sinh s=n\bigl(1+(n^2-1)s^2/6+O(s^4)\bigr)\) gives the stated \(\lambda_c(k)\) and \(B_k\). The denominator of \(B_k\) is positive for \(k\ge4\). Its numerator is positive at \(k=4,5\). For \(k\ge6\), it is negative because
\[
(k-1)^{1/k}>1+\frac{4}{3(k-1)}.
\]
Indeed, \(\log(k-1)>4k/(3(k-1))\) at \(k=6\), and the difference of the two sides is strictly increasing for real \(k\ge6\), while \(\log(1+x)<x\) gives the displayed inequality. Thus \(B_k<0\) exactly from \(k=6\) onward.

For \(k\ge6\), \(\Lambda_k(s)<\lambda_c(k)\) for all sufficiently small positive \(s\), but \(\Lambda_k(s)\to+\infty\) at the other endpoint. Continuity therefore gives a global minimum \(\lambda_{\min}(k)<\lambda_c(k)\). For each level strictly between these two values, the intermediate value theorem supplies at least two distinct positive \(s\)-values, one on each side of a minimizer. Each has a distinct parity-swapped partner, giving at least four non-translation-invariant boundary laws.

## Verification
The accompanying `verify.py` independently evaluates the simplified boundary laws in the three source equations for multiple orders and parameters, checks the reciprocal swap, verifies the sign change of \(B_k\), numerically confirms the unique positivity endpoint, and tests the second-order expansion. These finite calculations are corroborative; the proof above is analytic and applies to every integer \(k\ge4\).

For orientation, \(\lambda_c(4)=1.197166010741\ldots\), agreeing with the source's exact \(k=4\) value. At \(k=6\), \(\lambda_c(6)=0.395877845610\ldots\) while the branch numerically reaches about \(0.365260811906\), illustrating the subcritical fold without using that numerical minimum in the theorem.

## Relationship to prior work
Khakimov and Tozhiboev derive the general parameter \(t\) and formula (15), then prove their periodic classification only for \(k=2,3,4\). Their theorem gives the exact \(k=4\) threshold and the two non-translation-invariant solutions above it. The present result uses their general equation as the starting point but analyzes its previously untreated higher-order structure: a unique positive domain for every \(k\ge4\), an exact all-order merger activity, and the qualitative reversal at \(k=6\).

The earlier four-state work cited by the source concerns translation-invariant measures at lower orders, not this higher-order two-periodic generalized-key branch. A later paper by the same authors studies the different fertile graph called “key,” not the “generalized key” graph, and therefore does not imply the present statement.

## Limitations
This is an \(I_2\)-branch result, not a classification of all solutions of the six-variable periodic system. For \(k\ge6\), the argument proves at least four non-translation-invariant measures in \((\lambda_{\min},\lambda_c)\); it does not prove that four is the exact count, does not prove uniqueness of the minimizer, and does not address extremality, reconstruction, stability, or thermodynamic dominance. No assertion is made about the complete Gibbs-measure simplex.

## References
1. R. M. Khakimov and B. Z. Tozhiboev, “Gibbs measures for fertile models with hard-core interactions and four states,” *Theoretical and Mathematical Physics* 219 (2024), 823–838. DOI: 10.1134/S0040577924050106; Russian DOI: 10.4213/tmf10608.
2. R. M. Khakimov, “Gibbs measures for fertile hard-core models on the Cayley tree,” *Theoretical and Mathematical Physics* 186 (2016), 294–305. DOI: 10.1134/S0040577916020136.
3. B. Z. Tozhiboev and R. M. Khakimov, “Gibbs measures for the HC-model in the case of a graph of type ‘key’ on a Cayley tree,” *Mathematical Notes* 117 (2025), 629–642. DOI: 10.1134/S0001434625030289.

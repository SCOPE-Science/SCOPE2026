# Sharp discrete concavity index for integer-shape Yule–Simon laws

## Finding
For every integer shape parameter \(\rho\ge1\), consider the Yule–Simon probability mass function
\[p_\rho(k)=\frac{\rho\,\rho!}{k(k+1)\cdots(k+\rho)},\qquad k=1,2,\ldots.\]
Define \(a_\rho>0\) as the unique positive solution of
\[\left(\frac{\rho+3}{2}\right)^{a_\rho}+(\rho+2)^{-a_\rho}=2.\]
Then \(p_\rho\) is discrete \(\alpha\)-concave **if and only if** \(\alpha\le-a_\rho\). At the critical parameter \(\alpha=-a_\rho\), the local concavity inequality is an equality at the triple \(k=1,2,3\) and is strict at every later interior triple centered at \(k\ge3\). Moreover, writing
\[b_\rho=\frac{\sum_{j=1}^{\rho+1}j^{-2}}{\bigl(\sum_{j=1}^{\rho+1}j^{-1}\bigr)^2},\]
we have the strict comparison
\[\frac{1}{\rho+1}<a_\rho<b_\rho.\]
For \(\rho=1\), the exact root is approximately \(a_1=0.523305268852764\), improving the previously sufficient index \(b_1=5/9\). These statements classify the largest admissible concavity index, rather than just producing another sufficient parameter.

## Assumptions and scope
The shape parameter \(\rho\) is a **positive integer**, and the support is \(\{1,2,\ldots\}\). Following the discrete power-mean convention, for \(\alpha<0\) a positive contiguous-support mass sequence \(p\) is \(\alpha\)-concave when \(p(k)^\alpha\) is convex as a sequence at every interior index \(k\ge2\), i.e.
\[p(k-1)^\alpha+p(k+1)^\alpha\ge2p(k)^\alpha.\]
At the left boundary the adjacent zero imposes no additional restriction under the standard zero-value convention. For \(\alpha=0\) this is usual log-concavity. Larger \(\alpha\) impose stronger power-mean inequalities. All conclusions are exact and hold for all integers \(k\ge2\), with no finite cutoff assumption. General noninteger shapes are not covered.

## Proof
**1. Reduction and the first triple.** Fix integer \(\rho\ge1\), put \(m=\rho+1\), and define for real \(x>0\)
\[g(x)=\sum_{j=0}^{\rho}\log(x+j),\qquad h_a(x)=\exp(a g(x)),\qquad a>0.\]
Up to a positive constant, \(p_\rho(k)^{-a}=h_a(k)\). Thus discrete \((-a)\)-concavity is equivalent to
\[h_a(k-1)-2h_a(k)+h_a(k+1)\ge0\qquad(k\ge2).\]
The product telescoping gives
\[\frac{h_a(k+1)}{h_a(k)}=\left(\frac{k+\rho+1}{k}\right)^a,\quad \frac{h_a(k-1)}{h_a(k)}=\left(\frac{k-1}{k+\rho}\right)^a.\]
Consequently the \(k=2\) condition is \(F_\rho(a)\ge0\), with
\[F_\rho(a)=\left(\frac{\rho+3}{2}\right)^a+(\rho+2)^{-a}-2.\]
Here \(F_\rho(0)=0\), \(F_\rho'(0)=\log((\rho+3)/2)-\log(\rho+2)<0\), \(F_\rho''(a)>0\), and \(F_\rho(a)\to+\infty\). Therefore it has exactly one positive zero \(a_\rho\); for positive \(a\), the first-triple condition holds precisely when \(a\ge a_\rho\).

**2. A one-turn principle for lattice slopes.** Write
\[w(x)=g'(x)=\sum_{j=0}^{\rho}\frac1{x+j}>0,\qquad f(x)=-\frac{g''(x)}{g'(x)^2}.\]
For \(S_r(x)=\sum_{j=0}^{\rho}(x+j)^{-r}\), one has \(f=S_2/S_1^2\) and
\[f'(x)=\frac{2(S_2(x)^2-S_1(x)S_3(x))}{S_1(x)^3}<0.\]
The strict inequality follows from Cauchy–Schwarz, because the \(\rho+1\ge2\) positive numbers \((x+j)^{-1}\) are not all equal.

Define the continuous secant slope \(B_a(x)=h_a(x+1)-h_a(x)\), \(x\ge1\), and the auxiliary ratio
\[R(x)=\frac{\log(w(x)/w(x+1))}{g(x+1)-g(x)}=\frac{\int_x^{x+1}f(t)w(t)\,dt}{\int_x^{x+1}w(t)\,dt}.\]
As a positive-weight average of strictly decreasing \(f\), it satisfies \(f(x+1)<R(x)<f(x)\). Differentiating the two integrals with moving endpoints gives
\[R'(x)=\frac{w(x+1)[f(x+1)-R(x)]-w(x)[f(x)-R(x)]}{\int_x^{x+1}w(t)\,dt}<0.\]
Since \(h'_a(x)=a h_a(x)w(x)\),
\[\log\frac{h'_a(x+1)}{h'_a(x)}=\bigl(g(x+1)-g(x)\bigr)(a-R(x)).\]
Thus the sign of \(B_a'(x)=h'_a(x+1)-h'_a(x)\) is the sign of \(a-R(x)\), which can change **at most once**, and only from negative to positive, as \(x\) increases. Hence every \(B_a\) first decreases and then increases (with either phase possibly absent).

If \(a\ge a_\rho\), then \(B_a(2)\ge B_a(1)\) by step 1. As \(B_a'\) has only a negative-to-positive sign change, this forces \(a>R(2)\); otherwise \(B_a\) would be strictly decreasing throughout \([1,2]\). Since \(R\) is strictly decreasing, \(B_a'(x)>0\) for all \(x\ge2\). Therefore for every integer \(k\ge3\),
\[h_a(k-1)-2h_a(k)+h_a(k+1)=B_a(k)-B_a(k-1)>0.\]
Together with the \(k=2\) inequality, this proves sufficiency for all \(a\ge a_\rho\); necessity follows already from the first triple.

**3. Bounds and maximality over all real \(\alpha\).** Direct differentiation gives
\[h_a''(x)=h_a(x)g'(x)^2(a^2-a f(x))=a h_a(x)g'(x)^2(a-f(x)).\]
Cauchy–Schwarz also implies \(f(x)>1/(\rho+1)\) for finite \(x\ge1\). At \(a=1/(\rho+1)\), \(h_a''(x)<0\) on \([1,3]\), so \(F_\rho(a)<0\) and \(a_\rho>1/(\rho+1)\). Conversely \(b_\rho=f(1)\), and strict decrease of \(f\) implies \(h_{b_\rho}''(x)>0\) for \(x>1\); hence \(F_\rho(b_\rho)>0\) and \(a_\rho<b_\rho\).

Finally \(p_\rho\) is strictly log-convex: its adjacent successive ratios \(k/(k+\rho+1)\) strictly increase in \(k\). It is therefore neither log-concave nor \(\alpha\)-concave for \(\alpha\ge0\), since positive-order power means dominate the geometric mean. All admissible values are exactly \(\alpha\le-a_\rho\). This completes the proof.

## Verification
The companion `verify_yule_simon.py` evaluates the unique first-triple root by bisection without using a fitting model; it tests the strict bounds against the previously sufficient curvature parameter, all interior normalized second differences through index \(349\) for shapes \(1\) through \(16\), and the decreasing continuous curvature at sample points. The standalone program reported **6,049 passing numerical assertions**. Those finite tests are only cross-checks: the derivative and one-turn argument above proves the infinite classification. Run with `python verify_yule_simon.py` using Python 3 and its standard library.

## Relationship to prior work
Alqasem, Aravinda and Marsiglietti, *Majorization, Entropy and Concentration Inequalities for Discrete \(\alpha\)-Concave Random Variables*, arXiv:2610.05439v1 (first submitted October 4, 2026), Definition 1.1 and Example 1.2(3), exhibit the **sufficient**, continuous-curvature index \(\alpha=-b_\rho\) for integer-shape Yule–Simon laws. Their Theorems 1.3–1.5 develop related concentration and entropy consequences. The present claim sharpens only the **membership index** by giving the exact largest \(\alpha\); it does not assert originality for the definition, Yule–Simon law, or general inequalities. The strict gap \(a_\rho<b_\rho\) shows that the known sufficient parameter does not already entail the optimal boundary. Standard gamma-ratio identities and Cauchy–Schwarz are credited as common tools. The literature comparison and remaining priority risks are recorded separately in `REVIEW.md` and `AUDIT.json`.

## Limitations
The proof requires integer \(\rho\ge1\), so the logarithmic product has finitely many equally spaced factors. No exact threshold is claimed for noninteger Yule–Simon shape, finite truncations, or other beta-ratio families. The result classifies membership, not optimal coefficients in downstream variance or entropy inequalities. A broader published theorem about convexity of powers of rising factorials could subsume this special instance; independent priority review remains necessary.

## References
1. A. Alqasem, H. Aravinda and A. Marsiglietti, *Majorization, Entropy and Concentration Inequalities for Discrete \(\alpha\)-Concave Random Variables*, arXiv:2610.05439v1 (October 4, 2026), Definition 1.1, Example 1.2, Theorem 1.3.
2. Classical Yule–Simon mass function, \(p_\rho(k)=\rho B(k,\rho+1)\). See the probability-law reference in the original paper and the standard beta/gamma representation.

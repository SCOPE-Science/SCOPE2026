# Sharp total-variation approximation to uniformity by two three-sided dice

## Finding
Let \(p=(a,b,c)\) and \(q=(d,e,f)\) be arbitrary probability vectors on \(\{0,1,2\}\), and let \(r=p*q\) be their five-coordinate ordinary convolution. Put \(u=(1/5,1/5,1/5,1/5,1/5)\). Then
\[
\boxed{\min_{p,q\in\Delta_2}\|p*q-u\|_1=\frac15,\qquad
\min_{p,q\in\Delta_2}d_{\mathrm{TV}}(p*q,u)=\frac1{10}.}
\]
Furthermore, equality holds **if and only if**, up to interchanging the two factors,
\[
\boxed{p=(\tfrac12,0,\tfrac12),\qquad
q=(s,\tfrac25,\tfrac35-s),\quad \tfrac15\le s\le\tfrac25.}
\]
This establishes the three-sided case of the proposed \(n\)-by-\(n\) Manhattan-distance lower bound of Metya and Mukherjee (Conjecture 4.7, 2026) and proves completeness of their proposed equality family in this case.

## Assumptions and scope
The two random variables are independent, each takes values in \(\{0,1,2\}\), and its three probabilities are nonnegative and sum to one. Zero probabilities are allowed. Ordinary (noncyclic) convolution is used. The norm is the sum of the five absolute coordinate differences; total variation is half that norm. The statement does not assert anything for four-sided or larger dice, other metrics, or dependent variables.

Write
\[
(r_0,r_1,r_2,r_3,r_4)=(ad,\ ae+bd,\ af+be+cd,\ bf+ce,\ cf).
\]
For an arbitrary probability vector \(r\), let
\[
\delta=\frac12\sum_{j=0}^{4}|r_j-\tfrac15|.
\]
We will show \(\delta\ge 1/10\) and characterize equality.

## Proof
**1. A necessary convolution inequality.** Direct expansion yields the polynomial identity
\[
\begin{aligned}
r_1r_2r_3-r_4r_1^2-r_0r_3^2
={}&be\big[(af-cd)^2+abef+ace^2+b^2df+bcde\big]\ge0.
\end{aligned}
\tag{1}
\]
Every summand in the bracket is nonnegative. When \(r_0,r_4>0\), we have \(a,c,d,f>0\), so equality in (1) forces \(be=0\): if both \(b,e>0\), the term \(ace^2\) makes the right side strictly positive.

**2. An elementary total-variation dual bound.** For any five real numbers \(h_j\), write \(h_{\min}=\min_j h_j\) and \(h_{\max}=\max_j h_j\). Since the positive deviations of \(r\) from \(u\) sum to \(\delta\), as do the absolute negative deviations,
\[
\sum_{j=0}^4h_jr_j\ge\frac15\sum_{j=0}^4h_j-\delta(h_{\max}-h_{\min}).
\tag{2}
\]
Equality in (2), when \(\delta>0\), requires every coordinate with positive deviation to attain \(h_{\min}\) and every coordinate with negative deviation to attain \(h_{\max}\).

**3. The lower bound.** Suppose, for contradiction, \(\delta<1/10\). Each \(r_j\ge1/5-\delta>1/10\); hence \(r_1,r_3>0\). Reversing both factors, which replaces \(r_j\) with \(r_{4-j}\), if necessary, arrange
\[
t=\frac{r_1}{r_3}\ge1.
\]
Dividing (1) by \(r_1r_3\) gives
\[
D:=\frac{r_0}{t}-r_2+t r_4\le0.
\tag{3}
\]

For \(1\le t\le2\), select
\[
(h_0,h_1,h_2,h_3,h_4)
=\left(\frac1t,\frac{t-2}{2t},-1,\frac{2-t}{2},t\right).
\]
Here \(h_1r_1+h_3r_3=0\), \(h_{\min}=-1\), \(h_{\max}=t\), and \(\sum h_j=(t+1)/2\). Consequently (2) implies
\[
D\ge\frac{t+1}{10}-\delta(t+1)>0,
\]
contradicting (3).

For \(t\ge2\), select \(h=(1/t,0,-1,0,t)\). Again \(\sum h_jr_j=D\), with minimum \(-1\) and maximum \(t\). Therefore
\[
\begin{aligned}
D&\ge\frac{t+t^{-1}-1}{5}-\delta(t+1)\\
&>\frac{t+t^{-1}-1}{5}-\frac{t+1}{10}
=\frac{(t-1)(t-2)}{10t}\ge0,
\end{aligned}
\]
again contradicting (3). Thus \(\delta\ge1/10\), equivalently \(\|r-u\|_1\ge1/5\).

**4. Complete equality classification.** Now suppose \(\delta=1/10\). Each \(r_j\ge1/10>0\), so the preceding construction applies with \(t\ge1\) after possible simultaneous reversal. If \(t>2\), the second displayed bound for \(D\) is strictly positive, contradicting (3). If \(1<t\le2\), the first bound gives \(D\ge0\); equality with (3) must hold. For \(t>1\), the maximum \(h_j=t\) is attained only at index \(4\), and the minimum \(-1\) only at index \(2\). The equality condition in (2) then requires \(r_1=r_3=1/5\), contradicting \(t>1\). We conclude \(t=1\) and hence \(r_1=r_3\).

At \(t=1\), the first dual vector becomes \(h=(1,0,-1,0,1)\). Its minimum is attained only at index \(2\), and its maximum precisely at indices \(0,4\). Equality in (2) forces
\[
r_1=r_3=\frac15,\qquad r_2=\frac3{10},\qquad
r_0+r_4=\frac3{10},\quad r_0,r_4\in[\tfrac1{10},\tfrac15].
\tag{4}
\]
Since (3) is also equality, (1) is equality; as \(r_0,r_4>0\), this forces \(be=0\). After possibly interchanging factors, let \(b=0\). Now \(r_1=ae=1/5\) and \(r_3=ce=1/5\), so \(a=c=1/2\) by \(a+c=1\), and \(e=2/5\). Writing \(s=d\), equation (4) gives \(s=2r_0\in[1/5,2/5]\), and \(f=3/5-s\). Thus the displayed family is necessary, including its endpoints and all factor swaps.

**5. Attainment.** For every \(s\in[1/5,2/5]\), the displayed factors are probabilities, and
\[
p*q=(s/2,\ 1/5,\ 3/10,\ 1/5,\ (3/5-s)/2).
\]
Their only deviations from \(u\) are a total deficit \(1/10\) at indices \(0,4\) and a surplus \(1/10\) at index \(2\), giving \(\|p*q-u\|_1=1/5\). This completes sharpness and uniqueness.

## Verification
A standard-library exact-rational verifier is supplied as `checker.py`. Its 4096-point integer Cartesian test proves identity (1) by polynomial interpolation: each side has degree at most three in each of the six variables, and four distinct test values per variable determine such a polynomial. The program also verifies 101 exactly represented equality examples, 3969 rational-grid admissible factor pairs, and 500 dual-vector parameter checks. It reports 9469 successful exact assertions. These computations support the critical algebraic identity and examples; the inequality and equality classification on the full probability simplices follow from steps 2–5, not from numerical sampling.

Run `python3 checker.py` with Python 3.9 or later. No third-party package is required.

## Relationship to prior work
Metya and Mukherjee (2026, Section 4.3, Conjecture 4.7) define the same diagonal convolution model and conjecture that its uniform \(\ell_1\)-projection distance is \(1/(2n-1)\) for every \(n\ge3\). Their equation (22) already exhibits the attaining family, so that upper-bound construction is **not** claimed as new. The contribution here is the universal matching lower bound and complete equality characterization for \(n=3\).

Asgarli, Hartglass, Ostrov, and Walden (2023, Theorem 1) determine an exact \(\ell_2\)-squared projection and its unique minimizer for \(n\)-sided dice, including \(n=3\). This neither determines the \(\ell_1\) optimum nor its entire minimizing family. The 2026 source also treats relative entropy and line-metric Wasserstein distance separately; neither result contains the asserted Manhattan projection conclusion.

## Limitations
No result for \(n\ge4\) follows from the proof. The classification is for unconstrained nonnegative three-component factors; requiring every component to be strictly positive eliminates the displayed minimizers. The proof does not establish originality against inaccessible or unindexed independent arguments. The result has received only the documented self-review; no independent audit is represented.

## References
- N. Metya and S. Mukherjee, *Approximate Uniformity in Finite Convolution Models*, arXiv:2609.38243v1 (first posted 2026-09-29), especially Sections 4.1–4.3 and Conjecture 4.7. https://arxiv.org/html/2609.38243v1
- S. Asgarli, M. Hartglass, D. Ostrov, and B. Walden, *A Fair Shake: How Close Can the Sum of n-Sided Dice Be to a Uniform Distribution?*, arXiv:2304.08501v2 (2023), especially Theorem 1 and Section 3. https://arxiv.org/pdf/2304.08501

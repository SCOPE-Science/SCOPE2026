# Sharp endpoint growth and two extremizing masks for finite dyadic Haar-level projections

## Finding

For every integer \(n\ge 1\), let \(\Omega_n=\{0,1\}^n\) with uniform probability, and let \(E_k\) be conditional expectation onto the first \(k\) coordinates, for \(0\le k\le n\). Thus \(E_0\) is global averaging and \(E_n\) is the identity. For a binary level mask \(b=(b_0,\ldots,b_{n-1})\in\{0,1\}^n\), define the orthogonal Haar-level projection
\[
P_b=\sum_{k=0}^{n-1}b_k(E_{k+1}-E_k).
\]
The exact extremal strong endpoint norms are
\[
\boxed{\max_{b\in\{0,1\}^n}\|P_b\|_{L^\infty\to L^\infty}
=\max_{b\in\{0,1\}^n}\|P_b\|_{L^1\to L^1}
=\frac n3+\frac79+\frac{(-1)^n}{9\,2^{n-1}}.}
\]
For \(n=1\) the unique maximizing mask is \((1)\), and for \(n=2\) it is \((1,1)\). For every \(n\ge3\), exactly two level masks attain the maximum: \(b_0=b_{n-1}=1\), the intermediate bits \(b_1,\ldots,b_{n-2}\) alternate, and either choice \(b_1=0\) or \(b_1=1\) is permitted. Every mask has a sign-valued \(L^\infty\) extremizer. The maximum grows as \(n/3+7/9+O(2^{-n})\), even though each individual level difference has operator norm one and the sum of all differences has norm \(2-2^{1-n}\) for \(n\ge1\).

## Assumptions and scope

All functions are real-valued, although the endpoint operator norms coincide for complex-valued functions. The conditional expectations are with respect to the uniform product measure on exactly \(n\) binary coordinates. A mask selects *entire levels*: the same bit \(b_k\) is used for all \(2^k\) Haar functions at depth \(k\). The theorem does not optimize over arbitrary masks varying from one dyadic node to another, nor over biased binary product measures.

For any mask, define the prefix-weight state \(S_h=\sum_{k=0}^{h-1}b_k2^k\), with \(S_0=0\). A second, exact, nonoptimized formula is
\[
\boxed{\|P_b\|_{L^1\to L^1}=\|P_b\|_{L^\infty\to L^\infty}
=\sum_{h=0}^{n-1}\frac{|S_h-b_h2^h|}{2^{h+1}}+\frac{S_n}{2^n}.}
\]
This finite formula allows full reproduction of every claim without numerical approximation.

## Proof

**1. Orthogonal projection and the kernel.** Since \(E_kE_\ell=E_{\min(k,\ell)}\), the operators \(D_k=E_{k+1}-E_k\) are pairwise orthogonal self-adjoint idempotents. Thus every \(P_b\) is an orthogonal projection in \(L^2(\Omega_n)\). Writing conditional expectations as averages, the integral kernel relative to uniform probability is
\[
K_b(x,y)=\sum_{k=0}^{n-1}b_k\big(2^{k+1}{\bf1}_{\{x_{1:k+1}=y_{1:k+1}\}}-2^k{\bf1}_{\{x_{1:k}=y_{1:k}\}}\big).
\]
If \(y\ne x\) and exactly the first \(h\) bits agree, then \(K_b(x,y)=S_h-b_h2^h\). If \(y=x\), then \(K_b(x,x)=S_n\). For every fixed \(x\), the probability of the former event is \(2^{-h-1}\) and that of the latter is \(2^{-n}\). Hence the absolute row integral is precisely the asserted nonoptimized formula. It is independent of \(x\), so equals the \(L^\infty\) norm; its sharpness follows by taking \(f(y)=\operatorname{sgn}K_b(x,y)\) and defining either sign at zero entries. Symmetry of \(K_b\) identifies the \(L^1\) norm with the same absolute column sum.

**2. Bellman reduction.** Put \(z_h=S_h/2^h\), so \(z_0=0\), \(z_{h+1}=(z_h+b_h)/2\), and \(0\le z_h<1\). The exact row formula becomes
\[
N(b)=\frac12\sum_{h=0}^{n-1}|z_h-b_h|+z_n.
\]
Define \(V_r(z)\) as the largest possible value of this cost over \(r\) further mask bits, starting at \(z\in[0,1]\), with terminal payoff equal to the final state. It obeys
\[
V_0(z)=z,\qquad
V_{r+1}(z)=\max\left\{\frac z2+V_r(z/2),\frac{1-z}{2}+V_r((1+z)/2)\right\}.
\]
Directly \(V_1(z)=1\) for the entire interval. Inductively, for each \(r\ge1\),
\[
V_r(z)=M_r-a_r\min\{z,1-z\},
\qquad M_1=1,\ a_1=0,
\]
with recurrence
\[
a_{r+1}=\frac{1-a_r}{2},\qquad M_{r+1}=M_r+a_{r+1}.
\]
Indeed, for the first branch \(z/2\le 1/2\), so its value equals \(M_r+(1-a_r)z/2\); for the second branch \((1+z)/2\ge1/2\), so its value is \(M_r+(1-a_r)(1-z)/2\). Their maximum is exactly the stated tent-shaped formula with the displayed recursion. No approximate or unverified step enters this induction.

**3. Sharp bound.** The recursion gives \(a_r=(1+2(-1/2)^r)/3\) for every \(r\ge1\). Summing the increments of \(M_r\) gives
\[
M_n=\frac n3+\frac79+\frac{(-1)^n}{9\,2^{n-1}}.
\]
Since \(z_0=0\), the maximal operator norm is \(V_n(0)=M_n\).

**4. Exhaustive characterization of maximizing masks.** For any remaining horizon \(r\ge2\), the two Bellman branches are equal precisely at \(z=1/2\). Since \(1-a_{r-1}>0\), the uniquely optimal next bit is \(1\) if \(z<1/2\) and \(0\) if \(z>1/2\). When one step remains, the unique optimal bit is \(1\) for every reachable \(z<1\). Therefore the first bit is \(1\); when \(n\ge3\), the next state is \(1/2\) and either second bit is optimal. The state then lies strictly below or above \(1/2\); until the final step its optimal next bits alternate, and the last bit is always \(1\). The claimed two masks are exhaustive. The cases \(n=1,2\) follow directly from the one-step rule.

**5. Individual and complete-level comparison.** Each \(D_k\) has an absolute row integral equal to one. When every bit is one, \(P_b=I-E_0\), and its norm is \(2-2^{1-n}\) (which equals one at \(n=1\)); this supplies the claimed contrast between retaining all scales and selecting alternating scales.

## Verification

The companion `check.py` uses Python standard-library exact rational arithmetic. It exhaustively enumerates every level mask for \(1\le n\le12\), verifies both the sharp constant and the exact set of maximizing masks, constructs every kernel row for all masks through \(n=6\), and compares the Bellman formula on a rational grid for \(1\le r\le7\). Its completed run passed 14045 assertions. These finite checks are reproducibility tests, not substitutes for the induction proving the theorem at every integer \(n\ge1\).

## Relationship to prior work

Orthogonal Haar expansions, martingale-difference operators, and unconditionality questions are classical. Semenov and Uksusov (2012), particularly their Theorem 3, characterize bounded Haar multipliers at strong endpoints through bounded variation along dyadic chains up to norm-equivalence constants; that does not furnish the exact finite-depth constant or the two extremizing homogeneous level masks above. Osękowski (2013), Sections 1–2, proves sharp restricted weak-type bounds and martingale inequalities for Haar projections, rather than this finite-horizon strong \(L^1\)/\(L^\infty\) maximization. Choi's work identifies sharp \(L^p\) constants at interior exponents and is not a finite strong endpoint formula. The present theorem is an exact finite-horizon extremal classification, not a new general martingale-transform inequality.

## Limitations

The proof is restricted to uniformly split dyadic levels and masks that are constant across each level. No universal claim is made for general node-dependent Haar multipliers, unequal split probabilities, other endpoint scales, or nonlinear projections. The bibliographic comparison supports originality only within inspected material; an equivalent older finite-depth formula may exist under alternate Haar multiplier terminology. In particular, the later pages of the 2012 Russian-language source could not be examined completely during the comparison, so its full scope is an identified priority risk.

## References

1. E. M. Semenov and S. N. Uksusov, *Multipliers of the Haar series*, Sibirsk. Mat. Zh. 53 (2012), 388–395; English translation: Siberian Math. J. 53 (2012), 310–315. https://www.mathnet.ru/eng/smj2313 ; DOI: 10.1134/S0037446612020139.
2. A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces (2013), article 646012. DOI: 10.1155/2013/646012 (publicly issued 2013-12-05).
3. K. P. Choi, *A sharp inequality for martingale transforms and the unconditional basis constant of a monotone basis in \(L^p(0,1)\)*, Trans. Amer. Math. Soc. (1992). DOI: 10.2307/2153920.

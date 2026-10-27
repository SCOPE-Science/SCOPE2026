# Exact finite-termination phases and a golden-ratio startup law for AdaBB on isotropic quadratics

## Finding
For the original adaptive Barzilai–Borwein algorithm (AdaBB, Algorithm 1 of Zhou, Ma, and Yang), applied in exact arithmetic to \(f(x)=c\|x\|_2^2/2\) with \(c>0\), \(x^0\ne0\), and arbitrary dimension \(d\ge1\), the first zero-iterate index \(K=\min\{k\ge1:x^k=0\}\) is finite for every initial \(\alpha_0>0\), \(\theta_0\ge0\). Put \(a=c\alpha_0\) and let the initialization prescribed by equation (36) of the source be
\[
\theta_0^{\mathrm{inf}}=\begin{cases}(2a^2)^{-1}-1,&0<a\le 1/\sqrt2,\\0,&a>1/\sqrt2.\end{cases}
\]
Then the **complete and sharp termination-index classification** is
\[
K=\begin{cases}
7,&0<a\le1/(7\sqrt2),\\
4,&1/(7\sqrt2)<a<1,\quad a\ne1/\sqrt2,\\
3,&a=1/\sqrt2,\\
1,&a=1,\\
2,&1<a<2,\\
5,&a\ge2.
\end{cases}
\]
In particular the uniform bound \(K\le7\) is attained on a whole positive interval, and crossing \(a=1/(7\sqrt2)\) from above to below changes the exact required count from four to seven.

For the also-admissible uninformed initialization \(\theta_0=0\) and \(0<a<1\), define \(q_0=0\), \(q_j=\sqrt{1+q_{j-1}}\), \(P_j=\prod_{i=1}^{j}q_i\), and \(T(a)=\min\{j\ge1:aP_j\ge1\}\). Then
\[
K=\begin{cases}T(a)+1,&aP_{T(a)}=1,\\T(a)+2,&aP_{T(a)}>1,\end{cases}
\qquad
K=\frac{\log(1/a)}{\log((1+\sqrt5)/2)}+O(1)\quad(a\downarrow0).
\]
The leading coefficient is sharp. Thus the source's informed initialization removes an unbounded logarithmic startup delay on this elementary but natural strongly convex test family.

## Assumptions and scope
The objective is the centered isotropic quadratic on finite-dimensional real Euclidean space; \(c>0\), \(d\ge1\), \(x^0\ne0\), \(\alpha_0>0\), and \(\theta_0\ge0\). Iterations are exact and are stopped at the first zero iterate. The initial short Barzilai–Borwein quantity is well-defined: \(x^1-x^0=-\alpha_0cx^0\ne0\). The result concerns **Algorithm 1, with its Option II branches**, not any of the alternate Option I implementations or the experiment-only override of \(\theta_1\) sometimes used in the source.

For a nonterminal step, define normalized \(a_k=c\alpha_k\). Since \(\nabla f(x)=cx\), the short Barzilai–Borwein quotient equals \(\lambda_k=1/c\). The exact scalar transitions, applied when the previous normalized step is \(a\), are
\[
(a',\theta')=\begin{cases}
(a\sqrt{1+\theta},\sqrt{1+\theta}),&0<a\le1,\\
(1,2/a-1),&1<a<2,\\
(1/\sqrt2,1/(\sqrt2a)),&a\ge2.
\end{cases}\tag{1}
\]
Taking a normalized step of exactly one annihilates the entire iterate at the following index: \(x^{k+1}=(1-a_k)x^k\).

## Proof
**1. Uniform reset lemma.** Suppose the current normalized step is \(a\ge2\). Transition (1) produces \((a_1,\theta_1)=(1/\sqrt2,t)\), where \(0<t\le1/(2\sqrt2)\). Its next two case-I updates yield
\[
 a_2=u/\sqrt2,\quad \theta_2=u,\quad a_3=u\sqrt{1+u}/\sqrt2,\quad u=\sqrt{1+t}>1.
\]
Since \(u<\sqrt2\), \(1<a_3<\sqrt{1+\sqrt2}<2\). The subsequent case-II update sets \(a_4=1\), giving a zero iterate on the fifth update after the original \(a\ge2\). Every inequality is strict for finite \(a\). This proves the reset mechanism without any finite sampling assumption.

**2. Informed initialization and every boundary.** If \(0<a\le1/\sqrt2\), the prescribed initial value gives \(a_1=1/\sqrt2\) and \(\theta_1=1/(\sqrt2a)\). A second case-I update yields
\[
 a_2^2=\tfrac12\left(1+\frac1{\sqrt2a}\right).
\]
Consequently \(a_2\ge2\) exactly when \(a\le1/(7\sqrt2)\), \(1<a_2<2\) when \(1/(7\sqrt2)<a<1/\sqrt2\), and \(a_2=1\) exactly when \(a=1/\sqrt2\). In the first range, apply the reset lemma at \(a_2\) to obtain \(a_6=1\) and \(x^7=0\). None of \(a_0,\ldots,a_5\) equals one (the strict post-reset inequality is essential), so \(K=7\). The remaining two ranges give \(K=4\) and \(K=3\), respectively.

If \(1/\sqrt2<a<1\), the informed \(\theta_0\) is zero. Then \(a_1=a\), \(\theta_1=1\), and \(a_2=\sqrt2a\in(1,\sqrt2)\); the next case-II step gives \(a_3=1\) and \(K=4\). If \(a=1\), the first iterate is zero and \(K=1\). If \(1<a<2\), the first adaptive step sets \(a_1=1\) and \(K=2\). If \(a\ge2\), the reset lemma at the initial step gives \(a_4=1\) and \(K=5\). In all cases the listed earlier steps differ from one, proving the **exact** classification and sharp uniform bound.

**3. Arbitrary starts terminate.** When case I persists, the new ratio satisfies \(\theta_j=\sqrt{1+\theta_{j-1}}\). After at most two such updates, every subsequent ratio is at least \(\sqrt2\); therefore the normalized step cannot stay below one forever. At the first subsequent step \(a_j\ge1\), equality terminates immediately, \(1<a_j<2\) triggers case II and terminates one step later, and \(a_j\ge2\) invokes the reset lemma. Any initially oversized step can be treated directly by that lemma. Hence every admissible initialization terminates in finitely many steps.

**4. Sharp uninformed startup.** For \(\theta_0=0\), all first-crossing ratios are the fixed sequence \(q_1=1\), \(q_j=\sqrt{1+q_{j-1}}\) and increase strictly to \(\varphi=(1+\sqrt5)/2\). Before crossing one, \(a_j=aP_j\), which proves the exact formula for \(T(a)\). Because \(q_j<\varphi<2\), a strict crossing always lands below two, so either the crossing step itself equals one or the next case-II step does. Thus \(K=T+1\) at equality and \(K=T+2\) otherwise.

The map \(h(t)=\sqrt{1+t}\) is a contraction on \([0,\infty)\), with derivative at most \(1/2\). Therefore \(|q_j-\varphi|\le\varphi 2^{-j}\), and \(\sum_{j\ge1}|\log(q_j/\varphi)|<\infty\). Hence the infinite product \(C=\prod_{j\ge1}q_j/\varphi\) lies strictly between zero and infinity and \(P_j=C\varphi^j(1+o(1))\). First-crossing inequalities imply \(T(a)=\log(1/a)/\log\varphi+O(1)\). The exact formula for \(K\) finishes the asymptotic statement. The ratio of \(K(a)\) to \(\log(1/a)\) tends to \(1/\log\varphi\), so the leading coefficient cannot be reduced.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. The code checks thousands of informed-start branches at high Decimal precision, includes near-zero starts where binary floats can erase a mathematically strict post-reset crossing, tests the first-crossing formula for 199 uninformed starts, and checks a strict post-reset inequality. The analytical proof alone certifies the all-parameter result, exact irrational boundaries, and asymptotics; finite tests are corroboration only.

## Relationship to prior work
Zhou, Ma and Yang (2024), Algorithm 1, directly supplies the three branch rules; their equation (36) supplies the informed initialization. Their Lemma 4.1 proves uniform lower bounds on the later steps, while Table 1 includes an iterated-radical product in an analysis of a **different** adaptive gradient algorithm. Those results do not state the exact AdaBB termination-index partition, its discontinuity at \(1/(7\sqrt2)\), or the sharp leading coefficient of the uninformed AdaBB termination delay. The update laws and initialization are not claimed as new here.

Huang, Dai, Liu and Zhang (2022) prove finite termination on two-dimensional quadratics for **a different accelerated BB method incorporating a special spectral step**. That theorem does not give the present original-AdaBB scalar dynamics. An exact formula for the much simpler classical BB method on an isotropic quadratic is immediate (the short BB step equals \(1/c\)), but does not imply the behavior of the safeguarded AdaBB recurrence.

## Limitations
The finding is an exact-arithmetic one-spectrum benchmark: it does not imply bounded finite termination on general strongly convex or anisotropic quadratics, nor for alternate AdaBB variants. The informed \(\theta_0\) can grow quadratically as \(\alpha_0\downarrow0\); finite precision can overflow or round away the small strict post-reset inequality. No universal numerical robustness is asserted. Priority relative to undiscovered equivalent recurrences in older optimization literature remains an open human-verification risk; the result has not received independent audit.

## References
1. D. Zhou, S. Ma, and J. Yang, *AdaBB: Adaptive Barzilai-Borwein Method for Convex Optimization*, arXiv:2401.08024, first submitted 2024-01-16. https://arxiv.org/abs/2401.08024 . Algorithm 1, equation (36), Lemma 4.1, and Table 1 were inspected.
2. Y. Huang, Y.-H. Dai, X.-W. Liu, and H. Zhang, *On the acceleration of the Barzilai–Borwein method*, Computational Optimization and Applications 81 (2022), DOI:10.1007/s10589-022-00349-z. Open full text: https://www.math.lsu.edu/~hozhang/papers/AccBB.pdf . Theorem 1 and its distinct update construction were inspected.

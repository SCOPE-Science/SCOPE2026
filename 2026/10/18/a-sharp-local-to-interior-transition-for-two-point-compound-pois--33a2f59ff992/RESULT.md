# A sharp local-to-interior transition for two-point compound-Poisson sub-gamma scales

## Finding
Let \(\lambda>0\). Consider a centered compound-Poisson random variable whose jump \(J\) equals \(1\) with probability \(1-q\) and \(5\) with probability \(q\). Fix the quadratic proxy in the right sub-gamma moment bound at the true variance \(V=\lambda(1+24q)\), and minimize its scale \(c\). Define
\[
q_- = \frac{1927+575\sqrt{11}}{174752}=0.021940002142\ldots,\qquad
q_c = \frac{17}{592}+\frac{25\sqrt{21}}{4144}=0.056362063796\ldots.
\]
For **every** \(q\in[q_-,1]\), the following dichotomy is exact:

1. If \(q_-\le q<q_c\), the variational objective \(\Psi_q(t)\) defined below is strictly increasing up to **one and only one** positive argument \(t_q\), and strictly decreasing thereafter. In particular, \(t_q\) is the unique global optimizer, its second derivative is strictly negative there, and the optimal scale is \(c_*(q)=\Psi_q(t_q)>m_q\), where \(m_q=(1+124q)/(3(1+24q))\).
2. If \(q_c\le q\le1\), the objective is strictly decreasing on \((0,\infty)\); the optimal scale is exactly \(c_*(q)=m_q\), approached only in the limit \(t\downarrow0\). There is no positive optimizer.

The transition is quantitative. Let
\[
b_2(q)=\frac{16576q^2-952q+1}{36(1+24q)^2},\quad
b_3(q)=\frac{80976q^2-2852q+1}{45(1+24q)^2},
\]
and write \(d=b_2'(q_c)>0\), \(e=b_3(q_c)>0\). As \(q\uparrow q_c\),
\[
t_q=\frac de(q_c-q)+O((q_c-q)^2),\qquad
c_*(q)-m_q=\frac{d^2}{2e}(q_c-q)^2+O((q_c-q)^3).
\]
The two leading coefficients are approximately \(11.7513493680\) and \(27.0249963940\), respectively. At \(q=1/40\), the unique maximizer is \(t_q=0.473723111601\ldots\) and \(c_*(q)=0.895416095555\ldots\).

## Assumptions and scope
The Poisson count has mean \(\lambda>0\), independently of i.i.d. jumps \(J\in\{1,5\}\). The centered law is \(X=\sum_{j=1}^{N}J_j-\lambda\mathbb E J\). The admissible scale \(c\ge0\) must satisfy
\[
\log\mathbb E e^{tX}\le \frac{Vt^2}{2(1-ct)}\qquad (0\le t<1/c),
\]
where \(1/0=\infty\). Its infimum is \(c_*(q)\). The results concern the interval \(q\in[q_-,1]\), not every two-point jump distribution or every \(q\in[0,1]\). The intensity \(\lambda\) is arbitrary, and the conclusions are independent of it.

Set \(M_q(0)=1\) and, for \(t>0\),
\[
M_q(t)=\frac{2\{(1-q)e^t+qe^{5t}-1-(1+4q)t\}}{(1+24q)t^2},\qquad
\Psi_q(t)=\frac{1-M_q(t)^{-1}}{t}.
\]
The first quantity is the moment generating function of the second-order equilibrium transform of \(J\). The exact variational reduction is \(c_*(q)=\sup_{t>0}\Psi_q(t)\), and \(\Psi_q(0+)=m_q\). Every stated uniqueness assertion concerns optimization over all real \(t>0\).

## Proof
The centered compound-Poisson cumulant-generating function is
\[
K_q(t)=\lambda\{(1-q)(e^t-1-t)+q(e^{5t}-1-5t)\}.
\]
Consequently, \(2K_q(t)/(Vt^2)=M_q(t)\). For any \(c\ge0\), the sub-gamma inequality is equivalent, on its domain, to \(M_q(t)\le(1-ct)^{-1}\). Thus it implies \(\Psi_q(t)\le c\) for \(0<t<1/c\), while \(\Psi_q(t)\le1/t\le c\) for \(t\ge1/c\). Conversely, taking \(c=\sup_{t>0}\Psi_q(t)\) gives the bound at all \(t<1/c\). The supremum is finite because \(\Psi_q(t)\le1/t\) for large \(t\) and has a finite limit at zero. This proves the exact variational reduction without an additional tightness assumption.

Put \(M_q(t)=\sum_{n\ge0}a_n(q)t^n\) and \(a_0=1\). Direct exponential expansion gives the **exact entire series**
\[
a_n(q)=\frac{2\{1+(5^{n+2}-1)q\}}{(n+2)!(1+24q)}\quad(n\ge0).
\]
In particular \(a_1=m_q\), \(a_2=(1+624q)/(12(1+24q))\). Define
\[
H_q(t)=M_q(t)(M_q(t)-1)-tM_q'(t)
=\sum_{n\ge2}b_n(q)t^n,
\]
where
\[
b_n(q)=(1-n)a_n(q)+\sum_{k=1}^{n-1}a_k(q)a_{n-k}(q).
\]
Exact algebra yields the stated expressions for \(b_2,b_3\), and
\[
b_4(q)=\frac{2796032q^2-61664q+7}{720(1+24q)^2}.
\]
The larger root of the numerator of \(b_4\) is exactly \(q_-\); hence \(b_4\ge0\) for all \(q\ge q_-\). The larger root of the numerator of \(b_2\) is exactly \(q_c\); its smaller root is less than \(q_-\). Therefore \(b_2<0\) for \(q\in[q_-,q_c)\), and \(b_2\ge0\) for \(q\in[q_c,1]\). The positive root of \(b_3\) above zero is \((713+25\sqrt{781})/40488<q_c\), so \(b_3>0\) for \(q\ge q_c\).

We next prove **every** remaining coefficient positive, without reliance on a finite Taylor truncation. Since \(q_->1/50\), direct inspection of the rational formulas for \(a_1,a_2\) gives \(a_1,a_2\ge3/4\). Because \(1\le J\le5\), the jump moments obey \(\mathbb E J^{r+s}\le5^s\mathbb E J^r\) for integers \(r,s\ge0\). Consequently, for every \(n\ge5\),
\[
\frac{a_{n-1}}{a_n}\ge\frac{n+2}{5},\qquad
\frac{a_{n-2}}{a_n}\ge\frac{(n+2)(n+1)}{25}.
\]
The four distinct convolution terms corresponding to \(k=1,2,n-2,n-1\) give
\[
\begin{aligned}
\frac{b_n}{a_n}
&\ge 1-n+2a_1\frac{a_{n-1}}{a_n}+2a_2\frac{a_{n-2}}{a_n}\\
&\ge 1-n+\frac{3(n+2)}{10}+\frac{3(n+2)(n+1)}{50}\\
&=\frac{3n^2-26n+86}{50}>0\qquad(n\ge5).
\end{aligned}
\]
The last quadratic equals \(31/50\) at \(n=5\) and increases for all \(n\ge5\). This establishes the coefficient signs for the **entire** function, not merely for numerical samples.

If \(q_-\le q<q_c\), consider
\[
F_q(t)=\frac{H_q(t)}{t^3}=\frac{b_2}{t}+b_3+b_4t+\sum_{n\ge5}b_n t^{n-3}.
\]
Its derivative is strictly positive for every \(t>0\), since \(b_2<0\), \(b_4\ge0\), and \(b_n>0\) for \(n\ge5\). Also \(F_q(t)\to-\infty\) as \(t\downarrow0\), while \(F_q(t)\to+\infty\) as \(t\to\infty\), already from the positive \(b_5t^2\) term. Thus \(H_q\) has exactly one positive zero, \(t_q\), with \(H_q'(t_q)>0\). Since
\[
\Psi_q'(t)=-\frac{H_q(t)}{t^2M_q(t)^2},
\]
the objective increases before \(t_q\) and decreases afterwards, with \(\Psi_q''(t_q)<0\). This proves uniqueness and strict global optimality. If \(q\ge q_c\), the coefficients \(b_2,b_3,b_4,b_5,\ldots\) are all nonnegative, with \(b_3>0\), and hence \(H_q(t)>0\) for every positive \(t\). Thus \(\Psi_q\) is strictly decreasing and \(c_*(q)=\Psi_q(0+)=a_1=m_q\).

For the transition, the analytic function \(H_q(t)/t^2=b_2(q)+b_3(q)t+b_4(q)t^2+\cdots\) has derivative \(b_3(q_c)>0\) with respect to \(t\) at \((t,q)=(0,q_c)\). The analytic implicit-function theorem and the previously established unique-root property imply
\[
t_q=\frac{b_2'(q_c)}{b_3(q_c)}(q_c-q)+O((q_c-q)^2).
\]
Finally, the reciprocal-series expansion is uniform near \((q_c,0)\):
\[
\Psi_q(t)=a_1(q)-b_2(q)t+
\{a_1(q)b_2(q)-b_3(q)/2\}t^2+O(t^3).
\]
Inserting the expansion for \(t_q\) proves the stated quadratic onset of \(c_*(q)-m_q\). The intensity \(\lambda\) cancels everywhere, as claimed.

## Verification
The accompanying `verify.py` checks the three rational coefficient identities exactly with symbolic arithmetic, verifies the ordering and exact algebraic endpoints, checks the crucial \(n\ge5\) lower-bound polynomial, and reproduces the positive optimizer and scale at \(q=1/40\) at high precision. Run `python verify.py` with Python, SymPy, and mpmath installed. The infinite-sign proof, uniqueness, and critical asymptotics are analytical and do not rely on the finite checks.

## Relationship to prior work
Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws* (arXiv:2610.00032v1, initially public September 2, 2026), proves the general optimal-scale variational formula and gives the \(q=1/40\) two-point example. Its Section 7.2 explicitly establishes existence of an interior optimum but **does not establish uniqueness**. The present result resolves that issue, proves a complete optimizer dichotomy on an explicit nontrivial range of mixture probabilities, and quantifies the onset at the transition probability. Zhang and Wu's 2019 concentration inequalities for discrete compound-Poisson point processes use general Bernstein bounds; they do not yield this exact optimizer or phase transition. The earlier M-class literature characterizes local MGF-order behavior and is relevant background, not evidence of this particular optimization classification.

## Limitations
No classification is claimed for \(0\le q<q_-\), for other jump-size ratios, or for unbounded jumps. The lower range endpoint \(q_-\) is the coefficient-sign threshold used by the proof; it is **not** asserted to be the smallest probability for which uniqueness actually holds. The numerical decimal values are illustrative rather than exact certificates; the displayed radicals, equations, and analytic proof give the exact claims. Unindexed or unavailable earlier results may exist. Independent validation has not been performed.

## References
- Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public September 2, 2026), especially Sections 3, 6, and 7.2. https://arxiv.org/html/2610.00032v1
- H. Zhang and X. Wu, *Compound Poisson point processes, concentration and oracle inequalities*, Journal of Inequalities and Applications **2019**, Article 312, DOI:10.1186/s13660-019-2263-8; especially Section 3. https://link.springer.com/article/10.1186/s13660-019-2263-8
- B. Klar and A. Müller, *Characterizations of classes of lifetime distributions generalizing the NBUE class*, Journal of Applied Probability **40** (2003), 20–32, DOI:10.1239/jap/1044476825 (background on the M-class; abstract and metadata inspected).

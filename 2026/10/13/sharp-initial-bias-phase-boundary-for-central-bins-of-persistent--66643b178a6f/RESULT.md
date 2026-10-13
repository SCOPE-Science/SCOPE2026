# Sharp initial-bias phase boundary for central bins of persistent Markov walks

## Finding
Let \(X_1,\ldots,X_N\in\{+,-\}\) be a time-homogeneous Markov chain with \(\Pr(X_1=+)=\alpha\), \(\Pr(X_{i+1}=X_i)=p\), \(\Pr(X_{i+1}\ne X_i)=1-p\), where \(1/2<p<1\) and \(0\le\alpha\le1\). Write \(K_N=\#\{i:X_i=+\}\), \(u=(1-p)/p\), and \(b=2\alpha-1\). For each \(m\ge2\), put \(n=m-1\) and
\[
C_j(n,u)=\sum_{h=j}^{n}\binom{n}{h}\binom{n}{h-j}u^{2h-j}\quad(j=1,2),
\]
with an empty sum defined as zero. The **exact adjacent-central comparison** is
\[
\Pr(K_{2m}=m+1)-\Pr(K_{2m}=m)
=\frac{p^{2m-1}u}{m-1}\bigl[b(C_1+uC_2)-u(C_1+C_2)\bigr]. \tag{1}
\]
Consequently the left side is positive, zero, or negative exactly as
\[
b\quad\text{is greater than, equal to, or less than}\quad
\theta_m(u):=u\frac{C_1(n,u)+C_2(n,u)}{C_1(n,u)+uC_2(n,u)}. \tag{2}
\]
For every fixed \(0<u<1\),
\[
\theta_2(u)=u,\qquad
u\le\theta_m(u)<\frac{2u}{1+u}=2(1-p),\qquad
\lim_{m\to\infty}\theta_m(u)=2(1-p).
\]
Here the middle displayed lower bound is strict for \(m\ge3\). In particular the **sharp uniform-in-length phase boundary** is
\[
\boxed{\ \Pr(K_{2m}=m+1)>\Pr(K_{2m}=m)\ \text{for every integer }m\ge2
\quad\Longleftrightarrow\quad \alpha\ge\frac32-p.\ }
\tag{3}
\]
Equality \(\alpha=3/2-p\) in the parameter condition still yields a *strict* probability inequality at every finite length. If \(\alpha<3/2-p\), the opposite strict inequality holds for all sufficiently large even lengths.

A finite-size reversal occurs for **every** \(p\in(1/2,1)\) and every \(\alpha\) in the nonempty interval
\[
\frac1{2p}<\alpha<\frac32-p:\qquad
\Pr(K_4=3)>\Pr(K_4=2),\quad
\Pr(K_{2m}=m+1)<\Pr(K_{2m}=m)\ \text{for all sufficiently large }m.
\]
For example, \(p=3/4\), \(\alpha=7/10\) give differences \(1/320\) at \(N=4\) and \(-161/1310720\) at \(N=10\).

## Assumptions and scope
The chain has exactly two states, spatially symmetric persistence, free initial and terminal boundaries, and an arbitrary initial probability \(\alpha\). The parameter \(p\) is fixed in \((1/2,1)\), and the statement concerns even sample lengths \(N=2m\ge4\). All probabilities use the complete initial law, not conditioning on either endpoint state. The comparison is **between two adjacent central occupancy bins**; it does not identify the global mode when the endpoint bins can be larger.

## Proof
Fix \(m\ge2\) and \(n=m-1\). Every word beginning with \(+\), containing \(k\) plus signs and \(l=2m-k\) minus signs, has probability \(\alpha p^{2m-1}u^s\), where \(s\) is its number of switches. Let \(T(k)\) be the sum of \(u^s\) over such words. For \(1\le k,l\), separating odd and even numbers of switches into positive run compositions gives
\[
T(k)=\sum_{r\ge1}\binom{k-1}{r-1}\binom{l-1}{r-1}u^{2r-1}
+\sum_{r\ge1}\binom{k-1}{r}\binom{l-1}{r-1}u^{2r}. \tag{4}
\]
All binomial coefficients outside their usual range are zero. Starting with \(-\) instead of \(+\) gives the reflected weight \(T(2m-k)\), so
\[
\Pr(K_{2m}=k)=p^{2m-1}\bigl[\alpha T(k)+(1-\alpha)T(2m-k)\bigr]. \tag{5}
\]
The following binomial identities hold for integers \(n\ge1\), with zero-binomial conventions:
\[
\begin{aligned}
\binom{n+1}{h}\binom{n-1}{h}-\binom{n}{h}^2
&=-\frac1n\binom{n}{h}\binom{n}{h-1},\\
\binom{n+1}{r}\binom{n-1}{r-1}-\binom{n}{r}\binom{n}{r-1}
&=\frac1n\binom{n}{r}\binom{n}{r-1},\\
\binom{n-1}{r}\binom{n+1}{r-1}-\binom{n}{r}\binom{n}{r-1}
&=-\frac1n\binom{n}{r}\binom{n}{r-1}
-\frac2n\binom{n}{r}\binom{n}{r-2}.
\end{aligned} \tag{6}
\]
These follow by factorial cancellation; the edge cases follow from the zero convention. Apply (6) termwise in (4) at \(k=m+1,m,m-1\). The odd-switch contributions each change by \(-u^2C_1/n\); the even-switch contributions change respectively by \(uC_1/n\) and \(-(uC_1+2u^2C_2)/n\). Thus
\[
T(m+1)-T(m)=\frac{u}{n}(1-u)C_1,
\qquad
T(m-1)-T(m)=-\frac{u}{n}\bigl[(1+u)C_1+2uC_2\bigr]. \tag{7}
\]
Inserting (7) in (5) proves the exact identity (1) and its sign classification (2).

To bound the threshold, observe that \(C_j(n,u)\) is the coefficient of \(z^j\) in \((1+uz)^n(1+uz^{-1})^n\), equivalently the coefficient of \(z^j\) in \((1+u^2+u(z+z^{-1}))^n\). The latter is the \(n\)-fold convolution of the strictly positive symmetric unimodal three-point sequence with center weight \(1+u^2\) and neighbor weights \(u\). Convolution preserves symmetric unimodality. Moreover, writing its coefficients as \(c_n(j)\),
\[
\begin{aligned}
c_{n+1}(1)-c_{n+1}(2)
&=(1+u^2)\bigl(c_n(1)-c_n(2)\bigr)\\
&\quad+u\bigl[(c_n(0)-c_n(1))+(c_n(2)-c_n(3))\bigr]>0,
\end{aligned}
\]
starting from \(c_1(1)=u>c_1(2)=0\). Hence \(C_1>C_2\ge0\), with \(C_2>0\) for \(n\ge2\). The function \(r\mapsto u(1+r)/(1+ur)\) is strictly increasing for \(0<u<1\), and so (2) satisfies \(u\le\theta_m(u)<2u/(1+u)\), strictly above \(u\) for \(m\ge3\).

Finally, if \(Y_i,Z_i\) are independent Bernoulli variables of parameter \(u/(1+u)\), then
\[
\frac{C_j(n,u)}{(1+u)^{2n}}=\Pr\left(\sum_{i=1}^n(Y_i-Z_i)=j\right),\quad j=1,2.
\]
Their differences form an aperiodic, centered, integer-valued iid random walk of variance \(2u/(1+u)^2>0\). The elementary lattice local central limit theorem (or Fourier inversion of the displayed Laurent polynomial) yields, for each fixed \(j\),
\[
\frac{C_j(n,u)}{(1+u)^{2n}}\sim
\frac{1+u}{\sqrt{4\pi n u}}.
\]
Therefore \(C_2/C_1\to1\) and \(\theta_m\to2u/(1+u)=2(1-p)\). At the boundary \(b=2u/(1+u)\), the bracket in (1) simplifies exactly to \(u(1-u)(C_1-C_2)/(1+u)>0\), making strictness at equality explicit. Because every finite threshold is strictly below this limit, \(b\ge2(1-p)\) forces (1) strictly positive for all \(m\), whereas \(b<2(1-p)\) forces (1) negative eventually. Since \(b=2\alpha-1\), this is (3). For \(m=2\), \(C_2=0\), so the threshold is \(b=u\), equivalent to \(\alpha=1/(2p)\). Combining this with the limit proves the claimed nonempty reversal interval. The rational examples follow by direct Markov recursion.

## Verification
Run \(\texttt{python checker.py}\) using Python 3 and the included standalone \(\texttt{checker.py}\). The checker computes occupancy probabilities by an independent two-component Markov dynamic program, compares them exactly with (1) for 680 rational parameter/length triples, and checks \(C_1>C_2\), finite-threshold bounds, normalization and a short-to-long reversal. Its computations use \(\texttt{fractions.Fraction}\) and integer binomial coefficients. These finite checks are cross-checks of (4)–(7); the infinite-length statement follows from the proof and local limit argument above, not enumeration.

## Relationship to prior work
Pemmasani, *Uniform Bessel bounds for endpoint crossings in the persistent random walk* (arXiv:2610.06935v1, 3 October 2026) studies the same symmetric transition model with **fair initial direction** and compares center bins to endpoint bins, rather than the arbitrary-start adjacent-center bias boundary in (3). Its exact run-count formula is classical and is credited here. Dekking and Kong, *Multimodality of the Markov binomial distribution* (2011), give the general-initial-law probability mass function and a classification of one-, two- and three-peak shapes, including interior log-concavity. Those results underlie the setting but do not state the all-length sharp initial-bias threshold or the exhibited size reversal. Renshaw and Henderson (1981) give exact correlated-walk transition probabilities; only their publisher abstract and later summaries could be accessed, so an unrecognized equivalent formulation remains a priority risk.

## Limitations
The exact threshold concerns only a single adjacent-central comparison and even lengths. It neither locates all global modes, nor extends directly to non-symmetric transition matrices, more than two states, or periodically closed boundaries. The coefficient ratio convergence is asymptotic at fixed \(0<u<1\) and does not assert a uniform rate as \(p\to1\). Prior-literature priority cannot be guaranteed from searches; the 1981 full text remains uninspected. Independent verification of the scientific contribution has not occurred.

## References
1. A. Pemmasani, *Uniform Bessel bounds for endpoint crossings in the persistent random walk*, arXiv:2610.06935v1 (first posted 3 October 2026), https://arxiv.org/abs/2610.06935.
2. M. Dekking and D. Kong, *Multimodality of the Markov binomial distribution*, J. Appl. Probab. 48 (2011), 938–953; arXiv:1102.3613v1, https://arxiv.org/abs/1102.3613.
3. E. Renshaw and R. Henderson, *The correlated random walk*, J. Appl. Probab. 18 (1981), 403–414, https://doi.org/10.2307/3213286.

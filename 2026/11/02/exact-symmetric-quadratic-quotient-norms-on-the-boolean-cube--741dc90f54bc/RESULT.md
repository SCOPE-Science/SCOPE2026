# Exact symmetric quadratic quotient norms on the Boolean cube

## Finding
Let \(n\ge2\), let \(\Omega_n=\{-1,1\}^n\) carry uniform probability, and let \(\mathcal T_{>2}\subset L^\infty(\Omega_n;\mathbb R)\) be the subspace of functions whose Walsh coefficients of degrees zero, one and two all vanish. Define
\[
Q_n(x)=\sum_{1\le i<j\le n}x_ix_j=\tfrac12\left[\left(\sum_{i=1}^n x_i\right)^2-n\right].
\]
Set \(z_{n,k}=((n-2k)^2-n)/2\) and \(w_{n,k}=2^{-n}\binom nk\) for \(0\le k\le n\). Choose **any weighted median** \(m_n\) of the values \(z_{n,k}\), with weights \(w_{n,k}\); that is, both \(\sum_{z_{n,k}<m_n}w_{n,k}\le1/2\) and \(\sum_{z_{n,k}>m_n}w_{n,k}\le1/2\). Then the exact real Banach-quotient norm is
\[
\boxed{\operatorname{dist}_{\infty}(Q_n,\mathcal T_{>2})=
\frac{\binom n2}{\displaystyle\sum_{k=0}^n2^{-n}\binom nk|z_{n,k}-m_n|}.}
\]
There is an explicit optimal representative with only three values, depending on whether \(Q_n\) is smaller than, equal to, or larger than the median. In addition, with \(a=\Phi^{-1}(3/4)\), where \(\Phi\) and \(\varphi\) are the standard Gaussian distribution function and density,
\[
\boxed{\lim_{n\to\infty}\frac1n\operatorname{dist}_{\infty}(Q_n,\mathcal T_{>2})
=\frac1{4a\varphi(a)}=1.1663872874\ldots.}
\]
Thus the optimal bounded realization of the same quadratic Walsh coefficients has order \(n\), whereas the original quadratic polynomial has supremum norm \(\binom n2\).

## Assumptions and scope
All spaces and coefficients are **real**. Walsh characters are \(\chi_A(x)=\prod_{i\in A}x_i\), with \(\chi_\varnothing=1\); normalized Walsh coefficients are \(\widehat f(A)=2^{-n}\sum_{x\in\Omega_n}f(x)\chi_A(x)\). The quotient norm is the infimum of \(\|Q_n-g\|_\infty\) over all \(g\in\mathcal T_{>2}\). No restriction is imposed on the higher-degree coefficients of \(g\). A weighted median exists, its absolute-deviation sum is positive, and its choice does not change that sum. The theorem applies to every integer \(n\ge2\) without numerical asymptotic assumptions.

## Proof
**1. A dual lower bound.** Write \(V_n=\mathbb E Q_n^2=\binom n2\), since the degree-two Walsh characters form an orthonormal family. If \(h=Q_n-g\) for \(g\in\mathcal T_{>2}\), Walsh orthogonality gives \(\mathbb E h=0\) and \(\mathbb E hQ_n=V_n\). For any real \(c\),
\[
 V_n=\mathbb E\big[h(Q_n-c)\big]
 \le\|h\|_\infty\,\mathbb E|Q_n-c|.
\]
Every median minimizes the last absolute deviation; choosing \(c=m_n\) yields the stated lower bound \(V_n/M_n\), where \(M_n=\mathbb E|Q_n-m_n|\).

**2. Attainment and full low-degree matching.** Put \(p_-=\mathbb P(Q_n<m_n)\), \(p_+=\mathbb P(Q_n>m_n)\), and \(p_0=\mathbb P(Q_n=m_n)>0\) when a support-point median is chosen. Median inequalities imply \(\tau=(p_--p_+)/p_0\in[-1,1]\). Define
\[
 h_n(x)=\frac{V_n}{M_n}\begin{cases}
 -1,&Q_n(x)<m_n,\\
 \tau,&Q_n(x)=m_n,\\
 1,&Q_n(x)>m_n.
 \end{cases}
\]
Then \(\mathbb E h_n=0\). Because the sign agrees off the median level,
\[
 \mathbb E[h_n Q_n]=\mathbb E[h_n(Q_n-m_n)]
 =\frac{V_n}{M_n}\mathbb E|Q_n-m_n|=V_n.
\]
The function \(h_n\) is invariant under coordinate permutations and simultaneous sign reversal. Hence every degree-one Walsh coefficient vanishes, and its degree-two coefficients are all equal. Since their sum equals \(\mathbb E[h_nQ_n]=V_n\) and there are \(V_n\) of them, each is exactly one. The constant coefficient is zero. Thus \(h_n-Q_n\in\mathcal T_{>2}\). Moreover \(\|h_n\|_\infty\le V_n/M_n\), with equality forced by step 1. This proves the exact formula and provides an optimal representative. If the median lies in an interval between two support values, one may choose a support-point median without changing \(M_n\).

**3. Asymptotic constant.** Let \(S_n=\sum_i x_i\) and \(Y_n=S_n/\sqrt n\). The central limit theorem gives \(Y_n\Rightarrow Z\sim N(0,1)\), and the strict positivity of the density of \(|Z|\) at its unique median \(a=\Phi^{-1}(3/4)\) implies that a support-point median \(s_n\) of \(|S_n|\) satisfies \(s_n/\sqrt n\to a\). Thus \(m_n/n=(s_n^2/n-1)/2\to(a^2-1)/2\). Since \(\sup_n\mathbb E Y_n^4\le3\), the family \(Y_n^2\) is uniformly integrable, yielding
\[
 \lim_{n\to\infty}\frac{M_n}{n}
 =\frac12\mathbb E|Z^2-a^2|=2a\varphi(a).
\]
For the last equality, \(\mathbb P(|Z|>a)=1/2\) and direct integration gives \(\mathbb E[(Z^2-a^2)_+]=2a\varphi(a)+(1-a^2)/2\). Because \(\mathbb E(Z^2-a^2)=1-a^2\), the absolute expectation equals \(4a\varphi(a)\). Finally \(V_n/n^2\to1/2\), proving the limit for the quotient norm.

## Verification
The accompanying standard-library script `checker.py` computes the median, absolute deviation, optimizing three-value function, and dual witness using exact rational arithmetic. It exhaustively checks every degree-zero, one and two Walsh coefficient for dimensions \(2\le n\le12\), and checks the rational shell and optimizer identities for \(2\le n\le250\). The expected first norms are \(1,3,4,5,20/3,7,896/99\) for \(n=2,\ldots,8\). The infinite-dimensional asymptotic conclusion is established by the proof, not by these finite calculations. To reproduce: `python3 checker.py`.

## Relationship to prior work
Eskenazis and Zhang, *Approximation of polynomials from Walsh tail spaces*, arXiv:2311.09021v1 (first publicly submitted 2023-11-15), study tail-space approximation, including the symmetric elementary Walsh polynomials. Their Theorem 4 and Corollary 5 concern **\(L^1\)** approximation and a fixed-order asymptotic, not this exact **\(L^\infty\)** quotient norm, its median optimizer, or its Gaussian-quartile constant. Their Proposition 1 uses general Banach duality, which is compatible with, but does not evaluate, the present exact norm. Oleszkiewicz, *On mimicking Rademacher sums in tail spaces* (2017), treats the \(L^1\) distance of degree-one Rademacher sums. Known degree-two Walsh **projection operator norms** and fourth-moment estimates address different extremal problems: a projection norm maximizes over all inputs, while the present norm optimizes all representatives of one prescribed quotient class. These distinctions do not establish absolute novelty beyond the inspected literature.

## Limitations
The result concerns one permutationally symmetric quadratic element in a **real** finite-dimensional Banach quotient. It does not compute the full quotient norm on all quadratic coefficient arrays or its complex version. The sharp asymptotic here is only first-order, with an \(o(n)\) remainder. The literature comparison cannot eliminate an equivalent treatment in older, differently named optimal-recovery or binomial-median literature. Independent assessment has not been performed.

## References
- A. Eskenazis and H. Zhang, *Approximation of polynomials from Walsh tail spaces*, arXiv:2311.09021v1 (2023-11-15); Studia Mathematica 275 (2024), 285–296, DOI 10.4064/sm231123-4-1.
- K. Oleszkiewicz, *On mimicking Rademacher sums in tail spaces*, in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 2169 (2017), pp. 331–337.
- R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), for Walsh and Krawtchouk notation.

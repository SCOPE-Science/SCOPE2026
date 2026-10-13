# Log-periodic mixed covariance of part count and distinct part sizes in uniform compositions

## Finding

Let a composition of a positive integer \(n\) be chosen uniformly from all ordered lists of positive integers summing to \(n\). Let \(K_n\) count its parts with multiplicity, and let \(D_n\) count the distinct sizes represented among its parts. Put \(L_n=\log_2 n\), \(\theta_n=\{L_n\}\), and, for \(k\in\mathbb Z\), set \(u_k(\theta)=2^{\theta-k-1}\). Define the absolutely convergent series

\[
 A(\theta)=\sum_{k\in\mathbb Z}u_k(\theta)e^{-u_k(\theta)},\qquad
 B(\theta)=\frac12\sum_{k\in\mathbb Z}
       \bigl(4+\log_2u_k(\theta)\bigr)u_k(\theta)e^{-u_k(\theta)}.
\]

**Theorem.** For uniform ordinary compositions,

\[
 \operatorname{Cov}(K_n,D_n)
 =-\frac{L_n}{2}A(\theta_n)+B(\theta_n)+o(1),\qquad n\to\infty.
\]

Both \(A\) and \(B\) are smooth, one-periodic functions. The function \(A\) is strictly positive and nonconstant; its Fourier coefficients are

\[
 \widehat A(\ell)=\frac{1}{\ln2}\,
 \Gamma\!\left(1-\frac{2\pi i\ell}{\ln2}\right),
 \qquad \ell\in\mathbb Z.
\]

In particular, the covariance is strictly negative for all sufficiently large \(n\), and its leading logarithmic coefficient has a genuine, albeit small, periodic modulation. The period averages are \(\int_0^1 A(\theta)\,d\theta=1/\ln2\) and
\(\int_0^1 B(\theta)\,d\theta=2/\ln2-\gamma/(2(\ln2)^2)\), with \(\gamma\) Euler's constant. The error \(o(1)\) is absolute, not merely small relative to \(\log n\).

## Assumptions and scope

Every ordered composition of \(n\ge1\) has probability \(2^{-(n-1)}\). A part size is counted once in \(D_n\) irrespective of multiplicity. All logarithms with base two are indicated by \(\log_2\); \(\ln\) is the natural logarithm. The theorem concerns the joint covariance of the two statistics on the *same* uniformly sampled composition. The asymptotic variable \(n\) ranges over all positive integers without restrictions to dyadic subsequences.

## Proof

**1. Cut-variable influence identity.** Write a composition using independent, fair separator bits \(X_1,\ldots,X_{n-1}\), with an obligatory terminal separator. Then \(K_n=1+\sum_iX_i\), so for any function \(F\) of the bits,

\[
 \operatorname{Cov}(K_n,F)
 =\frac14\sum_{i=1}^{n-1}
 \mathbb E\bigl[F(X^{i=1})-F(X^{i=0})\bigr]. \tag{1}
\]

Here \(X^{i=a}\) denotes replacement of the \(i\)-th separator bit by \(a\) while all other bits stay fixed. When the cut at \(i\) is inserted, its parent part of length \(A_i+B_i\) splits into lengths \(A_i\) and \(B_i\). Let \(E_{i,j}\) be the event that some *other, unchanged* part has size \(j\). The contribution from size \(j\) is exactly

\[
 \Delta_{i,j}={\bf1}_{E_{i,j}^{c}}
 \bigl({\bf1}_{A_i=j}+{\bf1}_{B_i=j}
       -{\bf1}_{A_i=B_i=j}-{\bf1}_{A_i+B_i=j}\bigr). \tag{2}
\]

Thus \(\operatorname{Cov}(K_n,D_n)=\frac14\sum_i\sum_j\mathbb E\Delta_{i,j}\). The subtraction for \(A_i=B_i=j\) ensures that a duplicated new size is only counted once.

**2. Rare-size void approximation with quantitative error.** Put \(L=\log_2n\), \(M=\lceil4L\rceil\), and \(t_j=n2^{-j-1}\). We use the elementary independent-cut representation together with the standard dependency-neighborhood Poisson void estimate (Arratia–Goldstein–Gordon, Theorem 1). For a family of Bernoulli occurrences with mean \(\lambda\), and dependency-neighborhood sums \(b_1,b_2\) with no dependence outside each neighborhood, that estimate gives

\[
 \bigl|\mathbb P(W=0)-e^{-\lambda}\bigr|
 \le (1\wedge\lambda^{-1})(b_1+b_2). \tag{3}
\]

A complete, unaffected part of length \(j\) corresponds to the binary word consisting of a cut, then \(j-1\) noncuts, then a cut. In an interior fair-bit region it has probability \(2^{-j-1}\). Two such words at starting-site displacement \(d\) have zero intersection when \(1\le d<j\), share exactly one cut when \(d=j\), and are independent at larger displacement. Hence the dependency-neighborhood terms for \(O(n)\) candidate positions satisfy \(b_1=O(nj4^{-j})\), \(b_2=O(n4^{-j})\), with constants uniform in \(j\). The mean is \(t_j+O((j+M)2^{-j})\) after deleting a neighborhood of \(O(j+M)\) sites near \(i\). The removed word occurrences corresponding to *other* parts have total probability \(O((j+M)2^{-j})\), uniformly conditional on \(A_i,B_i\le M\): forced nearby cuts can remove at most one random bit from an otherwise unchanged part word, and the affected parent or its children are excluded by definition. All retained word indicators are functions of bits disjoint from those determining \(A_i,B_i\).

Consequently, for \(\lceil3L/4\rceil\le j\le\lfloor2L\rfloor\), \(2M<i<n-2M\), and \(A_i,B_i\le M\),

\[
 \bigl|\mathbb P(E_{i,j}^{c}\mid A_i,B_i)-e^{-t_j}\bigr|
 \le C(j+M)2^{-j}. \tag{4}
\]

To see the rate explicitly, (3) bounds the independent-region void error by \(O(j2^{-j})\), since \((1\wedge\lambda^{-1})n4^{-j}\le C2^{-j}\) for \(\lambda\asymp n2^{-j}\). Terms from the deleted region and the mean adjustment give the remaining \(O((j+M)2^{-j})\). Excluding \(A_i>M\) or \(B_i>M\) costs at most \(O(2^{-M})\) per site. By the geometric-run distribution, for interior sites

\[
 \mathbb P(A_i=j)=\mathbb P(B_i=j)=2^{-j},\quad
 \mathbb P(A_i+B_i=j)=(j-1)2^{-j},\quad
 \mathbb P(A_i=B_i=j)=4^{-j}. \tag{5}
\]

Using (2), (4), and (5), uniformly in the stated central-size window,

\[
 \mathbb E\Delta_{i,j}
 =e^{-t_j}\bigl((3-j)2^{-j}-4^{-j}\bigr)
   +O\!\left(j(j+M)4^{-j}+2^{-M}\right). \tag{6}
\]

The sum over all \(n\) sites of this error is \(O(n^{-1/2}(\log n)^3)+O(n2^{-M}\log n)=o(1)\). There are only \(O(M)\) excluded boundary sites; their total contribution in the central-size window is \(O(M(\log n)2^{-3L/4})=o(1)\).

For smaller sizes \(j<3L/4\), one can select \(\Omega(n/(j+1))\) disjoint length-\(j+1\) word locations well away from the modified cut. Each has independent success probability \(2^{-j-1}\); therefore the absence of every other size-\(j\) part has probability at most \(\exp[-c n2^{-j}/(j+1)]\). Summing all small-size contributions in (1) gives \(o(1)\). For \(j>2L\), the union bound \(\mathbb E|\Delta_{i,j}|\le C(j+1)2^{-j}\) gives a total at most \(O(n\sum_{j>2L}(j+1)2^{-j})=O((\log n)/n)=o(1)\). The exceptional duplicate term \(4^{-j}\) in (6) contributes \(o(1)\) after summing over central sizes and sites. We conclude

\[
 \operatorname{Cov}(K_n,D_n)
 =\frac12\sum_{j\ge1}(3-j)t_j e^{-t_j}+o(1). \tag{7}
\]

**3. Lattice rescaling and periodicity.** Write \(q=\lfloor L\rfloor\), \(j=q+k\), \(\theta=L-q\). Then \(t_j=2^{\theta-k-1}=u_k(\theta)\). The lower limit \(k\ge1-q\) may be extended to all of \(\mathbb Z\) with error \(o(1)\), because \(u e^{-u}\) decays exponentially at small \(u\) and superexponentially at large \(u\), even after multiplication by \(|\log u|\). Since \(3-j=4-L+\log_2u_k(\theta)\), equation (7) becomes the asserted \(-LA(\theta)/2+B(\theta)+o(1)\). The series and all derivatives converge locally uniformly, and shifting \(\theta\) by one simply reindexes \(k\).

For the Fourier coefficient of \(A\), substitute \(u=2^{\theta-k-1}\) in the period integral; the Mellin integral evaluates to \(\Gamma(1-2\pi i\ell/\ln2)/\ln2\). Euler's Gamma function has no zeros, so the first nonzero-frequency coefficient does not vanish: \(A\) is genuinely nonconstant. The period mean of \(B\) follows by integrating \(\ln u\,e^{-u}\), which equals \(-\gamma\). Because \(A\) is positive and continuous on a compact period, its minimum is positive, proving eventual strict negativity.

## Verification

The stand-alone file `artifacts/verify.py` uses exact integer recurrences and a separate direct enumeration. If \(q_t(j)\) is the number of compositions of \(t\) having no part of size \(j\), and \(s_t(j)\) the total number of their parts, then \(q_0(j)=1\), \(s_0(j)=0\), and

\[
 q_t(j)=\sum_{\substack{1\le h\le t\\h\ne j}}q_{t-h}(j),\qquad
 s_t(j)=\sum_{\substack{1\le h\le t\\h\ne j}}
       \bigl(s_{t-h}(j)+q_{t-h}(j)\bigr).
\]

Consequently the exact finite-size identity

\[
 \operatorname{Cov}(K_n,D_n)
 =2^{1-n}\sum_{j=1}^{n}
 \left(\frac{n+1}{2}q_n(j)-s_n(j)\right)
\]

follows from expressing \(D_n\) as the sum of indicators of the presence of each part size. This identity was checked against direct enumeration for \(1\le n\le12\), and the implementation computes additional exact and asymptotic checks. The tests do not substitute for the analytic argument in the proof.

## Relationship to prior work

Hwang–Yeh provide a broad occupancy-frequency generating function and detailed mean asymptotics for the number of distinct sizes in compositions. Hitczenko–Stengle derive an explicit periodically fluctuating mean. Hitczenko–Louchard analyze the distribution and moments of distinctness, typically replacing the random part count with a concentrated number of independent geometric samples. Bender–Canfield study numerous statistics of locally restricted compositions, including number of parts and first-order distinct-size behavior. Their machinery may encode related mixed moments, but the specific joint covariance and its two-term log-periodic expansion are not among the inspected conclusions. Finch's separate covariance problem concerns the **maximum** part size rather than the **number of distinct** part sizes. The novel contribution claimed here is only the two-term mixed covariance expansion and its nonconstant leading coefficient; the composition representation, the marked generating functions, and the rare-pattern approximation theorem are established ingredients.

## Limitations

The result is asymptotic: it does not assert a complete finite-\(n\) sign classification. The periodic fluctuation has small amplitude, and ordinary numerical regressions could mistake it for a constant. The exact recurrences allow finite checks but do not prove the infinite asymptotic by themselves. Existing general generating functions could imply the covariance after nontrivial differentiation and uniform asymptotic analysis; complete historical priority is not certified. An independent assessment of the proof and literature comparison has not been performed.

## References

1. H.-K. Hwang and Y.-N. Yeh, *Measures of Distinctness for Random Partitions and Compositions of an Integer*, Advances in Applied Mathematics 19 (1997), 378–414. DOI: 10.1006/aama.1997.0555. Full text: https://mathweb.ucsd.edu/~ebender/comp.papers/102-distinct_parts.pdf
2. P. Hitczenko and G. Stengle, *Expected Number of Distinct Part Sizes in a Random Integer Composition*, Combinatorics, Probability and Computing 9 (2000), 519–527. DOI: 10.1017/S0963548300004399. Public online version: 2001-04-09. Open preprint: https://arxiv.org/abs/math/0110189
3. P. Hitczenko and G. Louchard, *Distinctness of Compositions of an Integer: A Probabilistic Analysis*, Random Structures & Algorithms 19 (2001), 407–437. DOI: 10.1002/rsa.10008. Full text: https://mathweb.ucsd.edu/~ebender/comp.papers/93-distinct_parts.pdf
4. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics 12 (2005), #R57. DOI: 10.37236/1954.
5. R. Arratia, L. Goldstein, and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25. DOI: 10.1214/aop/1176991491.
6. S. Finch, *Covariance within Random Integer Compositions*, 2020 preprint, https://arxiv.org/abs/2010.06643.

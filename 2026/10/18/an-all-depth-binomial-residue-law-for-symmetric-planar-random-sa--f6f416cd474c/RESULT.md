# An all-depth binomial-residue law for symmetric planar random samples

## Finding

Let \(n\ge2\), and let \(X_1,\ldots,X_n\in\mathbb R^2\setminus\{0\}\) be **independent**, not necessarily identically distributed, random vectors. Assume that each \(X_i\) and \(-X_i\) have the same law and that, with probability one, no two vectors are collinear. Write the (unnormalized) empirical halfspace depth of the origin as
\[
D_n=\min_{u\in\mathbb S^1}\#\{i:u\cdot X_i\ge0\}.
\]
For every integer \(1\le r\le\lfloor n/2\rfloor\), let \(h=n-2r+2\). The complete exact tail law is
\[
\boxed{\mathbb P(D_n\ge r)=1-\frac{h}{2^n}
\sum_{\substack{0\le j\le n\\j\equiv r-1\pmod h}}\binom nj.}
\]
In addition, \(\mathbb P(D_n\ge r)=0\) when \(r>\lfloor n/2\rfloor\) and equals one for \(r\le0\). Consequently the entire distribution is independent of the underlying centrally symmetric planar laws, even for heterogeneous samples. The threshold event equals coverage of every open semicircle by at least \(r\) directional points (almost surely).

For \(n\ge2\), \(\mathbb P(D_n\ge1)=1-2n/2^n\) (the planar Wendel probability). For \(n\ge5\), \(\mathbb P(D_n\ge2)=1-2n(n-2)/2^n\). The case \(r=2\) is also a precise probability of the directed spanning-set condition for a zero-bias planar ReLU layer with independent centrally symmetric general-position weight rows; the general law determines the full active-row margin rather than merely injectivity.

## Assumptions and scope

Independence and individual antipodal symmetry are essential to the argument. The no-collinearity hypothesis means \(\mathbb P\{\det(X_i,X_j)=0\}=0\) for every \(i\ne j\); it holds for independent vectors having planar densities. The radii may be arbitrary, and the unoriented projective angles need not be uniform or independent after sorting. The theorem includes nonspherical and nonidentical distributions. Depth is unnormalized and uses **closed** halfspaces. Almost surely there is at most one sample vector orthogonal to a chosen unit normal, so the global minimum over closed halfspaces agrees with the minimum over generic normals containing no boundary observations; thus either halfplane boundary convention yields the same minimum.

## Proof

**Step 1 (conditional fair signs).** Choose a measurable representative of every unoriented line by its argument in \([0,\pi)\). Let \(\vartheta_i\in[0,\pi)\) denote the unoriented line angle of \(X_i\), and write its oriented direction as \(\varepsilon_i(\cos\vartheta_i,\sin\vartheta_i)\), with \(\varepsilon_i\in\{-1,+1\}\). Antipodal symmetry implies \(\mathbb P(\varepsilon_i=1\mid\vartheta_i)=1/2\). Independence of the vectors then makes the signs conditionally independent fair coins, given all projective angles and radial information. Sorting by the distinct projective angles merely permutes these fair coins. Thus, conditional on all unoriented geometric data, the ordered signs are independent and uniform on \(\{-1,+1\}^n\).

**Step 2 (walk representation).** Write the ordered signs as \(\varepsilon_1,\ldots,\varepsilon_n\), their partial sums as \(S_j=\sum_{i=1}^j\varepsilon_i\) with \(S_0=0\), and \(S=S_n\). In one reference open semicircle the positive points are exactly the positive signs. Move the window across the \(n\) projective angles, so the first \(j\) signs exchange membership between the window and its antipodal complement. Its point count is
\[
C_j=\frac{n+S}{2}-S_j,\qquad j=0,1,\ldots,n.
\]
The antipodal complementary window has count \(n-C_j\). These are all distinct generic semicircle counts up to repetition. Hence
\[
D_n=\min_{0\le j\le n}\min(C_j,n-C_j)
=\frac{n-\max_{0\le j\le n}|S-2S_j|}{2}.
\]
The almost-sure absence of collinear pairs ensures a boundary direction cannot create a smaller closed-halfspace count; at a boundary one point is included while the adjacent generic count on one side is already as small or smaller.

**Step 3 (two absorbing barriers).** Fix a signed-walk endpoint \(S=s\), with \(s\equiv n\pmod2\). Put \(w=n-2r\ge0\). The event \(D_n\ge r\) is precisely \(|s-2S_j|\le w\) for every \(j\). It is impossible unless \(-w\le s\le w\). Otherwise it confines the simple walk \(S_j\) to the integer interval \([\tfrac{s-w}{2},\tfrac{s+w}{2}]\). Shift by \(1-(s-w)/2\), so it becomes a walk strictly between absorbing barriers at \(0\) and \(h=w+2\), starting at \(a=(h-s)/2\) and ending at \(b=(h+s)/2\). Notice that \(a+b=h\).

**Step 4 (reflection count).** The standard repeated-reflection principle for the length-\(n\) simple symmetric walk killed at \(0\) and \(h\) yields the exact number of admissible signed sequences with endpoint \(s\):
\[
N_n(s)=\sum_{k\in\mathbb Z}\left[\binom n{(n+s)/2+kh}-\binom n{n-r+1+kh}\right].
\]
Here and throughout, \(\binom nj=0\) for integer \(j\notin[0,n]\). For clarity, this is the difference of unrestricted walks from \(a\) to the images \(b+2kh\) and \(-b+2kh\), respectively; converting endpoint displacements to step counts gives the two displayed binomials. The identity also follows by odd extension at both barriers and induction on walk length, so it is not inferred from finite enumeration.

**Step 5 (sum over endpoints).** As \(s\) runs through \(-w,-w+2,\ldots,w\), the integers \((n+s)/2\) run through \(r,r+1,\ldots,n-r\), exactly \(h-1\) consecutive residue classes modulo \(h\). Their unique omitted residue class is \(r-1\pmod h\). The reflection term always has index \(n-r+1\equiv r-1\pmod h\), so summing \(N_n(s)\) over permitted endpoints gives
\[
2^n-h\sum_{\substack{0\le j\le n\\j\equiv r-1\pmod h}}\binom nj.
\]
All \(2^n\) sign strings are equally likely, also conditional on the unoriented geometry; division by \(2^n\) proves the claimed formula and its distribution-free validity. No continuity approximation is involved.

**Boundary cases.** For \(r>\lfloor n/2\rfloor\), antipodal halfspaces have counts summing to \(n\), forcing \(D_n<r\). The case \(r\le0\) is automatic. The result also holds for \(n=2\) and \(r=1\), where the formula gives probability zero.

## Verification

A standalone pure-Python script `verification.py` computes the residue-class binomial coefficient formula and independently enumerates every one of the \(2^n\) sign strings for each \(2\le n\le14\) and all relevant integer thresholds. It tests 85 exact equality identities, including Wendel's first-depth law and the two-depth polynomial. Execute with `python verification.py`. These checks are finite corroboration; the infinite family is proved in Steps 1–5.

## Relationship to prior work

Wendel's planar theorem supplies exactly the \(r=1\) specialization and already allows centrally symmetric distributions; it does **not**, by its stated implication alone, determine higher halfspace depths. Yuan's 2026 circular scan-statistic results treat **uniform** circular points and specifically the \(N-1\) and \(3\) scan thresholds at general arc lengths; this is related to low-depth semicircle coverage but does not state the entire distribution-free all-depth formula for heterogeneous antipodally symmetric samples. Fojtík–Laketa–Mozharovskyi–Nagy study algorithms for computing realized Tukey central regions, not probability laws over random symmetric samples. Puthawala and coauthors identify the directed spanning-set criterion for ReLU injectivity but not the all-depth probability law. Xie's recent work addresses Gaussian ReLU injectivity at high-dimensional width thresholds; its full preprint was inaccessible for examination, so an implicit two-dimensional special-case formula cannot be excluded. These comparisons concern logical coverage, not merely differing titles. The classical two-sided random-walk reflection principle is used as a known lemma, not claimed as new.

## Limitations

The theorem does not cover dependent signs, samples lacking antipodal symmetry, directions with collinear pairs having positive probability, dimensions three and above, or any asymptotic relative-error expansion. It establishes no new theorem about nonzero biases or stability constants for ReLU networks. No claim is made that the uniform-circle \(r=1\) or \(r=2\) specializations are novel. Classical circular multiple-covering identities could contain an equivalent uniform-sample all-depth formula; the genuinely asserted scope is the exact all-depth law for independent possibly heterogeneous centrally symmetric planar vectors. The abstract-only accessibility of one relevant recent preprint and the possibility of differently named classical formulae remain originality risks. Independent validation has not been performed.

## References

1. H. Yuan, *Exact Closed-Form Formulae for Linear and Circular Continuous Scan Statistics*, arXiv:2604.25360, first posted 2026-04-28. https://arxiv.org/html/2604.25360v1
2. *The injectivity threshold of a Gaussian ReLU layer*, arXiv:2610.07492, first posted 2026-10-05. https://arxiv.org/abs/2610.07492
3. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111.
4. V. Fojtík, P. Laketa, P. Mozharovskyi, and S. Nagy, *On exact computation of Tukey depth central regions*, arXiv:2208.04587, first posted 2022-08-09. https://arxiv.org/html/2208.04587v2
5. M. Puthawala, K. Kothari, M. Lassas, I. Dokmanić, and M. de Hoop, *Globally Injective ReLU Networks*, Journal of Machine Learning Research 23 (2022), 1–55. https://jmlr.org/papers/volume23/21-0282/21-0282.pdf

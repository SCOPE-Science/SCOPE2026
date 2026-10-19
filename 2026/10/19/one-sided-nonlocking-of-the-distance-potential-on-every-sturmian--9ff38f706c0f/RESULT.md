# One-sided nonlocking of the distance potential on every Sturmian beta-shift

## Finding
Fix any irrational \(\alpha\in(0,1)\) and symbolic metric parameter \(\theta\in(0,1)\). In the Sturmian beta-shift \(Y_\alpha\), the potential \(-\Psi_\theta\), where \(\Psi_\theta(x)=d_\theta(x,X_\alpha)\) is distance to its Sturmian subsystem, has the unique maximizing invariant probability \(\mu_\alpha\). Nevertheless it has **zero locking radius** in the Lipschitz norm: for **every** \(t>0\), the potential
\[
G_t(x)=-\Psi_\theta(x)-t x_0
\]
is **not** maximized by \(\mu_\alpha\), even though \(\|G_t+\Psi_\theta\|_{\mathrm{Lip}}\le2t\). In fact, there are explicit periodic competitor measures \(\nu_k\) of periods less than twice the denominators \(q_k\) of infinitely many lower continued-fraction convergents to \(\alpha\), for which
\[
\int G_t\,d\nu_k-\int G_t\,d\mu_\alpha
\ge \frac{t}{2q_k^2}-\theta^{q_k-1}.
\]
Consequently this difference is positive for all sufficiently large such denominators. The exponential-versus-quadratic separation makes the loss of robustness quantitative, not merely topological.

## Assumptions and scope
Let \(\Sigma=\{0,1\}^{\mathbb N_0}\), with left shift \(\sigma\). For \(x\ne y\), put \(d_\theta(x,y)=\theta^{N(x,y)}\), where \(N(x,y)=\min\{j\ge0:x_j\ne y_j\}\), and put \(d_\theta(x,x)=0\). Let \(a_j(\alpha)=\lceil(j+1)\alpha\rceil-\lceil j\alpha\rceil\), \(\mathbf a(\alpha)=(a_j(\alpha))_{j\ge0}\), \(X_\alpha=\overline{\{\sigma^j\mathbf a(\alpha):j\ge0\}}\), and
\[
Y_\alpha=\{x\in\Sigma:\sigma^j x\le_{\rm lex}\mathbf a(\alpha)\ \text{for all}\ j\ge0\}.
\]
The Sturmian system \(X_\alpha\) is minimal and uniquely ergodic with invariant probability \(\mu_\alpha\), and \(X_\alpha\subseteq Y_\alpha\) (Huang–Jenkinson–Xu–Zhang, 2026). Set \(\Phi(x)=x_0\), \(\Psi_\theta(x)=\inf_{y\in X_\alpha}d_\theta(x,y)\), and use \(\|f\|_{\mathrm{Lip}}=\|f\|_\infty+\sup_{x\ne y}|f(x)-f(y)|/d_\theta(x,y)\). The claim concerns this precise function space, not the uniform topology alone or all nearby potentials.

## Proof
**1. A short-word stability lemma.** For a slope \(u\in(0,1)\) irrational or rational with denominator greater than \(m\), code circle rotation with upper mechanical words
\[
b_j(u,s)=\lceil s+(j+1)u\rceil-\lceil s+ju\rceil\quad(0\le j<m).
\]
The length-\(m\) language is determined by the circular order of the \(m+1\) discontinuity phases \(0,-u,\ldots,-mu\) modulo one. Their order changes only upon a collision \((i-j)u\in\mathbb Z\) with \(1\le|i-j|\le m\), i.e. at a reduced rational of denominator at most \(m\). At cutpoints, the ceiling convention yields one of the adjacent arc words. Therefore the complete length-\(m\) language is constant as the slope varies inside a connected component of \((0,1)\) minus those rationals. For irrational \(u\), varying the intercept runs through the shift-orbit closure \(X_u\); for rational \(u\), it runs through the finite shifts of its periodic upper mechanical sequence. This argument proves the lemma for both rational and irrational endpoints not lying at a collision.

**2. Arithmetic choice of periodic competitors.** Take an unbounded sequence of lower continued-fraction convergents \(p/q<\alpha\), where \(\gcd(p,q)=1\), \(0<\alpha-p/q<q^{-2}\), and the preceding convergent is an upper Farey neighbor of \(p/q\). For sufficiently large \(q\), \(1\le p<q\). Choose the unique \(s\in\{1,\ldots,q-1\}\) for which \(ps\equiv1\pmod q\), set \(r=(ps-1)/q\) and
\[
\beta=\frac{p+r}{q+s}<\frac pq<\alpha.
\]
The fractions \(r/s,p/q\) are Farey neighbors, as are \(\beta,p/q\), with
\[
\frac{p}{q}-\beta=\frac{1}{q(q+s)},\qquad
\frac{1}{2q^2}<\alpha-\beta<\frac{2}{q^2}.
\]
A reduced rational strictly between Farey neighbors with denominators \(a,b\) must have denominator at least \(a+b\). Hence the interval from \(\beta\) to \(p/q\) contains no rational with denominator \(<q\); the same holds from \(p/q\) to \(\alpha\), using the upper preceding convergent. By step 1, **every factor of length \(q-1\) of the periodic mechanical word of slope \(\beta\) occurs in \(X_\alpha\)**.

**3. Admissibility, distortion and the decisive comparison.** Write \(\mathbf a(\beta)\) for the periodic upper mechanical word of reduced slope \(\beta\); its period is \(q+s<2q\). For any shift \(j\ge0\) and length \(m\), telescoping the ceiling differences gives
\[
\sum_{i=0}^{m-1}a_{i+j}(\beta)
=\lceil(j+m)\beta\rceil-\lceil j\beta\rceil
\le\lceil m\beta\rceil
\le\lceil m\alpha\rceil.
\]
If \(\sigma^j\mathbf a(\beta)\) first differs from \(\mathbf a(\alpha)\) in position \(m-1\), their preceding digit sums are equal, and the displayed inequality excludes a competitor digit one when the reference digit is zero. Hence the first differing digit, if any, is zero for the competitor and one for the reference. Thus \(\sigma^j\mathbf a(\beta)\le_{\mathrm{lex}}\mathbf a(\alpha)\) and the whole periodic orbit lies in \(Y_\alpha\). Let \(\nu_\beta\) be its equally weighted orbit measure. Its frequency of digit one equals \(\beta\), so \(\int\Phi\,d\nu_\beta=\beta\), whereas \(\int\Phi\,d\mu_\alpha=\alpha\). By step 2, each shift has a length-\(q-1\) prefix occurring in \(X_\alpha\), whence
\[
0\le\int\Psi_\theta\,d\nu_\beta\le\theta^{q-1}.
\]
Consequently
\[
\int G_t\,d\nu_\beta-\int G_t\,d\mu_\alpha
=t(\alpha-\beta)-\int\Psi_\theta\,d\nu_\beta
>\frac{t}{2q^2}-\theta^{q-1}.
\]
For every fixed \(t>0\), the final expression is positive for all large enough lower convergent denominators.

**4. Uniqueness at the boundary and failure of locking.** Since \(\Psi_\theta\ge0\), its zero locus is exactly \(X_\alpha\), and the only invariant measure on that uniquely ergodic subsystem is \(\mu_\alpha\), the unique maximizing measure for \(-\Psi_\theta\) is \(\mu_\alpha\). Both \(\Phi\) and \(\Psi_\theta\) are Lipschitz with seminorm at most one, and \(\|\Phi\|_\infty=1\). Therefore \(\|G_t+\Psi_\theta\|_{\mathrm{Lip}}=\|t\Phi\|_{\mathrm{Lip}}\le2t\), which can be arbitrarily small. By step 3, none of these perturbations retains \(\mu_\alpha\) as maximizing. Thus \(-\Psi_\theta\) has zero locking radius.

## Verification
Run `python verify.py` using Python 3's standard library. The verifier checks continued-fraction/Farey identities, the lexicographic admissibility of finite shift prefixes, short-factor language inclusion, rational digit frequencies and the exponentially smaller distance bound for a concrete irrational golden-ratio slope across multiple denominators. These finite computations test implementation and critical conventions; the claims for every irrational slope and every sufficiently large denominator follow exclusively from the proof.

## Relationship to prior work
Huang, Jenkinson, Xu and Zhang (arXiv:2610.03619v1, Theorems A and C) prove an explicit open Lipschitz neighborhood with Sturmian maximizing measure around the *different* potential \(\Phi-\Psi_\theta\). This result studies the natural boundary potential \(-\Psi_\theta\) and supplies a uniform-in-slope construction of destabilizing periodic measures. The general two-parameter positive cone \(p\Phi-q\Psi_\theta\) appears in a published published-finding corpus finding; its hypothesis \(p>0\) does not cover the present \(p=0\) boundary. Mechanical-word, Farey-neighbor and Christoffel factor principles are established background, used here to obtain the exponential-vs-quadratic comparison; they are not claimed as new.

## Limitations
The result proves failure of *locking of the specific maximizing measure* at the exact distance potential, not an exact pressure function or a classification of all maximizers for the perturbed potential. Other formulas elsewhere may implicitly imply the same boundary result. No priority beyond the inspected comparison set or independent validation is asserted.

## References
1. W. Huang, O. Jenkinson, L. Xu, Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization*, arXiv:2610.03619v1 (first public 2026-10-02), especially Theorems A, C and the Sturmian definitions.
2. N. Carey and D. Clampitt, *Partitioned Factors in Christoffel and Sturmian Words*, arXiv:1804.08724 (2018), background on circular factors and rational mechanical words.
3. *A two-parameter robust cone of Sturmian-maximizing potentials*, published-finding corpus, record `2026/10/11/SCOPE-a-two-parameter-robust-cone-of-sturmian-maximizing-potentials--551b149cc657` (background positive-coefficient stability, not a boundary classification).
4. J.-P. Borel and C. Reutenauer, *On Christoffel classes*, RAIRO Theor. Inform. Appl. 40 (2006), 15–27, background on Christoffel conjugation classes.

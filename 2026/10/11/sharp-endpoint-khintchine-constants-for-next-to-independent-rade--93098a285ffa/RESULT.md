# Sharp endpoint Khintchine constants for next-to-independent Rademacher vectors

## Finding
For every even integer \(n\ge4\), every random vector \(\xi=(\xi_1,\ldots,\xi_n)\in\{-1,1\}^n\) having independent, fair coordinates on every proper subset, and
\[\theta=\mathbb E\prod_{i=1}^{n}\xi_i,\qquad -1\le\theta\le1,\]
the exact sharp inequality is
\[
\mathbb E\left|\sum_{i=1}^{n} a_i\xi_i\right|^n
\le
\frac{M_n+|\theta|n!}{n^{n/2}}
\left(\sum_{i=1}^{n} a_i^2\right)^{n/2},
\qquad
M_n=2^{-n}\sum_{j=0}^{n}\binom nj(n-2j)^n.
\]
For each fixed law and each nonzero coefficient vector, equality holds if and only if all coefficient magnitudes agree and are nonzero, with \(\operatorname{sgn}(\prod_i a_i)=\operatorname{sgn}(\theta)\) when \(\theta\ne0\). If \(\theta=0\), coefficient signs are unrestricted.

The hypothesis has a complete one-parameter classification: every such law is uniquely
\[\Pr(\xi=s)=2^{-n}\left(1+\theta\prod_{i=1}^{n}s_i\right)\quad(s\in\{-1,1\}^n),\]
with arbitrary \(\theta\in[-1,1]\). All moments of even orders strictly below \(n\) are those of independent fair signs. For \(\theta=1\), the moment constants at \(n=4,6,8\) are respectively \(4\), \(124/9\), and \(71\).

## Assumptions and scope
All coefficient vectors are real. The integer \(n\) is even and at least four. The sign vector is \((n-1)\)-wise independent with each marginal equally likely to be \(1\) or \(-1\). In particular \(\mathbb E\xi_i\xi_j=0\) for distinct coordinates, so
\[\mathbb E\left|\sum_i a_i\xi_i\right|^2=\sum_i a_i^2.\]
The displayed constant is an \(n\)-th power of the optimal \(L^n/L^2\) norm ratio, rather than the norm ratio itself; the latter equals the positive \(n\)-th root. The distribution is not assumed exchangeable under arbitrary coefficient-sign changes. No assumption of full mutual independence is made.

## Proof
**Step 1: classify the admissible laws.** On the sign cube, every probability mass function has the Fourier–Walsh inversion
\[\Pr(\xi=s)=2^{-n}\sum_{A\subseteq\{1,\ldots,n\}}\widehat\mu(A)\prod_{i\in A}s_i,\qquad \widehat\mu(A)=\mathbb E\prod_{i\in A}\xi_i.\]
For every nonempty proper \(A\), the independent fair marginals imply \(\widehat\mu(A)=0\). The empty coefficient equals one and the complete-set coefficient is \(\theta\). This proves the formula in the Finding. Its nonnegativity is equivalent to \(|\theta|\le1\), and every such parameter produces a legitimate law with the stipulated proper marginals.

**Step 2: the first surviving dependence term.** Let \(\varepsilon_i\) be independent fair signs. Walsh orthogonality gives, for every polynomial \(P\) in the sign coordinates,
\[\mathbb EP(\xi)=\mathbb EP(\varepsilon)+\theta\,\mathbb E\left[P(\varepsilon)\prod_i\varepsilon_i\right].\]
Take \(P(s)=(\sum_i a_is_i)^n\). After reducing sign powers modulo two, the product character can occur in this degree-\(n\) expansion only if each of the \(n\) coordinates occurs once. The multinomial coefficient is \(n!\). Hence
\[
\mathbb E\left(\sum_i a_i\xi_i\right)^n
=\mathbb E\left(\sum_i a_i\varepsilon_i\right)^n+\theta n!\prod_i a_i.
\tag{1}
\]
Because \(n\) is even, this is the required absolute moment. In any smaller even degree, the full-product character cannot occur, proving the lower-moment assertion.

**Step 3: strict equal-magnitude maximization of the independent term.** Fix \(S=\sum_i a_i^2>0\), write \(q_i=a_i^2\), and consider two coordinates \(i\ne j\). Conditional on the other signs, put \(Z=\sum_{\ell\ne i,j}a_\ell\varepsilon_\ell\), \(s=q_i+q_j\), and \(u=q_iq_j\). With \(n=2k\), independence and symmetry yield
\[
\mathbb E|Z+a_i\varepsilon_i+a_j\varepsilon_j|^{2k}
=\sum_{h=0}^{k}\binom{2k}{2h}\mathbb EZ^{2k-2h}
\frac{(s+2\sqrt u)^h+(s-2\sqrt u)^h}{2}.
\tag{2}
\]
For every integer \(h\ge0\), the final average is a polynomial in \(u\) with nonnegative coefficients: indeed
\[
\frac{(s+2\sqrt u)^h+(s-2\sqrt u)^h}{2}
=\sum_{r=0}^{\lfloor h/2\rfloor}\binom h{2r}s^{h-2r}(4u)^r.
\]
All factors \(\mathbb EZ^{2k-2h}\) in (2) are nonnegative. Since \(k\ge2\), the \(h=k\) term is strictly increasing in \(u\): its \(r=1\) coefficient is positive and \(\mathbb EZ^0=1\). Holding \(q_i+q_j=s\) fixed, replacing an unequal pair by \((s/2,s/2)\) strictly increases the independent moment. Compactness of the nonnegative \(q\)-simplex and this pairwise improvement show that its unique squared-magnitude maximizing vector is \(q_i=S/n\) for every \(i\). At that vector the independent moment is \(M_n(S/n)^{n/2}\), by the binomial distribution of the sum of \(n\) fair signs. Thus
\[\mathbb E\left|\sum_i a_i\varepsilon_i\right|^n\le M_n(S/n)^{n/2},\]
with equality precisely when all \(|a_i|=\sqrt{S/n}\).

**Step 4: sharp perturbation and equality.** Arithmetic–geometric mean gives \(|\prod_i a_i|\le(S/n)^{n/2}\), with equality precisely when the squared magnitudes are all equal and nonzero. Applying this and Step 3 to (1) proves the bound. Equal magnitudes and a coefficient-product sign aligned with \(\theta\) attain it; such choices exist for either sign of \(\theta\). For \(\theta=0\), any equal-magnitude sign pattern is extremal. Strictness in Step 3 gives necessity for every parameter.

**Step 5: even-cycle realization.** If \(\varepsilon_1,\ldots,\varepsilon_n\) are independent fair vertex signs on the even cycle, define edge characters \(\xi_i=\varepsilon_i\varepsilon_{i+1}\), reading indices cyclically. Then \(\prod_i\xi_i=1\). The edge-sign map has exactly two preimages for each parity-even sign vector, so the edge signs are uniform on that parity class, and their every proper subset is independent. In this case \(\theta=1\), and the theorem gives the exact endpoint moment norm of the edge-supported quadratic Walsh subspace. The four-cycle constant \(4\) is a previously accessible low-dimensional special case, not asserted to be new by itself.

## Verification
The standalone `verify.py` script is standard-library-only and verifies the identity (1), the sharp inequality and equality for rational values of \(\theta\), using exact `Fraction` arithmetic. It exhausts the \(2^n\) sign configurations for each sampled coefficient vector at \(n=4,6,8\), with 210 deterministic coefficient/parameter tests including equality cases. Running `python3 verify.py` returned `NEAR_INDEPENDENT_ENDPOINT_EXACT_OK 210` and `EVEN_CYCLE_CONSTANTS {4: '4', 6: '124/9', 8: '71'}`. The general proof is Steps 1–5 and does not depend on the finite test runs.

## Relationship to prior work
Pass and Spektor (2014) establish sharp fourth-moment behavior for exchangeable pairwise independent signs; their four-coordinate situation includes the known \(n=4\) endpoint of this theorem, but does not imply the all-even-dimension \((n-1)\)-wise classification. Pass and Spektor (2017) establish bounds for general \(k\)-wise independent Rademacher vectors and sharp results for \(k=2,3\); their interpolation estimate does not yield the exact constant and all coefficient extremizers here for \(n\ge6\). Spektor (2016) conditions signs on a zero sum, a different probability law from conditioning on the sign product. The new result is the exact last-independence-level endpoint at moment order \(n\), including arbitrary full-product interaction \(\theta\), not a general improvement to the classical independent-sign Khintchine inequality.

## Limitations
The claim is for real coefficients, even \(n\ge4\), and moment order exactly \(n\); it does not classify sharp non-even moments, unequal marginals, or arbitrary lower independence levels. An equivalent formulation in historical moment-inequality literature cannot be excluded by the searches undertaken. The 2017 paper is later supporting literature, not the date of the motivating 2014 source. No independent mathematical audit has been performed.

## References
1. B. Pass and S. Spektor, *On Khinchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859v1 (first posted 25 December 2014), https://arxiv.org/html/1412.7859v1 .
2. B. Pass and S. Spektor, *On Khintchine type inequalities for k-wise independent Rademacher random variables*, arXiv:1708.08775v1 (2017), https://arxiv.org/html/1708.08775v1 .
3. S. Spektor, *Restricted Khinchine Inequality*, Canadian Mathematical Bulletin 59 (2016), 204–210, doi:10.4153/CMB-2015-047-8 .
4. U. Haagerup, *The best constants in the Khintchine inequality*, Studia Mathematica 70 (1981), 231–283, doi:10.4064/sm-70-3-231-283 .

# Gaussian deficiencies and Poisson overlap corrections in random rook-monoid products

## Finding
Let \(I_n\) be the symmetric inverse monoid of all injective partial transformations of \([n]=\{1,\ldots,n\}\). Fix an integer \(m\ge1\), independently choose uniformly distributed \(X_1,\ldots,X_m\in I_n\), and compose them in this order. Put
\[
D_j=n-\operatorname{rank}(X_j),\qquad
S_j=n-\operatorname{rank}(X_j\circ\cdots\circ X_1),\qquad
H_j=S_{j-1}+D_j-S_j\quad(j\ge2).
\]
The nonnegative integer \(H_j\) measures an overlap between previously omitted image points and the missing domain of the next factor; it is not the rank lost during that multiplication.

**Exact finite law.** Write
\[
L_n(-a)=\sum_{d=0}^n\binom nd\frac{a^d}{d!}.
\]
Independently for all \(j\),
\[
\Pr(D_j=d)=\frac{\binom nd/d!}{L_n(-1)}\quad(0\le d\le n).
\]
Conditional on the previous factors and \(D_j=d\), writing \(s=S_{j-1}\), the full transition is
\[
\Pr(H_j=h\mid S_{j-1}=s,D_j=d)
=\frac{\binom{s}{h}\binom{n-s}{d-h}}{\binom nd},
\quad S_j=s+d-h,
\]
for \(\max\{0,s+d-n\}\le h\le\min\{s,d\}\), and zero otherwise. These two formulas give an explicit finite recursion for the entire joint distribution of the ranks and overlap corrections, at every \(n\ge1\) and \(m\ge1\).

**Multiscale limit.** As \(n\to\infty\), for every fixed \(m\),
\[
\left(\left(\frac{D_j-\sqrt n}{n^{1/4}}\right)_{j=1}^m,
(H_j)_{j=2}^m\right)
\Longrightarrow
\left((G_j)_{j=1}^m,(Z_j)_{j=2}^m\right),
\]
where the variables on the right are *mutually independent*, \(G_j\sim\mathcal N(0,1/2)\), and \(Z_j\sim\operatorname{Pois}(j-1)\). In particular, defining the total overlap
\[
C_m=\sum_{j=2}^m H_j=\sum_{j=1}^mD_j-S_m,
\]
one obtains the jointly independent limits
\[
\left(C_m,\frac{S_m-m\sqrt n}{n^{1/4}}\right)
\Longrightarrow
\left(\operatorname{Pois}\left(\binom m2\right),\mathcal N(0,m/2)\right).
\]
This includes the conventional degenerate zero-Poisson variable when \(m=1\).

**Exact expectation and its second-order term.** Let \(\mu_n=\mathbb E D_j\). Then
\[
\mu_n=\sqrt n-\frac34+O(n^{-1/2}),\qquad
\mathbb E\operatorname{rank}(X_m\circ\cdots\circ X_1)
=n\left(1-\frac{\mu_n}{n}\right)^m
=n-m\sqrt n+\frac{3m}{4}+\binom m2+O_m(n^{-1/2}).
\]
All error bounds in the asymptotic statements fix \(m\); no assertion is made for \(m\) increasing with \(n\).

## Assumptions and scope
The monoid includes the empty partial bijection and full permutations, and every element receives equal sampling weight. Rank is domain cardinality. The product is ordinary composition, with \(X_1\) applied first. The full range is arbitrary integers \(n\ge1\), fixed integers \(m\ge1\), and all admissible integer deficiencies and overlaps. The asymptotic variables at different \(n\) need not be coupled on one probability space. No claims about arbitrary noninjective transformations or rank-weighted sampling are included.

## Proof
**1. Exact one-factor law and conditional composition.** Rank-\((n-d)\) partial bijections number
\[
\binom n{n-d}^{\!2}(n-d)!=n!\binom nd/d!.
\]
Dividing by \(|I_n|=n!L_n(-1)\) gives the deficiency law. Let \(Y=X_{j-1}\circ\cdots\circ X_1\), whose image consists of \(n-s\) points, and let \(M_j=[n]\setminus\operatorname{dom}(X_j)\), a uniformly random \(d\)-set conditional on \(D_j=d\). Then
\[
\operatorname{rank}(X_j\circ Y)=|\operatorname{im}Y\setminus M_j|,
\qquad
S_j=s+d-|M_j\cap([n]\setminus\operatorname{im}Y)|.
\]
Therefore \(H_j=|M_j\cap([n]\setminus\operatorname{im}Y)|\). The latter is hypergeometric with population \(n\), marked population \(s\), and sample size \(d\). Choosing the marked and unmarked elements of \(M_j\) gives the stated transition. This also shows that the formula depends on the earlier factors only through \(s\).

An exact integer (unnormalized) transition from a state with deficiency \(s\) and current overlap total \(c\) to deficiency \(s+d-h\) and total \(c+h\) has multiplicity
\[
\frac{n!}{d!}\binom{s}{h}\binom{n-s}{d-h}.
\]
Thus the recursion can be evaluated using integer arithmetic without factorially many explicit products.

**2. Gaussian one-factor scale.** The defect weights \(w_n(d)=\binom nd/d!\) have adjacent ratio
\[
\frac{w_n(d+1)}{w_n(d)}=\frac{n-d}{(d+1)^2}.
\]
They are strictly log-concave and concentrate around \(\sqrt n\). For a quantified central limit theorem, use the classical positive-argument Perron expansion for the Laguerre polynomial evaluated at negative argument: locally uniformly for \(a\) in a complex neighborhood of each fixed \(a>0\),
\[
L_n(-a)=\frac{e^{-a/2}}{2\sqrt\pi\,(an)^{1/4}}e^{2\sqrt{an}}
\bigl(1+O_a(n^{-1/2})\bigr).
\]
Here \(L_n\) is the ordinary Laguerre polynomial, and local uniformity permits analytic differentiation of the logarithm. In the moment-generating identity
\[
\mathbb E e^{tD_j}=\frac{L_n(-e^t)}{L_n(-1)},
\]
substitute \(t=u/n^{1/4}\), subtract \(u\sqrt n/n^{1/4}\), and expand \(2\sqrt n(e^{u/(2n^{1/4})}-1)\). The surviving term is \(u^2/4\), the log moment-generating function of \(\mathcal N(0,1/2)\); the residual terms vanish locally uniformly in \(u\). In particular \(D_j/\sqrt n\to1\) in probability. The independent factors therefore have independent Gaussian limits. Differentiation at \(a=1\) yields
\[
\mu_n=\left.a\frac{d}{da}\log L_n(-a)\right|_{a=1}
=\sqrt n-\frac12-\frac14+O(n^{-1/2}),
\]
proving the stated mean expansion. The known single-factor Laguerre asymptotic is an input, not an independently claimed discovery.

**3. Conditional Poisson overlaps and independence.** For any integer \(r\ge1\), the conditional falling-factorial moment of the hypergeometric variable is exactly
\[
\mathbb E\bigl[(H_j)_r\mid S_{j-1}=s,D_j=d\bigr]
=\frac{(s)_r(d)_r}{(n)_r}.
\]
Suppose inductively that \(S_{j-1}/\sqrt n\to j-1\) in probability. Together with \(D_j/\sqrt n\to1\), the conditional moments converge in probability to \((j-1)^r\). The first conditional moment is uniformly bounded on typical \(s,d=O(\sqrt n)\) sets; all higher fixed moments likewise are bounded there. Conditional factorial-moment convergence and uniqueness of the Poisson law imply that the conditional laws of \(H_j\) converge to \(\operatorname{Pois}(j-1)\), uniformly on sets where \(s/\sqrt n\to j-1\) and \(d/\sqrt n\to1\). This uniform conditional convergence makes \(H_j\) asymptotically independent of all earlier factors and of the centered and scaled \(D_j\); applying it successively proves joint independence of every Gaussian and Poisson coordinate. Because \(H_j=O_{\mathsf P}(1)\), the relation \(S_j=S_{j-1}+D_j-H_j\) closes the induction and shows \(S_j/\sqrt n\to j\).

Summing the independent Poisson limits gives total intensity \(\sum_{j=2}^m(j-1)=\binom m2\). Dividing \(S_m=\sum_jD_j-\sum_{j\ge2}H_j\) by \(n^{1/4}\) gives the independent normal limit with variance \(m/2\).

**4. Expected product rank.** Conditional on a previous partial product having image size \(r\), an independent uniform next factor with defect \(D_j=d\) retains an expected \(r(1-d/n)\) points. Consequently the expected rank is multiplied by \(1-\mu_n/n\) at each step, starting from rank \(n\) for the identity product. The exact formula and binomial expansion (with fixed \(m\)) give the second-order rank expectation displayed above.

## Verification
The accompanying `verify.py` independently enumerates actual partial injections and explicitly composes them for eight small parameter pairs, with up to \(1{,}336{,}336\) ordered tuples in one case. It separately implements the exact integer transition using binomial coefficients, checks the full two-dimensional histograms of product deficiency and accumulated overlap for all eight cases, confirms the exact mean identity with cross-multiplied integers, and evaluates single-factor deficiency means at three larger sizes as an asymptotic sanity check. Run `python3 verify.py` with Python's standard library. A successful run ends with `VERIFY_OK 8 exhaustive direct-composition cases`. These finite tests do not prove the infinite-dimensional convergence; the conditional-moment and Laguerre arguments above do.

## Relationship to prior work
The classical rook-number identity \(|I_n|=\sum_r\binom nr^2r!\) and the associated Laguerre asymptotics are established facts. Gouyou-Beauchamps and Nicaud discuss the typical rank of one uniformly sampled partial injection. Fikioris and Fikioris examine products in a restricted consecutive-diagonal rook submonoid, rather than independent uniform products in the entire symmetric inverse monoid. Elliott, Levine, and Mitchell enumerate monogenic inverse monoids, which concerns powers and generated substructures of one element rather than independent products. The present result instead treats the exact multi-factor rank transition jointly with its asymptotically independent discrete overlap process and Gaussian defect fluctuations. Similarity to general hypergeometric intersection and random-occupancy limits is acknowledged; the specific synthesis and full distribution could still occur in literature not found by the searches.

## Limitations
Publication priority is provisional. This is a best-knowledge originality assessment, not a claim of complete historical uniqueness. The individual-rank Laguerre formula and hypergeometric-to-Poisson convergence are standard ingredients; what is asserted as the contribution is their exact and joint multi-factor product-rank formulation. The theorem fixes \(m\) and uses unweighted uniform sampling on the full rook monoid. A more general random semigroup convolution theorem could imply some or all of the results. No independent mathematical audit has been performed.

## References
1. P. Fikioris and G. Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496v1 (public February 19, 2023); open-access full text.
2. J. Elliott, M. Levine, and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387v1 (March 22, 2023); full text.
3. D. Gouyou-Beauchamps and C. Nicaud, *Random Generation Using Binomial Approximations*, 2010; particularly the enumeration of uniformly sampled partial injections in Section 4.
4. NIST Digital Library of Mathematical Functions, Chapter 18, classical Laguerre asymptotics and generating functions.

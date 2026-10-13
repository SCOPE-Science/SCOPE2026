# Critical Rényi-index transition in balanced twin-Fock entanglement

## Finding
For each integer \(n\ge1\), inject \(n\) indistinguishable photons into each port of an ideal lossless balanced two-mode beam splitter. Let \(\rho_n\) be the pure output state and \(\sigma_n\) either one-mode reduced state. For real \(q>0\), write \(F_n(q)=\operatorname{Tr}\sigma_n^q\). Define
\[
a_m=4^{-m}\binom{2m}{m},\qquad L(q)=\sum_{m=0}^{\infty}a_m^q\quad(q>2).\]
The complete finite-size moment-spectrum transition is
\[
\lim_{n\to\infty}n^{q-1}F_n(q)=\pi^{-q}B(1-q/2,1-q/2)\qquad(0<q<2),
\]
\[
\lim_{n\to\infty}\frac{nF_n(2)}{\log n}=\frac{2}{\pi^2},
\qquad
\lim_{n\to\infty}n^{q/2}F_n(q)=2\pi^{-q/2}L(q)\qquad(q>2).
\]
All three limits are strictly positive and finite in their stated ranges. The transition occurs at the Rényi order \(q=2\): the bulk supplies the leading moments below it, both edges above it, and a logarithmic divergence at the critical order. The weights of \(\sigma_n\) are exactly the symmetric beta-binomial law with parameters \((1/2,1/2)\).

With natural logarithms, the reduced von Neumann entropy and pure-state logarithmic negativity satisfy
\[
S(\sigma_n)=\log n+\log(\pi/4)+o(1),\qquad
E_{\mathcal N}(\rho_n)=\log n+\log\!\left(\frac{4\Gamma(3/4)^4}{\pi^2}\right)+o(1).
\]
In particular, defining unnormalized partial-transpose negativity \(\mathcal N_*(\rho_n)=\|\rho_n^{T_B}\|_1-1\),
\[
\lim_{n\to\infty}\frac{\mathcal N_*(\rho_n)}n=\frac{4\Gamma(3/4)^4}{\pi^2}.
\]
The largest Schmidt weight is \(a_n\), so the min-entropy is \(S_\infty(\sigma_n)=\tfrac12\log n+\tfrac12\log\pi+o(1)\). These are properties of mode bipartition entanglement; they are not claims about particle entanglement.

## Assumptions and scope
The two bosonic modes obey \([a,a^\dagger]=[b,b^\dagger]=1\) and commute with each other. Input \(|n,n\rangle=(a^\dagger)^n(b^\dagger)^n|0,0\rangle/n!\). The beam splitter acts on creation operators as \(a^\dagger\mapsto(c^\dagger+d^\dagger)/\sqrt2\) and \(b^\dagger\mapsto(c^\dagger-d^\dagger)/\sqrt2\); a physical alternative sign or phase convention gives the same eigenvalues. No absorption, mode mismatch, postselection or ancillary modes are present. The Rényi order \(q\) is fixed as \(n\to\infty\), not allowed to approach the critical value with \(n\). \(B\) denotes Euler's beta function. The subsystems are the two outgoing field modes, and \(T_B\) is transpose in their photon-number basis.

## Proof
**Exact Schmidt spectrum.** Commutativity and factorization give
\[
U|n,n\rangle=\frac{(c^{\dagger 2}-d^{\dagger 2})^n}{2^n n!}|0,0\rangle
=\sum_{k=0}^n(-1)^{n-k}\frac{\binom nk\sqrt{(2k)!(2n-2k)!}}{2^n n!}|2k,2n-2k\rangle.
\]
Distinct \(k\) have orthogonal local photon-number labels on both sides, so this is already a Schmidt decomposition up to phases. Its squared coefficients are
\[
p_{n,k}=\frac{\binom nk^2(2k)!(2n-2k)!}{4^n(n!)^2}=a_k a_{n-k}.
\]
The generating series \(\sum_{m\ge0}a_m z^m=(1-z)^{-1/2}\) implies \(\sum_{k=0}^n p_{n,k}=1\). Equivalently, using \(a_m=\Gamma(m+1/2)/(\sqrt\pi\,\Gamma(m+1))\), the spectrum is the beta-binomial probability mass function with both beta parameters equal to \(1/2\). Therefore \(F_n(q)=\sum_{k=0}^n(a_k a_{n-k})^q\).

**Bulk orders.** Stirling's formula with a fixed-parameter remainder gives \(a_m=(\pi m)^{-1/2}(1+O(m^{-1}))\) for \(m\ge1\), and constants \(c,C>0\) satisfy \(c(m+1)^{-1/2}\le a_m\le C(m+1)^{-1/2}\) for every integer \(m\ge0\). Thus for \(0<x<1\), \(n p_{n,\lfloor nx\rfloor}\to f(x)=1/(\pi\sqrt{x(1-x)})\). For fixed \(0<q<2\), Riemann summation on any compact subinterval of \((0,1)\) yields the integral \(\int f^q\), while the two omitted endpoint portions after scaling by \(n^{q-1}\) are bounded by constants times \(\delta^{1-q/2}\) (or smaller terms) for endpoint width \(\delta n\). This follows by bounding the half-range summands by \(C_qn^{-q/2}(k+1)^{-q/2}\) and summing. Taking \(\delta\downarrow0\) proves the first displayed limit, because \(\int_0^1 f(x)^qdx=\pi^{-q}B(1-q/2,1-q/2)\).

**Critical order.** From the same Stirling estimate, \(a_k^2=(\pi k)^{-1}+O(k^{-2})\) for \(k\ge1\). Consequently \(\sum_{k=0}^m a_k^2=(\log m)/\pi+O(1)\). On \(0\le k\le n/2\), uniformly \(a_{n-k}^2=(\pi n)^{-1}(1+O((k+1)/n))\). Its replacement by \((\pi n)^{-1}\) contributes at most \(O(n^{-1})\) in total because \(n^{-2}\sum_{k\le n/2}(k+1)a_k^2=O(n^{-1})\). By reflection \(k\leftrightarrow n-k\) and subtracting the possible doubly counted midpoint, \(F_n(2)=2(\log n)/(\pi^2n)+O(n^{-1})\), proving the critical claim.

**Edge orders.** For fixed \(q>2\), reflection reduces to the half-range \(k\le\lfloor n/2\rfloor\). The bound \(a_{n-k}\le Cn^{-1/2}\) makes \(n^{q/2}(a_ka_{n-k})^q\le C_q a_k^q\). Since \(\sum a_k^q<\infty\) precisely when \(q>2\), dominated convergence on this discrete index set and \(n^{1/2}a_{n-k}\to\pi^{-1/2}\) at fixed \(k\) give the limit \(\pi^{-q/2}L(q)\) from each edge. A single midpoint, when present, is of order \(n^{-q}\) and disappears after scaling. The factor two follows.

**Entropy and negativity.** Form a step density \(f_n(x)=(n+1)p_{n,k}\) on \([k/(n+1),(k+1)/(n+1))\). The preceding estimates give pointwise convergence \(f_n\to f\) on \((0,1)\) and the uniform domination \(f_n(x)\le C[x(1-x)]^{-1/2}\) almost everywhere. The inequality \(|t\log t|\le C_\varepsilon(t^{1+\varepsilon}+t^{1-\varepsilon})\) with \(0<\varepsilon<1\) supplies an integrable dominant, hence \(\int f_n\log f_n\to\int f\log f\). Since \(S(\sigma_n)=\log(n+1)-\int f_n\log f_n\), and the arcsine density has differential entropy \(-\int f\log f=\log(\pi/4)\), its claimed asymptotic follows. (The latter integral follows, for example, by differentiating the beta integral at parameter \(1/2\).)

For a pure Schmidt state with nonnegative coefficients \(\sqrt{p_{n,k}}\), its partial transpose has eigenvalues \(p_{n,k}\) and pairs \(\pm\sqrt{p_{n,k}p_{n,j}}\) for \(k<j\). Therefore \(\|\rho_n^{T_B}\|_1=(\sum_k\sqrt{p_{n,k}})^2=F_n(1/2)^2\). Substituting the bulk limit and \(B(3/4,3/4)=2\Gamma(3/4)^2/\sqrt\pi\) gives the stated constants.

Finally \(a_{m+1}/a_m=(2m+1)/(2m+2)\) increases with \(m\), so \(a_m\) is logarithmically convex. Thus \(a_ka_{n-k}\le\max\{a_0a_n,a_na_0\}=a_n\) for \(0\le k\le n\), establishing the min-entropy formula. This also explains why a half-logarithm coefficient applies to min-entropy, not to von Neumann entropy.

## Verification
The attached standalone \(\texttt{verify.py}\) uses only Python 3 standard-library modules and tests exact rational formulas, normalization and the largest Schmidt coefficient for all integers \(1\le n\le17\). It additionally reports numerical trends of the von Neumann constant, critical moment, both bulk and edge regimes, and logarithmic negativity at \(n=20000\). Reproduction: \(\texttt{python3 verify.py}\). These finite checks corroborate the stated identities and limits but do not establish any quantified infinite limit; the latter follow from the bounds above.

## Relationship to prior work
Gagatsos, Oreshkov and Cerf (arXiv:1301.5229v1, first public 2013-01-22) prove photon-number and reflectivity majorization properties for Fock-vacuum beam-splitter inputs. Their arguments do not cover the equal nonvacuum input \(|n,n\rangle\) or the order-dependent moment asymptotics here. Moosavi Khansari (2026) gives balanced equal-input photon-number probabilities and computes finite-input von Neumann entropies; its Section 6 states a leading half-logarithm entropy law. In contrast, the exact spectrum has a beta-binomial/arcsine bulk and the present proof gives the von Neumann coefficient one, while the half-logarithm coefficient belongs to min-entropy. The known exact probabilities, beta-binomial identity, and arcsine limiting law are not claimed as new. The contribution assessed here is the all-order sharp moment asymptotic with its critical order, consequences for mode Rényi entanglement and negativity, and the precise entropy distinction. Other work on Holland–Burnett interference and photonic state engineering does not immediately establish the three-regime spectrum. Any equivalent general result on Rényi entropies of beta-binomial or Dirichlet-multinomial distributions would limit priority.

## Limitations
There is no claim for unbalanced beam splitters, unequal inputs, loss, partial distinguishability, finite-\(n\) entropy optimization or a varying Rényi order approaching \(q=2\). This derivation is conditional on standard ideal two-mode bosonic transformations. As with any literature comparison, absence of a discovered equivalent theorem does not establish priority over inaccessible or differently indexed sources. Natural logarithms are used; conversion to bits divides by \(\log 2\).

## References
1. C. N. Gagatsos, O. Oreshkov, N. J. Cerf, *Majorization relations and entanglement generation in a beam splitter*, arXiv:1301.5229v1 (2013), https://arxiv.org/html/1301.5229v1.
2. S. M. Moosavi Khansari, *Quantum beam splitter as a deterministic entanglement source: exact photon-number statistics, Hong–Ou–Mandel interference, and von Neumann entropy scaling from balanced inputs*, J. Interfaces Thin Films Low Dimens. Syst. **10** (2026), 1077–1083, DOI:10.22051/jitl.2026.54680.1143, https://jitf.alzahra.ac.ir/article_9483_44f9e69bf98c8329ac1c9cfccc0ba5f0.pdf.
3. *Quantum simulations with multiphoton Fock states*, arXiv:1906.00678v2 (2020), https://arxiv.org/html/1906.00678v2 (interference setting and experimentally studied number statistics).

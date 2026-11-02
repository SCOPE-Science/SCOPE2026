# Arithmetic idempotent-free phases in random monomial evolution algebras

## Finding

Fix a prime power \(q\) and an integer \(n\geq 1\). Choose a permutation \(\pi\in S_n\) uniformly and independent weights \(a_1,\ldots,a_n\), each uniformly in \(\mathbb F_q^\times\). Let \(E\) be the perfect evolution algebra with a natural basis \(e_1,\ldots,e_n\) and products
\[
e_ie_j=0\quad(i\ne j),\qquad e_i^2=a_i e_{\pi(i)}.
\]
Let \(N\) be its number of **nonzero** idempotent elements and put \(M=N+1\). For every integer \(\ell\ge1\), set
\[
d_\ell=\gcd(q-1,2^\ell-1),\qquad p_\ell=1-\frac1{d_\ell}.
\]

**Cycle-law theorem.** Conditional on \(\pi\), independently for each cycle \(c\) of length \(\ell\), choose \(B_c\sim\operatorname{Bernoulli}(1/d_\ell)\). Then
\[
M\ \stackrel{\rm law}=\ \prod_{c\in\operatorname{Cyc}(\pi)}(1+d_{|c|}B_c).
\]
This determines the full finite distribution for every \(q,n\). In particular, with \(P_q(n)=\Pr(N=0)\) and \(P_q(0)=1\), the following are identities of formal power series:
\[
\sum_{n\ge0}P_q(n)z^n
=\exp\!\left(\sum_{\ell\ge1}p_\ell\frac{z^\ell}{\ell}\right),
\]
and, for each integer \(k\ge1\),
\[
\sum_{n\ge0}\mathbb E[M^k]z^n
=\exp\!\left(\sum_{\ell\ge1}\left[1+\frac{(1+d_\ell)^k-1}{d_\ell}\right]\frac{z^\ell}{\ell}\right).
\]
Consequently, for all \(q,n\),
\[
\mathbb E[N]=n,\qquad
\operatorname{Var}(N)=[z^n]\exp\!\left(\sum_{\ell\ge1}(d_\ell+3)\frac{z^\ell}{\ell}\right)-(n+1)^2.
\]
Here \([z^n]\) means coefficient extraction.

**Arithmetic support and minimal dimension.** Let \(m\) be the odd part of \(q-1\). When \(m=1\), \(P_q(n)=0\) for every \(n\ge1\). When \(m>1\), for each prime \(p\mid m\) write \(o_p=\operatorname{ord}_p(2)\). Then
\[
P_q(n)>0\quad\Longleftrightarrow\quad n\in\left\{\sum_{p\mid m}u_p o_p:u_p\in\mathbb Z_{\ge0}\right\}\setminus\{0\}.
\]
In particular, the smallest positive dimension admitting an idempotent-free monomial perfect evolution algebra is \(\min_{p\mid m}o_p\). This concerns the monomial subclass; no such restriction is asserted for general perfect evolution algebras.

**Sharp polynomial probabilities.** If \(m>1\), set \(t=\operatorname{ord}_m(2)\), let \(r=\gcd_{p\mid m}o_p\), and set
\[
\alpha=\frac1t\sum_{\ell=1}^t p_\ell,\qquad
C=\exp\!\left(\sum_{\ell\ge1}\frac{p_\ell-\alpha}{\ell}\right).
\]
The displayed series for \(C\) converges in ordinary increasing-index order. It satisfies \(0<\alpha<1\) and \(C>0\). Along positive multiples of \(r\),
\[
P_q(n)\sim\frac{rC}{\Gamma(\alpha)}n^{\alpha-1}\qquad(n\to\infty,\ r\mid n).
\]
On nonmultiples of \(r\), the probability is identically zero. The support characterization implies that all sufficiently large positive multiples of \(r\) are attainable. Thus the coefficient-field arithmetic governs both exact forbidden dimensions and a fractional polynomial decay exponent.

For example, if the odd part of \(q-1\) is \(3\), then
\[
\sum_{n\ge0}P_q(n)z^n=(1-z^2)^{-1/3},\qquad
P_q(2j)=\frac{(1/3)_j}{j!},\quad P_q(2j+1)=0.
\]
If the odd part is \(7\), the corresponding series is \((1-z^3)^{-2/7}\).

## Assumptions and scope

A finite-dimensional evolution algebra over a field is a not-necessarily-associative commutative algebra admitting a natural basis in which distinct basis elements multiply to zero. An idempotent is an element \(x\) with \(x^2=x\); zero is always idempotent. A perfect evolution algebra satisfies \(E^2=E\). A monomial structure matrix is a product of an invertible diagonal matrix and a permutation matrix. The sampling is over **labeled, equipped-natural-basis structures**, not over isomorphism classes; the distribution is explicitly dependent on that distinction. Every selected structure matrix is invertible, so all sampled algebras are perfect. No positivity, characteristic, or algebraic-closure restriction beyond finite-field hypotheses is made.

The independence of the weights and uniformity of the permutation are indispensable for the stated random laws. For a fixed weighted permutation algebra the cycle-by-cycle count below remains deterministic and exact.

## Proof

**1. One-cycle idempotent equation.** For a cycle \(c=(i_0,\ldots,i_{\ell-1})\), an element \(x=\sum_i x_i e_i\) satisfies \(x^2=x\) precisely when
\[
x_{i_{j+1}}=a_{i_j}x_{i_j}^2\quad(j\bmod\ell).
\]
If one coordinate on the cycle vanishes, all do, since the weights are nonzero and squaring detects zero over a field. Otherwise iteration returns to the initial coordinate and yields
\[
x_{i_0}^{2^\ell-1}=A_c^{-1},\qquad
A_c=a_{i_0}^{2^{\ell-1}}a_{i_1}^{2^{\ell-2}}\cdots a_{i_{\ell-2}}^2a_{i_{\ell-1}}.
\]
The last weight has exponent one, so for fixed other weights the product \(A_c\) is uniformly distributed on \(\mathbb F_q^\times\); distinct cycles use disjoint sets of independent weights. The multiplicative group \(\mathbb F_q^\times\) is cyclic of size \(q-1\). The power map with exponent \(2^\ell-1\) has kernel size \(d_\ell\) and image index \(d_\ell\). Therefore a cycle has exactly one idempotent when \(A_c^{-1}\) is outside the image, and exactly \(1+d_\ell\) when it is inside. The inside event has probability \(1/d_\ell\). Each nonzero root uniquely forces all remaining cycle coordinates, so there is no overcount. Different cycles define subalgebras multiplying crosswise to zero, and global idempotents form their Cartesian product. This proves the full conditional cycle law, including \(q=2\) and cycles of length one.

**2. Averaging over permutations.** For arbitrary scalars \(w_\ell\), the classical cycle-index identity, obtainable directly by counting permutations with \(m_\ell\) cycles of length \(\ell\), is
\[
\sum_{n\ge0}z^n\,\mathbb E_{\pi\in S_n}\left[\prod_{c\in\operatorname{Cyc}(\pi)}w_{|c|}\right]
=\exp\!\left(\sum_{\ell\ge1}w_\ell\frac{z^\ell}{\ell}\right).
\]
Indeed, a cycle profile \((m_1,m_2,\ldots)\) with \(\sum_\ell\ell m_\ell=n\) has probability \(\prod_\ell(\ell^{m_\ell}m_\ell!)^{-1}\). Setting \(w_\ell=\Pr(B_c=0)=p_\ell\) gives the idempotent-free series: the global zero idempotent is the **only** idempotent exactly when each cycle has only its zero solution. For the \(k\)-th moment, independence gives \(w_\ell=\mathbb E[(1+d_\ell B_c)^k]=1+((1+d_\ell)^k-1)/d_\ell\). With \(k=1\), all \(w_\ell=2\), hence \(\mathbb E[M]=[z^n](1-z)^{-2}=n+1\). With \(k=2\), all \(w_\ell=3+d_\ell\), so subtracting the squared mean proves the variance formula.

**3. Exact arithmetic support.** Since \(2^\ell-1\) is odd, \(d_\ell>1\) exactly when there exists an odd prime \(p\mid(q-1)\) with \(2^\ell\equiv1\pmod p\). This is equivalent to \(o_p\mid\ell\). All factors in the probability cycle index are nonnegative, so a coefficient \(P_q(n)\) is positive exactly if a permutation of \(n\) has all cycle lengths in this union of divisibility classes. Such a partition of \(n\) exists if and only if \(n\) is a nonzero nonnegative integer combination of the generators \(o_p\): a length divisible by \(o_p\) can be split into cycles of length \(o_p\) without changing its total dimension. This proves the semigroup characterization and its minimum. If \(q-1\) is a power of two, no cycle length is allowed and the probability vanishes for positive \(n\).

**4. Sharp asymptotic.** Suppose the odd part \(m>1\). The nonnegative sequence \(p_\ell\) has period \(t=\operatorname{ord}_m(2)\); its mean \(\alpha\) lies strictly between zero and one. Its support has greatest common divisor \(r=\gcd_{p\mid m}o_p\). Write \(\zeta=e^{2\pi i/t}\), and Fourier-expand this periodic sequence as \(p_\ell=\sum_{j=0}^{t-1}c_j\zeta^{j\ell}\), where \(c_j=t^{-1}\sum_{\ell=1}^t p_\ell\zeta^{-j\ell}\) and \(c_0=\alpha\). Thus, with logarithms continued from \(z=0\),
\[
F(z)=\exp\!\left(\sum_{\ell\ge1}p_\ell\frac{z^\ell}{\ell}\right)=\prod_{j=0}^{t-1}(1-\zeta^j z)^{-c_j}.
\]
The singular exponent at the root \(\zeta^{-j}\) is \(c_j\), with \(\Re c_j\le\alpha\). Equality holds if and only if \(\zeta^{j\ell}=1\) for every \(\ell\) with \(p_\ell>0\), since the positive weighted mean of \(\cos(2\pi j\ell/t)\) can reach its maximum only termwise. These are precisely the \(r\)-th roots of unity, each having exponent \(\alpha\). At \(z=1\), subtracting \(-\alpha\log(1-z)\) leaves a function tending to \(\sum_{\ell\ge1}(p_\ell-\alpha)/\ell\), which converges because its numerator is zero-mean periodic. Its exponential equals \(C\). Because the coefficient series has support on multiples of \(r\), \(F\) is invariant under multiplying \(z\) by an \(r\)-th root of unity, and every dominant singularity has the same local prefactor \(C\). Standard transfer of the finitely many algebraic singularities (or equivalent binomial coefficient estimates) therefore yields
\[
[z^n]F(z)=\frac{C}{\Gamma(\alpha)}n^{\alpha-1}\sum_{\omega^r=1}\omega^{-n}+o(n^{\alpha-1}),
\]
with the stated restriction and factor \(r\). The other singularities have smaller real exponent and contribute smaller-order terms. The numerical semigroup generated by the \(o_p\) contains all sufficiently large multiples of their greatest common divisor, completing the claimed asymptotic scope.

## Verification

The accompanying standalone `verify.py` constructs multiplication in several finite fields directly (including binary extension fields), enumerates every labeled weighted permutation structure matrix in small dimensions and every possible algebra element, and tests \(x^2=x\) in coordinates. It separately computes the predicted probabilities and the first two moments from the power-series recurrence. Across the tested cases \(q\in\{2,3,4,5,7,8\}\), \(1\le n\le3\), and \(q\in\{2,3,4\}\), \(n=4\), all exact rational comparisons pass. The arithmetic-support equivalence was also checked through dimension \(22\) for \(q\in\{4,7,8,11\}\). Execute `python3 verify.py` with a standard Python 3 interpreter; success ends in `VERIFY_OK`.

A finite census does not prove the universal statements. Those are established by the exact cycle equations, cycle-index identity, finite-group arithmetic, and singularity analysis above. The test script is an independent finite crosscheck, not an infinite certificate.

## Relationship to prior work

Narkuziyev's earlier work on evolution algebras associated with permutations gives a coordinate formula for idempotents in each permutation cycle and a direct-sum decomposition. Both features are credited as previously known. The present claim is **not** novelty of the cycle equations, nor novelty of existence of idempotent-free perfect algebras over all finite fields. Its mathematical contribution is the complete *uniform weighted-permutation probability distribution*, all-moment cycle-index transforms, exact arithmetic semigroup of dimensions admitting an idempotent-free monomial structure, and sharp arithmetic-dependent probability asymptotics.

Kaygorodov, Martín González, and Viruel (first public 15 October 2026) establish a mean-one count for nonzero idempotents in the different ensemble of *uniform invertible structure matrices*. They pose questions concerning random evolution algebras and idempotent distributions. Our monomial ensemble is a highly sparse and qualitatively different invertible ensemble, with mean \(n\), not one. Wei–Zou classify certain perfect evolution algebras up to isomorphism, rather than distribution of idempotent elements over randomly labeled monomial structures. No statement about universal novelty beyond inspected sources is intended.

## Limitations

The probability measure is uniform on labeled monomial structure matrices, not on algebra-isomorphism classes or the full general-linear ensemble. Exact coefficient formulas apply for all finite fields and dimensions; the asymptotic statement is for fixed \(q\) and \(n\to\infty\) along the specified congruence subsequence. The theorem does not classify nonmonomial evolution algebras. Priority remains subject to unindexed work on permutation evolution algebras and finite-field random algebra statistics; earlier cycle-by-cycle idempotent solutions already exist.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first submitted 15 October 2026. https://arxiv.org/abs/2610.22248
2. B. A. Narkuziyev, *Evolution algebras corresponding to permutations*, Uzbek Mathematical Journal (2014); author-posted text at https://www.researchgate.net/publication/324150680_On_absolute_nilpotent_and_idempotent_elements_of_an_evolution_algebra_corresponding_to_permutations . See Theorems 2 and 4, the cycle idempotent equations and decomposition.
3. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793, first submitted 9 May 2020; J. Algebra Appl. 21 (2022), DOI:10.1142/S0219498822501122. https://arxiv.org/abs/2005.05793
4. Y. Wei, Y. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023). https://arxiv.org/abs/2310.12368

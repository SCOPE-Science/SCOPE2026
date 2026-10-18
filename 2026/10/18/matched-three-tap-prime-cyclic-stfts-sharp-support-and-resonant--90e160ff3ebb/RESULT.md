# Matched three-tap prime cyclic STFTs: sharp support and resonant zero patterns

## Finding

Let \(p\ge5\) be prime, \(G=\mathbb Z/p\mathbb Z\), and let \(A\subseteq G\) have three elements. For any functions \(f,g:G\to\mathbb C\) satisfying \(\operatorname{supp}f=\operatorname{supp}g=A\), define
\[
V_g f(t,k)=p^{-1/2}\sum_{y\in G} f(y)\overline{g(y-t)}\exp(-2\pi i ky/p).
\]
Let \(m(A)\) be the minimum number of nonzero coefficients of \(V_gf\) over these function pairs. Then
\[
\boxed{m(A)=\begin{cases}5p-4,&A\text{ is a three-term arithmetic progression},\\ 7p-2,&A\text{ is not a three-term arithmetic progression}.\end{cases}}
\]
The second case can occur only for \(p\ge7\). A progression is a set \(\{x,x+a,x+2a\}\) with \(a\ne0\); its three elements need not appear in that order in a representation.

There is also a complete classification of optimal *zero locations*. Write \(z=\exp(-2\pi i k/p)\), and for a progression use \(w=z^a\). The two zero locations for a nonprogression always lie in the time shift \(t=0\), at any chosen two distinct frequency indices. Thus the number of distinct optimal zero-support patterns for each fixed nonprogression is \(\binom p2\). For a progression, all four zero locations consist of two distinct roots \(\gamma,\delta\in\mu_p\) at \(t=0\), one root \(\alpha\in\mu_p\) at \(t=a\), and one root \(\beta\in\mu_p\) at \(t=-a\), satisfying
\[
\boxed{\alpha\beta=\gamma\delta},\qquad \mu_p=\{z\in\mathbb C:z^p=1\}.
\]
Conversely *every* such quadruple of zero locations is achieved by functions with exact support \(A\). There are exactly \(p\binom p2\) distinct optimal zero-support patterns for each progression.

## Assumptions and scope

All primes are ordinary rational primes \(p\ge5\). All coefficient amplitudes are arbitrary nonzero complex numbers. The signal and window have exactly the same prescribed three-point time support but need not coincide. Zero means exact complex zero; the normalization \(p^{-1/2}\) does not affect support. The stated count of zero locations excludes whole time shifts on which the two translated supports do not intersect. The theorem does not assert anything about approximate numerical sparsity, the autocorrelation restriction \(f=g\), or composite cyclic orders.

## Proof

**Prime Fourier row bound.** For each shift \(t\), let \(h_t(y)=f(y)\overline{g(y-t)}\). Its support has size \(r_t=|A\cap(A+t)|\), since every coefficient on this intersection is nonzero. The row \(V_gf(t,\cdot)\) is the ordinary discrete Fourier transform of \(h_t\), up to a nonzero scalar. For a nonzero function on \(\mathbb Z_p\), the prime-order Fourier uncertainty theorem gives \(|\operatorname{supp}h|+|\operatorname{supp}\widehat h|\ge p+1\). Hence a row with \(r_t>0\) has at most \(r_t-1\) exact Fourier zeros. A row with \(r_t=1\) has no zeros. A row with \(r_t=0\) is identically zero and contributes nothing to the support of the STFT.

**Difference geometry.** For a three-element set \(A\), the six ordered differences between distinct points are all different unless the points form an arithmetic progression. Indeed, an equality between differences involving different ordered pairs forces one element to be the midpoint of the other two; equality with reversed pairs would force an element of order \(2\), impossible since \(p\) is odd. For a progression, \(A-A=\{0,\pm a,\pm2a\}\) has five distinct elements, with overlap multiplicities \(r_0=3\), \(r_{\pm a}=2\), and \(r_{\pm2a}=1\). For a nonprogression, \(A-A\) has seven distinct elements, with \(r_0=3\) and \(r_t=1\) at each of its six nonzero differences. The row bound therefore gives respectively \(|\operatorname{supp}V_gf|\ge5p-4\) and \(|\operatorname{supp}V_gf|\ge7p-2\).

**Attaining the nonprogression bound.** Enumerate \(A=\{a_0,a_1,a_2\}\) and fix any distinct frequency indices \(k_1,k_2\). Let \(E_{ij}=\exp(-2\pi i k_i a_j/p)\), where \(i=1,2\) and \(j=0,1,2\). Choose the three coefficient products \(f(a_j)\overline{g(a_j)}\) to be the signed \(2\times2\) minors of the \(2\times3\) matrix \((E_{ij})\). These products annihilate both chosen Fourier rows. Every product is nonzero because each corresponding \(2\times2\) prime Fourier minor is nonzero (or directly because \((k_1-k_2)(a_j-a_l)\not\equiv0\pmod p\)). Set \(g=1\) on \(A\) and \(f\) equal to these products. By the three-point row bound, the central row has exactly the two designated zeros; every other active row has a single nonzero input, hence no zero. This proves the bound and realizes each of the \(\binom p2\) possible zero pairs.

**Attaining the progression bound.** Translation and dilation allow us to use coordinates \(A=\{0,1,2\}\), replacing the Fourier variable by \(w=z^a\) in general. Choose any distinct \(\gamma,\delta\in\mu_p\) and any \(\alpha\in\mu_p\). Put \(\beta=\gamma\delta/\alpha\). Define the three signal coefficients in order by
\[
f_0=\frac{\gamma\delta(\gamma+\delta)}{\alpha},\quad f_1=-(\gamma+\delta),\quad f_2=1,
\]
and define the window coefficients by
\[
g_0=\alpha^{-1},\qquad g_1=g_2=\gamma^{-1}+\delta^{-1}.
\]
None is zero: two distinct roots of unity of odd order cannot be negatives of one another. Using \(\overline{g_0}=\alpha\) and \(\overline{g_1}=\overline{g_2}=\gamma+\delta\), the nontrivial row polynomials, up to nonzero Fourier monomials and the common transform normalization, factor as
\[
\begin{aligned}
t=0:&\quad (\gamma+\delta)(w-\gamma)(w-\delta),\\
t=a:&\quad (\gamma+\delta)w(w-\alpha),\\
t=-a:&\quad (\gamma+\delta)^2(\beta-w).
\end{aligned}
\]
The two outer rows \(t=\pm2a\) are nonzero Fourier monomials. Thus exactly four active-row entries vanish, yielding \(5p-4\) nonzero STFT entries and the announced zero locations.

**Necessity and completeness of the resonance relation.** Suppose \(A=\{x,x+a,x+2a\}\) has an optimal pair. Equality in the row bounds forces two distinct central roots \(\gamma,\delta\), one root \(\alpha\) in row \(t=a\), and one root \(\beta\) in row \(t=-a\), all of the variable \(w=z^a\). Write \(F_i=f(x+ia)\) and \(G_i=g(x+ia)\). The central row polynomial has coefficients \(c_i=F_i\overline{G_i}\) and, by the factor theorem, \(c_0/c_2=\gamma\delta\). The two side-row zeros give
\[
\frac{F_1\overline{G_0}}{F_2\overline{G_1}}=-\alpha,
\qquad
\frac{F_0\overline{G_1}}{F_1\overline{G_2}}=-\beta.
\]
Multiplying shows \(c_0/c_2=\alpha\beta\), proving the necessary resonance relation. The explicit construction realizes all satisfying quadruples, so there are \(\binom p2\) choices of unordered central root pairs, then \(p\) choices of \(\alpha\), and uniquely determined \(\beta\). All patterns are distinct. A nonprogression has no side overlap of size two and has precisely the previously classified central zero pair. The proof is complete.

For completeness, the number of progressions as subsets of \(\mathbb Z_p\) is \(p(p-1)/2\): every ordered center and nonzero step gives a progression, and reversal is the unique duplication for \(p\ge5\). The number of nonprogression three-sets is \(\binom p3-p(p-1)/2\).

## Verification

The accompanying standalone `checker.py` performs exact arithmetic in \(\mathbb Z[X]/(1+X+\cdots+X^{p-1})\), representing cyclotomic expressions by sparse integer exponent dictionaries. It tests the explicit four-hole construction and every admissible four-hole resonance pattern for primes \(5,7,11,13\); for each three-element support it independently checks the progression/difference-set dichotomy; for every nonprogression it constructs a two-zero center row and verifies that all other active rows have no zero. For these primes the numbers of progression/nonprogression supports are respectively \((10,0)\), \((21,14)\), \((55,110)\), and \((78,208)\). The checker concludes `CHECK_PASS`. This is exhaustive only for those finite primes; the general result is established by the proof above.

To reproduce, run `python3 checker.py` with Python 3; it uses only the standard library. Cyclotomic vanishing is tested exactly: an integer polynomial of degree at most \(p-1\) vanishes at a primitive \(p\)-th root precisely when its \(p\) residue-class coefficients are all equal. No floating-point tolerances or external databases are needed.

## Relationship to prior work

Nicola (2022) classifies the equality cases of the universal \(|\operatorname{supp}V_gf|\ge p\) bound on cyclic groups; that theorem does not prescribe matched three-point time supports or classify their minimal-support zero patterns. Tao's prime-order Fourier uncertainty theorem, equivalently the nonvanishing of all square Fourier minors, gives the sharp bound separately for each time slice, and is explicitly used in this proof. The new classification identifies the simultaneous attainability constraints between the five time slices, including the necessary and sufficient relation \(\alpha\beta=\gamma\delta\). Previously published two-sparse STFT classifications concern pairs with two nonzero coefficients per input and do not imply the three-tap matched-aperture result.

## Limitations

The result concerns precise complex support, not robustness under noise; it does not classify all signal-window amplitudes realizing each optimal pattern, only all optimal zero locations. It makes no claim about unequal signal/window supports, equal-coefficient or phase-only restrictions, composite orders, or higher sparsity. Prior literature on sparse Gabor masks may contain an equivalent formulation; independent mathematical and bibliographic validation has not been performed.

## References

- Fabio Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1 (29 April 2022), particularly Theorem 1.2 and Sections 2–4. https://arxiv.org/abs/2204.14176
- Terence Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286 (first posted 29 August 2003), Theorem 1.1 and Lemma 1.3. https://arxiv.org/abs/math/0308286

# Run-capped binary words have an exact subsequence-universality spectrum

## Finding

For every integer \(h\geq1\), let \(\mathcal R_h\) be the binary words in which no symbol occurs \(h+1\) times consecutively. The empty word belongs to \(\mathcal R_h\). Let \(\iota(w)\) be the largest \(k\geq0\) such that every binary word of length \(k\) is a scattered subsequence of \(w\). Define

\[
C_h(n,k)=\#\{w\in\mathcal R_h:|w|=n,\ \iota(w)=k\}.
\]

Put \(S_h(z)=1+z+\cdots+z^{h-1}\), \(S_0(z)=0\), \(T_h(z)=S_h(z)+S_{h-1}(z)\). The complete bivariate count is

\[
\boxed{F_h(z,u)=\sum_{n,k\geq0}C_h(n,k)z^nu^k
=\frac{1+2zS_h(z)+u z^{h+1}}{1-u z^2T_h(z)}.}
\]

In particular, for each \(k\geq1\),

\[
\boxed{\sum_{n\geq0}C_h(n,k)z^n
=2z^{2k}S_h(z)T_h(z)^{k-1}(1+zT_h(z)).}
\]

Its coefficients are strictly positive precisely for \(2k\leq n\leq (h+1)k+h\). Thus the *exact range* of possible universality indices among \(n\)-letter words in \(\mathcal R_h\) is

\[
\boxed{\max\left\{0,\left\lceil\frac{n-h}{h+1}\right\rceil\right\}\leq k\leq\left\lfloor\frac n2\right\rfloor.}
\]

At the longest length admitting index exactly \(k\geq1\), there are exactly two words: \(0^h(10^h)^k\) and \(1^h(01^h)^k\). At length \(2k\), there are \(2\) words if \(h=1\), and \(2^k\) if \(h\geq2\). Index zero occurs only at lengths \(0\leq n\leq h\), with one empty word and two constant words of each positive length.

There is also a quantitative asymptotic law. For fixed \(h\geq2\), choose \(W_n\) uniformly among \(\mathcal R_h\cap\{0,1\}^n\) and set \(K_n=\iota(W_n)\). Let \(\rho_h\in(0,1)\) solve \(\rho_h+\rho_h^2+\cdots+\rho_h^h=1\). Define \(c_j=2\) for \(2\leq j\leq h\), \(c_{h+1}=1\), and \(p_j=c_j\rho_h^j\). These numbers sum to one. Set \(\mu_h=\sum_{j=2}^{h+1}j p_j\) and \(v_h=\sum_{j=2}^{h+1}(j-\mu_h)^2p_j\). Then \(v_h>0\), and

\[
\mathbb E[K_n]=\frac n{\mu_h}+O_h(1),\qquad
\operatorname{Var}(K_n)=\frac{v_h}{\mu_h^3}n+O_h(1),\qquad
\frac{K_n-n/\mu_h}{\sqrt{v_hn/\mu_h^3}}\ \Longrightarrow\ \mathcal N(0,1).
\]

For the smallest nontrivial cap \(h=2\), the exact generating function and asymptotic parameters simplify to

\[
F_2(z,u)=\frac{1+2z+2z^2+uz^3}{1-u(2z^2+z^3)},\qquad
\frac1{\mu_2}=\frac1{\sqrt5},\qquad
\frac{v_2}{\mu_2^3}=1-\frac{11}{5\sqrt5}.
\]

For \(h=1\) the only nonempty words alternate and \(K_n=\lfloor n/2\rfloor\) deterministically. As \(h\to\infty\), the linear mean coefficient tends to \(1/3\) and the variance coefficient tends to \(2/27\).

## Assumptions and scope

The alphabet is the labeled binary set \(\{0,1\}\). A run means a maximal *contiguous* block of equal symbols; this is different from a scattered subsequence. All words are indexed linear strings, not necklaces or equivalence classes under complement. All integers \(h\geq1\), \(n,k\geq0\) are covered by the exact generating function. The Gaussian asymptotic takes \(n\to\infty\) at **fixed** \(h\geq2\); it makes no claim of uniformity when \(h\) grows with \(n\). The upper and lower support statements concern words of **exact** universality index, not merely index at least a prescribed level.

## Proof

**Greedy-arch lemma.** Start with an empty set of seen symbols and read the word left to right. Whenever both symbols have been seen since the last reset, close an arch and reset the seen set to empty. The number of closed arches is \(\iota(w)\). Indeed, choosing the first newly seen occurrence of each missing symbol gives one universally coverable layer per arch, while an adversarial pattern formed by choosing the symbols last introduced at successive arches (and a missing symbol in the final incomplete layer) witnesses the impossibility of covering all patterns with one additional layer. Equivalently, this is the standard arch-factorization universality theorem [1,2,3].

**Exact weighted finite-state decomposition.** A completed arch always ends with a symbol different from the preceding partial-arch symbol. Its final symbol consequently starts a fresh run of length one. Let \(A_j\) denote the generating function of permitted continuations after exactly one binary symbol has been seen in the current incomplete arch and its current run has length \(j\in\{1,\dots,h\}\). Let \(E\) denote permitted continuations immediately after an arch closes, with no symbol in the new incomplete arch and a final run of length one. Each appended symbol contributes \(z\), while an arch closure contributes an additional \(u\). Termination is always allowed and contributes one. Complement symmetry removes dependence on the particular bit. The exact disjoint alternatives are

\[
A_j=1+zuE+\mathbf 1_{j<h}\,zA_{j+1},\qquad
E=1+zA_1+\mathbf 1_{h\geq2}\,zA_2.
\]

In the second equation, the continuation after \(E\) starts a new partial arch: reading a different bit creates a run of length one; reading the same bit creates a run of length two, if permitted. In the first equation, a different bit completes the current arch, and a same bit can continue only before the cap. There are no other choices, so these recurrences count each word once.

The first recurrence gives \(A_j=S_{h-j+1}(z)(1+zuE)\). With \(A_2=0\) by convention when \(h=1\), substitution yields

\[
E=\frac{1+zT_h(z)}{1-uz^2T_h(z)},\qquad
A_1=\frac{S_h(z)(1+zu)}{1-uz^2T_h(z)}.
\]

The empty word contributes one, and a nonempty word chooses its first symbol in two ways, leading to

\[
F_h(z,u)=1+2zA_1.
\]

Multiplying out its numerator and using \(S_h-S_{h-1}=z^{h-1}\) gives the displayed rational identity. Expanding \((1-u z^2T_h)^{-1}\) and extracting the coefficient of \(u^k\) gives the claimed index-refined polynomial.

**Support, multiplicities, and extremizers.** For \(k\geq1\), the factor \(S_hT_h^{k-1}(1+zT_h)\) has strictly positive coefficients at *every* degree from zero through \(k(h-1)+h\). This follows because \(S_h\) has support \(\{0,\dots,h-1\}\), \(T_h\) has the same support (with positive coefficients), and \(1+zT_h\) has support \(\{0,\dots,h\}\), all without gaps. This also handles \(h=1\), where the first two factors are one. The smallest coefficient is \(2T_h(0)^{k-1}\), and the highest coefficient is two. The explicit longest words \(0^h(10^h)^k\) and their complements meet the run cap and have exactly \(k\) arches; because the highest coefficient is two, these are all longest words. At minimum length \(2k\), the \(k\) arches must each be a two-letter permutation, giving the counts above. The zero-index polynomial \(1+2zS_h\) yields exactly the asserted constant words and completes the support classification.

**Gaussian law and its constants.** Put \(B_h(z)=z^2T_h(z)=\sum_{j=2}^{h+1}c_jz^j\). The identity

\[
1-B_h(z)=(1+z)\left(1-\sum_{j=1}^{h}z^j\right)
\]

shows that \(B_h(\rho_h)=1\). For fixed \(h\geq2\), both \(z^2\) and \(z^3\) occur with positive coefficients in \(B_h\). Their coprime exponents imply that the positive root \(\rho_h\) is the unique zero of \(1-B_h(z)\) on its circle of convergence: equality in the triangle inequality would require the phases of both \(z^2\) and \(z^3\) to equal one. The root is simple since \(B_h'(\rho_h)>0\), and the numerator of \(F_h\) is positive there. Consequently for complex \(u\) near one, the equation \(uB_h(\rho(u))=1\) defines a unique analytic dominant simple pole, with coefficient asymptotics locally uniform in \(u\).

Taking the ratio of coefficients at \(u=e^t\) and \(u=1\) gives the moment-generating function in the quasi-powers form

\[
\mathbb E[e^{tK_n}]=H_h(t)\left(\frac{\rho_h}{\rho(e^t)}\right)^n(1+O_h(\theta^n)),
\]

where \(H_h\) is analytic, \(H_h(0)=1\), and some \(\theta\in(0,1)\) works locally uniformly for small complex \(t\). Put \(p_j=c_j\rho_h^j\). Logarithmic differentiation of \(e^tB_h(\rho(e^t))=1\) gives the first derivative \(1/\mu_h\) of the limiting log moment-generating function; differentiating once more gives \(v_h/\mu_h^3\). The same analytic expansion at \(t=is/\sqrt n\), after centering, converges to the standard Gaussian characteristic function, proving the central limit theorem. The distribution on lengths \(j\in\{2,\dots,h+1\}\) has at least two positive atoms for \(h\geq2\), hence \(v_h>0\). For \(h=1\) its sole atom is at two, as already handled directly.

For \(h=2\), \(\rho_2=(\sqrt5-1)/2\), \(p_2=2\rho_2^2\), \(p_3=\rho_2^3\), and substitution yields the stated exact constants. Finally \(\rho_h\to1/2\) and \(p_j\to2^{-(j-1)}\) for each fixed \(j\geq2\), with uniformly geometric tails, so \(\mu_h\to3\) and \(v_h\to2\).

## Verification

Run `python3 verify.py` using Python 3's standard library. The checker exhaustively lists all words of lengths zero through sixteen for each cap from one through five, computes the arch index, and compares each coefficient against the finite polynomial formula. It also uses an independent fully labeled state recurrence and explicitly enumerates binary subsequence patterns at shorter lengths. The completed run printed:

`VERIFY_OK caps=1..5 lengths=0..16 exhaustive_host_checks=249399 literal_subsequence_checks=2777 boundary_k=1..9`

This computational check is finite corroboration; the all-parameter conclusions follow from the displayed recurrences, coefficient factorization, and pole analysis. No external proof assistant or independent human validation is claimed.

## Relationship to prior work

Barker et al. [1] established the subsequence-universality framework and arch-factorization methods. Adamson [2] gave algorithms for unrestricted subsequence-universal words, while Adamson et al. [3] developed general decision and counting methods for intersections of regular languages with universal-word languages. Since \(\mathcal R_h\) is regular, the counting algorithms in [3] can in principle recover any fixed coefficient. The claim here is more specific: the closed two-variable rational identity valid simultaneously for every run cap, its gap-free support and exact two longest extremizers, and the explicit Gaussian fluctuation constants. None of the inspected relevant sections in [2,3] states these formulas or this run-cap classification. The unrestricted all-binary law arises as the formal limit \(h\to\infty\), so it is not claimed as new. An equivalent identity hidden in another coding-constraint or automata enumeration paper remains possible.

## Limitations

The alphabet is binary and the constraint is a bound on **both** symbol-run lengths. An asymmetric cap, a larger alphabet, cyclic words, weighted symbols, and caps growing with length are not covered by the Gaussian theorem. The finite checker does not prove the infinite formulas. The relation to prior work is assessed from accessible literature, not from an exhaustive universal bibliography; independent expert review has not been performed.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words* (2020), arXiv:2003.04629, https://arxiv.org/abs/2003.04629.
2. D. Adamson, *Ranking and Unranking k-Subsequence Universal Words* (2023), arXiv:2304.04583, https://arxiv.org/abs/2304.04583.
3. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages* (2023), arXiv:2311.10658, https://arxiv.org/abs/2311.10658.
4. P. Flajolet, R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), singularity analysis and quasi-powers principles.

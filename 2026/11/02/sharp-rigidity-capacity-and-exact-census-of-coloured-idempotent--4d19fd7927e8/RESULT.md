# Sharp rigidity capacity and exact census of coloured idempotent unary models

## Finding

Fix an integer \(q\geq1\). An admissible structure is a finite set \(X\), a total unary map \(f:X\to X\) satisfying \(f(f(x))=f(x)\) for all \(x\in X\), and a partition of \(X\) into exactly \(q\) **named colour classes**, any of which may be empty. Isomorphisms preserve the function and every colour class. Let \(u_q(n)\) be the number of isomorphism classes on \(n\) elements, and \(r_q(n)\) the number of those with trivial automorphism group, with an empty structure included at \(n=0\).

**Theorem (complete component and rigidity census).** Every isomorphism class is a multiset of coloured rooted-star types \((c;m_1,\dots,m_q)\), where \(1\le c\le q\) is the root colour and the nonnegative integers \(m_j\) count non-root elements of colour \(j\). An isomorphism class is rigid if and only if every \(m_j\in\{0,1\}\) and no rooted-star type occurs more than once. Hence

\[
\boxed{R_q(z)=\sum_{n\ge0}r_q(n)z^n
=\prod_{j=0}^{q}(1+z^{j+1})^{q\binom qj}.}
\]

Its degree is the **sharp rigidity capacity**

\[
\boxed{N_q=q2^{q-1}(q+2).}
\]

For every integer \(n\geq1\), a rigid \(q\)-coloured idempotent unary structure of size \(n\) exists **if and only if** \(n\leq N_q\). At size \(N_q\) there is exactly one such isomorphism type, and for all \(0\leq n\leq N_q\), \(r_q(n)=r_q(N_q-n)\). The number of *labelled* rigid structures on a fixed \(n\)-element carrier is exactly \(n!r_q(n)\).

For comparison, **all** isomorphism types (not necessarily rigid) have the exact multiset series

\[
\boxed{U_q(z)=\sum_{n\ge0}u_q(n)z^n
=\prod_{s\ge1}(1-z^s)^{-q\binom{s+q-2}{q-1}}.}
\]

In particular, with \(u_q(0)=1\), the coefficients satisfy the computable recurrence

\[
\boxed{nu_q(n)=\sum_{m=1}^n u_q(n-m)
\sum_{d\mid m}dq\binom{d+q-2}{q-1}\qquad(n\ge1).}
\]

For each fixed \(q\geq1\), the unrestricted population has the sharp logarithmic growth

\[
\boxed{\lim_{n\to\infty}\frac{\log u_q(n)}{n^{q/(q+1)}}
=(q+1)\left(\frac{\zeta(q+1)}{q^{q-1}}\right)^{1/(q+1)}.}
\]

Thus there are arbitrarily large non-rigid structures while *no* rigid structure exists above the explicit finite capacity. If the signature instead contains \(r\) independent unary predicates (so each element has one of \(q=2^r\) truth vectors), the capacity becomes \(2^r2^{2^r-1}(2^r+2)\).

## Assumptions and scope

The language has **one unary operation** and named colours; the idempotence equation holds everywhere. Components are not required to be connected in any ordering; they are the fibres of the idempotent map. The function is the only nonlogical operation and the colour classes have no nonemptiness requirement. An automorphism is a colour-preserving permutation commuting with \(f\). The enumeration is by isomorphism, not by labelled presentations. All products and formal power series are interpreted coefficientwise; their coefficients are finite for any fixed degree. The logarithmic limit keeps \(q\) fixed while \(n\to\infty\).

## Proof

**1. Canonical stars.** Every \(x\) maps in one step to a fixed point \(a=f(x)\), because \(f(a)=f(f(x))=f(x)=a\). The nonempty fibres \(f^{-1}(a)\) partition \(X\) and contain their unique fixed roots \(a\). Each fibre is a rooted star with arbitrarily many leaves, and its colour-preserving isomorphism type is precisely \((c;m_1,\dots,m_q)\). A whole model is therefore uniquely a multiset of those star types. Conversely every finite such multiset yields an admissible model. This proves the canonical classification without any enumeration or probabilistic assumption.

**2. Automorphisms and rigidity.** For each type \(\tau=(c;m_1,\dots,m_q)\), let \(k_\tau\) denote its multiplicity in the multiset. An automorphism can independently permute leaves of each colour in each copy, and can permute the \(k_\tau\) copies with equal type. All automorphisms arise this way, since fixed roots must map to fixed roots of the same coloured star type. Thus the automorphism group is a product, over types, of wreath products

\[
\left(\prod_{j=1}^{q}\mathfrak S_{m_j}\right)\wr\mathfrak S_{k_\tau}.
\]

This group is trivial exactly when every \(m_j\le1\) and every \(k_\tau\le1\). The number of possible rigid type choices having exactly \(j\) leaves is \(q\binom qj\), independently for each \(0\le j\le q\). Each choice may be selected once or not at all, with weight \(j+1\), proving the product for \(R_q(z)\). Since a rigid isomorphism type has exactly \(n!\) labelled realizations, the labelled formula follows from orbit–stabilizer.

**3. Sharp cutoff, full interval and complement symmetry.** The maximum weight of all rigid type choices is

\[
\sum_{j=0}^{q}(j+1)q\binom qj
=q\left(2^q+q2^{q-1}\right)=q2^{q-1}(q+2)=N_q.
\]

Every weight \(w\in\{1,\dots,q+1\}\) occurs at least once. A multiset containing at least one of every successive weight from \(1\) to \(q+1\) has no gaps in its subset-sum spectrum: inductively, if the previous weights realize \(0,\dots,S\) and the next weight is \(w\le S+1\), the new sums cover \(0,\dots,S+w\). In nondecreasing order of available weights, the required inequality always holds because all smaller positive weights appeared. Hence every degree \(0,\dots,N_q\) has positive coefficient, and no larger degree occurs. Complementing the chosen set of rigid star types bijects total weight \(n\) with \(N_q-n\), proving palindromicity. The unique choice selecting all types gives the single top-degree class.

**4. Unrestricted enumeration and recurrence.** The number of star types of total size \(s\ge1\) is the number of root colours, \(q\), times the weak compositions of \(s-1\) leaves among \(q\) named colours:

\[
a_s=q\binom{s+q-2}{q-1}.
\]

A multiset may contain any nonnegative number of each star type, yielding \(U_q(z)=\prod_{s\ge1}(1-z^s)^{-a_s}\). Taking the formal logarithmic derivative gives

\[
z\frac{U'_q(z)}{U_q(z)}
=\sum_{s\ge1}\sum_{h\ge1}sa_s z^{sh}
=\sum_{m\ge1}\Bigl(\sum_{d\mid m}da_d\Bigr)z^m.
\]

Equating coefficients proves the exact recurrence.

**5. Growth law.** Put \(L(t)=\log U_q(e^{-t})\), \(t>0\). Since \(a_s=\frac{q}{(q-1)!}s^{q-1}+O_q(s^{q-2})\) for \(q\ge2\) (and \(a_s=1\) identically for \(q=1\)), summing geometric/exponential moments in the log product gives, as \(t\downarrow0\),

\[
L(t)\sim Ct^{-q},\quad -L'(t)\sim qCt^{-q-1},\quad
L''(t)\sim q(q+1)Ct^{-q-2},\qquad C=q\zeta(q+1).
\]

These statements follow by splitting \(\sum_{h\ge1}h^{-1}\sum_{s\ge1}a_s e^{-sht}\) at \(ht=1\) and applying the Riemann-sum estimate \(\sum_{s\ge1}s^{q-1}e^{-s v}\sim(q-1)!v^{-q}\) and its differentiated analogues; for the tail, the exponential factors dominate, permitting dominated convergence after normalization. They also follow by the identity \(\sum_{s\ge1}\binom{s+q-2}{q-1}x^s=x/(1-x)^q\), which gives the **exact** expression

\[
L(t)=q\sum_{h\ge1}\frac{e^{-ht}}{h(1-e^{-ht})^q}.
\]

For the upper bound, \(S_n=\sum_{k=0}^n u_q(k)\le e^{tn}U_q(e^{-t})\). Choose \(t=(qC/n)^{1/(q+1)}\), obtaining

\[
\limsup_{n\to\infty}n^{-q/(q+1)}\log S_n
\le(q+1)(C/q^q)^{1/(q+1)}.
\]

For the lower bound, view \(K\) as a Boltzmann-distributed total size with \(\Pr_t(K=k)=u_q(k)e^{-tk}/U_q(e^{-t})\). Its mean is \(-L'(t)\) and variance \(L''(t)\). Fix \(0<\varepsilon<1/3\) and choose \(t=t_n\) with mean \((1-\varepsilon)n\) (uniqueness follows from the strictly decreasing mean and positivity of variance). Then \(t_n\sim(qC/((1-\varepsilon)n))^{1/(q+1)}\), and the variance estimate plus Chebyshev's inequality gives \(\Pr_t((1-2\varepsilon)n\le K\le n)\to1\). Consequently

\[
S_n\ge U_q(e^{-t_n})e^{t_n(1-2\varepsilon)n}(1-o(1)).
\]

On dividing by \(n^{q/(q+1)}\) and letting \(\varepsilon\downarrow0\), this yields the matching lower bound. Finally, adjoining a single isolated fixed root of a fixed colour maps each \(n\)-point isomorphism type injectively to an \((n+1)\)-point type, so \(u_q(n)\) is nondecreasing and \(S_n/(n+1)\le u_q(n)\le S_n\). The difference of logarithms is at most \(\log(n+1)\), negligible on the scale above. Substitute \(C=q\zeta(q+1)\) to obtain the displayed constant.

## Verification

The standalone `checker.py` independently builds all labelled idempotent unary maps and every named-colour assignment on carriers of sizes \(1\le n\le6\) for \(q=1\), \(1\le n\le5\) for \(q=2\), and \(1\le n\le4\) for \(q=4\). It canonicalizes each fibre multiset and tests the two automorphism obstructions directly, separately from the formal generating-function algorithms. Exhaustive isomorphism counts equal both independent coefficient methods. For \(q=2\) the first eight nonempty unrestricted counts are \(2,7,18,47,110,258,568,1237\). The finite rigidity cutoffs for \(q=1,2,4\) are \(3,16,192\). The checker also verifies palindromicity, no degree gaps, the top coefficient, and the independent divisor-sum recurrence through degree \(20\). Run `python3 checker.py` with Python 3 standard library only; its terminal success marker is `ALL_CHECKS_OK`.

The infinite algebraic and asymptotic assertions follow from the proof, **not** merely from this finite checker. Neither the exhaustive carrier bounds nor finite coefficient comparisons can establish priority or verify all infinite cases.

## Relationship to prior work

Kuželka's 2026 study of unary functions, automorphisms, and unlabeled first-order model counting [1] provides the motivation to distinguish trivial from nontrivial automorphism corrections in finite model counting. Its accessible primary full text discusses general unary-function counting and automorphism tracking, but does not state the explicit rigidity classification for coloured **idempotent** maps or the sharp finite capacity derived here. The unrestricted multiset-product enumeration is an elementary consequence of the canonical star decomposition; **it is not presented as a stand-alone historically new counting principle**. For \(q=2\), the resulting unrestricted coefficient sequence is OEIS A161870 [2], a pre-existing sequence with an equivalent plane-partition product. The one-colour unrestricted specialization is the classical integer-partition series [3]. Neither of these known unrestricted coefficient tables determines the rigid-series polynomial or its cutoff by logical implication alone. Relevant other published results on generic unary functions and polymorphism-homogeneous unary algebras concern different hypotheses and do not provide the particular rigidity classification in [1]'s coloured idempotent setting.

## Limitations

The sharp cutoff relies on **exactly one** total idempotent unary map, a **fixed** finite number of named colours, and homomorphisms required to preserve those colours. If multiple unary maps are permitted, if colours can be permuted, or if unary predicates are allowed unboundedly many values with \(n\), the rigidity theorem needs not apply. The logarithmic asymptotic holds for fixed \(q\) only; it is not uniform when \(q\) grows with \(n\). The formal power series count unlabeled structures but are not algorithms for isomorphism between arbitrary additional signatures. The motivating paper's general automorphism machinery and the known unrestricted sequences are prior work; historical priority of the **specific rigid polynomial and ceiling** cannot be proven by a finite literature search. An earlier equivalent result under coloured star forests or automorphism-free unary-algebra terminology could exist.

## References

[1] O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580, first publicly submitted 2026-08-31. https://arxiv.org/abs/2608.30580

[2] OEIS A161870, prior sequence counting two-colour multiset/plane-partition structures. https://oeis.org/A161870

[3] OEIS A000041, the classical integer partition numbers. https://oeis.org/A000041

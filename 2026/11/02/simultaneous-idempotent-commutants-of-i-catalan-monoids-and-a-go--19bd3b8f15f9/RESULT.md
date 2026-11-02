# Simultaneous idempotent commutants of \(i\)-Catalan monoids and a golden-ratio singularity transition

## Finding

Let \(IC_n\) be the monoid of all order-preserving, extensive, injective partial transformations of the chain \([n]=\{1,\dots,n\}\), with composition as multiplication. Let \(E_n\) be its idempotents. For a map \(f\in IC_n\), write \(r(f)=|\{i\in\operatorname{dom}(f):f(i)>i\}|\), and let \(c_E(f)=|\{e\in E_n:ef=fe\}|\).

**Centralizer-spectrum theorem.** For every \(n\geq1\), the idempotents are exactly the \(2^n\) partial identities, and
\[
 c_E(f)=2^{n-r(f)}.
\]
Define \(F_n(u)=\sum_{f\in IC_n}u^{r(f)}\) and \(F_0(u)=1\). The entire idempotent-commutant size distribution is thereby determined by the algebraic series
\[
 F(z,u)=\sum_{n\geq0}F_n(u)z^n=\frac{S(z,u)}{1-zS(z,u)},\qquad
 S(z,u)=1+zS(z,u)(1-u+uS(z,u)),\quad S(0,u)=1.
\]
Equivalently, for \(m\geq1\), let
\[
 S_m(u)=\frac1m\sum_{r=0}^{m-1}\binom m r\binom m{r+1}u^r,\qquad S_0(u)=1.
\]
Then \(F_n(u)\) is the explicit coefficient of \(z^n\) in \(S/(1-zS)\), with \(S(z,u)=\sum_{m\geq0}S_m(u)z^m\).

For every integer \(k\geq1\), the number of ordered tuples \((f,e_1,\ldots,e_k)\) with \(f\in IC_n\), all \(e_j\in E_n\), and \(fe_j=e_jf\) for every \(j\), is exactly
\[
 T_{n,k}=2^{kn}F_n(2^{-k}).
\]
(The idempotents commute with one another automatically.) In particular, if all \(k+1\) elements are chosen independently and uniformly from their respective sets, the simultaneous commutation probability is
\[
 P_{n,k}=\frac{F_n(2^{-k})}{C_{n+1}},\qquad C_{n+1}=\frac1{n+2}\binom{2n+2}{n+1}.
\]

**Golden-ratio transition.** Put \(u_*=(3-\sqrt5)/2\), \(v=\sqrt u\), and \(\rho(u)=(1+v)^{-2}\). The singularity of \(F(z,u)\), as \(n\to\infty\) with \(u\in(0,1)\) fixed, changes type precisely at \(u_*\):

* For \(u_*<u<1\), it is a square-root branch point at \(\rho(u)\), and
\[
 F_n(u)\sim\frac{\sqrt v(1+v)^3}{2\sqrt\pi\,(v^2+v-1)^2}\,\rho(u)^{-n}n^{-3/2}.
\]
* For \(0<u<u_*\), it is a simple pole at \(z_p=(1-u)/(2-u)\), and
\[
 F_n(u)\sim\frac{1-3u+u^2}{(1-u)^2}\left(\frac{2-u}{1-u}\right)^n.
\]
* At \(u=u_*\), with \(v_*=\sqrt{u_*}\), the collision gives
\[
 F_n(u_*)\sim\frac{\sqrt{v_*}(1+v_*)^2}{\sqrt\pi}\,\rho(u_*)^{-n}n^{-1/2}.
\]

Thus the natural integer moments straddle the transition: \(u=2^{-1}>u_*\) has the branch-point behavior, whereas **every** \(k\geq2\) has \(u=2^{-k}<u_*\) and a pole. In particular, for \(k\geq2\) fixed, writing \(u=2^{-k}\),
\[
 \boxed{P_{n,k}\sim\frac{\sqrt\pi}{4}\frac{1-3u+u^2}{(1-u)^2}\,n^{3/2}\left(\frac{2-u}{4(1-u)}\right)^n.}
\]
The \(k=1\) comparison is
\[
 P_{n,1}\sim \frac{\sqrt v(1+v)^3}{8(v^2+v-1)^2}\left(\frac{(1+v)^2}{4}\right)^n,\qquad v=2^{-1/2}.
\]
The \(k=1\) numerical sequence and its asymptotic were already known in a different combinatorial interpretation (OEIS A225887); **neither is asserted to be independently new**. The assessed contribution is the complete monoid idempotent-commutant spectrum and simultaneous \(k\geq2\) counts, including their singularity transition.

## Assumptions and scope

All statements concern ordinary finite partial functions and set-theoretic composition, not linear transformations or semigroup algebras. Elements of \(IC_n\) are specified uniquely by two increasing equally long lists \(D=(d_1<\cdots<d_s)\) and \(I=(b_1<\cdots<b_s)\) with \(d_j\leq b_j\), via \(f(d_j)=b_j\). The empty partial map is included. No field or characteristic assumption occurs. The parameter \(k\) counts **ordered, independently chosen idempotents** with repetitions allowed, and is fixed in each asymptotic statement. The continuous weight \(u\) is an analytic interpolation of the integer moments.

## Proof

**1. Idempotents and their relative centralizers.** If \(f^2=f\) and \(f\) is injective, then \(f(f(i))=f(i)\) implies \(f(i)=i\) by injectivity, for every \(i\in\operatorname{dom}(f)\). Hence \(f\) is the identity restricted to its domain, and conversely every such partial identity is idempotent. Denote by \(e_B\) the identity on \(B\subseteq[n]\). The equality \(fe_B=e_Bf\) holds precisely when, for all \(i\in\operatorname{dom}(f)\), \(i\in B\) if and only if \(f(i)\in B\). This is an equality of partial functions, including their domains.

Draw a directed edge \(i\to f(i)\) whenever \(f(i)>i\). Each vertex has at most one incoming and one outgoing edge (injectivity and single-valuedness), and edges strictly increase, so this graph is a disjoint union of directed paths and isolated vertices. There are \(r(f)\) edges and hence \(n-r(f)\) connected components. The admissible subsets \(B\) are precisely unions of components, giving \(c_E(f)=2^{n-r(f)}\). In particular, the complete multiplicity of each possible relative idempotent-centralizer size is read from \(F_n(u)\).

**2. Strict transformations and Narayana coefficients.** A map with no fixed point is strictly extensive on its domain. For an interval of length \(m\), subtracting one from every image gives a bijection between strictly extensive order-preserving partial injections of \([m]\) and all elements of \(IC_{m-1}\), preserving their number of nonempty arrows (rank). For \(m\geq1\), the number of rank-\(r\) elements of \(IC_{m-1}\) is the number of pairs of \(r\)-subsets \(D,I\subseteq[m-1]\) whose corresponding sorted entries satisfy \(d_j\leq b_j\). The classical first-violation reflection bijection gives
\[
 \binom{m-1}{r}^2-\binom{m-1}{r-1}\binom{m-1}{r+1}
 =\frac1m\binom mr\binom m{r+1}.
\]
This remains valid for \(r=0\) and \(r=m-1\), interpreting out-of-range binomial coefficients as zero. Therefore the strict-map polynomial is \(S_m(u)\) as stated, with \(S_0=1\). Let \(R=S-1\). Lagrange inversion of \(R=z(1+R)(1+uR)\) gives exactly the displayed Narayana coefficients and, equivalently, \(S=1+zS(1-u+uS)\).

**3. Inserting fixed points.** If \(f(j)=j\), order preservation forces every domain point below \(j\) to map below \(j\), and every domain point above \(j\) to map above \(j\). Hence its fixed points split the chain uniquely into consecutive gaps carrying independent strictly extensive partial injections. If there are \(s\) fixed points, there are \(s+1\) gaps; the weight of the chosen fixed points is \(z^s\) and the gap weight is \(S^{s+1}\). Summing over \(s\geq0\) proves
\[
 F=\sum_{s\geq0}z^sS^{s+1}=\frac{S}{1-zS}.
\]
The graph computation in step 1 gives \(T_{n,k}=\sum_f c_E(f)^k=2^{kn}F_n(2^{-k})\). At \(u=1\), the quadratic gives \(S(z,1)=C(z)\), the Catalan series; \(F(z,1)=C(z)^2\), so \(F_n(1)=C_{n+1}=|IC_n|\), fixing the probability normalization.

**4. Singularity analysis with boundaries.** For \(u>0\), the power-series branch is
\[
 S(z,u)=\frac{1-(1-u)z-\sqrt{[1-(1-u)z]^2-4uz}}{2uz}.
\]
Its first branch point is \(\rho=(1+\sqrt u)^{-2}\), where \(S(\rho,u)=(1+\sqrt u)/\sqrt u\). The denominator \(1-zS\) can vanish on the physical branch before \(\rho\) exactly when \(u<u_*\): its only candidate positive zero is \(z_p=(1-u)/(2-u)\), and it is attained on that branch if and only if \(1-3u+u^2>0\). At such a zero, differentiation of \(S=1+zS(1-u+uS)\) shows that the coefficient of \((1-z/z_p)^{-1}\) in \(F\) is \((1-3u+u^2)/(1-u)^2\). When \(u>u_*\), the denominator does not vanish at or before \(\rho\), and the coefficient of \(-\sqrt{1-z/\rho}\) in \(F\) equals \(\sqrt v(1+v)^3/(v^2+v-1)^2\), where \(v=\sqrt u\). The square-root transfer theorem gives the \(n^{-3/2}\) asymptotic. At equality \(u=u_*\), the denominator vanishes to square-root order, giving the displayed \(n^{-1/2}\) coefficient. Positivity and the presence of coefficients in consecutive degrees rule out competing same-modulus dominant singularities; the next algebraic singularity is farther away.

Finally \(C_{n+1}\sim 4^{n+1}/(\sqrt\pi n^{3/2})\). Division gives the two separate formulas for \(P_{n,k}\). Since \(2^{-1}>u_*>2^{-2}\), the moment-order change occurs sharply between \(k=1\) and \(k=2\).

## Verification

The standalone Python 3 file `verify.py` enumerates partial injections independently from pairs of increasing subsets, computes compositions of partial functions directly, and tests the commutation equations. It checks the complete nonfixed-edge distribution for \(1\le n\le8\), direct one-idempotent commuting counts through \(n=7\), direct simultaneous two-idempotent counts through \(n=5\), and three-idempotent counts through \(n=4\). It also checks the Catalan cardinalities and the Narayana-convolution coefficients. Running `python3 verify.py` prints `VERIFY_OK`. These are finite cross-checks, not the proof of the universal or asymptotic theorems.

For instance,
\[
 F_4(u)=16+17u+8u^2+u^3.
\]
Thus in the \(42\)-element monoid \(IC_4\), exactly \(5316\) ordered triples consisting of an element and two commuting idempotents satisfy the simultaneous commutation conditions, out of \(42\cdot 16^2=10752\) possible triples; the probability is \(443/896\).

## Relationship to prior work

Sapir and Volkov, arXiv:2211.12952v1 (23 November 2022), establish the prominence of \(IC_4\) in the finite-basis problem and define the entire family \(IC_n\); their Appendix A gives the classical \(C_{n+1}\) cardinality. Their inspected sections concern identities and cardinalities, not relative idempotent commutants or multi-idempotent moment asymptotics. The Catalan/Narayana ranks in step 2 are established enumerative ingredients, not claimed to be new.

The **exact** one-idempotent commuting-pair totals \(1,4,18,86,426,2162,\ldots\) coincide with OEIS A225887, which already records their ordinary generating function and \(n^{-3/2}\) asymptotic from unrelated Schröder-path interpretations. Those numerical and analytic \(k=1\) facts are explicitly regarded as prior coverage here. Oste and Van der Jeugt's 2015 work supplies general weighted Motzkin/Schröder-path generating-function machinery; the weighted lattice-path theory is likewise not claimed as new. The present monoid-specific idempotent-centralizer spectrum and exact \(k\ge2\) simultaneous commutation probabilities, including the pole-versus-branch transition and its constants, are not stated in these inspected sources and do not follow from the **single specialization** in A225887 alone.

Al-Kharousi, Umar, and Zubairu (arXiv:2501.00285v1, 31 December 2024) study the **same injective partial Catalan monoid**, expressed with order-decreasing rather than extensive maps; reversing the chain order identifies the two conventions. The complete available arXiv HTML text was checked, including the definitions, Green relations, generation and rank theorems, and maximal subsemigroups. Its shift statistic is structurally related to the strict-arrow count, but its stated results do **not** determine how many partial-identity idempotents commute with an element or the joint centralization probabilities for \(k\geq2\). In particular, these counts are not a corollary of its total cardinality or its generator-rank formulas.

Stein's arXiv:1812.01300 studies representation theory of monoid algebras for order-preserving and order-decreasing partial functions, permitting noninjective maps; its inspected claims concern quiver presentations, Cartan matrices, and Loewy length, not the present \(i\)-Catalan centralization statistic. Searches for the same claim under the phrases “injective Catalan”, “partial order-preserving extensive injections”, “idempotent centralizer”, “Narayana commutation”, “simultaneous idempotents”, and “golden ratio singularity” located no earlier statement of the combined theorem. This is evidence of noncoverage in the inspected material, not proof of worldwide publication priority.

## Limitations

The exact distribution is for **centralizing idempotents**, not the sizes of full element-centralizers in \(IC_n\). The moment asymptotics take \(k\) fixed as \(n\to\infty\); joint limits in which \(k\) grows with \(n\) are not addressed. The \(k=1\) enumerator and asymptotic are known, and the Narayana and weighted Schröder machinery is classical. An equivalent combinatorial form of the \(k\ge2\) formulas might occur in broader colored-lattice-path or monoid literature under different terminology. No independent mathematical audit or priority certification has been performed.

## References

1. O. B. Sapir and M. V. Volkov, *Catalan monoids inherently nonfinitely based relative to finite \(\mathcal R\)-trivial semigroups*, arXiv:2211.12952v1, first publicly available 23 November 2022, especially Section 2 and Appendix A.
2. N. J. A. Sloane et al., OEIS A225887, full sequence, generating function, asymptotic, and Schröder-path interpretations (entry created 2013; relevant notes 2016–2017), https://oeis.org/A225887.
3. R. Oste and J. Van der Jeugt, *Motzkin Paths, Motzkin Polynomials and Recurrence Relations*, Electronic Journal of Combinatorics 22(2) (2015), P2.8, especially Sections 6–7, https://doi.org/10.37236/4781.
4. F. S. Al-Kharousi, A. Umar, and M. M. Zubairu, *On injective partial Catalan monoids*, arXiv:2501.00285v1, first public 31 December 2024 (later revisions consulted).
5. I. Stein, *Representation theory of order-related monoids of partial functions as locally trivial category algebras*, arXiv:1812.01300v1, first public 4 December 2018.

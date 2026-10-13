# Sharp \(3/2\) separation of parity-conditioned modes for Poisson-trinomial sums

## Finding

**Theorem (sharp parity-mode localization).** Let \(n\ge1\) and let \(X_1,\ldots,X_n\) be independent, not necessarily identically distributed, random variables taking values in \(\{0,\frac12,1\}\). Put \(X=\sum_{i=1}^{n}X_i\). Assume both \(\Pr(X\in\mathbb Z)>0\) and \(\Pr(X\in\mathbb Z+\frac12)>0\). Write
\[
 P(z)=\sum_{k=0}^{n}\Pr(X=k)z^k,\qquad
 Q(z)=\sum_{k=0}^{n-1}\Pr(X=k+\tfrac12)z^k.
\]
Let \(E\) and \(O\) be the complete sets of integer indices at which the coefficients of \(P\) and \(Q\), respectively, attain their maxima. They are also the modal index sets of the two corresponding normalized parity-conditioned distributions. Write \(a=\min E\) and \(b=\max E\). Then \(b-a\le1\), and the **entire odd modal index set obeys**
\[
  O\subseteq\{a-1,a,\ldots,b\}\cap\mathbb Z.
\]
Consequently, for **every** integer-supported conditional mode \(m_e\in E\) and every half-integer-supported conditional mode \(m_o=j+\frac12\), \(j\in O\),
\[
  |m_e-m_o|\le\frac32.
\]
If the integer-conditioned law has a unique mode \(m\), every half-integer-conditioned mode is one of \(m-\frac12\) and \(m+\frac12\), and hence its distance from \(m\) is exactly \(\frac12\).

The constant \(\frac32\) is best possible for **every** \(n\ge2\). For \(n=1\), the sharp constant is \(\frac12\). These assertions include arbitrary zero probabilities at individual outcomes, subject only to the two positive parity probabilities.

## Assumptions and scope

Set \(L_i=\Pr(X_i=0)\), \(T_i=\Pr(X_i=\frac12)\), \(W_i=\Pr(X_i=1)\), with \(L_i,T_i,W_i\ge0\) and \(L_i+T_i+W_i=1\). Conditional mode means any maximizer of the conditional mass function; ties are retained rather than broken arbitrarily. Thus a distribution with two adjacent maxima contributes *both* to its modal set. The theorem concerns these two parity-conditioned laws, **not** modes of the unconditioned interlaced distribution. All comparisons are in the original point-score units \(0,\frac12,1\).

## Proof

**Step 1: Even and odd polynomials have a common real-rooted structure.** First suppose \(L_i,T_i,W_i>0\) for every \(i\). The probability generating polynomial of \(2X\) is
\[
 G(w)=\prod_{i=1}^{n}(L_i+T_iw+W_iw^2)=P(w^2)+wQ(w^2).
\]
Every quadratic factor has both zeros in the open left half-plane: its nonreal roots have real part \(-T_i/(2W_i)<0\), and when its roots are real, they are both negative. Thus \(G\) is Hurwitz stable. The **strict** Hermite--Biehler theorem gives that \(P\), of degree \(n\), and \(Q\), of degree \(n-1\), have simple, strictly negative real zeros, with the zeros of \(Q\) strictly interlacing those of \(P\). This is a classical theorem, not a newly asserted lemma; see Ellard--Šmigoc and the Hermite--Biehler discussion in Broadie--Petkova.

Write the zeros of \(P\) as \(-r_1,\ldots,-r_n\), where \(0<r_1<\cdots<r_n\). By positivity of its coefficients and normalization, we have the Poisson-binomial factorization
\[
  \frac{P(z)}{P(1)}=\prod_{j=1}^{n}\frac{z+r_j}{1+r_j}
      =\prod_{j=1}^{n}\bigl[(1-p_j)+p_jz\bigr],
  \qquad p_j=\frac1{1+r_j}\in(0,1).
\]
Thus the normalized coefficients of \(P\) are the law of \(S=\sum_{j=1}^{n}B_j\), where \(B_j\) are independent Bernoulli variables with parameters \(p_j\).

**Step 2: The odd law is a positive mixture of single-Bernoulli deletions.** Since \(Q/P\) is a proper rational function with simple poles at the negative zeros of \(P\),
\[
 \frac{Q(z)}{P(z)}=\sum_{j=1}^{n}\frac{c_j}{z+r_j},\qquad
 c_j=\frac{Q(-r_j)}{P'(-r_j)}>0.
\]
The strict positivity follows because the zeros of \(Q\) separate successive zeros of \(P\): the numerator and denominator in the residue have the same alternating sign. Define
\[
 D_j(z)=\prod_{k\ne j}\bigl[(1-p_k)+p_kz\bigr],\qquad
 \omega_j=\frac{c_j/(1+r_j)}{\sum_{h=1}^{n}c_h/(1+r_h)}.
\]
Each \(D_j\) is the generating function of the Poisson-binomial sum \(S-B_j\), and \(\omega_j>0\), \(\sum_j\omega_j=1\). Substituting the factorization of \(P\) into the partial fractions and evaluating at \(z=1\) proves the **exact distributional identity**
\[
  \frac{Q(z)}{Q(1)}=\sum_{j=1}^{n}\omega_j D_j(z).
\]
In particular, the half-integer law, after its one-half shift, is a convex mixture of the distributions obtained by deleting one Bernoulli factor from the integer-conditioned law. This positive-deletion mixture, rather than merely the two laws' separate mean bounds, is the crucial comparison.

**Step 3: Deleting one Bernoulli cannot move a mode outside the adjacent modal envelope.** We prove the following elementary lemma, including deterministic Bernoulli variables. Suppose \(S=B+D\), where \(B\) is Bernoulli, \(D\) is a sum of independent Bernoulli variables, and \(B\) and \(D\) are independent. Suppose the complete modal set of \(S\) consists of consecutive integers from \(a\) to \(b\). Then **every** mode of \(D\) lies in \(\{a-1,\ldots,b\}\).

Indeed, let \(d(k)=\Pr(D=k)\), \(s(k)=\Pr(S=k)\), and \(p=\Pr(B=1)\). The convolution identity is
\[
 s(k)=(1-p)d(k)+p\,d(k-1).
\]
Both \(d\) and \(s\) are unimodal, and \(s(a)>s(a-1)\), \(s(b)>s(b+1)\), with probabilities outside the support understood as zero. If \(d\) had a mode \(t\le a-2\), unimodality would imply \(d(a)\le d(a-1)\le d(a-2)\), whence \(s(a)\le s(a-1)\), a contradiction. Likewise, if it had a mode \(t\ge b+1\), we would have \(d(b+1)\ge d(b)\ge d(b-1)\), giving \(s(b+1)\ge s(b)\), another contradiction. This proves the lemma.

Every Poisson-binomial law has at most two adjacent modes: its nonzero coefficients obey Newton's strict ultra-log-concavity for a product of linear factors with nonnegative coefficients, preventing three consecutive equal positive maxima. This is also the standard Poisson-binomial modal fact used by Broadie--Petkova. Let the full modal set of \(P/P(1)\) be \(E=\{a,\ldots,b\}\) with \(b-a\le1\). The lemma shows that each \(D_j\) has all its modes in \([a-1,b]\). By unimodality, each deletion mass function is nondecreasing to the left of this interval and nonincreasing to its right. More precisely, a positive mass strictly outside cannot equal its mass at the nearest interval endpoint, since equality across a nontrivial distance would give a modal plateau outside the interval by log-concavity. Consequently, their positive convex mixture has no global modal index outside \([a-1,b]\). Step 2 now yields \(O\subseteq[a-1,b]\cap\mathbb Z\).

**Step 4: Boundary probabilities.** For arbitrary allowable triples, replace each \((L_i,T_i,W_i)\) by \((1-\varepsilon)(L_i,T_i,W_i)+\varepsilon(\frac14,\frac12,\frac14)\). The perturbed laws satisfy the strict-interior assumptions; both normalized parity polynomials converge coefficientwise to the original normalized polynomials because both original parity probabilities are positive. For each perturbation, Step 2 supplies Bernoulli parameters in \([0,1]^n\) and mixture weights in the compact \(n\)-simplex. Sort the Bernoulli parameters and choose a convergent subsequence of both the parameters and weights. In the limit, the original \(P/P(1)\) is the generating function of the limit Bernoulli sum, and \(Q/Q(1)\) remains a convex mixture of its \(n\) deletion laws. Step 3 therefore applies directly to the original limiting modal set, with no illicit assumption that modes themselves vary continuously. This proves the localization for all allowed boundary distributions.

**Step 5: Distances and optimality.** Since \(E\subseteq\{a,b\}\), with \(b-a\le1\), and every odd modal score is \(j+\frac12\) for \(j\in[a-1,b]\), any cross-parity modal distance is at most \(\frac32\). If \(a=b=m\), the only possibilities are \(j=m-1,m\), giving exactly \(\frac12\) distance.

For sharpness, take two independent trials with
\[
 (L_1,T_1,W_1)=(0,\tfrac14,\tfrac34),\qquad
 (L_2,T_2,W_2)=(\tfrac12,0,\tfrac12).
\]
Their unnormalized generating polynomial is
\[
 G(w)=(\tfrac14w+\tfrac34w^2)(\tfrac12+\tfrac12w^2)
      =\tfrac18w+\tfrac38w^2+\tfrac18w^3+\tfrac38w^4.
\]
Hence the integer-conditioned modes are \(1,2\), and the half-integer-conditioned modes are \(\frac12,\frac32\). The extreme pair \(2\) and \(\frac12\) is separated by \(\frac32\). Adjoining any number of zero-valued independent variables gives equality for every \(n\ge2\). For \(n=1\), the half-integer-conditioned law is concentrated at \(\frac12\), whereas every integer-conditioned mode is \(0\) or \(1\), giving exactly \(\frac12\). All cases are proved.

## Verification

Run the complete standalone exact-arithmetic checker using `python3 verify_modal_gap.py`. It enumerates all admissible triples on the quarter-probability grid for \(n=1,2,3,4\), including endpoints and tied modes, and checks the full modal containment, the separation bound, and the unique-even-mode refinement. The observed admissible-case counts are \(9,189,3159,49329\), totaling \(52686\), with largest modal distances respectively \(\frac12,\frac32,\frac32,\frac32\). It separately verifies the explicit sharpness polynomial with integer coefficients \((0,2,6,2,6)\) before normalization by \(16\). These **finite** calculations independently check the examples and many boundary configurations; Steps 1--5, not the enumeration, establish the assertion for arbitrary \(n\) and arbitrary real probabilities.

## Relationship to prior work

Broadie and Petkova (2026), Theorem 1 and Proposition 3, introduced the parity-conditioned Poisson-trinomial viewpoint and proved the general modal separation upper bound \(\frac52\), using proximity of each conditional mode to the unconditional mean. Their Section 3 already establishes the separate Poisson-binomial factorizations via Hurwitz stability and Hermite--Biehler, which are **not** claimed here as discoveries. The new statement sharpens \(\frac52\) to the **attained** constant \(\frac32\), and further locates all odd-mode indices relative to the *exact entire modal interval* of the integer-conditioned law. In particular, it proves nearest-neighbor behavior when the integer-conditioned mode is unique, which is not implied by the earlier mean bounds.

Ellard and Šmigoc (2017), Theorem 1.1, explicitly state the classical zero-interlacing portion of Hermite--Biehler. That theorem alone describes roots, not parity-conditioned modal distances or the attained constant. The bridge used here is the positive partial-fraction/deletion-mixture representation and the deletion-mode localization lemma. Classical Darroch (1964) bounds a single Poisson-binomial mode relative to its mean, but does not itself compare these two linked conditional modal sets. No independent priority claim is made beyond the stated mathematical comparison; an equivalent earlier specialized corollary in less searchable literature remains possible.

## Limitations

The bound is for independent \(\{0,\frac12,1\}\)-valued summands and requires both conditioning events to have positive probabilities. It does not assert a modal separation for arbitrary dependent three-point summands, wider outcome alphabets, the unconditional mass function, or a corresponding sharp bound on conditional means. This is a mathematical derivation checked against the identified sources, not independent third-party validation. The finite checker cannot establish an infinite-parameter theorem by itself. A preexisting equivalence under different terminology cannot be ruled out solely by literature searches.

## References

1. Mark Broadie and Ina Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1 (submitted 9 March 2026), especially Theorem 1, Section 3, and Proposition 3; https://arxiv.org/pdf/2603.09019.
2. Richard Ellard and Helena Šmigoc, *An extension of the Hermite-Biehler theorem with application to polynomials with one positive root*, arXiv:1701.07912v1 (2017), Theorem 1.1; https://arxiv.org/pdf/1701.07912.
3. J. N. Darroch, *On the distribution of the number of successes in independent trials*, Annals of Mathematical Statistics **35** (1964), 1317–1321, as cited and applied in Broadie--Petkova, Theorem 4.

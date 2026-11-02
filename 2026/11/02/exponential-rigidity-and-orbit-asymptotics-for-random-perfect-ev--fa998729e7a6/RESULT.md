# Exponential rigidity and orbit asymptotics for random perfect evolution algebras

## Finding

Fix a prime power \(q\ge 2\). For each integer \(n\ge 1\), let \(M\) be uniform on \(\operatorname{GL}_n(\mathbb F_q)\) and let \(E_M\) be the evolution algebra with natural basis \(e_1,\ldots,e_n\), pairwise products \(e_i e_j=0\) for \(i\ne j\), and
\[
e_i^2=\sum_{j=1}^{n}M_{ij}e_j.
\]
Let \(K_{n,q}\) be the number of isomorphism classes of perfect \(n\)-dimensional evolution algebras over \(\mathbb F_q\), and put
\[
p_{n,q}=\prod_{j=1}^{n}(1-q^{-j}).
\]
Define \(b_{n,2}=0\) and, for \(q>2\),
\[
b_{n,q}=n(q-2)q^{-\lfloor n/(q-2)\rfloor},\qquad
\Delta_{n,q}=\sum_{s=1}^{n}b_{n,q}^{s}
 +(q-1)^n\sum_{s=2}^{n}n^{s}q^{-\lceil s(2n-s)/2\rceil}.
\]
Empty sums are zero. Then the following two bounds hold simultaneously:
\[
\begin{aligned}
\Pr\bigl(\operatorname{Aut}(E_M)\ne\{1\}\bigr)
&\le \mathbb E\bigl[|\operatorname{Aut}(E_M)|-1\bigr]
\le \frac{\Delta_{n,q}}{p_{n,q}},\\
0\le \frac{n!(q-1)^nK_{n,q}}{|\operatorname{GL}_n(\mathbb F_q)|}-1
&\le \frac{\Delta_{n,q}}{p_{n,q}}.
\end{aligned}
\]
For every fixed prime power \(q\), \(\Delta_{n,q}\to0\) exponentially as \(n\to\infty\). Thus a uniformly sampled perfect evolution algebra is automorphism-rigid with probability tending to one, and
\[
\boxed{K_{n,q}\sim\frac{q^{n^2}}{n!(q-1)^n}
\prod_{j=1}^{\infty}(1-q^{-j})}
\qquad(n\to\infty,\ q\text{ fixed}).
\]
The asymptotic classification is of isomorphism classes, not of labeled structure matrices.

## Assumptions and scope

A finite-dimensional evolution algebra is an algebra admitting a basis with zero products of distinct basis vectors; it need not be associative. Perfect means \(E^2=E\), equivalent here to \(\det M\ne0\). Every prime power is allowed, including \(q=2\), and the limiting variable is dimension \(n\) with \(q\) fixed. Automorphisms are \(\mathbb F_q\)-linear algebra automorphisms. The probability and expectation concern the uniform distribution on invertible structure matrices in a specified natural basis. Since changes of natural basis preserve uniformity under the induced action, the event that the algebra has a nontrivial automorphism is intrinsic.

## Proof

**1. Every automorphism is monomial.** Since \(M\) is invertible, the squares \(e_1^2,\ldots,e_n^2\) are linearly independent. Write an automorphism \(\phi(e_i)=\sum_a u_{ai}e_a\). For \(i\ne j\), multiplying gives \(0=\phi(e_i)\phi(e_j)=\sum_a u_{ai}u_{aj}e_a^2\). Independence implies \(u_{ai}u_{aj}=0\) for every row \(a\). Each row of the invertible matrix \(U=(u_{ai})\) therefore has precisely one nonzero entry, and invertibility forces one per column too. Consequently there is a unique permutation \(\sigma\in S_n\) and unique nonzero scalars \(t_1,\ldots,t_n\) with \(\phi(e_i)=t_i e_{\sigma(i)}\).

Comparing \(\phi(e_i^2)\) with \(\phi(e_i)^2\) now gives the necessary and sufficient fixed-matrix equations
\[
 t_i^2M_{\sigma(i),\sigma(j)}=t_jM_{ij}
 \qquad(1\le i,j\le n).\tag{1}
\]
Every such monomial map is invertible and preserves the entire multiplication, so these solutions count the automorphisms exactly. The acting monomial group has order \(n!(q-1)^n\).

**2. Average over all matrices first.** Let \(\widetilde M\) have \(n^2\) independent uniform entries in \(\mathbb F_q\), without a determinant restriction. The event \(\det\widetilde M\ne0\) has probability \(p_{n,q}\). For a fixed nonidentity monomial map \((\sigma,t)\), equation (1) is a system of restrictions on the entries of \(\widetilde M\). We bound its satisfaction probability and then divide by \(p_{n,q}\) to obtain a bound after conditioning on invertibility.

**3. Nonidentity permutation.** Suppose \(\sigma\) moves \(s\ge2\) points. Under the simultaneous permutation of both matrix indices, \((i,j)\mapsto(\sigma(i),\sigma(j))\), exactly \((n-s)^2\) pairs are fixed and every other orbit has length at least two. Thus the number of index orbits is at most
\[
\frac{n^2+(n-s)^2}{2}
 =n^2-\frac{s(2n-s)}2.
\]
Because all \(t_i\) are nonzero, equation (1) relates the values on each orbit by invertible multipliers. There are at most \(q\) choices per orbit, possibly fewer if the multipliers have inconsistent product around the orbit. Therefore
\[
\Pr\bigl((1)\text{ holds for fixed }(\sigma,t)\bigr)
\le q^{-\lceil s(2n-s)/2\rceil}.
\]
At most \(n^s\) permutations move exactly \(s\) points, and there are \((q-1)^n\) scaling vectors. The total contribution of all maps with nonidentity permutation to the expected number of nonidentity solutions is no greater than the second sum in \(\Delta_{n,q}\).

**4. Identity permutation with nontrivial scaling.** For \(q=2\), no such scaling exists. Assume \(q>2\), take \(\sigma=1\), and let \(s\ge1\) of the scalars \(t_i\) differ from one. Equation (1) becomes \((t_i^2-t_j)M_{ij}=0\). Every entry from a row with \(t_i=1\) to a column with \(t_j\ne1\) must vanish, giving \(s(n-s)\) forbidden entries. For each fixed exotic scalar \(c\ne1\), every entry with both its row and column bearing scalar \(c\) must vanish, since \(c^2\ne c\). If \(m_c\) is the multiplicity of \(c\), these contribute \(\sum_{c\ne1}m_c^2\) additional, disjoint forbidden entries. By Cauchy–Schwarz,
\[
F(t)\ge s(n-s)+\sum_{c\ne1}m_c^2
\ge s(n-s)+\frac{s^2}{q-2}
\ge \frac{sn}{q-2}.
\]
The fixed-map probability is exactly \(q^{-F(t)}\), as all forbidden matrix entries are independent. There are \(\binom ns(q-2)^s\le[n(q-2)]^s\) choices with \(s\) exotic scalars. Summing over \(s\) and weakening the exponent using \(\lfloor n/(q-2)\rfloor\) gives the first sum in \(\Delta_{n,q}\).

**5. Conditioning and orbit count.** In the full matrix model, linearity of expectation and Steps 3–4 yield an expected number of nonidentity monomial solutions no greater than \(\Delta_{n,q}\). After conditioning on invertibility this expected number is at most \(\Delta_{n,q}/p_{n,q}\). By Step 1 it equals \(\mathbb E(|\operatorname{Aut}(E_M)|-1)\); its probability of being positive is at most its mean. This proves the first displayed bound.

The monomial group acts on the invertible structure matrices by change of natural basis, and its orbits are precisely the isomorphism classes. Burnside's lemma gives
\[
K_{n,q}=\frac{1}{n!(q-1)^n}
\sum_{M\in\operatorname{GL}_n(\mathbb F_q)}
 |\operatorname{Aut}(E_M)|.
\]
Dividing by \(|\operatorname{GL}_n(\mathbb F_q)|/[n!(q-1)^n]\) yields \(\mathbb E|\operatorname{Aut}(E_M)|\); the second bound follows.

**6. Limit.** For each fixed \(q\), the infinite product \(p_{\infty,q}=\prod_{j\ge1}(1-q^{-j})\) is strictly positive; hence \(p_{n,q}\ge p_{\infty,q}\). When \(q>2\), \(b_{n,q}=O_q(nq^{-n/(q-2)})\), so the first sum tends to zero exponentially. For the other sum, \(\lceil s(2n-s)/2\rceil\ge sn/2\) for \(2\le s\le n\). If \(h_{n,q}=nq^{-n/2}\), then for sufficiently large \(n\), \(h_{n,q}<1/2\) and
\[
(q-1)^n\sum_{s=2}^{n}n^sq^{-\lceil s(2n-s)/2\rceil}
\le(q-1)^n\frac{h_{n,q}^2}{1-h_{n,q}}
\le2n^2(1-q^{-1})^n.
\]
Thus \(\Delta_{n,q}\to0\) exponentially, also for \(q=2\). Finally \(|\operatorname{GL}_n(\mathbb F_q)|=q^{n^2}p_{n,q}\), and the asserted isomorphism-class asymptotic follows.

## Verification

Two independently structured standalone Python checkers accompany this proof and use only the standard library. The first enumerates every structure matrix over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\) in dimensions two and three, tests invertibility, and checks each monomial map by directly comparing images of basis squares. The second independently enumerates fixed matrices of the monomial equations, comparing direct enumeration with an index-orbit counting method. Both return `VERIFY_OK` and match their recorded outputs.

For \((q,n)=(2,2),(2,3),(3,2),(3,3)\), the pairs \((|\operatorname{GL}_n(\mathbb F_q)|,K_{n,q})\) are respectively \((6,4),(168,33),(48,7),(11232,249)\). The corresponding counts of matrices with a nontrivial automorphism are \(2,24,8,576\). The finite computations corroborate the proof; no limit is inferred solely from these samples. For prime powers other than primes, the proof, not these particular runs, supplies the result.

## Relationship to prior work

The monomial-automorphism description and finite-field orbit-action framework are classical in this subject. Wei and Zou (2023) give a Burnside counting identity for the number of perfect evolution-algebra isomorphism classes at finite dimension, and explicit low-dimensional formulas. The present finding does not claim that identity or any small-dimensional count as new: it supplies an explicit exponentially decaying bound for the **expected number of nonidentity automorphisms** in the fixed-field, growing-dimension regime, thereby proving that the orbit action is asymptotically free and evaluating the large-dimensional orbit asymptotic. An exact unevaluated Burnside sum does not itself furnish the needed stabilization estimates.

Costoya, Mayorga, and Viruel (2025) analyze automorphism permutation representations rather than typical automorphism groups in the random finite-field model. Kaygorodov, Martín González, and Viruel (2026), Question 22, explicitly identify random evolution-algebra automorphism probabilities as a direction for investigation. This theorem resolves the perfect, uniform-structure-matrix part of that question; it does not resolve the full unrestricted random-matrix model.

## Limitations

The field size \(q\) is fixed while \(n\to\infty\); the proof does not establish a joint \(q,n\)-limit. It applies to perfect algebras, not arbitrary singular structure matrices. The upper bound is not claimed sharp. The count is of ordinary algebra isomorphism classes, not isotopy classes or automorphism group schemes. The proof establishes a new quantitative conclusion relative to the inspected sources; exhaustive historical priority is not independently certified.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), especially Question 22; https://arxiv.org/html/2610.22248 . Primary MSC2020: 17A60.
2. Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (first posted 2023-10-18), Sections 1–3, especially the monomial action and Burnside formula; https://arxiv.org/pdf/2310.12368 .
3. C. Costoya, P. Mayorga, A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics 22 (2025), article 149, published 2025-07-29; https://doi.org/10.1007/s00009-025-02924-0 .
4. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (first posted 2013-12-17); https://arxiv.org/abs/1312.4685 .

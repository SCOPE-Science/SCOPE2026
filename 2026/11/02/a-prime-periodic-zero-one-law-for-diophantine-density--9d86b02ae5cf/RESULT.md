# A prime-periodic zero--one law for Diophantine density

## Finding
For any prime \(\ell\) and any subset \(R\subseteq\mathbb Z/\ell\mathbb Z\), define
\[
A_R=\{v\in\mathbb N:v\bmod\ell\in R\}.
\]
With the Diophantine density \(\delta\) introduced in [1, 2], there is an exact zero--one law:
\[
\boxed{\delta(A_R)=1\quad\Longleftrightarrow\quad
0\in R\ \text{or}\ R=(\mathbb Z/\ell\mathbb Z)^\times.}
\]
For every other \(R\), the density is zero. In particular, the set of positive integers avoiding exactly two residue classes, \(0\) and one nonzero residue \(t\), has ordinary asymptotic density \((\ell-2)/\ell\) but Diophantine density zero. Adding either missing residue class makes its Diophantine density one.

## Assumptions and scope
The prime \(\ell\) is arbitrary, including \(\ell=2\); the residue subset \(R\) may be empty. We take \(\mathbb N=\{1,2,\ldots\}\), and \(\|x\|\) denotes distance to the nearest integer. For any set \(A\subseteq\mathbb N\), its Diophantine density is the supremum of exponents \(\eta\ge0\) for which a constant \(C>0\) and a threshold \(q_0\) exist such that, for every coprime \((p,q)\in\mathbb Z\times\mathbb N\) with \(q\ge q_0\),
\[
\min_{v\in A,\ 1\le v<q}\left\|\frac{vp}{q}\right\|\le Cq^{-\eta}.
\]
The empty set has density zero by definition. For nonempty periodic sets, the minimum is defined for all sufficiently large \(q\). This theorem concerns complete unions of residue classes for *prime* moduli, not arbitrary composite moduli or modified sets.

## Proof
**Universal upper bound.** If \(p\) and \(q\) are coprime, then \(vp\not\equiv0\pmod q\) for every \(1\le v<q\). Thus \(\|vp/q\|\ge1/q\), so \(\delta(A)\le1\) for every \(A\subseteq\mathbb N\) with a nonempty defining minimum.

**First sufficient condition.** If \(0\in R\), the multiples of \(\ell\) lie in \(A_R\). For \(q>\ell\), apply Dirichlet's pigeonhole inequality to \(\ell p/q\) with \(N=\lfloor(q-1)/\ell\rfloor\). Some \(1\le j\le N\) obeys \(\|j\ell p/q\|\le1/(N+1)\le\ell/q\); taking \(v=j\ell<q\) proves \(\delta(A_R)=1\).

**Second sufficient condition.** Suppose \(R=(\mathbb Z/\ell\mathbb Z)^\times\). Let \(u\in\{1,\ldots,q-1\}\) be the inverse of \(p\) modulo \(q\). If \(\ell\nmid u\), take \(v=u\); otherwise, since \(\gcd(u,q)=1\), one has \(\ell\nmid q\) and hence \(\ell\nmid(q-u)\), so take \(v=q-u\). In both cases \(v\in A_R\), \(1\le v<q\), and \(vp\equiv\pm1\pmod q\). This gives \(\|vp/q\|=1/q\) and therefore \(\delta(A_R)=1\).

**Necessity.** Now suppose \(0\notin R\) and \(R\ne(\mathbb Z/\ell\mathbb Z)^\times\). If \(R=\varnothing\), the definition gives zero. Otherwise choose \(t\in(\mathbb Z/\ell\mathbb Z)^\times\setminus R\), and choose the representative \(a\in\{1,\ldots,\ell-1\}\) of \(-t^-1\) modulo \(\ell\). There are infinitely many positive integers \(q\) satisfying \(a q\equiv-1\pmod\ell\). For each, set \(p=(a q+1)/\ell\). Then \(\ell p-aq=1\), so \(\gcd(p,q)=1\). For any \(v\in A_R\) with \(0<v<q\), let \(k\in\{1,\ldots,\ell-1\}\) be the residue \(av\bmod\ell\). Since \(v\not\equiv0,t\pmod\ell\), we have \(1\le k\le\ell-2\). Furthermore,
\[
\frac{vp}{q}=\frac{av}{\ell}+\frac{v}{\ell q},\qquad 0<\frac{v}{\ell q}<\frac1\ell.
\]
The fractional part therefore lies strictly between \(1/\ell\) and \((\ell-1)/\ell\), and consequently
\[
\min_{v\in A_R,\ 0<v<q}\left\|\frac{vp}{q}\right\|\ge\frac1\ell.
\]
The infinitely many coprime pairs with \(q\to\infty\) exclude every positive exponent in the definition; hence \(\delta(A_R)=0\). For \(\ell=2\), the only nonempty subset not containing zero is already the full unit set, so the preceding obstruction case is vacuous.

**Counting and density consequence.** Of the \(2^\ell\) residue subsets, \(2^{\ell-1}\) contain zero, and the only additional full-Diophantine-density subset is the set of all nonzero residues. Thus \(2^{\ell-1}+1\) subsets have value one; the remaining \(2^{\ell-1}-1\), including the empty set, have value zero. If \(R=(\mathbb Z/\ell\mathbb Z)\setminus\{0,t\}\) for \(t\ne0\), standard periodic counting gives ordinary density \((\ell-2)/\ell\) and the zero case above applies. This ordinary density approaches one as the prime grows. \(\square\)

## Verification
The standalone file `verify.py` exhaustively visits all \(172\) residue subsets for the primes \(2,3,5,7\), tests \(99,798\) coprime numerator/denominator instances for the full-density cases, and tests \(2,946\) explicit obstruction pairs for the zero-density cases, including a \(99/101\)-density example. It computes distances by integer modular arithmetic without floating-point rounding. Run `python3 verify.py`. These computations are finite corroboration only; they do not prove the theorem for unbounded moduli or denominators.

## Relationship to prior work
The definition and the full-density multiple-of-a-modulus case occur in Sanford's initial paper [1] and expanded treatment [2]. The latter also gives a zero-density translated-progression example and asks about failure of subadditivity and other properties. A separate earlier single-residue-class classification identifies individual arithmetic progressions with density zero or one and exhibits a union of two zero-density classes having density one. Those statements do not imply the present *simultaneous classification for every union of prime residue classes*: without subadditivity, the invariant of a union cannot be inferred from invariants of its constituents. The present contribution is the finite-field missing-unit obstruction valid uniformly for any subset and the resulting sharp classification. It does not claim discovery of qualitative non-subadditivity.

## Limitations
The statement is restricted to *complete* periodic residue unions with *prime* period, and does not classify arbitrary composite periods, truncated residue classes, or all positive-density sets. No independent expert review or priority certification is claimed. The proof is elementary, so an unindexed or implicit earlier generalization cannot be ruled out.

## References
[1] C. Sanford, *A Note on Diophantine Approximation with Restricted Denominators*, arXiv:2606.02620v1, first publicly posted 2026-05-28, https://arxiv.org/abs/2606.02620.

[2] C. Sanford, *On a Notion of Density Related to Restricted Diophantine Approximation*, arXiv:2610.27497v1, first publicly posted 2026-10-20, https://arxiv.org/abs/2610.27497; particularly Definition 1, Propositions 4--6 and Section 7.

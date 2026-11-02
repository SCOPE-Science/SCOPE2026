# Affine rigidity from unbounded exponential drift: Catalan and Fuss–Catalan value sets

## Finding

**Theorem (unbounded-drift affine rigidity).** Let \((u_n)_{n\ge n_0}\) be positive integers, eventually strictly increasing, and unbounded. Set \(S=\{u_n:n\ge n_0\}\). Suppose that for some real \(\rho>1\),
\[
\lim_{n\to\infty}\frac{u_{n+1}}{u_n}=\rho
\quad\text{and}\quad
\lim_{n\to\infty}(u_{n+1}-\rho u_n)\in\{+\infty,-\infty\}.
\]
Then the complete collection of real affine self-maps of \(S\) is
\[
\{x\mapsto x\}\;\cup\;\{x\mapsto s:s\in S\}.
\]
Here a self-map means an affine function \(f(x)=ax+b\) with real coefficients satisfying \(f(S)\subseteq S\); the displayed constants include all maps of slope zero.

**Hypergeometric corollaries.** For each integer \(r\ge1\), put
\[
F_{r,n}=\frac{1}{rn+1}\binom{(r+1)n}{n}\qquad(n\ge1).
\]
For each pair of integers \(m>\ell\ge1\), put
\[
B_{m,\ell,n}=\binom{mn}{\ell n}\qquad(n\ge1).
\]
Both \(\{F_{r,n}:n\ge1\}\) and \(\{B_{m,\ell,n}:n\ge1\}\) have exactly the identity and their constant maps as real affine endomorphisms. The first family includes ordinary Catalan numbers, and the second includes central binomial coefficients.

## Assumptions and scope

Only eventual strict increase, integral values, positivity, and the two limits in the theorem are required. No recurrence, linearity, or algebraic assumption on \(\rho\) is made. The map need not be integer-affine a priori and need only send the value set into itself, not onto itself. The initial finite portion may contain repetitions, which do not affect the proof; the listed hypergeometric sets are strictly increasing from the given starting indices.

## Proof

**Step 1: slopes are nonnegative integers.** Since \(S\subset\mathbb Z_{>0}\) is unbounded, a negative slope sends sufficiently large elements below zero, impossible. A slope-zero map has constant value in \(S\). Suppose \(a>0\), and take distinct integers \(s,t\in S\). Because every iterate \(f^{\circ k}\) sends \(S\) into itself,
\[
a^k(s-t)=f^{\circ k}(s)-f^{\circ k}(t)\in\mathbb Z\qquad(k\ge1).
\]
The case \(k=1\) forces \(a\in\mathbb Q\). Writing \(a=A/B\) in coprime positive integers gives \(B^k\mid(s-t)\) for every \(k\), whence \(B=1\). Thus \(a\) is a positive integer.

**Step 2: a self-map eventually shifts indices by a fixed amount.** For each sufficiently large \(n\) there is a unique integer \(m(n)\) with \(f(u_n)=u_{m(n)}\). Since \(u_n\to\infty\), also \(m(n)\to\infty\), and
\[
\frac{u_{m(n)}}{u_n}=a+\frac b{u_n}\longrightarrow a.
\]
The ratio condition gives \(u_{n+j}/u_n\to\rho^j\) for every fixed integer \(j\). Moreover \(m(n)-n\) must be bounded: choose \(K\) large with \(\rho^K>2(a+1)\) and \(\rho^{-K}<a/2\). Monotonicity and these fixed-shift limits prevent \(m(n)\ge n+K\) and \(m(n)\le n-K\) for all sufficiently large \(n\). Since only finitely many shifts remain, every shift appearing infinitely often must satisfy \(a=\rho^j\). The values \(\rho^j\) are pairwise distinct, so one unique integer \(j\) occurs eventually and
\[
m(n)=n+j,\qquad a=\rho^j\qquad(n\text{ large}).
\]
Because \(a\) is a positive integer, either \(a=1\), \(j=0\), or \(a>1\), \(j\ge1\).

**Step 3: telescoping forbids nonzero shifts.** Set \(d_n=u_{n+1}-\rho u_n\). For each fixed \(j\ge1\),
\[
u_{n+j}-\rho^j u_n
=\sum_{i=0}^{j-1}\rho^{j-1-i}d_{n+i}.
\]
The sum tends to \(+\infty\) if \(d_n\to+\infty\), and to \(-\infty\) if \(d_n\to-\infty\), since it has finitely many strictly positive weights. But the eventual index shift would make this sum equal to the fixed intercept \(b\), a contradiction. Hence \(j=0\), \(a=1\), and the equality \(u_n+b=u_n\) forces \(b=0\).

**Step 4: a reusable asymptotic test.** Suppose, in addition to integral and eventually strictly increasing values, that for real \(\gamma\ne0\), \(\rho>1\), \(K>0\) and some constant \(c\),
\[
u_n=K\rho^n n^\gamma\bigl(1+c/n+O(n^{-2})\bigr).
\]
Taking the ratio of successive expansions gives
\[
\frac{u_{n+1}}{\rho u_n}=1+\frac\gamma n+O(n^{-2}),
\qquad
u_{n+1}-\rho u_n=\rho K\rho^n n^{\gamma-1}
\bigl(\gamma+O(n^{-1})\bigr).
\]
The latter tends to the infinite limit of sign \(\gamma\), because the exponential factor dominates every fixed power. Thus the theorem applies.

**Step 5: the exact enumerative families.** For \(m>\ell\ge1\), the factorial identity gives the exact quotient
\[
\frac{B_{m,\ell,n+1}}{B_{m,\ell,n}}
=\frac{\prod_{i=1}^{m}(mn+i)}
{\prod_{i=1}^{\ell}(\ell n+i)\prod_{i=1}^{m-\ell}((m-\ell)n+i)}.
\]
Expanding the logarithm of each finite product at large \(n\), the coefficient of \(1/n\) is
\[
\frac{(m+1)-(\ell+1)-(m-\ell+1)}2=-\frac12.
\]
Consequently \(B_{m,\ell,n+1}/B_{m,\ell,n}=\Lambda_{m,\ell}(1-1/(2n)+O(n^{-2}))\). As \(F_{r,n}=B_{r+1,1,n}/(rn+1)\), its exact quotient introduces the further factor \((rn+1)/(r(n+1)+1)=1-1/n+O(n^{-2})\), so
\[
\frac{F_{r,n+1}}{F_{r,n}}
=\Lambda_r\bigl(1-3/(2n)+O(n^{-2})\bigr).
\]
Thus the one-step drifts in both families tend to \(-\infty\), because their terms grow at least geometrically by the limiting ratio \(\Lambda>1\). This proves the applications directly from finite factorial products. The standard two-term Stirling expansion also yields, for fixed \(r\ge1\),
\[
F_{r,n}=K_r\Lambda_r^n n^{-3/2}\bigl(1+O(n^{-1})\bigr),
\qquad
\Lambda_r=\frac{(r+1)^{r+1}}{r^r},\quad
K_r=\frac{\sqrt{r+1}}{\sqrt{2\pi}\,r^{3/2}}.
\]
The full Stirling series yields the required form with a specific \(c/n\) and an \(O(n^{-2})\) remainder. Likewise, for fixed \(m>\ell\ge1\),
\[
B_{m,\ell,n}=K_{m,\ell}\Lambda_{m,\ell}^n n^{-1/2}
\bigl(1+c_{m,\ell}/n+O(n^{-2})\bigr),
\]
where
\[
\Lambda_{m,\ell}=\frac{m^m}{\ell^\ell(m-\ell)^{m-\ell}},
\qquad
K_{m,\ell}=\sqrt{\frac{m}{2\pi\ell(m-\ell)}}.
\]
Strict increase of \(B_{m,\ell,n}\) follows by extending each \(\ell n\)-element subset of an \(mn\)-element set with a fixed \(\ell\)-subset of the \(m\) new elements; the embedding is not onto since \(m>\ell\). Strict increase of \(F_{r,n}\) follows from its full ordered \((r+1)\)-ary-tree interpretation: replace the leftmost leaf by a vertex with \(r+1\) leaf children. The resulting injection is not onto, since a tree with a leftmost child of the root that is a leaf and a second child containing all other internal vertices is omitted. Both exponential bases exceed one. The asymptotic test applies with \(\gamma=-3/2\) and \(\gamma=-1/2\), respectively.

For the two familiar families an entirely elementary local computation is also available:
\[
C_{n+1}-4C_n=-\frac{6C_n}{n+2},\qquad
\binom{2n+2}{n+1}-4\binom{2n}{n}
=-\frac2{n+1}\binom{2n}{n}.
\]
Both right sides tend to \(-\infty\): the consecutive-term ratios converge to four and eventually exceed three, so the numerators grow exponentially.

**Sharp boundary.** For any integers \(q\ge2\), \(d\ge0\), the set \(\{q^n+d:n\ge1\}\) admits the nonidentity self-map
\[
x\longmapsto qx+(1-q)d.
\]
Its limiting ratio is \(q\) but its drift is the bounded constant \((1-q)d\). Thus the ratio limit alone does not yield affine rigidity.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and exact integer or rational arithmetic. It checks the two elementary Catalan/binomial recurrences on 602 index instances, the negative one-step drifts for 900 Fuss–Catalan and 2304 general binomial parameter/index instances, and a 49,341-candidate finite affine screening for three sequence sets. These are consistency checks. The unbounded statement is proved by the iteration, bounded-shift and telescoping arguments above, not by numerical enumeration.

Run: `python3 verify.py`.

## Relationship to prior work

Shin-ichiro Seki, *Irreducibility of truncations of the Catalan generating function* (arXiv:2609.10526v1, initially public September 9, 2026), proves irreducibility of \(\sum_{k=0}^n C_k x^k\) over \(\mathbb Q\) for every positive integer \(n\). This motivates a different arithmetic rigidity question for the **set of coefficients** rather than the polynomials: which affine maps preserve all Catalan values? Irreducibility neither states nor implies this classification. The present theorem addresses the value-set endomorphism monoid, extends to Fuss–Catalan and binomial families, and isolates an elementary one-step drift criterion that applies beyond these sequences.

The OEIS entries A000108 (Catalan) and A000984 (central binomial) contain extensive value formulas and identities, but the examined descriptions did not supply an affine-endomorphism classification. The result is separate from divisibility, asymptotic enumeration, and coefficient-polynomial irreducibility.

## Limitations

This proof assumes a limiting consecutive ratio and an unbounded one-step drift of constant eventual sign; no converse classification is claimed. The theorem does not assert that every exponentially growing integer sequence is rigid, as the shifted geometric counterexample shows. The literature comparison relies on accessible abstracts and surveys for the September 2026 irreducibility preprint because its original PDF was not accessible. A prior equivalent affine-rigidity lemma in less directly indexed literature remains a historical-priority risk. No independent audit has been conducted.

## References

1. S. Seki, *Irreducibility of truncations of the Catalan generating function*, arXiv:2609.10526v1 (2026), https://arxiv.org/abs/2609.10526 .
2. M. Ramani, *Exact Computation of the Catalan Number C(2,050,572,903)*, arXiv:2601.11621 (2026), https://arxiv.org/abs/2601.11621 .
3. The On-Line Encyclopedia of Integer Sequences, A000108, https://oeis.org/A000108 .
4. The On-Line Encyclopedia of Integer Sequences, A000984, https://oeis.org/A000984 .

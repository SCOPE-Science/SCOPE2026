# Residue-tail geometry of near-diagonal two-generator semigroup quotients

## Finding

For integers \(a\ge2\) and \(k\ge1\) with \(\gcd(a,k)=1\), define the numerical semigroup
\[
Q_{a,k}=\{n\in\mathbb Z_{\ge0}:(a-1)n\in\langle a,a+k\rangle\}.
\]
For \(1\le t\le k\), set
\[
u_t=at-k\left\lfloor\frac{(a-1)t}{k+1}\right\rfloor.
\]
Then the \(k\) numbers \(u_t\) are strictly positive and represent all residue classes modulo \(k\), and the following *complete membership and gap classification* holds:
\[
Q_{a,k}=\{0\}\ \sqcup\ \bigsqcup_{t=1}^{k}
\{u_t+jk:j\in\mathbb Z_{\ge0}\}.
\]
In particular, the full gap set is the disjoint union
\[
\mathbb Z_{>0}\setminus Q_{a,k}
=\bigsqcup_{t=1}^{k}\{u_t-jk:j\ge1,\ u_t-jk\ge1\}.
\]
The Hilbert series, Frobenius number, and genus are consequently
\[
H_{Q_{a,k}}(z)=1+\frac{\sum_{t=1}^{k}z^{u_t}}{1-z^k},\qquad
F(Q_{a,k})=\max_{1\le t\le k}(u_t-k),\qquad
g(Q_{a,k})=\sum_{t=1}^{k}\left\lfloor\frac{u_t-1}{k}\right\rfloor.
\]
The representation determines the entire semigroup through \(k\) floor expressions, regardless of the size of \(a\).

For the first nontrivial difference \(k=2\), every admissible parameter \(a\ge3\) is odd. Set
\[
O=a-2\left\lfloor\frac{a-1}{3}\right\rfloor,\qquad
E=2a-2\left\lfloor\frac{2(a-1)}3\right\rfloor.
\]
Then \(O\) is odd, \(E\) is even, and \(E=2O\) unless \(a\equiv3\pmod6\), when \(E=2O-2\). The quotient has exactly the odd integers at least \(O\) and the positive even integers at least \(E\), together with zero. Its **complete minimal generating set** is
\[
\{O,O+2,\ldots,O+E-2\}\ \cup\
\{E,E+2,\ldots,2O-2\}.
\]
Thus its multiplicity and embedding dimension are both \(O\). In particular, this natural family of quotients of two-generated semigroups gives nonordinary numerical semigroups of **unbounded maximal embedding dimension**. Its Frobenius number is \(E-2\), and its genus is \((O-1)/2+E/2-1\).

## Assumptions and scope

The notation \(\langle r,s\rangle\) means \(\{rx+sy:x,y\in\mathbb Z_{\ge0}\}\). The numerical semigroup \(Q_{a,k}\) uses quotient divisor \(a-1\), not division of its generators. The coprimality hypothesis guarantees that \(\langle a,a+k\rangle\) is cofinite and that the classes \(at\pmod k\) for \(1\le t\le k\) are distinct. The gap set consists of *positive* excluded integers, genus is its cardinality, Frobenius number its maximum, and embedding dimension the number of minimal positive generators. The generating function is a formal power series in \(z\).

## Proof

**Representations.** A positive integer \(n\) belongs to \(Q_{a,k}\) exactly when there are nonnegative integers \(x,y\) with
\[
(a-1)n=ax+(a+k)y.
\]
Modulo \(a-1\), the right side is \(x+(k+1)y\). Consequently there is a unique positive integer \(t\) with \(x+(k+1)y=(a-1)t\); \(t=0\) forces \(x=y=0\). Substitution gives \(n=at-ky\), and conversely every
\[
0\le y\le\left\lfloor\frac{(a-1)t}{k+1}\right\rfloor
\]
produces a nonnegative representation. Thus for each \(t\ge1\), precisely the progression
\[
u_t,u_t+k,\ldots,at
\]
occurs. The first term is positive since
\[
u_t\ge at-\frac{k(a-1)t}{k+1}=\frac{(a+k)t}{k+1}>0.
\]

**No disconnected residue components.** For every \(t\ge1\), let \(B_t=\lfloor(a-1)t/(k+1)\rfloor\). Since \((t+k)/(k+1)\ge1\), we have \(B_{t+k}\ge a-1\), hence
\[
u_{t+k}=a(t+k)-kB_{t+k}\le at+k.
\]
Also \(B_{t+k}-B_t\le a-1\): the difference of the real arguments is \((a-1)k/(k+1)<a-1\), so their floors differ by at most \(a-1\). Therefore
\[
u_{t+k}-u_t=ak-k(B_{t+k}-B_t)\ge k.
\]
The progression for index \(t+k\) begins strictly after the first term for index \(t\), but at most one step past the old progression's last term. Iterating, the union of all progressions indexed by \(t,t+k,t+2k,\ldots\) is exactly the infinite progression \(u_t+k\mathbb Z_{\ge0}\). Finally \(\gcd(a,k)=1\) makes the \(k\) classes \(at\pmod k\), for \(1\le t\le k\), distinct and exhaustive. This proves the classification including its converse, with no unaccounted gaps.

**Invariants.** In the class of \(u_t\), exactly \(\lfloor(u_t-1)/k\rfloor\) positive integers precede \(u_t\), and the largest missing integer there, if any, is \(u_t-k\). Summing or taking the maximum over these disjoint classes gives the stated genus and Frobenius formulas. A geometric-series sum gives the Hilbert series.

**Maximal embedding dimension at difference two.** When \(k=2\), the two classes have respective odd and even first elements \(O\) and \(E\). Write \(a-1=3q+r\), \(0\le r\le2\). Then \(O=q+r+1\) and \(E=2O-2\lfloor2r/3\rfloor\), giving \(E=2O\) for \(r=0,1\) and \(E=2O-2\) for \(r=2\). Since \(a\) is odd, the latter case is exactly \(a\equiv3\pmod6\). We have \(O\ge3\) and \(O<E\le2O\). An odd member below \(O+E\) is indecomposable because the sum of two positive members with odd parity must include one odd and one even, whose minimum total is \(O+E\). Every odd member at least \(O+E\) decomposes as \(O\) plus a permitted even member. An even member below \(2O\) is indecomposable because the smallest sum of two positive members of even parity is \(2O\); every even member at least \(2O\) decomposes as \(O\) plus a permitted odd member. Therefore precisely the displayed odd and even intervals form the minimal generating set. Their total cardinality is \(E/2+(2O-E)/2=O\), while the smallest positive member is \(O\). This proves maximal embedding dimension and the remaining formulas. As \(a\to\infty\) over odd integers, \(O\to\infty\).

## Verification

The accompanying standalone `verify.py` independently tests the quotient membership via the least nonnegative solution of a two-coin congruence, rather than the threshold representation. It exhaustively checks every coprime parameter pair \(2\le a\le90\), \(1\le k\le50\), all integers through the asserted conductor plus an extra margin, and the exact genus and Frobenius identities. For \(k=2\) it independently enumerates minimal generators for all odd \(a\le90\). The execution output is `VERIFY_OK parameter_pairs=2721 checked_memberships=267879 maximal_embedding_examples=44 integer_exact=PASS finite_only=YES`. The proof above, not these finite checks, establishes the theorem for all admissible parameters.

## Relationship to prior work

Liu's 2026 investigation (arXiv:2607.23076) motivates exact Frobenius descriptions for semigroup quotients and studies fixed quotient divisors and specific arithmetic regions. The present result uses a *varying* divisor \(a-1\) tied to a generator and describes the full semigroup for every coprime parameter pair \((a,k)\), rather than a Frobenius formula for a particular parameter region. Cabanillas (arXiv:1904.08240) supplies general algorithms and invariants for all quotients of two-generated semigroups, so algorithmic computability and the general genus problem are **not** claimed new. The explicit two-parameter disjoint residue-tail geometry and its uniform maximal-embedding-dimension consequence were not identified in the inspected presentations. Adeniran and collaborators (arXiv:1809.09360) give general quotient genus formulas, which may also derive the genus formula by specialization, but do not present the same full residue-tail decomposition. Liu's separate 2026 work (arXiv:2604.26415) assumes the quotient divisor divides an original generator, which excludes the present divisor for \(a\ge3\).

## Limitations

This theorem is restricted to the linked parameters \(b=a+k\) and quotient divisor \(a-1\), with \(\gcd(a,k)=1\). It is neither a general closed formula for arbitrary two-generator quotients nor a claim that all such quotients have maximal embedding dimension. The prior general algorithms and genus formulas may allow the identities to be deduced through nontrivial specialization; a previously unindexed exact expression would affect priority. No independent audit has been carried out.

## References

1. F. Liu, *On the Frobenius Number of Quotients of Numerical Semigroups* (2026), arXiv:2607.23076, https://arxiv.org/abs/2607.23076.
2. E. Cabanillas, *Quotients of numerical semigroups generated by two numbers* (2019), arXiv:1904.08240, https://arxiv.org/abs/1904.08240.
3. A. Adeniran et al., *On the Genus of a Quotient of a Numerical Semigroup* (2018/2019), arXiv:1809.09360, https://arxiv.org/abs/1809.09360.
4. F. Liu, *The Frobenius problem for a class of quotients of numerical semigroups* (2026), arXiv:2604.26415, https://arxiv.org/abs/2604.26415.
